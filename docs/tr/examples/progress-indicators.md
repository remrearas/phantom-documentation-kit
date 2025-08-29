# İlerleme Göstergeleri

İlerleme göstergeleri çok adımlı süreçlerin mevcut durumunu gösterir, iş akışları, kurulum adımları veya test yürütme aşamalarını görselleştirmek için mükemmeldir.

## Aktif İlerleme

Şu anda devam eden bir süreci gösterir:

<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step active"></div>
  <div class="progress-step"></div>
</div>

## Tamamlanmış İlerleme

Tamamen tamamlanmış bir süreci gösterir:

<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
</div>

## İlerleme Durumları

### Mevcut Sınıflar

| Sınıf                     | Açıklama                  | Durum      |
|---------------------------|---------------------------|------------|
| `progress-step`           | Varsayılan/bekleyen durum | Bekleyen   |
| `progress-step completed` | Tamamlanmış adım          | Tamamlandı |
| `progress-step active`    | Şu anda aktif adım        | Aktif      |

## Farklı Adım Sayıları ile Örnekler

### 3 Adımlı Süreç
<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step active"></div>
  <div class="progress-step"></div>
</div>

### 6 Adımlı Süreç
<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step active"></div>
  <div class="progress-step"></div>
  <div class="progress-step"></div>
</div>

### 8 Adımlı Süreç (Uzun)
<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step active"></div>
  <div class="progress-step"></div>
  <div class="progress-step"></div>
</div>

## Kullanım Alanları

İlerleme göstergeleri şunlar için idealdir:

1. **Kurulum Sihirbazları**: Kurulum sürecinin hangi adımının aktif olduğunu göster
2. **Test Yürütme**: Hangi test modülünün şu anda çalıştığını görüntüle
3. **Form Sihirbazları**: Kullanıcıları çok adımlı formlarda yönlendir

## En İyi Uygulamalar

1. **Net Durumlar**: Her zaman bir aktif adımınız olsun (tamamlanmadığı veya başlatılmadığı sürece)
2. **Tepkisel (Responsive)**: Göstergeler mobil cihazlarda uygun şekilde ölçeklenir
3. **Bağlam**: Her adımın neyi temsil ettiğini açıklayan açıklayıcı metinle eşleştirin