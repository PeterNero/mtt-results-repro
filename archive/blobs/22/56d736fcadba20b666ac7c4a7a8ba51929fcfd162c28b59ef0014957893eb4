"""Audit the selected electroweak C1 primitive response scaffold."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_C1_Primitive_Response_Scaffold_v1.md"
CERT = REPO / "certificates" / "selected_electroweak_c1_primitive_response_scaffold_certificate.json"
REDUCED = REPO / "certificates" / "selected_electroweak_c1_response_reduced.template.json"
FILL_CERT = REPO / "certificates" / "selected_electroweak_c1_response_fill_attempt_certificate.json"
CALCULATOR = REPO / "scripts" / "compute_electroweak_c1_response.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def run_reduced() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CALCULATOR), str(REDUCED)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = load_json(CERT)
    reduced = load_json(REDUCED)
    fill = load_json(FILL_CERT)
    note = read(NOTE)
    run = run_reduced()
    terms = reduced["raw_response_per_v1"]["terms"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "PEW_ALPHA1_PRIMITIVE_RESPONSE_REDUCED_TO_THREE_SOURCE_TERMS",
            cert["status"],
        ),
        check(
            "zero terms filled",
            terms["scheme_counterterm"] == [0.0, 0.0, 0.0]
            and terms["basis_transport"] == [0.0, 0.0, 0.0],
            {"scheme": terms["scheme_counterterm"], "basis": terms["basis_transport"]},
        ),
        check(
            "three physical terms remain open",
            terms["local_determinant"] is None
            and terms["torsion_curvature"] is None
            and terms["bundle_index"] is None
            and set(cert["remaining_physical_terms"].keys())
            == {"local_determinant", "torsion_curvature", "bundle_index"},
            cert["remaining_physical_terms"],
        ),
        check(
            "reduced template refuses only physical terms",
            run.returncode == 2
            and "raw_response_per_v1.terms.local_determinant" in run.stdout
            and "raw_response_per_v1.terms.torsion_curvature" in run.stdout
            and "raw_response_per_v1.terms.bundle_index" in run.stdout
            and "raw_response_per_v1.terms.scheme_counterterm" not in run.stdout
            and "raw_response_per_v1.terms.basis_transport" not in run.stdout,
            run.stdout.splitlines(),
        ),
        check(
            "inherits no-fill discipline",
            fill["verdict"]["numeric_electroweak_closure"] is False
            and all(shortcut in cert["forbidden_shortcuts"] for shortcut in ["using Execution I fitted c1,c2"]),
            fill["verdict"],
        ),
        check(
            "weak split formula recorded",
            "lambda_12" in cert["weak_split_formula"]
            and "p_det,U1-p_det,SU2" in cert["weak_split_formula"]["lambda_12"]
            and "lambda_12" in note,
            cert["weak_split_formula"],
        ),
        check(
            "no numeric electroweak closure",
            cert["verdict"]["numeric_electroweak_closure"] is False
            and cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        ),
        check(
            "note names reduced template",
            "selected_electroweak_c1_response_reduced.template.json" in note
            and "PEW_ALPHA1_PRIMITIVE_RESPONSE_REDUCED_TO_THREE_SOURCE_TERMS" in note,
            "reduced template and status",
        ),
    ]

    print("\nSelected electroweak C1 primitive response scaffold audit")
    print("=========================================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())

