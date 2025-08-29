# Kod Blokları

Tema sistemimizdeki kod blokları otomatik olarak oluşturulan estetik dil rozetleri ve şık bir tasarımla beraber gelir. 
Dil tanımlayıcıları ile standart markdown kod çitlerini kullanmanız yeterlidir.

## Bash Komutları

```bash
# Merhaba dünya yazdır
echo "Merhaba, Dünya!"

# Güncel tarihi görüntüle
date

# Dosyaları listele
ls -la
```

## Python Kodu

```python
# Basit merhaba dünya
print("Merhaba, Dünya!")

# Değişkenlerle çalışma
name = "Phantom"
version = 2.0
print(f"{name} v{version}'e hoş geldiniz")

# Basit fonksiyon
def greet(user):
    return f"Merhaba, {user}!"

print(greet("Geliştirici"))
```

## JavaScript/TypeScript

```javascript
// Merhaba dünya yazdır
console.log("Merhaba, Dünya!");

// Basit fonksiyon
function greet(name) {
    return `Merhaba, ${name}!`;
}

// Fonksiyonu kullan
const message = greet("Geliştirici");
console.log(message);

// Ok fonksiyonu
const add = (a, b) => a + b;
console.log(add(5, 3)); // 8
```

## YAML Yapılandırması

```yaml
# Basit yapılandırma
name: Benim Uygulamam
version: 1.0.0
description: Basit bir merhaba dünya uygulaması

# Ayarlar
settings:
  debug: true
  port: 8080
  
# Özellikler listesi
features:
  - authentication
  - logging
  - monitoring
```

## JSON Yanıtı

```json
{
  "message": "Merhaba, Dünya!",
  "status": "başarılı",
  "data": {
    "user": "geliştirici",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

## Dockerfile

```dockerfile
# Hafif temel imajı kullan
FROM alpine:latest

# Selamlama scripti ekle
RUN echo 'echo "Docker\'dan merhaba!"' > /greet.sh
RUN chmod +x /greet.sh

# Başlangıçta selamlamayı çalıştır
CMD ["/greet.sh"]
```

## SQL Sorguları

```sql
-- Basit tablo oluştur
CREATE TABLE greetings (
    id INTEGER PRIMARY KEY,
    message TEXT NOT NULL
);

-- Veri ekle
INSERT INTO greetings (message) 
VALUES ('Merhaba, Dünya!');

-- Veri sorgula
SELECT * FROM greetings;
```

## HTML/XML

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <title>Merhaba Dünya</title>
</head>
<body>
    <h1>Merhaba, Dünya!</h1>
    <p>Phantom Documentation'a hoş geldiniz</p>
</body>
</html>
```

## CSS Stilleri

```css
/* Basit stiller */
body {
    font-family: monospace;
    background: #f0f0f0;
}
```

## Kullanım Kılavuzu

````markdown
```python
print("Merhaba, Dünya!")
```

```bash
echo "Merhaba, Dünya!"
```

```javascript
console.log("Merhaba, Dünya!");
```
````

## Dil Rozeti Renkleri

Belgelerimiz kod bloklarına otomatik olarak renkli rozetler ekler:

| Dil            | Rozet                                                                                                                                          | Renk Kodu  |
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

### Ek Dil Rozetleri

| Dil          | Rozet                                                                                                                                         | Renk Kodu  |
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

## Daha Fazla Dil

### Go
```go
package main
import "fmt"

func main() {
    fmt.Println("Merhaba, Dünya!")
}
```

### Rust
```rust
fn main() {
    println!("Merhaba, Dünya!");
}
```

### Java
```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Merhaba, Dünya!");
    }
}
```

### C++
```cpp
#include <iostream>

int main() {
    std::cout << "Merhaba, Dünya!" << std::endl;
    return 0;
}
```

### Ruby
```ruby
# Basit selamlama
puts "Merhaba, Dünya!"

# Metot örneği
def greet(name)
  "Merhaba, #{name}!"
end

puts greet("Geliştirici")
```

### PHP
```php
<?php
// Basit selamlama
echo "Merhaba, Dünya!";

// Fonksiyon örneği
function greet($name) {
    return "Merhaba, $name!";
}

echo greet("Geliştirici");
?>
```