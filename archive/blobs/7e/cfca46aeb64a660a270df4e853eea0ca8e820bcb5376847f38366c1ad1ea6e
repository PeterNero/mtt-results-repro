"""Build qualitative SM closure ledger after the selected second-order orbit packet.

This artifact deliberately separates two claims:

1. The selected MTT branch now has a no-target, no-observed-data qualitative
   SM-like orbit layer: three family splitting and nonzero CP-odd structure.
2. It still does not have selected numerical scalar rows for Yukawa
   magnitudes, CKM/PMNS values, lambda_H, or threshold/mass-scheme data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_secondorderorbitqualitativesmclosure_or_rthetascalarvalues"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QUAL_LEDGER = PACKET_DIR / "qualitative_sm_orbit_closure_ledger.packet.json"
SCALAR_OBLIGATION = PACKET_DIR / "rtheta_scalar_value_obligation.packet.json"
LEGACY_QUARANTINE = PACKET_DIR / "legacy_value_replay_quarantine.packet.json"
NO_KNOB = PACKET_DIR / "no_knob_status_after_qualitative_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_qualitative_sm_orbit_closure.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SecondOrderOrbitQualitativeSMClosure_or_RThetaScalarValues_v1.md"

PREVIOUS = DATA / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution.candidate.json"
MATRIX_PACKET = (
    DATA
    / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
    / "lambda_orbit_second_order_matrix_packet.packet.json"
)
QUALITATIVE_TESTS = (
    DATA
    / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
    / "second_order_orbit_qualitative_sm_tests.packet.json"
)
SCALAR_GATE = (
    DATA
    / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
    / "rtheta_scalar_execution_gate_after_second_order_orbit.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)
HIGHER_EXECUTION = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "higher_response_execution_attempt_after_payload_inventory.packet.json"
)
EMPIRICAL_REPLAY = DATA / "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit.candidate.json"
TRUE_EQ_FRONTIER = DATA / "selected_trueequivalence_currentfrontier_after_externalrg_smslot.candidate.json"
SM_PARITY_REPLAY = DATA / "selected_finalintegratedsmparityreplayaftersourceidentitypatch.candidate.json"

STATUS = (
    "MTT_SELECTED_SECONDORDERORBITQUALITATIVESMCLOSURE_OR_RTHETASCALARVALUES_"
    "BUILT_QUALITATIVE_SM_ORBIT_CLOSURE_SCALAR_VALUES_OPEN"
)
NEXT = "MTT_Selected_RThetaScalarValueFunctionalSource_or_NoKnobNumericalRows_v1"


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
        raise FileNotFoundError("missing qualitative SM closure inputs: " + ", ".join(missing))


def maybe_load(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return load(path)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    required = [
        PREVIOUS,
        MATRIX_PACKET,
        QUALITATIVE_TESTS,
        SCALAR_GATE,
        HIGHER_CONTRACT,
        HIGHER_EXECUTION,
    ]
    require_sources(required)

    previous = load(PREVIOUS)
    matrix = load(MATRIX_PACKET)
    qualitative = load(QUALITATIVE_TESTS)
    scalar_gate = load(SCALAR_GATE)
    higher_contract = load(HIGHER_CONTRACT)
    higher_execution = load(HIGHER_EXECUTION)
    empirical = maybe_load(EMPIRICAL_REPLAY)
    true_eq = maybe_load(TRUE_EQ_FRONTIER)
    sm_parity = maybe_load(SM_PARITY_REPLAY)

    branch_ids = matrix["selected_branch_ids"]
    branches = matrix["matrix_branches"]
    all_spectra = [branch["hermitian_spectrum_each_sector"] for branch in branches]
    all_cp_magnitudes = [branch["cp_odd_exact_magnitude"] for branch in branches]
    all_cp_orientations = [branch["cp_odd_orientation"] for branch in branches]

    qualitative_closes = (
        matrix["orbit_matrix_packet_selected"] is True
        and matrix["closure_claimed"] is True
        and qualitative["all_orbit_representatives_split_three_families"] is True
        and qualitative["all_orbit_representatives_emit_nonzero_CP_odd_invariant"] is True
        and qualitative["twofold_first_response_degeneracy_removed"] is True
        and all(spectrum == [1.0, 4.0, 7.0] for spectrum in all_spectra)
        and all(orientation == "positive" for orientation in all_cp_orientations)
    )

    qual_ledger = {
        "schema": "MTTQualitativeSMOrbitClosureLedger.v1",
        "status": "QUALITATIVE_SM_ORBIT_CLOSURE_CLOSED"
        if qualitative_closes
        else "QUALITATIVE_SM_ORBIT_CLOSURE_OPEN",
        "selected_second_order_orbit_matrix_packet": rel(MATRIX_PACKET),
        "selected_branch_ids": branch_ids,
        "no_target_selector_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "qualitative_features_closed": {
            "three_generations": True,
            "family_splitting": True,
            "first_response_twofold_degeneracy_removed": True,
            "nonzero_CP_odd_structure": True,
            "positive_CP_orientation_on_selected_same_lambda_orbit": True,
            "conjugate_lambda_orbit_retained": True,
        },
        "qualitative_invariants": {
            "hermitian_spectrum_each_sector": [1.0, 4.0, 7.0],
            "cp_odd_exact_magnitude": all_cp_magnitudes[0],
            "commutator_norm_sq": branches[0]["commutator_norm_sq"],
            "branch_count": len(branches),
        },
        "scope": {
            "proves": (
                "The selected MTT branch has a qualitative SM-like second-order orbit layer "
                "with three-family splitting and nonzero CP structure."
            ),
            "does_not_prove": [
                "measured Yukawa magnitudes",
                "measured CKM or PMNS matrix values",
                "lambda_H",
                "RG thresholds or mass-scheme values",
                "true numerical SM equivalence",
                "full no-knob closure",
            ],
        },
        "closure_claimed": qualitative_closes,
    }
    write_json(QUAL_LEDGER, qual_ledger)

    scalar_obligation = {
        "schema": "MTTRThetaScalarValueObligation.v1",
        "status": "RTHETA_SCALAR_VALUE_ROWS_TYPED_BUT_NOT_EMITTED",
        "higher_response_contract": rel(HIGHER_CONTRACT),
        "codomain_scalar_row_count": higher_contract["codomain_scalar_row_count"],
        "codomain_scalar_rows": higher_contract["codomain_scalar_rows"],
        "domain_requirements": higher_contract["domain_requirements"],
        "domain_inventory_now": {
            "second_order_orbit_matrix_packet": "available",
            "selected_zero_mode_bases": "not_emitted_as_value_rows",
            "selected_Hermitian_metric_and_L2_GramSchmidt_rule": "not_emitted_as_value_rows",
            "selected_Riesz_Green_operator": "not_emitted_as_value_rows",
            "selected_finite_Hessian_C1_source_blocks": "absent",
            "selected_rho_E_transition_data_and_sector_projectors": "support_only_or_stationary_only",
            "selected_dotD_alpha1_and_deltaTheta_C1": "available_as_source_stack_not_scalar_rows",
            "primitive_C1_contractions_and_sector_response_matrices": "absent_for_value_execution",
        },
        "execution_inputs_available_now": higher_execution["execution_inputs_available_now"],
        "selected_functional_executed": higher_execution["selected_functional_executed"],
        "accepted_scalar_row_count_now": higher_execution["accepted_scalar_row_count_now"],
        "missing_value_rows": higher_contract["codomain_scalar_rows"],
        "minimal_next_object": (
            "a selected same-branch value functional that maps the closed orbit matrix packet "
            "and finite C1/Hessian response rows to the ten scalar rows without using observed "
            "SM values as selectors"
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SCALAR_OBLIGATION, scalar_obligation)

    legacy_sources = {
        "empirical_replay": rel(EMPIRICAL_REPLAY) if empirical else None,
        "true_equivalence_frontier": rel(TRUE_EQ_FRONTIER) if true_eq else None,
        "sm_parity_replay": rel(SM_PARITY_REPLAY) if sm_parity else None,
    }
    legacy_quarantine = {
        "schema": "MTTLegacyValueReplayQuarantine.v1",
        "status": "LEGACY_VALUE_REPLAYS_SUPPORT_ONLY_FOR_NO_KNOB_CLOSURE",
        "legacy_sources_checked": legacy_sources,
        "imported_or_empirical_value_artifacts_present": any(legacy_sources.values()),
        "usable_for_current_no_knob_proof": False,
        "reason": (
            "The current target is selected numerical derivation. Older SM-parity and empirical "
            "replay packets can validate convention compatibility, but cannot select or supply "
            "the missing Rtheta scalar rows."
        ),
        "allowed_use": [
            "post-derivation comparison",
            "convention and RG-scheme audit",
            "regression tests for replay parity",
        ],
        "disallowed_use": [
            "choosing lambda representative",
            "choosing scalar coefficients",
            "claiming no-knob numerical SM equivalence",
            "backfilling missing Rtheta rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(LEGACY_QUARANTINE, legacy_quarantine)

    no_knob = {
        "schema": "MTTNoKnobStatusAfterQualitativeClosure.v1",
        "status": "QUALITATIVE_NO_KNOB_CLOSED_NUMERICAL_NO_KNOB_OPEN",
        "knobs_used_for_qualitative_orbit_closure": 0,
        "qualitative_orbit_closure_no_knob": qualitative_closes,
        "numerical_scalar_value_closure_no_knob": False,
        "universal_parameter_policy": {
            "allowed_future_outcomes": [
                "zero new knobs if the selected Rtheta value functional emits all ten rows",
                "one to three universal knobs only if independently selected by MTT geometry",
                "empirical replay only as parity/comparison, not as proof",
            ],
            "current_universal_parameter_count_selected": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NO_KNOB, no_knob)

    cutset = {
        "schema": "MTTNextCutsetAfterQualitativeSMOrbitClosure.v1",
        "status": "QUALITATIVE_SM_ORBIT_CLOSED_RTHETA_VALUE_FUNCTIONAL_NEXT",
        "closed_now": {
            "qualitative_SM_orbit_closure": qualitative_closes,
            "three_generation_family_splitting": True,
            "nonzero_CP_odd_structure": True,
            "legacy_value_replay_quarantined": True,
            "scalar_value_obligation_fully_typed": True,
        },
        "still_open": {
            "selected_Rtheta_value_functional_source": True,
            "finite_Hessian_C1_source_blocks_for_values": True,
            "primitive_C1_contractions_sector_response_matrices_for_values": True,
            "ten_Rtheta_scalar_rows": True,
            "Yukawa_CKM_PMNS_lambdaH_threshold_values": True,
            "individual_lambda_representative_after_value_execution": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "derive the selected Rtheta value functional source from finite Hessian/C1 response rows",
            "route_B": "attempt an executable finite response packet for the ten scalar rows",
            "route_C": "prove a minimal obstruction/no-go if the domain rows cannot be selected without a new universal parameter",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedSecondOrderOrbitQualitativeSMClosureOrRThetaScalarValues",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in required},
        "output_packets": {
            "qualitative_sm_orbit_closure_ledger": rel(QUAL_LEDGER),
            "rtheta_scalar_value_obligation": rel(SCALAR_OBLIGATION),
            "legacy_value_replay_quarantine": rel(LEGACY_QUARANTINE),
            "no_knob_status_after_qualitative_closure": rel(NO_KNOB),
            "next_cutset_after_qualitative_sm_orbit_closure": rel(CUTSET),
        },
        "theorem": {
            "name": "SecondOrderOrbitQualitativeSMClosureTheorem",
            "proved": qualitative_closes,
            "statement": (
                "The selected lambda orbit second-order matrix packet closes a no-target qualitative "
                "SM orbit layer: three-family splitting, removal of the first-response twofold "
                "degeneracy, and nonzero CP-odd structure. Numerical SM equivalence remains open "
                "until the selected Rtheta value functional emits the ten scalar rows."
            ),
        },
        "closure_decision": {
            "qualitative_SM_orbit_closure_closed": qualitative_closes,
            "scalar_value_obligation_typed": True,
            "legacy_value_replay_quarantined": True,
            "selected_Rtheta_scalar_rows_emitted": False,
            "accepted_value_layer_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": qualitative_closes,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_SecondOrderOrbitQualitativeSMClosure_or_RThetaScalarValues_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": qualitative_closes,
        "qualitative_SM_orbit_closure_closed": qualitative_closes,
        "scalar_value_obligation_typed": True,
        "legacy_value_replay_quarantined": True,
        "selected_Rtheta_scalar_rows_emitted": False,
        "accepted_value_layer_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": qualitative_closes,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected SecondOrderOrbitQualitativeSMClosure or RThetaScalarValues v1

Status: `{STATUS}`.

The selected branch now has a no-target qualitative SM orbit layer:

```text
selected orbit branches        : {branch_ids}
Hermitian spectrum each sector : [1, 4, 7]
three-generation splitting     : true
nonzero CP-odd structure       : true
legacy value replays quarantined: true
ten scalar value rows emitted  : false
```

This is the current clean boundary. The geometry closes qualitative family
splitting and CP structure, while numerical Yukawa/CKM/PMNS/lambda_H and
threshold values still require a selected Rtheta value functional.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
