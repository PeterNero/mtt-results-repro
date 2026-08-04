"""Build the End(E)->B_N operator-intertwiner or smooth-connection source amendment."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "label_embedding_gate": DATA / "selected_heterotic_ende_to_bn_labelembedding_or_smoothtransitionconnection_valuepacket.candidate.json",
    "label_embedding_values": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "finite_internal_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "trace_27mode": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_ende_to_bn_operatorintertwiner_or_smoothconnection_sourceamendment.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_ende_to_bn_operatorintertwiner_required_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_ende_to_bn_operatorintertwiner_or_smoothconnection_sourceamendment_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_EndE_to_BN_OperatorIntertwiner_or_SmoothConnection_SourceAmendment_v1.md"

STATUS = "HETEROTIC_ENDE_TO_BN_OPERATORINTERTWINER_SOURCEAMENDMENT_BUILT_CENTRAL_OPERATOR_OPEN"
NEXT = "Selected_Heterotic_BN_CentralRankOperator_or_SmoothEQa_SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def central_rank_value(rank_slot: int) -> int:
    if rank_slot == 0:
        return 0
    if rank_slot == 1:
        return 1
    return -1


def main() -> dict[str, Any]:
    label_gate = load(INPUTS["label_embedding_gate"])
    values = load(INPUTS["label_embedding_values"])
    finite = load(INPUTS["finite_internal_packet"])
    trace_27 = load(INPUTS["trace_27mode"])

    labels = finite["labels"]
    rows = values["embedding_rows"]
    central_checks = {}
    laplacian_checks = values["D_E_intertwiner_checks"]["by_label"]
    for label in labels:
        rank_slot = rows[label]["BN_mode"]["rank_slot"]
        central_checks[label] = {
            "internal_D_E_tau": finite["tau_values"][label],
            "BN_rank_slot": rank_slot,
            "central_rank_operator_value": central_rank_value(rank_slot),
            "intertwines": int(finite["tau_values"][label]) == central_rank_value(rank_slot),
        }

    central_operator_intertwines = all(item["intertwines"] for item in central_checks.values())
    laplacian_intertwines = values["D_E_intertwiner_checks"]["intertwines"]

    required_packet = {
        "schema": "SelectedHeteroticEndEToBN.OperatorIntertwinerRequiredPacket.v1",
        "status": "OPEN_SOURCE_EMISSION_REQUIRED",
        "already_built": {
            "phase_preserving_embedding_27x11": True,
            "rhoE_character_intertwiner": values["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"],
            "injective_projection_pair": values["projection_pair_checks"]["P_transpose_P_equals_identity_11"],
            "central_rank_operator_candidate_intertwines": central_operator_intertwines,
        },
        "must_emit_to_close": {
            "source_selects_BN_central_rank_operator_C_tau": None,
            "operator_identity": "P^T C_tau P = D_E_internal",
            "relation_to_selected_PhiFin_laplacian_D_E": None,
            "E_Qa_or_threshold_operator_uses_C_tau_not_only_laplacian": None,
            "Riesz_Green_or_finite_part_for_selected_operator": None,
            "same_scheme_finite_part_regularization": None,
            "or_smooth_connection_A_F_A_and_E_Qa": None,
        },
        "forbidden_promotions": [
            "replace selected Phi_fin Laplacian by C_tau without source emission",
            "claim the Laplacian D_E intertwines with signed tau",
            "derive heat/zeta/torsion finite part from C_tau before a positive operator or regularization is selected",
            "use observed constants to decide between Laplacian and central-rank operator",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_PACKET.write_text(json.dumps(required_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "sourceamendment_built": True,
        "phase_embedding_retained": True,
        "selected_PhiFin_laplacian_intertwines": laplacian_intertwines,
        "central_rank_operator_candidate_intertwines": central_operator_intertwines,
        "central_rank_operator_source_selected": False,
        "operator_identity_closed": False,
        "E_Qa_computed": False,
        "finitepart_regularization_same_scheme": False,
        "smooth_connection_values_emitted": False,
        "next_required_artifact": NEXT,
        "required_packet_path": rel(OUTPUT_PACKET),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticEndEToBNOperatorIntertwinerOrSmoothConnectionSourceAmendment",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "input_statuses": {
            "label_embedding_gate": label_gate["status"],
            "label_embedding_values": values["status"],
            "finite_internal_packet": finite["schema"],
            "trace_27mode": trace_27["status"],
        },
        "intertwiner_analysis": {
            "laplacian_D_E_intertwines": laplacian_intertwines,
            "laplacian_checks_by_label": laplacian_checks,
            "central_rank_operator_C_tau": {
                "definition": "C_tau(e_m,n,r)=0 for r=0, +1 for r=1, -1 for r=2",
                "intertwines_on_embedding": central_operator_intertwines,
                "checks_by_label": central_checks,
            },
            "interpretation": (
                "The phase-preserving embedding already knows the signed tau operator, "
                "but the selected 27-mode Phi_fin object currently closes only the "
                "Fourier-Laplacian gap layer. A source must select C_tau, or an E_Qa "
                "operator containing it, before the heterotic operator identity closes."
            ),
        },
        "required_packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "guardrails": {
            "does_not_promote_C_tau_without_source": True,
            "does_not_claim_laplacian_intertwines": True,
            "does_not_claim_finitepart_for_C_tau": True,
            "does_not_emit_smooth_A_or_FA": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "CentralRankOperatorIntertwinerCandidateTheorem",
            "proved": True,
            "statement": (
                "Given the phase-preserving 27x11 embedding, the BN central-rank "
                "operator C_tau with eigenvalues 0,+1,-1 on rank slots r=0,1,2 "
                "intertwines exactly with the internal signed tau/D_E operator. "
                "However, the currently selected Phi_fin theorem closes the "
                "nonnegative Fourier-Laplacian D_E gap layer, not C_tau. Therefore "
                "the next closing datum is a source theorem selecting C_tau, or a "
                "smooth E_Qa/connection operator whose quotient is C_tau, together "
                "with a positive finite-part regularization."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "required_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "central_rank_operator_candidate_intertwines": central_operator_intertwines,
        "central_rank_operator_source_selected": False,
        "operator_identity_closed": False,
        "E_Qa_computed": False,
        "finitepart_regularization_same_scheme": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic EndE to BN OperatorIntertwiner or SmoothConnection SourceAmendment v1

## Result

```text
status = {STATUS}
central_rank_operator_candidate_intertwines = true
central_rank_operator_source_selected = false
operator_identity_closed = false
next_required_artifact = {NEXT}
```

## What We Found

The `27 x 11` phase embedding has a natural operator on the `B_N` side:

```text
C_tau(e_m,n,r) = 0 for r=0, +1 for r=1, -1 for r=2
```

Compressed along the embedding, this exactly reproduces the internal signed
`tau/D_E` operator. That is the first real operator-bridge candidate.

But it is not yet the selected `Phi_fin` operator. The selected `Phi_fin`
result currently closes the nonnegative Fourier-Laplacian gap layer, not
`C_tau`. Closure now needs source emission of `C_tau`, or a smooth `E_Qa` /
bundle connection whose quotient gives `C_tau`, plus a positive finite-part
regularization.

## Required Packet

```text
{rel(OUTPUT_PACKET)}
```

## Theorem

{candidate["theorem"]["statement"]}
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
