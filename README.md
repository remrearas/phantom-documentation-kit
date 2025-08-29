# 👻 Phantom Documentation Kit

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Node.js](https://img.shields.io/badge/Node.js-22%2B-green?logo=node.js&logoColor=white)](https://nodejs.org/)
[![MkDocs Material](https://img.shields.io/badge/MkDocs-Material-purple?logo=material-design&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**🌟 A modern, space-tech themed documentation framework built on MkDocs Material**

Originally developed for Phantom-WireGuard documentation needs, now available as an open-source toolkit.

[Live Demo](https://phantom-documentation-kit.pages.dev/)

---
## 🚀 Quick Start

### Prerequisites

```bash
# Install Python dependencies
pip install -r requirements.txt

# Node.js 22+ required
node --version  # Should be v22.0.0 or higher
```

### 🏃 Development Server

```bash
python serve.py
# Open http://localhost:8000
```

### 📦 Production Build

```bash
python build.py
# Output: outputs/site/
```

### 🐳 Docker Mode

```bash
# Local Docker
python serve.py --docker
python build.py --docker
```

---

## 📁 Project Structure

```
phantom-documentation-kit/
├── 📄 mkdocs.yml              # MkDocs configuration
├── 📄 config.json             # Project settings
├── 🐍 serve.py                # Development server
├── 🐍 build.py                # Production builder
├── 📁 docs/                   # Documentation source
│   ├── 🌍 en/                 # English docs
│   ├── 🇹🇷 tr/                 # Turkish docs
│   └── 📁 assets/             # Static assets
├── 📁 overrides/              # Theme customization
│   ├── 📄 main.html           # Custom HTML template
│   └── 📁 assets/             
│       ├── 🎨 stylesheets/    # Custom CSS
│       ├── 📜 javascripts/    # Custom JS
│       └── 🔤 fonts/          # Custom fonts
├── 📁 tools/                  # Development tools
│   ├── 🖼️ image-optimizer/    # Sharp-based optimizer
│   └── 📦 vendor-builder/     # Dependency bundler
└── 📁 lib/                    # Core Python modules
    ├── 🐳 docker.py           # Docker integration
    ├── 📝 logging.py          # Logging system
    └── 🎯 main.py             # Main application
```

---

## 🔧 Configuration

### config.json

```json
{
  "paths": {
    "output_dir": "outputs/www",
    "vendor_dir": "overrides/assets/vendor",
    "vendor_builder_dir": "tools/vendor-builder"
  },
  "build": {
    "clean_before_build": true,
    "check_vendor_dependencies": true
  },
  "serve": {
    "port": 8000,
    "host": "localhost",
    "check_vendor_dependencies": true
  },
  "docker": {
    "image_name": "phantom-docs-kit",
    "build_tag": "latest",
    "container_prefix": "phantom-docs"
  },
  "logging": {
    "enabled": false,
    "console_level": "INFO",
    "file_level": "DEBUG",
    "log_directory": "logs",
    "max_file_size": "10MB",
    "backup_count": 5,
    "timestamp_format": "%Y-%m-%d %H:%M:%S",
    "log_filename_pattern": "phantom-{mode}-{date}-{time}.log"
  }
}
```

---

## 🛠️ Built-in Tools

### Image Optimizer

```bash
cd tools/image-optimizer
npm install
node optimize.js ./images --quality 80 --output ./optimized
```

### Vendor Builder

```bash
cd tools/vendor-builder
npm install
node build.js
```

---

## 🌟 Advanced Features

### Remote Development with Mutagen

```bash
# Install Mutagen (macOS)
brew install mutagen-io/mutagen/mutagen

# Configure SSH
ssh-keygen -t ed25519 -C "phantom-docs"
ssh-copy-id user@remote-server

# Connect & sync
export DOCKER_HOST=ssh://user@remote-server && python serve.py --docker
```

### Multi-language Documentation

```yaml
# mkdocs.yml
plugins:
  - i18n:
      languages:
        - locale: en
          name: English
        - locale: tr
          name: Türkçe
```

### Example Implementations

The `examples/` directory contains practical implementations and utilities:

**Mutagen Integration** ([examples/mutagen-integration-sample/](examples/mutagen-integration-sample/README.md))  
Demonstrates remote Docker development with Mutagen file synchronization. Includes SDK implementation and testing scripts for efficient remote container workflows.

**Utility Scripts**  
- `run_with_recording.py` - Captures terminal sessions as Asciinema recordings for documentation demos

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses

See [THIRD_PARTY_LICENSES](THIRD_PARTY_LICENSES) for dependencies.

****Copyright © 2025 Rıza Emre ARAS****
