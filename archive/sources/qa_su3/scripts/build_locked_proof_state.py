"""Build the locked Qa/SU3 proof-state certificate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

COMPLEMENT = DATA / "complement_spectrum_or_smooth_operator_source.candidate.json"
SMOOTH = DATA / "smooth_determinant_spectral_table_or_source_operator.candidate.json"
ORBIT = DATA / "central_twist_orbit_democracy_source_or_determinant_operator.candidate.json"
CAxis = DATA / "caxis_orthogonality_source_or_weighted_operator_packet.candidate.json"

OUTPUT_DATA = DATA / "locked_proof_state.candidate.json"
OUTPUT_CERT = CERTS / "locked_proof_state_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Locked_Proof_State_v1.md"


def build() -> tuple[dict[str, object], dict[str, object], str]:
    complement = json.loads(COMPLEMENT.read_text(encoding="utf-8"))
    smooth = json.loads(SMOOTH.read_text(encoding="utf-8"))
    orbit = json.loads(ORBIT.read_text(encoding="utf-8"))
    caxis = json.loads(CAxis.read_text(encoding="utf-8"))

    locked_state = {
        "finite_hessian": {
            "H_sel": [[26, -3, 0], [-3, 10, 0], [0, 0, 8]],
            "G_ret": [["10/251", "3/251", 0], ["3/251", "26/251", 0], [0, 0, "1/8"]],
            "Pi_tw": [0, 0, 1],
            "tau": caxis["sample_non_unit_packet"]["tau"],
            "spectrum": smooth["finite_hessian_determinant"]["eigenvalues_exact"],
            "determinant": 2008,
            "finite_rank_logdet": "log(2008)",
        },
        "closed_results": [
            "typed monad product charges land in P",
            "c-axis twist cancellation and tau table are validated",
            "finite Galerkin H_sel/G_ret/Pi_tw packet is validated",
            "finite c-axis orthogonality is closed under source-selected finite trace weights a=b=p=1",
            "finite projected Hessian determinant is log(2008)",
            "conditional reduced coherent-sector determinant is log(2008)",
        ],
        "conditional_results": {
            "reduced_determinant_promotes_if": complement["reduced_determinant_conditional"]["conditions_needed"],
            "value_if_promoted": "log(2008)",
        },
        "open_gate": {
            "name": "Selected_Qa_SU3_Source_Amendment_Complement_Quotient_or_Smooth_Spectrum_v1",
            "required_one_of": [
                "source theorem that the Qa/SU3 determinant domain is exactly the reduced coherent-sector finite H_sel block, with complement cancellation/quotient and no double counting",
                "same-source smooth Qa/SU3 threshold operator with positive spectrum, multiplicities, index weights, zero-mode policy, and heat/zeta/torsion finite part",
            ],
        },
        "forbidden_promotions": [
            "claiming full Qa/SU3 threshold closure from log(2008) without complement quotient/cancellation",
            "using spectral gaps or first eigenvalue bounds as zeta determinant finite parts",
            "using q79/S3/visible-sector data as direct Qa/SU3 source values",
            "choosing complement spectrum or weights from observed couplings or residuals",
            "double-counting local FP/BRST or gauge quotient determinants",
        ],
    }

    candidate = {
        "candidate": "SelectedQaSU3LockedProofState",
        "status": "QA_SU3_PROOF_STATE_LOCKED_FINITE_REDUCED_DETERMINANT_CONDITIONAL_SMOOTH_SOURCE_OPEN",
        "inputs": {
            "complement_gate": str(COMPLEMENT.relative_to(ROOT)),
            "smooth_gate": str(SMOOTH.relative_to(ROOT)),
            "orbit_gate": str(ORBIT.relative_to(ROOT)),
            "caxis_gate": str(CAxis.relative_to(ROOT)),
        },
        "locked_state": locked_state,
        "decision": {
            "finite_reduced_branch_locked": True,
            "full_Qa_SU3_threshold_closure_now": False,
            "current_source_exhausted": True,
            "next_allowed_artifact": locked_state["open_gate"]["name"],
        },
        "acceptance_rule_for_future_work": [
            "new work must fill one of the open_gate.required_one_of entries",
            "new work must preserve target_fitting_used=false",
            "new work must not weaken any forbidden_promotions guardrail",
            "new work must update verify.py and pass the full audit suite",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": "SelectedQaSU3LockedProofState",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "finite_reduced_branch_locked": True,
            "forbidden_promotions_locked": True,
            "next_allowed_artifact_named": True,
        },
        "what_remains_open": {
            "source_amendment_or_smooth_spectrum": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": locked_state["open_gate"]["name"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, object]) -> str:
    state = candidate["locked_state"]
    closed = "\n".join(f"- {item}" for item in state["closed_results"])
    forbidden = "\n".join(f"- {item}" for item in state["forbidden_promotions"])
    required = "\n".join(f"- {item}" for item in state["open_gate"]["required_one_of"])
    return f"""# Selected Qa/SU3 Locked Proof State v1

## Locked Result

The current branch is locked at:

```text
finite H_sel determinant = 2008
finite-rank logdet = log(2008)
conditional reduced coherent-sector determinant = log(2008)
full smooth Qa/SU3 threshold closure = no
```

## Closed

{closed}

## Still Open

Future work must supply one of:

{required}

## Forbidden Promotions

{forbidden}

## Next Allowed Artifact

```text
{state["open_gate"]["name"]}
```

This lock prevents the finite/reduced determinant from being overpromoted while
preserving the exact path to closure.
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
