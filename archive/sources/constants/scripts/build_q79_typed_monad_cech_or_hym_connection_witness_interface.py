"""Build the q79 typed-monad/Cech or HYM connection witness interface."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "q79_routec_selected_source_witness_reduction_import_certificate.json"
Q79_WITNESS = (
    Q79
    / "candidate_data"
    / "q79_routec_selected_source_certificate_or_typed_de_construction"
    / "selected_connection_witness_contract.open.json"
)
Q79_TYPED = (
    Q79
    / "candidate_data"
    / "q79_routec_selected_source_certificate_or_typed_de_construction"
    / "typed_de_witness_contract.open.json"
)
QA_FINITE = CERTS / "selected_qa_su3_finite_selected_connection_source_solve_attempt_certificate.json"
QA_TYPED = CERTS / "selected_qa_su3_typed_monad_data_fill_attempt_certificate.json"
QA_ROUTE = CERTS / "selected_qa_su3_twisted_section_basis_or_operator_exit_construction_certificate.json"

OUTPUT_PACKET = DATA / "q79_typed_monad_cech_or_hym_connection_witness_interface.candidate.json"
OUTPUT_CERT = CERTS / "q79_typed_monad_cech_or_hym_connection_witness_interface_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_Interface_v1.md"

STATUS = "Q79_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_Value_Fill_Attempt_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def q79_rel(path: Path) -> str:
    try:
        return path.relative_to(Q79).as_posix()
    except ValueError:
        return str(path)


def local_rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def build_witness_payload_schema(typed: dict[str, Any]) -> dict[str, Any]:
    return {
        "route_A_honest_selected_routec_source_certificate": {
            "must_supply": [
                "source.selected_by_mtt = true",
                "source.fixture_only = false",
                "source.source_certificate points to this or stronger witness",
                "background.charge_sector_only = false",
                "background.visible_sm_bundle_model_selected = true",
                "background.matter_operator_source_constructed = true",
                "operator_source.selected_D_E_constructed = true",
                "operator_source.selected_dotD_constructed = true",
                "operator_source.selected_riesz_green_constructed = true",
                "operator_source.projector_retention_selected = true",
            ],
            "must_pass": [
                "validate_iwasawa_route_c_residuals.py",
                "validate_iwasawa_selected_source_promotion.py",
                "validate_selected_hym_operator_source.py",
            ],
        },
        "route_B_typed_monad_cech_de_witness": {
            "must_supply": [
                "typed f_i and g_i sections in declared line-bundle spaces",
                "Cech transitions and cocycle data",
                "machine-checkable g o f = 0",
                "exactness or controlled torsion-free substitute",
                "selected Hermitian metric and gauge fixing",
                "integrability F^(0,2)=0",
                "finite basis B_N and D_E action on B_N",
                "Riesz gap, reduced Green, and dotD alpha1 response packets",
            ],
            "then_compute": typed.get("then_compute", []),
            "must_pass": typed.get("validator_targets_after_witness", []),
        },
        "route_C_direct_selected_hym_connection": {
            "must_supply": [
                "selected stable visible SM bundle or sheaf model",
                "selected Gauduchon/balanced metric",
                "explicit HYM or Strominger connection coefficients",
                "gauge-fixing condition",
                "F^(0,2)=0 residual bound",
                "Lambda F = lambda Id residual bound",
                "Bianchi/Green-Schwarz residual bound",
                "finite rho_E, D_E, Riesz, Green, dotD, and projector packets",
            ],
            "must_pass": typed.get("validator_targets_after_witness", []),
        },
    }


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    witness = load(Q79_WITNESS)
    typed = load(Q79_TYPED)
    finite = load(QA_FINITE)
    typed_attempt = load(QA_TYPED)
    route = load(QA_ROUTE)

    payload_schema = build_witness_payload_schema(typed)
    checks = {
        "R0_previous_next_is_q79_witness": previous["verdict"]["next_required_artifact"]
        == "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1",
        "R1_q79_witness_contract_open": witness["status"]
        == "OPEN_SELECTED_CONNECTION_WITNESS_REQUIRED",
        "R2_q79_typed_contract_open": typed["status"]
        == "OPEN_TYPED_DE_OR_SELECTED_HYM_CONNECTION_REQUIRED"
        and typed["currently_computable"] is False,
        "R3_exact_three_route_payload_schema": set(payload_schema)
        == {
            "route_A_honest_selected_routec_source_certificate",
            "route_B_typed_monad_cech_de_witness",
            "route_C_direct_selected_hym_connection",
        },
        "R4_existing_finite_connection_attempt_blocks_on_source": finite["gate_result"][
            "selected_connection_source_solved"
        ]
        is False
        and finite["gate_result"]["next_step_is_new_selected_operator_source_packet"] is True,
        "R5_existing_typed_monad_attempt_blocks_on_typed_maps": typed_attempt[
            "fill_result"
        ]["typed_maps_filled"]
        is False
        and typed_attempt["fill_result"]["de_operator_packet_filled"] is False,
        "R6_routec_is_shortest_non_circular_route_but_values_open": route[
            "decision"
        ]["primary_next_artifact"]
        == "Selected_Qa_SU3_Finite_Selected_Connection_Solve_Packet_v1"
        and route["live_routes"]["finite_selected_connection_solve_route_c"][
            "contract_available"
        ]
        is True,
        "R7_forbidden_shortcuts_preserved": all(
            shortcut in witness["forbidden_shortcuts"]
            for shortcut in [
                "selected-flags-only diagnostic promoted as proof",
                "abstract Li-Yau existence promoted to finite matrices",
                "observed masses, CKM angles, or benchmark Yukawa entries",
                "charge-sector Fu-Yau data treated as visible matter operator source",
            ]
        ),
    }
    proved = all(checks.values())

    return {
        "packet": "Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_Interface_v1",
        "status": STATUS if proved else "Q79_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_INTERFACE_FAILED",
        "inputs": {
            "previous": local_rel(PREVIOUS),
            "q79_selected_connection_witness_contract": q79_rel(Q79_WITNESS),
            "q79_typed_de_witness_contract": q79_rel(Q79_TYPED),
            "qa_finite_connection_source_attempt": local_rel(QA_FINITE),
            "qa_typed_monad_fill_attempt": local_rel(QA_TYPED),
            "qa_route_selection": local_rel(QA_ROUTE),
        },
        "interface_checks": checks,
        "theorem": {
            "name": "Q79TypedMonadCechOrHYMConnectionWitnessInterfaceTheorem",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "The selected q79 witness target has an executable acceptance "
                "interface with exactly three honest routes: a passing selected "
                "Route-C source certificate, typed monad/Cech D_E data, or a "
                "direct selected HYM/Strominger connection. Existing finite and "
                "typed-monad attempts remain blocked at source values, so this "
                "artifact defines the next value-fill problem without claiming "
                "selected matrices or SM closure."
            ),
        },
        "witness_payload_schema": payload_schema,
        "validator_order_after_value_fill": [
            "validate_iwasawa_route_c_residuals.py",
            "validate_iwasawa_de_action.py",
            "validate_iwasawa_riesz_gap.py",
            "validate_iwasawa_reduced_green.py",
            "validate_iwasawa_dotd_response.py",
            "validate_iwasawa_selected_source_promotion.py",
            "validate_selected_hym_operator_source.py",
        ],
        "existing_attempts": {
            "finite_connection_source_solve": {
                "status": finite["status"],
                "selected_connection_source_solved": finite["gate_result"][
                    "selected_connection_source_solved"
                ],
                "all_current_non_source_blockers_reduced": finite["gate_result"][
                    "all_current_non_source_blockers_reduced"
                ],
            },
            "typed_monad_data_fill": {
                "status": typed_attempt["status"],
                "typed_maps_filled": typed_attempt["fill_result"]["typed_maps_filled"],
                "de_operator_packet_filled": typed_attempt["fill_result"][
                    "de_operator_packet_filled"
                ],
                "rhoE_packet_filled": typed_attempt["fill_result"]["rhoE_packet_filled"],
            },
        },
        "what_closes_now": {
            "q79_witness_acceptance_interface": True,
            "route_A_B_C_payloads_named": True,
            "validator_order_named": True,
            "diagnostic_shortcuts_forbidden": True,
            "existing_attempts_aligned_to_same_source_gap": True,
        },
        "what_remains_open": {
            "typed_f_g_maps_or_direct_connection_coefficients": True,
            "selected_visible_sm_bundle_or_sheaf_model": True,
            "finite_rhoE_transition_data": True,
            "honest_routec_residual_packet": True,
            "honest_DE_Riesz_Green_dotD_packets": True,
            "same_source_ChernWeil_GS_row": True,
            "all_24_primitive_C1_3x3_matrices": True,
            "selected_C1_response_matrices": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_selected_connection_values": False,
            "claims_typed_monad_maps_filled": False,
            "claims_honest_routec_source_certificate": False,
            "claims_DE_Riesz_Green_dotD_packets": False,
            "claims_C1_matrices": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "next_required_artifact": NEXT,
            "best_next_compute": (
                "Fill the value packet for one route, preferably Route C direct "
                "selected HYM/Strominger connection or typed monad/Cech maps if "
                "the actual f,g sections can be recovered."
            ),
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Typed Monad/Cech or HYM Connection Witness Interface v1

## Result

Status: `{packet["status"]}`

This builds the executable acceptance interface for
`Q79_Typed_Monad_Cech_or_HYM_Connection_Witness_v1`. It does not fill the
witness values. It defines what would count as a proof-source payload and keeps
the diagnostic shortcuts forbidden.

## Interface Checks

```json
{json.dumps(packet["interface_checks"], indent=2, sort_keys=True)}
```

## Witness Payload Schema

```json
{json.dumps(packet["witness_payload_schema"], indent=2, sort_keys=True)}
```

## Existing Attempts

```json
{json.dumps(packet["existing_attempts"], indent=2, sort_keys=True)}
```

## What Remains Open

```json
{json.dumps(packet["what_remains_open"], indent=2, sort_keys=True)}
```

Next required artifact: `{packet["verdict"]["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
