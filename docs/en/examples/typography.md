# Typography

Our documentation uses custom heading fonts for better visual hierarchy and monospace fonts for technical content.

## Font Information

### Heading Font
- **Font Family**: Orbitron (CSS variable: `--phantom-font-heading`)
- **Google Fonts**: [fonts.google.com/specimen/Orbitron](https://fonts.google.com/specimen/Orbitron)
- **Local Files**: `assets/fonts/orbitron-{400,600,800}.ttf`
- **Usage**: Headlines and emphasized text in custom components
- **Purpose**: Futuristic, technology-focused appearance

### Code and Terminal Font
- **Font Family**: Share Tech Mono (CSS variable: `--phantom-font-mono`)
- **Google Fonts**: [fonts.google.com/specimen/Share+Tech+Mono](https://fonts.google.com/specimen/Share+Tech+Mono)
- **Local File**: `assets/fonts/share-tech-mono-400.ttf`
- **Usage**: Code blocks, terminal commands, and technical content
- **Purpose**: Retro terminal aesthetic, perfect character alignment

### Material Default Fonts
- **Body Text**: Roboto (MkDocs Material default)
- **Code Blocks**: Roboto Mono (MkDocs Material default)
- **Usage**: General documentation content
- **Purpose**: Compatible with Google Material Design, modern appearance

## Headings

# H1: Main Page Title
## H2: Section Header
### H3: Subsection Header
#### H4: Component Title
##### H5: Feature Title
###### H6: Minor Heading


## Text Formatting

This is a paragraph demonstrating the regular body text styling. The monospace font maintains readability while giving documentation a technical feel.

**Bold text** for emphasis  
*Italic text* for subtle emphasis  
***Bold and italic*** for strong emphasis  
~~Strikethrough text~~ for deprecated content  
`Inline code` for code references  


## Links

- [External Link](https://github.com/remrearas) - Opens in same window
- [Internal Link](#headings) - Smooth scroll to section
- [Email Link](mailto:emre@aras.tc) - Opens email client
- `https://www.aras.tc` - Auto-linked URL


## Lists

### Unordered Lists

- First level item
- Another first level item
  - Second level item
  - Another second level item
    - Third level item
    - Another third level item
- Back to first level

### Ordered Lists

1. First step
2. Second step
   1. Sub-step A
   2. Sub-step B
      1. Detail 1
      2. Detail 2
3. Third step

### Mixed Lists

1. **Setup Environment**
   - Install Python 3.8+
   - Install Docker
   - Clone repository
2. **Configure Application**
   - Copy `.env.example` to `.env`
   - Update configuration values:
     - API tokens
     - Database credentials
     - Service endpoints
3. **Run Tests**
   - Unit tests: `pytest tests/unit`
   - Integration tests: `pytest tests/integration`

## Blockquotes

> This is a blockquote. It's useful for highlighting important information or quotes from external sources.

> **Note:** Multi-line blockquotes can contain formatted text.
> 
> They can even contain lists:
> 
> - Item one
> - Item two
> - Item three

> > Nested blockquotes are also supported for deeper context levels.

## Horizontal Rules

Use horizontal rules to separate major sections:

---

Like this one above and below.

---

## Definition Lists

**Term 1**
:   Definition for term 1. This can be a longer explanation that spans multiple lines if needed.

**Term 2**
:   Definition for term 2
:   Can have multiple definitions

**API Token**
:   A unique identifier used to authenticate requests to the API. Should be kept secure and never committed to version control.

**Environment Variable**
:   A dynamic value that can affect the way running processes behave on a computer. Commonly used for configuration.

## Tables

### Basic Table

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

### Aligned Table

| Left Aligned                          | Center Aligned | Right Aligned |
|:--------------------------------------|:--------------:|--------------:|
| Left                                  |     Center     |         Right |
| 123                                   |      456       |           789 |
| Long text that demonstrates alignment |    Centered    |         Right |

### Complex Table

| Feature       | Free Tier |  Pro Tier   | Enterprise |
|---------------|:---------:|:-----------:|:----------:|
| **Users**     |     5     |     50      | Unlimited  |
| **Storage**   |   10 GB   |   100 GB    |   1 TB+    |
| **Support**   | Community |    Email    | 24/7 Phone |
| **API Calls** | 1,000/day | 100,000/day | Unlimited  |
| **Price**     |    $0     |   $49/mo    | Contact Us |

## Special Characters

- Copyright: © 2024 Phantom
- Trademark: Phantom™
- Registered: Phantom®
- Arrows: → ← ↑ ↓ ↔
- Math: ± × ÷ ≈ ≠ ≤ ≥
- Misc: • … — –


## Emphasis Patterns

### Do This
- Use **bold** for important terms on first mention
- Use `inline code` for:
  - File names: `config.yaml`
  - Commands: `docker-compose up`
  - Function names: `calculate_total()`
  - Variable names: `API_TOKEN`

### Don't Do This
- Don't use CAPS LOCK for emphasis
- Don't overuse ***bold italic*** combinations
- Don't underline text (reserved for links)