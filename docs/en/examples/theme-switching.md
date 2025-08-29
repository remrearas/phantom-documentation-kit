# Theme Switching

Our theme system, which components depend on and is adapted on top of MkDocs Material style, supports both light and dark themes. 
All components automatically adapt to the selected theme using CSS variables.

## CSS Variables

Our theming system is built on CSS custom properties (variables) that automatically update when switching themes.

### Core Variables

```css
:root {
  /* Background colors */
  --md-default-bg-color: #ffffff; /* Background color */
  --md-default-fg-color: #000000; /* Foreground/text color */

  /* Accent colors */
  --md-primary-fg-color: #1976d2; /* Primary accent color */
  --md-accent-fg-color: #ff6b35; /* Secondary accent color */

  /* Custom variables */
  --phantom-bg-secondary: #f5f5f5; /* Secondary background */
  --phantom-border: #e0e0e0; /* Border color */
  --phantom-accent: #1976d2; /* Accent color */
  --phantom-text-secondary: #666666; /* Secondary text color */
}
```

## Visual Examples

<div class="phantom-grid phantom-grid-2">
  <div style="padding: 1rem; background: var(--md-default-bg-color); border: 2px solid var(--phantom-border); border-radius: 8px;">
    <strong>Default Background</strong><br>
    <code>--md-default-bg-color</code>
  </div>
  <div style="padding: 1rem; background: var(--phantom-bg-secondary); border: 2px solid var(--phantom-border); border-radius: 8px;">
    <strong>Secondary Background</strong><br>
    <code>--phantom-bg-secondary</code>
  </div>
  <div style="padding: 1rem; color: var(--md-primary-fg-color); border: 2px solid var(--md-primary-fg-color); border-radius: 8px;">
    <strong>Primary Color</strong><br>
    <code>--md-primary-fg-color</code>
  </div>
  <div style="padding: 1rem; color: var(--phantom-accent); border: 2px solid var(--phantom-accent); border-radius: 8px;">
    <strong>Accent Color</strong><br>
    <code>--phantom-accent</code>
  </div>
</div>

## Theme-Aware Components

All our custom components automatically adapt to the current theme:

### Light Mode Example
<div class="phantom-test-status-grid" style="margin-bottom: 20px;">
  <div class="phantom-test-status-card success">
    <div class="phantom-test-status-value">✓</div>
    <div class="phantom-test-status-label">Light Mode</div>
  </div>
</div>

### How It Works

1. **Base Variables**: MkDocs Material provides base theme variables
2. **Custom Variables**: We extend these with our own `--phantom-*` variables, adapting our own styling approach
3. **Automatic Switching**: Variables update when theme changes

Try switching between light and dark mode using the theme toggle in the header to see how all components adapt!

## Color Palette

### Primary Colors
<div class="phantom-grid phantom-grid-auto">
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: var(--md-primary-fg-color); border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Primary</strong><br>
    <code style="font-size: 0.875em;">--md-primary-fg-color</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: var(--md-accent-fg-color); border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Accent</strong><br>
    <code style="font-size: 0.875em;">--md-accent-fg-color</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: var(--phantom-accent); border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Phantom Accent</strong><br>
    <code style="font-size: 0.875em;">--phantom-accent</code>
  </div>
</div>

### Status Colors
<div class="phantom-grid phantom-grid-auto">
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: #22c55e; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Success</strong><br>
    <code style="font-size: 0.875em;">#22c55e</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: #f59e0b; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Warning</strong><br>
    <code style="font-size: 0.875em;">#f59e0b</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: #ef4444; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Error</strong><br>
    <code style="font-size: 0.875em;">#ef4444</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: #3b82f6; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Info</strong><br>
    <code style="font-size: 0.875em;">#3b82f6</code>
  </div>
</div>

## Creating Theme-Aware Components

### Example: Custom Card

```css
.custom-card {
  background: var(--phantom-bg-secondary);
  border: 1px solid var(--phantom-border);
  color: var(--md-default-fg-color);
  padding: 1rem;
  border-radius: 8px;
}

.custom-card:hover {
  border-color: var(--phantom-accent);
}
```

<div class="custom-card" style="background: var(--phantom-bg-secondary); border: 1px solid var(--phantom-border); color: var(--md-default-fg-color); padding: 1rem; border-radius: 8px;">
  This card automatically adapts to the current theme using CSS variables.
</div>

## Dark Mode Considerations

When designing for both themes, consider:

1. **Contrast Ratios**: Ensure text remains readable in both modes
2. **Color Meanings**: Status colors should be distinguishable in both themes
3. **Shadows**: Use `box-shadow` sparingly as it may not work well in dark mode
4. **Images**: Consider providing theme-specific images when necessary

## Testing Your Theme

### Contrast Checker
<div class="phantom-grid phantom-grid-2">
  <div style="background: var(--md-default-bg-color); color: var(--md-default-fg-color); padding: 20px; border: 2px solid var(--phantom-border); border-radius: 8px;">
    <strong>Default Text on Default Background</strong><br>
    This text should be clearly readable in both light and dark modes.
  </div>
  <div style="background: var(--phantom-bg-secondary); color: var(--phantom-text-secondary); padding: 20px; border: 2px solid var(--phantom-border); border-radius: 8px;">
    <strong>Secondary Text on Secondary Background</strong><br>
    This combination is used for less prominent content.
  </div>
</div>

## Theme Toggle Location

The theme toggle button is located in the header navigation bar. Look for the sun/moon icon to switch between light and dark modes.

## Best Practices

1. **Use CSS Variables**: Always use theme variables instead of hard-coded colors
2. **Test Both Modes**: Check your content in both light and dark themes
3. **Semantic Colors**: Use meaningful variable names that describe purpose, not appearance
4. **Fallback Values**: Provide fallback colors for older browsers if needed
5. **Media Queries**: Respect user's system theme preference with `prefers-color-scheme`