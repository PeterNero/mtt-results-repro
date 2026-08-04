"""Attempt to construct the selected U1/hypercharge local determinant spectrum.

This is the narrowest next move after the dual frontier attack.  The selected
P_perp quotient is already closed; this script tests whether that quotient also
emits the positive determinant spectrum needed for lambda_12.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
NONSM = ROOT.parent / "mtt-nonsm-constants-no-knob"

INPUTS = {
    "dual_frontier": DATA / "dual_attack_local_determinant_or_omega0_source.candidate.json",
    "u1_projector": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "local_interface": NONSM / "certificates" / "selected_local_determinant_computation_interface_certificate.json",
    "determinant_template": NONSM / "certificates" / "selected_local_determinant_spectrum.template.json",
    "qc_circle": NONSM / "certificates" / "selected_qc_circle_gauge_block_equivalence_certificate.json",
    "su2_policy": NONSM / "certificates" / "selected_flat_fp_quotient_normalization_policy_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1_hypercharge_local_determinant_spectrum_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1_hypercharge_local_determinant_spectrum_attempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_Hypercharge_Local_Determinant_Spectrum_Attempt_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    dual = load(INPUTS["dual_frontier"])
    u1 = load(INPUTS["u1_projector"])
    interface = load(INPUTS["local_interface"])
    template = load(INPUTS["determinant_template"])
    qc = load(INPUTS["qc_circle"])
    su2 = load(INPUTS["su2_policy"])

    selected_p_su2 = su2["selected_flat_su2_data"]["selected_p_SU2_for_weak_split"]
    selected_p_qc = qc["selected_values"]["selected_p_Qc_for_weak_split"]
    v1_tilde = dual["lane_A_local_determinant"]["strongest_selected_inputs"]["v1_tilde"]
    target_witness = dual["lane_A_local_determinant"]["diagnostics_not_proof"]["target_witness_lambda_12"]

    # Route A diagnostic: if the P_perp quotient is mistakenly treated as the
    # determinant operator with unit eigenvalues, the finite determinant is zero.
    # This is calculable but rejected: a projector subspace is not a positive
    # local threshold spectrum.
    quotient_identity = {
        "name": "Pperp_quotient_identity_spectrum",
        "candidate_modes": [
            {"eigenvalue": 1.0, "multiplicity": 2.0, "index_weight": 1.0},
        ],
        "p_U1_candidate": 0.0,
        "lambda_12_if_used": 0.0 - selected_p_su2,
        "Delta_G_12_if_used": v1_tilde * (0.0 - selected_p_su2) / (4.0 * math.pi),
        "status": "REJECTED_PROJECTOR_IS_NOT_THRESHOLD_OPERATOR",
        "reason": "P_perp selects the two-dimensional quotient carrier and trace index, but it does not supply positive eigenvalues, boundary conditions, or a local determinant operator.",
    }

    # Route B diagnostic: reuse the Qc central circle determinant for U1.  This
    # double-counts the shared circle that P_perp explicitly quotients away.
    central_circle_reuse = {
        "name": "central_circle_torsion_reuse_for_U1",
        "p_U1_candidate": selected_p_qc,
        "lambda_12_if_used": selected_p_qc - selected_p_su2,
        "Delta_G_12_if_used": v1_tilde * (selected_p_qc - selected_p_su2) / (4.0 * math.pi),
        "status": "REJECTED_DOUBLE_COUNTS_QUOTIENTED_SHARED_CIRCLE",
        "reason": "The selected U1 theorem removes the shared central-circle line before U1 threshold tracing; the Qc circle determinant can support Qc accounting but cannot be imported as the U1 quotient determinant.",
    }

    # Route C: the orthodox source route.  It remains open because the actual
    # section-ring/local operator spectrum is not printed in current sources.
    heterotic_section_ring = {
        "name": "heterotic_or_section_ring_u1_hypercharge_spectrum",
        "required_fields": [
            "positive eigenvalues of the U1/hypercharge threshold operator on V/<s>",
            "multiplicities and hypercharge/index weights",
            "boundary conditions or compact quotient domain",
            "bundle/connection or twisted-module data selecting the operator",
            "proof the spectrum is emitted before electroweak comparison",
        ],
        "status": "OPEN_PRIMARY_ROUTE",
        "reason": "This is the route that could close lambda_12 honestly, but current repositories do not emit the U1/hypercharge operator spectrum.",
    }

    # Hypercharge accounting remains a convention/source map problem.  The Qc
    # block is closed, but Y cannot be completed without the Qa/U1 spectral row.
    hypercharge_gate = {
        "status": "OPEN",
        "closed_part": {
            "Qc_circle_block": selected_p_qc,
            "SU2_block": selected_p_su2,
            "U1_quotient_index": "2/3",
        },
        "missing_part": "selected U1/Qa/hypercharge local determinant spectral row",
        "formula_after_row": "lambda_12 = p_U1_or_Y - p_SU2",
        "target_witness_not_used": target_witness,
    }

    source_checks = {
        "u1_projector_closed": u1["decision"]["selected_U1_SU2_threshold_index_pair_closed"] is True,
        "p_perp_rank_two": u1["projector_theorem"]["checks"]["rank"] == 2,
        "local_determinant_accounting_closed": interface["verdict"]["determinant_accounting_interface_closed"] is True,
        "template_requires_spectra": template["status"] == "OPEN_SELECTED_GAUGE_FACTOR_SPECTRA_REQUIRED",
        "qc_block_closed": qc["verdict"]["qc_selected_for_lambda_12_accounting"] is True,
        "su2_block_closed": su2["verdict"]["su2_selected_for_lambda_12_accounting"] is True,
        "target_fitting_used": False,
    }

    decision = {
        "u1_hypercharge_spectrum_closed": False,
        "lambda_12_closed": False,
        "Pperp_quotient_identity_promoted": False,
        "central_circle_reuse_promoted": False,
        "primary_route": "heterotic_or_section_ring_u1_hypercharge_spectrum",
        "next_required_object": "Selected_U1_Hypercharge_Operator_Spectrum_Source_Packet_v1",
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedU1HyperchargeLocalDeterminantSpectrumAttempt",
        "status": "U1_HYPERCHARGE_SPECTRUM_ATTEMPT_DONE_SELECTED_SPECTRUM_OPEN",
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "source_checks": source_checks,
        "attempts": {
            "quotient_identity": quotient_identity,
            "central_circle_reuse": central_circle_reuse,
            "heterotic_section_ring": heterotic_section_ring,
        },
        "hypercharge_gate": hypercharge_gate,
        "decision": decision,
        "guardrails": [
            "Do not treat P_perp itself as a local determinant operator.",
            "Do not reuse the quotiented central-circle determinant as the U1 quotient determinant.",
            "Do not use the diagnostic target lambda_12 to choose eigenvalues or weights.",
            "Do not compare to electroweak data until the U1/hypercharge spectral row is source-emitted.",
        ],
        "closure_claimed": True,
        "closure_scope": "attempt_and_reduction_only",
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedU1HyperchargeLocalDeterminantSpectrumAttempt",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT_DATA),
        "closed": {
            "Pperp_quotient_carrier": True,
            "Qc_and_SU2_blocks_available": True,
            "bad_spectrum_shortcuts_rejected": True,
            "primary_route_identified": decision["primary_route"],
            "no_target_fit_used": True,
        },
        "open": {
            "selected_U1_hypercharge_positive_spectrum": True,
            "selected_multiplicities_and_index_weights": True,
            "selected_boundary_conditions_or_operator_domain": True,
            "lambda_12": True,
            "measured_electroweak_closure": True,
        },
        "next_required_object": decision["next_required_object"],
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    attempts = candidate["attempts"]
    checks = "\n".join(f"{k} = {v}" for k, v in candidate["source_checks"].items())
    guards = "\n".join(f"- {g}" for g in candidate["guardrails"])
    req = "\n".join(f"- {x}" for x in attempts["heterotic_section_ring"]["required_fields"])
    return f"""# Selected U1 Hypercharge Local Determinant Spectrum Attempt v1

