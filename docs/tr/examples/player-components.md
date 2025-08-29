---
extra_javascript:
  - assets/javascripts/asciinema-player.js
  - assets/javascripts/youtube-player.js
---
# Oynatıcı Bileşenleri

!!! important "Gerekli Yapılandırma"
    Markdown dosyalarınızda oynatıcı bileşenlerini kullanmak için, belgenizin başına aşağıdaki YAML ön maddesini **mutlaka** eklemelisiniz:
    ```yaml
    ---
    extra_javascript:
      - assets/javascripts/asciinema-player.js
      - assets/javascripts/youtube-player.js
    ---
    ```
    Bu yapılandırma olmadan oynatıcılar düzgün render edilmez.

## Asciinema Player

### Basit Embed

<div class="asciinema-player" data-cast-file="recordings/build_docker_remote.cast"></div>

**Not:** Oynatıcı, cast dosyası mevcut olduğunda terminal kaydını yükleyecektir.

### Başlıklı Tam Konteyner

<div class="asciinema-player-container">
    <div class="asciinema-player-header">
        <h3>Phantom Kurulum Süreci</h3>
        <span class="asciinema-player-info">Kurulum Demosu</span>
    </div>
    <div class="asciinema-player-wrapper">
        <div class="asciinema-player" 
             data-cast-file="recordings/build_docker_remote.cast"
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

### Mevcut Seçenekler

| Seçenek          | Açıklama                 | Değerler                                            |
|------------------|--------------------------|-----------------------------------------------------|
| `data-cols`      | Terminal sütunları       | Varsayılan: 100                                     |
| `data-rows`      | Terminal satırları       | Varsayılan: 30                                      |
| `data-autoplay`  | Yüklemede otomatik oynat | `true` / `false`                                    |
| `data-loop`      | Döngü oynatım            | `true` / `false`                                    |
| `data-speed`     | Oynatım hızı             | `0.5` - `3.0`                                       |
| `data-theme`     | Renk teması              | `solarized-dark`, `solarized-light`, `monokai`, vb. |
| `data-font-size` | Yazı tipi boyutu         | `small`, `medium`, `large`                          |

## YouTube Oynatıcı

### Basit Embed

<div class="youtube-player" data-video-id="eV6lTEY95yY"></div>

**Not:** `VIDEO_ID_HERE` yerine gerçek YouTube video ID'nizi yazın.

### Başlıklı Tam Kapsayıcı

<div class="youtube-player-container">
    <div class="youtube-player-header">
        <h3>Phantom E2E Eğitimi</h3>
        <span class="youtube-player-info">Başlangıç Kılavuzu</span>
    </div>
    <div class="youtube-player-wrapper">
        <div class="youtube-player" 
             data-video-id="eV6lTEY95yY"
             data-autoplay="false"
             data-controls="true"
             data-loop="false"
             data-mute="false"
             data-rel="false"
             data-modestbranding="true">
        </div>
    </div>
</div>

### Mevcut Seçenekler

| Seçenek               | Açıklama                      | Değerler         |
|-----------------------|-------------------------------|------------------|
| `data-video-id`       | YouTube video ID'si           | **Gerekli**      |
| `data-autoplay`       | Videoyu otomatik oynat        | `true` / `false` |
| `data-controls`       | Oynatıcı kontrollerini göster | `true` / `false` |
| `data-loop`           | Videoyu döngüye al            | `true` / `false` |
| `data-mute`           | Varsayılan olarak sessize al  | `true` / `false` |
| `data-rel`            | İlgili videoları göster       | `true` / `false` |
| `data-modestbranding` | Minimal YouTube markalaması   | `true` / `false` |

## Oynatıcılar için Yükleme Durumları

Oynatıcılar yüklenirken bir spinner görüntülenir:

<div style="position: relative; height: 300px; background: var(--phantom-code-bg); border-radius: 8px; display: flex; align-items: center; justify-content: center;">
  <div class="player-spinner">
    <div class="spinner-inner"></div>
  </div>
</div>

**CSS Animasyonu:**
Spinner CSS animasyonları kullanarak otomatik olarak döner. Boyut ve rengi CSS değişkenleri aracılığıyla özelleştirebilirsiniz.

## En İyi Uygulamalar

1. **Dosya Boyutu**: Hızlı yükleme için Asciinema kayıtlarını 1MB altında tutun
2. **Boş Zaman**: Kayıtlardaki uzun duraklamaları atlamak için `data-speed` kullanın
3. **Temalar**: Dokümantasyon stilinizle uyumlu temalar seçin
4. **Yedekler**: Erişilebilirlik için metin alternatifleri sağlayın
5. **Barındırma**: Daha iyi performans için .cast dosyalarını yerel olarak barındırın

## Terminal Oturumlarını Kaydetme

Kendi Asciinema kayıtlarınızı oluşturmak için:

```bash
# asciinema kur
pip install asciinema

# Kayıt başlat
asciinema rec demo.cast

# Belirli ayarlarla kayıt et
asciinema rec -i 2 -t "Demo Başlığı" demo.cast

# Yerel olarak oynat
asciinema play demo.cast
```

## YouTube Entegrasyon İpuçları

1. **Gizlilik**: İlgisiz videoları göstermemek için `data-rel="false"` kullanın
2. **Markalama**: Daha temiz görünüm için `data-modestbranding="true"` kullanın
3. **Otomatik Oynatım**: Daha iyi kullanıcı deneyimi için otomatik oynatımdan kaçının
4. **Sessize Alma**: Otomatik oynatım gerekliyse sessize almayı düşünün
5. **Tepkisel (Responsive)**: Oynatıcılar otomatik olarak kapsayıcı genişliğine ölçeklenir