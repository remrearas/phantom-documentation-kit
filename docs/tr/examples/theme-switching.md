# Tema Değiştirme

Bileşenlerin bağlı olduğu ve Mkdocs Material stili üzerine uyarlanan tema sistemimiz hem açık hem de koyu temaları destekler. 
Tüm bileşenler CSS değişkenleri kullanarak seçilen temaya otomatik olarak adapte olur.

## CSS Değişkenleri

Tema sistemimiz, tema değiştirildiğinde otomatik olarak güncellenen CSS özel özellikleri (değişkenler) üzerine inşa edilmiştir.

### Temel Değişkenler

```css
:root {
  /* Arka plan renkleri */
  --md-default-bg-color: #ffffff; /* Arka plan rengi */
  --md-default-fg-color: #000000; /* Ön plan/metin rengi */

  /* Vurgu renkleri */
  --md-primary-fg-color: #1976d2; /* Birincil vurgu rengi */
  --md-accent-fg-color: #ff6b35; /* İkincil vurgu rengi */

  /* Özel değişkenler */
  --phantom-bg-secondary: #f5f5f5; /* İkincil arka plan */
  --phantom-border: #e0e0e0; /* Kenarlık rengi */
  --phantom-accent: #1976d2; /* Vurgu rengi */
  --phantom-text-secondary: #666666; /* İkincil metin rengi */
}
```

## Görsel Örnekler

<div class="phantom-grid phantom-grid-2">
  <div style="padding: 1rem; background: var(--md-default-bg-color); border: 2px solid var(--phantom-border); border-radius: 8px;">
    <strong>Varsayılan Arka Plan</strong><br>
    <code>--md-default-bg-color</code>
  </div>
  <div style="padding: 1rem; background: var(--phantom-bg-secondary); border: 2px solid var(--phantom-border); border-radius: 8px;">
    <strong>İkincil Arka Plan</strong><br>
    <code>--phantom-bg-secondary</code>
  </div>
  <div style="padding: 1rem; color: var(--md-primary-fg-color); border: 2px solid var(--md-primary-fg-color); border-radius: 8px;">
    <strong>Birincil Renk</strong><br>
    <code>--md-primary-fg-color</code>
  </div>
  <div style="padding: 1rem; color: var(--phantom-accent); border: 2px solid var(--phantom-accent); border-radius: 8px;">
    <strong>Vurgu Rengi</strong><br>
    <code>--phantom-accent</code>
  </div>
</div>

## Tema Değişikliğine Duyarlı Bileşenler

Tüm özel bileşenlerimiz mevcut temaya otomatik olarak adapte olur:

### Açık Mod Örneği
<div class="phantom-test-status-grid" style="margin-bottom: 20px;">
  <div class="phantom-test-status-card success">
    <div class="phantom-test-status-value">✓</div>
    <div class="phantom-test-status-label">Açık Mod</div>
  </div>
</div>

### Nasıl Çalışır

1. **Temel Değişkenler**: MkDocs Material temel tema değişkenleri sağlar
2. **Özel Değişkenler**: Kendi `--phantom-*` değişkenlerimizle kendi stil yaklaşımımızı uyarlayarak bunları genişletir
3. **Otomatik Değiştirme**: Tema değiştiğinde değişkenler güncellenir

Tüm bileşenlerin nasıl adapte olduğunu görmek için başlıktaki tema değiştirici düğmesini kullanarak açık ve koyu mod arasında geçiş yapmayı deneyin!

## Renk Paleti

### Birincil Renkler
<div class="phantom-grid phantom-grid-auto">
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: var(--md-primary-fg-color); border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Birincil</strong><br>
    <code style="font-size: 0.875em;">--md-primary-fg-color</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: var(--md-accent-fg-color); border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Vurgu</strong><br>
    <code style="font-size: 0.875em;">--md-accent-fg-color</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: var(--phantom-accent); border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Phantom Vurgu</strong><br>
    <code style="font-size: 0.875em;">--phantom-accent</code>
  </div>
</div>

### Durum Renkleri
<div class="phantom-grid phantom-grid-auto">
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: #22c55e; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Başarı</strong><br>
    <code style="font-size: 0.875em;">#22c55e</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: #f59e0b; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Uyarı</strong><br>
    <code style="font-size: 0.875em;">#f59e0b</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: #ef4444; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Hata</strong><br>
    <code style="font-size: 0.875em;">#ef4444</code>
  </div>
  <div style="text-align: center;">
    <div style="width: 100%; height: 80px; background: #3b82f6; border-radius: 8px; margin-bottom: 0.5rem;"></div>
    <strong>Bilgi</strong><br>
    <code style="font-size: 0.875em;">#3b82f6</code>
  </div>
</div>

## Tema Duyarlı Bileşenler Oluşturma

### Örnek: Özel Kart

```css
.custom-card {
  background: var(--phantom-bg-secondary);
  border: 1px solid var(--phantom-border);
  color: var(--md-default-fg-color);
  padding: 1rem;
  border-radius: 8px;
}

.custom-card:hover {
  border-color: var(--phantom-accent);
}
```

<div class="custom-card" style="background: var(--phantom-bg-secondary); border: 1px solid var(--phantom-border); color: var(--md-default-fg-color); padding: 1rem; border-radius: 8px;">
  Bu kart CSS değişkenleri kullanarak mevcut temaya otomatik olarak adapte olur.
</div>

## Koyu Mod Düşünceleri

Her iki tema için tasarım yaparken şunları düşünün:

1. **Kontrast Oranları**: Metinlerin her iki modda da okunabilir kaldığından emin olun
2. **Renk Anlamları**: Durum renkleri her iki temada da ayırt edilebilir olmalı
3. **Gölgeler**: `box-shadow` kullanımını sınırlayın çünkü koyu modda iyi çalışmayabilir
4. **Resimler**: Gerektiğinde temaya özel resimler sağlamayı düşünün

## Temanızı Test Etme

### Kontrast Kontrolcüsü
<div class="phantom-grid phantom-grid-2">
  <div style="background: var(--md-default-bg-color); color: var(--md-default-fg-color); padding: 20px; border: 2px solid var(--phantom-border); border-radius: 8px;">
    <strong>Varsayılan Arka Planda Varsayılan Metin</strong><br>
    Bu metin hem açık hem de koyu modlarda net okunabilir olmalıdır.
  </div>
  <div style="background: var(--phantom-bg-secondary); color: var(--phantom-text-secondary); padding: 20px; border: 2px solid var(--phantom-border); border-radius: 8px;">
    <strong>İkincil Arka Planda İkincil Metin</strong><br>
    Bu kombinasyon daha az önemli içerik için kullanılır.
  </div>
</div>

## Tema Değiştiricinin Konumu

Tema değiştirici düğmesi başlık navigasyon çubuğunda bulunur. Açık ve koyu mod arasında geçiş yapmak için güneş/ay simgesini arayın.

## En İyi Uygulamalar

1. **CSS Değişkenleri Kullanın**: Sabit kodlu renkler yerine her zaman tema değişkenlerini kullanın
2. **Her İki Modu Test Edin**: İçeriğinizi hem açık hem de koyu temalarda kontrol edin
3. **Semantik Renkler**: Görünüm değil amacı açıklayan anlamlı değişken adları kullanın
4. **Yedek Değerler**: Gerekirse eski tarayıcılar için yedek renkler sağlayın
5. **Medya Sorguları**: `prefers-color-scheme` ile kullanıcının sistem tema tercihine saygı gösterin