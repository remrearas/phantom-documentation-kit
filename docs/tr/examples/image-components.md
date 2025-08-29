---
extra_javascript:
  - assets/javascripts/phantom-image.js
---

# Görüntü Bileşenleri

Phantom Görüntü Bileşenleri; lazy-loading, lightbox desteği ve tepkisel (responsive) düzenler gibi özelliklerle 
belgelerinizdeki resimleri görüntülemek için güçlü,esnek ve benzersiz bir yol sağlar.

!!! info "Bileşen Özellikleri"
    - **Lazy Loading**: Resimler yalnızca görünüm alanına girdiğinde yüklenir
    - **Lightbox Desteği**: Tam ekran resim görüntüleme
    - **Tepkisel (Responsive) Tasarım**: Farklı ekran boyutlarına kolaylıkla adapte olur
    - **Esnek Konumlandırma**: Sola, sağa veya merkeze yerleştirin
    - **Izgara Düzenleri**: Birden fazla resmi verimli şekilde görüntüleyin

!!! tip "Resim Yolu Çözümleme"
    Resimler otomatik olarak `/assets/static/images/` dizininden çözümlenir. Sadece dosya adını kullanın:
    
    - `data-src="example.png"` → `/assets/static/images/example.png`
    - Mutlak yollar için `/` ile başlayın: `data-src="/custom/path/image.png"`
    - Harici resimler için tam URL kullanın: `data-src="https://example.com/image.png"`

## Temel Kullanım

### Basit Resim

En temel kullanım - sadece resim kaynağını sağlayın:

<div class="phantom-image-container" 
     data-src="phantom-logo.jpg"
     data-alt="Phantom Documentation Kit Logosu">
</div>

### Altyazılı Resim

Resimlerinize altyazılarla bağlam ekleyin:

<div class="phantom-image-container" 
     data-src="example-2.jpg"
     data-alt="Altyazılı resim örneği"
     data-caption="Bu açıklayıcı altyazılı örnek bir resimdir">
</div>

## Boyut Varyantları

Resimlerinizin görüntüleme boyutunu kontrol edin:

### Küçük Resim

<div class="phantom-image-container" 
     data-src="phantom-logo.jpg"
     data-alt="Küçük boyut örneği"
     data-size="small"
     data-caption="Küçük boyut (max-width: 300px)">
</div>

### Orta Resim (Varsayılan)

<div class="phantom-image-container" 
     data-src="example-2.jpg"
     data-alt="Orta boyut örneği"
     data-size="medium"
     data-caption="Orta boyut (max-width: 600px)">
</div>

### Büyük Resim

<div class="phantom-image-container" 
     data-src="example-3.jpg"
     data-alt="Büyük boyut örneği"
     data-size="large"
     data-caption="Büyük boyut (max-width: 900px)">
</div>

### Tam Genişlik Resim

<div class="phantom-image-container" 
     data-src="og-image.jpg"
     data-alt="Tam genişlik örneği"
     data-size="full"
     data-caption="Tam genişlik resim">
</div>

## Metinle Konumlandırma

Resimler metin içeriğinizle akacak şekilde konumlandırılabilir:

### Sola Hizalanmış Resim

<div class="phantom-image-container" 
     data-src="phantom-logo.jpg"
     data-alt="Sola hizalanmış resim"
     data-size="small"
     data-position="left">
</div>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

<div class="phantom-clear"></div>

### Sağa Hizalanmış Resim

<div class="phantom-image-container" 
     data-src="phantom-logo.jpg"
     data-alt="Sağa hizalanmış resim"
     data-size="small"
     data-position="right"
     data-caption="Sağa yerleşen">
</div>

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

<div class="phantom-clear"></div>

## Lightbox Özelliği

Lightbox etkin resimlere tıklayarak tam ekranda görüntüleyin:

<div class="phantom-image-container" 
     data-src="og-image.jpg"
     data-alt="Lightbox örneği"
     data-caption="Lightbox'ta açmak için resme tıklayın"
     data-size="medium"
     data-lightbox="true">
</div>

## Resim Izgarası

Birden fazla resimi tepkisel (responsive) ızgara düzeninde görüntüleyin:

<div class="phantom-image-grid">
  <div class="phantom-image-container" 
       data-src="example-1.jpg"
       data-alt="Grid resim 1"
       data-caption="İlk resim"
       data-lightbox="true">
  </div>
  <div class="phantom-image-container" 
       data-src="example-2.jpg"
       data-alt="Grid resim 2"
       data-caption="İkinci resim"
       data-lightbox="true">
  </div>
  <div class="phantom-image-container" 
       data-src="example-3.jpg"
       data-alt="Grid resim 3"
       data-caption="Üçüncü resim"
       data-lightbox="true">
  </div>
  <div class="phantom-image-container" 
       data-src="og-image.jpg"
       data-alt="Grid resim 4"
       data-caption="Dördüncü resim"
       data-lightbox="true">
  </div>
</div>

## Resim Karşılaştırması

İki resmi yan yana karşılaştırın:

<div class="phantom-image-comparison">
  <div class="phantom-image-container" 
       data-src="phantom-logo.jpg"
       data-alt="Önceki durum"
       data-caption="Optimizasyondan önce">
  </div>
  <div class="phantom-image-container" 
       data-src="og-image.jpg"
       data-alt="Sonraki durum"
       data-caption="Optimizasyondan sonra">
  </div>
