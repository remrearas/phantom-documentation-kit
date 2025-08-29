# Breadcrumb Navigation Demo

## Live Breadcrumb Demo

Below you can see how the breadcrumb navigation would appear at different nesting levels:

### Level 1 Navigation
<nav class="phantom-breadcrumbs" aria-label="Breadcrumb navigation">
  <div class="phantom-breadcrumbs-wrapper">
    <ol itemscope itemtype="https://schema.org/BreadcrumbList">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="../../" itemprop="item"><span itemprop="name">Home</span></a>
        <meta itemprop="position" content="1" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span class="active" itemprop="item"><span itemprop="name">Getting Started</span></span>
        <meta itemprop="position" content="2" />
      </li>
    </ol>
  </div>
</nav>

### Level 3 Navigation (Medium Path)
<nav class="phantom-breadcrumbs" aria-label="Breadcrumb navigation">
  <div class="phantom-breadcrumbs-wrapper">
    <ol itemscope itemtype="https://schema.org/BreadcrumbList">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="../../" itemprop="item"><span itemprop="name">Home</span></a>
        <meta itemprop="position" content="1" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Styling Examples</span></a>
        <meta itemprop="position" content="2" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Configuration</span></a>
        <meta itemprop="position" content="3" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span class="active" itemprop="item"><span itemprop="name">Advanced Settings</span></span>
        <meta itemprop="position" content="4" />
      </li>
    </ol>
  </div>
</nav>

### Level 5 Navigation (Long Path - Shows Scrolling)
<nav class="phantom-breadcrumbs" aria-label="Breadcrumb navigation">
  <div class="phantom-breadcrumbs-wrapper">
    <ol itemscope itemtype="https://schema.org/BreadcrumbList">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="../../" itemprop="item"><span itemprop="name">Home</span></a>
        <meta itemprop="position" content="1" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Styling Examples</span></a>
        <meta itemprop="position" content="2" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Getting Started Guide</span></a>
        <meta itemprop="position" content="3" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Configuration Management</span></a>
        <meta itemprop="position" content="4" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Advanced System Settings</span></a>
        <meta itemprop="position" content="5" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span class="active" itemprop="item"><span itemprop="name">Custom Component Configuration</span></span>
        <meta itemprop="position" content="6" />
      </li>
    </ol>
  </div>
</nav>

## Features Demonstrated

### Responsive Behavior
- **Desktop**: Full breadcrumb paths with hover effects and smooth animations
- **Tablet**: Slightly compressed breadcrumbs while maintaining readability
- **Mobile**: Compact breadcrumbs with horizontal scrolling when needed

### Visual Indicators
- **Gradient Indicators**: Shows when content is scrollable (try resizing your window)
- **Hover Effects**: Interactive link animations and underline effects
- **Text Truncation**: Long page titles are ellipsized when space is limited

### Accessibility Features
- **Schema.org**: Structured data for better SEO and machine readability
- **Keyboard Navigation**: Full keyboard accessibility support
- **Focus Management**: Clear focus indicators and logical tab order

## Technical Implementation

The breadcrumb system automatically:
- Scrolls to show the current page when navigation path is long
- Displays gradient indicators for scrollable content
- Truncates long page titles with ellipsis
- Maintains accessibility with proper ARIA labels and structured data
- Adapts to different screen sizes with responsive design

## Testing Instructions

1. **Resize Window**: Make your browser window narrow to see horizontal scrolling in action
2. **Hover Effects**: Try hovering over breadcrumb links to see interactive animations  
3. **Mobile View**: Use responsive design mode to test mobile behavior
4. **Accessibility**: Use tab navigation to test keyboard accessibility

The breadcrumb component is automatically generated and requires no manual configuration.