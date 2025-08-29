# Durum Kartları

Durum kartları ölçümler, istatistikler ve temel performans göstergeleri için görsel geri bildirim sağlar.

## Test Durum (Izgara)

Durum kartları ölçüm, istatistik ve temel performans göstergelerini görüntülemek için mükemmeldir. Çeşitli durumlar için farklı renk şemalarını desteklerler.

<div class="phantom-test-status-grid">
  <div class="phantom-test-status-card success">
    <div class="phantom-test-status-value">4</div>
    <div class="phantom-test-status-label">Aktif Modüller</div>
  </div>
  <div class="phantom-test-status-card error">
    <div class="phantom-test-status-value">0</div>
    <div class="phantom-test-status-label">Başarısız Testler</div>
  </div>
  <div class="phantom-test-status-card warning">
    <div class="phantom-test-status-value">2</div>
    <div class="phantom-test-status-label">Uyarılar</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">12</div>
    <div class="phantom-test-status-label">Toplam Testler</div>
  </div>
</div>

### Mevcut Sınıflar

| Sınıf                              | Açıklama                | Renk Şeması                                                     |
|------------------------------------|-------------------------|-----------------------------------------------------------------|
| `phantom-test-status-card success` | Başarılı durumlar       | <span style="color: #22c55e; font-weight: bold;">Yeşil</span>   |
| `phantom-test-status-card error`   | Hata durumları          | <span style="color: #ef4444; font-weight: bold;">Kırmızı</span> |
| `phantom-test-status-card warning` | Uyarı durumları         | <span style="color: #f59e0b; font-weight: bold;">Turuncu</span> |
| `phantom-test-status-card info`    | Bilgilendirici durumlar | <span style="color: #3b82f6; font-weight: bold;">Mavi</span>    |

## Modül Kartları

Modül kartları özellikleri, hizmetleri veya test modüllerini açıklamalar ve meta verilerle sergilemek için tasarlanmıştır.

<div class="phantom-module-card">
  <div class="phantom-module-card-header">
    <span class="phantom-module-card-title">Dağıtım Testi</span>
    <span class="phantom-module-card-duration">~5 dk</span>
  </div>
  <div class="phantom-module-card-description">
    Temel altyapı dağıtımını doğrular ve tüm bileşenlerin erişilebilir olduğundan emin olur.
  </div>
</div>

<div class="phantom-module-card">
  <div class="phantom-module-card-header">
    <span class="phantom-module-card-title">Trafik Akışı Doğrulaması</span>
    <span class="phantom-module-card-duration">~3 dk</span>
  </div>
  <div class="phantom-module-card-description">
    WireGuard tüneli aracılığıyla eşler arasındaki ağ bağlantısını test eder.
  </div>
</div>

## Simgelerle Örnek

Daha iyi görsel iletişim için durum kartlarını Font Awesome simgeleriyle geliştirebilirsiniz:

<div class="phantom-test-status-grid">
  <div class="phantom-test-status-card success">
    <i class="fas fa-check-circle fa-2x mb-2"></i>
    <div class="phantom-test-status-value">4</div>
    <div class="phantom-test-status-label">Geçen Testler</div>
  </div>
  <div class="phantom-test-status-card error">
    <i class="fas fa-times-circle fa-2x mb-2"></i>
    <div class="phantom-test-status-value">0</div>
    <div class="phantom-test-status-label">Başarısız Testler</div>
  </div>
  <div class="phantom-test-status-card warning">
    <i class="fas fa-exclamation-triangle fa-2x mb-2"></i>
    <div class="phantom-test-status-value">2</div>
    <div class="phantom-test-status-label">Uyarılar</div>
  </div>
  <div class="phantom-test-status-card info">
    <i class="fas fa-info-circle fa-2x mb-2"></i>
    <div class="phantom-test-status-value">12</div>
    <div class="phantom-test-status-label">Toplam Testler</div>
  </div>
</div>