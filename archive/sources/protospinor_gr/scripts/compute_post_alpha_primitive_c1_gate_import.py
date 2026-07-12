from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "alpha1_driver_replay_closure_import.packet.json"
PRIM = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_primitive_c1_gate_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_primitive_c1_gate_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_PrimitiveC1_Gate_Import_v1.md"

STATUS = "POST_ALPHA_PRIMITIVE_C1_LAMBDA12_GATE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    prim = load(PRIM)

    alpha_prefix_closed = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["alpha1_driver_verified"] is True,
            prev["what_closes_now"]["honest_dotD_alpha1_replay"] is True,
            prim["post_alpha_prefix"]["alpha1_driver_verified"] is True,
            prim["post_alpha_prefix"]["du_dalpha1_equals_h_ext"] is True,
            prim["post_alpha_prefix"]["honest_dotD_validator_closed"] is True,
        ]
    )
    primitive_contract_sharp = all(
        [
            prim["theorem"]["proved"] is True,
            prim["decision"]["alpha1_and_honest_dotD_prefix_closed"] is True,
            prim["primitive_status"]["atom_count"] == 24,
            prim["primitive_status"]["missing_atom_count"] == 24,
            prim["primitive_status"]["all_primitive_atoms_emitted"] is False,
            all(not sector["all_terms_emitted"] for sector in prim["atom_table"].values()),
        ]
    )
    lambda12_separate = all(
        [
            prim["what_closes_now"]["lambda12_separated_from_alpha1_and_C1"] is True,
            prim["lambda12_status"]["lambda_12_closed"] is False,
            prim["lambda12_status"]["lambda_12_computable_from_this_gate"] is False,
            prim["guardrails"]["uses_diagnostic_lambda12_values"] is False,
        ]
    )
    theorem_proved = all([alpha_prefix_closed, primitive_contract_sharp, lambda12_separate])

    packet = {
        "theorem": {
            "name": "PostAlphaPrimitiveC1GateImport",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "After alpha1 driver replay, the remaining flavor/SM obstruction is no longer dotD provenance. "
                "The selected branch has oriented functional operator emission, overlap normalization, du/dalpha1=h_ext, "
                "and honest dotD replay. The next required object is the primitive C1 atom table: for each of u,d,e,nuD, "
                "emit theta-overlap variation, left/right/Higgs zero-mode responses, explicit vertex, and basis-connection "
                "terms. Without these 24 atoms, A_selected, b_selected, response matrices, Yukawa magnitudes, and full SM "
                "closure are not computable. Lambda12 remains a separate selected spectral/local-determinant table problem."
            ),
        },
        "imported_status": {"status": STATUS, "primitive_status": prim["status"]},
        "post_alpha_prefix": prim["post_alpha_prefix"],
        "atom_table": prim["atom_table"],
        "primitive_status": prim["primitive_status"],
        "lambda12_status": prim["lambda12_status"],
        "proof_chain": {
            "alpha_prefix_closed": alpha_prefix_closed,
            "primitive_contract_sharp": primitive_contract_sharp,
            "lambda12_separate": lambda12_separate,
            "target_fitting_used": prim["target_fitting_used"],
        },
        "what_closes_now": {
            "post_alpha_prefix_carried_forward": True,
            "primitive_C1_atom_contract_sharpened": True,
            "lambda12_separated_from_alpha1_and_C1": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "all_24_primitive_C1_atoms": True,
            "sector_response_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_magnitudes": True,
            "selected_lambda12_spectral_table": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "does_not_claim_lambda12": True,
            "does_not_use_diagnostic_lambda12_values": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous_alpha1_driver": str(PREV), "primitive_gate": str(PRIM)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_primitive_c1_gate_import",
        "status": STATUS,
        "closure_claimed": False,
        "checks": {
            "theorem_proved": theorem_proved,
            "alpha_prefix_closed": alpha_prefix_closed,
            "primitive_contract_sharp": primitive_contract_sharp,
            "lambda12_separate": lambda12_separate,
            "target_fitting_excluded": prim["target_fitting_used"] is False,
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "next_required_artifact": NEXT,
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha PrimitiveC1 Gate Import v1

## Result

Alpha1 is no longer the blocker. The remaining primitive C1 atom contract is:

```text
sectors = u,d,e,nuD
terms per sector = theta overlap, left response, right response, Higgs response, vertex, basis connection
missing atoms = 24
```

`lambda_12` is separate: it still needs a selected spectral/local-determinant
table, not diagnostic near-hit values.

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
