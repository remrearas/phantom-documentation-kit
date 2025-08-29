---
extra_javascript:
  - assets/javascripts/phantom-image.js
---

# Image (Visual Content) Components

Phantom Image (Visual Content) Components provide a powerful, flexible and unique way to display images in your documentation with features like lazy-loading, lightbox support and responsive layouts.

!!! info "Component Features"
    - **Lazy Loading**: Images load only when entering viewport
    - **Lightbox Support**: Full-screen image viewing
    - **Responsive Design**: Adapts to different screen sizes
    - **Flexible Positioning**: Float left, right, or center
    - **Grid Layouts**: Display multiple images efficiently

!!! tip "Image Path Resolution"
    Images are automatically resolved from the `/assets/static/images/` directory. Simply use the filename:
    
    - `data-src="example.png"` → `/assets/static/images/example.png`
    - For absolute paths, start with `/`: `data-src="/custom/path/image.png"`
    - For external images, use full URLs: `data-src="https://example.com/image.png"`

## Basic Usage

### Simple Image

The most basic usage - just provide the image source:

<div class="phantom-image-container" 
     data-src="phantom-logo.jpg"
     data-alt="Phantom Documentation Kit Logo">
</div>

### Image with Caption

Add context to your images with captions:

<div class="phantom-image-container" 
     data-src="example-2.jpg"
     data-alt="Image with caption example"
     data-caption="This is an example image with a descriptive caption">
</div>

## Size Variants

Control the display size of your images:

### Small Image

<div class="phantom-image-container" 
     data-src="phantom-logo.jpg"
     data-alt="Small size example"
     data-size="small"
     data-caption="Small size (max-width: 300px)">
</div>

### Medium Image (Default)

<div class="phantom-image-container" 
     data-src="example-2.jpg"
     data-alt="Medium size example"
     data-size="medium"
     data-caption="Medium size (max-width: 600px)">
</div>

### Large Image

<div class="phantom-image-container" 
     data-src="example-3.jpg"
     data-alt="Large size example"
     data-size="large"
     data-caption="Large size (max-width: 900px)">
</div>

### Full Width Image

<div class="phantom-image-container" 
     data-src="og-image.jpg"
     data-alt="Full width example"
     data-size="full"
     data-caption="Full width image">
</div>

## Positioning with Text

Images can be positioned to flow with your text content:

### Left-Aligned Image

<div class="phantom-image-container" 
     data-src="phantom-logo.jpg"
     data-alt="Left-aligned image"
     data-size="small"
     data-position="left">
</div>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

<div class="phantom-clear"></div>

### Right-Aligned Image

<div class="phantom-image-container" 
     data-src="phantom-logo.jpg"
     data-alt="Right-aligned image"
     data-size="small"
     data-position="right"
     data-caption="Floating right">
</div>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<div class="phantom-clear"></div>

## Lightbox Feature

Click on images with lightbox enabled to view them in full screen:

<div class="phantom-image-container" 
     data-src="og-image.jpg"
     data-alt="Lightbox example"
     data-caption="Click image to open in lightbox"
     data-size="medium"
     data-lightbox="true">
</div>

## Image Grid

Display multiple images in a responsive grid layout:

<div class="phantom-image-grid">
  <div class="phantom-image-container" 
       data-src="example-1.jpg"
       data-alt="Grid image 1"
       data-caption="First image"
       data-lightbox="true">
  </div>
  <div class="phantom-image-container" 
       data-src="example-2.jpg"
       data-alt="Grid image 2"
       data-caption="Second image"
       data-lightbox="true">
  </div>
  <div class="phantom-image-container" 
       data-src="example-3.jpg"
       data-alt="Grid image 3"
       data-caption="Third image"
       data-lightbox="true">
  </div>
  <div class="phantom-image-container" 
       data-src="og-image.jpg"
       data-alt="Grid image 4"
       data-caption="Fourth image"
       data-lightbox="true">
  </div>
</div>

## Image Comparison

Compare two images side by side:

