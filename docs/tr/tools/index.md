# Araçlara Giriş

Phantom Documentation Kit, dokümantasyon projelerinizi daha verimli ve profesyonel hale getirmek için güçlü araçlar sunar. 

## :fontawesome-solid-cube: Vendor Builder

### Ne İşe Yarar?

**Phantom Vendor Builder**, JavaScript ve CSS bağımlılıklarınızı otomatik olarak yöneten bir araçtır. Chart.js, Font Awesome gibi üçüncü parti kütüphaneleri tek merkezden yönetmenizi sağlar.

### Temel Özellikler

- **:fontawesome-solid-rotate: Otomatik Derleme**: `serve.py` ve `build.py` çalıştığında eksik dosyalar otomatik derlenir
- **:fontawesome-solid-box: NPM Entegrasyonu**: Tüm npm paketleriyle uyumlu
- **:fontawesome-solid-bolt: Akıllı Optimizasyon**: Terser ve cssnano ile özelleştirilebilir optimizasyon
- **:fontawesome-solid-palette: Font Awesome Built-in**: Font Awesome otomatik olarak dahil edilir

### Konfigürasyon

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

### Otomatik İşlenen Kütüphaneler

- **Font Awesome**: CSS ve webfonts otomatik dahil
- **Chart.js**: Grafik kütüphanesi
- **Asciinema Player**: Terminal kayıt oynatıcı
- **LoadJS**: Dinamik script yükleyici

[:fontawesome-solid-book: Detaylı Dokümantasyon →](./vendor-builder.md)

## :fontawesome-solid-image: Image Optimizer

### Ne İşe Yarar?

**Phantom Image Optimizer**, dokümantasyonlarınızda kullandığınız görselleri otomatik olarak optimize eden güçlü bir araçtır. 
Sharp kütüphanesinin endüstriyel gücünden faydalanarak, görsel kalitesini korurken dosya boyutlarını önemli ölçüde azaltır.

### Temel Özellikler

- **:fontawesome-solid-rocket: Yüksek Performans**: Paralel işleme desteği ile hızlı optimizasyon
- **:fontawesome-solid-chart-line: Akıllı Sıkıştırma**: Görsel kalitesini koruyarak %70'e varan boyut azaltımı
- **:fontawesome-solid-bullseye: Çoklu Format Desteği**: JPEG, PNG, WebP, AVIF formatları
- **:fontawesome-solid-gears: Esnek Yapılandırma**: Özelleştirilebilir kalite ve boyut ayarları
- **:fontawesome-solid-flask: Test Sistemi**: Oxford Pet Dataset ile performans testi

### Kullanım Senaryoları

- Dokümantasyon ekran görüntüleri
- Blog ve makale görselleri
- Ürün fotoğrafları
- Diyagram ve infografikler

[:fontawesome-solid-book: Detaylı Dokümantasyon →](./image-optimizer.md)



