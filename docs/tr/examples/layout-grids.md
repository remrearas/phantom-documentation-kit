# Yerleşim Izgaraları

**Yerleşim Izgaraları** içeriği tepkisel (responsive) biçimde sütunlar üzerinde düzenlemeye yardımcı olur. 
Farklı ekran boyutlarına otomatik olarak uyum sağlarlar.

## İki Sütun Düzeni

<div class="phantom-grid phantom-grid-2">
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Sol Sütun</span>
    </div>
    <div class="phantom-module-card-description">
      İki sütunlu yerleşim ızgarasının sol sütunundaki içerik.
    </div>
  </div>
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Sağ Sütun</span>
    </div>
    <div class="phantom-module-card-description">
      İki sütunlu yerleşim ızgarasının sağ sütunundaki içerik.
    </div>
  </div>
</div>

## Üç Sütun Düzeni

<div class="phantom-grid phantom-grid-3">
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">1</div>
    <div class="phantom-test-status-label">Birinci Sütun</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">2</div>
    <div class="phantom-test-status-label">İkinci Sütun</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">3</div>
    <div class="phantom-test-status-label">Üçüncü Sütun</div>
  </div>
</div>

## Dört Sütun Düzeni

<div class="phantom-grid phantom-grid-4">
  <div class="phantom-test-status-card success">
    <div class="phantom-test-status-value">A</div>
    <div class="phantom-test-status-label">İlk</div>
  </div>
  <div class="phantom-test-status-card warning">
    <div class="phantom-test-status-value">B</div>
    <div class="phantom-test-status-label">İkinci</div>
  </div>
  <div class="phantom-test-status-card error">
    <div class="phantom-test-status-value">C</div>
    <div class="phantom-test-status-label">Üçüncü</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">D</div>
    <div class="phantom-test-status-label">Dördüncü</div>
  </div>
</div>

## Asimetrik Izgara Yapısı

### 2/3 + 1/3 Bölme

<div class="phantom-grid phantom-grid-2-1">
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Ana İçerik (2/3)</span>
    </div>
    <div class="phantom-module-card-description">
      Bu sütun mevcut alanın üçte ikisini kaplar. Ana içerik alanları için mükemmeldir.
    </div>
  </div>
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Kenar Çubuğu (1/3)</span>
    </div>
    <div class="phantom-module-card-description">
      Bu sütun alanın üçte birini kaplar.
    </div>
  </div>
</div>

### 1/4 + 3/4 Bölme

<div class="phantom-grid phantom-grid-1-3">
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Nav</span>
    </div>
    <div class="phantom-module-card-description">
      Navigasyon için dar sütun
    </div>
  </div>
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">İçerik Alanı</span>
    </div>
    <div class="phantom-module-card-description">
      Detaylı bilgi için bol yer ile ana içerik görüntüleme için geniş sütun.
    </div>
  </div>
</div>

## Tepkisel (Responsive) Izgara Yapısı

Bu ızgara masaüstünde 4 sütun, tablette 2 sütun, mobilde 1 sütun olarak otomatik ayarlanır:

<div class="phantom-grid phantom-grid-auto">
  <div class="phantom-test-status-card success">
    <div class="phantom-test-status-value">
      <i class="fas fa-check-circle"></i>
      4
    </div>
    <div class="phantom-test-status-label">Responsive</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">
      <i class="fas fa-info-circle"></i>
      2
    </div>
    <div class="phantom-test-status-label">Esnek</div>
  </div>
  <div class="phantom-test-status-card warning">
    <div class="phantom-test-status-value">
      <i class="fas fa-exclamation-triangle"></i>
      1
    </div>
    <div class="phantom-test-status-label">Uyarlanabilir</div>
  </div>
  <div class="phantom-test-status-card error">
    <div class="phantom-test-status-value">
      <i class="fas fa-times-circle"></i>
      0
    </div>
    <div class="phantom-test-status-label">Dinamik</div>
  </div>
</div>

## İç İçe Izgaralar

<div class="phantom-grid phantom-grid-2">
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Ana Grid - Sol</span>
    </div>
    <div class="phantom-module-card-description">
      <div class="phantom-grid phantom-grid-2 phantom-grid-nested phantom-grid-gap-sm">
        <div class="phantom-grid-item">İç İçe 1</div>
        <div class="phantom-grid-item">İç İçe 2</div>
      </div>
    </div>
  </div>
  <div class="phantom-module-card">
    <div class="phantom-module-card-header">
      <span class="phantom-module-card-title">Ana Grid - Sağ</span>
    </div>
    <div class="phantom-module-card-description">
      <div class="phantom-grid phantom-grid-nested phantom-grid-gap-sm">
        <div class="phantom-grid-item">Tam Genişlik İç İçe</div>
        <div class="phantom-grid-item">Tam Genişlik İç İçe</div>
      </div>
    </div>
  </div>
</div>

## Farklı Aralıklı Izgaralar

### Küçük Aralık (10px)
<div class="phantom-grid phantom-grid-3 phantom-grid-gap-sm">
  <div class="phantom-grid-item">Küçük</div>
  <div class="phantom-grid-item">Aralık</div>
  <div class="phantom-grid-item">Grid</div>
</div>

### Orta Aralık (20px)
<div class="phantom-grid phantom-grid-3 phantom-grid-gap-md">
  <div class="phantom-grid-item">Orta</div>
  <div class="phantom-grid-item">Aralık</div>
  <div class="phantom-grid-item">Grid</div>
</div>

### Büyük Aralık (30px)
<div class="phantom-grid phantom-grid-3 phantom-grid-gap-lg">
  <div class="phantom-grid-item">Büyük</div>
  <div class="phantom-grid-item">Aralık</div>
  <div class="phantom-grid-item">Grid</div>
</div>

## En İyi Uygulamalar

1. **Tepkisel (Responsive) Tasarım**: Otomatik tepkisel ızgara yapıları için `phantom-grid-auto` sınıfını kullanın
2. **Aralık Boyutlandırma**: Tutarlı boşluklar için aralık sınıflarını (`phantom-grid-gap-sm`, `phantom-grid-gap-md`, `phantom-grid-gap-lg`) kullanın
