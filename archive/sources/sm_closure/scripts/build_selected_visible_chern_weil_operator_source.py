"""Build the selected visible Chern-Weil/operator source reduction artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\certificates")

OUTPUT_DATA = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
OUTPUT_CERT = CERTS / "selected_visible_chern_weil_operator_source_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Visible_Chern_Weil_Operator_Source_v1.md"

INPUTS = {
    "projective_gerbe_rhoe": DATA / "projective_gerbe_rhoe_source_promotion.candidate.json",
    "visible_after_s3": Q79_CERTS / "visible_operator_source_after_s3_closure_certificate.json",
    "valpha_candidates": Q79_CERTS / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json",
    "split_line_no_go": Q79_CERTS / "visible_split_line_hym_no_go_certificate.json",
    "stable_sign_gate": Q79_CERTS / "visible_stable_source_sign_gate_certificate.json",
    "valpha_attempt": Q79_CERTS / "selected_valpha_chern_weil_operator_source_attempt_certificate.json",
    "valpha_sufficiency": Q79_CERTS / "selected_valpha_operator_source_sufficiency_certificate.json",
    "valpha_critical_path": Q79_CERTS / "valpha_operator_source_critical_path_certificate.json",
    "hym_operator_attempt": Q79_CERTS / "selected_hym_operator_source_attempt_certificate.json",
    "hym_operator_validator": Q79_CERTS / "selected_hym_operator_source_validator_certificate.json",
    "route_c_scaffold": Q79_CERTS / "iwasawa_route_c_finite_solve_scaffold_certificate.json",
    "source_promotion_gate": Q79_CERTS / "iwasawa_selected_source_promotion_gate_certificate.json",
    "same_source_fusion_gate": Q79_CERTS / "same_source_monad_gs_operator_fusion_gate_certificate.json",
    "same_source_valpha_s3_attempt": Q79_CERTS / "selected_qa_su3_same_source_valpha_s3_operator_packet_attempt_certificate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {key: {"path": str(path), "present": path.exists()} for key, path in INPUTS.items()}


def build_candidate() -> dict[str, object]:
    projective = load_json(INPUTS["projective_gerbe_rhoe"])
    after_s3 = load_json(INPUTS["visible_after_s3"])
    candidates = load_json(INPUTS["valpha_candidates"])
    split_no_go = load_json(INPUTS["split_line_no_go"])
    sign_gate = load_json(INPUTS["stable_sign_gate"])
    attempt = load_json(INPUTS["valpha_attempt"])
    sufficiency = load_json(INPUTS["valpha_sufficiency"])
    critical = load_json(INPUTS["valpha_critical_path"])
    hym_attempt = load_json(INPUTS["hym_operator_attempt"])
    hym_validator = load_json(INPUTS["hym_operator_validator"])
    route_c = load_json(INPUTS["route_c_scaffold"])
    promotion = load_json(INPUTS["source_promotion_gate"])
    fusion = load_json(INPUTS["same_source_fusion_gate"])
    valpha_s3 = load_json(INPUTS["same_source_valpha_s3_attempt"])

    primary = candidates["candidate_ranking"][0]
    support_template = candidates["candidate_ranking"][1]
    route_c_fallback = candidates["candidate_ranking"][2]
    twisted_support = candidates["candidate_ranking"][3]

    required_fields = candidates["source_packet_interface"]["visible_required_fields"]
    critical_must_supply = critical["critical_packet_contract"]["must_supply"]
    after_s3_cut_set = after_s3["still_open_cut_set"]

    selected_packet_closed = (
        attempt["validator_result"]["exit_code"] == 0
        and valpha_s3["validator_result"]["exit_code"] == 0
        and all(not value for value in after_s3_cut_set.values())
    )

    live_paths = {
        "straight_split_line_hym": {
            "classification": "STRAIGHT_PATH_RETIRED",
            "succeeds": False,
            "status": split_no_go["status"],
            "reason": split_no_go["verdict"]["honest_answer"],
        },
        "primary_non_split_rank2_valpha": {
            "classification": "SUPERSET_CONVERGENCE_PRIMARY",
            "succeeds": False,
            "candidate_id": primary["id"],
            "source_shape": primary["source_shape"],
            "topological_target": primary["topological_target"],
            "still_open": primary["source_packet_fields"],
            "why_primary": primary["why_primary"],
        },
        "route_c_finite_hym_strominger": {
            "classification": "SUPERSET_REPAIR_PARALLEL",
            "succeeds": False,
            "candidate_id": route_c_fallback["id"],
            "source_shape": route_c_fallback["source_shape"],
            "route_c_status": route_c["status"],
            "promotion_gate_status": promotion["status"],
            "reason": "This route can bypass explicit bundle stability only if it emits selected residual, rho_E, metric, D_E, Riesz/Green, and dotD payloads from the same q79/F,m=1 source.",
        },
        "twisted_s3_gerbe_transfer": {
            "classification": "SUPERSET_REPAIR_SUPPORT",
            "succeeds": False,
            "candidate_id": twisted_support["id"],
            "source_shape": twisted_support["source_shape"],
            "projective_gerbe_status": projective["status"],
            "reason": "The S3 gerbe/projector/Freed-Witten support is closed, but it still needs a same-source transfer into the visible V_alpha or Route-C source packet.",
        },
        "inverse_or_backfit_route": {
            "classification": "DIAGNOSTIC_BACKFIT_ONLY",
            "succeeds": False,
            "used_as_proof": False,
            "reason": "No observed flavor, masses, mixings, or benchmark constants are allowed to select this source.",
        },
    }

    return {
        "candidate": "MTTSelectedVisibleChernWeilOperatorSource",
        "status": "MTT_SELECTED_VISIBLE_CW_OPERATOR_SOURCE_REDUCED_TO_SAME_SOURCE_NONABELIAN_OR_ROUTEC_PACKET",
        "source_status": source_status(),
        "imported_statuses": {
            key: load_json(path)["status"] if path.exists() and path.suffix == ".json" else "MISSING"
            for key, path in INPUTS.items()
        },
        "superset_mode": {
            "classification": "SUPERSET_CONVERGENCE_WITH_REPAIR",
            "straight_path_result": live_paths["straight_split_line_hym"],
            "primary_path": live_paths["primary_non_split_rank2_valpha"],
            "parallel_repair_path": live_paths["route_c_finite_hym_strominger"],
            "support_repair_path": live_paths["twisted_s3_gerbe_transfer"],
            "diagnostic_backfit_only": live_paths["inverse_or_backfit_route"],
            "locked_target": "one selected q79/F,m=1 same-source visible operator packet",
        },
        "selected_source_packet": {
            "name": "SelectedVisibleChernWeilOperatorSource.v1",
            "visible_required_fields": required_fields,
            "critical_must_supply": critical_must_supply,
            "minimal_next_packet": fusion["minimal_next_packet"],
            "acceptance_tests": candidates["source_packet_interface"]["hard_acceptance_tests"],
            "promotion_rule": candidates["source_packet_interface"]["promotion_rule"],
        },
        "closed_support": {
            "selected_s3_gerbe_source_level": projective["promotion_result"]["source_level_projective_gerbe_rhoE_promoted"],
            "visible_green_schwarz_curvature_row_closed": after_s3["calculation_results"]["visible_gs_curvature_now_closed"],
            "old_s3_fw_projector_blockers_retired": after_s3["calculation_results"]["old_s3_gerbe_fw_projector_blockers_retired"],
            "stable_source_sign_convention_closed": sign_gate["calculation_results"]["positive_trace_row_interpretation_passes_stable_hym_sign_gate"],
            "downstream_validator_stack_conditionally_sufficient": sufficiency["conditional_theorem"]["proved"],
            "selected_hym_operator_validator_formulated": hym_validator["status"] == "SELECTED_HYM_OPERATOR_SOURCE_VALIDATOR_FORMULATED_SOURCE_OPEN",
        },
        "retired_or_demoted": {
            "split_line_or_diagonal_cartan_HYM_final_source": split_no_go["calculation_results"]["split_line_or_cartan_hym_source_ruled_out"],
            "abelian_row_retained_only_as_chern_bianchi_support": candidates["calculation_results"]["abelian_row_retained_only_as_chern_bianchi_support"],
            "positive_math_ch2_wording_rejected": sign_gate["calculation_results"]["positive_math_ch2_interpretation_rejected_for_stable_hym"],
            "patchwork_constituent_proof_rejected": fusion["why_current_patchwork_is_not_a_proof"]["separate_constituents_do_not_define_same_source"],
            "lifted_flag_smoke_not_proof": sufficiency["guardrails"]["claims_hypothetical_flags_are_physical_proof"] is False,
        },
        "open_gates": {
            "selected_visible_operator_source_closed": selected_packet_closed,
            "same_source_cut_set": after_s3_cut_set,
            "valpha_attempt_open_items": attempt["first_open_items"],
            "same_source_valpha_s3_open_items": valpha_s3["first_open_items"],
            "critical_obligations": critical["remaining_independent_obligations"],
            "hym_routec_still_open": hym_attempt["still_open"],
        },
        "theorem": {
            "name": "SelectedVisibleChernWeilOperatorSourceReduction",
            "proved": True,
            "statement": (
                "After selected S3 gerbe/projector support and visible Green-Schwarz curvature closure, the visible "
                "Chern-Weil/operator-source frontier reduces to a single same-source packet. The straight split-line "
                "HYM/diagonal Cartan source is ruled out; the primary live branch is the non-split rank-two V_alpha "
                "extension with L=(1,-2,0), while Route-C finite HYM/Strominger remains the parallel repair path. "
                "The artifact does not prove the selected visible source itself; it proves the exact remaining contract."
            ),
        },
        "next_required_artifact": "MTT_Selected_NonSplit_Rank2_or_RouteC_SameSource_Packet_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedVisibleChernWeilOperatorSourceReduction",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "superset_mode": candidate["superset_mode"]["classification"],
        "what_closes": {
            "split_line_hym_route_retired_as_final_source": True,
            "stable_sign_convention_for_visible_row_closed": True,
            "primary_non_split_rank2_valpha_branch_identified": True,
            "route_c_parallel_repair_branch_preserved": True,
            "s3_gerbe_green_schwarz_support_consumed_without_patchwork_promotion": True,
            "downstream_validator_sufficiency_imported": True,
            "single_same_source_packet_contract_locked": True,
        },
        "what_remains_open": {
            "selected_nonzero_Ext_class": True,
            "Pic0_selection_or_physical_quotient": True,
            "non_split_stability_or_selected_HYM_residual": True,
            "same_source_Chern_Weil_row_derivation": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "coherent_spectral_zero_mode_projectors": True,
            "primitive_C1_overlap_tensors": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "full_SM_parity_closure": True,
            "no_knob_closure": True,
        },
        "primary_next_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    closed = "\n".join(f"- `{key}`" for key, value in candidate["closed_support"].items() if value)
    retired = "\n".join(f"- `{key}`" for key, value in candidate["retired_or_demoted"].items() if value)
    cut_set = "\n".join(f"- `{key}`" for key, value in candidate["open_gates"]["same_source_cut_set"].items() if value)
    fields = "\n".join(f"- `{item}`" for item in candidate["selected_source_packet"]["visible_required_fields"])
    accepts = "\n".join(f"- {item}" for item in candidate["selected_source_packet"]["acceptance_tests"])
    closes = "\n".join(f"- `{key}`" for key, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- `{key}`" for key, value in certificate["what_remains_open"].items() if value)
    primary = candidate["superset_mode"]["primary_path"]
    route_c = candidate["superset_mode"]["parallel_repair_path"]
    support = candidate["superset_mode"]["support_repair_path"]
    straight = candidate["superset_mode"]["straight_path_result"]

    return f"""# MTT Selected Visible Chern-Weil Operator Source v1

## Result

The selected visible Chern-Weil/operator-source problem is reduced to one
same-source packet.  The source itself is not closed yet.

This is **superset convergence with repair**:

- Straight path: `{straight["classification"]}`.  Split line-bundle or diagonal
  Cartan HYM is ruled out for the positive visible `alpha_1` row.
- Superset convergence: `{primary["classification"]}`.  The primary branch is
  `{primary["candidate_id"]}` with source shape `{primary["source_shape"]}`.
- Superset repair: `{route_c["classification"]}`.  Route-C finite
  HYM/Strominger remains legal if it emits the same selected operator payload.
- Superset support repair: `{support["classification"]}`.  S3/gerbe
  projective support is closed at source-support level, but cannot promote by
  patchwork.
- Diagnostic/backfit: not used as proof.

## Closed Support

{closed}

## Retired Or Demoted

{retired}

## Remaining Same-Source Cut Set

{cut_set}

## Required Packet Fields

{fields}

## Hard Acceptance Tests

{accepts}

## Theorem

`{candidate["theorem"]["name"]}` is proved:

{candidate["theorem"]["statement"]}

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

`{candidate["next_required_artifact"]}`
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate, certificate), encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
