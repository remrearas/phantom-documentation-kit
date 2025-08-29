---
extra_javascript:
  - assets/javascripts/chart.js
---

# Grafik Örnekleri (Chart.js)

Bu sayfa, Phantom Documentation Kit içinde Chart.js kullanımını göstermektedir. 
Bu sayfayı inceleyerek grafik uygulamalarını ve canlı kod örneklerini görebilirsiniz.

!!! important "Gerekli Yapılandırma"
    Markdown dosyalarınızda Chart.js kullanmak için, belgenizin başına aşağıdaki YAML ön maddesini **mutlaka** eklemelisiniz:
    ```yaml
    ---
    extra_javascript:
      - assets/javascripts/chart.js
    ---
    ```
    Bu yapılandırma olmadan grafikler düzgün render edilmez.

## Çizgi Grafiği

Aylık veri eğilimlerini gösteren basit tepkisel (responsive) çizgi grafiği.

<div class="chart-container" 
     data-chart-title="Aylık Satış Trendi"
     data-chart-config='{
       "type": "line",
       "data": {
         "labels": ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"],
         "datasets": [{
           "label": "2024 Satışları",
           "data": [65, 59, 80, 81, 56, 95],
           "borderColor": "#3b82f6",
           "backgroundColor": "rgba(59, 130, 246, 0.1)",
           "borderWidth": 2,
           "tension": 0.4,
           "pointRadius": 4,
           "pointHoverRadius": 6,
           "pointBackgroundColor": "#3b82f6",
           "pointBorderColor": "#fff",
           "pointBorderWidth": 2
         }]
       },
       "options": {
         "responsive": true,
         "maintainAspectRatio": false,
         "aspectRatio": 2,
         "plugins": {
           "legend": {
             "display": true,
             "position": "top"
           },
           "tooltip": {
             "mode": "index",
             "intersect": false
           }
         },
         "scales": {
           "y": {
             "beginAtZero": true,
             "grid": {
               "drawBorder": false
             }
           },
           "x": {
             "grid": {
               "display": false
             }
           }
         }
       }
     }'></div>

## Bar Grafiği

Kategori karşılaştırmalarını gösteren tepkisel (responsive) bar grafiği.

<div class="chart-container" 
     data-chart-title="Ürün Kategorileri Performansı"
     data-chart-config='{
       "type": "bar",
       "data": {
         "labels": ["Elektronik", "Giyim", "Gıda", "Kitap", "Spor", "Ev"],
         "datasets": [{
           "label": "Gelir (₺k)",
           "data": [120, 95, 80, 45, 65, 110],
           "backgroundColor": [
             "rgba(239, 68, 68, 0.8)",
             "rgba(245, 158, 11, 0.8)",
             "rgba(34, 197, 94, 0.8)",
             "rgba(59, 130, 246, 0.8)",
             "rgba(168, 85, 247, 0.8)",
             "rgba(236, 72, 153, 0.8)"
           ],
           "borderColor": [
             "#ef4444",
             "#f59e0b",
             "#22c55e",
             "#3b82f6",
             "#a855f7",
             "#ec4899"
           ],
           "borderWidth": 2,
           "borderRadius": 6
         }]
       },
       "options": {
         "responsive": true,
         "maintainAspectRatio": false,
         "aspectRatio": 2,
         "plugins": {
           "legend": {
             "display": true,
             "position": "top"
           },
           "tooltip": {
             "mode": "index",
             "intersect": false
           }
         },
         "scales": {
           "y": {
             "beginAtZero": true,
             "title": {
               "display": true,
               "text": "Gelir (₺k)"
             }
           },
           "x": {
             "title": {
               "display": true,
               "text": "Kategoriler"
             }
           }
         }
       }
     }'></div>

## Çoklu Eksen (Çizgi ve Bar) Grafiği

Farklı metrikleri gösteren çoklu y-eksenli kombinasyon grafiği.

<div class="chart-container" 
     data-chart-title="Website Analitik Genel Bakış"
     data-chart-config='{
       "type": "bar",
       "data": {
         "labels": ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"],
         "datasets": [
           {
             "label": "Sayfa Görüntüleme",
             "data": [2500, 3200, 2800, 3500, 4200, 3800, 3000],
             "backgroundColor": "rgba(59, 130, 246, 0.6)",
             "borderColor": "#3b82f6",
             "borderWidth": 2,
             "borderRadius": 4,
             "yAxisID": "y"
           },
           {
             "label": "Dönüşüm Oranı (%)",
             "data": [2.5, 3.2, 2.8, 3.5, 4.2, 3.8, 3.0],
             "type": "line",
             "borderColor": "#22c55e",
             "backgroundColor": "rgba(34, 197, 94, 0.1)",
             "borderWidth": 3,
             "pointRadius": 5,
             "pointHoverRadius": 7,
             "pointBackgroundColor": "#22c55e",
             "pointBorderColor": "#fff",
             "pointBorderWidth": 2,
             "tension": 0.3,
             "yAxisID": "y1"
           }
         ]
       },
       "options": {
         "responsive": true,
         "maintainAspectRatio": false,
         "aspectRatio": 2,
         "interaction": {
           "mode": "index",
           "intersect": false
         },
         "plugins": {
           "legend": {
             "display": true,
             "position": "top"
           },
           "tooltip": {
             "mode": "index",
             "intersect": false
           }
         },
         "scales": {
           "x": {
             "title": {
               "display": true,
               "text": "Haftanın Günleri"
             }
           },
           "y": {
             "type": "linear",
             "display": true,
             "position": "left",
             "title": {
               "display": true,
               "text": "Sayfa Görüntüleme"
             },
             "beginAtZero": true
           },
           "y1": {
             "type": "linear",
             "display": true,
             "position": "right",
             "title": {
               "display": true,
               "text": "Dönüşüm Oranı (%)"
             },
             "beginAtZero": true,
             "grid": {
               "drawOnChartArea": false
             }
           }
         }
       }
     }'></div>