</div>

## Gelişmiş Kullanım

### Resimlerle Eğitim

<div class="phantom-tutorial-step">
  <h3>Adım 1: Ayarları Aç</h3>
  <div class="phantom-image-container" 
       data-src="example-1.jpg"
       data-alt="Ayarlar ekranı"
       data-size="small"
       data-position="right">
  </div>
  <p>İlk olarak, sağ üst köşedeki dişli simgesine tıklayarak ayarlar sayfasına gidin. Ayarlar sayfası uygulamanız için tüm yapılandırma seçeneklerini içerir.</p>
  <p>Genel ayarlar, görünüm ve gelişmiş seçenekler dahil çeşitli bölümler bulacaksınız.</p>
</div>

<div class="phantom-clear"></div>

<div class="phantom-tutorial-step">
  <h3>Adım 2: Seçenekleri Yapılandır</h3>
  <div class="phantom-image-container" 
       data-src="example-2.jpg"
       data-alt="Yapılandırma paneli"
       data-size="small"
       data-position="left">
  </div>
  <p>Yapılandırma panelinde, ihtiyaçlarınıza göre çeşitli ayarları düzenleyebilirsiniz. Her seçeneğin işlevini açıklayan bir araç ipucu vardır.</p>
  <p>Sayfadan ayrılmadan önce değişikliklerinizi kaydettiğinizden emin olun.</p>
</div>

<div class="phantom-clear"></div>

### Özellik Vitrini

<div class="phantom-feature-showcase">
  <div class="phantom-image-container" 
       data-src="phantom-logo.jpg"
       data-alt="Özellik simgesi"
       data-size="small">
  </div>
  <div class="feature-content">
    <h3>Gelişmiş Resim İşleme</h3>
    <p>Resim bileşenimiz belgelerinizdeki resimleri görüntülemek için son teknoloji özellikler sağlar:</p>
    <ul>
      <li>Performans için otomatik lazy loading</li>
      <li>Responsive boyutlandırma ve konumlandırma</li>
      <li>Yerleşik lightbox işlevselliği</li>
    </ul>
  </div>
</div>

## Yapılandırma Seçenekleri

### Veri Öznitelikleri

| Öznitelik       | Tür     | Varsayılan | Açıklama                                   |
|-----------------|---------|------------|--------------------------------------------|
| `data-src`      | string  | gerekli    | Resim kaynak URL'i                         |
| `data-alt`      | string  | ""         | Erişilebilirlik için alternatif metin      |
| `data-caption`  | string  | null       | Resim altında altyazı metni                |
| `data-size`     | string  | "medium"   | Boyut varyantı: small, medium, large, full |
| `data-position` | string  | "center"   | Konum: left, right, center                 |
| `data-loading`  | string  | "lazy"     | Yükleme stratejisi: lazy, eager            |
| `data-lightbox` | boolean | false      | Tıklamada lightbox etkinleştir             |

## Hata Durumları

### Başarısız Resim Yüklemesi

Bir resim yüklenemediğinde, bileşen net bir hata mesajı görüntüler:

<div class="phantom-image-container" 
     data-src="non-existent-image.jpg"
     data-alt="Başarısız yükleme örneği"
     data-caption="Resim başarısız olduğunda bu altyazı görünmez">
</div>

### Yükleme Durumu

Resimler yüklenirken bir spinner görüntülenir. İşte yükleme durumunu gösteren daha büyük bir resim örneği:

<div class="phantom-image-container" 
     data-src="https://picsum.photos/1920/1080?random=1"
     data-alt="Yükleme durumunu gösteren büyük resim"
     data-caption="Bu büyük resim indirme sırasında yükleme spinner'ını gösterir"
     data-size="large">
</div>

## En İyi Uygulamalar

1. **Her zaman alt metin sağlayın**: Erişilebilirlik ve SEO için gereklidir
2. **Uygun boyutları kullanın**: İçeriğiniz için doğru boyut varyantını seçin
3. **Detaylı resimler için lightbox etkinleştirin**: Gerektiğinde kullanıcıların tam çözünürlüğü görmesini sağlayın
4. **Bağlam için altyazı ekleyin**: Kullanıcıların neye baktıklarını anlamalarına yardımcı olun
5. **Resimlerinizi optimize edin**: Uygun formatları ve sıkıştırmayı kullanın
6. **Mobil kullanıcıları düşünün**: Resimlerin küçük ekranlarda nasıl göründüğünü test edin

## Sorun Giderme

### Resim Yüklenmiyor

- `data-src` geçerli bir resim URL'ini işaret ettiğini kontrol edin
- Resim dosyasının var olduğunu ve erişilebilir olduğunu doğrulayın
- Hata mesajları için tarayıcı konsolunu kontrol edin
- Yerel resimler için `/docs/assets/static/images/` içinde olduklarını doğrulayın

### Lightbox Çalışmıyor

- `data-lightbox="true"` ayarlandığını doğrulayın
- JavaScript'in etkin olduğunu kontrol edin
- `phantom-image.js` yüklendiğini doğrulayın
- Resmin başarıyla yüklendiğini onaylayın (lightbox başarısız resimler için devre dışı bırakılır)

### Düzen Sorunları

- Ana kapsayıcıların uygun genişliğe sahip olduğunu kontrol edin
- Farklı ekran boyutlarında tepkisel (responsive) davranışı test edin