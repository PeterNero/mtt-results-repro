"""Audit Route-C PhiFinC1 binding reduction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_phifinc1_binding_reduction_import.candidate.json"
CERT = ROOT / "certificates" / "routec_phifinc1_binding_reduction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_PhiFinC1BindingReduction_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_phifinc1_binding_reduction.py"

STATUS = "ROUTEC_PHIFINC1_BINDING_REDUCTION_IMPORTED_I10_OR_QUADRATURE_OPEN"
NEXT = "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    summary = data["phifinc1_binding_reduction_summary"]
    require(summary["I10_theorem_slot_created"] is True, "I10 slot missing")
    require(summary["I10_proved_now"] is False, "I10 overproved")
    require(summary["I1_minimizer_trace_open"] is True, "I1 gap missing")
    require(summary["I5_dotD_C1_response_open"] is True, "I5 gap missing")
    require(summary["independent_quadrature_template_created"] is True, "quadrature template missing")
    require(summary["independent_quadrature_values_filled"] is False, "quadrature overfilled")
    require(summary["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    upstream = data["upstream_candidate"]
    for key in [
        "prove_I1_selected_minimizer_to_PhiFin_trace",
        "prove_I5_selected_dotD_C1_response",
        "prove_I10_PhiFinC1_minimizes_defect_functional",
        "fill_independent_quadrature_table_values",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(upstream["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    packets = data["upstream_packets"]
    require(packets["phifinc1_minimizer_binding_reduction"]["proved_now"] is False, "binding overproved")
    require(packets["independent_quadrature_table_template"]["values_filled_now"] is False, "template overfilled")

    for key in [
        "claims_I10_proved",
        "claims_I1_proved",
        "claims_I5_proved",
        "claims_independent_quadrature_values",
        "claims_unpatched_A_selected",
        "claims_unpatched_b_selected",
        "claims_unpatched_deltaTheta_C1",
        "claims_unpatched_SM_dynamic_closure",
        "claims_true_SM_equivalence",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("I10 theorem slot" in note, "note missing I10")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
