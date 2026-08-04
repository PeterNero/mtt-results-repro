"""Build R_theta matter-slot routing or primitive-C1 no-need theorem packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rtheta_matterslotrouting_or_primitivec1noneedtheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTING_IMPORT = PACKET_DIR / "rtheta_static_matterslot_routing_import.packet.json"
PI_RECHECK = PACKET_DIR / "pi_rtheta_recheck_after_matterslot_routing.packet.json"
PRIMITIVE_GATE = PACKET_DIR / "primitive_c1_noneed_or_overlap_gate.packet.json"
VALUE_GATE = PACKET_DIR / "rtheta_value_gate_after_matterslot_routing_recheck.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_matterslot_routing_recheck.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RThetaMatterSlotRouting_or_PrimitiveC1NoNeedTheorem_v1.md"

PREVIOUS = DATA / "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure.candidate.json"
PREVIOUS_PI = (
    DATA
    / "selected_rtheta_dynamicpievaluator_or_matterslotroutingclosure"
    / "pi_rtheta_recheck_after_dotd_transport_merge.packet.json"
)
MATTERSLOT = DATA / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json"
STATIC_READOUT = (
    DATA
    / "selected_matterslot_readout_backimport_from_smslotfunctor"
    / "selected_static_matterslot_readout.packet.json"
)
READOUT_DECISION = (
    DATA
    / "selected_matterslot_readout_backimport_from_smslotfunctor"
    / "readout_promotion_decision.packet.json"
)
DOWNSTREAM_LEDGER = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
PRIMITIVE_CONTRACTIONS = DATA / "selected_primitivec1_contractions_or_dynamicoverlaptensor_sourceemission.candidate.json"
PRIMITIVE_OVERLAP = DATA / "selected_primitiveoverlapcontractions_valueemission_or_honestgalerkinrun.candidate.json"

STATUS = (
    "MTT_SELECTED_RTHETA_MATTERSLOTROUTING_OR_PRIMITIVEC1NONEEDTHEOREM_"
    "CLOSED_STATIC_ROUTING_PRIMITIVE_OPEN"
)
NEXT = "MTT_Selected_RThetaPrimitiveC1Overlap_or_PiNoNeedTheorem_v1"


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
        raise FileNotFoundError("missing R_theta matter-slot sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_PI,
        MATTERSLOT,
        STATIC_READOUT,
        READOUT_DECISION,
        DOWNSTREAM_LEDGER,
        PRIMITIVE_CONTRACTIONS,
        PRIMITIVE_OVERLAP,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_pi = load(PREVIOUS_PI)
    matterslot = load(MATTERSLOT)
    readout = load(STATIC_READOUT)
    decision = load(READOUT_DECISION)
    ledger = load(DOWNSTREAM_LEDGER)
    primitive_contractions = load(PRIMITIVE_CONTRACTIONS)
    primitive_overlap = load(PRIMITIVE_OVERLAP)

    selected_readouts = readout["selected_readouts"]
    static_routing_closed = (
        matterslot.get("SM_parity_closed") is True
        and matterslot.get("theorem", {}).get("proved") is True
        and matterslot.get("observed_data_used_as_selector") is False
        and matterslot.get("target_fitting_used") is False
        and readout.get("status") == "STATIC_SOURCE_TIER_READOUT_CLOSED"
        and selected_readouts["selected_10M_clock_readout"]["closed"] is True
        and selected_readouts["selected_bar5M_shift_readout"]["closed"] is True
        and selected_readouts["selected_1M_Dirac_shift_readout"]["closed"] is True
        and selected_readouts["selected_phase_shift_partition"]["closed"] is True
        and decision.get("selected_U10_Ubar5_1M_samebranch_emitted_static") is True
        and decision.get("selected_sector_charge_or_chirality_closed_static") is True
        and decision.get("dynamic_C1_promoted") is False
    )
    sufficient_for_rtheta_slot_ownership = static_routing_closed
    primitive_open = (
        primitive_contractions.get("what_remains_open", {}).get("selected_primitive_C1_contractions") is True
        or primitive_overlap.get("what_remains_open", {}).get("selected_primitive_overlap_contraction_values") is True
    )
    primitive_c1_overlap_closed = not primitive_open
    primitive_c1_no_need_theorem_closed = False
    primitive_or_no_need_closed = primitive_c1_overlap_closed or primitive_c1_no_need_theorem_closed

    routing_import = {
        "schema": "MTTRThetaStaticMatterSlotRoutingImport.v1",
        "status": "STATIC_MATTERSLOT_ROUTING_IMPORTED_FOR_RTHETA_SLOT_OWNERSHIP",
        "matter_slot_backimport_source": rel(MATTERSLOT),
        "static_readout_source": rel(STATIC_READOUT),
        "readout_decision_source": rel(READOUT_DECISION),
        "downstream_ledger_source": rel(DOWNSTREAM_LEDGER),
        "selected_10M_clock_readout": selected_readouts["selected_10M_clock_readout"],
        "selected_bar5M_shift_readout": selected_readouts["selected_bar5M_shift_readout"],
        "selected_1M_Dirac_shift_readout": selected_readouts["selected_1M_Dirac_shift_readout"],
        "selected_phase_shift_partition": selected_readouts["selected_phase_shift_partition"],
        "selected_overlap_transfer_normalization_static": selected_readouts[
            "selected_overlap_transfer_normalization_static"
        ],
        "static_matter_slot_routing_closed": static_routing_closed,
        "sufficient_for_Rtheta_slot_ownership": sufficient_for_rtheta_slot_ownership,
        "old_rho_s_invariant_nogo_preserved": decision.get("old_rho_s_invariant_nogo_preserved") is True,
        "dynamic_C1_promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": static_routing_closed,
    }
    write_json(ROUTING_IMPORT, routing_import)

    primitive_gate = {
        "schema": "MTTRThetaPrimitiveC1NoNeedOrOverlapGate.v1",
        "status": "PRIMITIVE_C1_OVERLAP_OR_NONEED_THEOREM_STILL_OPEN",
        "primitive_contractions_source": rel(PRIMITIVE_CONTRACTIONS),
        "primitive_overlap_source": rel(PRIMITIVE_OVERLAP),
        "primitive_C1_overlap_contractions_closed": primitive_c1_overlap_closed,
        "primitive_C1_no_need_theorem_closed": primitive_c1_no_need_theorem_closed,
        "primitive_C1_or_no_need_gate_closed": primitive_or_no_need_closed,
        "open_value_sources": [
            "selected_primitive_C1_contractions",
            "selected_primitive_overlap_contraction_values",
            "selected_dynamic_overlap_tensor_or_transfer_functor",
            "selected_deltaTheta_C1",
            "selected_b_selected_or_Hessian_normalization",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PRIMITIVE_GATE, primitive_gate)

    prev_tests = previous_pi["component_tests_after_dotd_transport_merge"]
    component_tests = dict(prev_tests)
    component_tests.update(
        {
            "selected_matter_slot_routing_available": sufficient_for_rtheta_slot_ownership,
            "selected_static_matter_slot_readout_available": static_routing_closed,
            "primitive_C1_overlap_or_no_need_available": primitive_or_no_need_closed,
        }
    )

    pi_closed = (
        previous["closure_decision"]["stationary_sector_transfer_closed"]
        and previous["closure_decision"]["selected_stationary_rho_s_closed"]
        and previous["closure_decision"]["dotD_alpha1_transport_subgate_closed"]
        and sufficient_for_rtheta_slot_ownership
        and primitive_or_no_need_closed
    )

    remaining_missing = [
        "primitive_C1_overlap_contractions_or_no-need theorem for Pi_Rtheta"
    ]
    pi_recheck = {
        "schema": "MTTPiRThetaRecheckAfterMatterSlotRouting.v1",
        "status": "PI_RTHETA_RECHECKED_MATTERSLOT_ROUTING_CLOSED_PRIMITIVE_C1_OPEN",
        "previous_pi_recheck": rel(PREVIOUS_PI),
        "component_tests_after_matterslot_routing": component_tests,
        "retired_missing_primitives": [
            "selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership"
        ],
        "still_retired_from_previous": previous_pi["retired_missing_primitives"],
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "new_minimal_missing_primitives": remaining_missing,
        "why_not_closed": [
            "static matter-slot ownership is now selected, but no primitive C1 overlap tensor has been emitted",
            "no theorem has been supplied proving Pi_Rtheta can evaluate R_theta coefficients without primitive C1 overlaps",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PI_RECHECK, pi_recheck)

    value_gate = {
        "schema": "MTTRThetaValueGateAfterMatterSlotRoutingRecheck.v1",
        "status": "RTHETA_VALUES_STILL_REJECTED_PRIMITIVE_C1_OPEN",
        "stationary_sector_transfer_closed": previous["closure_decision"]["stationary_sector_transfer_closed"],
        "dotD_alpha1_transport_subgate_closed": previous["closure_decision"][
            "dotD_alpha1_transport_subgate_closed"
        ],
        "matter_slot_routing_closed": sufficient_for_rtheta_slot_ownership,
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
        "schema": "MTTNextCutsetAfterMatterSlotRoutingRecheck.v1",
        "status": "NEXT_ATTACK_RTHETA_PRIMITIVE_C1_OVERLAP_OR_PI_NONEED",
        "closed_now": {
            "selected_matter_slot_routing_or_1M_rule_for_Rtheta_slot_ownership": sufficient_for_rtheta_slot_ownership,
            "static_source_tier_matter_slot_readout": static_routing_closed,
            "values_still_rejected_without_primitive_C1": True,
        },
        "still_open": remaining_missing,
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "prove Pi_Rtheta no-need: R_theta coefficients depend only on stationary rho_s, dotD_alpha1, and static slot ownership",
            "route_B": "emit selected primitive C1 overlap contractions from the dynamic overlap tensor/Galerkin response",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedRThetaMatterSlotRoutingOrPrimitiveC1NoNeedTheorem",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "rtheta_static_matterslot_routing_import": rel(ROUTING_IMPORT),
            "pi_rtheta_recheck_after_matterslot_routing": rel(PI_RECHECK),
            "primitive_c1_noneed_or_overlap_gate": rel(PRIMITIVE_GATE),
            "rtheta_value_gate_after_matterslot_routing_recheck": rel(VALUE_GATE),
            "next_cutset_after_matterslot_routing_recheck": rel(CUTSET),
        },
        "theorem": {
            "name": "RThetaStaticMatterSlotRoutingPromotionTheorem",
            "proved": static_routing_closed,
            "statement": (
                "The selected SM-slot functor back-import emits the static source-tier matter-slot "
                "ownership required by R_theta: 10_M routes to u,e; bar5_M routes to d; 1_M=N^c "
                "routes to nuD; and the q79 U_10/U_bar5 polarization plus trace normalization are "
                "selected without observed data or locked C1 targets. This retires the R_theta "
                "matter-slot/1_M ownership blocker. It does not emit primitive C1 overlap contractions "
                "or prove they are unnecessary for Pi_Rtheta."
            ),
        },
        "closure_decision": {
            "stationary_sector_transfer_closed": previous["closure_decision"]["stationary_sector_transfer_closed"],
            "selected_stationary_rho_s_closed": previous["closure_decision"]["selected_stationary_rho_s_closed"],
            "dotD_alpha1_transport_subgate_closed": previous["closure_decision"][
                "dotD_alpha1_transport_subgate_closed"
            ],
            "matter_slot_routing_closed": sufficient_for_rtheta_slot_ownership,
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
        "source_tier_note": ledger["payload_tiers"]["static_sm_slot_tier"],
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTTSelectedRThetaMatterSlotRoutingOrPrimitiveC1NoNeedTheorem",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "matter_slot_routing_closed": sufficient_for_rtheta_slot_ownership,
        "primitive_C1_or_no_need_gate_closed": primitive_or_no_need_closed,
        "Pi_Rtheta_closed": pi_closed,
        "accepted_coefficient_value_count": 0,
        "theorem_proved": static_routing_closed,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RThetaMatterSlotRouting or PrimitiveC1NoNeedTheorem v1

Status: `{STATUS}`.

This artifact imports the selected static SM-slot functor readout into the
`R_theta` dynamic `Pi` frontier.

```text
static matter-slot routing closed             : {str(static_routing_closed).lower()}
sufficient for R_theta slot ownership         : {str(sufficient_for_rtheta_slot_ownership).lower()}
primitive C1 overlap/no-need gate closed      : {str(primitive_or_no_need_closed).lower()}
Pi_Rtheta closed                              : {str(pi_closed).lower()}
accepted coefficient values                   : 0
```

The retired blocker is now:

- selected matter-slot routing or `1_M` rule for `R_theta` slot ownership.

The imported ownership rule is:

- `10_M` / clock / phase routes to `u,e`;
- `bar5_M` / shift routes to `d`;
- `1_M=N^c` / Dirac-neutrino shift routes to `nuD`.

The old `rho_s`-only no-go is not contradicted: `rho_s` alone was invariant.
The selected source-tier SM-slot functor supplies the missing grading/readout.

The remaining `Pi_Rtheta` frontier is now a single blocker:

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
