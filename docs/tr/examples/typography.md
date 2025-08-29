# Tipografi

Dokümantasyonumuz daha iyi görsel hiyerarşi için özel başlık yazı tipi ve teknik içerik için monospace yazı tipi kullanır.

## Yazı Tipi Bilgileri

### Başlık Yazı Tipi
- **Yazı Tipi Ailesi**: Orbitron (CSS değişkeni: `--phantom-font-heading`)
- **Google Fonts**: [fonts.google.com/specimen/Orbitron](https://fonts.google.com/specimen/Orbitron)
- **Yerel Dosyalar**: `assets/fonts/orbitron-{400,600,800}.ttf`
- **Kullanım**: Özel bileşenlerdeki başlıklar ve vurgulu metinler
- **Amaç**: Fütüristik, teknoloji odaklı görünüm

### Kod ve Terminal Yazı Tipi
- **Yazı Tipi Ailesi**: Share Tech Mono (CSS değişkeni: `--phantom-font-mono`)
- **Google Fonts**: [fonts.google.com/specimen/Share+Tech+Mono](https://fonts.google.com/specimen/Share+Tech+Mono)
- **Yerel Dosya**: `assets/fonts/share-tech-mono-400.ttf`
- **Kullanım**: Kod blokları, terminal komutları ve teknik içerik
- **Amaç**: Retro terminal estetiği, mükemmel karakter hizalaması

### Material Varsayılan Yazı Tipleri
- **Gövde Metni**: Roboto (MkDocs Material varsayılanı)
- **Kod Blokları**: Roboto Mono (MkDocs Material varsayılanı)
- **Kullanım**: Genel dokümantasyon içeriği
- **Amaç**: Google Material Design ile uyumlu, modern görünüm

## Başlıklar

# H1: Ana Sayfa Başlığı
## H2: Bölüm Başlığı
### H3: Alt Bölüm Başlığı
#### H4: Bileşen Başlığı
##### H5: Özellik Başlığı
###### H6: Küçük Başlık

## Metin Biçimlendirme

Bu, normal gövde metni stilini gösteren bir paragraftır. Monospace yazı tipi, okunabilirliği korurken dokümantasyona teknik bir his verir.

**Kalın metin** vurgu için  
*İtalik metin* hafif vurgu için  
***Kalın ve italik*** güçlü vurgu için  
~~Üstü çizili metin~~ kullanımdan kaldırılan içerik için  
`Satır içi kod` kod referansları için

## Bağlantılar

- [Harici Bağlantı](https://github.com/remrearas) - Aynı pencerede açılır
- [Dahili Bağlantı](#başlıklar) - Bölüme yumuşak kaydırma
- [E-posta Bağlantısı](mailto:emre@aras.tc) - E-posta istemcisini açar
- `https://www.aras.tc` - Otomatik bağlantılı URL

## Listeler

### Sırasız Listeler

- İlk seviye öğe
- Başka bir ilk seviye öğe
  - İkinci seviye öğe
  - Başka bir ikinci seviye öğe
    - Üçüncü seviye öğe
    - Başka bir üçüncü seviye öğe
- İlk seviyeye geri dön

### Sıralı Listeler

1. İlk adım
2. İkinci adım
   1. Alt adım A
   2. Alt adım B
      1. Detay 1
      2. Detay 2
3. Üçüncü adım

### Karışık Listeler

1. **Ortamı Kur**
   - Python 3.8+ kur
   - Docker kur
   - Depoyu klonla
2. **Uygulamayı Yapılandır**
   - `.env.example` dosyasını `.env` olarak kopyala
   - Yapılandırma değerlerini güncelle:
     - API tokenları
     - Veritabanı kimlik bilgileri
     - Hizmet uç noktaları
3. **Testleri Çalıştır**
   - Birim testleri: `pytest tests/unit`
   - Entegrasyon testleri: `pytest tests/integration`

## Blok Alıntılar

> Bu bir blok alıntıdır. Önemli bilgileri vurgulamak veya harici kaynaklardan alıntılar için kullanışlıdır.

> **Not:** Çok satırlı blok alıntılar biçimlendirilmiş metin içerebilir.
> 
> Hatta listeler bile içerebilirler:
> 
> - Öğe bir
> - Öğe iki
> - Öğe üç

> > İç içe blok alıntılar da daha derin bağlam seviyeleri için desteklenir.

## Yatay Çizgiler

Ana bölümleri ayırmak için yatay çizgiler kullanın:

---

Yukarıda ve aşağıda bunun gibi.

---

## Tanım Listeleri

**Terim 1**
:   Terim 1 için tanım. Bu, gerekirse birden fazla satıra yayılabilen daha uzun bir açıklama olabilir.

**Terim 2**
:   Terim 2 için tanım
:   Birden fazla tanıma sahip olabilir

**API Token**
:   API'ye yapılan istekleri doğrulamak için kullanılan benzersiz tanımlayıcı. Güvenli tutulmalı ve asla sürüm kontrolüne commitlenmemelidir.

**Ortam Değişkeni**
:   Bir bilgisayarda çalışan süreçlerin davranış şeklini etkileyebilen dinamik bir değer. Yaygın olarak yapılandırma için kullanılır.

## Tablolar

### Temel Tablo

| Başlık 1 | Başlık 2 | Başlık 3 |
|----------|----------|----------|
| Hücre 1  | Hücre 2  | Hücre 3  |
| Hücre 4  | Hücre 5  | Hücre 6  |

### Hizalanmış Tablo

| Sola Hizalı                           | Merkez Hizalı  |   Sağa Hizalı |
|:--------------------------------------|:--------------:|--------------:|
| Sol                                   |     Merkez     |           Sağ |
| 123                                   |      456       |           789 |
| Hizalamayı gösteren uzun metin        |    Merkezde    |           Sağ |

### Karmaşık Tablo

| Özellik       | Ücretsiz  |     Pro     |   Kurumsal   |
|---------------|:---------:|:-----------:|:------------:|
| **Kullanıcı** |     5     |     50      |   Sınırsız   |
| **Depolama**  |   10 GB   |   100 GB    |    1 TB+     |
| **Destek**    | Topluluk  |   E-posta   | 7/24 Telefon |
| **API Çağrı** | 1,000/gün | 100,000/gün |   Sınırsız   |
| **Fiyat**     |    0₺     |   490₺/ay   | Bize Ulaşın  |

## Özel Karakterler

- Telif hakkı: © 2024 Phantom
- Marka: Phantom™
- Tescilli: Phantom®
- Oklar: → ← ↑ ↓ ↔
- Matematik: ± × ÷ ≈ ≠ ≤ ≥
- Çeşitli: • … — –


## Vurgu Desenleri

### Bunu Yapın
- İlk bahsedildiğinde önemli terimler için **kalın** kullanın
- `Satır içi kod` şunlar için kullanın:
  - Dosya adları: `config.yaml`
  - Komutlar: `docker-compose up`
  - Fonksiyon adları: `calculate_total()`
  - Değişken adları: `API_TOKEN`

### Bunu Yapmayın
- Vurgu için BÜYÜK HARF kullanmayın
- ***Kalın italik*** kombinasyonlarını aşırı kullanmayın
- Metnin altını çizmeyin (bağlantılar için ayrılmış)