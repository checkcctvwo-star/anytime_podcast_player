// DO NOT EDIT. This is code generated via package:intl/generate_localized.dart
// This is a library that looks up messages for specific locales by
// delegating to the appropriate library.
// @dart=2.12
// Ignore issues from commonly used lints in this file.
// ignore_for_file:implementation_imports, file_names
// ignore_for_file:unnecessary_brace_in_string_interps, directives_ordering
// ignore_for_file:argument_type_not_assignable, invalid_assignment
// ignore_for_file:prefer_single_quotes, prefer_generic_function_type_aliases
// ignore_for_file:comment_references

import 'package:intl/intl.dart';
import 'package:intl/message_lookup_by_library.dart';
import 'package:intl/src/intl_helpers.dart';

import 'messages_en.dart' deferred as messages_en;
import 'messages_es.dart' deferred as messages_es;
import 'messages_de.dart' deferred as messages_de;
import 'messages_gl.dart' deferred as messages_gl;
import 'messages_it.dart' deferred as messages_it;
import 'messages_nl.dart' deferred as messages_nl;
import 'messages_ru.dart' deferred as messages_ru;
import 'messages_tr.dart' deferred as messages_tr;
import 'messages_vi.dart' deferred as messages_vi;
import 'messages_zh_Hans.dart' deferred as messages_zh_hans;

typedef Future<dynamic> LibraryLoader();
Map<String, LibraryLoader> _deferredLibraries = {
  'en': messages_en.loadLibrary,
  'es': messages_es.loadLibrary,
  'de': messages_de.loadLibrary,
  'gl': messages_gl.loadLibrary,
  'it': messages_it.loadLibrary,
  'nl': messages_nl.loadLibrary,
  'ru': messages_ru.loadLibrary,
  'tr': messages_tr.loadLibrary,
  'vi': messages_vi.loadLibrary,
  'zh_Hans': messages_zh_hans.loadLibrary,
};

MessageLookupByLibrary? _findExact(String localeName) {
  switch (localeName) {
    case 'en':
      return messages_en.messages;
    case 'es':
      return messages_es.messages;
    case 'de':
      return messages_de.messages;
    case 'gl':
      return messages_gl.messages;
    case 'it':
      return messages_it.messages;
    case 'nl':
      return messages_nl.messages;
    case 'ru':
      return messages_ru.messages;
    case 'tr':
      return messages_tr.messages;
    case 'vi':
      return messages_vi.messages;
    case 'zh_Hans':
      return messages_zh_hans.messages;
    default:
      return null;
  }
}

/// User programs should call this before using [localeName] for messages.
Future<bool> initializeMessages(String? localeName) async {
  var availableLocale = Intl.verifiedLocale(
    localeName,
    (locale) => _deferredLibraries[locale] != null,
    onFailure: (_) => null);
  if (availableLocale == null) {
    return Future.value(false);
  }
  var lib = _deferredLibraries[availableLocale];
  await (lib == null ? Future.value(false) : lib());
  initializeInternalMessageLookup(() => CompositeMessageLookup());
  messageLookup.addLocale(availableLocale, _findGeneratedMessagesFor);
  return Future.value(true);
}

bool _messagesExistFor(String locale) {
  try {
    return _findExact(locale) != null;
  } catch (e) {
    return false;
  }
}

MessageLookupByLibrary? _findGeneratedMessagesFor(String locale) {
  var actualLocale = Intl.verifiedLocale(locale, _messagesExistFor,
      onFailure: (_) => null);
  if (actualLocale == null) return null;
  return _findExact(actualLocale);
}
