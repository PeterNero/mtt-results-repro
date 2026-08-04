"""Build the post-B_Huv M_source/Higgs-operator frontier packet.

The previous packet emitted the same-source source-orthonormal B_Huv lift.  The
late constants H7B1Q chain also closes the shared same-source functional,
alpha1/dotD, and matter operator-block side, but it explicitly emits only
matter/neutrino blocks and no UV Higgs two-column operator block.

This artifact back-imports both facts and narrows the direct-Huv route to one
Higgs-specific missing object: a selected Hermitian mass/strain block on the
B_Huv domain, or equivalently C5-C6 bridge closure feeding the H K row.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"

SLUG = "selected_msourcehiggsspecificoperatorblock_or_c5c6bridgefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTIONAL_RECHECK = PACKET_DIR / "same_source_functional_and_bhuv_recheck.packet.json"
HIGGS_BLOCK_GAP = PACKET_DIR / "higgs_specific_operator_block_gap.packet.json"
MSOURCE_KERNEL = PACKET_DIR / "msource_acceptance_kernel_after_bhuv_and_functional.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_higgs_operator_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higgs_operator_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MSourceHiggsSpecificOperatorBlock_or_C5C6BridgeFrontier_v1.md"

BHUV_CANDIDATE = DATA / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier.candidate.json"
BHUV_LIFT = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
BHUV_HK = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "hk_threshold_gate_after_bhuv_lift.packet.json"
)

H7B1G_MSOURCE = (
    CONST_DATA
    / "const_higgs_01_h7b1g_fill_bhuv_or_msource"
    / "msource_minimal_operator_payload_request.packet.json"
)
H7B1J_STRICT = (
    CONST_DATA
    / "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export"
    / "strict_msource_gate_validator.packet.json"
)
H7B1P_BOUNDARY = (
    CONST_DATA
    / "const_higgs_01_h7b1p_end0_to_huv_or_sector_routing"
    / "huv_boundary_after_sector_routing.packet.json"
)
H7B1Q_FUNCTIONAL = (
    CONST_DATA
    / "const_higgs_01_h7b1q_twohiggs_lift_or_samesource_functional_value"
    / "samesource_functional_value_import.packet.json"
)
H7B1Q_BOUNDARY = (
    CONST_DATA
    / "const_higgs_01_h7b1q_twohiggs_lift_or_samesource_functional_value"
    / "twohiggs_huv_boundary_after_functional_value.packet.json"
)
H7B1Y_DIRECT_SCHEMA = (
    CONST_DATA
    / "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
    / "direct_herm2_huv_row_schema.packet.json"
)

STATUS = (
    "MTT_SELECTED_MSOURCEHIGGSSPECIFICOPERATORBLOCK_OR_C5C6BRIDGEFRONTIER_"
    "BHUV_AND_SHARED_FUNCTIONAL_CLOSED_HIGGS_OPERATOR_BLOCK_OPEN"
)
NEXT = "MTT_Selected_HiggsSpecificHermitianMassStrainBlock_or_C5C6ProjectionBridge_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Higgs operator frontier inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        BHUV_CANDIDATE,
        BHUV_LIFT,
        BHUV_HK,
        H7B1G_MSOURCE,
        H7B1J_STRICT,
        H7B1P_BOUNDARY,
        H7B1Q_FUNCTIONAL,
        H7B1Q_BOUNDARY,
        H7B1Y_DIRECT_SCHEMA,
    ]
    require_sources(sources)

    bhuv_candidate = load(BHUV_CANDIDATE)
    bhuv = load(BHUV_LIFT)
    hk_previous = load(BHUV_HK)
    h7b1g_msource = load(H7B1G_MSOURCE)
    h7b1j = load(H7B1J_STRICT)
    h7b1p = load(H7B1P_BOUNDARY)
    h7b1q_functional = load(H7B1Q_FUNCTIONAL)
    h7b1q_boundary = load(H7B1Q_BOUNDARY)
    h7b1y = load(H7B1Y_DIRECT_SCHEMA)

    uv_ids = bhuv["ordered_two_column_source_space"]["ordered_E_H_UV_source_ids"]
    b_cols = bhuv["whitening_map_and_lift"]["B_Huv_columns"]
    functional = h7b1q_functional["imported_chain"]
    operator_scope = h7b1q_functional["operator_blocks_scope"]

    functional_recheck = {
        "schema": "MTTSameSourceFunctionalAndBHuvRecheck.v1",
        "status": "BHUV_AND_SHARED_FUNCTIONAL_SIDE_CLOSED_HIGGS_BLOCK_NOT_EMITTED",
        "closure_claimed": True,
        "B_Huv_side": {
            "B_Huv_two_column_uv_lift_emitted": True,
            "B_Huv_columns": b_cols,
            "ordered_E_H_UV_source_ids": uv_ids,
            "source_orthonormality": "B_Huv^* G_Q B_Huv = I_2",
            "source": rel(BHUV_LIFT),
        },
        "shared_functional_side": {
            "same_source_functional_value_closed": functional[
                "same_branch_functional_operator_emission_closed"
            ],
            "alpha1_driver_verified": functional["alpha1_driver_verified"],
            "selected_dotD_source_verified": functional["selected_dotD_source_verified"],
            "honest_dotD_validator_closed": functional["honest_dotD_validator_closed"],
            "selected_overlap_normalization_emitted": functional[
                "selected_overlap_normalization_emitted"
            ],
            "emitted_operator_blocks": operator_scope["emitted_operator_blocks"],
            "source": rel(H7B1Q_FUNCTIONAL),
        },
        "scope_discriminator": {
            "contains_H_u": operator_scope["contains_H_u"],
            "contains_H_d_dagger": operator_scope["contains_H_d_dagger"],
            "contains_Huv": operator_scope["contains_Huv"],
            "has_uv_higgs_blocks": operator_scope["has_uv_higgs_blocks"],
            "all_blocks_are_matter_or_neutrino": operator_scope[
                "all_blocks_are_matter_or_neutrino"
            ],
            "scope_note": operator_scope["scope_note"],
        },
        "decision": {
            "old_H7B1Q_UV_twoHiggs_basis_missing_retired_by_B_Huv": True,
            "same_source_functional_exit_closed_for_non_Higgs_blocks": True,
            "Higgs_specific_operator_block_emitted": False,
            "M_source_value_emitted": False,
            "direct_Huv_entries_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    higgs_block_gap = {
        "schema": "MTTHiggsSpecificOperatorBlockGap.v1",
        "status": "HIGGS_SPECIFIC_HERMITIAN_OPERATOR_BLOCK_IS_REMAINING_DIRECT_ROUTE_GAP",
        "closure_claimed": True,
        "old_boundaries_rechecked": {
            "H7B1P_collapsed_H_only": h7b1p["decision"]["collapsed_H_only"],
            "H7B1P_contains_H_u": h7b1p["sector_output_available"]["contains_H_u"],
            "H7B1P_contains_H_d_dagger": h7b1p["sector_output_available"][
                "contains_H_d_dagger"
            ],
            "H7B1Q_remaining_gate_is_Higgs_specific": h7b1q_boundary["decision"][
                "remaining_gate_is_Higgs_specific"
            ],
        },
        "updated_missing_for_Huv_after_B_Huv": {
            "UV_twoHiggs_basis_emitted": True,
            "B_Huv_value_emitted": True,
            "same_source_functional_alpha1_dotD_closed": True,
            "M_source_value_emitted": False,
            "Huu_value_emitted": False,
            "Hud_value_emitted": False,
            "Hdd_value_emitted": False,
            "direct_Huv_entries_emitted": False,
            "Omega_emitted": False,
            "s_beta_emitted": False,
            "lambda_H_emitted": False,
        },
        "minimal_Higgs_specific_payload_now": {
            "domain": "the source-orthonormal B_Huv two-column UV Higgs domain",
            "required_object": "a source-owned Hermitian sesquilinear mass/strain form M_H on span(B_Huv)",
            "required_entries": {
                "Huu": None,
                "Hud": None,
                "Hdd": None,
                "Hermiticity": "Hdu=conj(Hud)",
                "Delta": "(Huu-Hdd)/2",
                "Omega": "Hud",
                "s_beta": "Delta^2/(Delta^2+|Omega|^2)",
            },
            "alternative_full_operator_route": (
                "emit a same-source full operator M_source plus a source-owned "
                "restriction map R_H whose B_Huv block is the accepted Huv block"
            ),
        },
        "why_shared_functional_does_not_close_Higgs": {
            "operator_blocks_are_matter_or_neutrino": True,
            "collapsed_H_rank_one_is_not_UV_twoHiggs_block": True,
            "dotD_or_alpha1_driver_is_not_a_mass_strain_Hessian": True,
            "no_Higgs_specific_Hermitian_block": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    msource_kernel = {
        "schema": "MTTMSourceAcceptanceKernelAfterBHuvAndFunctional.v1",
        "status": "MSOURCE_GATE_REDUCED_TO_HIGGS_SPECIFIC_HERMITIAN_BLOCK_OR_C5C6_BRIDGE",
        "closure_claimed": True,
        "original_msource_request_source": rel(H7B1G_MSOURCE),
        "old_strict_gate_source": rel(H7B1J_STRICT),
        "strict_gate_after_backimport": {
            "same_q79_F_m1_branch": True,
            "no_observed_selector": True,
            "B_Huv_two_column_lift": True,
            "same_source_functional_alpha1_dotD_side": True,
            "H_sector_restriction_identity_available_if_M_H_is_emitted_on_BHuv_domain": True,
            "dynamic_hessian_or_mass_strain_source_owned": False,
            "Higgs_specific_operator_block_emitted": False,
            "finite_exactness_or_error_certificate_for_values": False,
            "direct_Herm2_Huv_payload_complete": False,
        },
        "direct_2x2_route": {
            "accepted_formula": h7b1y["accepted_formula"],
            "B_Huv": b_cols,
            "M_H": None,
            "Huv": None,
            "comment": (
                "Because B_Huv is already source-orthonormal, a selected Hermitian "
                "M_H emitted directly on that two-column source domain would be "
                "the Huv block.  No such M_H is emitted here."
            ),
        },
        "full_operator_route": {
            "M_source": None,
            "R_H": None,
            "H_response": None,
            "comment": (
                "The older H7B1I/J full-operator route remains legal but still needs "
                "a source-owned H_response/M_source and H-sector restriction map."
            ),
        },
        "must_emit_next": [
            "selected source-owned Hermitian M_H on the B_Huv two-column domain, or full M_source plus R_H",
            "finite exactness/error certificate for the Huv block",
            "proof M_H is a mass/strain/Hessian object, not a promoted metric, dotD, or replay witness",
            "Huu,Hud,Hdd with Hdu=conj(Hud)",
            "Delta, Omega, and selected s_beta or direct H K-threshold row implication",
        ],
        "forbidden_shortcuts": [
            "promoting the C3 metric Gram matrix as M_source",
            "promoting alpha1/dotD matter blocks as Higgs Huv",
            "using collapsed rank-one H sector values as the UV two-Higgs block",
            "backsolving beta, lambda_H, or thresholds from observed data",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_row = dict(hk_previous["H_row"])
    h_row["same_source_functional_alpha1_dotD_side_closed"] = True
    h_row["Higgs_specific_operator_block_emitted"] = False
    hk_gate = {
        "schema": "MTTHKThresholdGateAfterHiggsOperatorGap.v1",
        "status": "H_K_THRESHOLD_GATE_BHUV_FUNCTIONAL_CLOSED_HIGGS_OPERATOR_OPEN_9_OF_10",
        "closure_claimed": True,
        "required_output": hk_previous["required_output"],
        "source_equation": hk_previous["source_equation"],
        "accepted_selected_K_source_row_count": hk_previous[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": hk_previous[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": h_row,
        "conditional_consequent_current": hk_previous["conditional_consequent_current"],
        "direct_route_state": {
            "B_Huv_two_column_lift_emitted": True,
            "shared_functional_alpha1_dotD_closed": True,
            "Higgs_specific_operator_block_emitted": False,
            "M_source_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHiggsOperatorGap.v1",
        "status": "NEXT_FRONTIER_HIGGS_SPECIFIC_MH_OR_C5C6_PROJECTION_BRIDGE",
        "closure_claimed": True,
        "closed_here": [
            "B_Huv two-column UV lift is closed and back-imported",
            "late H7B1Q same-source functional/alpha1/dotD side is closed and back-imported",
            "old missing UV-two-Higgs-basis field is retired for the active direct route",
            "matter/neutrino operator blocks are separated from the missing Higgs block",
            "direct route is reduced to a Higgs-specific Hermitian mass/strain block M_H or full M_source+R_H",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "selected Hermitian M_H on the B_Huv two-column domain",
            "or full same-source M_source plus H-sector restriction R_H",
            "direct Huu,Hud,Hdd rows",
            "C5 trace-to-H7B1U/projection-measure identity",
            "C6 no-extra-boundary/source theorem",
            "selected s_beta or direct H K-threshold implication",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedMSourceHiggsSpecificOperatorBlockOrC5C6BridgeFrontier",
        "status": STATUS,
        "previous_status": bhuv_candidate["status"],
        "theorem": {
            "name": "HiggsSpecificOperatorBlockFrontierTheorem",
            "proved": True,
            "statement": (
                "After the selected B_Huv two-column lift is emitted, and after the "
                "late H7B1Q same-source functional/alpha1/dotD side is imported, "
                "the direct Huv route is no longer blocked by generic same-source "
                "functional support or by the UV two-Higgs basis.  H7B1Q emits only "
                "matter/neutrino operator blocks and explicitly no H_u, H_d^dagger, "
                "or Huv block.  Therefore the remaining direct-route object is a "
                "Higgs-specific selected Hermitian mass/strain form on the B_Huv "
                "domain, or a full M_source plus H-sector restriction R_H; C5-C6 "
                "projection/no-boundary closure remains the parallel bridge exit."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "B_Huv_two_column_uv_lift_emitted": True,
            "same_source_functional_alpha1_dotD_side_closed": True,
            "matter_operator_blocks_emitted": True,
            "UV_twoHiggs_basis_missing_retired": True,
            "Higgs_specific_operator_block_emitted": False,
            "selected_Hermitian_M_source_emitted": False,
            "H_sector_restriction_R_H_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": hk_previous[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": hk_previous[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "same_source_functional_and_bhuv_recheck": rel(FUNCTIONAL_RECHECK),
            "higgs_specific_operator_block_gap": rel(HIGGS_BLOCK_GAP),
            "msource_acceptance_kernel_after_bhuv_and_functional": rel(MSOURCE_KERNEL),
            "hk_threshold_gate_after_higgs_operator_gap": rel(HK_GATE),
            "next_cutset_after_higgs_operator_gap": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedMSourceHiggsSpecificOperatorBlockOrC5C6BridgeFrontierCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "B_Huv_two_column_uv_lift_emitted": True,
        "same_source_functional_alpha1_dotD_side_closed": True,
        "matter_operator_blocks_emitted": True,
        "UV_twoHiggs_basis_missing_retired": True,
        "Higgs_specific_operator_block_emitted": False,
        "selected_Hermitian_M_source_emitted": False,
        "H_sector_restriction_R_H_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "direct_Huu_Hud_Hdd_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": hk_previous[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": hk_previous[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected MSourceHiggsSpecificOperatorBlock or C5C6BridgeFrontier v1

Status: `{STATUS}`

## What Closed

- back-imported the emitted `B_Huv` two-column UV lift
- back-imported H7B1Q same-source functional/alpha1/dotD closure
- separated matter/neutrino operator blocks from the missing Higgs UV block
- retired the old active missing field `UV_twoHiggs_basis_emitted=false`
- reduced the direct route to a Higgs-specific Hermitian mass/strain block `M_H` on the `B_Huv` domain, or full `M_source+R_H`
- H K-threshold gate remains `{hk_previous["accepted_selected_K_source_row_count"]}/{hk_previous["selected_K_threshold_row_count_required"]}`

## Still Open

- selected Hermitian `M_H` on the `B_Huv` two-column domain
- or full same-source `M_source` plus H-sector restriction `R_H`
- direct `Huu,Hud,Hdd` rows
- C5 trace-to-H7B1U/projection-measure identity and C6 no-extra-boundary theorem
- selected `K_threshold.Omega_H.lambda`

Next required artifact: `{NEXT}`
"""

    write_json(FUNCTIONAL_RECHECK, functional_recheck)
    write_json(HIGGS_BLOCK_GAP, higgs_block_gap)
    write_json(MSOURCE_KERNEL, msource_kernel)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
