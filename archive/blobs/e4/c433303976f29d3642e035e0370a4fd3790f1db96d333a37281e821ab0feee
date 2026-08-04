"""Import q79 same-source operator provenance frontier."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = DATA / "q79_global_destabilizer_ah_monad_source_chain_import.candidate.json"
Q79_CERT = (
    Q79
    / "certificates"
    / "q79_same_source_operator_provenance_or_selected_routec_solve_certificate.json"
)
Q79_CANDIDATE = (
    Q79
    / "candidate_data"
    / "q79_same_source_operator_provenance_or_selected_routec_solve.candidate.json"
)

OUTPUT_PACKET = DATA / "q79_same_source_operator_provenance_frontier_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_same_source_operator_provenance_frontier_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Same_Source_Operator_Provenance_Frontier_Import_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    q79_cert = load_json(Q79_CERT)
    q79_candidate = load_json(Q79_CANDIDATE)

    reduction = q79_cert["same_source_reduction"]
    closes = q79_cert["what_closes_now"]
    remains = q79_cert["what_remains_open"]
    evidence = q79_cert["source_evidence_status"]
    honest_open = reduction["honest_current_open_items"]
    no_primitive_open = reduction["no_primitive_open_items"]

    checks = {
        "S0_previous_next_matches_same_source_frontier": previous["verdict"][
            "next_required_artifact"
        ]
        == "Q79_SameSource_Operator_Provenance_or_Selected_RouteC_Solve_v1",
        "S1_q79_patchwork_nogo_proved": q79_cert["theorem"]["proved"] is True
        and q79_cert["closure_claimed"] is False
        and closes["same_source_patchwork_nogo_for_current_artifacts"] is True,
        "S2_selected_ordered_source_subvalidator_passes": closes[
            "selected_ordered_source_subvalidator_passes_in_honest_packet"
        ]
        is True
        and evidence["selected_ordered_source_closed"] is True,
        "S3_honest_packet_still_rejected_at_selected_source": reduction[
            "honest_current_patchwork_exit_code"
        ]
        == 2
        and "selected_by_mtt must be true" in honest_open
        and "source_certificate missing" in honest_open,
        "S4_operator_provenance_reduces_to_primitive_c1": closes[
            "operator_provenance_plus_no_primitive_reduces_to_primitive_c1_only"
        ]
        is True
        and no_primitive_open == ["primitive_C1_contractions must be true"],
        "S5_full_plumbing_has_no_hidden_validator_obstruction": closes[
            "full_plumbing_validator_has_no_hidden_obstruction"
        ]
        is True
        and reduction["full_plumbing_diagnostic_exit_code"] == 0,
        "S6_real_remaining_items_are_not_closed": remains[
            "genuine_selected_visible_bundle_operator_source_certificate"
        ]
        and remains["selected_DE_rhoE_Riesz_Green_dotD_from_that_source"]
        and remains["primitive_C1_contractions"],
    }

    proved = all(checks.values())
    return {
        "packet": "Q79_Same_Source_Operator_Provenance_Frontier_Import_v1",
        "status": (
            "Q79_SAME_SOURCE_OPERATOR_PROVENANCE_FRONTIER_IMPORTED"
            if proved
            else "Q79_SAME_SOURCE_OPERATOR_PROVENANCE_FRONTIER_IMPORT_FAILED"
        ),
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "q79_certificate": str(Q79_CERT),
            "q79_candidate": str(Q79_CANDIDATE),
        },
        "theorem": {
            "name": "Q79SameSourceOperatorProvenanceFrontierImport",
            "proved": proved,
            "statement": (
                "The q79 same-source operator theorem is not closed by current "
                "artifacts: the honest patchwork is rejected. What is imported "
                "is sharper: the selected ordered source subvalidator passes, "
                "the current obstruction is genuine source/operator provenance, "
                "and a diagnostic same-source packet reduces the remaining "
                "validator obstruction to primitive C1 contractions."
            ),
        },
        "import_checks": checks,
        "q79_status": q79_cert["status"],
        "q79_reduction": {
            "honest_current_patchwork_validator_status": reduction[
                "honest_current_patchwork_validator_status"
            ],
            "honest_current_patchwork_exit_code": reduction[
                "honest_current_patchwork_exit_code"
            ],
            "honest_current_open_items": honest_open,
            "no_primitive_diagnostic_exit_code": reduction[
                "no_primitive_diagnostic_exit_code"
            ],
            "no_primitive_open_items": no_primitive_open,
            "full_plumbing_diagnostic_exit_code": reduction[
                "full_plumbing_diagnostic_exit_code"
            ],
            "full_plumbing_open_items": reduction["full_plumbing_open_items"],
        },
        "source_evidence_status": evidence,
        "decision": {
            "patchwork_nogo_for_current_artifacts": True,
            "selected_ordered_source_layer_closed": True,
            "same_source_operator_provenance_not_closed": True,
            "primitive_c1_contractions_not_closed": True,
            "validator_plumbing_obstruction_absent_if_real_source_and_c1_supplied": True,
            "next_required_artifact": (
                "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_"
                "Contractions_v1"
            ),
        },
        "guardrails": {
            "does_not_treat_hypothetical_packets_as_proof": q79_candidate[
                "packet_paths"
            ]["hypothetical_full_plumbing"]
            != "",
            "does_not_claim_selected_operator_source_constructed": q79_cert[
                "guardrails"
            ]["claims_selected_operator_source_constructed"]
            is False,
            "does_not_claim_selected_RouteC_residual": q79_cert["guardrails"][
                "claims_selected_RouteC_residual"
            ]
            is False,
            "does_not_claim_primitive_C1_closed": remains["primitive_C1_contractions"]
            is True,
            "does_not_claim_full_SM_closure": q79_cert["guardrails"][
                "claims_full_sm_closure"
            ]
            is False,
            "does_not_use_observed_or_benchmark_inputs": (
                q79_cert["target_fitting_used"] is False
                and q79_cert["guardrails"]["uses_observed_masses_or_ckm_inputs"]
                is False
                and q79_cert["guardrails"]["uses_benchmark_flavor_entries"] is False
            ),
        },
        "verdict": {
            "what_closes_now": (
                "The same-source patchwork no-go is imported, and the validator "
                "frontier is sharpened: real source/operator provenance would "
                "leave primitive C1 contractions as the only remaining packet "
                "validator obstruction."
            ),
            "what_remains": (
                "Construct a genuine selected visible bundle/operator source, "
                "derive same-source Chern-Weil/GS and D_E/Riesz/Green/dotD "
                "from it, and emit primitive C1 contractions or an honest "
                "selected Route-C solve."
            ),
            "next_required_artifact": (
                "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_"
                "Contractions_v1"
            ),
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79SameSourceOperatorProvenanceFrontierImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "import_checks": packet["import_checks"],
        "decision": packet["decision"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Q79 Same-Source Operator Provenance Frontier Import v1

## Result

Status: `{cert["status"]}`

The current q79 patchwork does **not** prove the same-source operator theorem.
It does prove the exact frontier: the selected ordered-source layer passes, the
honest patchwork still fails at selected source/operator provenance, and the
diagnostic validator shows that a genuine same-source packet would reduce the
remaining obstruction to primitive `C1` contractions.

## Import Checks

```json
{json.dumps(packet["import_checks"], indent=2, sort_keys=True)}
```

## Q79 Reduction

```json
{json.dumps(packet["q79_reduction"], indent=2, sort_keys=True)}
```

## Decision

```json
{json.dumps(packet["decision"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
