"""Import non-split/Route-C visible lane and minimal Hsel/Gret QA candidate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

PREVIOUS = CERTS / "visible_operator_and_hessian_frontier_import_certificate.json"
VISIBLE_PACKET = SM / "candidate_data" / "selected_nonsplit_rank2_or_routec_same_source_packet.candidate.json"
VISIBLE_CERT = SM / "certificates" / "selected_nonsplit_rank2_or_routec_same_source_packet_certificate.json"
QA_PACKET = QA / "candidate_data" / "minimal_hsel_gret_finite_galerkin_candidate.candidate.json"
QA_CERT = QA / "certificates" / "minimal_hsel_gret_finite_galerkin_candidate_certificate.json"

OUTPUT_PACKET = DATA / "nonsplit_routec_and_minimal_hsel_gret_import.candidate.json"
OUTPUT_CERT = CERTS / "nonsplit_routec_and_minimal_hsel_gret_import_certificate.json"
OUTPUT_NOTE = CORPUS / "NonSplitRouteC_and_MinimalHselGret_Import_v1.md"

STATUS = "NONSPLIT_ROUTEC_AND_MINIMAL_HSEL_GRET_IMPORTED_PROMOTION_OPEN"
PREVIOUS_STATUS = "VISIBLE_OPERATOR_HESSIAN_FRONTIER_IMPORTED_SELECTED_VALUES_OPEN"
VISIBLE_STATUS = "MTT_SELECTED_NONSPLIT_RANK2_OR_ROUTEC_SAME_SOURCE_PACKET_REDUCED_TO_SYMMETRY_BREAKING_SOURCE"
QA_STATUS = "QA_SU3_MINIMAL_HSEL_GRET_FINITE_GALERKIN_CANDIDATE_CONSTRUCTED_VALIDATOR_PASS_CONDITIONAL_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_SameSource_SymmetryBreaking_Source_v1"
PARALLEL_NEXT = "Selected_Qa_SU3_Finite_Galerkin_to_Smooth_Operator_Promotion_or_NoGo_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    visible = load(VISIBLE_PACKET)
    visible_cert = load(VISIBLE_CERT)
    qa = load(QA_PACKET)
    qa_cert = load(QA_CERT)

    checks = {
        "F0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "F1_visible_lane_reduction_proved": visible["status"] == VISIBLE_STATUS
        and visible["theorem"]["proved"] is True
        and visible["target_fitting_used"] is False
        and visible["next_required_artifact"] == NEXT,
        "F2_rank2_primary_lane_is_live_but_blocked": visible["rank2_lane"]["classification"]
        == "SUPERSET_CONVERGENCE_PRIMARY_FILL_LANE"
        and visible["rank2_lane"]["closed"]["topological_c2_target"] is True
        and visible["rank2_lane"]["closed"]["appell_humbert_automorphy_exists"] is True
        and visible["rank2_lane"]["blocked_by"]["selected_l2_cochain_packet_absent"] is True
        and visible["rank2_lane"]["blocked_by"]["nonzero_ext_not_selected"] is True
        and visible["rank2_lane"]["blocked_by"]["stability_not_proved"] is True,
        "F3_routec_repair_lane_is_live_but_unvalued": visible["route_c_lane"]["classification"]
        == "SUPERSET_REPAIR_PARALLEL_FILL_LANE"
        and visible["route_c_lane"]["closed"]["route_c_residual_schema_formulated"] is True
        and visible["route_c_lane"]["blocked_by"]["actual_selected_rho_E_values"] is True
        and visible["route_c_lane"]["blocked_by"]["actual_Riesz_Green_dotD_data"] is True,
        "F4_common_same_source_blocker_identified": visible["same_source_packet_contract"]["common_blocker"]["name"]
        == "SameSourceSymmetryBreakingSource.v1"
        and "no observed flavor, mass, mixing, or benchmark inputs"
        in visible["same_source_packet_contract"]["common_blocker"]["must_supply"],
        "F5_visible_certificate_agrees": visible_cert["status"] == VISIBLE_STATUS
        and visible_cert["primary_next_artifact"] == NEXT
        and visible_cert["closure_claimed"] is False,
        "F6_qa_minimal_hsel_gret_is_concrete": qa["status"] == QA_STATUS
        and qa["closure_claimed"] is False
        and qa["target_fitting_used"] is False
        and qa["hessian"]["matrix"] == [[26, -3, 0], [-3, 10, 0], [0, 0, 8]]
        and qa["hessian"]["determinant"] == 2008
        and qa["hessian"]["positive_definite"] is True
        and qa["hessian"]["sylvester_minors"] == [26, 251, 2008]
        and qa["green"]["inverse_verified"] is True
        and qa["green"]["identity_check"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        "F7_qa_tau_is_hessian_green_derived_in_finite_model": qa["selection_proof"]["selected_covector"] == [0, 0, 1]
        and qa["selection_proof"]["selected_covector_retarded_norm"] == "1/8"
        and qa["tau"]["all_products_cancel"] is True
        and qa["tau"]["cancellation"]["F1+G1->P"] is True
        and qa["validator_result"]["exit_code"] == 0,
        "F8_qa_certificate_keeps_promotion_open": qa_cert["status"] == QA_STATUS
        and qa_cert["closure_claimed"] is False
        and qa_cert["next_required_artifact"] == PARALLEL_NEXT,
        "F9_no_overclaim": previous["guardrails"]["full_SM_closure_claimed"] is False
        and qa["closure_claimed"] is False
        and visible["target_fitting_used"] is False,
    }

    return {
        "packet": "NonSplitRouteC_and_MinimalHselGret_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "visible_same_source_lane_packet": str(VISIBLE_PACKET),
            "visible_same_source_lane_certificate": str(VISIBLE_CERT),
            "qa_minimal_hsel_gret_packet": str(QA_PACKET),
            "qa_minimal_hsel_gret_certificate": str(QA_CERT),
        },
        "theorem": {
            "name": "NonSplitRouteCMinimalHselGretImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The visible source frontier is reduced to two live same-source "
                "lanes: the preferred non-split rank-two V_alpha lane and the "
                "parallel Route-C finite HYM/Strominger repair lane. Both still "
                "require SameSourceSymmetryBreakingSource.v1. In parallel, Qa/SU3 "
                "now has an explicit finite Galerkin Hessian H_sel, exact rational "
                "G_ret, and H/G-derived tau values. This is a real finite-model "
                "advance, but not smooth/operator or full SM closure."
            ),
        },
        "checks": checks,
        "visible_same_source_lane": visible,
        "qa_minimal_hsel_gret": qa,
        "what_closes_now": {
            "visible_two_lane_reduction_imported": True,
            "rank2_valpha_preferred_fill_lane_identified": True,
            "routec_repair_lane_preserved": True,
            "same_source_symmetry_breaking_source_named_as_common_blocker": True,
            "qa_actual_finite_H_sel_matrix_imported": True,
            "qa_actual_exact_rational_G_ret_imported": True,
            "qa_H_sel_G_ret_identity_verified": True,
            "qa_finite_Pi_tw_plus_e3_selection_imported": True,
            "qa_tau_values_derived_in_finite_model": True,
            "no_target_fitting_reaffirmed": True,
        },
        "what_remains_open": {
            "same_source_symmetry_breaking_source": True,
            "selected_L2_cochain_packet": True,
            "selected_nonzero_Ext_class": True,
            "Pic0_selection_or_physical_quotient": True,
            "non_split_stability_or_selected_RouteC_residual": True,
            "same_source_Chern_Weil_row_derivation": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "primitive_C1_overlap_tensors": True,
            "qa_finite_to_smooth_operator_promotion": True,
            "qa_full_admissibility_packet": True,
            "qa_actual_threshold_determinant_finite_part": True,
            "qa_independent_MTT_Hessian_source_confirmation": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_same_source_symmetry_breaking_source": False,
            "claims_selected_visible_operator_source": False,
            "claims_selected_L2_cochain_or_Ext": False,
            "claims_selected_RouteC_residual": False,
            "claims_selected_DE_dotD_Riesz_Green": False,
            "claims_smooth_Qa_SU3_operator_promotion": False,
            "claims_qa_threshold_determinant": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "parallel_next_required_artifact": PARALLEL_NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "NonSplitRouteCMinimalHselGretImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
        "parallel_next_required_artifact": packet["parallel_next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    hessian = packet["qa_minimal_hsel_gret"]["hessian"]
    green = packet["qa_minimal_hsel_gret"]["green"]
    tau = packet["qa_minimal_hsel_gret"]["tau"]["values"]
    return f"""# NonSplitRouteC and MinimalHselGret Import v1

Status: `{cert["status"]}`.

The visible side has been reduced to two live same-source lanes.  The primary
fill lane is the non-split rank-two `V_alpha` packet; the parallel repair lane
is Route-C finite HYM/Strominger.  Both lanes now share the same blocker:
`SameSourceSymmetryBreakingSource.v1`.

The QA/SU3 side has a concrete finite Galerkin candidate:

```text
H_sel = {hessian["matrix"]}
det(H_sel) = {hessian["determinant"]}
G_ret = {green["matrix"]}
selected covector = [0, 0, 1]
tau = {tau}
```

This closes the finite algebraic `H_sel/G_ret/tau` layer only.  Smooth
same-source operator promotion, selected `D_E/dotD/Riesz/Green`, primitive C1
overlaps, `A_selected`, `b_selected`, Yukawas, and full SM closure remain open.

No observed masses, CKM/PMNS data, benchmark matrices, or target residuals are
used as selectors.

Next artifact: `{cert["next_required_artifact"]}`.
Parallel QA/SU3 artifact: `{cert["parallel_next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
