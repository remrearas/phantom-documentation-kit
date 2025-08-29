# Yükleme Aşamaları ve Durumları

Yükleme aşamaları ve durumları içerik işleme sırasında görsel geri bildirim sağlar, kullanıcıların sistemin çalıştığını ve içeriğin hazırlandığını anlamalarına yardımcı olur.

## Spinner Animasyonu

İçerik yükleme işlemleri için spinner animasyonlarını kullanın.

<div style="display: flex; align-items: center; gap: 20px; padding: 20px; background: var(--phantom-code-bg); border-radius: 8px; position: relative; min-height: 60px;">
  <div class="player-spinner" style="position: relative; transform: none; top: auto; left: auto;">
    <div class="spinner-inner"></div>
  </div>
  <span>Oynatıcı içeriği yükleniyor...</span>
</div>

## Farklı Yükleme Bağlamları

### Kart Yükleme Durumu

<div class="phantom-module-card" style="position: relative; min-height: 120px;">
  <div class="player-spinner" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
    <div class="spinner-inner"></div>
  </div>
</div>

### Veri Tabloları Yükleme Durumu

<div style="padding: 40px; background: var(--phantom-bg-secondary); border-radius: 8px; text-align: center;">
  <div style="margin-bottom: 20px;">
    <i class="fas fa-spinner fa-spin" style="color: var(--phantom-accent); font-size: 40px;"></i>
  </div>
  <p style="color: var(--phantom-text-secondary); margin: 0;">Veri yükleniyor...</p>
</div>

### Satır İçi Yükleme

<p>
  İstek işleniyor <i class="fas fa-spinner fa-spin" style="color: var(--phantom-accent); font-size: 14px; margin-left: 8px;"></i>
</p>

## İlerleme ile Yükleme Durumları

### Belirli İlerleme

<div style="padding: 20px; background: var(--phantom-code-bg); border-radius: 8px;">
  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
    <span>Dosyalar yükleniyor...</span>
    <span style="color: var(--phantom-text-secondary);">%75</span>
  </div>
  <div style="width: 100%; height: 8px; background: var(--phantom-border); border-radius: 4px; overflow: hidden;">
    <div style="width: 75%; height: 100%; background: var(--phantom-accent); transition: width 0.3s ease;"></div>
  </div>
</div>

### Çok Adımlı Yükleme

<div style="padding: 20px; background: var(--phantom-code-bg); border-radius: 8px;">
  <div style="margin-bottom: 15px;">
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
      <i class="fas fa-check-circle" style="color: #22c55e;"></i>
      <span>Ortam başlatılıyor</span>
    </div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
      <i class="fas fa-check-circle" style="color: #22c55e;"></i>
      <span>Bağımlılıklar yükleniyor</span>
    </div>
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
      <i class="fas fa-spinner fa-spin" style="color: var(--phantom-accent); font-size: 16px;"></i>
      <span>Kaynaklar derleniyor...</span>
    </div>
    <div style="display: flex; align-items: center; gap: 10px;">
      <i class="fas fa-circle" style="color: var(--phantom-text-secondary); opacity: 0.3;"></i>
      <span style="color: var(--phantom-text-secondary); opacity: 0.6;">Uygulama başlatılıyor</span>
    </div>
  </div>
</div>

## İskelet Yükleyiciler

İskelet yükleyiciler içerik yüklenirken yer tutucu arayüz gösterir:

<div class="phantom-module-card">
  <div class="phantom-module-card-header">
    <div style="width: 150px; height: 20px; background: var(--phantom-border); border-radius: 4px; animation: skeleton-pulse 1.5s ease-in-out infinite;"></div>
    <div style="width: 60px; height: 20px; background: var(--phantom-border); border-radius: 4px; animation: skeleton-pulse 1.5s ease-in-out infinite;"></div>
  </div>
  <div class="phantom-module-card-description">
    <div style="width: 100%; height: 16px; background: var(--phantom-border); border-radius: 4px; margin-bottom: 8px; animation: skeleton-pulse 1.5s ease-in-out infinite;"></div>
    <div style="width: 80%; height: 16px; background: var(--phantom-border); border-radius: 4px; animation: skeleton-pulse 1.5s ease-in-out infinite;"></div>
  </div>
</div>

<style>
@keyframes skeleton-pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}
</style>

## En İyi Uygulamalar

1. **Bağlam Sağlayın**: Her zaman neyin yüklendiğini açıklayan metin ekleyin
2. **İlerlemeyi Gösterin**: Mümkün olduğunda sonsuz dönen animasyonlar yerine belirli ilerleme gösterin

## CSS Animasyonu

Dönen animasyonlar CSS kullanarak otomatik olarak çalışır. Animasyon şu şekilde tanımlanır:

```css
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

Boyut ve rengi CSS değişkenleri veya satır içi stiller aracılığıyla özelleştirebilirsiniz.