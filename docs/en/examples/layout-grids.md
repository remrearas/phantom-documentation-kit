# Grid Layouts

Grid layouts help organize content in responsive columns. They automatically adapt to different screen sizes.

## Two Column Layout

<div class="phantom-grid phantom-grid-2">
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Left Column</span>
    </div>
    <div class="phantom-module-card-description">
      Content in the left column of a two-column grid layout.
    </div>
  </div>
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Right Column</span>
    </div>
    <div class="phantom-module-card-description">
      Content in the right column of a two-column grid layout.
    </div>
  </div>
</div>

## Three Column Layout

<div class="phantom-grid phantom-grid-3">
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">1</div>
    <div class="phantom-test-status-label">Column One</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">2</div>
    <div class="phantom-test-status-label">Column Two</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">3</div>
    <div class="phantom-test-status-label">Column Three</div>
  </div>
</div>

## Four Column Layout

<div class="phantom-grid phantom-grid-4">
  <div class="phantom-test-status-card success">
    <div class="phantom-test-status-value">A</div>
    <div class="phantom-test-status-label">First</div>
  </div>
  <div class="phantom-test-status-card warning">
    <div class="phantom-test-status-value">B</div>
    <div class="phantom-test-status-label">Second</div>
  </div>
  <div class="phantom-test-status-card error">
    <div class="phantom-test-status-value">C</div>
    <div class="phantom-test-status-label">Third</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">D</div>
    <div class="phantom-test-status-label">Fourth</div>
  </div>
</div>

## Asymmetric Grid Layouts

### 2/3 + 1/3 Split

<div class="phantom-grid phantom-grid-2-1">
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Main Content (2/3)</span>
    </div>
    <div class="phantom-module-card-description">
      This column takes up two-thirds of the available space. Perfect for main content areas.
    </div>
  </div>
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Sidebar (1/3)</span>
    </div>
    <div class="phantom-module-card-description">
      This column takes up one-third of the space.
    </div>
  </div>
</div>

### 1/4 + 3/4 Split

<div class="phantom-grid phantom-grid-1-3">
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Nav</span>
    </div>
    <div class="phantom-module-card-description">
      Narrow column for navigation
    </div>
  </div>
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Content Area</span>
    </div>
    <div class="phantom-module-card-description">
      Wide column for main content display with plenty of room for detailed information.
    </div>
  </div>
</div>

## Responsive Grid

This grid automatically adjusts from 4 columns on desktop to 2 on tablet to 1 on mobile:

<div class="phantom-grid phantom-grid-auto">
  <div class="phantom-test-status-card success">
    <div class="phantom-test-status-value">
      <i class="fas fa-check-circle"></i>
      4
    </div>
    <div class="phantom-test-status-label">Responsive</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">
      <i class="fas fa-info-circle"></i>
      2
    </div>
    <div class="phantom-test-status-label">Flexible</div>
  </div>
  <div class="phantom-test-status-card warning">
    <div class="phantom-test-status-value">
      <i class="fas fa-exclamation-triangle"></i>
      1
    </div>
    <div class="phantom-test-status-label">Adaptive</div>
  </div>
  <div class="phantom-test-status-card error">
    <div class="phantom-test-status-value">
      <i class="fas fa-times-circle"></i>
      0
    </div>
    <div class="phantom-test-status-label">Dynamic</div>
  </div>
</div>

## Nested Grids

<div class="phantom-grid phantom-grid-2">
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Parent Grid - Left</span>
    </div>
    <div class="phantom-module-card-description">
      <div class="phantom-grid phantom-grid-2 phantom-grid-nested phantom-grid-gap-sm">
        <div class="phantom-grid-item">Nested 1</div>
        <div class="phantom-grid-item">Nested 2</div>
      </div>
    </div>
  </div>
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Parent Grid - Right</span>
    </div>
    <div class="phantom-module-card-description">
      <div class="phantom-grid phantom-grid-nested phantom-grid-gap-sm">
        <div class="phantom-grid-item">Full Width Nested</div>
        <div class="phantom-grid-item">Full Width Nested</div>
      </div>
    </div>
  </div>
</div>

## Grid with Gap Variations

### Small Gap (10px)
<div class="phantom-grid phantom-grid-3 phantom-grid-gap-sm">
  <div class="phantom-grid-item">Small</div>
  <div class="phantom-grid-item">Gap</div>
  <div class="phantom-grid-item">Grid</div>
</div>

### Medium Gap (20px)
<div class="phantom-grid phantom-grid-3 phantom-grid-gap-md">
  <div class="phantom-grid-item">Medium</div>
  <div class="phantom-grid-item">Gap</div>
  <div class="phantom-grid-item">Grid</div>
</div>

### Large Gap (30px)
<div class="phantom-grid phantom-grid-3 phantom-grid-gap-lg">
  <div class="phantom-grid-item">Large</div>
  <div class="phantom-grid-item">Gap</div>
  <div class="phantom-grid-item">Grid</div>
</div>

## Best Practices

1. **Responsive Design**: Use `phantom-grid-auto` class for automatic responsive grids
2. **Gap Sizing**: Use gap variation classes (`phantom-grid-gap-sm`, `phantom-grid-gap-md`, `phantom-grid-gap-lg`) for consistent spacing