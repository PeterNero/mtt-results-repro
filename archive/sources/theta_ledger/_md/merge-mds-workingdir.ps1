# merge-mds.ps1
# Merge Markdown files in the CURRENT WORKING DIRECTORY into a single file:
# 1) List all merged papers (filenames)
# 2) Include NOTATION.md
# 3) Include each remaining .md file (papers) in alphabetical order
#
# Edit this variable:
$OutputFilename = "ALL_PAPERS_MERGED.md"   # output filename (created in the working folder)

$ErrorActionPreference = "Stop"

# Use the current working directory
$InputDir = Get-Location
$OutPath  = Join-Path $InputDir $OutputFilename

# Find NOTATION.md (case-insensitive) in working directory
$notation = Get-ChildItem -Path $InputDir -File -Filter *.md |
    Where-Object { $_.Name -ieq "NOTATION.md" } |
    Select-Object -First 1

# Collect paper markdown files (exclude output file and NOTATION.md)
$papers = Get-ChildItem -Path $InputDir -File -Filter *.md |
    Where-Object {
        $_.FullName -ne $OutPath -and
        $_.Name -ine "NOTATION.md"
    } |
    Sort-Object Name

if (-not $papers -or $papers.Count -eq 0) {
    throw "No paper .md files found in the working directory."
}

# Build the merged content
$out = New-Object System.Collections.Generic.List[string]

$out.Add("# Merged Papers")
$out.Add("")
$out.Add("## Included papers")
foreach ($p in $papers) {
    $out.Add("- " + $p.Name)
}
$out.Add("")
$out.Add("---")
$out.Add("")

# Include NOTATION.md if present
if ($notation) {
    $out.Add("# NOTATION")
    $out.Add("")
    $out.Add((Get-Content -LiteralPath $notation.FullName -Raw))
    $out.Add("")
    $out.Add("---")
    $out.Add("")
} else {
    $out.Add("> NOTE: NOTATION.md was not found in the working directory, so it was not included.")
    $out.Add("")
    $out.Add("---")
    $out.Add("")
}

# Include each paper
foreach ($p in $papers) {
    $out.Add("==================================================")
    $out.Add("PAPER FILE: " + $p.Name)
    $out.Add("==================================================")
    $out.Add("")
    $out.Add((Get-Content -LiteralPath $p.FullName -Raw))
    $out.Add("")
    $out.Add("---")
    $out.Add("")
}

# Write output
$out | Set-Content -LiteralPath $OutPath -Encoding UTF8

Write-Host "Merged $($papers.Count) papers into: $OutPath"
if ($notation) { Write-Host "Included NOTATION.md" }
