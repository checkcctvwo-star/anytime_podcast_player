# Anytime Podcast Player

A Flutter-based mobile podcast player that supports OPML import, audio streaming, background playback, and offline downloads.

## Language

**Podcast**:
A syndicated audio show subscription defined by an RSS feed, containing metadata and a sequence of episodes.
_Avoid_: Show, channel, series, album

**Episode**:
A single playable audio release belonging to a Podcast.
_Avoid_: Track, song, audio, item

**Download Root Directory**:
The base filesystem location selected by the user to store offline episode files.
_Avoid_: Save folder, storage path, download path

**Podcast Directory**:
A subdirectory directly under the Download Root Directory, titled after the Podcast's title, grouping all downloaded episodes of that podcast together.
_Avoid_: Artist folder, series folder, category directory

**Episode Audio File**:
The offline audio file (typically MP3) representing an Episode, saved within its respective Podcast Directory.
_Avoid_: Downloaded track, sound file, media file
