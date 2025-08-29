---
extra_javascript:
  - assets/javascripts/asciinema-player.js
---

# Phantom Image Optimizer

## :fontawesome-solid-wrench: Bu Araç Ne İşe Yarar?

**Phantom Image Optimizer**, Phantom Documentation Kit'in bağımsız çalışan görsel optimizasyon aracıdır.

### Temel Amaç
Dokümantasyon projelerinde kullanılan görsellerin optimize edilmesi için geliştirilmiştir. 
Büyük boyutlu görseller dokümantasyon sayfalarının yavaş yüklenmesine neden olur. 
Bu araç, görsel kalitesini koruyarak dosya boyutlarını önemli ölçüde küçültür.

### Güçlü Altyapı

**Sharp** kütüphanesinin endüstriyel gücünden faydalanır. Bu sayede:

  - Dokümantasyon görselleri
  - Web site fotoğrafları  
  - Blog içeriklerinde kullandığınız görseller
  - E-ticaret ürün görselleri
  - Tüm dijital projelerinizdeki optimizasyon ihtiyacı olan görseller

için profesyonel seviyede optimizasyon sağlar.

---

## :fontawesome-solid-rocket: Hadi Başlayalım! 

### Adım 1: Kurulum 

#### Sistem Gereksinimleri

##### :fontawesome-brands-node-js: Node.js Sürümü
- **Minimum Node.js sürümü: 22.x veya üzeri** gereklidir
- Node.js sürümünüzü kontrol etmek için: `node --version`
- Uygun Node.js sürümünü indirmek için: [https://nodejs.org/en/download](https://nodejs.org/en/download)

##### :fontawesome-brands-apple: macOS Sistem Paketleri

Sharp kütüphanesinin düzgün çalışması için aşağıdaki paketlerin kurulu olması gerekir:

Homebrew ile gerekli paketlerin kurulumunu rahatlıkla yapabilirsiniz.
```bash
brew install vips pkg-config
```
```bash
brew install libjpeg libpng webp giflib libtiff
```

##### :fontawesome-brands-linux: Linux Sistem Paketleri

**Ubuntu/Debian tabanlı sistemler için:**
```bash
sudo apt-get update && sudo apt-get install -y \
    libvips42 libvips-dev \
    libjpeg-dev libpng-dev libwebp-dev \
    libgif-dev libtiff-dev \
    pkg-config build-essential
```

**RHEL/CentOS/Fedora tabanlı sistemler için:**
```bash
sudo yum install -y \
    vips vips-devel \
    libjpeg-turbo-devel libpng-devel libwebp-devel \
    giflib-devel libtiff-devel \
    pkgconfig gcc-c++ make
```

##### :fontawesome-brands-docker: Phantom Documentation Kit Docker Modu

Phantom Documentation Kit, Docker imajında bu aracı çalıştırmak için gerekli araçlar ve Node versiyonu standart
halde bulunur. Docker modunda `serve` çalıştırdıktan sonra çalışan konteyner içerisinde kurulum adımlarını
takip ederek, aracı çalıştırabilirsiniz. 

Burada dikkat edilmesi gereken nokta her `serve` çalıştırdığınızda bu araç için gerekli kurulum adımlarını tekrardan
takip etmeniz gerekmektedir.


#### Paket Kurulumu

Terminal'i açın ve projenin olduğu dizine gelin ardından şunu yazarak Phantom Image Optimizer'ın olduğu dizine gelin:

```bash
cd tools/image-optimizer
```

Gerekli npm paketlerinin kurulumunu aşağıdaki komutla gerçekleştirin:

```bash
npm install
```

Global olarak kullanmak isterseniz aşağıdaki komutu uygulayın.

```bash
npm link
```

Ardından doğrudan `phantom-optimize` komutuyla istediğiniz yerde çalıştırabilirsiniz.

```bash
phantom-optimize ./images
```

### Adım 2: İlk Optimizasyonumuz!

#### :fontawesome-solid-star: En Basit Kullanım

Aşağıdaki komutla 'images' dizini içerisindeki görsellerinizin optimizasyonunu gerçekleştirin:

```bash
node optimize.js ../../docs/assets/static/images
```

Dilerseniz orijinallerini koruyarak optimize edilmiş görselleri farklı bir dizinede kaydedebilirsiniz.
```bash
node optimize.js \
         ../../docs/assets/static/images \
         --output ../../docs/assets/static/optimized_images
```

---

## :fontawesome-solid-lightbulb: Hızlı İpuçları 

### "Dosyalarım Çok Büyük" Diyorsanız:
```bash
node optimize.js ./photos --quality 60
```

###  "Orijinalleri Kaybetmek İstemiyorum" Diyorsanız:
```bash
node optimize.js ./original-photos --output ./optimized
```

###  "Önce Test Etmek İstiyorum" Diyorsanız:
```bash
node optimize.js ./photos --dry-run
```

###  "Sadece JPEG'leri Optimize Et" Diyorsanız:
```bash
node optimize.js ./photos --formats jpeg
```

---

## :fontawesome-solid-dice: Pratik Denemeler

### Hız Testi
4 dosyayı aynı anda işle (turbo mod!)
```bash
node optimize.js ./photos --concurrency 4
```

### Detaylı Bilgi
Her şeyi anlat bana!
```bash
node optimize.js ./photos --verbose
```

### Sessiz Mod
Sadece hataları göster, gerisini boşver
```bash
node optimize.js ./photos --silent
```

---

## :fontawesome-solid-flask: Gerçek Test Sonuçlarımız

### Test Sistemimiz Nasıl Çalışıyor?

**Basit Anlatım:** Bir test betiği yazıldı, Phantom Image Optimizer'ın tüm özelliklerini gerçek dünya 
koşullarında kapsamlı bir şekilde test ediyor.

### Test Betiğini Çalıştırmak İster misiniz?
`tools/image-optimizer` dizininde olduğunuzdan emin olun ve test betiğinin olduğu 'testing' klasörüne gidin:
```bash
cd testing
```
Test betiğini çalıştırmanın farklı yolları mevcut, dilediğiniz gibi çalıştırarak sizde test edebilirsiniz. 
Dilersen testlerin sonunda sonuçları karşılaştırmak için saklayarak hem raporu hem de görselleri inceleyerek
karşılaştırmalarını yapabilirsiniz.

Test betiğini çalıştırın:
```bash
python test_comprehensive.py
```
Daha detaylı hata takibi ve çıktılar için:
```bash
python test_comprehensive.py --verbose
```
Test sonuçlarını karşılaştırmak için saklamak isterseniz:
```bash
python test_comprehensive.py --keep-artifacts
```

### Test Tam Olarak Ne Yapıyor?

1. **:fontawesome-solid-download: Önce fotoğrafları indiriyor** - Oxford Üniversitesi'nin 7390 kedi-köpek fotoğrafı
2. **:fontawesome-solid-microscope: 15 farklı test yapıyor** - Kritik durumları gerçek kullanıcı kullanımına göre deniyor
3. **:fontawesome-solid-file-lines: Rapor yazıyor** - Rapor dosyasına sonuçları kaydediyor
4. **:fontawesome-solid-broom: Temizlik yapıyor** - İsterseniz test dosyalarını siliyor, isterseniz karşılaştırma yapmak için saklıyor

###  Neden Oxford Pet Dataset?

**Açık Konuşalım:** Test için gerçek fotoğraflar gerekliydi. Oxford Üniversitesi'nin kedi-köpek fotoğrafları seçildi çünkü:

-  **Her zaman ulaşılabilir** - Akademik bir çalışma, link her zaman erişilebilir
-  **Gerçek fotoğraflar** - Gerçek hayattan akademik bir çalışma için seçilmiş görüntüler
-  **7390 fotoğraf** - Hem hızlı test (15 tanesi) hem büyük test (hepsi) yapılabiliyor
-  **Herkes kullanabilir** - Açık kaynak, ücretsiz, bilimsel amaçlı

Bu sayede testler gerçekçi oluyor ve sonuçlar rahatlıkla karşılaştırılabiliyor!

### Gerçek Test Sonuçları

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python test_comprehensive.py --verbose</span>
</div>
<div class="asciinema-player-container">
    <div class="asciinema-player-header">
        <h3>Phantom Image Optimizer</h3>
        <span class="asciinema-player-info">Test Terminal Kaydı</span>
    </div>
    <div class="asciinema-player-wrapper">
        <div class="asciinema-player" 
             data-cast-file="recordings/tests/tools/image-optimizer/test_comprehensive_20250807_092345.cast"
             data-cols="120"
             data-rows="40"
             data-autoplay="false"
             data-loop="false"
             data-speed="1.5"
             data-theme="solarized-dark"
             data-font-size="small">
        </div>
    </div>
</div>

Gerçek test sonuçlarının kapsamlı ve olduğu gibi çıktılarını görmek isterseniz aşağıdaki dosya konumlarındaki
dosyaları kontrol edebilirsiniz.

- `testing/reports/TEST_REPORT_20250807_092504.md`
- `testing/recordings/test_comprehensive_20250807_092345.cast`

#### Yüksek Kalite Optimizasyon (Quality 90)

**Komut:**
<div class="phantom-command-example">
      <span class="command-prompt">$</span>
      <span class="command-text">node optimize.js \
         ./testing/data/mini_dataset \
         -q 90 \
         --output ./testing/outputs/output_high_quality</span>
</div>

**Gerçek Sonuçlar:**
```
15 görsel işlendi
İşlem süresi: 0.35 saniye
Toplam boyut: 1.29MB → 562.3KB (%57.3 küçülme)

Örnek dosyalar:
├── scottish_terrier_43.jpg: 172.93KB → 83.38KB (%51.8 küçüldü)
├── shiba_inu_95.jpg: 140.04KB → 55.78KB (%60.2 küçüldü)
├── pomeranian_38.jpg: 133.27KB → 41.2KB (%69.1 küçüldü)
└── Birman_134.jpg: 103.85KB → 34.48KB (%66.8 küçüldü)
```

#### Orta Kalite Optimizasyon (Quality 75)

**Komut:**
<div class="phantom-command-example">
      <span class="command-prompt">$</span>
      <span class="command-text">node optimize.js \
         ./testing/data/mini_dataset \
         -q 75 \
         --output ./testing/outputs/output_medium_quality</span>
</div>

**Gerçek Sonuçlar:**
```
15 görsel işlendi
İşlem süresi: 0.29 saniye
Toplam boyut: 1.29MB → 312.3KB (%76.3 küçülme)

Örnek dosyalar:
├── scottish_terrier_43.jpg: 172.93KB → 48.66KB (%71.9 küçüldü)
├── pomeranian_38.jpg: 133.27KB → 18.81KB (%85.9 küçüldü!)
└── Birman_134.jpg: 103.85KB → 15.34KB (%85.2 küçüldü!)
```

#### Agresif Optimizasyon (Quality 60)

**Komut:**
<div class="phantom-command-example">
      <span class="command-prompt">$</span>
      <span class="command-text">node optimize.js \
         ./testing/data/mini_dataset \
         -q 60 \
         --output ./testing/outputs/output_low_quality</span>
</div>

**Gerçek Sonuçlar:**
```
15 görsel işlendi
İşlem süresi: 0.22 saniye
Toplam boyut: 1.29MB → 220.17KB (%83.3 küçülme!)

Örnek dosyalar:
├── pomeranian_38.jpg: 133.27KB → 12.43KB (%90.7 küçüldü!!)
├── Birman_134.jpg: 103.85KB → 10.22KB (%90.2 küçüldü!!)
└── British_Shorthair_60.jpg: 101.52KB → 14.48KB (%85.7 küçüldü!)
```

---

## :fontawesome-solid-rocket: Pratik Kullanım Tablosu

| Ne İstiyorum?          | Komutu Kopyala                             |
|------------------------|--------------------------------------------|
| En Basit Kullanım      | `node optimize.js ./photos`                |
| Yüksek Kalite          | `node optimize.js ./photos -q 90`          |
| Hızlı ve Küçük         | `node optimize.js ./photos -q 60`          |
| Güvenli Test           | `node optimize.js ./photos --dry-run`      |
| Yedekle ve Optimize Et | `node optimize.js ./photos -o ./optimized` |
| Sadece JPEG            | `node optimize.js ./photos -f jpeg`        |
| Turbo Mod              | `node optimize.js ./photos -c 8`           |
| Sessiz Çalış           | `node optimize.js ./photos --silent`       |

