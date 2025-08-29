# Status Cards

Status cards provide visual feedback for metrics, statistics, and key performance indicators.

## Test Status Grid

Status cards are perfect for displaying metrics, statistics, and key performance indicators. They support different color schemes for various states.

<div class="phantom-test-status-grid">
  <div class="phantom-test-status-card success">
    <div class="phantom-test-status-value">4</div>
    <div class="phantom-test-status-label">Active Modules</div>
  </div>
  <div class="phantom-test-status-card error">
    <div class="phantom-test-status-value">0</div>
    <div class="phantom-test-status-label">Failed Tests</div>
  </div>
  <div class="phantom-test-status-card warning">
    <div class="phantom-test-status-value">2</div>
    <div class="phantom-test-status-label">Warnings</div>
  </div>
  <div class="phantom-test-status-card info">
    <div class="phantom-test-status-value">12</div>
    <div class="phantom-test-status-label">Total Tests</div>
  </div>
</div>

### Available Classes

| Class                              | Description          | Color Scheme                                                   |
|------------------------------------|----------------------|----------------------------------------------------------------|
| `phantom-test-status-card success` | Successful states    | <span style="color: #22c55e; font-weight: bold;">Green</span>  |
| `phantom-test-status-card error`   | Error states         | <span style="color: #ef4444; font-weight: bold;">Red</span>    |
| `phantom-test-status-card warning` | Warning states       | <span style="color: #f59e0b; font-weight: bold;">Orange</span> |
| `phantom-test-status-card info`    | Informational states | <span style="color: #3b82f6; font-weight: bold;">Blue</span>   |

## Module Cards

Module cards are designed to showcase features, services, or test modules with descriptions and metadata.

<div class="phantom-module-card">
  <div class="phantom-module-card-header">
    <span class="phantom-module-card-title">Deployment Test</span>
    <span class="phantom-module-card-duration">~5 min</span>
  </div>
  <div class="phantom-module-card-description">
    Validates basic infrastructure deployment and ensures all components are accessible.
  </div>
</div>

<div class="phantom-module-card">
  <div class="phantom-module-card-header">
    <span class="phantom-module-card-title">Traffic Flow Validation</span>
    <span class="phantom-module-card-duration">~3 min</span>
  </div>
  <div class="phantom-module-card-description">
    Tests network connectivity between peers through the WireGuard tunnel.
  </div>
</div>

## Example with Icons

You can enhance status cards with Font Awesome icons for better visual communication:

<div class="phantom-test-status-grid">
  <div class="phantom-test-status-card success">
    <i class="fas fa-check-circle fa-2x mb-2"></i>
    <div class="phantom-test-status-value">4</div>
    <div class="phantom-test-status-label">Tests Passed</div>
  </div>
  <div class="phantom-test-status-card error">
    <i class="fas fa-times-circle fa-2x mb-2"></i>
    <div class="phantom-test-status-value">0</div>
    <div class="phantom-test-status-label">Tests Failed</div>
  </div>
  <div class="phantom-test-status-card warning">
    <i class="fas fa-exclamation-triangle fa-2x mb-2"></i>
    <div class="phantom-test-status-value">2</div>
    <div class="phantom-test-status-label">Warnings</div>
  </div>
  <div class="phantom-test-status-card info">
    <i class="fas fa-info-circle fa-2x mb-2"></i>
    <div class="phantom-test-status-value">12</div>
    <div class="phantom-test-status-label">Total Tests</div>
  </div>
</div>