# Command Examples

The command examples component displays terminal commands with proper and elegant syntax highlighting in addition to formatting.

## Basic Command

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">python phantom_e2e_modular.py --module deployment_test</span>
</div>

## Multi-line Command

For longer commands that span multiple lines, use line continuation:

<div class="phantom-command-example">
  <span class="command-prompt">$</span>
  <span class="command-text">docker run -it \
    -v $(pwd):/app \
    -e DO_API_TOKEN=$DO_API_TOKEN \
    phantom/e2e-runner</span>
</div>

## Different Command Types

You can customize the component for different command types:

### Root User
<div class="phantom-command-example">
  <span class="command-prompt">#</span>
  <span class="command-text">apt-get update && apt-get upgrade -y</span>
</div>

### PowerShell
<div class="phantom-command-example">
  <span class="command-prompt">PS&gt;</span>
  <span class="command-text">Get-Process | Where-Object {$_.CPU -gt 100}</span>
</div>

### Custom Prompt
<div class="phantom-command-example">
  <span class="command-prompt">user@host:~$</span>
  <span class="command-text">ls -la /var/log/</span>
</div>

## Usage Tips

1. **Keep it Simple**: Use the basic `$` prompt for most examples
2. **Line Breaks**: Use `\` for line continuation in long commands
3. **Syntax Highlighting**: For more complex scripts, consider using code blocks with syntax highlighting
4. **Copy-Friendly**: The command text is easily selectable for copying

## Alternative: Code Blocks

For scripts or multiple commands, standard code blocks might be more appropriate:

```bash
# Update system packages
sudo apt-get update
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```