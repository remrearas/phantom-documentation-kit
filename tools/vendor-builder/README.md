# Phantom Vendor Builder

JavaScript and CSS dependency manager for Phantom Documentation Kit. This tool automates the process of collecting, optimizing, and organizing third-party assets for documentation projects.

## Features

- Automatic dependency collection from npm packages
- JavaScript minification with Terser
- CSS optimization with PostCSS and cssnano
- Font file handling with path corrections
- Integration with Python build system

## Installation

```bash
cd tools/vendor-builder
npm install
```

## Usage

### Automatic Build

The vendor builder is automatically triggered by the main build system:

```bash
# From project root
python serve.py  # Checks and builds vendor files if needed
python build.py  # Includes vendor check in build process
```

### Manual Build

```bash
# From vendor-builder directory
npm run build

# Clean vendor files
npm run clean
```

## Configuration

### dependencies.json

Define your vendor dependencies in `dependencies.json`:

```json
{
  "dependencies": [
    {
      "name": "Chart.js",
      "package": "chart.js",
      "from": "node_modules/chart.js/dist/chart.umd.js",
      "to": "chart.umd.js",
      "type": "js",
      "minify": true
    },
    {
      "name": "Font Awesome CSS",
      "package": "@fortawesome/fontawesome-free",
      "from": "node_modules/@fortawesome/fontawesome-free/css/all.min.css",
      "to": "fontawesome-all.min.css",
      "type": "css",
      "minify": false
    }
  ]
}
```

### Dependency Properties

- `name`: Human-readable name for logging
- `package`: npm package name (for reference)
- `from`: Source file path relative to vendor-builder
- `to`: Target filename in vendor directory
- `type`: File type (`js` or `css`)
- `minify`: Whether to apply optimization

## How It Works

### Build Process

1. **Python Integration**: `serve.py` or `build.py` calls `VendorManager`
2. **Dependency Check**: System verifies if vendor files exist
3. **Build Trigger**: If files are missing, runs `npm run build`
4. **File Processing**: For each dependency:
   - Reads source file from `node_modules`
   - Applies minification (if configured)
   - Copies to `vendor` directory
   - Fixes paths (e.g., Font Awesome fonts)

### Directory Structure

```
vendor-builder/
├── build.js              # Main build script
├── dependencies.json     # Dependency configuration
├── package.json         # npm configuration
└── node_modules/        # npm packages (git-ignored)

Output:
overrides/assets/vendor/  # Built vendor files
├── chart.umd.min.js
├── fontawesome-all.min.css
└── webfonts/            # Font files
```

## Optimization Settings

### JavaScript (Terser)

- Removes debugger statements
- Preserves console.log for debugging
- Safari 10 compatibility
- Removes all comments

### CSS (cssnano)

- Removes all comments
- Normalizes whitespace
- Optimizes colors
- Minifies font values
- Optimizes gradients

## Adding New Dependencies

- Install the npm package:
```bash
cd tools/vendor-builder
npm install package-name
```

- Add to `dependencies.json`:
```json
{
  "name": "Package Name",
  "package": "package-name",
  "from": "node_modules/package-name/dist/file.js",
  "to": "package.min.js",
  "type": "js",
  "minify": true
}
```

- Run build:
```bash
npm run build
```

## Integration Points

- **serve.py**: Checks vendor files on startup
- **build.py**: Includes vendor check in build process
- **config.json**: Defines vendor directory paths
- **Docker**: Excludes node_modules from volume mounts

## Notes

- Files already containing `.min.` are not re-minified
- Font Awesome fonts are automatically copied to `webfonts/`
- CSS font paths are automatically corrected
- Build fails if any dependency is missing
- Node.js is required for building vendor files