# Progress Indicators

Progress indicators show the current state of multi-step processes, perfect for visualizing workflows, installation steps, or test execution stages.

## Active Progress

Shows a process that is currently in progress:

<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step active"></div>
  <div class="progress-step"></div>
</div>

## Completed Progress

Shows a fully completed process:

<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
</div>

## Progress States

### Available Classes

| Class                     | Description           | State     |
|---------------------------|-----------------------|-----------|
| `progress-step`           | Default/pending state | Pending   |
| `progress-step completed` | Completed step        | Completed |
| `progress-step active`    | Currently active step | Active    |

## Examples with Different Step Counts

### 3-Step Process
<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step active"></div>
  <div class="progress-step"></div>
</div>

### 6-Step Process
<div class="phantom-progress-indicator">
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step completed"></div>
  <div class="progress-step active"></div>
  <div class="progress-step"></div>
  <div class="progress-step"></div>
</div>

### 8-Step Process (Long)
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

## Use Cases

Progress indicators are ideal for:

1. **Installation Wizards**: Show which step of the installation process is active
2. **Test Execution**: Display which test module is currently running
3. **Form Wizards**: Guide users through multi-step forms

## Best Practices

1. **Clear States**: Always have one active step (unless completed or not started)
2. **Responsive**: The indicators scale appropriately on mobile devices
3. **Context**: Pair with descriptive text to explain what each step represents