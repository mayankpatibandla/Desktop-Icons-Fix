$scriptPath = Join-Path -Path $PSScriptRoot -ChildPath "desktop_icons_fix.py"

try {
  & python $scriptPath
} catch {
  Write-Host "Python executable not found or script execution failed."
}
