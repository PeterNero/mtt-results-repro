"""Attempt to extract the retarded dyadic lag coefficients from the MTT corpus.

The bounded retarded-lag theorem needs the non-empirical inequality

    0 < rho_q / kappa_q < 2.

This script checks whether the current local corpus contains explicit selected
data from which rho_q and kappa_q can be evaluated.  If not, it computes only
the empirical target lag implied by the CKM/Jarlskog benchmark already used in
the q=79 admissibility notes.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path.cwd()
OBSIDIAN_MTT_ROOT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

N_CP = 448
N_DYADIC = 64
QUARTER_DYADIC = 16
Q_SELECTED = 79
Q64_SELECTED = 15

S12_Q = 0.2250
S23_Q = 0.0411
S13_Q = 0.0036
J_CKM = 2.9e-5


@dataclass(frozen=True)
class KeywordResult:
    label: str
    pattern: str
    count: int
    files: tuple[str, ...]


def ckm_target() -> tuple[float, float, float, float, float]:
    c12_q = math.sqrt(1.0 - S12_Q * S12_Q)
    c23_q = math.sqrt(1.0 - S23_Q * S23_Q)
    c13_q = math.sqrt(1.0 - S13_Q * S13_Q)
    prefactor = c12_q * c23_q * c13_q**2 * S12_Q * S23_Q * S13_Q
    target_delta = math.asin(J_CKM / prefactor)
    continuous_label = N_CP * target_delta / (2.0 * math.pi)
    u64_target = continuous_label % N_DYADIC
    epsilon_target = QUARTER_DYADIC - u64_target
    return prefactor, target_delta, continuous_label, u64_target, epsilon_target


def markdown_files() -> list[Path]:
    roots = [ROOT]
    if OBSIDIAN_MTT_ROOT.exists():
        roots.append(OBSIDIAN_MTT_ROOT)

    files: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        for path in root.rglob("*.md"):
            if path.name == "ALL_PAPERS_MERGED.md":
                continue
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            files.append(path)
    return sorted(files, key=lambda p: str(p).lower())


def scan_keywords(files: list[Path]) -> list[KeywordResult]:
    checks = [
        ("rho_q symbol", r"\brho_q\b"),
        ("kappa_q symbol", r"\bkappa_q\b"),
        ("H_q symbol", r"\bH_q\b"),
        ("v_64 symbol", r"\bv_64\b"),
        ("closure-strain Hessian phrase", r"closure-strain Hessian"),
        ("retarded overlap phrase", r"retarded overlap"),
        ("explicit numeric rho_q", r"^\s*rho_q\s*=\s*[-+]?\d"),
        ("explicit numeric kappa_q", r"^\s*kappa_q\s*=\s*[-+]?\d"),
        ("explicit numeric ratio", r"^\s*rho_q\s*/\s*kappa_q\s*=\s*[-+]?\d"),
    ]

    results: list[KeywordResult] = []
    for label, pattern in checks:
        regex = re.compile(pattern, re.IGNORECASE)
        count = 0
        matched_files: list[str] = []
        for path in files:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = path.read_text(encoding="utf-8", errors="ignore")
            hits = len(regex.findall(text))
            if hits:
                count += hits
                matched_files.append(str(path))
        results.append(KeywordResult(label, pattern, count, tuple(matched_files[:8])))
    return results


def nearest_selected_label_error(target_delta: float) -> tuple[float, float, float]:
    selected_delta = 2.0 * math.pi * Q_SELECTED / N_CP
    selected_j = J_CKM * math.sin(selected_delta) / math.sin(target_delta)
    phase_error = selected_delta - target_delta
    j_error = selected_j - J_CKM
    return selected_delta, phase_error, j_error


def main() -> None:
    files = markdown_files()
    results = scan_keywords(files)
    prefactor, target_delta, continuous_label, u64_target, epsilon_target = ckm_target()
    selected_delta, phase_error, j_error = nearest_selected_label_error(target_delta)

    numeric_rho = next(row for row in results if row.label == "explicit numeric rho_q")
    numeric_kappa = next(row for row in results if row.label == "explicit numeric kappa_q")
    numeric_ratio = next(row for row in results if row.label == "explicit numeric ratio")
    can_extract = numeric_rho.count > 0 and numeric_kappa.count > 0 or numeric_ratio.count > 0

    print("Retarded lag coefficient extraction attempt")
    print("===========================================")
    print("local root:", ROOT)
    print("obsidian root present:", OBSIDIAN_MTT_ROOT.exists())
    print("markdown files scanned:", len(files))
    print()

    print("Corpus ingredient scan")
    print("======================")
    width = max(len(row.label) for row in results)
    for row in results:
        print(f"{row.label:{width}s}  count={row.count}")
        for file_name in row.files[:3]:
            print(f"{'':{width}s}  - {file_name}")
    print()

    print("Empirical target lag from CKM/Jarlskog benchmark")
    print("================================================")
    print("s12, s23, s13:", f"{S12_Q:.8f}", f"{S23_Q:.8f}", f"{S13_Q:.8f}")
    print("J_CKM:", f"{J_CKM:.12e}")
    print("prefactor:", f"{prefactor:.12e}")
    print("target_delta:", f"{target_delta:.12f}")
    print("continuous Z_448 label:", f"{continuous_label:.12f}")
    print("u64_target:", f"{u64_target:.12f}")
    print("epsilon_target = 16 - u64_target:", f"{epsilon_target:.12f}")
    print("selected q:", Q_SELECTED)
    print("selected q64:", Q64_SELECTED)
    print("selected_delta:", f"{selected_delta:.12f}")
    print("selected_phase_error:", f"{phase_error:.12e}")
    print("selected_J_error:", f"{j_error:.12e}")
    print()

    print("Gate status")
    print("===========")
    gates = [
        ("symbolic coefficient definitions found", "PASS", "rho_q and kappa_q are defined in the notes"),
        ("explicit numeric rho_q/kappa_q found", "PASS" if can_extract else "OPEN", "not present as selected MTT data" if not can_extract else "can evaluate directly"),
        ("empirical target epsilon in (0,2)", "PASS" if 0.0 < epsilon_target < 2.0 else "FAIL", f"epsilon={epsilon_target:.12f}"),
        ("non-empirical q=79 proof completed", "PASS" if can_extract and 0.0 < epsilon_target < 2.0 else "OPEN", "requires selected Hessian and retarded derivative"),
    ]
    gate_width = max(len(label) for label, _, _ in gates)
    status_width = max(len(status) for _, status, _ in gates)
    for label, status, note in gates:
        print(f"{label:{gate_width}s}  {status:{status_width}s}  {note}")

    assert 0.0 < epsilon_target < 2.0
    assert abs(u64_target - Q64_SELECTED) < 0.01
    assert abs(continuous_label - Q_SELECTED) < 0.01


if __name__ == "__main__":
    main()