## Pasta Grafiği

Veri dağılımını gösteren tepkisel (responsive) pasta grafiği.

<div class="chart-container" 
     data-chart-title="Pazar Payı Dağılımı"
     data-chart-config='{
       "type": "pie",
       "data": {
         "labels": ["Ürün A", "Ürün B", "Ürün C", "Ürün D", "Ürün E"],
         "datasets": [{
           "data": [30, 25, 20, 15, 10],
           "backgroundColor": [
             "rgba(239, 68, 68, 0.8)",
             "rgba(59, 130, 246, 0.8)",
             "rgba(34, 197, 94, 0.8)",
             "rgba(245, 158, 11, 0.8)",
             "rgba(168, 85, 247, 0.8)"
           ],
           "borderColor": [
             "#ef4444",
             "#3b82f6",
             "#22c55e",
             "#f59e0b",
             "#a855f7"
           ],
           "borderWidth": 2
         }]
       },
       "options": {
         "responsive": true,
         "maintainAspectRatio": false,
         "aspectRatio": 1.5,
         "plugins": {
           "legend": {
             "display": true,
             "position": "right"
           },
           "tooltip": {
             "enabled": true
           }
         }
       }
     }'></div>

## Halka Grafiği

Toplam değeri merkez metniyle gösteren tepkisel (responsive) halka grafiği.

<div class="chart-container" 
     data-chart-title="Bütçe Tahsisi"
     data-chart-config='{
       "type": "doughnut",
       "data": {
         "labels": ["Geliştirme", "Pazarlama", "Operasyon", "Destek", "Ar-Ge"],
         "datasets": [{
           "data": [35, 20, 25, 10, 10],
           "backgroundColor": [
             "rgba(59, 130, 246, 0.8)",
             "rgba(34, 197, 94, 0.8)",
             "rgba(245, 158, 11, 0.8)",
             "rgba(239, 68, 68, 0.8)",
             "rgba(168, 85, 247, 0.8)"
           ],
           "borderColor": [
             "#3b82f6",
             "#22c55e",
             "#f59e0b",
             "#ef4444",
             "#a855f7"
           ],
           "borderWidth": 2
         }]
       },
       "options": {
         "responsive": true,
         "maintainAspectRatio": false,
         "aspectRatio": 1.5,
         "cutout": "60%",
         "plugins": {
           "legend": {
             "display": true,
             "position": "right"
           },
           "tooltip": {
             "enabled": true
           }
         }
       }
     }'></div>

## Chart.js Uygulaması

Phantom Documentation Kit içindeki Chart.js uygulaması `overrides/assets/javascripts/chart.js` dosyası aracılığıyla sağlanır. Bu uygulama aşağıdaki özellikleri sunar:

### Nasıl Çalışır

1. **Otomatik Başlatma**: Sayfa yüklendiğinde, tüm `.chart-container` öğeleri otomatik olarak taranır ve grafikler oluşturulur.

2. **JSON Tabanlı Yapılandırma**: Grafikler JSON formatında `data-chart-config` özniteliği aracılığıyla yapılandırılır. Bu yaklaşım:
    - JavaScript kodu yazmadan grafik oluşturmayı sağlar
    - Markdown dosyaları içinde temiz ve okunabilir yapı sunar
    - Güvenli yapılandırma yöntemi sağlar

3. **Tema Desteği**: Uygulama Material for MkDocs tema değişikliklerini otomatik olarak algılar:
    - Açık/koyu tema geçişleri sırasında grafikler otomatik olarak güncellenir
    - Metin renkleri, grid çizgileri ve arka planlar tema uyumlu hale gelir
    - Tema değişiklikleri `MutationObserver` API kullanılarak izlenir

4. **Tepkisel (responsive) Tasarım**: Tüm grafikler için varsayılan ayarlar:
    - `responsive: true` - Kapsayıcı boyutuna göre otomatik ölçekleme
    - `maintainAspectRatio: false` - Esnek en-boy oranı
    - `aspectRatio: 2` - Varsayılan 2:1 en-boy oranı

### Kullanılan Teknolojiler

- **Chart.js v4.4.7**: Vendor builder aracılığıyla optimize edilmiş sürüm
- **Lazy Loading**: Chart.js yalnızca grafik içeren sayfalarda yüklenir
- **Tema Gözlemcisi**: Gerçek zamanlı tema değişikliği izleme
- **JSON Parse**: Güvenli yapılandırma okuma

### Grafik Oluşturma Süreci

```
1. HTML öğesi tarama → .chart-container
2. JSON config okuma → data-chart-config özniteliği
3. Tema renklerini uygula → applyThemeToConfig()
4. Canvas oluşturma → Chart.js render
5. Tema değişikliği dinleyicisi → updateCharts()
```

### Faydalı Bağlantılar

Uygulamamızla ilgili Chart.js belgeleri:

- [Grafik Türleri](https://www.chartjs.org/docs/latest/charts/) - Desteklenen grafik türleri ve yapılandırmaları
- [Yapılandırma Seçenekleri](https://www.chartjs.org/docs/latest/configuration/) - Grafik yapılandırma seçenekleri
- [Responsive Grafikler](https://www.chartjs.org/docs/latest/configuration/responsive.html) - Tepkisel (Responsive) grafik ayarları
- [Ölçekler](https://www.chartjs.org/docs/latest/axes/) - Eksen yapılandırmaları