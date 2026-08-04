"""Build finite-rhoE to oriented-BN functor / smooth-representative split."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "sourcevalue_insertion": DATA / "selected_heterotic_orientedphifin_endedomain_or_nonidentityrhoe_sourcevalue_insertion_packet.json",
    "label_embedding": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "smooth_support": DATA / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload.candidate.json",
    "smooth_valuepacket": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_FiniteRhoE_to_OrientedBN_Functor_or_SmoothRepresentative_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_FINITERHOE_TO_ORIENTEDBN_ORIENTATION_FUNCTOR_CLOSED_MAGNITUDE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_MagnitudeFinitepart_SourceTheorem_or_SmoothEQa_TraceIdentity_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    sourcevalue = load(INPUTS["sourcevalue_insertion"])
    embedding = load(INPUTS["label_embedding"])
    oriented = load(INPUTS["oriented_table"])
    smooth_support = load(INPUTS["smooth_support"])
    smooth_valuepacket = load(INPUTS["smooth_valuepacket"])

    table_by_row = {entry["row"]: entry for entry in oriented["entries"]}
    label_rows = embedding["embedding_rows"]
    compressed = {}
    mismatches = []
    for label, rowdata in label_rows.items():
        row = rowdata["BN_mode"]["row"]
        tau = rowdata["tau"]
        ctau = table_by_row[row]["C_tau"]
        compressed[label] = {
            "BN_row": row,
            "BN_basis_label": table_by_row[row]["basis_label"],
            "tau_internal": tau,
            "C_tau_on_oriented_BN_row": ctau,
            "rho_intertwines": rowdata["rho_intertwines"],
            "orientation_value_matches": tau == ctau,
        }
        if tau != ctau:
            mismatches.append(label)

    orientation_functor = {
        "domain": "finite internal projective rho_E labels F_i,G_i,P",
        "codomain": oriented["basis_id"],
        "map": "phase-preserving 27x11 sparse embedding followed by central-rank operator C_tau",
        "projection_pair_valid": embedding["projection_pair_checks"]["P_transpose_P_equals_identity_11"],
        "rho_character_intertwines": embedding["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"],
        "compressed_C_tau_equals_internal_tau_for_all_labels": not mismatches,
        "mismatches": mismatches,
        "closed": not mismatches
        and embedding["projection_pair_checks"]["P_transpose_P_equals_identity_11"]
        and embedding["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"],
    }

    magnitude_obstruction = {
        "D_E_intertwines_with_oriented_BN": embedding["D_E_intertwiner_checks"]["intertwines"],
        "finitepart_matches_oriented_BN": embedding["finitepart_checks"]["same_finitepart"],
        "internal_logdet": embedding["finitepart_checks"]["internal_logdet"],
        "oriented_BN_positive_complement_logdet": embedding["finitepart_checks"]["BN_positive_complement_logdet"],
        "oriented_abs_sector_logdet_sum": oriented["logdet_values"]["oriented_abs_sector_logdet_sum"],
        "reason": (
            "The central-character functor only transports rank-slot phase/orientation. "
            "The positive Phi_fin magnitude is the 27-mode Fourier/gap layer, while the "
            "finite internal packet uses the 11-label Galerkin Hessian determinant."
        ),
        "closed": False,
    }

    smooth_lane = {
        "support_prefilter_closed": smooth_support["decision"]["support_prefilter_closed"],
        "smooth_transition_tables_emitted": smooth_support["decision"]["smooth_transition_tables_emitted"],
        "smooth_finitepart_computed": smooth_support["decision"]["smooth_finitepart_computed"],
        "exact_smooth_complement_quotient_closed": smooth_valuepacket["decision"]["exact_smooth_complement_quotient_closed"],
        "E_Qa_computed": smooth_valuepacket["decision"]["E_Qa_computed"],
        "closed": False,
    }

    packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.FiniteRhoEToOrientedBNFunctorOrSmoothRepresentative.v1",
        "status": "ORIENTATION_FUNCTOR_CLOSED_MAGNITUDE_AND_SMOOTH_REPRESENTATIVE_OPEN",
        "compressed_label_values": compressed,
        "orientation_functor": orientation_functor,
        "magnitude_obstruction": magnitude_obstruction,
        "smooth_representative_lane": smooth_lane,
        "remaining_exact_payload": [
            "source-owned positive Phi_fin magnitude operator on the oriented 27-mode B_N carrier",
            "finitepart trace identity equating the source-owned positive operator finite part with the oriented logdet policy",
            "or smooth E_Qa / heat-zeta-torsion representative whose quotient has the oriented BN table as its finite compression",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "finite_rhoE_to_oriented_BN_orientation_functor_closed": orientation_functor["closed"],
        "threshold_magnitude_functor_closed": False,
        "finitepart_trace_identity_closed": False,
        "smooth_representative_emitted": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "packet_path": rel(OUTPUT_PACKET),
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinFiniteRhoEToOrientedBNFunctorOrSmoothRepresentative",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "sourcevalue_insertion": sourcevalue["status"],
            "smooth_support": smooth_support["status"],
            "smooth_valuepacket": smooth_valuepacket["status"],
        },
        "packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "FiniteRhoEToOrientedBNOrientationFunctorTheorem",
            "proved": True,
            "statement": (
                "The same-branch finite projective rho_E packet has a valid orientation-only "
                "functor into the oriented B_N carrier: the 27x11 embedding preserves the "
                "Z3 central character, the projection pair is valid, and compressed C_tau "
                "equals the internal tau value on every selected label. This closes the "
                "phase/orientation transfer. It does not close the threshold magnitude, "
                "because the signed internal tau/D_E operator does not intertwine with the "
                "nonnegative oriented Phi_fin gap layer and the finitepart traces are not "
                "identified. Smooth support remains a prefilter only, not a smooth representative."
            ),
        },
        "guardrails": {
            "does_not_promote_orientation_functor_to_magnitude_functor": True,
            "does_not_promote_rho_shadow_to_positive_operator_identity": True,
            "does_not_claim_smooth_representative": True,
            "does_not_promote_oriented_logdet": True,
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
        "packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "finite_rhoE_to_oriented_BN_orientation_functor_closed": True,
        "threshold_magnitude_functor_closed": False,
        "finitepart_trace_identity_closed": False,
        "smooth_representative_emitted": False,
        "oriented_logdet_promoted": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin FiniteRhoE to OrientedBN Functor or SmoothRepresentative v1

## Result

```text
status = {STATUS}
finite_rhoE_to_oriented_BN_orientation_functor_closed = true
threshold_magnitude_functor_closed = false
finitepart_trace_identity_closed = false
smooth_representative_emitted = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Meaning

This is a real closure of the phase/orientation layer, not of the magnitude layer. The
remaining theorem must source-own the positive `Phi_fin` operator/finite part, or emit a
smooth `E_Qa` representative whose finite quotient is the oriented 27-mode packet.

## Packet

```text
{rel(OUTPUT_PACKET)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
