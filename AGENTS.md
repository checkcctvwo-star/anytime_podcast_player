# Anytime Podcast Player - Agent Guidelines

## Agent skills

### Issue tracker

GitHub issues tracked via `gh` CLI on `checkcctvwo-star/anytime_podcast_player`. See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context layout with root `CONTEXT.md` and `docs/adr/`. See `docs/agents/domain.md`.

## Build and CI Instructions

- **APK Compilation**: All release and debug APK builds MUST be performed in the cloud via GitHub Actions (`.github/workflows/build-apk.yml`). Do NOT attempt local gradle/flutter APK builds.
- **Testing**: Flutter unit tests can be run locally via `flutter test test/unit/`.
