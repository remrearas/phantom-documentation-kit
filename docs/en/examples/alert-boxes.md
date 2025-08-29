# Alert Boxes

Alert boxes are used to display important messages with appropriate visual styling. 
They support different types for various message contexts.

## Success Alert

<div class="phantom-alert success">
  <i class="fas fa-check-circle"></i>
  <strong>Success!</strong> All tests passed successfully. Your infrastructure is ready.
</div>


## Error Alert

<div class="phantom-alert error">
  <i class="fas fa-times-circle"></i>
  <strong>Error:</strong> Connection failed. Please check your API credentials.
</div>


## Warning Alert

<div class="phantom-alert warning">
  <i class="fas fa-exclamation-triangle"></i>
  <strong>Warning:</strong> Some tests are taking longer than expected. Consider optimizing your network settings.
</div>


## Info Alert

<div class="phantom-alert info">
  <i class="fas fa-info-circle"></i>
  <strong>Note:</strong> This test requires at least 2GB of available memory to run properly.
</div>


## Available Classes

| Class                   | Description            | Color Scheme                                                   |
|-------------------------|------------------------|----------------------------------------------------------------|
| `phantom-alert success` | Success messages       | <span style="color: #22c55e; font-weight: bold;">Green</span>  |
| `phantom-alert error`   | Error messages         | <span style="color: #ef4444; font-weight: bold;">Red</span>    |
| `phantom-alert warning` | Warning messages       | <span style="color: #f59e0b; font-weight: bold;">Orange</span> |
| `phantom-alert info`    | Informational messages | <span style="color: #3b82f6; font-weight: bold;">Blue</span>   |

## Usage Without Icons

Alerts can also be used without icons for a cleaner look:

<div class="phantom-alert success">
  <strong>Success!</strong> Operation completed successfully.
</div>

<div class="phantom-alert error">
  <strong>Error:</strong> Invalid configuration detected.
</div>

<div class="phantom-alert warning">
  <strong>Warning:</strong> This action cannot be undone.
</div>

<div class="phantom-alert info">
  <strong>Info:</strong> New version available for download.
</div>

## Multi-line Alerts

For longer messages, alerts maintain proper formatting:

<div class="phantom-alert info">
  <i class="fas fa-info-circle"></i>
  <strong>Installation Requirements:</strong>
  <br><br>
  Before proceeding with the installation, please ensure:
  <ul style="margin: 0.5rem 0 0 1.5rem;">
    <li>Python 3.8 or higher is installed</li>
    <li>Docker is running and accessible</li>
    <li>You have at least 4GB of free disk space</li>
    <li>Your API token has been configured</li>
  </ul>
</div>

## Best Practices

1. **Icon Usage**: Always pair alerts with appropriate Font Awesome icons
2. **Title Format**: Use `<strong>` tags for alert titles (Success!, Error:, Warning:, Note:)
3. **Message Length**: Keep messages concise and actionable
4. **Contextual Use**: 
   - Success: Confirm completed actions
   - Error: Show failures that need attention
   - Warning: Highlight potential issues
   - Info: Provide helpful information

## Common Use Cases

### Form Validation
<div class="phantom-alert error">
  <i class="fas fa-times-circle"></i>
  <strong>Validation Error:</strong> Please fill in all required fields.
</div>

### System Status
<div class="phantom-alert success">
  <i class="fas fa-check-circle"></i>
  <strong>System Status:</strong> All services are operational.
</div>

### Configuration Tips
<div class="phantom-alert info">
  <i class="fas fa-info-circle"></i>
  <strong>Tip:</strong> You can customize the timeout value in the configuration file.
</div>

### Deprecation Notice
<div class="phantom-alert warning">
  <i class="fas fa-exclamation-triangle"></i>
  <strong>Deprecation Notice:</strong> This feature will be removed in version 3.0.
</div>