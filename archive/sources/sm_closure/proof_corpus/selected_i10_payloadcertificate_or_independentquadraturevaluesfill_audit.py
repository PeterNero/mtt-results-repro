"""Audit I10 payload certificate / independent quadrature values fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A_ATTEMPT = PACKET_DIR / "route_a_i10_payload_certificate_fill_attempt.packet.json"
ROUTE_B_ATTEMPT = PACKET_DIR / "route_b_independent_quadrature_values_fill_attempt.packet.json"
CUTSET = PACKET_DIR / "minimal_next_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_I10_PAYLOAD_OR_QUADRATURE_VALUES_FILL_ATTEMPT_BUILT_CUTSET_OPEN"
NEXT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A_ATTEMPT)
    route_b = load(ROUTE_B_ATTEMPT)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    checks = route_a["payload_checks"]
    require(checks["selected_minimizer_trace_payload_verified"]["value"] is False, "minimizer trace oververified")
    require(checks["selected_c1_response_payload_verified"]["value"] is False, "C1 response oververified")
    require(checks["defect_functional_minimizer_payload_verified"]["value"] is False, "functional minimizer oververified")
    require(checks["no_observed_data_as_selector"]["value"] is True, "observed-data guardrail missing")
    require(route_a["accepted_now"] is False, "route A overaccepted")

    require(route_b["accepted_now"] is False, "route B overaccepted")
    require(route_b["table_counts"]["zero_mode_basis_rows"] == 0, "zero-mode table unexpectedly filled")
    require(route_b["table_counts"]["primitive_contraction_rows"] == 0, "primitive table unexpectedly filled")
    require(route_b["table_counts"]["hessian_source_rows"] == 0, "hessian table unexpectedly filled")
    require(route_b["table_counts"]["sector_matrix_rows"] == 0, "sector table unexpectedly filled")
    require(route_b["acceptance_checks"]["no_patched_replay_copying"] is True, "patched-copy guardrail missing")
    for key, value in route_b["acceptance_checks"].items():
        if key != "no_patched_replay_copying":
            require(value is False, f"route B check overaccepted: {key}")

    require(cutset["status"] == "NEXT_CUTSET_SELECTED", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "recommended next mismatch")
    require("straight_route" in cutset["recommended_next"]["superset_strategy"], "straight route missing")
    require("parallel_route" in cutset["recommended_next"]["superset_strategy"], "parallel route missing")

    for key in [
        "route_A_payload_fields_evaluated",
        "route_B_quadrature_tables_evaluated",
        "minimal_cutset_selected",
        "no_observed_data_as_selector_verified",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_minimizer_trace_payload_verified",
        "selected_c1_response_payload_verified",
        "defect_functional_minimizer_payload_verified",
        "independent_quadrature_values_filled",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    decision = data["promotion_decision"]
    for key in [
        "route_A_i10_payload_certificate_accepted",
        "route_B_independent_quadrature_values_accepted",
        "I10_proved",
        "unpatched_A_selected_promoted",
        "unpatched_b_selected_promoted",
        "unpatched_deltaTheta_C1_promoted",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "cutset theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("Route A result" in note and "Route B result" in note, "note missing route result")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
