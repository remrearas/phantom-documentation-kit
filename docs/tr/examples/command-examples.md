# Komut Örnekleri

Komut örnekleri bileşeni, terminal komutlarını uygun ve şık sözdizimi vurgulama (syntax highlighting) özelliğine ek biçimlendirilmiş bir şekilde görüntüler.

## Temel Komut

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python phantom_e2e_modular.py --module deployment_test</span>
</div>

## Çok Satırlı Komut

Birden fazla satıra yayılan uzun komutlar için satır devamı kullanın:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">docker run -it \
    -v $(pwd):/app \
    -e DO_API_TOKEN=$DO_API_TOKEN \
    phantom/e2e-runner</span>
</div>

## Farklı Komut Türleri

Farklı komut türleri için bileşeni özelleştirebilirsiniz:

### Root Kullanıcı
<div class="phantom-command-example">
  <span class="command-prompt">#</span>
  <span class="command-text">apt-get update && apt-get upgrade -y</span>
</div>

### PowerShell
<div class="phantom-command-example">
  <span class="command-prompt">PS&gt;</span>
  <span class="command-text">Get-Process | Where-Object {$_.CPU -gt 100}</span>
</div>

### Özel Komut
<div class="phantom-command-example">
  <span class="command-prompt">user@host:~$</span>
  <span class="command-text">ls -la /var/log/</span>
</div>

## Kullanım İpuçları

1. **Basit Tutun**: Çoğu örnek için temel `$` istemini kullanın
2. **Satır Sonları**: Uzun komutlarda satır devamı için `\` kullanın
3. **Sözdizimi Vurgulama**: Daha karmaşık betikler için sözdizimi vurgulamalı kod bloklarını düşünün
4. **Kopyalama Dostu**: Komut metni kopyalamak için kolayca seçilebilir

## Alternatif: Kod Blokları

Betikler veya çoklu komutlar için standart kod blokları daha uygun olabilir:

```bash
# Sistem paketlerini güncelle
sudo apt-get update
sudo apt-get upgrade -y

# Docker kur
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```