<div class="phantom-image-comparison">
  <div class="phantom-image-container" 
       data-src="phantom-logo.jpg"
       data-alt="Before state"
       data-caption="Before optimization">
  </div>
  <div class="phantom-image-container" 
       data-src="og-image.jpg"
       data-alt="After state"
       data-caption="After optimization">
  </div>
</div>

## Advanced Usage

### Tutorial with Images

<div class="phantom-tutorial-step">
  <h3>Step 1: Open Settings</h3>
  <div class="phantom-image-container" 
       data-src="example-1.jpg"
       data-alt="Settings screen"
       data-size="small"
       data-position="right">
  </div>
  <p>First, navigate to the settings page by clicking the gear icon in the top right corner. The settings page contains all configuration options for your application.</p>
  <p>You'll find various sections including general settings, appearance, and advanced options.</p>
</div>

<div class="phantom-clear"></div>

<div class="phantom-tutorial-step">
  <h3>Step 2: Configure Options</h3>
  <div class="phantom-image-container" 
       data-src="example-2.jpg"
       data-alt="Configuration panel"
       data-size="small"
       data-position="left">
  </div>
  <p>In the configuration panel, you can adjust various settings according to your needs. Each option has a tooltip that explains its function.</p>
  <p>Make sure to save your changes before leaving the page.</p>
</div>

<div class="phantom-clear"></div>

### Feature Showcase

<div class="phantom-feature-showcase">
  <div class="phantom-image-container" 
       data-src="phantom-logo.jpg"
       data-alt="Feature icon"
       data-size="small">
  </div>
  <div class="feature-content">
    <h3>Advanced Image Processing</h3>
    <p>Our image component provides state-of-the-art features for displaying images in documentation:</p>
    <ul>
      <li>Automatic lazy loading for performance</li>
      <li>Responsive sizing and positioning</li>
      <li>Built-in lightbox functionality</li>
    </ul>
  </div>
</div>

## Configuration Options

### Data Attributes

| Attribute       | Type    | Default  | Description                              |
|-----------------|---------|----------|------------------------------------------|
| `data-src`      | string  | required | Image source URL                         |
| `data-alt`      | string  | ""       | Alternative text for accessibility       |
| `data-caption`  | string  | null     | Caption text below image                 |
| `data-size`     | string  | "medium" | Size variant: small, medium, large, full |
| `data-position` | string  | "center" | Position: left, right, center            |
| `data-loading`  | string  | "lazy"   | Loading strategy: lazy, eager            |
| `data-lightbox` | boolean | false    | Enable lightbox on click                 |

## Error States

### Failed Image Load

When an image fails to load, the component displays a clear error message:

<div class="phantom-image-container" 
     data-src="non-existent-image.jpg"
     data-alt="Failed load example"
     data-caption="This caption won't appear when image fails">
</div>

### Loading State

While images are loading, a spinner is displayed. Here's an example with a larger image that demonstrates the loading state:

<div class="phantom-image-container" 
     data-src="https://picsum.photos/1920/1080?random=1"
     data-alt="Large image demonstrating loading state"
     data-caption="This large image shows the loading spinner while downloading"
     data-size="large">
</div>

## Best Practices

1. **Always provide alt text**: Essential for accessibility and SEO
2. **Use appropriate sizes**: Choose the right size variant for your content
3. **Enable lightbox for detailed images**: Let users see full resolution when needed
4. **Add captions for context**: Help users understand what they're looking at
5. **Optimize your images**: Use appropriate formats and compression
6. **Consider mobile users**: Test how images appear on smaller screens

## Troubleshooting

### Image Not Loading

- Check that `data-src` points to a valid image URL
- Ensure the image file exists and is accessible
- Check browser console for error messages
- For local images, verify they're in `/docs/assets/static/images/`

### Lightbox Not Working

- Verify `data-lightbox="true"` is set
- Check that JavaScript is enabled
- Ensure `phantom-image.js` is loaded
- Confirm the image loaded successfully (lightbox is disabled for failed images)

### Layout Issues

- Check that parent containers have appropriate width
- Test responsive behavior on different screen sizes
- Test responsive behavior at different screen sizes