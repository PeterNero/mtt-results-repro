"""Audit Route-C C1 defect-functional source import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_c1_defect_functional_source_import.candidate.json"
CERT = ROOT / "certificates" / "routec_c1_defect_functional_source_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_C1DefectFunctionalSource_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_c1_defect_functional_source.py"

STATUS = "ROUTEC_C1_DEFECT_FUNCTIONAL_SOURCE_IMPORTED_PHIFINC1_BINDING_OPEN"
NEXT = "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1"


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

    summary = data["c1_defect_functional_source_summary"]
    require(summary["formal_C1_defect_functional_sourced"] is True, "formal source missing")
    require(summary["unique_up_to_positive_scale"] is True, "uniqueness missing")
    require(summary["scale_cancels_from_euler_projection"] is True, "scale cancellation missing")
    require(summary["physical_PhiFinC1_application_rule_proved"] is False, "PhiFinC1 overclaimed")
    require(summary["independent_quadrature_data_filled"] is False, "quadrature overclaimed")
    require(summary["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")

    upstream = data["upstream_candidate"]
    require(upstream["promotion_decision"]["selected_C1_defect_functional_formal_source_promoted"] is True, "formal functional not promoted")
    for key in [
        "physical_PhiFinC1_application_rule_proved",
        "independent_quadrature_data_filled",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(upstream["promotion_decision"][key] is False, f"promotion overclaimed: {key}")

    packets = data["upstream_packets"]
    require(packets["c1_defect_functional_uniqueness_source"]["status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE", "functional status mismatch")
    require(packets["phifinc1_physical_application_source_gap"]["status"] == "FUNCTIONAL_SOURCED_PHYSICAL_APPLICATION_RULE_OPEN", "physical gap status mismatch")
    require(packets["independent_quadrature_data_fill_attempt"]["status"] == "DATA_REQUIREMENTS_RESTATED_NO_INDEPENDENT_VALUES_FILLED", "quadrature status mismatch")

    for key in [
        "claims_physical_PhiFinC1_application_rule",
        "claims_independent_quadrature_data",
        "claims_unpatched_A_selected",
        "claims_unpatched_b_selected",
        "claims_unpatched_deltaTheta_C1",
        "claims_unpatched_SM_dynamic_closure",
        "claims_true_SM_equivalence",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("formal C1 defect functional is now sourced" in note, "note missing summary")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
