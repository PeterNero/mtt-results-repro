# convert-overleaf-zips-v4-workingdir.ps1
# Overleaf ZIP (source) -> extract -> detect main .tex -> pandoc -> LLM-friendly Markdown
# v4-workingdir:
# - Uses CURRENT WORKING DIRECTORY for input/output
# - Rewrites labels + references via clean-math-v4.lua
# - Preserves bibliography
#
# REQUIREMENTS:
# - pandoc in PATH
# - clean-math-v4.lua placed in the SAME folder as this script

$ErrorActionPreference = "Stop"

# Use current working directory
$InputDir = Get-Location

$WorkDir = Join-Path $InputDir "_work"
$OutDir  = Join-Path $InputDir "_md"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LuaFilter = Join-Path $ScriptDir "clean-math-v4.lua"

if (-not (Test-Path -LiteralPath $LuaFilter)) {
    throw "Missing Lua filter: clean-math-v4.lua must be in the same folder as this script."
}

New-Item -ItemType Directory -Force -Path $WorkDir | Out-Null
New-Item -ItemType Directory -Force -Path $OutDir  | Out-Null

function Get-MainTexFile {
    param([string]$ProjectPath)

    $texFiles = Get-ChildItem -Path $ProjectPath -Recurse -File -Filter *.tex -ErrorAction SilentlyContinue
    if (-not $texFiles) { return $null }

    # Prefer main.tex if present
    $main = $texFiles | Where-Object { $_.Name -ieq "main.tex" } | Select-Object -First 1
    if ($main) { return $main.FullName }

    # Otherwise find a file with documentclass + begin{document}
    $candidates = @()
    foreach ($f in $texFiles) {
        try {
            $content = Get-Content -LiteralPath $f.FullName -Raw -ErrorAction Stop
            if ($content -match "\\documentclass" -and $content -match "\\begin\{document\}") {
                $candidates += $f
            }
        } catch { }
    }

    if ($candidates.Count -gt 0) {
        return ($candidates | Sort-Object Length -Descending | Select-Object -First 1).FullName
    }

    # Fallback: largest .tex file
    return ($texFiles | Sort-Object Length -Descending | Select-Object -First 1).FullName
}

# Verify pandoc
try {
    $null = & pandoc --version
} catch {
    throw "Pandoc not found in PATH. Ensure 'pandoc --version' works."
}

# Find ZIP files in working directory
$zips = Get-ChildItem -Path $InputDir -File -Filter *.zip | Sort-Object Name
if (-not $zips) {
    throw "No .zip files found in the working directory."
}

Write-Host "Found $($zips.Count) zip files in working directory:"
foreach ($z in $zips) { Write-Host " - $($z.Name)" }

Write-Host ""
Write-Host "Work dir : $WorkDir"
Write-Host "Output dir: $OutDir"
Write-Host "Lua filter: $LuaFilter"

foreach ($zip in $zips) {
    $baseName = [IO.Path]::GetFileNameWithoutExtension($zip.Name)
    $projPath = Join-Path $WorkDir $baseName

    if (Test-Path $projPath) { Remove-Item -Recurse -Force $projPath }
    New-Item -ItemType Directory -Force -Path $projPath | Out-Null

    Write-Host "`n[$baseName] Extracting..."
    Expand-Archive -LiteralPath $zip.FullName -DestinationPath $projPath -Force

    $mainTex = Get-MainTexFile -ProjectPath $projPath
    if (-not $mainTex) {
        Write-Warning "[$baseName] No .tex files found; skipping."
        continue
    }

    $outMd = Join-Path $OutDir ($baseName + ".md")

    Write-Host "[$baseName] Main TeX: $mainTex"
    Write-Host "[$baseName] Converting to: $outMd"

    & pandoc $mainTex `
        --from=latex `
        --to=markdown `
        --wrap=preserve `
        --mathjax `
        --standalone `
        --markdown-headings=atx `
        --lua-filter $LuaFilter `
        -o $outMd

    Write-Host "[$baseName] Done."
}

Write-Host "`nAll done."
Write-Host "Markdown output: $OutDir"
Write-Host "Extracted sources: $WorkDir"
