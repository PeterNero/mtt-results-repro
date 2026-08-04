"""Import alpha1 driver closure and post-alpha primitive C1 gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

PREVIOUS = CERTS / "alpha1_tangent_kernel_crossrepo_refinement_certificate.json"
QA_ALPHA = (
    QA
    / "candidate_data"
    / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"
)
QA_ALPHA_CERT = (
    QA
    / "certificates"
    / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap_certificate.json"
)
QA_POSTALPHA = (
    QA
    / "candidate_data"
    / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"
)
QA_POSTALPHA_CERT = (
    QA
    / "certificates"
    / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate_certificate.json"
)

OUTPUT_PACKET = DATA / "alpha1_driver_closure_and_postalpha_gate_import.candidate.json"
OUTPUT_CERT = CERTS / "alpha1_driver_closure_and_postalpha_gate_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Alpha1_Driver_Closure_and_PostAlpha_Gate_Import_v1.md"

STATUS = "ALPHA1_DRIVER_CLOSED_POSTALPHA_PRIMITIVE_C1_LAMBDA12_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    alpha = load(QA_ALPHA)
    alpha_cert = load(QA_ALPHA_CERT)
    post = load(QA_POSTALPHA)
    post_cert = load(QA_POSTALPHA_CERT)

    requirements = alpha["alpha_requirements"]
    value = alpha["promoted_value"]
    replay = alpha["honest_dotd_replay"]
    post_prefix = post["post_alpha_prefix"]
    primitive = post["primitive_status"]
    lambda12 = post["lambda12_status"]

    checks = {
        "F0_previous_frontier_is_same_source_alpha1_packet": previous[
            "frontier_update"
        ]["current_next"]
        == "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1",
        "F1_QA_alpha_driver_replay_audited_closed": alpha["status"]
        == "U1Y_ROUTEC_ALPHA1_DRIVER_REPLAY_CLOSED_PRIMITIVE_C1_LAMBDA_OPEN"
        and alpha["theorem"]["proved"]
        and alpha_cert["alpha1_driver_verified"]
        and alpha_cert["honest_dotD_validator_closed"]
        and alpha_cert["primitive_C1_contractions_closed"] is False
        and alpha_cert["lambda_12_closed"] is False,
        "F2_alpha_requirements_all_selected_or_theorem_derived": all(
            requirements.values()
        ),
        "F3_selected_value_is_exact_unit_h_ext": value[
            "selected_value_emitted_by_this_theorem"
        ]
        is True
        and value["N_alpha1_h_ext"] == 1.0
        and value["lambda_alpha1"] == 1.0
        and value["du_dalpha1"] == "h_ext"
        and value["tangent_residual_l2"] == 0.0,
        "F4_honest_dotD_replay_not_diagnostic_lift": replay[
            "selected_dotD_source_verified"
        ]
        and replay["alpha1_driver_verified"]
        and replay["honest_dotD_validator_closed"]
        and "not diagnostic flags" in replay["why_not_lifted_flags"].lower(),
        "F5_postalpha_gate_audited_open": post["status"]
        == "U1Y_ROUTEC_PRIMITIVE_C1_LAMBDA12_GATE_POST_ALPHA_OPEN"
        and post["theorem"]["proved"]
        and post_cert["alpha1_and_honest_dotD_prefix_closed"]
        and post_cert["primitive_C1_contractions_closed"] is False
        and post_cert["lambda_12_closed"] is False,
        "F6_primitive_atom_contract_is_exact_24_open": primitive["atom_count"] == 24
        and primitive["missing_atom_count"] == 24
        and primitive["all_primitive_atoms_emitted"] is False
        and set(post["atom_table"]) == {"u", "d", "e", "nuD"}
        and all(len(row["missing_terms"]) == 6 for row in post["atom_table"].values()),
        "F7_lambda12_kept_separate_and_unclosed": lambda12["lambda_12_closed"]
        is False
        and lambda12["lambda_12_computable_from_this_gate"] is False
        and lambda12["electroweak_lane_A_lambda12_closed"] is False,
        "F8_guardrails_no_targets_no_full_closure": alpha["target_fitting_used"]
        is False
        and post["target_fitting_used"] is False
        and alpha["guardrails"]["uses_observed_data"] is False
        and post["guardrails"]["uses_observed_data"] is False
        and post["guardrails"]["claims_Yukawa_or_full_SM_closure"] is False,
    }

    return {
        "packet": "Alpha1_Driver_Closure_and_PostAlpha_Gate_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "qa_alpha_driver_replay": str(QA_ALPHA),
            "qa_alpha_driver_replay_certificate": str(QA_ALPHA_CERT),
            "qa_postalpha_gate": str(QA_POSTALPHA),
            "qa_postalpha_gate_certificate": str(QA_POSTALPHA_CERT),
        },
        "theorem": {
            "name": "Alpha1DriverClosureAndPostAlphaGateImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected oriented terminal slot map, same-branch functional "
                "operator emission, and overlap normalization promote the "
                "canonical unit value N_alpha1(h_ext)=1 to the selected alpha1 "
                "source-strength value. Therefore du/dalpha1=h_ext, "
                "selected_dotD_source_verified=true, alpha1_driver_verified=true, "
                "and the finite dotD validator closes without lifted flags. "
                "The post-alpha frontier is not SM closure: it is the 24 selected "
                "primitive C1 atoms or an independent selected lambda12 spectral table."
            ),
        },
        "checks": checks,
        "closed_alpha1_driver": {
            "alpha_requirements": requirements,
            "promoted_value": value,
            "honest_dotd_replay": replay,
            "certificate": alpha_cert,
        },
        "post_alpha_frontier": {
            "prefix": post_prefix,
            "primitive_status": primitive,
            "atom_table": post["atom_table"],
            "lambda12_status": lambda12,
            "certificate": post_cert,
        },
        "frontier_update": {
            "old_next": previous["frontier_update"]["current_next"],
            "current_next": NEXT,
            "why": (
                "The imported QA proof supplies the selected same-source "
                "normalization value and honest dotD replay.  The remaining "
                "frontier is no longer alpha1/dotD provenance; it is primitive "
                "C1 atom emission and, separately, selected lambda12 spectral data."
            ),
        },
        "guardrails": {
            "does_not_claim_primitive_C1_contractions": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_claim_Yukawa_or_full_SM_closure": True,
            "does_not_use_diagnostic_lift_as_proof": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The alpha1 source-strength value, du/dalpha1=h_ext, "
                "alpha1_driver_verified, selected_dotD_source_verified, and "
                "honest dotD replay close by imported same-source oriented-overlap theorem."
            ),
            "what_remains": (
                "Emit 24 selected primitive C1 atoms for u,d,e,nuD or close an "
                "independent selected lambda12 spectral table.  A_selected, b_selected, "
                "Yukawas, and full SM closure remain open."
            ),
            "next_required_artifact": NEXT,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Alpha1DriverClosureAndPostAlphaGateImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "checks": packet["checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Alpha1 Driver Closure and PostAlpha Gate Import v1

## Result

Status: `{cert["status"]}`

The same-source alpha1 normalization gate is closed by importing the audited
U1/Y Route-C oriented-overlap theorem.  The selected value is:

```text
N_alpha1(h_ext) = 1
lambda_alpha1 = 1
du/dalpha1 = h_ext
alpha1_driver_verified = true
selected_dotD_source_verified = true
honest dotD replay = PASS
```

This is not a full SM closure claim.  The post-alpha obstruction is now the
selected primitive C1 atom table or an independent selected `lambda_12` spectral
table.

## Closed Alpha1 Driver

```json
{json.dumps(packet["closed_alpha1_driver"], indent=2, sort_keys=True)}
```

## Post-Alpha Frontier

```json
{json.dumps(packet["post_alpha_frontier"], indent=2, sort_keys=True)}
```

## Frontier Update

```json
{json.dumps(packet["frontier_update"], indent=2, sort_keys=True)}
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
