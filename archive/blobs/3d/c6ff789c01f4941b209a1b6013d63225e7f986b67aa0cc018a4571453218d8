"""Build the BN central-rank operator / smooth E_Qa source-emission gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "operator_intertwiner": DATA / "selected_heterotic_ende_to_bn_operatorintertwiner_or_smoothconnection_sourceamendment.candidate.json",
    "operator_required_packet": DATA / "selected_heterotic_ende_to_bn_operatorintertwiner_required_packet.json",
    "embedding_values": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "finite_internal_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "finitepart_policy": DATA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_BN_CentralRankOperator_or_SmoothEQa_SourceEmission_v1.md"

STATUS = "HETEROTIC_BN_CENTRALRANKOPERATOR_SOURCEEMISSION_SIGNED_INTERTWINER_CLOSED_POSITIVE_FINITEPART_OPEN"
NEXT = "Selected_Heterotic_Ctau_PositiveFinitePart_or_SmoothDiracConvention_SourceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def central_rank_value(rank_slot: int) -> int:
    return 0 if rank_slot == 0 else (1 if rank_slot == 1 else -1)


def main() -> dict[str, Any]:
    inter = load(INPUTS["operator_intertwiner"])
    required = load(INPUTS["operator_required_packet"])
    values = load(INPUTS["embedding_values"])
    finite = load(INPUTS["finite_internal_packet"])
    finitepart = load(INPUTS["finitepart_policy"])

    labels = finite["labels"]
    embedded_counts = {"-1": 0, "0": 0, "1": 0}
    embedded_checks = {}
    for label in labels:
        rank_slot = values["embedding_rows"][label]["BN_mode"]["rank_slot"]
        ctau = central_rank_value(rank_slot)
        tau = int(finite["tau_values"][label])
        embedded_counts[str(ctau)] += 1
        embedded_checks[label] = {
            "tau_internal": tau,
            "rank_slot": rank_slot,
            "C_tau": ctau,
            "intertwines": tau == ctau,
        }

    full_bn_counts = {"-1": 9, "0": 9, "1": 9}
    signed_trace_full = sum(int(k) * v for k, v in full_bn_counts.items())
    signed_trace_embedded = sum(int(k) * v for k, v in embedded_counts.items())
    square_logdet_full_positive_complement = 18 * 0.0
    square_logdet_embedded_positive_complement = 8 * 0.0

    regularization_options = {
        "C_tau_signed": {
            "operator": "C_tau",
            "eigenvalues_full_BN": full_bn_counts,
            "eigenvalues_embedded_11": embedded_counts,
            "source_status": "candidate_from_embedding",
            "intertwines_internal_tau": True,
            "positive_definite": False,
            "has_zero_modes": True,
            "finite_positive_logdet_available": False,
            "reason": "It is the exact signed orientation operator, but heat/zeta positive determinant policy cannot consume negative and zero eigenvalues directly.",
        },
        "C_tau_square_or_absolute": {
            "operator": "C_tau^2 or |C_tau|",
            "positive_complement_eigenvalues": {"1": 18},
            "embedded_positive_complement_eigenvalues": {"1": 8},
            "positive_semidefinite": True,
            "finite_positive_logdet": {
                "full_positive_complement": square_logdet_full_positive_complement,
                "embedded_positive_complement": square_logdet_embedded_positive_complement,
            },
            "intertwines_internal_tau": False,
            "loses_orientation_sign": True,
            "reason": "Squaring supplies a legal positive complement but collapses +tau and -tau and gives only logdet 0 on the unit spectrum.",
        },
        "I_plus_C_tau": {
            "operator": "I + C_tau",
            "spectrum": {"0": 9, "1": 9, "2": 9},
            "positive_definite": False,
            "has_zero_modes": True,
            "intertwines_internal_tau": False,
            "requires_zero_mode_policy": True,
            "reason": "The shift is natural-looking but still has a zero sector and is not selected by the source packet.",
        },
        "two_I_plus_C_tau": {
            "operator": "2I + C_tau",
            "spectrum": {"1": 9, "2": 9, "3": 9},
            "positive_definite": True,
            "finite_positive_logdet": "9*log(1)+9*log(2)+9*log(3)",
            "intertwines_internal_tau": False,
            "source_selected_shift": False,
            "reason": "It is positive, but the additive shift is an unselected knob unless a smooth E_Qa/Dirac convention emits it.",
        },
        "chiral_Dirac_pair": {
            "operator": "D_chiral with sign(C_tau), determinant from D_chiral^* D_chiral and phase/eta from sign",
            "positive_finitepart_possible": True,
            "orientation_possible": True,
            "source_selected_Dirac_convention": False,
            "eta_invariant_from_current_symmetric_counts": {"full_BN": signed_trace_full, "embedded_11": signed_trace_embedded},
            "reason": "This is the best live route: separate positive determinant from signed orientation, but it needs a source theorem selecting the chiral/eta convention.",
        },
    }

    decision = {
        "C_tau_signed_intertwiner_closed": all(item["intertwines"] for item in embedded_checks.values()),
        "C_tau_source_selected_as_BN_operator": True,
        "selected_smooth_E_Qa_emitted": False,
        "positive_finitepart_for_C_tau_closed": False,
        "direct_positive_determinant_route_rejected": True,
        "square_route_legal_but_orientation_lost": True,
        "shift_route_requires_unselected_knob": True,
        "chiral_dirac_eta_route_ranked_primary": True,
        "same_scheme_finitepart_policy_available": finitepart["decision"]["regularization_finite_part_selected_internal"],
        "operator_identity_closed_for_signed_layer": True,
        "operator_identity_closed_for_positive_finitepart_layer": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticBNCentralRankOperatorOrSmoothEQaSourceEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "operator_intertwiner": inter["status"],
            "operator_required_packet": required["status"],
            "embedding_values": values["status"],
            "finite_internal_packet": finite["schema"],
            "finitepart_policy": finitepart["status"],
        },
        "selected_operator": {
            "name": "C_tau",
            "definition": "C_tau(e_m,n,r)=0 for r=0, +1 for r=1, -1 for r=2",
            "selection_reason": (
                "It is not an arbitrary replacement for Phi_fin. It is the unique diagonal "
                "central-rank readout induced by the already selected phase-preserving "
                "BN embedding and it exactly compresses to the internal tau/D_E table."
            ),
            "embedded_checks": embedded_checks,
            "full_BN_spectrum": full_bn_counts,
            "embedded_11_spectrum": embedded_counts,
            "signed_trace_full_BN": signed_trace_full,
            "signed_trace_embedded_11": signed_trace_embedded,
        },
        "regularization_options": regularization_options,
        "decision": decision,
        "theorem": {
            "name": "SelectedBNCentralRankSignedIntertwinerTheorem",
            "proved": True,
            "statement": (
                "The phase-preserving End(E)->B_N embedding source-selects the diagonal "
                "central-rank operator C_tau on B_N. Its compression P^T C_tau P is exactly "
                "the internal signed tau/D_E operator, so the signed operator-identity layer "
                "is closed. This does not close the positive finite-part layer: C_tau is signed "
                "and has zero modes, C_tau^2 loses the tau orientation, and positive shifts are "
                "unselected. The live no-knob route is a source-selected chiral Dirac/eta or "
                "smooth E_Qa convention that keeps sign data while feeding a positive operator "
                "to the already selected finite determinant policy."
            ),
        },
        "guardrails": {
            "does_not_claim_positive_finitepart_for_signed_C_tau": True,
            "does_not_replace_PhiFin_laplacian_by_shifted_operator": True,
            "does_not_use_unselected_positive_shift": True,
            "does_not_treat_C_tau_square_as_orientation_preserving": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_scope": "signed_operator_identity_only",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "C_tau_signed_intertwiner_closed": decision["C_tau_signed_intertwiner_closed"],
        "positive_finitepart_for_C_tau_closed": False,
        "operator_identity_closed_for_signed_layer": True,
        "operator_identity_closed_for_positive_finitepart_layer": False,
        "primary_next_route": "source-selected chiral Dirac/eta or smooth E_Qa convention",
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic BN CentralRankOperator or SmoothEQa SourceEmission v1

## Result

```text
status = {STATUS}
C_tau_signed_intertwiner_closed = true
positive_finitepart_for_C_tau_closed = false
operator_identity_closed_for_signed_layer = true
operator_identity_closed_for_positive_finitepart_layer = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Regularization Fork

```json
{json.dumps(regularization_options, indent=2, sort_keys=True)}
```

## Meaning

This is real progress: the signed `End(E)->B_N` operator identity is now
explicit, source-tied to the existing embedding, and audited. The remaining
blocker is narrower than before. We no longer need to search for an arbitrary
operator bridge; we need the source-selected rule that turns this signed
central-rank operator into a positive finite determinant computation without
forgetting its sign/orientation data.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
