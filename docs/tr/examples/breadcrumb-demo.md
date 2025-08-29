# Breadcrumb Navigasyon Demosu

## Canlı Breadcrumb Demosu

Aşağıda breadcrumb navigasyonunun farklı iç içe geçme seviyelerinde nasıl görüneceğini görebilirsiniz:

### Seviye 1 Navigasyon
<nav class="phantom-breadcrumbs" aria-label="Breadcrumb navigation">
  <div class="phantom-breadcrumbs-wrapper">
    <ol itemscope itemtype="https://schema.org/BreadcrumbList">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="../../" itemprop="item"><span itemprop="name">Ana Sayfa</span></a>
        <meta itemprop="position" content="1" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span class="active" itemprop="item"><span itemprop="name">Başlangıç</span></span>
        <meta itemprop="position" content="2" />
      </li>
    </ol>
  </div>
</nav>

### Seviye 3 Navigasyon (Orta Yol)
<nav class="phantom-breadcrumbs" aria-label="Breadcrumb navigation">
  <div class="phantom-breadcrumbs-wrapper">
    <ol itemscope itemtype="https://schema.org/BreadcrumbList">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="../../" itemprop="item"><span itemprop="name">Ana Sayfa</span></a>
        <meta itemprop="position" content="1" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Stil Örnekleri</span></a>
        <meta itemprop="position" content="2" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Yapılandırma</span></a>
        <meta itemprop="position" content="3" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span class="active" itemprop="item"><span itemprop="name">Gelişmiş Ayarlar</span></span>
        <meta itemprop="position" content="4" />
      </li>
    </ol>
  </div>
</nav>

### Seviye 5 Navigasyon (Uzun Yol - Kaydırmayı Gösterir)
<nav class="phantom-breadcrumbs" aria-label="Breadcrumb navigation">
  <div class="phantom-breadcrumbs-wrapper">
    <ol itemscope itemtype="https://schema.org/BreadcrumbList">
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="../../" itemprop="item"><span itemprop="name">Ana Sayfa</span></a>
        <meta itemprop="position" content="1" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Stil Örnekleri</span></a>
        <meta itemprop="position" content="2" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Başlangıç Kılavuzu</span></a>
        <meta itemprop="position" content="3" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Yapılandırma Yönetimi</span></a>
        <meta itemprop="position" content="4" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="#" itemprop="item"><span itemprop="name">Gelişmiş Sistem Ayarları</span></a>
        <meta itemprop="position" content="5" />
      </li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span class="active" itemprop="item"><span itemprop="name">Özel Bileşen Yapılandırması</span></span>
        <meta itemprop="position" content="6" />
      </li>
    </ol>
  </div>
</nav>

## Gösterilen Özellikler

### Responsive Davranış
- **Masaüstü**: Hover efektleri ve yumuşak animasyonlarla tam breadcrumb yolları
- **Tablet**: Okunabilirliği koruyarak hafif sıkıştırılmış breadcrumb'lar
- **Mobil**: Gerektiğinde yatay kaydırma ile kompakt breadcrumb'lar

### Görsel Göstergeler
- **Geçiş Göstergeleri**: İçeriğin kaydırılabilir olduğunu gösterir (pencerenizi yeniden boyutlandırmayı deneyin)
- **Hover Efektleri**: Etkileşimli bağlantı animasyonları ve alt çizgi efektleri
- **Metin Kısaltma**: Alan sınırlı olduğunda uzun sayfa başlıkları üç nokta ile kısaltılır

### Erişilebilirlik Özellikleri
- **Schema.org**: Daha iyi SEO ve makine okunabilirliği için yapılandırılmış veri
- **Klavye Navigasyonu**: Tam klavye erişilebilirlik desteği
- **Odak Yönetimi**: Net odak göstergeleri ve mantıklı sekme sırası

## Teknik Uygulama

Breadcrumb sistemi otomatik olarak:

- Navigasyon yolu uzun olduğunda mevcut sayfayı göstermek için kayar
- Kaydırılabilir içerik için gradyan göstergeleri görüntüler
- Uzun sayfa başlıklarını üç nokta ile kısaltır
- Uygun ARIA etiketleri ve yapılandırılmış veri ile erişilebilirliği korur
- Tepkisel (Responsive) tasarımla farklı ekran boyutlarına adapte olur

## Test Talimatları

1. **Pencereyi Yeniden Boyutlandır**: Yatay kaydırmayı çalışır halde görmek için tarayıcı pencerenizi daraltın
2. **Hover Efektleri**: Etkileşimli animasyonları görmek için breadcrumb bağlantılarının üzerine gelmeyi deneyin  
3. **Mobil Görünüm**: Mobil davranışı test etmek için tepkisel (responsive) tasarım modunu kullanın
4. **Erişilebilirlik**: Klavye erişilebilirliğini test etmek için sekme navigasyonunu kullanın

Breadcrumb bileşeni otomatik olarak oluşturulur ve manuel yapılandırma gerektirmez.