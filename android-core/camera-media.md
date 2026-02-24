[← Back to main index](../../README.md) | [← Back to folder](../README.md)

---

## 20. Camera & Media Integration

### CameraX Basics

> **TL;DR:** Initialize `ProcessCameraProvider` → build `Preview` + `ImageCapture` use cases → `bindToLifecycle()` to attach to fragment lifecycle. Always `unbindAll()` before rebinding.

`ProcessCameraProvider` · Lifecycle-aware binding · `Preview` + `ImageCapture` · Main thread executor

<details>
<summary>💻 Code Example</summary>

```kotlin
class CameraScreen : Fragment() {
    private lateinit var imageCapture: ImageCapture

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val future = ProcessCameraProvider.getInstance(requireContext())
        future.addListener({
            startCamera(future.result)
        }, ContextCompat.getMainExecutor(requireContext()))
    }

    private fun startCamera(provider: ProcessCameraProvider) {
        val preview = Preview.Builder().build().also {
            it.setSurfaceProvider(previewView.surfaceProvider)
        }
        imageCapture = ImageCapture.Builder().build()
        provider.bindToLifecycle(this, CameraSelector.DEFAULT_BACK_CAMERA, preview, imageCapture)
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### CameraX Architecture

**Use cases:** Preview, ImageCapture, ImageAnalysis, VideoCapture plugged into single `cameraProvider`.

**bindToLifecycle():** Ties use cases to fragment lifecycle. When fragment destroyed, camera releases automatically.

**What you write vs framework does:**
```
You: bindToLifecycle(this, selector, preview, imageCapture)
Framework:
  - Registers fragment lifecycle observer
  - Attaches camera thread lifecycle (separate from UI thread)
  - On fragment destroy: releases camera, stops preview thread
```

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "bindToLifecycle handles cleanup" | Fragment lifecycle observer + camera thread lifecycle observer. On destroy, both stop simultaneously (framework callback). |
| "Use cases are composable" | CameraX supports multiple use cases bound at once (e.g., Preview + ImageAnalysis). Resource conflict = exception. |
| "ProcessCameraProvider is async" | getInstance() returns ListenableFuture (non-blocking). Provider initialized on camera thread, not UI thread. |

### Gotchas at depth

- **Multiple fragments:** Each fragment gets separate camera instance if both bind independently. Sharing camera = Singleton anti-pattern. Better: bind to activity.
- **Permissions timing:** Even with permission granted, ProcessCameraProvider might fail if camera hardware unavailable or already in use.
- **Frame drops:** Too many use cases or slow analysis = frame drops. Profile with Perfetto's camera trace.

</details>

### Media3 (ExoPlayer) Basics

> **TL;DR:** Create `ExoPlayer` → set `MediaItem` (URL or local file) → `prepare()` → `play()`. Always `release()` in `onDestroyView`.

`ExoPlayer` · `MediaItem` · Lifecycle cleanup · Plays local + remote

<details>
<summary>💻 Code Example</summary>

```kotlin
class VideoScreen : Fragment() {
    private lateinit var player: ExoPlayer

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        player = ExoPlayer.Builder(requireContext()).build()
        playerView.player = player
        player.setMediaItem(MediaItem.fromUri("https://example.com/video.mp4"))
        player.prepare()
        player.play()
    }

    override fun onDestroyView() {
        super.onDestroyView()
        player.release()
    }
}
```

</details>

<details>
<summary>🔩 Under the Hood</summary>

### ExoPlayer State Machine

**State transitions:**
```
IDLE → BUFFERING → READY → ENDED
 ↑        ↓
 └────────┴─→ ERROR
```

**prepare():** Starts buffering. Async operation; `onPlayerStateChanged` callback fires when ready.

**release():** Stops all playback threads, releases decoder resources, closes connections. Critical for battery/memory.

### Media3 Architecture

- **Renderer:** Audio, video, text renderers (pluggable)
- **Extractor:** Demuxes container format (MP4, HLS, DASH)
- **Decoder:** Software decoder (fallback) or hardware decoder (preferred)

**Why Media3 over VideoView:**
- VideoView = simple wrapper; no control
- ExoPlayer = full control (speed, quality, buffering)

### User vs Understander

| A user knows | An understander also knows |
|---|---|
| "Always release() in onDestroyView" | ExoPlayer spawns decoder thread + network thread. release() stops threads, frees codec. If not released, threads live until GC (memory leak). |
| "setMediaItem before prepare()" | ExoPlayer parses URL/file in background thread. prepare() starts buffering. If you set item post-prepare, buffering restarts. |
| "PlayerView handles UI" | PlayerView = wrapper around ExoPlayer. Renders player controls, player state callbacks. Alternative: Custom surface render + manual UI. |

### Gotchas at depth

- **Pause vs pause on resume:** ExoPlayer pauses when app goes background (lifecycle pause), then auto-resumes when resumed (configurable). Can interfere with user expectations.
- **Bandwidth throttling:** ExoPlayer adapts bitrate (for HLS/DASH). On slow network, automatically switches to lower quality. Can surprise users.
- **Codec compatibility:** Not all devices support all codecs. Fallback to software decoder (CPU cost). Check supported codecs before playback.

</details>

---

