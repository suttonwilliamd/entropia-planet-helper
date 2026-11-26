# Creates (or updates) "Entropia Planet Helper.lnk" on your Desktop.
# Usage:  powershell -ExecutionPolicy Bypass -File scripts\install_shortcut.ps1 [-Planet aris] [-Pythonw C:\path\pythonw.exe]
param(
    [string]$Planet = "aris",
    [string]$Pythonw = ""
)
$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot

if (-not $Pythonw) {
    $py = Get-Command python -ErrorAction SilentlyContinue
    if ($py) {
        $exe = & $py.Source -c "import sys; print(sys.executable)"
        $candidate = Join-Path (Split-Path -Parent $exe) "pythonw.exe"
        if (Test-Path $candidate) { $Pythonw = $candidate }
    }
}
if (-not $Pythonw -or -not (Test-Path $Pythonw)) {
    throw "Could not find pythonw.exe (Python 3.10+ with Tk). Pass -Pythonw <path>."
}

# Refuse to create a shortcut to a destination the data does not contain.
$check = & (Join-Path (Split-Path -Parent $Pythonw) "python.exe") -m planet_helper --check --planet $Planet 2>&1
if ($LASTEXITCODE -ne 0) { throw "Data check failed:`n$check" }

$desktop = [Environment]::GetFolderPath("Desktop")
$lnkPath = Join-Path $desktop "Entropia Planet Helper.lnk"
$shell = New-Object -ComObject WScript.Shell
$lnk = $shell.CreateShortcut($lnkPath)
$lnk.TargetPath = $Pythonw
$lnk.Arguments = "-m planet_helper --planet $Planet"
$lnk.WorkingDirectory = $repo
$lnk.Description = "Entropia Planet Helper (offline guide, opens on $Planet)"
$lnk.IconLocation = "$env:SystemRoot\System32\shell32.dll,13"
$lnk.Save()
Write-Output "Shortcut: $lnkPath"
Write-Output "Target:   $Pythonw -m planet_helper --planet $Planet  (in $repo)"
