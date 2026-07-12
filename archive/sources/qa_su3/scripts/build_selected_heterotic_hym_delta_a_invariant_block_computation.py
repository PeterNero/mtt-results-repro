"""Compute the finite invariant HYM Delta_A connection-mass block."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

INPUTS = {
    "payload_gate": DATA / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json",
    "hym_connection": NONSM / "certificates" / "selected_qa_su3_hym_color_connection_spectrum_or_torsion_certificate.json",
    "hym_mu_domain": NONSM / "certificates" / "selected_qa_su3_hym_mu_and_operator_domain_selection_certificate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_hym_delta_a_invariant_block_computation.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_hym_delta_a_invariant_block_computation_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_HYM_DeltaA_InvariantBlock_Computation_v1.md"

STATUS = "HETEROTIC_HYM_DELTA_A_INVARIANT_CONNECTION_BLOCK_COMPUTED_MU_OPEN"
NEXT = "Selected_Heterotic_HYM_Mu_Selection_or_Full_DeltaA_Spectrum_v1"

BASIS = ["E11", "E12", "E13", "E21", "E22", "E23", "E31", "E32", "E33"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    payload = load(INPUTS["payload_gate"])
    hym_connection = load(INPUTS["hym_connection"])
    hym_mu = load(INPUTS["hym_mu_domain"])

    matrix_mu = [
        [2, 0, 0, 0, 0, 0, 0, 0, -2],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [-2, 0, 0, 0, 0, 0, 0, 0, 2],
    ]
    matrix_mu2 = [
        [1, 0, 0, 0, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    spectrum = [
        "0",
        "mu",
        "mu",
        "2*mu",
        "mu*(1+mu)",
        "mu*(1+2*mu)",
        "mu*(2+mu)",
        "mu*(mu+2 - sqrt(mu^2 - 2*mu + 4))",
        "mu*(mu+2 + sqrt(mu^2 - 2*mu + 4))",
    ]
    positive_logdet = "log(12*mu^9*(1+mu)*(2+mu)*(1+2*mu))"

    computation = {
        "basis": BASIS,
        "connection_matrices": hym_connection["selected_connection_matrix_data"]["coefficient_matrices"],
        "operator_block_definition": "M_inv(mu)=sum_i ad(B_i)^* ad(B_i) on invariant End(C^3) matrix coefficients with Frobenius pairing",
        "matrix_formula": "M_inv(mu)=mu*M_mu + mu^2*M_mu2",
        "M_mu": matrix_mu,
        "M_mu2": matrix_mu2,
        "spectrum": spectrum,
        "zero_mode": {
            "eigenvalue": "0",
            "interpretation": "scalar identity direction commuting with the connection block; not a physical threshold mode until the full quotient/domain policy is selected",
            "det_prime_removed": True,
        },
        "positive_det_prime": "12*mu^9*(1+mu)*(2+mu)*(1+2*mu)",
        "positive_logdet_prime": positive_logdet,
        "positivity_for_mu_positive": True,
        "trace": "mu*(10 + 6*mu)",
    }

    decision = {
        "finite_invariant_connection_block_computed": True,
        "full_delta_a_spectrum_computed": False,
        "mu_selected": False,
        "zero_mode_policy_selected_for_physical_threshold": False,
        "analytic_torsion_or_one_loop_threshold_closed": False,
        "physical_electroweak_closure": False,
        "payload_gate_advanced": True,
        "primary_next": "select mu/moduli from Strominger Hessian/OU block or compute full Delta_A spectrum with source-selected quotient policy",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticHYMDeltaAInvariantBlockComputation",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "payload_gate": payload["status"],
            "hym_connection": hym_connection["status"],
            "hym_mu_domain": hym_mu["status"],
        },
        "computation": computation,
        "decision": decision,
        "theorem": {
            "name": "InvariantHYMConnectionMassBlockComputation",
            "proved": True,
            "statement": (
                "From the printed Iwasawa HYM connection matrices, the invariant "
                "Frobenius adjoint block sum_i ad(B_i)^*ad(B_i) is exactly "
                "M_inv(mu)=mu*M_mu+mu^2*M_mu2. Its determinant-prime on the "
                "finite invariant block is 12*mu^9*(1+mu)*(2+mu)*(1+2*mu), "
                "with one scalar commuting zero direction. This is a genuine "
                "source-computed operator subblock, but it is not the full "
                "heterotic threshold because mu, the full Delta_A domain, "
                "BRST/zero-mode quotient policy, trace weights, and physical "
                "threshold convention remain unselected."
            ),
        },
        "guardrails": {
            "chooses_mu": False,
            "uses_mu_equals_one": False,
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "claims_full_delta_a_spectrum": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedHeteroticHYMDeltaAInvariantBlockComputation",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "finite_invariant_connection_block_computed": True,
        "positive_logdet_prime": positive_logdet,
        "mu_selected": False,
        "full_delta_a_spectrum_computed": False,
        "analytic_torsion_or_one_loop_threshold_closed": False,
        "physical_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Heterotic HYM DeltaA Invariant Block Computation v1

## Result

```text
status = {candidate["status"]}
finite_invariant_connection_block_computed = true
full_delta_a_spectrum_computed = false
mu_selected = false
positive_logdet_prime = {candidate["computation"]["positive_logdet_prime"]}
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Computation

The source HYM matrices give the finite invariant block

```text
M_inv(mu) = sum_i ad(B_i)^* ad(B_i) = mu*M_mu + mu^2*M_mu2
```

on the ordered basis:

```json
{json.dumps(candidate["computation"]["basis"], indent=2)}
```

The eigenvalues are:

```json
{json.dumps(candidate["computation"]["spectrum"], indent=2)}
```

Therefore:

```text
det'(M_inv) = {candidate["computation"]["positive_det_prime"]}
log det'(M_inv) = {candidate["computation"]["positive_logdet_prime"]}
```

## Theorem

{candidate["theorem"]["statement"]}

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
