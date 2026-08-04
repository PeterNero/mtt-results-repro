"""Build B45/G4 primitive-portfolio comparison packet.

This packet is an anti-loop bridge between the latest weak-mixing handoff and
the constants-repo GR absolute-scale work.  B45 says alpha plus weak mixing are
down to one shared symbolic physical primitive.  CONST-GR-01 G4 then evaluates
that primitive class and freezes it as a one-universal-metrology tier, with the
physical value still open.

The live question for the local HRG/H-threshold route is whether the calibrated
dimensionless multiplier UP-RET-OVERLAP.HRG can be silently treated as that same
metrology primitive.  Current selected packets do not supply such a typed
identity theorem, and the roles differ: metrology converts internal units to
physical scale, while HRG is a dimensionless retarded-overlap/threshold
multiplier.  This builder records that separation and the resulting portfolio
budget without claiming true SM/no-knob closure.
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

SLUG = "selected_b45portfolioprimitivecomparison_or_constgr01sharedprimitivesourcetest"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
G4_IMPORT = PACKET_DIR / "frontier_import_g4_latest.packet.json"
SEPARATION = PACKET_DIR / "primitive_class_separation.packet.json"
PORTFOLIO = PACKET_DIR / "portfolio_budget_after_separation.packet.json"
HIGGS_HANDOFF = PACKET_DIR / "higgs_handoff_status.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_b45_g4_comparison.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_B45PortfolioPrimitiveComparison_or_CONSTGR01SharedPrimitiveSourceTest_v1.md"

PREVIOUS = DATA / "selected_hrguniversalprimitivesourcerule_or_qasu3retardedmatchingmap.candidate.json"
PREVIOUS_B45_IMPORT = (
    DATA
    / "selected_hrguniversalprimitivesourcerule_or_qasu3retardedmatchingmap"
    / "b45_portfolio_frontier_import.packet.json"
)
H_THRESHOLD_SOURCE = DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun.candidate.json"
H_POLICY_MATRIX = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "h_threshold_universal_primitive_admission_matrix.packet.json"
)

CONST_DATA = TEXPAPERS / "mtt-individual-constants-source-search" / "candidate_data"
CONST_B45 = CONST_DATA / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff.candidate.json"
CONST_B45_BUDGET = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
    / "universal_primitive_budget_status.packet.json"
)
CONST_B45_NEXT = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
    / "next_labeled_workorder.packet.json"
)

CONST_GR_G1 = CONST_DATA / "const_gr_01_absolute_scale_g1_shared_primitive_source_search.candidate.json"
CONST_GR_G2 = CONST_DATA / "const_gr_01_absolute_scale_g2_modal_gap_dimensional_anchor_packet_fill.candidate.json"
CONST_GR_G3 = CONST_DATA / "const_gr_01_absolute_scale_g3_cuv_qtau_omega0_source_data.candidate.json"
CONST_GR_G4 = CONST_DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive.candidate.json"
G4_DIR = CONST_DATA / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive"
G4_CONTRACT = G4_DIR / "one_metrology_primitive_contract.packet.json"
G4_DOWNSTREAM = G4_DIR / "downstream_formulae_and_falsification.packet.json"
G4_HANDOFF = G4_DIR / "portfolio_handoff.packet.json"
G4_BOUNDARY = G4_DIR / "g4_boundary.packet.json"
G4_NEXT = G4_DIR / "next_labeled_workorder.packet.json"

STATUS = (
    "MTT_SELECTED_B45PORTFOLIOPRIMITIVECOMPARISON_OR_CONSTGR01SHAREDPRIMITIVESOURCETEST_"
    "G4_IMPORTED_HRG_SEPARATED_METROLOGY_OPEN"
)
NEXT = "MTT_Selected_HiggsSharedMetrologyPrimitiveHandoff_or_HRGSourceTheoremReentry_v1"


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
        raise FileNotFoundError("missing B45/G4 portfolio inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_B45_IMPORT,
        H_THRESHOLD_SOURCE,
        H_POLICY_MATRIX,
        CONST_B45,
        CONST_B45_BUDGET,
        CONST_B45_NEXT,
        CONST_GR_G1,
        CONST_GR_G2,
        CONST_GR_G3,
        CONST_GR_G4,
        G4_CONTRACT,
        G4_DOWNSTREAM,
        G4_HANDOFF,
        G4_BOUNDARY,
        G4_NEXT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_b45 = load(PREVIOUS_B45_IMPORT)
    h_threshold = load(H_THRESHOLD_SOURCE)
    h_policy = load(H_POLICY_MATRIX)
    b45 = load(CONST_B45)
    b45_budget = load(CONST_B45_BUDGET)
    b45_next = load(CONST_B45_NEXT)
    g1 = load(CONST_GR_G1)
    g2 = load(CONST_GR_G2)
    g3 = load(CONST_GR_G3)
    g4 = load(CONST_GR_G4)
    g4_contract = load(G4_CONTRACT)
    g4_downstream = load(G4_DOWNSTREAM)
    g4_handoff = load(G4_HANDOFF)
    g4_boundary = load(G4_BOUNDARY)
    g4_next = load(G4_NEXT)

    previous_numbers = previous["key_numbers"]
    hrg_value = previous_numbers["UP_RET_OVERLAP_HRG"]
    log_hrg = previous_numbers["log_UP_RET_OVERLAP_HRG"]
    weak_sin2 = previous_numbers["B44_conditional_minimal_threshold_sin2"]
    b45_global_budget = b45_budget["global_budget"]
    g4_shared_formulae = g4_downstream["shared_formulae"]
    g4_parameter_budget = g4_contract["parameter_budget"]
    h_decision = h_threshold["closure_decision"]
    h_policy_decision = h_policy["decision"]
    h_policy_classes = h_policy["candidate_class_mapping"]

    g4_import = {
        "schema": "MTTSelectedB45PortfolioPrimitiveComparisonG4Import.v1",
        "status": "G4_LATEST_CONST_GR_01_FRONTIER_IMPORTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "b45_import": {
            "status": b45["status"],
            "local_previous_status": previous["status"],
            "weak_mixing_down_to_one_shared_primitive_tier": b45[
                "weak_mixing_down_to_one_shared_primitive_tier"
            ],
            "selected_next_constant": b45["selected_next_constant"],
            "selected_numeric_primitive_values_now": b45_global_budget[
                "selected_numeric_primitive_values_now"
            ],
            "conditional_profile_replay_sin2": weak_sin2,
            "local_previous_b45_decision": previous_b45["decision"],
            "next_workorder": b45_next,
        },
        "const_gr_01_chain": {
            "G1": g1["status"],
            "G2": g2["status"],
            "G3": g3["status"],
            "G4": g4["status"],
        },
        "g4_result": {
            "theorem": g4["theorem"],
            "relative_physical_scale_solution_closed": g4["relative_physical_scale_solution_closed"],
            "one_universal_metrology_primitive_tier_defined": g4[
                "one_universal_metrology_primitive_tier_defined"
            ],
            "selected_next_constant": g4["selected_next_constant"],
            "boundary_status": g4_boundary["status"],
            "closed_or_decided_now": g4_boundary["closed_or_decided_now"],
            "still_open": g4_boundary["still_open"],
            "parameter_budget": g4_parameter_budget,
            "shared_formulae": g4_shared_formulae,
            "physical_predictions_now": g4_downstream["physical_predictions_now"],
            "next_workorder": g4_next,
        },
        "decision": {
            "B45_latest_weak_mixing_frontier_imported": True,
            "CONST_GR_01_G4_latest_imported": True,
            "G4_relative_physical_scale_solution_closed": True,
            "G4_one_metrology_primitive_tier_defined": True,
            "G4_strict_same_branch_Omega0_E0_L0_derived": False,
            "G4_selected_metrology_primitive_value": False,
            "G4_Newton_or_Planck_prediction": False,
            "G4_recommends_Higgs_shared_metrology_next": True,
        },
    }

    separation_tests = [
        {
            "test": "typed_role",
            "UP_ABS_SCALE": "dimensionful metrology conversion between internal MTT units and physical units",
            "UP_RET_OVERLAP_HRG": "dimensionless retarded-overlap / H-threshold RG multiplier",
            "accepted_identity_now": False,
            "reason": "The current selected corpus has no typed map equating a physical unit anchor with a threshold multiplier.",
        },
        {
            "test": "source_provenance",
            "UP_ABS_SCALE": "G4 allows one preselected metrology primitive but forbids choosing it from alpha, weak angle, G_N, Planck, masses, cosmology, TeV, or the target.",
            "UP_RET_OVERLAP_HRG": "current value is the controlled empirical lambda_H calibration layer.",
            "accepted_identity_now": False,
            "reason": "Using the HRG calibration value as the metrology value would select a primitive from the H target.",
        },
        {
            "test": "crossuse_evidence",
            "UP_ABS_SCALE": "formula/relative tier shared across alpha, weak mixing, and GR, physical value open",
            "UP_RET_OVERLAP_HRG": "non-Higgs cross-use audit currently accepts zero same-HRG maps and zero predictions",
            "accepted_identity_now": False,
            "reason": "Current HRG cross-use does not establish the same source value across independent non-Higgs sectors.",
        },
        {
            "test": "prediction_credit",
            "UP_ABS_SCALE": "downstream predictions must state dependence on the metrology primitive until derived",
            "UP_RET_OVERLAP_HRG": "lambda_H is calibration, not prediction, if HRG is fit from lambda_H",
            "accepted_identity_now": False,
            "reason": "Hiding HRG inside UP-ABS-SCALE would make a calibrated H target look like a prediction.",
        },
    ]

    separation = {
        "schema": "MTTSelectedPrimitiveClassSeparationB45G4HRG.v1",
        "status": "PRIMITIVE_CLASS_SEPARATION_ESTABLISHED_FOR_CURRENT_LEDGER",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "primitive_classes": {
            "UP_ABS_SCALE": {
                "id": "UP-ABS-SCALE",
                "class": "universal metrology primitive",
                "typed_domain": "dimensionful physical unit / absolute-scale conversion",
                "symbols": ["E0", "L0", "Omega0", "T0"],
                "source_packet": rel(G4_CONTRACT),
                "contract_status": g4_contract["status"],
                "selected_value_now": False,
                "strict_no_knob_now": False,
                "relative_solution_closed": True,
                "shared_formulae": {
                    "alpha_from_E0": g4_shared_formulae["alpha_from_E0"],
                    "alpha_from_L0": g4_shared_formulae["alpha_from_L0"],
                    "GR_G_eff_from_E0": g4_shared_formulae["GR_G_eff_from_E0"],
                    "GR_G_eff_from_L0": g4_shared_formulae["GR_G_eff_from_L0"],
                    "Omega0_from_E0_selected_convention": g4_shared_formulae[
                        "Omega0_from_E0_selected_convention"
                    ],
                    "Omega0_from_L0_selected_convention": g4_shared_formulae[
                        "Omega0_from_L0_selected_convention"
                    ],
                },
            },
            "UP_RET_OVERLAP_HRG": {
                "id": "UP-RET-OVERLAP.HRG",
                "class": "retarded-overlap threshold multiplier candidate",
                "typed_domain": "dimensionless H-threshold / RG transport multiplier",
                "value_if_empirically_calibrated": hrg_value,
                "log_value_if_empirically_calibrated": log_hrg,
                "source_packet": rel(H_THRESHOLD_SOURCE),
                "strict_source_selected_now": h_decision["UP_RET_OVERLAP_HRG_selected_strict_source"],
                "universal_admitted_now": previous["closure_decision"]["UP_RET_OVERLAP_HRG_universal_admitted"],
                "empirical_layer_admitted_now": h_decision["UP_RET_OVERLAP_HRG_admitted_empirical_layer"],
                "lambda_H_calibrated": h_decision["lambda_H_calibrated"],
                "lambda_H_predicted": h_decision["lambda_H_predicted"],
            },
        },
        "separation_tests": separation_tests,
        "identity_route_status": {
            "typed_identity_theorem_found_now": False,
            "HRG_equals_E0_or_L0_or_Omega0_now": False,
            "HRG_promoted_by_B45_now": False,
            "HRG_promoted_by_G4_now": False,
            "deeper_identity_theorem_excluded": False,
            "required_to_supersede_this_packet": (
                "a selected typed source map deriving UP-RET-OVERLAP.HRG from "
                "the metrology primitive without using lambda_H or any target "
                "residual as selector"
            ),
        },
        "decision": {
            "HRG_and_metrology_primitives_typed_separate_now": True,
            "current_ledger_must_not_merge_HRG_with_UP_ABS_SCALE": True,
            "UP_ABS_SCALE_value_remains_open": True,
            "UP_RET_OVERLAP_HRG_strict_source_remains_open": True,
            "UP_RET_OVERLAP_HRG_universal_admission_remains_open": True,
        },
    }

    portfolio = {
        "schema": "MTTSelectedPortfolioBudgetAfterB45G4Separation.v1",
        "status": "PORTFOLIO_AFTER_SEPARATION_TWO_OPEN_PRIMITIVE_CLASSES_IF_HRG_RETAINED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "b45_budget": b45_global_budget,
        "g4_parameter_budget": g4_parameter_budget,
        "h_threshold_policy_decision": h_policy_decision,
        "current_minimal_portfolio_if_HRG_retained": {
            "candidate_primitive_class_count": 2,
            "strict_no_knob_primitive_count": 0,
            "selected_numeric_primitive_value_count": 0,
            "ordinary_fitted_sector_knobs": 0,
            "conditional_empirical_calibrations_now": 1,
            "classes": [
                {
                    "id": "UP-ABS-SCALE",
                    "role": "one universal metrology primitive for physical unit scale",
                    "status": "contract defined by G4; selected physical value open",
                    "can_count_as_no_knob_now": False,
                },
                {
                    "id": "UP-RET-OVERLAP.HRG",
                    "role": "H-threshold retarded-overlap/RG multiplier",
                    "status": "controlled empirical layer available; strict source and universal admission open",
                    "can_count_as_no_knob_now": False,
                },
            ],
        },
        "policy_guardrails": {
            "ordinary_H_only_knob_allowed": h_policy_decision["ordinary_H_only_knob_allowed"],
            "credible_minimal_parameter_path_exists": h_policy_decision[
                "credible_minimal_parameter_path_exists"
            ],
            "selected_existing_physical_unit_primitive_now": h_policy_decision[
                "selected_existing_physical_unit_primitive_now"
            ],
            "selected_H_threshold_primitive_now": h_policy_decision[
                "selected_H_threshold_primitive_now"
            ],
            "calibrating_H_lambda_makes_H_lambda_a_prediction": h_policy_decision[
                "calibrating_H_lambda_makes_H_lambda_a_prediction"
            ],
        },
        "candidate_class_import": {
            "UP_ABS_SCALE": h_policy_classes["UP_ABS_SCALE"],
            "UP_RET_OVERLAP_for_H_threshold": h_policy_classes["UP_RET_OVERLAP_for_H_threshold"],
        },
        "decision": {
            "minimal_one_primitive_solves_everything_now": False,
            "minimal_two_class_portfolio_is_current_legal_if_HRG_retained": True,
            "one_metrology_primitive_cross_constant_test_ready": True,
            "HRG_requires_source_theorem_or_admission_before_prediction_credit": True,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
    }

    higgs_handoff = {
        "schema": "MTTSelectedHiggsHandoffStatusAfterB45G4Separation.v1",
        "status": "HIGGS_HANDOFF_REFINED_TO_SHARED_METROLOGY_OR_HRG_SOURCE_REENTRY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "g4_selected_next": g4_handoff["selected_next"],
        "g4_primary_workorder": g4_next["primary"],
        "local_h_threshold_status": h_threshold["status"],
        "local_h_threshold_decision": {
            "strict_K_rows": h_decision["strict_accepted_selected_K_source_row_count"],
            "required_K_rows": h_decision["strict_selected_K_threshold_row_count_required"],
            "controlled_empirical_conditional_K_rows": h_decision[
                "controlled_empirical_conditional_K_row_count"
            ],
            "UP_RET_OVERLAP_HRG_admitted_empirical_layer": h_decision[
                "UP_RET_OVERLAP_HRG_admitted_empirical_layer"
            ],
            "UP_RET_OVERLAP_HRG_selected_strict_source": h_decision[
                "UP_RET_OVERLAP_HRG_selected_strict_source"
            ],
            "crossuse_prediction_audit_passed": h_decision["crossuse_prediction_audit_passed"],
        },
        "refined_next_routes": [
            {
                "route": "shared_metrology_handoff",
                "target": "use the G4 UP-ABS-SCALE contract only for physical-unit/action-normalization dependencies such as A_EW or mu_match",
                "allowed_now": True,
                "closes_HRG": False,
            },
            {
                "route": "HRG_source_theorem_reentry",
                "target": "derive UP-RET-OVERLAP.HRG as selected retarded-overlap/threshold source data or admit it as a declared universal parameter before replay",
                "allowed_now": True,
                "closes_HRG": False,
            },
            {
                "route": "silent_identity_with_metrology",
                "target": "treat UP-RET-OVERLAP.HRG as already paid for by E0/L0/Omega0",
                "allowed_now": False,
                "closes_HRG": False,
            },
        ],
    }

    cutset = {
        "schema": "MTTNextCutsetAfterB45G4PrimitiveComparison.v1",
        "status": "NEXT_FRONTIER_HIGGS_SHARED_METROLOGY_OR_HRG_SOURCE_REENTRY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "B45 latest weak-mixing one-shared-primitive handoff imported",
            "CONST-GR-01 G1-G4 chain imported as the latest absolute-scale shared primitive test",
            "G4 one-universal-metrology primitive tier classified as defined but value-open",
            "G4 relative physical scale solution classified as closed",
            "UP-ABS-SCALE and UP-RET-OVERLAP.HRG separated for the current typed ledger",
            "current portfolio budget after separation computed",
            "silent HRG-as-metrology merge rejected until a selected typed identity theorem exists",
        ],
        "still_open": [
            "selected physical E0/L0/Omega0 value or strict same-branch physical unit theorem",
            "Newton/Planck prediction from the metrology primitive",
            "strict source theorem for UP-RET-OVERLAP.HRG",
            "universal admission and non-Higgs cross-use prediction for UP-RET-OVERLAP.HRG",
            "Higgs shared metrology handoff against A_EW/mu_match without target selection",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedB45PortfolioPrimitiveComparisonOrCONSTGR01SharedPrimitiveSourceTest",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorem": {
            "name": "B45PortfolioPrimitiveComparisonOrCONSTGR01SharedPrimitiveSourceTestTheorem",
            "proved": True,
            "statement": (
                "The latest B45 weak-mixing handoff and CONST-GR-01 G4 absolute-scale "
                "packet select a metrology-primitive tier, not a value for that tier. "
                "The current HRG value is a dimensionless threshold/retarded-overlap "
                "calibration candidate.  Because no selected typed identity theorem "
                "maps HRG to E0/L0/Omega0, the two primitive classes must remain "
                "separate in the current ledger.  If HRG is retained, the legal "
                "portfolio is therefore a value-open metrology primitive plus a "
                "separate HRG source/admission obligation, with no true SM/no-knob "
                "closure claimed."
            ),
        },
        "closure_decision": {
            "B45_latest_weak_mixing_frontier_imported": True,
            "CONST_GR_01_G4_latest_imported": True,
            "G4_relative_physical_scale_solution_closed": True,
            "G4_one_metrology_primitive_tier_defined": True,
            "G4_strict_same_branch_Omega0_E0_L0_derived": False,
            "G4_selected_metrology_primitive_value": False,
            "G4_Newton_or_Planck_prediction": False,
            "HRG_and_metrology_primitives_typed_separate_now": True,
            "HRG_equals_E0_L0_or_Omega0_now": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "minimal_portfolio_requires_two_distinct_open_primitives_if_HRG_retained": True,
            "silent_HRG_as_metrology_merge_allowed": False,
            "deeper_identity_theorem_excluded": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg_value,
            "log_UP_RET_OVERLAP_HRG": log_hrg,
            "B44_conditional_minimal_threshold_sin2": weak_sin2,
            "B45_selected_numeric_primitive_values_now": b45_global_budget[
                "selected_numeric_primitive_values_now"
            ],
            "tau_int": g4_shared_formulae["tau_int"],
            "Omega0_over_sqrt_alpha_phys": g4_shared_formulae["Omega0_over_sqrt_alpha_phys"],
            "GR_G_eff_L0_coeff": 0.29759362932431804,
            "selected_numeric_metrology_values_now": 0,
            "selected_HRG_source_value_now": 0,
            "strict_H_K_rows": h_decision["strict_accepted_selected_K_source_row_count"],
            "required_H_K_rows": h_decision["strict_selected_K_threshold_row_count_required"],
        },
        "packets": {
            "frontier_import_g4_latest": rel(G4_IMPORT),
            "primitive_class_separation": rel(SEPARATION),
            "portfolio_budget_after_separation": rel(PORTFOLIO),
            "higgs_handoff_status": rel(HIGGS_HANDOFF),
            "cutset": rel(CUTSET),
        },
        "what_closes": {
            "B45_G4_latest_frontier_import": True,
            "metrology_vs_HRG_class_separation": True,
            "portfolio_budget_after_separation": True,
            "silent_identity_route_rejected": True,
            "non_looping_next_target_selected": True,
        },
        "what_remains_open": {
            "selected_metrology_value": True,
            "strict_same_branch_physical_unit_theorem": True,
            "Newton_or_Planck_prediction": True,
            "strict_HRG_source_theorem": True,
            "HRG_universal_admission_and_crossuse_prediction": True,
            "Higgs_shared_metrology_handoff": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedB45PortfolioPrimitiveComparisonOrCONSTGR01SharedPrimitiveSourceTest",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "B45_latest_weak_mixing_frontier_imported": True,
        "CONST_GR_01_G4_latest_imported": True,
        "G4_relative_physical_scale_solution_closed": True,
        "G4_one_metrology_primitive_tier_defined": True,
        "G4_strict_same_branch_Omega0_E0_L0_derived": False,
        "G4_selected_metrology_primitive_value": False,
        "G4_Newton_or_Planck_prediction": False,
        "HRG_and_metrology_primitives_typed_separate_now": True,
        "HRG_equals_E0_L0_or_Omega0_now": False,
        "UP_RET_OVERLAP_HRG_universal_admitted": False,
        "minimal_portfolio_requires_two_distinct_open_primitives_if_HRG_retained": True,
        "silent_HRG_as_metrology_merge_allowed": False,
        "deeper_identity_theorem_excluded": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected B45 Portfolio Primitive Comparison or CONST-GR-01 Shared Primitive Source Test v1

Status: `{STATUS}`

## Result

This packet imports the actual next result after B45: CONST-GR-01 has already
advanced through G4.

```text
B45 = {b45["status"]}
G4  = {g4["status"]}
```

G4 closes the relative physical-scale solution and defines a
one-universal-metrology-primitive tier, but it does **not** select the physical
value:

```text
relative physical scale closed = {g4["relative_physical_scale_solution_closed"]}
one metrology primitive tier   = {g4["one_universal_metrology_primitive_tier_defined"]}
selected metrology values now  = 0
Newton/Planck prediction now   = false
```

The key G4 formulae now imported are:

```text
tau_int = {g4_shared_formulae["tau_int"]}
Omega0/sqrt(alpha_phys) = {g4_shared_formulae["Omega0_over_sqrt_alpha_phys"]}
G_eff(L0) = {g4_shared_formulae["GR_G_eff_from_L0"]}
G_eff(E0) = {g4_shared_formulae["GR_G_eff_from_E0"]}
```

## Separation

`UP-ABS-SCALE` and `UP-RET-OVERLAP.HRG` are not the same object in the current
typed ledger.

```text
UP-ABS-SCALE       = dimensionful metrology conversion: E0/L0/Omega0/T0
UP-RET-OVERLAP.HRG = dimensionless threshold/RG multiplier
HRG value           = {hrg_value}
log(HRG)            = {log_hrg}
```

No selected typed identity theorem currently maps the HRG value to
`E0/L0/Omega0`.  A deeper identity theorem is not ruled out, but until it is
supplied the ledger must not count HRG as already paid for by the metrology
primitive.

## Portfolio After This Cut

If HRG is retained, the current legal portfolio is:

```text
1. UP-ABS-SCALE: G4 metrology primitive tier, value open.
2. UP-RET-OVERLAP.HRG: H-threshold retarded-overlap candidate, strict source open.
```

That is not an ordinary fitted H knob: the controlled empirical HRG layer is
recorded, but it gives no no-knob or prediction credit for `lambda_H`.  It also
does not close true SM equivalence.

## What Actually Moved

- B45/G4 is no longer an unexamined pointer; it is imported into this repo.
- The silent one-primitive-does-everything route is rejected for the current
  formal ledger.
- The next non-looping target is sharpened to either a Higgs shared-metrology
  handoff or a strict HRG source/admission theorem.

## Next

`{NEXT}`
"""

    write_json(G4_IMPORT, g4_import)
    write_json(SEPARATION, separation)
    write_json(PORTFOLIO, portfolio)
    write_json(HIGGS_HANDOFF, higgs_handoff)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
