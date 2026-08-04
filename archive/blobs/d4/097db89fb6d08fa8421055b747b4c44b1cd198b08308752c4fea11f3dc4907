"""Import visible Route-C PhiFin alpha1 derivative fill reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "alpha1_sourcestrength_value_gate_reduction_certificate.json"
VISIBLE_PARTIAL = SM / "candidate_data" / "visible_routec_sourceidentity_or_typedbn_derivative.partial_fill.json"
PHIFIN = SM / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json"
PHIFIN_CERT = SM / "certificates" / "selected_phifin_alpha1_payload_certificate.json"
SPECTRAL = SM / "candidate_data" / "selected_spectral_galerkin_projector_retention_data.candidate.json"
SPECTRAL_CERT = SM / "certificates" / "selected_spectral_galerkin_projector_retention_data_certificate.json"

OUTPUT_PACKET = DATA / "visible_routec_phifin_alpha1_derivative_fill_reduction.candidate.json"
OUTPUT_CERT = CERTS / "visible_routec_phifin_alpha1_derivative_fill_reduction_certificate.json"
OUTPUT_NOTE = CORPUS / "Visible_RouteC_PhiFin_Alpha1_Derivative_Fill_Reduction_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    visible = load(VISIBLE_PARTIAL)
    phifin = load(PHIFIN)
    phifin_cert = load(PHIFIN_CERT)
    spectral = load(SPECTRAL)
    spectral_cert = load(SPECTRAL_CERT)

    phifin_summary = phifin["payload_summary"]
    spectral_layer = spectral["two_layer_projector_audit"]["spectral_projector_layer"]

    checks = {
        "B0_previous_frontier_is_phifin_derivative_fill": previous["frontier_update"][
            "current_next"
        ]
        == "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1",
        "B1_visible_partial_requires_phifin_derivative": visible["next_required_artifact"]
        == "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1"
        and not visible["promotion_result"]["selected_value_emitted"]
        and not visible["promotion_result"]["alpha1_driver_verified"]
        and not visible["partial_fill_result"]["lane_A_phi_fin_alpha1_payload_closed"]
        and not visible["partial_fill_result"][
            "lane_A_same_branch_alpha1_derivative_closed"
        ],
        "B2_phifin_support_present_but_values_unselected": phifin_summary[
            "all_support_shapes_present"
        ]
        and all(phifin_summary["support_candidate_present"].values())
        and not phifin_summary["all_selected_values_emitted"]
        and all(value is False for value in phifin_summary["selected_payload_flags"].values())
        and phifin_cert["closure_claimed"] is False,
        "B3_phifin_reduces_to_spectral_galerkin_retention": phifin[
            "next_required_artifact"
        ]
        == "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1"
        and phifin_cert["primary_next_artifact"] == phifin["next_required_artifact"],
        "B4_spectral_reduction_builds_routec_solve_contract": spectral[
            "status"
        ]
        == "MTT_SELECTED_SPECTRAL_GALERKIN_PROJECTOR_RETENTION_DATA_REDUCED_TO_SELECTED_ROUTEC_GALERKIN_SOLVE"
        and spectral["next_required_artifact"]
        == "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1"
        and spectral_cert["primary_next_artifact"] == spectral["next_required_artifact"],
        "B5_block_projectors_not_confused_with_spectral_projectors": spectral[
            "two_layer_projector_audit"
        ]["layer_separation_honest"]
        and spectral["two_layer_projector_audit"]["block_projector_layer"][
            "block_family_Higgs_projector_retention"
        ]
        and not spectral_layer["coherent_spectral_zero_mode_projector_retention"]
        and not spectral_layer["selected_D_E_dotD_Riesz_Green"],
        "B6_routec_solve_acceptance_contract_has_required_fields": {
            "selected_source_verified true for route residual, D_E, Riesz/Green, and dotD slots",
            "coherent spectral projectors proved, not merely block projectors",
            "zero-mode bases supplied for Q,u,d,L,e,N,H",
            "alpha1_driver_verified true from selected Hessian/C1 equation",
            "primitive C1 contractions become computable from emitted data",
            "no observed masses, CKM/PMNS phases, benchmark matrices, or target residuals used as selectors",
        }.issubset(set(spectral["selected_solve_contract"]["acceptance"])),
    }

    return {
        "packet": "Visible_RouteC_PhiFin_Alpha1_Derivative_Fill_Reduction_v1",
        "status": "VISIBLE_ROUTEC_PHIFIN_ALPHA1_DERIVATIVE_FILL_REDUCED_TO_SELECTED_ROUTEC_GALERKIN_SOLVE_OPEN",
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "visible_partial": str(VISIBLE_PARTIAL),
            "phifin_payload_attempt": str(PHIFIN),
            "phifin_certificate": str(PHIFIN_CERT),
            "spectral_galerkin_retention_reduction": str(SPECTRAL),
            "spectral_certificate": str(SPECTRAL_CERT),
        },
        "theorem": {
            "name": "VisibleRouteCPhiFinAlpha1DerivativeFillReductionTheorem",
            "proved": all(checks.values()),
            "statement": (
                "The visible Route-C Phi_fin alpha1 derivative fill cannot be "
                "promoted from the current Phi_fin support packet: all finite "
                "support shapes exist, but selected payload values are absent. "
                "The missing derivative therefore reduces first to coherent "
                "spectral Galerkin projector retention and then to the selected "
                "Route-C/Strominger Galerkin residual solve contract."
            ),
        },
        "checks": checks,
        "phifin_value_state": {
            "all_support_shapes_present": phifin_summary["all_support_shapes_present"],
            "all_selected_values_emitted": phifin_summary["all_selected_values_emitted"],
            "selected_payload_flags": phifin_summary["selected_payload_flags"],
            "next_required_artifact": phifin["next_required_artifact"],
        },
        "projector_layer_separation": spectral["two_layer_projector_audit"],
        "selected_solve_contract": spectral["selected_solve_contract"],
        "frontier_update": {
            "old_next": previous["frontier_update"]["current_next"],
            "intermediate_next": phifin["next_required_artifact"],
            "current_next": spectral["next_required_artifact"],
            "why": (
                "Block-family/Higgs projector retention is real but insufficient. "
                "The alpha1 derivative needs selected spectral zero-mode projector "
                "retention plus same-source D_E, Riesz/Green, dotD, zero-mode, "
                "and C1 data from an honest Route-C/Strominger Galerkin solve."
            ),
        },
        "guardrails": {
            "does_not_promote_phifin_payload_values": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_honest_dotD_replay": True,
            "does_not_claim_selected_DE_Riesz_Green_dotD": True,
            "does_not_claim_coherent_spectral_projector_retention": True,
            "does_not_claim_C1_response_or_full_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The PhiFin alpha1 derivative fill is reduced to the selected "
                "Route-C/Strominger Galerkin solve contract."
            ),
            "what_remains": (
                "Construct and solve the selected Route-C/Strominger Galerkin "
                "residual system with selected source flags, spectral projector "
                "retention, zero-mode bases, dotD_alpha1, and C1 Hessian data."
            ),
            "next_required_artifact": "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "VisibleRouteCPhiFinAlpha1DerivativeFillReduction",
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
    return f"""# Visible RouteC PhiFin Alpha1 Derivative Fill Reduction v1

## Result

Status: `{cert["status"]}`

The visible Route-C `Phi_fin` alpha1 derivative fill is not selected yet.  The
current PhiFin packet has all support shapes, but no selected payload values.
The real next object is therefore not another coordinate normalization choice;
it is the selected Route-C/Strominger Galerkin residual solve that emits
same-source `D_E`, Riesz/Green, `dotD_alpha1`, zero-mode, spectral-projector,
and C1 data.

## Checks

```json
{json.dumps(packet["checks"], indent=2, sort_keys=True)}
```

## PhiFin Value State

```json
{json.dumps(packet["phifin_value_state"], indent=2, sort_keys=True)}
```

## Projector Layer Separation

```json
{json.dumps(packet["projector_layer_separation"], indent=2, sort_keys=True)}
```

## Selected Solve Contract

```json
{json.dumps(packet["selected_solve_contract"], indent=2, sort_keys=True)}
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
