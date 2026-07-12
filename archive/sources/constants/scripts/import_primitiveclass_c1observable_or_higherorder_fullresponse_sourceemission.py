"""Import primitive-class C1 observable / higher-order response frontier."""

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

PREVIOUS = CERTS / "primitive_fibershift_or_typed_retarded_selector_sourcetheorem_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
SM_CERT = SM / "certificates" / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_certificate.json"

OUTPUT_PACKET = DATA / "primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_import.candidate.json"
OUTPUT_CERT = CERTS / "primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_import_certificate.json"
OUTPUT_NOTE = CORPUS / "PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_Import_v1.md"

STATUS = "PRIMITIVECLASS_C1OBSERVABLE_IMPORTED_HIGHERORDER_FULLRESPONSE_VALUES_OPEN"
PREVIOUS_STATUS = "PRIMITIVE_FIBERCLASS_QUOTIENT_IMPORTED_HIGHERORDER_FULLRESPONSE_OPEN"
SM_STATUS = "MTT_SELECTED_PRIMITIVECLASS_C1OBSERVABLE_OR_HIGHERORDER_FULLRESPONSE_SOURCEEMISSION_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    observable = sm_packet["primitive_class_C1_observable_packet"]
    emission = sm_packet["higherorder_or_fullresponse_source_emission_packet"]
    promotion = sm_packet["promotion_decision"]
    remains = sm_packet["what_remains_open"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_cert["selected_values_available"] is False,
        "G2_primitive_observable_layer_emitted": observable["active_shift"] == [1, 1]
        and observable["fixed_fiber_quotient_class"] == [0, 1, 2]
        and observable["computation_representative"] == "fiber_shift_0"
        and observable["all_representatives_scalar_identity"] is True
        and observable["all_representatives_same_scalar"] is True,
        "G3_current_layer_flavor_nogo": observable["flavor_splitting_possible_at_current_layer"] is False
        and promotion["current_primitive_class_promoted_as_flavor_closure"] is False
        and emission["current_layer_status"]["no_go_proved"] is True,
        "G4_alpha1_dotD_retired_as_active_blocker": emission["alpha1_dotD_status"][
            "active_blocker"
        ]
        is False
        and emission["alpha1_dotD_status"]["alpha1_driver_verified_imported"] is True
        and emission["alpha1_dotD_status"]["selected_dotD_source_verified_imported"] is True
        and emission["alpha1_dotD_status"]["honest_dotD_alpha1_replay_imported"] is True,
        "G5_higherorder_acceptance_packet_built_values_open": emission["current_layer_status"][
            "higher_order_criterion_proved"
        ]
        is True
        and emission["current_layer_status"]["full_response_criterion_proved"] is True
        and emission["current_layer_status"]["current_values_available"] is False
        and emission["source_emission_status"]["source_emission_contract_built"] is True
        and emission["source_emission_status"]["selected_source_emits_splitter"] is False,
        "G6_delta_gate_built_no_A_b": emission["deltaTheta_gate_status"]["delta_solve_gate_built"]
        is True
        and emission["deltaTheta_gate_status"]["A_selected_claimed"] is False
        and emission["deltaTheta_gate_status"]["b_selected_claimed"] is False
        and emission["deltaTheta_gate_status"]["rank_tests_allowed_now"] is False,
        "G7_remaining_values_are_exact_frontier": remains["selected_higher_order_or_full_response_matrices"]
        is True
        and remains["selected_A_selected"] is True
        and remains["selected_b_selected"] is True
        and remains["sector_response_matrices_M_u_M_d_M_e_M_nuD"] is True,
        "G8_no_target_or_closure_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_primitiveclass_packet": str(SM_PACKET),
            "sm_primitiveclass_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "PrimitiveClassC1ObservableOrHigherOrderFullResponseImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected primitive quotient class emits a valid current C1 "
                "spectral-observable layer with active shift (1,1), fixed fiber "
                "class {0,1,2}, and shift 0 as computation gauge. Alpha1/dotD is "
                "imported as no longer active. Because YY* is scalar identity in "
                "every sector, this current layer cannot produce flavor splitting. "
                "The remaining live target is selected higher-order/full-response "
                "data: A_selected, b_selected, deltaTheta_C1, and sector response "
                "matrices without observed targets."
            ),
        },
        "checks": checks,
        "primitive_class_C1_observable_packet": observable,
        "higherorder_or_fullresponse_source_emission_packet": emission,
        "promotion_decision": promotion,
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": remains,
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "Current C1 spectral observables are selected but flavor-degenerate; "
                "the next artifact must either emit selected primitive C1 "
                "contractions or show the Weyl-pair routing is sufficient for the "
                "higher-order/full-response target."
            ),
        },
        "guardrails": {
            "primitive_class_C1_observable_emitted": True,
            "current_C1_layer_flavor_closure_claimed": False,
            "selected_values_available": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "PrimitiveClassC1ObservableOrHigherOrderFullResponseImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "frontier_update": packet["frontier_update"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    obs = packet["primitive_class_C1_observable_packet"]
    return f"""# PrimitiveClass C1Observable or HigherOrderFullResponse SourceEmission Import v1

Status: `{cert["status"]}`.

## Result

The selected primitive quotient class emits the current C1 spectral-observable
layer:

```text
active shift = {obs["active_shift"]}
fixed fiber class = {obs["fixed_fiber_quotient_class"]}
computation representative = {obs["computation_representative"]}
YY* scalar = {obs["reference_YYstar_scalar"]}
rank = {obs["reference_rank"]}
|det| = {obs["reference_det_abs"]}
```

Alpha1/dotD is no longer the active blocker.  The current C1 layer is still
flavor-degenerate, because every sector has scalar `YY*`.

## Remaining Target

Selected higher-order/full-response matrices must emit `A_selected`,
`b_selected`, `deltaTheta_C1`, and sector response matrices without observed
targets.

Next artifact: `{packet["next_required_artifact"]}`.
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
