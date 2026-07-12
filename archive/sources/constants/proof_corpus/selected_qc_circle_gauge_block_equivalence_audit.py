"""Audit the selected Qc circle gauge-block equivalence lemma."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
CERT = REPO / "certificates" / "selected_qc_circle_gauge_block_equivalence_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qc_Circle_Gauge_Block_Equivalence_v1.md"
SCRIPT = REPO / "scripts" / "compute_selected_qc_circle_gauge_block_equivalence.py"
GAUGE_FIXING = OBSIDIAN / "5 Dirac Delta" / "Gauge_Fixing_as_Admissible_Section_Selection_in_Modal_Triplet_Theory.md"
STRING_TRACE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__From_MTT_to_String_Theory.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def approx(left: float, right: float, tolerance: float = 1e-12) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=tolerance)


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def report(name: str, ok: bool, detail: object = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    gauge_fixing = read(GAUGE_FIXING)
    string_trace = read(STRING_TRACE)
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "QC_CIRCLE_GAUGE_BLOCK_EQUIVALENCE_CLOSED_FOR_WEAK_SPLIT",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate value",
            approx(
                computed["selected_values"]["selected_p_Qc_for_weak_split"],
                cert["selected_values"]["selected_p_Qc_for_weak_split"],
            )
            and approx(computed["selected_values"]["heat_index_weight"], 1.0),
            computed["selected_values"],
        )
    )
    failures.append(
        not report(
            "gauge fixing source supports abelian ghost decoupling",
            "In the Abelian case the ghost determinant is therefore field-independent and decouples" in gauge_fixing
            and "constant along the physical field directions" in gauge_fixing,
            GAUGE_FIXING,
        )
    )
    failures.append(
        not report(
            "trace source supports abelian normalization",
            "mathrm{Tr}(T^{2})=1" in string_trace
            and "abelian generator" in string_trace,
            STRING_TRACE,
        )
    )
    failures.append(
        not report(
            "weak-split closure but no absolute normalization overclaim",
            cert["verdict"]["qc_selected_for_lambda_12_accounting"] is True
            and cert["verdict"]["absolute_universal_constant_fixed"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )
    failures.append(
        not report(
            "note names next SU2 block",
            "Selected_SU2_Sphere_Gauge_Block_Equivalence_v1" in note
            and "does not claim an absolute universal determinant normalization" in note
            and "D_Qc = selected circle gauge block for weak-split accounting" in note,
            NOTE,
        )
    )

    print("\nSelected Qc circle gauge-block equivalence audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
