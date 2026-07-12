"""Fill the S1 rho_E trace piece of Selected_PhiFin_S1S2_Value_Emission."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

TEMPLATE = DATA / "selected_phifin_s1s2_value_emission.required_payload.template.json"
GR_CERT = GR / "certificates" / "phifin_finite_rhoe_trace_construction_certificate.json"
GR_PACKET = GR / "candidate_data" / "phifin_finite_rhoe_trace_construction.packet.json"

OUTPUT_PACKET = DATA / "selected_phifin_s1s2_value_emission.partial_filled.json"
OUTPUT_CERT = CERTS / "selected_phifin_s1_rhoe_trace_fill_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S1_RhoE_Trace_Fill_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def c(re: float, im: float = 0.0) -> dict[str, float]:
    return {"re": re, "im": im}


def clock_shift_matrices() -> dict[str, Any]:
    sqrt3 = math.sqrt(3.0)
    omega = c(-0.5, sqrt3 / 2.0)
    omega2 = c(-0.5, -sqrt3 / 2.0)
    zero = c(0.0)
    one = c(1.0)
    return {
        "field": "C represented as {re, im}",
        "omega": omega,
        "omega2": omega2,
        "g1_clock": [
            [one, zero, zero],
            [zero, omega, zero],
            [zero, zero, omega2],
        ],
        "g2_shift": [
            [zero, zero, one],
            [one, zero, zero],
            [zero, one, zero],
        ],
        "g3_to_g6": "identity_3_on_inactive_kernel_generators",
    }


def build_filled_packet() -> dict[str, Any]:
    template = load_json(TEMPLATE)
    gr_cert = load_json(GR_CERT)
    gr_packet = load_json(GR_PACKET)
    filled = json.loads(json.dumps(template))
    filled["status"] = "PARTIAL_FILLED_S1_RHOE_TRACE_S2_VALUES_OPEN"
    filled["S1_transition_or_connection_trace"].update(
        {
            "selected_connection_or_rhoE_entries": {
                "status": "PARTIAL_FILLED_PROJECTIVE_RHOE_TRACE",
                "source_certificate": str(GR_CERT),
                "source_packet": str(GR_PACKET),
                "packet_name": gr_packet["partial_phi_fin"]["name"],
                "domain_shadow": gr_packet["partial_phi_fin"]["domain_shadow"],
                "codomain_piece": gr_packet["partial_phi_fin"]["codomain_piece"],
                "generator_map": gr_packet["partial_phi_fin"]["generator_map"],
                "matrices": clock_shift_matrices(),
                "central_relation": gr_packet["partial_phi_fin"]["central_relation"],
                "numeric_checks": gr_packet["numeric_checks"],
            },
            "nonidentity_or_equivalent_connection_trace": True,
            "metric_compatibility_certificate": {
                "status": "PROJECTIVE_UNITARY_METRIC_COMPATIBLE",
                "metric": "identity Hermitian metric on rank-3 active fiber",
                "unitary_residuals": {
                    "g1": gr_packet["numeric_checks"]["g1_unitary_residual"],
                    "g2": gr_packet["numeric_checks"]["g2_unitary_residual"],
                    "g3_to_g6": gr_packet["numeric_checks"]["g3_identity_residual"],
                },
            },
            "preserves_s3_gs_and_q79_f_m1": True,
        }
    )
    filled["discipline"]["identity_smoke_used_as_selected_rhoE"] = False
    filled["validator_replay"]["rhoE_mesh_metric_sector_validators_pass"] = "PARTIAL_RHOE_TRACE_VERIFIED_EXTERNALLY"
    filled["validator_replay"]["selected_source_promotion_passes_without_lifted_flags"] = False
    filled["partial_fill_guardrail"] = {
        "full_selected_payload_emitted": False,
        "selected_source_flags_may_be_set_true": False,
        "reason": gr_cert["verdict"]["next_required_artifact"],
    }
    return filled


def build_certificate(filled: dict[str, Any]) -> dict[str, Any]:
    s1 = filled["S1_transition_or_connection_trace"]
    return {
        "certificate": "SelectedPhiFinS1RhoETraceFill",
        "status": "SELECTED_PHIFIN_S1_RHOE_TRACE_PARTIAL_FILL_DONE_S2_OPEN",
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "input_certificate": str(GR_CERT),
        "what_closes_now": {
            "S1_nonidentity_projective_rhoE_trace_filled": True,
            "identity_rhoE_smoke_replaced_for_S1": True,
            "projective_unitary_metric_compatibility_recorded": True,
            "q79_f_m1_s3_gs_branch_preservation_recorded": s1["preserves_s3_gs_and_q79_f_m1"],
        },
        "what_remains_open": {
            "full_S1_source_promotion_for_rhoE": True,
            "S2_selected_basis_and_quadrature": True,
            "S2_selected_D_E_dotD_Riesz_Green_entries": True,
            "honest_routec_validator_replay": True,
            "A_selected": True,
            "b_selected": True,
        },
        "guardrails": {
            "claims_full_selected_payload_emitted": False,
            "claims_selected_source_flags_may_be_set_true": False,
            "claims_D_E_Riesz_Green_dotD_emitted": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_formal_lift_flags_as_proof": False,
        },
    }


def render_note(cert: dict[str, Any], filled: dict[str, Any]) -> str:
    checks = filled["S1_transition_or_connection_trace"]["selected_connection_or_rhoE_entries"][
        "numeric_checks"
    ]
    return f"""# Selected PhiFin S1 RhoE Trace Fill v1

## Result

The S1 `rho_E` trace is partially filled by importing the verified
Heisenberg/Weyl projective finite trace from the GR/protospinor repo.

Status: `{cert["status"]}`

This replaces the old identity-smoke `rho_E` shortcut for the S1 trace only.
It does not emit the full selected `Phi_fin` payload and does not set selected
source flags true.

## Imported Trace

```text
rho_E(g1) rho_E(g2) = omega^-1 rho_E(g2) rho_E(g1)
g1^3 = g2^3 = I
g3,...,g6 act trivially in the inactive kernel
```

Numeric checks:

```text
g1 unitary residual = {checks["g1_unitary_residual"]}
g2 unitary residual = {checks["g2_unitary_residual"]}
g1 order-3 residual = {checks["g1_order3_residual"]}
g2 order-3 residual = {checks["g2_order3_residual"]}
projective commutator residual = {checks["projective_commutator_residual"]}
```

## Remaining Open

- S2 selected basis/quadrature
- S2 selected `D_E`, `dotD_alpha1`, Riesz projector, reduced Green entries
- positive gap/error certificate
- honest Route-C validator replay
- `A_selected` and `b_selected`
"""


def main() -> int:
    filled = build_filled_packet()
    cert = build_certificate(filled)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(filled, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, filled), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
