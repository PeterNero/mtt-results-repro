from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraloverlapkernelvaluesourceorphysicalunittheorem"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
PACKET = ROOT / "candidate_data" / SLUG / "neutral_overlap_value_source_readiness.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralOverlapKernelValueSourceOrPhysicalUnitTheorem_v1.md"

STATUS = "MTT_SELECTED_NEUTRALOVERLAP_VALUESOURCE_PARTIAL_PROJECTOR_GRAM_PROMOTION_VALUES_OPEN"
NEXT = "MTT_Selected_NeutralGammaNuActionRowsOrDiracCompleteness_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    packet = load(PACKET)
    candidate = load(CANDIDATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == STATUS, "packet status changed")
    require(cert["status"] == STATUS, "certificate status changed")
    require(packet["next_required_artifact"] == NEXT, "next artifact changed")
    require(cert["next_required_artifact"] == NEXT, "cert next changed")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(packet["target_fitting_used"] is False, "target fitting used")

    closes = packet["what_closes_here"]
    require(closes["neutral_L_N_H_projector_carriers"] is True, "neutral carriers not promoted")
    require(closes["neutral_trace_Gram_normalization"] is True, "trace Gram not promoted")
    require(closes["neutral_slot_consistency"] is True, "slot consistency not promoted")
    require(closes["OK3_promoted"] is True, "OK3 not promoted")
    require(closes["OK4_promoted"] is True, "OK4 not promoted")
    require(closes["value_rows_emitted"] is False, "value rows overemitted")

    carriers = packet["neutral_carrier_projectors"]
    require(carriers["L"]["rank"] == 3, "L rank changed")
    require(carriers["N"]["rank"] == 3, "N rank changed")
    require(carriers["H_as_Hu_carrier"]["rank"] == 1, "H rank changed")
    for name, row in carriers.items():
        require(row["projector_idempotent"] is True, f"{name} projector not idempotent")
        require(row["projector_self_adjoint"] is True, f"{name} projector not self-adjoint")
        require(row["source_verified_by_transport_conjugation"] is True, f"{name} source not verified")
        require(row["stationary_rho_s_promoted"] is True, f"{name} rho_s not promoted")

    sub = packet["readiness_subfields"]
    require(packet["readiness_subfields_closed"] == 6, "readiness count changed")
    require(packet["readiness_subfields_total"] == 12, "readiness total changed")
    for key in [
        "selected_L_projector_rank3",
        "selected_Nc_projector_rank3",
        "selected_Hu_carrier_projector_rank1",
        "selected_trace_Gram_normalization",
        "selected_1M_Nc_Dirac_slot_arrow",
        "selected_same_source_slot_consistency",
    ]:
        require(sub[key] is True, f"subfield not closed: {key}")
    for key in [
        "Gamma_nu_ij_channel_sets",
        "neutral_action_cost_rows_S_gamma",
        "neutral_prefactors_A_gamma",
        "neutral_retarded_sign_rows",
        "Dirac_only_action_completeness",
        "same_scheme_physical_normalization",
    ]:
        require(sub[key] is False, f"subfield overclosed: {key}")

    ok = packet["neutral_overlap_OK_gate_acceptance"]
    require(packet["neutral_overlap_OK_gates_closed"] == 5, "OK gate count changed")
    require(packet["neutral_overlap_OK_gates_total"] == 9, "OK gate total changed")
    require(ok["OK3_normalized_zero_mode_bases"] is True, "OK3 false")
    require(ok["OK4_kinetic_metrics_positive"] is True, "OK4 false")
    for key in [
        "OK5_finite_neutral_overlap_channel_sets",
        "OK6_action_costs_prefactors_characters_retarded_signs",
        "OK7_nil_coherence_anchor_projectors",
        "OK8_RG_threshold_matching_map",
    ]:
        require(ok[key] is False, f"OK value gate overclosed: {key}")

    require(packet["accepted_route_exit_count"] == 0, "route overaccepted")
    require(packet["new_value_fields_closed_here"] == 0, "value fields overclosed")
    for field in [
        "dimensionful_M_D_3x3_closed",
        "dimensionful_M_L_3x3_closed",
        "dimensionful_M_R_3x3_closed",
        "absolute_normalization_and_scheme_closed",
        "selected_neutral_operator_accepted",
        "U5_closed",
    ]:
        require(packet[field] is False, f"overclosed: {field}")
        require(cert[field] is False, f"cert overclosed: {field}")

    require(len(packet["remaining_value_blockers"]) == 5, "blocker count changed")
    for phrase in [
        "promotes neutral overlap OK gates from `3/9`",
        "`5/9`",
        "Accepted exits remain `0/3`",
        "finite `Gamma_nu[i,j]`",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {phrase}")

    print(json.dumps({
        "neutral_OK_gates": "5/9",
        "readiness": "6/12",
        "accepted_routes": 0,
        "new_value_fields_closed": 0,
        "next": NEXT,
    }, indent=2))
    print("selected neutral overlap value-source/physical-unit theorem audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
