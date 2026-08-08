// Copyright 2020 Ben Hills and the project contributors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'dart:io';

import 'package:anytime/entities/downloadable.dart';
import 'package:anytime/entities/episode.dart';
import 'package:anytime/repository/repository.dart';
import 'package:anytime/repository/sembast/sembast_repository.dart';
import 'package:anytime/services/audio/mp3_converter_service.dart';
import 'package:anytime/services/download/download_manager.dart';
import 'package:anytime/services/download/mobile_download_service.dart';
import 'package:anytime/services/notifications/notification_service.dart';
import 'package:anytime/services/podcast/mobile_podcast_service.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:path_provider_platform_interface/path_provider_platform_interface.dart';
import 'package:rxdart/rxdart.dart';

import '../mocks/mock_notification_service.dart';
import '../mocks/mock_path_provider.dart';
import '../mocks/mock_podcast_api.dart';
import '../mocks/mock_settings_service.dart';

class _NoOpRunner implements AudioConverterRunner {
  @override
  Future<bool> run(List<String> args) async => true;
}

/// Records calls to ensureMp3 so a test can assert whether conversion ran.
class _RecordingConverter extends Mp3ConverterService {
  final List<String> calls = [];

  _RecordingConverter() : super(_NoOpRunner());

  @override
  Future<String> ensureMp3(String sourcePath) async {
    calls.add(sourcePath);
    return sourcePath;
  }
}

class _FakeDownloadManager implements DownloadManager {
  /// Public so a test can push progress into the service through the manager.
  final BehaviorSubject<DownloadProgress> progress = BehaviorSubject<DownloadProgress>();

  @override
  Stream<DownloadProgress> get downloadProgress => progress;

  @override
  Future<String?> enqueueTask(String url, String downloadPath, String fileName) async => 'task1';

  @override
  void dispose() {}
}

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  PathProviderPlatform.instance = MockPathProvder();

  const dbName = 'anytime-download.db';
  final repository = SembastRepository(databaseName: dbName);
  final notificationService = MockNotificationService();
  final podcastService = MobilePodcastService(
    api: MockPodcastApi(),
    repository: repository,
    notificationService: notificationService,
    settingsService: MockSettingsService(),
  );
  final settings = MockSettingsService();
  final converter = _RecordingConverter();

  // A single service instance is reused across assertions because the static
  // downloadProgress subject can only be piped once.
  final manager = _FakeDownloadManager();
  final service = MobileDownloadService(
    repository: repository,
    downloadManager: manager,
    podcastService: podcastService,
    audioConverter: converter,
    settingsService: settings,
  );

  tearDown(() {
    final f = File('${Directory.systemTemp.path}/$dbName');
    if (f.existsSync()) f.deleteSync();
  });

  Future<void> readyEpisode(String taskId, String filename) async {
    await repository.saveEpisode(Episode(
      guid: 'EP_$taskId',
      podcast: 'Show',
      title: 'Episode',
      downloadTaskId: taskId,
      filepath: Directory.systemTemp.path,
      filename: filename,
    ));
    File('${Directory.systemTemp.path}/$filename').createSync();
  }

  test('MP3 conversion runs when convertToMp3 is enabled', () async {
    settings.convertToMp3 = true;
    await readyEpisode('task-on', 'episode.m4a');

    manager.progress.add(DownloadProgress('task-on', 100, DownloadState.downloaded));
    await Future<void>.delayed(const Duration(milliseconds: 100));

    expect(converter.calls, hasLength(1));
    expect(converter.calls.single, endsWith('episode.m4a'));
  });

  test('MP3 conversion is skipped when convertToMp3 is disabled', () async {
    settings.convertToMp3 = false;
    await readyEpisode('task-off', 'episode2.m4a');

    manager.progress.add(DownloadProgress('task-off', 100, DownloadState.downloaded));
    await Future<void>.delayed(const Duration(milliseconds: 100));

    expect(converter.calls, hasLength(1)); // only the previous 'task-on' call
  });

  tearDownAll(() {
    service.dispose();
  });
}