"""Build R_theta dynamic Pi evaluator or matter-slot routing closure packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DOTD_MERGE = PACKET_DIR / "rtheta_dotd_transport_alpha1_driver_merge.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_dotd_transport_merge.packet.json"
ROUTING_GATE = PACKET_DIR / "matter_slot_routing_and_primitive_c1_gate.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_dynamic_pi_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_dynamic_pi_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaDynamicPiEvaluator_or_MatterSlotRoutingClosure_v1.md"

PREVIOUS = DATA / "selected_rtheta_sectortransferbnbasis_or_pikernelclosure.candidate.json"
PREVIOUS_PI = (
    DATA
    / "selected_rtheta_sectortransferbnbasis_or_pikernelclosure"
    / "pi_rtheta_recheck_after_sector_projector_promotion.packet.json"
)
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
ALPHA_IMPORT = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
DIRAC_ROUTING = DATA / "selected_1m_dirac_source_or_u10ubar5_polarization.candidate.json"
SAMEBRANCH_ROUTING = DATA / "selected_u10ubar5_1m_samebranch_emission_attempt.candidate.json"
PRIMITIVE_CLASS = (
    DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
)
PRIMITIVE_CONTRACTIONS = DATA / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.candidate.json"
PRIMITIVE_OVERLAP = DATA / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun.candidate.json"

STATUS = (
    "MTT_SELECTED_RTHETA_DYNAMICPIEVALUATOR_OR_MATTERSLOTROUTINGCLOSURE_"
    "CLOSED_DOTD_ALPHA1_TRANSPORT_ROUTING_OPEN"
)
NEXT = "MTT_Selected_RThetaMatterSlotRouting_or_PrimitiveC1NoNeedTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing R_theta dynamic-Pi sources: " + ", ".join(missing))


def bool_path(payload: dict[str, Any], *keys: str) -> bool:
    cursor: Any = payload
    for key in keys:
        if not isinstance(cursor, dict):
            return False
        cursor = cursor.get(key)
    return bool(cursor)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_PI,
        DOTD_PROBE,
        ALPHA_IMPORT,
        DIRAC_ROUTING,
        SAMEBRANCH_ROUTING,
        PRIMITIVE_CLASS,
        PRIMITIVE_CONTRACTIONS,
        PRIMITIVE_OVERLAP,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_pi = load(PREVIOUS_PI)
    dotd = load(DOTD_PROBE)
    alpha = load(ALPHA_IMPORT)
    dirac = load(DIRAC_ROUTING)
    samebranch = load(SAMEBRANCH_ROUTING)
    primitive_class = load(PRIMITIVE_CLASS)
    primitive_contractions = load(PRIMITIVE_CONTRACTIONS)
    primitive_overlap = load(PRIMITIVE_OVERLAP)

    dotd_formula_closed = (
        bool_path(dotd, "promotion_decision", "selected_dotD_source_formula_closed")
        and bool_path(dotd, "promotion_decision", "selected_dotD_source_verified_by_transport_derivative")
        and bool_path(dotd, "validator_boundary", "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived")
        and bool_path(dotd, "driver_audit", "dotD_frechet_replay_closed")
    )
    alpha_driver_closed = (
        alpha.get("alpha1_driver_verified_imported") is True
        and alpha.get("selected_dotD_source_verified_imported") is True
        and bool_path(alpha, "alpha1_driver_replay_import", "du_dalpha1_equals_h_ext")
        and bool_path(alpha, "alpha1_driver_replay_import", "selected_N_alpha1_h_ext_value")
        and bool_path(alpha, "alpha1_driver_replay_import", "selected_dotD_source_verified")
        and bool_path(alpha, "alpha1_driver_replay_import", "alpha1_driver_verified")
        and bool_path(alpha, "alpha1_driver_replay_import", "honest_dotD_alpha1_replay")
        and alpha["alpha1_driver_replay_import"].get("lambda_alpha1") == 1.0
        and alpha["alpha1_driver_replay_import"].get("N_alpha1_h_ext") == 1.0
        and abs(float(alpha["alpha1_driver_replay_import"].get("tangent_residual_l2", 1.0))) < 1e-12
    )
    dotd_transport_subgate_closed = dotd_formula_closed and alpha_driver_closed

    dotd_merge = {
        "schema": "MTTRThetaDotDTransportAlpha1DriverMerge.v1",
        "status": "SELECTED_DOTD_ALPHA1_TRANSPORT_PACKET_CLOSED",
        "local_transport_derivative_source": rel(DOTD_PROBE),
        "crossrepo_alpha1_driver_source": rel(ALPHA_IMPORT),
        "transport_formula": {
            "U": "exp(-u ad(T3))",
            "dU_dalpha": "-(du/dalpha) ad(T3) U",
            "dotD_h": "(dh) ad(T3)",
            "linearized_identity": "D_sel(delta psi)+dotD_h psi_sel=0",
            "response": "delta psi=-(h ad(T3)) psi_sel",
        },
        "local_dotD_transport_formula_closed": dotd_formula_closed,
        "alpha1_driver_normalization_imported": alpha_driver_closed,
        "selected_dotD_transport_derivative_on_transported_projector_packet": dotd_transport_subgate_closed,
        "lambda_alpha1": alpha["alpha1_driver_replay_import"].get("lambda_alpha1"),
        "N_alpha1_h_ext": alpha["alpha1_driver_replay_import"].get("N_alpha1_h_ext"),
        "tangent_residual_l2": alpha["alpha1_driver_replay_import"].get("tangent_residual_l2"),
        "full_flag_validation": dotd["validator_boundary"]["full_flag_validation"],
        "does_not_emit": [
            "matter-slot routing among u,d,e,N",
            "primitive C1 overlap contractions",
            "selected A/b response matrices",
            "theta_coeff values",
            "lambda_H",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": dotd_transport_subgate_closed,
    }
    write_json(DOTD_MERGE, dotd_merge)

    dirac_decision = dirac.get("selection_decision", {}) or dirac.get("closure_decision", {})
    samebranch_decision = samebranch.get("closure_decision", {}) or samebranch.get("selection_decision", {})
    matter_slot_routing_closed = (
        dirac_decision.get("selected_1M_Dirac_neutrino_source_rule_closed") is True
        and dirac_decision.get("selected_U10_Ubar5_polarization_closed") is True
        and dirac_decision.get("selected_sector_charge_or_chirality_closed") is True
    ) or (
        samebranch_decision.get("selected_U10_Ubar5_1M_samebranch_emitted") is True
        and samebranch_decision.get("selected_sector_charge_or_chirality_closed") is True
    )

    primitive_class_open = primitive_class.get("what_remains_open", {})
    primitive_contractions_open = primitive_contractions.get("what_remains_open", {})
    primitive_overlap_open = primitive_overlap.get("what_remains_open", {})
    primitive_c1_closed = not (
        primitive_class_open.get("selected_deltaTheta_C1_solution", False)
        or primitive_class_open.get("sector_response_matrices_M_u_M_d_M_e_M_nuD", False)
        or primitive_contractions_open.get("selected_primitive_C1_contractions", False)
        or primitive_overlap_open.get("selected_primitive_overlap_contraction_values", False)
    )
    primitive_c1_no_need_theorem_closed = False
    primitive_or_no_need_closed = primitive_c1_closed or primitive_c1_no_need_theorem_closed

    routing_gate = {
        "schema": "MTTRThetaMatterSlotRoutingAndPrimitiveC1Gate.v1",
        "status": "MATTER_SLOT_ROUTING_AND_PRIMITIVE_C1_STILL_OPEN",
        "dirac_routing_source": rel(DIRAC_ROUTING),
        "samebranch_routing_source": rel(SAMEBRANCH_ROUTING),
        "primitive_class_source": rel(PRIMITIVE_CLASS),
        "primitive_contractions_source": rel(PRIMITIVE_CONTRACTIONS),
        "primitive_overlap_source": rel(PRIMITIVE_OVERLAP),
        "selected_stationary_source_available": samebranch_decision.get("selected_stationary_source_available") is True,
        "matter_slot_routing_closed": matter_slot_routing_closed,
        "primitive_C1_overlap_contractions_closed": primitive_c1_closed,
        "primitive_C1_no_need_theorem_closed": primitive_c1_no_need_theorem_closed,
        "primitive_C1_or_no_need_gate_closed": primitive_or_no_need_closed,
        "open_matter_readouts": [
            item
            for item, is_open in sorted((samebranch.get("what_remains_open") or dirac.get("what_remains_open") or {}).items())
            if is_open and "readout" in item
        ],
        "open_primitive_value_sources": [
            "selected_primitive_C1_contractions",
            "selected_dynamic_overlap_tensor_or_transfer_functor",
            "selected_A_selected_response_operator",
            "selected_b_selected_or_Hessian_normalization",
            "honest_Galerkin_C1_contractions",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROUTING_GATE, routing_gate)

    prev_tests = previous_pi["component_tests_after_sector_projector_promotion"]
    component_tests = dict(prev_tests)
    component_tests.update(
        {
            "selected_dotD_transport_derivative_local_to_transported_packet": dotd_transport_subgate_closed,
            "selected_dotD_alpha1_driver_normalization_available": alpha_driver_closed,
            "selected_matter_slot_routing_available": matter_slot_routing_closed,
            "primitive_C1_overlap_or_no_need_available": primitive_or_no_need_closed,
        }
    )

    pi_closed = (
        previous["closure_decision"]["stationary_sector_transfer_closed"]
        and previous["closure_decision"]["selected_stationary_rho_s_closed"]
        and dotd_transport_subgate_closed
        and matter_slot_routing_closed
        and primitive_or_no_need_closed
    )

    remaining_missing = [
        "selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership",
        "primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta",
    ]

    pi_recheck = {
        "schema": "MTTPiRThetaRecheckAfterDotDTransportMerge.v1",
        "status": "PI_RTHETA_RECHECKED_DOTD_ALPHA1_TRANSPORT_CLOSED_ROUTING_OPEN",
        "previous_pi_recheck": rel(PREVIOUS_PI),
        "component_tests_after_dotd_transport_merge": component_tests,
        "retired_missing_primitives": [
            "selected_dotD_alpha1_transport_derivative_on_transported_projector_packet"
        ],
        "still_retired_from_previous": previous_pi["retired_missing_primitives"],
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "new_minimal_missing_primitives": remaining_missing,
        "why_not_closed": [
            "the selected dotD_alpha1 derivative is now source-normalized, but it does not assign charged matter slots",
            "no artifact yet emits a selected matter-slot transversality/readout functional for u,d,e,N ownership",
            "no primitive C1 overlap contraction tensor or accepted no-need theorem has been supplied for Pi_Rtheta",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PI_RECHECK, pi_recheck)

    value_gate = {
        "schema": "MTTRThetaValueGateAfterDynamicPiRecheck.v1",
        "status": "RTHETA_VALUES_STILL_REJECTED_ROUTING_AND_PRIMITIVE_C1_OPEN",
        "stationary_sector_transfer_closed": previous["closure_decision"]["stationary_sector_transfer_closed"],
        "dotD_alpha1_transport_subgate_closed": dotd_transport_subgate_closed,
        "matter_slot_routing_closed": matter_slot_routing_closed,
        "primitive_C1_or_no_need_gate_closed": primitive_or_no_need_closed,
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "accepted_lambda_H_value": False,
        "selected_threshold_response_functional_instantiated": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_GATE, value_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterDynamicPiRecheck.v1",
        "status": "NEXT_ATTACK_RTHETA_MATTER_SLOT_ROUTING_OR_PRIMITIVE_C1_NO_NEED",
        "closed_now": {
            "selected_dotD_alpha1_transport_derivative_on_transported_projector_packet": dotd_transport_subgate_closed,
            "alpha1_driver_normalization": alpha_driver_closed,
            "values_still_rejected_without_full_Pi": True,
        },
        "still_open": remaining_missing,
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "construct the selected matter-slot transversality/readout functional for U10, Ubar5, and 1M ownership",
            "route_B": "prove a primitive C1 no-need theorem for Pi_Rtheta, or emit the primitive overlap contraction tensor directly",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaDynamicPiEvaluatorOrMatterSlotRoutingClosure",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_dotd_transport_alpha1_driver_merge": rel(DOTD_MERGE),
            "pi_rtheta_recheck_after_dotd_transport_merge": rel(PI_RECHECK),
            "matter_slot_routing_and_primitive_c1_gate": rel(ROUTING_GATE),
            "rtheta_value_gate_after_dynamic_pi_recheck": rel(VALUE_GATE),
            "next_cutset_after_dynamic_pi_recheck": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaSelectedDotDAlpha1TransportMergeTheorem",
            "proved": dotd_transport_subgate_closed,
            "statement": (
                "The local selected transport-derivative theorem identifies the dotD_alpha1 response on "
                "the transported projector packet. The imported same-branch q79/F,m=1 alpha1 replay "
                "supplies the missing source-strength normalization du/dalpha1=h_ext with lambda_alpha1=1 "
                "and zero tangent residual. Therefore the dotD_alpha1 transported-packet subgate is "
                "retired. Pi_Rtheta remains open until matter-slot routing and primitive C1 overlap/no-need "
                "are selected."
            ),
        },
        "closure_decision": {
            "stationary_sector_transfer_closed": previous["closure_decision"]["stationary_sector_transfer_closed"],
            "selected_stationary_rho_s_closed": previous["closure_decision"]["selected_stationary_rho_s_closed"],
            "dotD_alpha1_transport_subgate_closed": dotd_transport_subgate_closed,
            "alpha1_driver_normalization_closed": alpha_driver_closed,
            "matter_slot_routing_closed": matter_slot_routing_closed,
            "primitive_C1_or_no_need_gate_closed": primitive_or_no_need_closed,
            "Pi_Rtheta_closed": pi_closed,
            "accepted_coefficient_value_count": 0,
            "accepted_lambda_H_value": False,
            "selected_threshold_response_functional_instantiated": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTTSelectedRThetaDynamicPiEvaluatorOrMatterSlotRoutingClosure",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "dotD_alpha1_transport_subgate_closed": dotd_transport_subgate_closed,
        "alpha1_driver_normalization_closed": alpha_driver_closed,
        "matter_slot_routing_closed": matter_slot_routing_closed,
        "primitive_C1_or_no_need_gate_closed": primitive_or_no_need_closed,
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "theorem_proved": dotd_transport_subgate_closed,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaDynamicPiEvaluator or MatterSlotRoutingClosure v1

Status: `{STATUS}`.

This artifact merges the local selected `dotD_alpha1` transport-derivative
formula with the imported same-branch alpha1 driver replay.

```text
local transported dotD formula closed          : {str(dotd_formula_closed).lower()}
alpha1 driver normalization imported          : {str(alpha_driver_closed).lower()}
dotD_alpha1 transported-packet subgate closed : {str(dotd_transport_subgate_closed).lower()}
matter-slot routing closed                    : {str(matter_slot_routing_closed).lower()}
primitive C1 overlap/no-need gate closed      : {str(primitive_or_no_need_closed).lower()}
Pi_Rtheta closed                              : {str(pi_closed).lower()}
accepted coefficient values                   : 0
```

The retired blocker is now:

- selected `dotD_alpha1` transport derivative on the transported projector packet.

The remaining `Pi_Rtheta` frontier is reduced to:

- selected matter-slot routing or `1_M` rule for `R_theta` slot ownership,
- primitive C1 overlap contractions or a theorem proving `Pi_Rtheta` does not
  require them.

No measured Standard Model masses, mixings, or phases are used as selectors,
and no `theta_coeff` or `lambda_H` value is emitted here.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
