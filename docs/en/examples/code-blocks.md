# Code Blocks

Code blocks in our theme system automatically come with language badges and elegant design. 
Simply use standard markdown code fences with language identifiers.

## Bash Commands

```bash
# Print hello world
echo "Hello, World!"

# Display current date
date

# List files
ls -la
```

## Python Code

```python
# Simple hello world
print("Hello, World!")

# Working with variables
name = "Phantom"
version = 2.0
print(f"Welcome to {name} v{version}")

# Simple function
def greet(user):
    return f"Hello, {user}!"

print(greet("Developer"))
```

## JavaScript/TypeScript

```javascript
// Print hello world
console.log("Hello, World!");

// Simple function
function greet(name) {
    return `Hello, ${name}!`;
}

// Use the function
const message = greet("Developer");
console.log(message);

// Arrow function
const add = (a, b) => a + b;
console.log(add(5, 3)); // 8
```

## YAML Configuration

```yaml
# Simple configuration
name: My Application
version: 1.0.0
description: A simple hello world app

# Settings
settings:
  debug: true
  port: 8080
  
# Features list
features:
  - authentication
  - logging
  - monitoring
```

## JSON Response

```json
{
  "message": "Hello, World!",
  "status": "success",
  "data": {
    "user": "developer",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

## Dockerfile

```dockerfile
# Use lightweight base image
FROM alpine:latest

# Add greeting script
RUN echo 'echo "Hello from Docker!"' > /greet.sh
RUN chmod +x /greet.sh

# Run greeting on start
CMD ["/greet.sh"]
```

## SQL Queries

```sql
-- Create simple table
CREATE TABLE greetings (
    id INTEGER PRIMARY KEY,
    message TEXT NOT NULL
);

-- Insert data
INSERT INTO greetings (message) 
VALUES ('Hello, World!');

-- Query data
SELECT * FROM greetings;
```

## HTML/XML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to Phantom Documentation</p>
</body>
</html>
```

## CSS Styles

```css
/* Simple styles */
body {
    font-family: monospace;
    background: #f0f0f0;
}
```

## Usage Guide

````markdown
```python
print("Hello, World!")
```

```bash
echo "Hello, World!"
```

```javascript
console.log("Hello, World!");
```
````

## Language Badge Colors

Our documentation automatically adds colored badges to code blocks:

| Language       | Badge                                                                                                                                          | Color Code |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **Python**     | <span style="background: #3776ab; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">PYTHON</span> | `#3776ab`  |
| **Bash**       | <span style="background: #4EAA25; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">BASH</span>   | `#4EAA25`  |
| **YAML**       | <span style="background: #CB171E; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">YAML</span>   | `#CB171E`  |
| **JSON**       | <span style="background: #292929; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">JSON</span>   | `#292929`  |
| **JavaScript** | <span style="background: #f7df1e; color: black; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">JS</span>     | `#f7df1e`  |
| **TypeScript** | <span style="background: #3178c6; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">TS</span>     | `#3178c6`  |
| **Docker**     | <span style="background: #2496ed; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">DOCKER</span> | `#2496ed`  |
| **SQL**        | <span style="background: #336791; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">SQL</span>    | `#336791`  |
| **HTML**       | <span style="background: #e34c26; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">HTML</span>   | `#e34c26`  |
| **CSS**        | <span style="background: #1572b6; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">CSS</span>    | `#1572b6`  |

### Additional Language Badges

| Language     | Badge                                                                                                                                         | Color Code |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **Go**       | <span style="background: #00ADD8; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">GO</span>    | `#00ADD8`  |
| **Rust**     | <span style="background: #dea584; color: black; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">RUST</span>  | `#dea584`  |
| **Java**     | <span style="background: #007396; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">JAVA</span>  | `#007396`  |
| **C++**      | <span style="background: #00599C; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">C++</span>   | `#00599C`  |
| **Ruby**     | <span style="background: #CC342D; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">RUBY</span>  | `#CC342D`  |
| **PHP**      | <span style="background: #777BB4; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">PHP</span>   | `#777BB4`  |
| **Markdown** | <span style="background: #083fa1; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">MD</span>    | `#083fa1`  |
| **Shell**    | <span style="background: #89e051; color: black; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">SH</span>    | `#89e051`  |
| **XML**      | <span style="background: #e34c26; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">XML</span>   | `#e34c26`  |
| **Swift**    | <span style="background: #FA7343; color: white; padding: 0.2em 0.6em; border-radius: 3px; font-size: 0.875em; font-weight: 600;">SWIFT</span> | `#FA7343`  |

## More Languages

### Go
```go
package main
import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

### Rust
```rust
fn main() {
    println!("Hello, World!");
}
```

### Java
```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### C++
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Ruby
```ruby
# Simple greeting
puts "Hello, World!"

# Method example
def greet(name)
  "Hello, #{name}!"
end

puts greet("Developer")
```

### PHP
```php
<?php
// Simple greeting
echo "Hello, World!";

// Function example
function greet($name) {
    return "Hello, $name!";
}

echo greet("Developer");
?>
```

