---
extra_javascript:
  - assets/javascripts/phantom-ascii.js
  - assets/javascripts/animated-ascii-art.js
extra_css:
  - assets/stylesheets/ascii-styles.css
  - assets/stylesheets/animated-ascii-art.css
---

# Animated ASCII Art

## Live Demo

<div class="ascii-demo-container">
  <div id="pulse-error-alert" class="phantom-alert error" style="display: none; margin-bottom: 1rem;">
    <i class="fas fa-times-circle"></i>
    <strong>Error:</strong> <span id="pulse-error-message"></span>
  </div>
  <pre id="phantom-ascii-pulse" class="ascii-art" data-effect="pulse"></pre>
  <div class="phantom-grid phantom-grid-auto phantom-grid-gap-sm" style="margin-top: 1rem;">
    <button id="pulse-toggle-btn" class="md-button md-button--primary">
      <i class="fas fa-play"></i> Play
    </button>
  </div>
</div>


### Test Error State

<div class="ascii-demo-container">
  <div id="test-error-alert" class="phantom-alert error" style="display: none; margin-bottom: 1rem;">
    <i class="fas fa-times-circle"></i>
    <strong>Error:</strong> <span id="test-error-message"></span>
  </div>
  <pre id="phantom-ascii-test" class="ascii-art"></pre>
  <div class="phantom-grid phantom-grid-auto phantom-grid-gap-sm" style="margin-top: 1rem;">
    <button id="test-error-btn" class="md-button md-button--primary">Test Error</button>
    <button id="clear-error-btn" class="md-button md-button--primary">Clear Error</button>
  </div>
</div>


## Speed Control Example

This example demonstrates how to dynamically control the animation speed using the `setSpeed()` method.

<div class="ascii-demo-container">
  <pre id="phantom-ascii-speed" class="ascii-art"></pre>
  <div class="speed-control-wrapper">
    <label for="speed-slider" class="speed-label">Animation Speed: <span id="speed-value">500</span>ms</label>
    <input 
      type="range" 
      id="speed-slider" 
      class="speed-slider"
      min="100" 
      max="2000" 
      value="500" 
      step="50"
    >

  </div>
  <div class="phantom-grid phantom-grid-auto phantom-grid-gap-sm" style="margin-top: 1rem;">
    <button id="speed-toggle-btn" class="md-button md-button--primary">
      <i class="fas fa-play"></i> Play
    </button>
  </div>
</div>

## Browser Compatibility

- Chrome/Edge: Full support
- Firefox: Full support
- Safari: Full support
- Mobile browsers: Optimized for performance