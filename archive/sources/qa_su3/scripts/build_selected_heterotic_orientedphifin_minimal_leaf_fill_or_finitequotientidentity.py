"""Build the minimal oriented Phi_fin leaf-fill / finite-quotient identity gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "sourcefill_candidate": DATA / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_or_smootheqa_construction.candidate.json",
    "sourcefill_packet": DATA / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_packet.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "selected_finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "internal_finitepart": DATA / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_minimal_leaf_fill_or_finitequotientidentity.candidate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_orientedphifin_minimal_finitequotientidentity_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_minimal_leaf_fill_or_finitequotientidentity_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_MinimalSmoothEQa_LeafFill_or_FiniteQuotientIdentity_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_MINIMAL_LEAFFILL_FINITE_QUOTIENT_PRIMARY_SMOOTH_EQA_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_FiniteQuotientIdentity_SourceTheorem_or_SmoothEQaPayload_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    sourcefill = load(INPUTS["sourcefill_candidate"])
    fill_packet = load(INPUTS["sourcefill_packet"])
    oriented_table = load(INPUTS["oriented_table"])
    finite_packet = load(INPUTS["selected_finite_packet"])
    internal_finitepart = load(INPUTS["internal_finitepart"])

    smooth_route_required = [
        "selected smooth source certificate or good cover/domain",
        "selected connection A or equivalent threshold operator source",
        "curvature F_A and representation action on u(E)-valued one-forms",
        "kernel, quotient, zero-mode, and no-double-count policy at smooth scope",
        "E_Qa matrix or Weitzenbock zero-order block",
        "positive spectrum/heat coefficients and zeta/torsion finite part",
    ]

    finite_route_required = [
        "source certificate that the selected heterotic Qa/SU3 threshold object is the oriented 27-mode B_N quotient",
        "exact finite quotient functor from the selected internal rho_E packet to the oriented B_N threshold table",
        "operator identity E_Qa^or = sign(C_tau) * |PhiFin_DE| on the selected quotient",
        "trace/finitepart policy authorizing the oriented table logdet values as heterotic threshold finite part",
        "kernel and zero-mode subtraction policy, including no shared-circle double count",
        "audit replay proving the identity before comparison with observed constants",
    ]

    smooth_route = {
        "route": "smooth_EQa_payload",
        "rank": 2,
        "currently_buildable_from_repo": False,
        "blocked_by": smooth_route_required,
        "why_secondary": (
            "It asks for several absent smooth objects at once: source cover/domain, "
            "connection, curvature, action, E_Qa, spectrum, and regularization."
        ),
    }

    finite_route = {
        "route": "finite_quotient_identity",
        "rank": 1,
        "currently_buildable_from_repo": False,
        "available_support": {
            "oriented_table_dimension": oriented_table["basis_dimension"],
            "same_basis_commutation": oriented_table["commutation"]["commutator_zero"],
            "PhiFin_positive_count": oriented_table["counts"]["PhiFin_positive_count"],
            "oriented_nonzero_count": oriented_table["counts"]["oriented_nonzero_Ctau_positive_magnitude_count"],
            "finite_internal_packet_selected": finite_packet.get("selected") is True
            and finite_packet["schema"] == "SelectedHeteroticProjectiveRhoEFiniteInternalOperatorPacket.v1",
            "internal_finitepart": internal_finitepart["Delta_selected_internal_exact"],
        },
        "missing_minimal_source_fields": finite_route_required,
        "why_primary": (
            "It reuses already selected finite data and the complete oriented table, and "
            "requires one identity theorem rather than a full smooth connection/spectrum payload."
        ),
    }

    contract = {
        "schema": "SelectedHeterotic.OrientedPhiFin.MinimalFiniteQuotientIdentityContract.v1",
        "primary_route": finite_route,
        "secondary_route": smooth_route,
        "must_not_use": [
            "observed electroweak constants or fitted target values",
            "promotion of log(2008) outside internal rho_E scope",
            "promotion of the 27-mode oriented table without source certificate",
            "smooth E_Qa language unless smooth domain/operator/spectrum leaves are emitted",
        ],
        "minimal_acceptance_tests": {
            "source_certificate_closed": False,
            "quotient_functor_closed": False,
            "operator_identity_closed": False,
            "finitepart_trace_identity_closed": False,
            "kernel_policy_closed": False,
            "audit_replay_closed": False,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "finite_quotient_identity_route_selected_primary": True,
        "smooth_EQa_route_retained_secondary": True,
        "finite_quotient_identity_constructed": False,
        "smooth_EQa_constructed": False,
        "source_emission_closed": False,
        "minimal_contract_built": True,
        "required_finite_identity_leaf_count": len(finite_route_required),
        "closed_finite_identity_leaf_count": 0,
        "required_smooth_leaf_count": len(smooth_route_required),
        "closed_smooth_leaf_count": 0,
        "current_source_nogo": True,
        "mathematical_impossibility_claimed": False,
        "heterotic_threshold_magnitude_promoted": False,
        "next_required_artifact": NEXT,
        "contract_path": rel(OUTPUT_CONTRACT),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinMinimalLeafFillOrFiniteQuotientIdentity",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourcefill": sourcefill["status"],
            "sourcefill_next": sourcefill["decision"]["next_required_artifact"],
        },
        "route_ranking": {
            "primary": finite_route,
            "secondary": smooth_route,
        },
        "contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "theorem": {
            "name": "MinimalLeafFillRouteSelection",
            "proved": True,
            "statement": (
                "Given the current repository state, the finite quotient identity route is "
                "strictly the smaller next gate for oriented Phi_fin threshold closure. "
                "The smooth E_Qa route remains legal but demands an entire smooth source, "
                "operator, and regularization payload. The finite route instead asks for "
                "one same-branch source theorem identifying the already built oriented "
                "27-mode B_N table as the selected heterotic Qa/SU3 threshold quotient, "
                "with a trace finitepart identity and no-double-count policy."
            ),
        },
        "guardrails": {
            "does_not_claim_finite_quotient_identity": True,
            "does_not_claim_smooth_EQa": True,
            "does_not_promote_oriented_values": True,
            "does_not_promote_internal_log2008": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "finite_quotient_identity_route_selected_primary": True,
        "minimal_contract_built": True,
        "finite_quotient_identity_constructed": False,
        "smooth_EQa_constructed": False,
        "source_emission_closed": False,
        "heterotic_threshold_magnitude_promoted": False,
        "current_source_nogo": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin MinimalSmoothEQa LeafFill or FiniteQuotientIdentity v1

## Result

```text
status = {STATUS}
primary_route = finite_quotient_identity
secondary_route = smooth_EQa_payload
finite_quotient_identity_constructed = false
smooth_EQa_constructed = false
heterotic_threshold_magnitude_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Minimal Finite-Quotient Contract

```text
{rel(OUTPUT_CONTRACT)}
```

The contract asks for exactly six leaves:

```json
{json.dumps(finite_route_required, indent=2)}
```

## Why This Is Progress

The previous source-fill artifact proved that the current sources do not close any of the six threshold-identity leaves. This artifact does not close them either; it orders the next attack. The finite quotient identity path is now the primary path because it can reuse the selected finite internal packet and the oriented 27-mode table, while the smooth `E_Qa` path still requires a full smooth operator payload.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
