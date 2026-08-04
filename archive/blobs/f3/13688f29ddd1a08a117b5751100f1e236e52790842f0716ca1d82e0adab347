"""Audit the heterotic bundle-curvature/trace or direct-operator gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_bundle_curvature_trace_or_direct_operator_gate.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_bundle_curvature_trace_or_direct_operator_gate_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_BundleCurvature_Trace_or_DirectOperator_Gate_v1.md"

STATUS = "HETEROTIC_BUNDLE_CURVATURE_TRACE_OR_DIRECT_OPERATOR_GATE_BUILT_VALUES_OPEN"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    cert = load(CERT)

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("R+ carried forward", data["what_closes_now"]["R_plus_geometric_curvature_available"] is True and cert["R_plus_available"] is True, data["what_closes_now"])

    standard = data["routes"]["A_conditional_standard_embedding"]
    check("standard embedding conditional only", standard["closes_now"] is False and data["decision"]["standard_embedding_selected"] is False, standard)
    check("conditional fills named", standard["fills_if_selected"]["curvature_F_A_components"].startswith("F_A"), standard["fills_if_selected"])
    check("conditional has R+ support", standard["computed_support"]["R_plus_nonzero_components"] > 0, standard["computed_support"])

    direct = data["routes"]["B_direct_finite_operator"]
    check("direct route open", direct["closes_now"] is False and data["decision"]["direct_finite_operator_emitted"] is False, direct)
    check("required direct payload complete", {"rho_E or equivalent finite transition/operator data", "D_E action on the selected quotient domain", "Riesz projectors and complement gap", "Weitzenbock E_Qa or equivalent finite zero-order block"} <= set(direct["required_payload"]), direct["required_payload"])

    routec = data["routes"]["C_routec_phi_fin_import"]
    check("routec support not promotion", routec["present"] is True and routec["closes_now"] is False, routec)
    check("phi_fin still open", routec["open_sublemma"] == "FiniteEmissionMorphismLemma", routec)

    remains = data["what_remains_open"]
    check("bundle fields remain open", remains["selected_bundle_connection_A"] and remains["selected_bundle_curvature_F_A"] and remains["trace_normalization"], remains)
    check("operator remains open", remains["E_Qa_or_direct_finite_operator"] and data["decision"]["E_Qa_computed"] is False, data["decision"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records two routes", "exactly two legal next routes" in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic bundle-curvature/trace or direct-operator gate audit")


if __name__ == "__main__":
    main()
