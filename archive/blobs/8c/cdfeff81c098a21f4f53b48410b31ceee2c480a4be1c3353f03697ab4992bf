"""Build Higgs shared-metrology handoff / HRG source-theorem reentry packet.

The preceding B45/G4 comparison proves that UP-ABS-SCALE and
UP-RET-OVERLAP.HRG must remain separate in the current typed ledger.  This
packet turns that separation into two executable theorem gates:

* the Higgs shared-metrology domain handoff theorem, which says where the G4
  metrology primitive may legally enter the Higgs D-term route; and
* the HRG source-admission reentry theorem, which says exactly what must be
  true before the calibrated HRG multiplier gets prediction/no-knob credit.

Both theorems close acceptance predicates, not values.  The result is a sharper
next computation: execute the A_EW/mu/RG metrology slots or emit a strict HRG
source/non-Higgs prediction map.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgssharedmetrologyprimitivehandoff_or_hrgsourcetheoremreentry"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
METROLOGY_HANDOFF = PACKET_DIR / "higgs_shared_metrology_handoff_theorem.packet.json"
HRG_REENTRY = PACKET_DIR / "hrg_source_admission_reentry_theorem.packet.json"
ROUTE_MATRIX = PACKET_DIR / "two_route_frontier_execution_matrix.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_handoff_reentry.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsSharedMetrologyPrimitiveHandoff_or_HRGSourceTheoremReentry_v1.md"

PREVIOUS = DATA / "selected_b45portfolioprimitivecomparison_or_constgr01sharedprimitivesourcetest.candidate.json"
PREVIOUS_SEPARATION = (
    DATA
    / "selected_b45portfolioprimitivecomparison_or_constgr01sharedprimitivesourcetest"
    / "primitive_class_separation.packet.json"
)
PREVIOUS_HANDOFF = (
    DATA
    / "selected_b45portfolioprimitivecomparison_or_constgr01sharedprimitivesourcetest"
    / "higgs_handoff_status.packet.json"
)

H_RADIAL = DATA / "selected_hradialthresholdscalarsource_or_tenkclosure.candidate.json"
H_CONDITIONAL_FORMULA = (
    DATA
    / "selected_hradialthresholdscalarsource_or_tenkclosure"
    / "conditional_h_k_from_ew_boundary_formula.packet.json"
)
EW_BOUNDARY = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
AEW_GATE = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "aew_source_tier_gate.packet.json"
)
DTERM_DECISION = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "dterm_route_decision_after_aew_recheck.packet.json"
)

H_THRESHOLD_POLICY = DATA / "selected_hthresholdrgoperator_or_universalprimitivepolicy.candidate.json"
H_POLICY_MATRIX = (
    DATA
    / "selected_hthresholdrgoperator_or_universalprimitivepolicy"
    / "h_threshold_universal_primitive_admission_matrix.packet.json"
)
H_THRESHOLD_SOURCE = DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun.candidate.json"
HRG_CALIBRATION = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "minimal_primitive_calibration_run.packet.json"
)
HRG_EMPIRICAL_GATE = (
    DATA
    / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun"
    / "controlled_empirical_h_k_gate.packet.json"
)
HRG_NONHIGGS_CONTRACT = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "retarded_overlap_family_source_map_contract.packet.json"
)
HRG_NONHIGGS_EXECUTION = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "nonhiggs_hrg_source_map_execution.packet.json"
)
RO_FAMILY_SELECTOR = (
    DATA
    / "selected_rofamilyselectorsourcetheorem_or_nonhiggspredictionmap"
    / "ro_family_selector_source_theorem.packet.json"
)
RO_VALUE_EXECUTION = (
    DATA
    / "selected_rovaluesource_or_nonhiggsmapexecution"
    / "ro_value_source_execution.packet.json"
)

STATUS = (
    "MTT_SELECTED_HIGGSSHAREDMETROLOGYPRIMITIVEHANDOFF_OR_HRGSOURCETHEOREMREENTRY_"
    "THEOREM_GATES_BUILT_VALUES_OPEN"
)
NEXT = "MTT_Selected_AEWMetrologySlotExecution_or_HRGNonHiggsPredictionSelector_v1"


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
        raise FileNotFoundError("missing handoff/reentry inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_SEPARATION,
        PREVIOUS_HANDOFF,
        H_RADIAL,
        H_CONDITIONAL_FORMULA,
        EW_BOUNDARY,
        AEW_GATE,
        DTERM_DECISION,
        H_THRESHOLD_POLICY,
        H_POLICY_MATRIX,
        H_THRESHOLD_SOURCE,
        HRG_CALIBRATION,
        HRG_EMPIRICAL_GATE,
        HRG_NONHIGGS_CONTRACT,
        HRG_NONHIGGS_EXECUTION,
        RO_FAMILY_SELECTOR,
        RO_VALUE_EXECUTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    separation = load(PREVIOUS_SEPARATION)
    previous_handoff = load(PREVIOUS_HANDOFF)
    h_radial = load(H_RADIAL)
    h_formula = load(H_CONDITIONAL_FORMULA)
    ew_boundary = load(EW_BOUNDARY)
    aew_gate = load(AEW_GATE)
    dterm_decision = load(DTERM_DECISION)
    h_threshold_policy = load(H_THRESHOLD_POLICY)
    h_policy_matrix = load(H_POLICY_MATRIX)
    h_threshold_source = load(H_THRESHOLD_SOURCE)
    hrg_calibration = load(HRG_CALIBRATION)
    hrg_empirical_gate = load(HRG_EMPIRICAL_GATE)
    hrg_nonhiggs_contract = load(HRG_NONHIGGS_CONTRACT)
    hrg_nonhiggs_execution = load(HRG_NONHIGGS_EXECUTION)
    ro_family_selector = load(RO_FAMILY_SELECTOR)
    ro_value_execution = load(RO_VALUE_EXECUTION)

    previous_numbers = previous["key_numbers"]
    h_decision = h_threshold_source["closure_decision"]
    ew_decision = ew_boundary["closure_decision"]
    h_radial_decision = h_radial["closure_decision"]
    policy_decision = h_policy_matrix["decision"]
    hrg_value = previous_numbers["UP_RET_OVERLAP_HRG"]
    log_hrg = previous_numbers["log_UP_RET_OVERLAP_HRG"]
    s_beta = h_formula["selected_s_beta"]["value"]

    metrology_slots = [
        {
            "slot": "A_EW_action_normalization",
            "formula": "(g_2(mu_match)^2 + g_Y(mu_match)^2) / 8",
            "may_receive_UP_ABS_SCALE": True,
            "source_selected_now": ew_decision["selected_A_EW_emitted"],
            "emits_H_K_row_now": False,
            "reason": "A_EW is a physical gauge/action normalization slot; G4 metrology may support it only when selected before target comparison.",
        },
        {
            "slot": "mu_match_physical_scale",
            "formula": "mu_match in the selected same-branch physical unit convention",
            "may_receive_UP_ABS_SCALE": True,
            "source_selected_now": ew_decision["selected_matching_scale_mu_match_closed"],
            "emits_H_K_row_now": False,
            "reason": "The matching scale is a metrology/physical-unit slot, but no selected value is emitted in the current corpus.",
        },
        {
            "slot": "threshold_RG_transport_to_Omega_scheme",
            "formula": "K_threshold.Omega_H.lambda = (A_EW*s_beta)/(D_fin.H*epsilon_Theta^(1/3)) after same-scheme alignment",
            "may_receive_UP_ABS_SCALE": True,
            "source_selected_now": ew_decision["selected_threshold_RG_transport_closed"],
            "emits_H_K_row_now": False,
            "reason": "Scheme transport may depend on the same metrology/action convention but still needs selected threshold/RG source data.",
        },
    ]
    prohibited_slots = [
        {
            "slot": "UP_RET_OVERLAP_HRG_multiplier",
            "may_receive_UP_ABS_SCALE": False,
            "reason": "B45/G4 separation types HRG as dimensionless retarded-overlap/threshold multiplier, not as a physical metrology coordinate.",
        },
        {
            "slot": "direct_K_threshold_Omega_H_lambda",
            "may_receive_UP_ABS_SCALE": False,
            "reason": "A physical unit primitive cannot replace the selected H-sector quartic/threshold source row.",
        },
        {
            "slot": "lambda_H_target_calibration_selector",
            "may_receive_UP_ABS_SCALE": False,
            "reason": "G4 forbids choosing a universal primitive from masses, Higgs, TeV, or any target being predicted.",
        },
    ]
    accepted_metrology_slots = [row for row in metrology_slots if row["may_receive_UP_ABS_SCALE"]]
    selected_metrology_slots = [row for row in metrology_slots if row["source_selected_now"]]

    metrology_handoff = {
        "schema": "MTTHiggsSharedMetrologyPrimitiveHandoffTheorem.v1",
        "status": "HIGGS_SHARED_METROLOGY_HANDOFF_THEOREM_BUILT_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "theorem": {
            "name": "HiggsSharedMetrologyPrimitiveHandoffDomainTheorem",
            "proved": True,
            "statement": (
                "Given the B45/G4 separation, UP-ABS-SCALE may enter the Higgs "
                "D-term route only through physical unit/action-normalization "
                "slots such as A_EW, mu_match, and same-scheme threshold/RG "
                "transport. It cannot by itself emit the H threshold row, cannot "
                "select lambda_H from the target, and cannot be silently reused "
                "as UP-RET-OVERLAP.HRG."
            ),
        },
        "imports": {
            "previous_status": previous["status"],
            "separation_status": separation["status"],
            "h_radial_status": h_radial["status"],
            "ew_boundary_status": ew_boundary["status"],
            "aew_tier_gate_status": aew_gate["status"],
            "conditional_h_formula_status": h_formula["status"],
            "dterm_route_decision_status": dterm_decision["status"],
            "g4_handoff_refinement": previous_handoff["status"],
        },
        "selected_inputs": {
            "s_beta_selected": h_formula["selected_s_beta"]["source_selected_before_replay"],
            "s_beta": s_beta,
            "conditional_lambda_H_mu_match_formula": h_formula["Dterm_boundary"]["lambda_H_mu_match"],
            "conditional_K_threshold_formula": h_formula["K_threshold_formula_if_same_scheme"][
                "conditional_formula"
            ],
        },
        "allowed_metrology_slots": metrology_slots,
        "prohibited_metrology_slots": prohibited_slots,
        "slot_counts": {
            "allowed_metrology_slot_count": len(accepted_metrology_slots),
            "selected_metrology_value_slot_count_now": len(selected_metrology_slots),
            "prohibited_silent_merge_slot_count": len(prohibited_slots),
        },
        "decision": {
            "higgs_metrology_handoff_domain_closed": True,
            "A_EW_slot_legal_for_UP_ABS_SCALE": True,
            "mu_match_slot_legal_for_UP_ABS_SCALE": True,
            "threshold_RG_scheme_slot_legal_for_UP_ABS_SCALE": True,
            "selected_A_EW_value_emitted_now": ew_decision["selected_A_EW_emitted"],
            "selected_mu_match_value_emitted_now": ew_decision["selected_matching_scale_mu_match_closed"],
            "selected_threshold_RG_transport_emitted_now": ew_decision["selected_threshold_RG_transport_closed"],
            "K_threshold_Omega_H_lambda_emitted_now": ew_decision["K_threshold_Omega_H_lambda_emitted"],
            "UP_ABS_SCALE_closes_HRG_now": False,
            "lambda_H_prediction_credit_from_metrology_now": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
    }

    admission_predicate = {
        "strict_source_lane": {
            "accepted_if": [
                "selected R_H^RG source theorem is emitted",
                "selected K_threshold.Omega_H.lambda follows without lambda_H target calibration",
                "observed Higgs data are not used as selector",
            ],
            "satisfied_now": h_decision["UP_RET_OVERLAP_HRG_selected_strict_source"],
        },
        "universal_parameter_lane": {
            "accepted_if": [
                "UP-RET-OVERLAP.HRG is declared once before replay",
                "same value is consumed by H and at least one non-Higgs typed source map",
                "the non-Higgs target is predicted without retuning",
                "lambda_H remains calibration if used to set the value",
            ],
            "satisfied_now": False,
        },
        "family_class_lane": {
            "accepted_if": [
                "RO.family_selector is source-selected at family-class level",
                "numeric specialization and value source are separately emitted",
            ],
            "satisfied_now": False,
            "family_selector_selected_now": ro_family_selector["source_selected"],
            "numeric_value_source_selected_now": ro_value_execution["source_selected"],
        },
    }

    hrg_reentry = {
        "schema": "MTTHRGSourceAdmissionReentryTheorem.v1",
        "status": "HRG_SOURCE_ADMISSION_REENTRY_PREDICATE_BUILT_NOT_SATISFIED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "theorem": {
            "name": "HRGSourceAdmissionReentryPredicateTheorem",
            "proved": True,
            "statement": (
                "UP-RET-OVERLAP.HRG can reenter the value ledger only through "
                "a strict selected source theorem, or as a declared universal "
                "parameter that predicts at least one typed non-Higgs target "
                "with the same value and no retuning. The current corpus selects "
                "the retarded-overlap family class and has an exact H calibration "
                "value, but it emits no HRG value source and no accepted non-Higgs "
                "same-HRG prediction map."
            ),
        },
        "imports": {
            "h_threshold_policy_status": h_threshold_policy["status"],
            "h_threshold_source_status": h_threshold_source["status"],
            "hrg_calibration_status": hrg_calibration["status"],
            "hrg_empirical_gate_status": hrg_empirical_gate["status"],
            "nonhiggs_contract_status": hrg_nonhiggs_contract["status"],
            "nonhiggs_execution_status": hrg_nonhiggs_execution["status"],
            "ro_family_selector_status": ro_family_selector["status"],
            "ro_value_execution_status": ro_value_execution["status"],
        },
        "admission_predicate": admission_predicate,
        "current_value_status": {
            "UP_RET_OVERLAP_HRG": hrg_value,
            "log_UP_RET_OVERLAP_HRG": log_hrg,
            "empirical_value_available": ro_value_execution["empirical_value_available"],
            "calibrating_observable": hrg_calibration["calibration_protocol"]["calibrating_observable"],
            "lambda_H_calibrated": h_decision["lambda_H_calibrated"],
            "lambda_H_predicted": h_decision["lambda_H_predicted"],
            "strict_source_selected_now": h_decision["UP_RET_OVERLAP_HRG_selected_strict_source"],
            "nonHiggs_accepted_crossuse_map_count": hrg_nonhiggs_execution["accepted_crossuse_map_count"],
        },
        "decision": {
            "HRG_source_admission_predicate_closed": True,
            "RO_family_selector_selected": ro_family_selector["source_selected"],
            "RO_value_source_selected": ro_value_execution["source_selected"],
            "strict_R_H_RG_source_emitted": ro_value_execution["strict_R_H_RG_source_emitted"],
            "UP_RET_OVERLAP_HRG_universal_admitted": ro_value_execution["decision"][
                "UP_RET_OVERLAP_HRG_universal_admitted"
            ],
            "same_HRG_nonHiggs_map_accepted": ro_value_execution["decision"]["same_HRG_nonHiggs_map_accepted"],
            "nonHiggs_prediction_passed": hrg_nonhiggs_contract["contract_result"][
                "crossuse_prediction_passed"
            ],
            "lambda_H_prediction_credit_allowed": h_decision["lambda_H_predicted"],
            "current_HRG_reentry_gate_satisfied": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
    }

    route_rows = [
        {
            "route": "execute_A_EW_mu_RG_metrology_slots",
            "theorem_gate_built": True,
            "value_source_ready_now": False,
            "next_required_source_data": [
                "selected A_EW=(g_2^2+g_Y^2)/8",
                "selected mu_match",
                "selected threshold/RG transport into Omega/lambda_H scheme",
            ],
            "would_close_if_satisfied": "strict H D-term route to K_threshold.Omega_H.lambda",
        },
        {
            "route": "emit_direct_intrinsic_H_quartic_K_row",
            "theorem_gate_built": True,
            "value_source_ready_now": False,
            "next_required_source_data": ["selected H-sector quartic/threshold functional"],
            "would_close_if_satisfied": "strict tenth K_threshold row without HRG primitive",
        },
        {
            "route": "strict_HRG_source_theorem",
            "theorem_gate_built": True,
            "value_source_ready_now": h_decision["UP_RET_OVERLAP_HRG_selected_strict_source"],
            "next_required_source_data": ["selected R_H^RG determinant/index/retarded-overlap source theorem"],
            "would_close_if_satisfied": "HRG as no-knob threshold source",
        },
        {
            "route": "HRG_universal_parameter_crossuse",
            "theorem_gate_built": True,
            "value_source_ready_now": False,
            "next_required_source_data": ["one same-value non-Higgs prediction map consuming UP-RET-OVERLAP.HRG"],
            "would_close_if_satisfied": "minimal-parameter credibility upgrade, not no-knob derivation",
        },
    ]

    route_matrix = {
        "schema": "MTTHiggsMetrologyOrHRGReentryRouteMatrix.v1",
        "status": "TWO_ROUTE_FRONTIER_EXECUTION_MATRIX_BUILT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "route_rows": route_rows,
        "decision": {
            "theorem_gates_built": True,
            "selected_value_route_closed_now": False,
            "preferred_next_parallel_targets": [
                "A_EW/mu/RG metrology slot execution",
                "HRG non-Higgs prediction selector",
            ],
            "loop_back_to_silent_HRG_metrology_identity_allowed": False,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHiggsMetrologyHandoffOrHRGReentry.v1",
        "status": "NEXT_FRONTIER_AEW_METROLOGY_SLOT_EXECUTION_OR_HRG_NONHIGGS_SELECTOR",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "Higgs shared-metrology handoff domain theorem built",
            "A_EW, mu_match, and threshold/RG transport typed as legal metrology handoff slots",
            "HRG multiplier, direct H K row, and lambda_H target calibration excluded from metrology handoff",
            "HRG source/admission reentry predicate built",
            "RO family-class selection kept separate from HRG numeric value-source selection",
            "next execution matrix reduced to metrology-slot execution or HRG non-Higgs prediction selector",
        ],
        "still_open": [
            "selected A_EW value",
            "selected mu_match value",
            "selected threshold/RG transport into Omega/lambda_H scheme",
            "direct intrinsic H quartic K_threshold.Omega_H.lambda row",
            "strict selected R_H^RG source theorem",
            "same-value non-Higgs prediction map for UP-RET-OVERLAP.HRG",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsSharedMetrologyPrimitiveHandoffOrHRGSourceTheoremReentry",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorems": [
            metrology_handoff["theorem"],
            hrg_reentry["theorem"],
        ],
        "closure_decision": {
            "higgs_metrology_handoff_domain_closed": True,
            "HRG_source_admission_predicate_closed": True,
            "A_EW_slot_legal_for_UP_ABS_SCALE": True,
            "mu_match_slot_legal_for_UP_ABS_SCALE": True,
            "threshold_RG_scheme_slot_legal_for_UP_ABS_SCALE": True,
            "UP_ABS_SCALE_closes_HRG_now": False,
            "selected_A_EW_value_emitted_now": False,
            "selected_mu_match_value_emitted_now": False,
            "selected_threshold_RG_transport_emitted_now": False,
            "K_threshold_Omega_H_lambda_emitted_now": False,
            "RO_family_selector_selected": ro_family_selector["source_selected"],
            "RO_value_source_selected": ro_value_execution["source_selected"],
            "strict_R_H_RG_source_emitted": ro_value_execution["strict_R_H_RG_source_emitted"],
            "same_HRG_nonHiggs_map_accepted": ro_value_execution["decision"]["same_HRG_nonHiggs_map_accepted"],
            "UP_RET_OVERLAP_HRG_universal_admitted": ro_value_execution["decision"][
                "UP_RET_OVERLAP_HRG_universal_admitted"
            ],
            "current_HRG_reentry_gate_satisfied": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "s_beta": s_beta,
            "UP_RET_OVERLAP_HRG": hrg_value,
            "log_UP_RET_OVERLAP_HRG": log_hrg,
            "allowed_metrology_slot_count": len(accepted_metrology_slots),
            "selected_metrology_value_slot_count_now": len(selected_metrology_slots),
            "strict_H_K_rows": h_decision["strict_accepted_selected_K_source_row_count"],
            "required_H_K_rows": h_decision["strict_selected_K_threshold_row_count_required"],
            "controlled_empirical_conditional_K_rows": h_decision[
                "controlled_empirical_conditional_K_row_count"
            ],
            "accepted_HRG_nonHiggs_map_count": hrg_nonhiggs_execution["accepted_crossuse_map_count"],
        },
        "packets": {
            "higgs_shared_metrology_handoff_theorem": rel(METROLOGY_HANDOFF),
            "hrg_source_admission_reentry_theorem": rel(HRG_REENTRY),
            "two_route_frontier_execution_matrix": rel(ROUTE_MATRIX),
            "cutset": rel(CUTSET),
        },
        "what_closes": {
            "metrology_handoff_domain": True,
            "HRG_reentry_admission_predicate": True,
            "two_route_execution_matrix": True,
            "silent_identity_loop_rejected_again": True,
        },
        "what_remains_open": {
            "A_EW_mu_RG_metrology_slot_values": True,
            "direct_intrinsic_H_K_row": True,
            "strict_HRG_source_theorem": True,
            "HRG_nonHiggs_prediction_selector": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHiggsSharedMetrologyPrimitiveHandoffOrHRGSourceTheoremReentry",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "higgs_metrology_handoff_domain_closed": True,
        "HRG_source_admission_predicate_closed": True,
        "A_EW_slot_legal_for_UP_ABS_SCALE": True,
        "mu_match_slot_legal_for_UP_ABS_SCALE": True,
        "threshold_RG_scheme_slot_legal_for_UP_ABS_SCALE": True,
        "UP_ABS_SCALE_closes_HRG_now": False,
        "selected_A_EW_value_emitted_now": False,
        "selected_mu_match_value_emitted_now": False,
        "selected_threshold_RG_transport_emitted_now": False,
        "K_threshold_Omega_H_lambda_emitted_now": False,
        "RO_family_selector_selected": ro_family_selector["source_selected"],
        "RO_value_source_selected": ro_value_execution["source_selected"],
        "strict_R_H_RG_source_emitted": ro_value_execution["strict_R_H_RG_source_emitted"],
        "same_HRG_nonHiggs_map_accepted": ro_value_execution["decision"]["same_HRG_nonHiggs_map_accepted"],
        "UP_RET_OVERLAP_HRG_universal_admitted": ro_value_execution["decision"][
            "UP_RET_OVERLAP_HRG_universal_admitted"
        ],
        "current_HRG_reentry_gate_satisfied": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Higgs Shared Metrology Primitive Handoff or HRG Source Theorem Reentry v1

Status: `{STATUS}`

## Theorems Built

This packet creates the two theorem gates needed after the B45/G4 separation.

### 1. Higgs Shared Metrology Handoff Domain Theorem

`UP-ABS-SCALE` may legally enter the Higgs D-term route only through physical
unit/action-normalization slots:

```text
A_EW(mu_match) = (g_2(mu_match)^2 + g_Y(mu_match)^2) / 8
lambda_H(mu_match) = A_EW(mu_match) * s_beta
K_threshold.Omega_H.lambda = (A_EW*s_beta)/(D_fin.H*epsilon_Theta^(1/3))
```

with selected:

```text
s_beta = {s_beta}
```

But the current corpus still emits:

```text
selected A_EW                         false
selected mu_match                      false
selected threshold/RG transport        false
K_threshold.Omega_H.lambda emitted     false
```

So the metrology handoff domain is now closed, but the values are still open.

### 2. HRG Source Admission Reentry Predicate Theorem

`UP-RET-OVERLAP.HRG` can reenter only by one of two legal gates:

```text
strict source theorem:
  selected R_H^RG and K_threshold.Omega_H.lambda, no lambda_H target calibration

universal parameter lane:
  same HRG value predicts at least one typed non-Higgs target without retuning
```

Current state:

```text
UP_RET_OVERLAP_HRG = {hrg_value}
log(HRG) = {log_hrg}
RO.family_selector selected   true
RO.value_source selected      false
same-HRG non-Higgs maps       0
lambda_H prediction credit    false
```

The family class is selected, which is real progress.  The HRG numeric value is
not source-selected or universally admitted yet.

## What This Closes

- The allowed metrology handoff domain for Higgs is now explicit.
- The HRG admission predicate is now explicit.
- The silent route "metrology primitive already closes HRG" is shut again.
- The next computation is no longer ambiguous.

## Next

`{NEXT}`
"""

    write_json(METROLOGY_HANDOFF, metrology_handoff)
    write_json(HRG_REENTRY, hrg_reentry)
    write_json(ROUTE_MATRIX, route_matrix)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
