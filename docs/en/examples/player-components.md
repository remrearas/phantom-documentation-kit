---
extra_javascript:
  - assets/javascripts/asciinema-player.js
  - assets/javascripts/youtube-player.js
---
# Player Components

!!! important "Required Configuration"
    To use player components in your markdown files, you **must** include the following YAML front matter at the top of your document:
    ```yaml
    ---
    extra_javascript:
      - assets/javascripts/asciinema-player.js
      - assets/javascripts/youtube-player.js
    ---
    ```
    Without this configuration, players will not render properly.

## Asciinema Player

### Simple Embed

<div class="asciinema-player" data-cast-file="recordings/build_docker_remote.cast"></div>

**Note:** The player will load the terminal recording when the cast file is available.

### Full Container with Header

<div class="asciinema-player-container">
    <div class="asciinema-player-header">
        <h3>Phantom Setup Process</h3>
        <span class="asciinema-player-info">Installation Demo</span>
    </div>
    <div class="asciinema-player-wrapper">
        <div class="asciinema-player" 
             data-cast-file="recordings/build_docker_remote.cast"
             data-cols="120"
             data-rows="40"
             data-autoplay="false"
             data-loop="false"
             data-speed="1.5"
             data-theme="solarized-dark"
             data-font-size="small">
        </div>
    </div>
</div>

### Available Options

| Option           | Description       | Values                                               |
|------------------|-------------------|------------------------------------------------------|
| `data-cols`      | Terminal columns  | Default: 100                                         |
| `data-rows`      | Terminal rows     | Default: 30                                          |
| `data-autoplay`  | Auto-play on load | `true` / `false`                                     |
| `data-loop`      | Loop playback     | `true` / `false`                                     |
| `data-speed`     | Playback speed    | `0.5` - `3.0`                                        |
| `data-theme`     | Color theme       | `solarized-dark`, `solarized-light`, `monokai`, etc. |
| `data-font-size` | Font size         | `small`, `medium`, `large`                           |

## YouTube Player

### Simple Embed

<div class="youtube-player" data-video-id="eV6lTEY95yY"></div>

**Note:** Replace `VIDEO_ID_HERE` with your actual YouTube video ID.

### Full Container with Header

<div class="youtube-player-container">
    <div class="youtube-player-header">
        <h3>Phantom E2E Tutorial</h3>
        <span class="youtube-player-info">Getting Started Guide</span>
    </div>
    <div class="youtube-player-wrapper">
        <div class="youtube-player" 
             data-video-id="eV6lTEY95yY"
             data-autoplay="false"
             data-controls="true"
             data-loop="false"
             data-mute="false"
             data-rel="false"
             data-modestbranding="true">
        </div>
    </div>
</div>

### Available Options

| Option                | Description              | Values           |
|-----------------------|--------------------------|------------------|
| `data-video-id`       | YouTube video ID         | **Required**     |
| `data-autoplay`       | Auto-play video          | `true` / `false` |
| `data-controls`       | Show player controls     | `true` / `false` |
| `data-loop`           | Loop video               | `true` / `false` |
| `data-mute`           | Mute by default          | `true` / `false` |
| `data-rel`            | Show related videos      | `true` / `false` |
| `data-modestbranding` | Minimal YouTube branding | `true` / `false` |

## Loading States for Players

While players are loading, a spinner is displayed:

<div style="position: relative; height: 300px; background: var(--phantom-code-bg); border-radius: 8px; display: flex; align-items: center; justify-content: center;">
  <div class="player-spinner">
    <div class="spinner-inner"></div>
  </div>
</div>

**CSS Animation:**
The spinner automatically rotates using CSS animations. You can customize the size and color through CSS variables.

## Best Practices

1. **File Size**: Keep Asciinema recordings under 1MB for fast loading
2. **Idle Time**: Use `data-speed` to skip long pauses in recordings
3. **Themes**: Choose themes that match your documentation style
4. **Fallbacks**: Provide text alternatives for accessibility
5. **Hosting**: Host .cast files locally for better performance

## Recording Terminal Sessions

To create your own Asciinema recordings:

```bash
# Install asciinema
pip install asciinema

# Start recording
asciinema rec demo.cast

# Record with specific settings
asciinema rec -i 2 -t "Demo Title" demo.cast

# Play back locally
asciinema play demo.cast
```

## YouTube Integration Tips

1. **Privacy**: Use `data-rel="false"` to prevent showing unrelated videos
2. **Branding**: Use `data-modestbranding="true"` for cleaner appearance
3. **Autoplay**: Avoid autoplay for better user experience
4. **Muting**: Consider muting if autoplay is necessary
5. **Responsive**: Players automatically scale to container width