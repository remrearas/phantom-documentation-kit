# Uyarı Kutuları

Uyarı kutuları, önemli mesajları uygun görsel stillerle görüntülemek için kullanılır. 
Çeşitli mesaj bağlamları için farklı türleri destekler.

## Başarı Uyarısı

<div class="phantom-alert success">
  <i class="fas fa-check-circle"></i>
  <strong>Başarılı!</strong> Tüm testler başarıyla geçti. Altyapınız hazır.
</div>


## Hata Uyarısı

<div class="phantom-alert error">
  <i class="fas fa-times-circle"></i>
  <strong>Hata:</strong> Bağlantı başarısız oldu. Lütfen API kimlik bilgilerinizi kontrol edin.
</div>


## Uyarı Mesajı

<div class="phantom-alert warning">
  <i class="fas fa-exclamation-triangle"></i>
  <strong>Uyarı:</strong> Bazı testler beklenenden uzun sürüyor. Ağ ayarlarınızı optimize etmeyi düşünün.
</div>


## Bilgi Uyarısı

<div class="phantom-alert info">
  <i class="fas fa-info-circle"></i>
  <strong>Not:</strong> Bu test düzgün çalışmak için en az 2GB kullanılabilir bellek gerektirir.
</div>


## Kullanılabilir Sınıflar

| Sınıf                   | Açıklama                | Renk Şeması                                                     |
|-------------------------|-------------------------|-----------------------------------------------------------------|
| `phantom-alert success` | Başarı mesajları        | <span style="color: #22c55e; font-weight: bold;">Yeşil</span>   |
| `phantom-alert error`   | Hata mesajları          | <span style="color: #ef4444; font-weight: bold;">Kırmızı</span> |
| `phantom-alert warning` | Uyarı mesajları         | <span style="color: #f59e0b; font-weight: bold;">Turuncu</span> |
| `phantom-alert info`    | Bilgilendirme mesajları | <span style="color: #3b82f6; font-weight: bold;">Mavi</span>    |

## Simgesiz Kullanım

Uyarılar daha temiz bir görünüm için simgesiz de kullanılabilir:

<div class="phantom-alert success">
  <strong>Başarılı!</strong> İşlem başarıyla tamamlandı.
</div>

<div class="phantom-alert error">
  <strong>Hata:</strong> Geçersiz yapılandırma tespit edildi.
</div>

<div class="phantom-alert warning">
  <strong>Uyarı:</strong> Bu işlem geri alınamaz.
</div>

<div class="phantom-alert info">
  <strong>Bilgi:</strong> İndirme için yeni sürüm mevcut.
</div>

## Çok Satırlı Uyarılar

Daha uzun mesajlar için uyarılar uygun biçimlendirmeyi korur:

<div class="phantom-alert info">
  <i class="fas fa-info-circle"></i>
  <strong>Kurulum Gereksinimleri:</strong>
  <br><br>
  Kuruluma devam etmeden önce, lütfen şunlardan emin olun:
  <ul style="margin: 0.5rem 0 0 1.5rem;">
    <li>Python 3.8 veya üzeri kurulu</li>
    <li>Docker çalışıyor ve erişilebilir durumda</li>
    <li>En az 4GB boş disk alanınız var</li>
    <li>API tokeniniz yapılandırılmış</li>
  </ul>
</div>

## En İyi Uygulamalar

1. **Simge Kullanımı**: Uyarıları her zaman uygun Font Awesome simgeleri ile eşleştirin
2. **Başlık Formatı**: Uyarı başlıkları için `<strong>` etiketlerini kullanın (Başarılı!, Hata:, Uyarı:, Not:)
3. **Mesaj Uzunluğu**: Mesajları kısa ve işlem odaklı tutun
4. **Bağlamsal Kullanım**: 
   - Başarı: Tamamlanan işlemleri onaylayın
   - Hata: Dikkat gerektiren hataları gösterin
   - Uyarı: Potansiyel sorunları vurgulayın
   - Bilgi: Yardımcı bilgiler sağlayın

## Yaygın Kullanım Senaryoları

### Form Doğrulama
<div class="phantom-alert error">
  <i class="fas fa-times-circle"></i>
  <strong>Doğrulama Hatası:</strong> Lütfen tüm zorunlu alanları doldurun.
</div>

### Sistem Durumu
<div class="phantom-alert success">
  <i class="fas fa-check-circle"></i>
  <strong>Sistem Durumu:</strong> Tüm servisler çalışıyor.
</div>

### Yapılandırma İpuçları
<div class="phantom-alert info">
  <i class="fas fa-info-circle"></i>
  <strong>İpucu:</strong> Zaman aşımı değerini yapılandırma dosyasından özelleştirebilirsiniz.
</div>

### Kullanımdan Kaldırma Bildirimi
<div class="phantom-alert warning">
  <i class="fas fa-exclamation-triangle"></i>
  <strong>Kullanımdan Kaldırma Bildirimi:</strong> Bu özellik 3.0 sürümünde kaldırılacaktır.
</div>