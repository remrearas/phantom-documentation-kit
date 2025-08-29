---
extra_javascript:
  - assets/javascripts/asciinema-player.js

---
# Phantom Documentation Kit

Bu kit, `Phantom Wireguard` yazılımının dokümantasyon sürecinde kolay ve benzersiz bir dokümantasyon deneyimi sağlamak için geliştirildi.
MkDocs kütüphanesinin endüstriyel gücü ve esnekliği, ihtiyaçlarımızla birleştiğinde `Phantom Documentation Kit` ortaya çıktı.
Dokümantasyon sürecinde ihtiyacımız olan özellikler ve bileşenler geliştirildi ve bu çatı altında toplandı.  


## Hızlı Başlangıç

### Ön Hazırlık

#### Python Paketleri
Gerekli Python paketlerini yüklemek için proje dizininde aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

#### Node.js Kurulumu
Phantom Documentation Kit içindeki `Vendor Builder` ve  `Image Optimizer` araçlarını kullanılabilmek için
**Node.js 22 veya üzeri** sürüm gereklidir. Bu araçlarla ilgili daha detaylı bilgi sahibi olmak için 
[Araçlar](./tools/index.md) dökümanına göz atabilirsiniz.

- Mevcut sürümünüzü kontrol edin: `node --version`
- Node.js'i indirmek için: [https://nodejs.org/en/download](https://nodejs.org/en/download)

### 1. Geliştirme Sunucusu (serve.py)

Dokümantasyonunuzu yerel olarak görüntülemek ve geliştirmek için:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python serve.py</span>
</div>

Tarayıcınızda http://localhost:8000 adresini açın.

### 2. Dokümantasyon Derleme (build.py)

Production-ready statik HTML oluşturmak için:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python build.py</span>
</div>

Derlenmiş dosyalar `outputs/site/` dizininde oluşturulur.

## Yapılandırma (config.json)

Proje ayarlarını özelleştirmek için `config.json` dosyasını düzenleyin:

```json
{
  "paths": {
    "output_dir": "outputs/www",
    "vendor_dir": "overrides/assets/vendor",
    "vendor_builder_dir": "tools/vendor-builder"
  },
  "build": {
    "clean_before_build": true,
    "check_vendor_dependencies": true
  },
  "serve": {
    "port": 8000,
    "host": "localhost",
    "check_vendor_dependencies": true
  },
  "docker": {
    "image_name": "phantom-docs-kit",
    "build_tag": "latest",
    "container_prefix": "phantom-docs"
  },
  "logging": {
    "enabled": true,
    "console_level": "INFO",
    "file_level": "DEBUG",
    "log_directory": "logs",
    "max_file_size": "10MB",
    "backup_count": 5,
    "timestamp_format": "%Y-%m-%d %H:%M:%S",
    "log_filename_pattern": "phantom-{mode}-{date}-{time}.log"
  }
}
```

## Gelişmiş Kullanım

### Docker ile Çalıştırma

Aşağıdaki komutları uygulayarak Docker üzerinde rahatlıkla çalışabilirsiniz.

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python serve.py --docker</span>
</div>

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python build.py --docker</span>
</div>

### Docker ile Uzak Ortamda Çalıştırma

Docker ile uzak ortamda çalışmak isterseniz, dosyaların senkronizasyonu ve port yönlendirmeleri için Mutagen
kurulumu zorunludur. Mutagen sayesinde, sanki yerel ortamınızda çalışıyormuş gibi uzak Docker ortamında çalışmanız
mümkün olmaktadır.

Mutagen kurulumu için Mac cihazınızda aşağıdaki komutu çalıştırın:

```bash
brew install mutagen-io/mutagen/mutagen
```

Kurulum tamamlandıktan sonra, Terminal üzerinden aşağıdaki komutu çalıştırarak kurulumun durumunu doğrulayın:

```bash
mutagen version
```

Docker SDK ve Mutagen, uzak sunucunuzu `DOCKER_HOST` çevre değişkeniyle tanıyacaktır. 

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">DOCKER_HOST=ssh://user@remote-server</span>
</div>

SSH erişiminin herhangi bir engele takılmadan geliştirme cihazınız ve Docker yüklü olan uzak sunucunuz arasında yapılması gerekmektedir.

Örnek adımlar aşağıda bulunmaktadır:

SSH anahtarınız yoksa, yerel makinenizde oluşturun:

```bash
ssh-keygen -t ed25519 -C "phantom-docs"
```

Public anahtarı uzak sunucuya kopyalayın:
```bash
ssh-copy-id user@remote-server
```

Bağlantınızı test edin:

```bash
ssh user@remote-server docker info
```

Bu aşamaya kadar başarılı bir şekilde geldiyseniz, `DOCKER_HOST` çevre değişkenini uzak sunucunuzun bilgileriyle
tanımlayın:

```bash
export DOCKER_HOST=ssh://user@remote-server
```

Ardından, proje dizininde olduğunuzdan emin olun ve `serve` komutunu çalıştırın:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python serve.py --docker</span>
</div>
<div class="asciinema-player-container">
    <div class="asciinema-player-header">
        <h3>Phantom Documentation Kit</h3>
        <span class="asciinema-player-info">Terminal Kaydı</span>
    </div>
    <div class="asciinema-player-wrapper">
        <div class="asciinema-player" 
             data-cast-file="recordings/serve_docker_remote_firstRun.cast"
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

`build` için aşağıdaki komutu çalıştırın:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python build.py --docker</span>
</div>
<div class="asciinema-player-container">
    <div class="asciinema-player-header">
        <h3>Phantom Documentation Kit</h3>
        <span class="asciinema-player-info">Terminal Kaydı</span>
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

Dikkat edilmesi gereken detaylardan biri; Docker ile uzak ortamda derleme yaptığınızda, derleme çıktıları
çıktı dizininde `phantom-docs-build-docker-remote-{timestamp}.tar.gz` formatında arşivlenerek kaydedilir.

### Komut Parametreleri

| Parametre   | Açıklama                         |
|-------------|----------------------------------|
| `--docker`  | Docker container içinde çalıştır |
| `--verbose` | Detaylı log çıktısı              |
| `--quiet`   | Minimal log çıktısı              |

## Sistem Gereksinimleri

- Python 3.8+
- Node.js 22+ 
- Docker (opsiyonel)

## İlk Çalıştırma

İlk kez çalıştırdığınızda, sistem otomatik olarak:

- Eksik bağımlılıkları kontrol eder
- Vendor dosyalarını derler (JavaScript/CSS)
- MkDocs sunucusunu başlatır
