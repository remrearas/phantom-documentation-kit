---
extra_javascript:
  - assets/javascripts/chart.js
---

# Chart Examples (Chart.js)

This page demonstrates Chart.js usage within Phantom Documentation Kit. 
By reviewing this page, you can examine chart implementations and their live code examples.

!!! important "Required Configuration"
    To use Chart.js in your markdown files, you **must** include the following YAML front matter at the top of your document:
    ```yaml
    ---
    extra_javascript:
      - assets/javascripts/chart.js
    ---
    ```
    Without this configuration, charts will not render properly.

## Line Chart

A simple responsive line chart showing monthly data trends.

<div class="chart-container" 
     data-chart-title="Monthly Sales Trend"
     data-chart-config='{
       "type": "line",
       "data": {
         "labels": ["January", "February", "March", "April", "May", "June"],
         "datasets": [{
           "label": "Sales 2024",
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

## Bar Chart

A responsive bar chart displaying category comparisons.

<div class="chart-container" 
     data-chart-title="Product Categories Performance"
     data-chart-config='{
       "type": "bar",
       "data": {
         "labels": ["Electronics", "Clothing", "Food", "Books", "Sports", "Home"],
         "datasets": [{
           "label": "Revenue ($k)",
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
               "text": "Revenue ($k)"
             }
           },
           "x": {
             "title": {
               "display": true,
               "text": "Categories"
             }
           }
         }
       }
     }'></div>

## Multiple Axis (Line and Bar) Chart

A combination chart with multiple y-axes showing different metrics.

<div class="chart-container" 
     data-chart-title="Website Analytics Overview"
     data-chart-config='{
       "type": "bar",
       "data": {
         "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
         "datasets": [
           {
             "label": "Page Views",
             "data": [2500, 3200, 2800, 3500, 4200, 3800, 3000],
             "backgroundColor": "rgba(59, 130, 246, 0.6)",
             "borderColor": "#3b82f6",
             "borderWidth": 2,
             "borderRadius": 4,
             "yAxisID": "y"
           },
           {
             "label": "Conversion Rate (%)",
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
               "text": "Days of Week"
             }
           },
           "y": {
             "type": "linear",
             "display": true,
             "position": "left",
             "title": {
               "display": true,
               "text": "Page Views"
             },
             "beginAtZero": true
           },
           "y1": {
             "type": "linear",
             "display": true,
             "position": "right",
             "title": {
               "display": true,
               "text": "Conversion Rate (%)"
             },
             "beginAtZero": true,
             "grid": {
               "drawOnChartArea": false
             }
           }
         }
       }
     }'></div>

## Pie Chart

A responsive pie chart showing distribution of data.

<div class="chart-container" 
     data-chart-title="Market Share Distribution"
     data-chart-config='{
       "type": "pie",
       "data": {
         "labels": ["Product A", "Product B", "Product C", "Product D", "Product E"],
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

## Donut Chart

A responsive donut chart with center text displaying total value.

<div class="chart-container" 
     data-chart-title="Budget Allocation"
     data-chart-config='{
       "type": "doughnut",
       "data": {
         "labels": ["Development", "Marketing", "Operations", "Support", "R&D"],
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

## Chart.js Implementation

The Chart.js implementation within Phantom Documentation Kit is provided through the `overrides/assets/javascripts/chart.js` file. 
This implementation offers the following features:

### How It Works

1. **Automatic Initialization**: On page load, all `.chart-container` elements are automatically scanned and charts are created.

2. **JSON-Based Configuration**: Charts are configured via the `data-chart-config` attribute in JSON format. This approach:
    - Enables chart creation without writing JavaScript code
    - Provides clean and readable structure within Markdown files
    - Offers a secure configuration method

3. **Theme Support**: The implementation automatically detects Material for MkDocs theme changes:
    - Charts automatically update during light/dark theme transitions
    - Text colors, grid lines, and backgrounds become theme-compatible
    - Theme changes are monitored using the `MutationObserver` API

4. **Responsive Design**: Default settings for all charts:
    - `responsive: true` - Automatic scaling based on container size
    - `maintainAspectRatio: false` - Flexible aspect ratio
    - `aspectRatio: 2` - Default 2:1 aspect ratio

### Technologies Used

- **Chart.js v4.4.7**: Optimized version through vendor builder
- **Lazy Loading**: Chart.js is loaded only on pages containing charts
- **Theme Observer**: Real-time theme change monitoring
- **JSON Parse**: Secure configuration reading

### Chart Creation Process

```
1. HTML element scanning → .chart-container
2. JSON config reading → data-chart-config attribute
3. Apply theme colors → applyThemeToConfig()
4. Canvas creation → Chart.js render
5. Theme change listener → updateCharts()
```

### Useful Links

Chart.js documentation related to our implementation:

- [Chart Types](https://www.chartjs.org/docs/latest/charts/) - Supported chart types and configurations
- [Configuration Options](https://www.chartjs.org/docs/latest/configuration/) - Chart configuration options
- [Responsive Charts](https://www.chartjs.org/docs/latest/configuration/responsive.html) - Responsive chart settings
- [Scales](https://www.chartjs.org/docs/latest/axes/) - Axis configurations