"""Audit C1 first-variation certificate fill / quadrature rows first run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_c1firstvariationcertificatefill_or_quadraturerowsfirstrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A_FILL = PACKET_DIR / "route_a_first_variation_certificate_partial_fill.packet.json"
ROUTE_B_FIRST_RUN = PACKET_DIR / "route_b_basis_rows_first_run.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_partial_fill.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_C1FirstVariationCertificateFill_or_QuadratureRowsFirstRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_C1_FIRSTVARIATION_PARTIAL_FILL_OR_QUADRATURE_BASIS_FIRST_RUN_BUILT_OPEN"
NEXT = "MTT_Selected_TraceMapAndBasisValues_or_PrimitiveRowsExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route_a = load(ROUTE_A_FILL)
    route_b = load(ROUTE_B_FIRST_RUN)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    fields = route_a["filled_fields"]
    require(fields["hessian_or_coercivity"]["verified"] is True, "formal Hessian not filled")
    require(fields["hessian_or_coercivity"]["constant_c"] == 1.0, "coercivity constant mismatch")
    require(fields["normalization_compatibility"]["verified"] is True, "normalization not filled")
    require(fields["selected_trace_map"]["verified"] is False, "trace map overfilled")
    require(fields["first_variation_identity"]["verified"] is False, "first variation overfilled")
    require(fields["boundary_cancellation"]["verified"] is False, "boundary overfilled")
    require(route_a["certificate_accepted_now"] is False, "route A overaccepted")

    require(route_b["row_count"] == 19, "basis row count mismatch")
    require(route_b["selected_row_count"] == 0, "basis rows overselected")
    require(route_b["all_basis_rows_selected"] is False, "all basis rows overaccepted")
    require(route_b["can_advance_to_primitive_rows"] is False, "advanced too early")
    require(len(route_b["basis_rows"]) == 19, "basis rows missing")
    for row in route_b["basis_rows"]:
        require(row["selected_now"] is False, f"row overselected: {row['basis_id']}")
        require(row["selected_basis_value"] is None, f"basis value overfilled: {row['basis_id']}")
        require(row["selected_projector_value"] is None, f"projector value overfilled: {row['basis_id']}")

    require(cutset["status"] == "NEXT_CUTSET_AFTER_PARTIAL_FILL_SELECTED", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "recommended next mismatch")
    require(
        "selected HYM/Strominger finite trace" in cutset["recommended_next"]["superset_strategy"]["shared_missing_object"],
        "shared source reason missing",
    )

    for key in [
        "formal_hessian_coercivity_on_residual_quotient",
        "normalization_scale_independence",
        "basis_row_stubs_emitted",
        "shared_trace_basis_cutset_identified",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "selected_trace_map_values",
        "physical_first_variation_identity",
        "boundary_cancellation_for_selected_trace",
        "selected_basis_projector_gram_gap_values",
        "primitive_quadrature_rows",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    decision = data["promotion_decision"]
    for key in [
        "route_A_first_variation_certificate_accepted",
        "route_B_basis_rows_accepted",
        "route_B_can_advance_to_primitive_rows",
        "I10_proved",
        "unpatched_SM_parity_dynamic_packet_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "partial theorem missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and data["unpatched_theorem_closure_claimed"] is False, "closure overclaimed")
    require("formal Hessian/coercivity" in note and "basis row stubs emitted" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