## Result

```text
u1_hypercharge_spectrum_closed = {str(candidate["decision"]["u1_hypercharge_spectrum_closed"]).lower()}
lambda_12_closed = {str(candidate["decision"]["lambda_12_closed"]).lower()}
Pperp_quotient_identity_promoted = {str(candidate["decision"]["Pperp_quotient_identity_promoted"]).lower()}
central_circle_reuse_promoted = {str(candidate["decision"]["central_circle_reuse_promoted"]).lower()}
target_fitting_used = {str(candidate["decision"]["target_fitting_used"]).lower()}
```

The selected `P_perp` quotient closes the U1 physical carrier and the `2/3`
trace index. It does not by itself emit the positive local determinant spectrum
needed for `lambda_12`.

## Attempt 1: Pperp Identity Spectrum

```text
status = {attempts["quotient_identity"]["status"]}
p_U1_candidate = {attempts["quotient_identity"]["p_U1_candidate"]}
lambda_12_if_used = {attempts["quotient_identity"]["lambda_12_if_used"]}
Delta_G_12_if_used = {attempts["quotient_identity"]["Delta_G_12_if_used"]}
reason = {attempts["quotient_identity"]["reason"]}
```

## Attempt 2: Central Circle Reuse

```text
status = {attempts["central_circle_reuse"]["status"]}
p_U1_candidate = {attempts["central_circle_reuse"]["p_U1_candidate"]}
lambda_12_if_used = {attempts["central_circle_reuse"]["lambda_12_if_used"]}
Delta_G_12_if_used = {attempts["central_circle_reuse"]["Delta_G_12_if_used"]}
reason = {attempts["central_circle_reuse"]["reason"]}
```

## Attempt 3: Heterotic or Section-Ring Spectrum

```text
status = {attempts["heterotic_section_ring"]["status"]}
reason = {attempts["heterotic_section_ring"]["reason"]}
```

Required fields:

{req}

## Hypercharge Gate

```text
status = {candidate["hypercharge_gate"]["status"]}
Qc_circle_block = {candidate["hypercharge_gate"]["closed_part"]["Qc_circle_block"]}
SU2_block = {candidate["hypercharge_gate"]["closed_part"]["SU2_block"]}
U1_quotient_index = {candidate["hypercharge_gate"]["closed_part"]["U1_quotient_index"]}
missing_part = {candidate["hypercharge_gate"]["missing_part"]}
formula_after_row = {candidate["hypercharge_gate"]["formula_after_row"]}
target_witness_not_used = {candidate["hypercharge_gate"]["target_witness_not_used"]}
```

## Source Checks

```text
{checks}
```

## Guardrails

{guards}

## Next Required Object

```text
{candidate["decision"]["next_required_object"]}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [str(path) for path in INPUTS.values() if not path.exists()]
    if missing:
        print("Missing inputs:")
        print("\n".join(missing))
        return 1
    candidate, certificate, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, certificate)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"Wrote {OUTPUT_DATA}")
    print(f"Wrote {OUTPUT_CERT}")
    print(f"Wrote {OUTPUT_NOTE}")
    print(certificate["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
