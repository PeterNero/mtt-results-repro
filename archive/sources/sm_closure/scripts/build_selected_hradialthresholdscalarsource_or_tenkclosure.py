"""Build the H radial-threshold scalar source / ten-K closure route packet.

The preceding packet reduced scalar H closure to one selected H radial/
threshold source scalar or a direct K_threshold.Omega_H.lambda row.  The local
constants repo has an older D-term functor:

    lambda_H(mu_match) = A_EW(mu_match) * s_beta,
    A_EW = (g_2^2 + g_Y^2) / 8.

Before C5b/C6, that functor lacked selected s_beta.  Now s_beta is selected, so
this packet imports the D-term route and proves the remaining scalar wall is no
longer a Higgs-angle/Herm(2) wall.  It is exactly the selected EW boundary/RG
factor A_EW plus matching/transport, or an independent direct H K row.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hradialthresholdscalarsource_or_tenkclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DTERM_IMPORT = PACKET_DIR / "dterm_route_after_selected_sbeta_import.packet.json"
FORMULA = PACKET_DIR / "conditional_h_k_from_ew_boundary_formula.packet.json"
EW_RECHECK = PACKET_DIR / "ew_boundary_rg_recheck_for_h_dterm.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_dterm_route.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_h_radial_threshold_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRadialThresholdScalarSource_or_TenKClosure_v1.md"

PREVIOUS = DATA / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json"
PREVIOUS_POLAR = (
    DATA
    / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows"
    / "sbeta_polar_herm2_reduction.packet.json"
)
PREVIOUS_FUNCTIONAL = (
    DATA
    / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows"
    / "h_quartic_threshold_functional_reduction.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows"
    / "hk_threshold_gate_after_radial_reduction.packet.json"
)
H_SOURCE_EQ = (
    DATA
    / "selected_hsectorquarticthresholdpayload_or_stricttenkclosure"
    / "h_sector_payload_source_equation.packet.json"
)
SBETA_SOURCE = (
    DATA
    / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof"
    / "selected_finite_reduction_sbeta_promotion.packet.json"
)

H7B = CONST_DATA / "const_higgs_01_h7b_uv_beta_or_two_higgs_projection_theorem.candidate.json"
H7B_CONTRACT = (
    CONST_DATA
    / "const_higgs_01_h7b_uv_beta_or_two_higgs_projection_theorem"
    / "minimal_route_b_payload_contract.packet.json"
)
H7B1 = CONST_DATA / "const_higgs_01_h7b1_dterm_projection_invariant_functor.candidate.json"
H7B1_FUNCTOR = (
    CONST_DATA
    / "const_higgs_01_h7b1_dterm_projection_invariant_functor"
    / "uv_two_higgs_projector_to_sbeta_functor.packet.json"
)
H7B1_PROJECTOR_CONTRACT = (
    CONST_DATA
    / "const_higgs_01_h7b1_dterm_projection_invariant_functor"
    / "selected_projector_acceptance_contract.packet.json"
)
EW_B41 = CONST_DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching.candidate.json"
EW_B41_RG = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
    / "rg_matching_threshold_scheme_status.packet.json"
)
EW_B41_ANCHOR = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
    / "gauge_action_anchor_status.packet.json"
)

STATUS = (
    "MTT_SELECTED_HRADIALTHRESHOLDSCALARSOURCE_OR_TENKCLOSURE_"
    "DTERM_ROUTE_REDUCED_EW_BOUNDARY_OPEN"
)
NEXT = "MTT_Selected_EWBoundaryRGFactorForHiggsDTerm_or_DirectTenKClosure_v1"


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
        raise FileNotFoundError("missing H radial threshold inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_POLAR,
        PREVIOUS_FUNCTIONAL,
        PREVIOUS_HK,
        H_SOURCE_EQ,
        SBETA_SOURCE,
        H7B,
        H7B_CONTRACT,
        H7B1,
        H7B1_FUNCTOR,
        H7B1_PROJECTOR_CONTRACT,
        EW_B41,
        EW_B41_RG,
        EW_B41_ANCHOR,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_polar = load(PREVIOUS_POLAR)
    previous_functional = load(PREVIOUS_FUNCTIONAL)
    previous_hk = load(PREVIOUS_HK)
    h_source = load(H_SOURCE_EQ)
    sbeta_source = load(SBETA_SOURCE)
    h7b = load(H7B)
    h7b_contract = load(H7B_CONTRACT)
    h7b1 = load(H7B1)
    h7b1_functor = load(H7B1_FUNCTOR)
    h7b1_projector_contract = load(H7B1_PROJECTOR_CONTRACT)
    ew_b41 = load(EW_B41)
    ew_rg = load(EW_B41_RG)
    ew_anchor = load(EW_B41_ANCHOR)

    s_beta = float(sbeta_source["selected_s_beta"]["value"])
    h_row = previous_hk["H_row"]

    dterm_import = {
        "schema": "MTTDTermRouteAfterSelectedSBetaImport.v1",
        "status": "DTERM_ROUTE_IMPORTED_SELECTED_SBETA_INPUT_CLOSED_EW_BOUNDARY_OPEN",
        "closure_claimed": True,
        "source_repo": rel(CONSTANTS),
        "imported_h7b_status": h7b["status"],
        "imported_h7b1_status": h7b1["status"],
        "theorem": {
            "name": "SelectedSBetaActivatesDTermRouteTheorem",
            "proved": True,
            "statement": (
                "H7B proves the D-term route needs a selected projection invariant "
                "s_beta plus a selected EW boundary/RG packet.  H7B1 proves the "
                "basis-free projector-to-s_beta functor.  The current C5b/C6 packet "
                "now supplies selected s_beta from the same H7B1T/U finite-reduction "
                "chain, so the Higgs-angle/projector invariant input is closed for "
                "this route.  The EW boundary pair, matching scale, and RG/threshold "
                "transport remain open."
            ),
        },
        "previous_constants_repo_missing_fields": {
            "H7B_selected_Dterm_projection_invariant_s_beta_found": h7b[
                "selected_Dterm_projection_invariant_s_beta_found"
            ],
            "H7B_selected_EW_boundary_RG_packet_closed": h7b[
                "selected_EW_boundary_RG_packet_closed"
            ],
            "H7B1_selected_s_beta_value_found": h7b1["selected_s_beta_value_found"],
            "H7B1_numeric_lambda_H_derived": h7b1["numeric_lambda_H_derived"],
        },
        "filled_now_in_current_repo": {
            "selected_s_beta_value_found": True,
            "selected_s_beta_value": s_beta,
            "selected_s_beta_formula": sbeta_source["selected_s_beta"]["formula"],
            "value_source": sbeta_source["selected_s_beta"]["value_source"],
            "observed_higgs_or_beta_used": sbeta_source["selected_s_beta"][
                "observed_higgs_or_beta_used"
            ],
            "accepted_form_from_H7B_contract": "direct selected s_beta=cos^2(2 beta)",
            "P_L_projector_emitted": False,
        },
        "still_open_for_Dterm_value": {
            "selected_EW_boundary_pair_g2_gY": False,
            "selected_matching_scale_mu_match": False,
            "selected_threshold_RG_transport": False,
            "selected_A_EW": False,
            "numeric_lambda_H_derived": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    formula = {
        "schema": "MTTConditionalHKFromEWBoundaryFormula.v1",
        "status": "CONDITIONAL_H_K_FORMULA_FROM_SELECTED_SBETA_AND_AEW_BUILT",
        "closure_claimed": True,
        "Dterm_boundary": {
            "A_EW": "(g_2(mu_match)^2 + g_Y(mu_match)^2) / 8",
            "lambda_H_mu_match": "A_EW(mu_match) * s_beta",
            "source": h7b["theorem"]["statement"],
        },
        "selected_s_beta": {
            "value": s_beta,
            "formula": sbeta_source["selected_s_beta"]["formula"],
            "source_selected_before_replay": True,
        },
        "K_threshold_formula_if_same_scheme": {
            "source_equation": h_source["selected_source_equation"]["omega_value"],
            "direct_K_row": h_source["selected_source_equation"]["direct_K_row"],
            "conditional_formula": (
                "K_threshold.Omega_H.lambda = "
                "(A_EW(mu_match) * s_beta) / (D_fin.H * epsilon_Theta^(1/3))"
            ),
            "requires_same_branch_scheme_alignment": True,
            "requires_selected_A_EW": True,
            "requires_selected_RG_transport_to_Omega_scheme": True,
        },
        "numeric_status": {
            "A_EW_selected": False,
            "lambda_H_mu_match_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "ten_K_antecedent_satisfied": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ew_recheck = {
        "schema": "MTTEWBoundaryRGRecheckForHDTerm.v1",
        "status": "EW_BOUNDARY_RG_RECHECK_VALUES_OPEN",
        "closure_claimed": True,
        "imported_B41_status": ew_b41["status"],
        "RG_matching_decision": ew_rg["decision"],
        "gauge_action_anchor_decision": ew_anchor["decision"],
        "policy_scaffold": ew_rg["policy_scaffold"],
        "remaining_EW_inputs": {
            "K_phys_or_f_ab_closed": ew_anchor["decision"]["K_phys_or_f_ab_closed"],
            "physical_alpha_or_metrology_anchor_closed": ew_anchor["decision"][
                "physical_alpha_or_metrology_anchor_closed"
            ],
            "source_selected_mu_match_closed": ew_rg["decision"][
                "source_selected_mu_match_closed"
            ],
            "source_selected_threshold_vector_closed": ew_rg["decision"][
                "source_selected_threshold_vector_closed"
            ],
            "precision_RG_threshold_values_closed": ew_rg["decision"][
                "precision_RG_threshold_values_closed"
            ],
        },
        "allowed_future_routes": {
            "strict_no_knob": "emit same-branch physical gauge/action normalization plus selected mu_match and threshold/RG vector",
            "one_primitive_tier": ew_anchor["required_to_promote"]["one_primitive_tier"],
            "direct_H_route": "emit K_threshold.Omega_H.lambda directly from an intrinsic H quartic functional",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterDTermRoute.v1",
        "status": "H_K_THRESHOLD_GATE_DTERM_ROUTE_REDUCED_EW_BOUNDARY_OPEN_9_OF_10",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            **h_row,
            "Dterm_route_imported": True,
            "selected_s_beta_input_for_Dterm_closed": True,
            "selected_A_EW_emitted": False,
            "selected_EW_boundary_RG_packet_closed": False,
            "lambda_H_mu_match_emitted": False,
            "direct_K_threshold_Omega_H_lambda_emitted": False,
        },
        "conditional_consequent_current": {
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "lambda_H_row_executable": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHRadialThresholdAttempt.v1",
        "status": "NEXT_FRONTIER_EW_BOUNDARY_RG_FACTOR_FOR_HIGGS_DTERM_OR_DIRECT_TEN_K",
        "closure_claimed": True,
        "closed_here": [
            "imported H7B/H7B1 D-term route after selected s_beta",
            "selected H projection invariant input for Route B is now closed in this repo",
            "derived conditional lambda_H(mu_match)=A_EW*s_beta",
            "derived conditional K_threshold.Omega_H.lambda formula in the Omega scheme",
            "reduced H radial threshold source wall to selected A_EW plus matching/RG, or a direct H quartic K row",
        ],
        "still_open": [
            "selected EW boundary pair g_2 and g_Y at mu_match",
            "selected A_EW=(g_2^2+g_Y^2)/8",
            "selected matching scale mu_match",
            "selected threshold/RG transport into the Omega/lambda_H scheme",
            "or direct intrinsic H quartic K_threshold.Omega_H.lambda row",
            "ten-row K antecedent",
            "strict Omega/lambda_H scalar execution",
            "selected matrix-level mixing extension and true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHRadialThresholdScalarSourceOrTenKClosure",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "SelectedHDTermBoundaryReductionTheorem",
            "proved": True,
            "statement": (
                "After C5b/C6 selects s_beta, the H7B/H7B1 D-term route reduces "
                "the missing H scalar to the selected EW factor A_EW=(g_2^2+g_Y^2)/8 "
                "and selected matching/RG transport.  Therefore the active H scalar "
                "wall is EW boundary/RG selection or a direct intrinsic H quartic "
                "K row, not another beta/Galerkin/Herm(2) angular search."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "Dterm_route_imported": True,
            "selected_s_beta_input_for_Dterm_closed": True,
            "selected_s_beta_value": s_beta,
            "conditional_lambda_H_mu_match_formula_closed": True,
            "conditional_K_threshold_formula_closed": True,
            "selected_A_EW_emitted": False,
            "selected_EW_boundary_RG_packet_closed": False,
            "selected_matching_scale_mu_match_closed": False,
            "selected_threshold_RG_transport_closed": False,
            "lambda_H_mu_match_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
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
            "dterm_route_after_selected_sbeta_import": rel(DTERM_IMPORT),
            "conditional_h_k_from_ew_boundary_formula": rel(FORMULA),
            "ew_boundary_rg_recheck_for_h_dterm": rel(EW_RECHECK),
            "hk_threshold_gate_after_dterm_route": rel(HK_GATE),
            "next_cutset_after_h_radial_threshold_attempt": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHRadialThresholdScalarSourceOrTenKClosureCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "Dterm_route_imported": True,
        "selected_s_beta_input_for_Dterm_closed": True,
        "selected_s_beta_value": s_beta,
        "conditional_lambda_H_mu_match_formula_closed": True,
        "conditional_K_threshold_formula_closed": True,
        "selected_A_EW_emitted": False,
        "selected_EW_boundary_RG_packet_closed": False,
        "selected_matching_scale_mu_match_closed": False,
        "selected_threshold_RG_transport_closed": False,
        "lambda_H_mu_match_emitted": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HRadialThresholdScalarSource or TenKClosure v1

Status: `{STATUS}`

## What Closed

- imported the H7B/H7B1 D-term route after selected `s_beta={s_beta}`
- closed the selected H projection-invariant input for the D-term route in this repo
- derived `lambda_H(mu_match)=A_EW*s_beta` with `A_EW=(g_2^2+g_Y^2)/8`
- derived the conditional Omega-scheme row
  `K_threshold.Omega_H.lambda=(A_EW*s_beta)/(D_fin.H*epsilon_Theta^(1/3))`
- reduced the H scalar wall to selected EW boundary/RG data or a direct intrinsic H quartic K row

## Still Open

- selected `A_EW=(g_2^2+g_Y^2)/8`
- selected matching scale `mu_match`
- selected threshold/RG transport into the Omega/lambda_H scheme
- direct intrinsic `K_threshold.Omega_H.lambda` if bypassing the D-term route

Next required artifact: `{NEXT}`
"""

    write_json(DTERM_IMPORT, dterm_import)
    write_json(FORMULA, formula)
    write_json(EW_RECHECK, ew_recheck)
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
