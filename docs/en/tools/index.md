# Introduction to Tools

Phantom Documentation Kit provides powerful tools to make your documentation projects more efficient and professional.


## :fontawesome-solid-cube: Vendor Builder

### What Does It Do?

**Phantom Vendor Builder** is a tool that automatically manages your JavaScript and CSS dependencies. 
It allows you to manage third-party libraries like Chart.js and Font Awesome from a single location.

### Key Features

- **:fontawesome-solid-rotate: Automatic Build**: Missing files are automatically compiled when `serve.py` and `build.py` run
- **:fontawesome-solid-box: NPM Integration**: Compatible with all npm packages
- **:fontawesome-solid-bolt: Smart Optimization**: Customizable optimization with Terser and cssnano
- **:fontawesome-solid-palette: Font Awesome Built-in**: Font Awesome is automatically included

### Configuration

```json
{
  "dependencies": [
    {
      "name": "Chart.js",
      "from": "node_modules/chart.js/dist/chart.umd.js",
      "to": "chart.umd.js",
      "type": "js",
      "minify": true
    }
  ]
}
```

### Automatically Processed Libraries

- **Font Awesome**: CSS and webfonts automatically included
- **Chart.js**: Charting library
- **Asciinema Player**: Terminal recording player
- **LoadJS**: Dynamic script loader

[:fontawesome-solid-book: Detailed Documentation →](./vendor-builder.md)

## :fontawesome-solid-image: Image Optimizer

### What Does It Do?

**Phantom Image Optimizer** is a powerful tool that automatically optimizes images used in your documentation. 
Leveraging the industrial strength of the Sharp library, it significantly reduces file sizes while preserving visual quality.

### Key Features

- **:fontawesome-solid-rocket: High Performance**: Fast optimization with parallel processing support
- **:fontawesome-solid-chart-line: Smart Compression**: Up to 70% size reduction while preserving visual quality
- **:fontawesome-solid-bullseye: Multiple Format Support**: JPEG, PNG, WebP, AVIF formats
- **:fontawesome-solid-gears: Flexible Configuration**: Customizable quality and size settings
- **:fontawesome-solid-flask: Test System**: Performance testing with Oxford Pet Dataset

### Use Cases

- Documentation screenshots
- Blog and article images
- Product photos
- Diagrams and infographics

[:fontawesome-solid-book: Detailed Documentation →](./image-optimizer.md)



