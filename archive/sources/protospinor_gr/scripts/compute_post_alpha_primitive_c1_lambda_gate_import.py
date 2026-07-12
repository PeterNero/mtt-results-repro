from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_dotd_alpha1_driver_bridge.packet.json"
SOURCE = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_primitive_c1_lambda_gate_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_primitive_c1_lambda_gate.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PrimitiveC1_LambdaGate_Import_v1.md"

STATUS = "POST_ALPHA_PRIMITIVE_C1_LAMBDA_GATE_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1"
SECTORS = ["u", "d", "e", "nuD"]
TERMS = [
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def atom_table_ok(source: dict) -> bool:
    table = source["atom_table"]
    if sorted(table) != sorted(SECTORS):
        return False
    return all(
        table[sector]["required_terms"] == TERMS
        and len(table[sector]["missing_terms"]) == len(TERMS)
        and table[sector]["all_terms_emitted"] is False
        for sector in SECTORS
    )


def main() -> None:
    prev = load(PREV)
    source = load(SOURCE)
    decision = source["decision"]
    primitive = source["primitive_status"]
    lambda12 = source["lambda12_status"]

    previous_ready = all(
        [
            prev["theorem"]["proved"] is True,
            prev["status"] == "POST_ALPHA_DOTD_ALPHA1_DRIVER_REPLAY_CLOSED_PRIMITIVE_C1_LAMBDA_OPEN",
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1",
            prev["what_closes_now"]["alpha1_driver_verified"] is True,
            prev["what_closes_now"]["honest_dotD_alpha1_replay"] is True,
        ]
    )
    source_ok = all(
        [
            source["status"] == "U1Y_ROUTEC_PRIMITIVE_C1_LAMBDA12_GATE_POST_ALPHA_OPEN",
            source["closure_claimed"] is False,
            source["target_fitting_used"] is False,
            source["observed_data_used"] is False,
            source["next_required_artifact"] == NEXT,
            source["theorem"]["proved"] is True,
            decision["post_alpha_gate_built"] is True,
            decision["alpha1_and_honest_dotD_prefix_closed"] is True,
            decision["primitive_C1_contractions_closed"] is False,
            decision["A_selected_emitted"] is False,
            decision["b_selected_emitted"] is False,
            decision["lambda_12_closed"] is False,
            decision["lambda_12_computable"] is False,
            decision["Yukawa_or_full_SM_closure"] is False,
            primitive["atom_count"] == 24,
            primitive["missing_atom_count"] == 24,
            primitive["all_primitive_atoms_emitted"] is False,
            primitive["sector_response_matrices_emitted"] is False,
            lambda12["lambda_12_closed"] is False,
            lambda12["lambda_12_computable_from_this_gate"] is False,
            lambda12["electroweak_lane_A_lambda12_closed"] is False,
            atom_table_ok(source),
            all(value is False for value in source["guardrails"].values()),
        ]
    )
    theorem_proved = previous_ready and source_ok
    packet = {
        "theorem": {
            "name": "PostAlphaPrimitiveC1LambdaGateImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "After alpha1/dotD replay closes, the active obstruction is the primitive C1 atom table "
                "or a selected lambda12 spectral table. The selected branch has the post-alpha prefix, "
                "but no selected source emits the 24 required atom matrices for u,d,e,nuD, and lambda12 "
                "is not computable from diagnostic near-hit values."
            ),
        },
        "status": STATUS,
        "atom_table": source["atom_table"],
        "primitive_status": primitive,
        "lambda12_status": lambda12,
        "checks": {
            "previous_ready": previous_ready,
            "source_ok": source_ok,
            "theorem_proved": theorem_proved,
        },
        "what_closes_now": source["what_closes_now"],
        "what_remains_open": source["what_remains_open"],
        "guardrails": {
            "does_not_claim_primitive_C1_contractions": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "does_not_use_diagnostic_lambda12_values": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous": str(PREV), "source": str(SOURCE)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_primitive_c1_lambda_gate",
        "status": STATUS,
        "closure_claimed": False,
        "primitive_C1_contractions_closed": False,
        "missing_atom_count": 24,
        "lambda12_computable": False,
        "checks": {
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha PrimitiveC1 LambdaGate Import v1

## Result

The alpha1/dotD blocker is retired, and the next obstruction is now exactly:

```text
primitive C1 atom matrices: 0 / 24 emitted
A_selected: not emitted
b_selected: not emitted
lambda_12: not computable from this gate
Yukawa/full SM closure: not claimed
```

For each of `u,d,e,nuD`, the selected source must emit:

```text
theta_overlap_variation
left_zero_mode_response
right_zero_mode_response
higgs_zero_mode_response
explicit_vertex
basis_connection
```

Diagnostic lambda near-hits are explicitly not proof.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
