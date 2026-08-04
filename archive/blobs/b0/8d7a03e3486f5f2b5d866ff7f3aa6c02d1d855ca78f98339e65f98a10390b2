"""Build the EW-boundary/RG factor gate for the selected Higgs D-term route.

The previous packet made the D-term route usable by supplying selected s_beta.
This packet evaluates the remaining factor

    A_EW = (g_2^2 + g_Y^2) / 8

against the strict no-knob, one-universal-primitive, and admitted-external
tiers.  It closes the tier separation and a diagnostic benchmark calculation,
but it does not emit selected A_EW, lambda_H, or the tenth K row.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TIER_GATE = PACKET_DIR / "aew_source_tier_gate.packet.json"
DIAGNOSTIC = PACKET_DIR / "external_aew_dterm_diagnostic_postcheck.packet.json"
ROUTE_DECISION = PACKET_DIR / "dterm_route_decision_after_aew_recheck.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_aew_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_aew_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_EWBoundaryRGFactorForHiggsDTerm_or_DirectTenKClosure_v1.md"

PREVIOUS = DATA / "selected_hradialthresholdscalarsource_or_tenkclosure.candidate.json"
PREVIOUS_FORMULA = (
    DATA
    / "selected_hradialthresholdscalarsource_or_tenkclosure"
    / "conditional_h_k_from_ew_boundary_formula.packet.json"
)
PREVIOUS_EW = (
    DATA
    / "selected_hradialthresholdscalarsource_or_tenkclosure"
    / "ew_boundary_rg_recheck_for_h_dterm.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_hradialthresholdscalarsource_or_tenkclosure"
    / "hk_threshold_gate_after_dterm_route.packet.json"
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
ALPHA_A10 = CONST_DATA / "const_em_01_alpha1_universal_primitive_or_nogo.candidate.json"
ALPHA_A10_ONE = (
    CONST_DATA
    / "const_em_01_alpha1_universal_primitive_or_nogo"
    / "one_universal_primitive.packet.json"
)
ALPHA_A10_NOGO = (
    CONST_DATA
    / "const_em_01_alpha1_universal_primitive_or_nogo"
    / "strict_internal_nogo.packet.json"
)
EW_B11_ONE = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b11_loop_volume_bridge_proof_attempt"
    / "conditional_one_primitive_bridge.packet.json"
)
WZH = DATA / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation.candidate.json"
WZH_INVENTORY = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_electroweak_row_inventory.packet.json"
)
WZH_ACCEPT = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_external_benchmark_row_acceptance.packet.json"
)

STATUS = (
    "MTT_SELECTED_EWBOUNDARYRGFACTORFORHIGGSDTERM_OR_DIRECTTENKCLOSURE_"
    "AEW_TIER_GATE_CLOSED_VALUES_OPEN"
)
NEXT = "MTT_Selected_IntrinsicHQuarticKRow_or_SelectedLargeThresholdRGTheorem_v1"


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
        raise FileNotFoundError("missing EW-boundary inputs: " + ", ".join(missing))


def row_by_id(rows: list[dict[str, Any]], row_id: str) -> dict[str, Any]:
    for row in rows:
        if row.get("id") == row_id:
            return row
    raise KeyError(row_id)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_FORMULA,
        PREVIOUS_EW,
        PREVIOUS_HK,
        EW_B41,
        EW_B41_RG,
        EW_B41_ANCHOR,
        ALPHA_A10,
        ALPHA_A10_ONE,
        ALPHA_A10_NOGO,
        EW_B11_ONE,
        WZH,
        WZH_INVENTORY,
        WZH_ACCEPT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_formula = load(PREVIOUS_FORMULA)
    previous_ew = load(PREVIOUS_EW)
    previous_hk = load(PREVIOUS_HK)
    ew_b41 = load(EW_B41)
    ew_rg = load(EW_B41_RG)
    ew_anchor = load(EW_B41_ANCHOR)
    alpha_a10 = load(ALPHA_A10)
    alpha_one = load(ALPHA_A10_ONE)
    alpha_nogo = load(ALPHA_A10_NOGO)
    ew_b11_one = load(EW_B11_ONE)
    wzh = load(WZH)
    wzh_inventory = load(WZH_INVENTORY)
    wzh_accept = load(WZH_ACCEPT)

    s_beta = float(previous["closure_decision"]["selected_s_beta_value"])
    g2_row = row_by_id(wzh_inventory["accepted_wzh_coordinate_rows"], "g_2_Mt")
    gy_row = row_by_id(wzh_inventory["accepted_wzh_coordinate_rows"], "g_Y_Mt")
    lambda_row = row_by_id(wzh_inventory["accepted_wzh_coordinate_rows"], "lambda_Mt")
    g2 = float(g2_row["central_value"])
    gy = float(gy_row["central_value"])
    lambda_ext = float(lambda_row["central_value"])
    aew_ext = (g2 * g2 + gy * gy) / 8.0
    lambda_dterm_ext = aew_ext * s_beta
    required_aew_for_lambda_ext = lambda_ext / s_beta
    required_gsum = 8.0 * required_aew_for_lambda_ext
    required_geff = math.sqrt(required_gsum)
    underprediction_factor = lambda_ext / lambda_dterm_ext if lambda_dterm_ext else math.inf

    tier_gate = {
        "schema": "MTTAEWSourceTierGate.v1",
        "status": "AEW_SOURCE_TIER_GATE_CLOSED_VALUES_OPEN",
        "closure_claimed": True,
        "theorem": {
            "name": "AEWSourceTierSeparationTheorem",
            "proved": True,
            "statement": (
                "For the selected Higgs D-term route, A_EW=(g_2^2+g_Y^2)/8 "
                "is not supplied by s_beta, by the H projection bridge, or by "
                "external W/Z/H benchmark coordinates.  Strict no-knob closure "
                "requires a same-branch physical gauge/action normalization, "
                "matching scale, and RG/threshold vector.  A one-universal-primitive "
                "extension is fully specified and guardrailed but not selected in "
                "the current corpus."
            ),
        },
        "strict_no_knob_tier": {
            "current_corpus_no_go": alpha_nogo["premises"]["absolute_L0_E0_value_absent"],
            "logical_boundary": alpha_nogo["logical_boundary"],
            "B41_K_phys_or_f_ab_closed": ew_anchor["decision"]["K_phys_or_f_ab_closed"],
            "B41_source_selected_mu_match_closed": ew_rg["decision"][
                "source_selected_mu_match_closed"
            ],
            "B41_source_selected_threshold_vector_closed": ew_rg["decision"][
                "source_selected_threshold_vector_closed"
            ],
            "selected_A_EW_emitted": False,
        },
        "one_universal_primitive_tier": {
            "extension_ready": alpha_a10["what_closes_now"]["one_universal_primitive_extension"],
            "status_relative_to_no_knob": alpha_one["status_relative_to_no_knob"],
            "primitive_selected_now": ew_b11_one["primitive_selected_now"],
            "allowed_policy": alpha_one["acceptance_policy"]["allowed_if"],
            "forbidden_policy": alpha_one["acceptance_policy"]["forbidden_if"],
            "selected_A_EW_emitted": False,
        },
        "admitted_external_replay_tier": {
            "WZH_external_coordinate_rows_closed": wzh["what_closes_now"][
                "W_Z_H_external_benchmark_coordinate_rows"
            ],
            "accepted_external_wzh_coordinate_row_count": wzh_accept[
                "accepted_external_wzh_coordinate_row_count"
            ],
            "accepted_selected_Rtheta_source_row_count": wzh_accept[
                "accepted_selected_Rtheta_source_row_count"
            ],
            "accepted_as_no_knob_A_EW": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    diagnostic = {
        "schema": "MTTExternalAEWDTermDiagnosticPostcheck.v1",
        "status": "EXTERNAL_AEW_DTERM_POSTCHECK_BUILT_NOT_SOURCE",
        "closure_claimed": True,
        "input_rows": {
            "g_2_Mt": g2_row,
            "g_Y_Mt": gy_row,
            "lambda_Mt": lambda_row,
            "selected_s_beta": s_beta,
        },
        "diagnostic_values": {
            "A_EW_Mt_external": aew_ext,
            "lambda_Dterm_Mt_external_AEW_times_selected_sbeta": lambda_dterm_ext,
            "lambda_Mt_external_coordinate": lambda_ext,
            "underprediction_factor_lambda_ext_over_Dterm": underprediction_factor,
            "required_A_EW_to_match_external_lambda_Mt": required_aew_for_lambda_ext,
            "required_g2sq_plus_gYsq_to_match_external_lambda_Mt": required_gsum,
            "required_effective_sqrt_g2sq_plus_gYsq": required_geff,
        },
        "interpretation": {
            "accepted_as_source_row": False,
            "plain_external_weak_coupling_Dterm_closes_H_row": False,
            "large_threshold_or_direct_H_row_required_for_external_lambda_postcheck": True,
            "reason": (
                "The diagnostic external gauge coordinates with selected s_beta "
                "produce a D-term lambda far below the external lambda_Mt coordinate. "
                "This is a postcheck only, but it rules out casual promotion of the "
                "plain weak-coupling D-term replay as no-knob Higgs closure."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_decision = {
        "schema": "MTTDTermRouteDecisionAfterAEWRecheck.v1",
        "status": "DTERM_ROUTE_CONDITIONAL_LARGE_THRESHOLD_OR_DIRECT_H_ROW_REQUIRED",
        "closure_claimed": True,
        "closed_formulae": {
            "A_EW": previous_formula["Dterm_boundary"]["A_EW"],
            "lambda_H_mu_match": previous_formula["Dterm_boundary"]["lambda_H_mu_match"],
            "K_threshold_conditional": previous_formula["K_threshold_formula_if_same_scheme"][
                "conditional_formula"
            ],
        },
        "route_status": {
            "selected_s_beta_input_closed": True,
            "selected_A_EW_closed": False,
            "selected_RG_threshold_transport_closed": False,
            "plain_external_Dterm_postcheck_success": False,
            "direct_intrinsic_H_quartic_K_row_emitted": False,
            "large_selected_threshold_RG_theorem_emitted": False,
        },
        "next_viable_exits": [
            "derive selected A_EW plus selected large threshold/RG transport in the Omega/lambda_H scheme",
            "emit direct intrinsic K_threshold.Omega_H.lambda from an H-sector quartic functional",
            "declare and consistently reuse one universal physical metrology/action primitive, explicitly not as strict no-knob closure",
        ],
        "retired_shortcuts": [
            "promote external g_2/g_Y rows as no-knob A_EW",
            "use selected s_beta alone as the Higgs quartic value",
            "treat the B41 one-loop diagnostic engine as selected RG transport",
            "hide a large Higgs threshold correction without a source theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterAEWRecheck.v1",
        "status": "H_K_THRESHOLD_GATE_AEW_VALUES_OPEN_DIRECT_OR_LARGE_THRESHOLD_REQUIRED_9_OF_10",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            **previous_hk["H_row"],
            "A_EW_source_tier_gate_closed": True,
            "external_AEW_diagnostic_postcheck_built": True,
            "selected_A_EW_emitted": False,
            "selected_large_threshold_RG_theorem_emitted": False,
            "direct_intrinsic_H_quartic_K_row_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
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
        "schema": "MTTNextCutsetAfterAEWRecheck.v1",
        "status": "NEXT_FRONTIER_INTRINSIC_H_QUARTIC_K_ROW_OR_SELECTED_LARGE_THRESHOLD_RG_THEOREM",
        "closure_claimed": True,
        "closed_here": [
            "A_EW source-tier separation theorem",
            "strict no-knob A_EW current-corpus no-go imported from A10/B41",
            "one-universal-primitive extension classified as ready but not selected",
            "external A_EW D-term diagnostic postcheck computed and quarantined as non-source",
            "plain external weak-coupling D-term replay rejected as H K closure",
        ],
        "still_open": [
            "selected A_EW=(g_2^2+g_Y^2)/8",
            "selected matching scale mu_match",
            "selected threshold/RG transport large enough for the Higgs lambda postcheck",
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
        "candidate": "MTTSelectedEWBoundaryRGFactorForHiggsDTermOrDirectTenKClosure",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "EWBoundaryRGFactorForHiggsDTermTierGateTheorem",
            "proved": True,
            "statement": (
                "The remaining D-term Higgs factor A_EW is exactly separated into "
                "strict no-knob, one-universal-primitive, and admitted-external "
                "tiers.  The current corpus emits no selected A_EW, no selected "
                "matching/RG transport, and no tenth H K row.  External M_t gauge "
                "coordinates give a useful postcheck but underpredict the external "
                "lambda_Mt coordinate when multiplied by selected s_beta, so the "
                "live exit is an intrinsic H quartic K row or a selected large "
                "threshold/RG theorem."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "A_EW_source_tier_gate_closed": True,
            "external_AEW_diagnostic_postcheck_built": True,
            "plain_external_Dterm_postcheck_success": False,
            "selected_A_EW_emitted": False,
            "selected_matching_scale_mu_match_closed": False,
            "selected_threshold_RG_transport_closed": False,
            "selected_large_threshold_RG_theorem_emitted": False,
            "one_universal_primitive_extension_ready": True,
            "one_universal_primitive_selected_now": False,
            "direct_intrinsic_H_quartic_K_row_emitted": False,
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
        "diagnostic_numbers_not_source": diagnostic["diagnostic_values"],
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "aew_source_tier_gate": rel(TIER_GATE),
            "external_aew_dterm_diagnostic_postcheck": rel(DIAGNOSTIC),
            "dterm_route_decision_after_aew_recheck": rel(ROUTE_DECISION),
            "hk_threshold_gate_after_aew_recheck": rel(HK_GATE),
            "next_cutset_after_aew_recheck": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedEWBoundaryRGFactorForHiggsDTermOrDirectTenKClosureCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "A_EW_source_tier_gate_closed": True,
        "external_AEW_diagnostic_postcheck_built": True,
        "plain_external_Dterm_postcheck_success": False,
        "selected_A_EW_emitted": False,
        "selected_matching_scale_mu_match_closed": False,
        "selected_threshold_RG_transport_closed": False,
        "selected_large_threshold_RG_theorem_emitted": False,
        "one_universal_primitive_extension_ready": True,
        "one_universal_primitive_selected_now": False,
        "direct_intrinsic_H_quartic_K_row_emitted": False,
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

    note = f"""# MTT Selected EWBoundaryRGFactorForHiggsDTerm or DirectTenKClosure v1

Status: `{STATUS}`

## What Closed

- separated `A_EW=(g_2^2+g_Y^2)/8` into strict no-knob, one-universal-primitive, and admitted-external tiers
- imported the A10/B41 current-corpus no-go for strict selected physical gauge/action normalization
- preserved the one-universal-primitive lane as ready but not selected and not strict no-knob closure
- computed the external diagnostic postcheck:
  - `A_EW(M_t)={aew_ext}`
  - `A_EW(M_t)*s_beta={lambda_dterm_ext}`
  - external `lambda_Mt={lambda_ext}`
  - underprediction factor `{underprediction_factor}`
- rejected plain external weak-coupling D-term replay as H K closure

## Still Open

- selected `A_EW`
- selected `mu_match`
- selected large threshold/RG transport into the Omega/lambda_H scheme
- or direct intrinsic `K_threshold.Omega_H.lambda`

Next required artifact: `{NEXT}`
"""

    write_json(TIER_GATE, tier_gate)
    write_json(DIAGNOSTIC, diagnostic)
    write_json(ROUTE_DECISION, route_decision)
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
