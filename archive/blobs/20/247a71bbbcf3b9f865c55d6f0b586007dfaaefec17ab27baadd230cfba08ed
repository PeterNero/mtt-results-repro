"""Import alpha1 tangent-kernel cross-repo refinement."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
PROTOSPINOR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

PREVIOUS = CERTS / "routec_transport_source_promotion_repair_certificate.json"
LOCAL_ALPHA_GATE = CERTS / "alpha1_sourcestrength_value_gate_reduction_certificate.json"
KERNEL_CERT = (
    PROTOSPINOR
    / "certificates"
    / "selected_alpha1_tangent_or_retarded_overlap_kernel_construct_certificate.json"
)
KERNEL_PACKET = (
    PROTOSPINOR
    / "candidate_data"
    / "selected_alpha1_tangent_or_retarded_overlap_kernel_construct.packet.json"
)
SOURCE_GATE = (
    PROTOSPINOR
    / "certificates"
    / "alpha1_source_strength_normalization_gate_certificate.json"
)

OUTPUT_PACKET = DATA / "alpha1_tangent_kernel_crossrepo_refinement.candidate.json"
OUTPUT_CERT = CERTS / "alpha1_tangent_kernel_crossrepo_refinement_certificate.json"
OUTPUT_NOTE = CORPUS / "Alpha1_TangentKernel_CrossRepo_Refinement_v1.md"


EXPECTED_ACCEPTANCE_FIELDS = {
    "source_identity.selected_emitted",
    "source_strength_coordinate.selected_emitted",
    "normalization_functional.selected_emitted",
    "tangent_equality.residual_l2 <= 1e-12",
    "sector_dotd_equality.selected_emitted",
    "honest_dotd_validator_replay_passes_without_lifted_flags",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    local_alpha_gate = load(LOCAL_ALPHA_GATE)
    kernel_cert = load(KERNEL_CERT)
    kernel_packet = load(KERNEL_PACKET)
    source_gate = load(SOURCE_GATE)

    tangent = kernel_packet["constructed_tangent_kernel"]["tangent"]
    normalization = kernel_packet["constructed_tangent_kernel"][
        "normalization_functional"
    ]
    acceptance = kernel_packet["promotion_acceptance_theorem"]
    retarded = kernel_packet["retarded_overlap_alternative"]

    checks = {
        "E0_previous_frontier_is_alpha1_value_or_same_source": previous[
            "frontier_update"
        ]["current_next"]
        == "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
        "E1_protospinor_kernel_constructed_not_selected": kernel_cert[
            "status"
        ]
        == "SELECTED_ALPHA1_TANGENT_KERNEL_CONSTRUCTED_SELECTION_NORMALIZATION_OPEN"
        and kernel_cert["kernel_constructed"]
        and kernel_cert["alpha1_driver_verified"] is False
        and kernel_cert["closure_claimed"] is False,
        "E2_kernel_formula_and_unit_dual_pinned": tangent["zero_mean"]
        and tangent["selected_now"] is False
        and abs(normalization["N_alpha1_h_ext"] - 1.0) < 1e-15
        and abs(normalization["lambda_alpha1_candidate"] - 1.0) < 1e-15
        and normalization["selected_now"] is False,
        "E3_acceptance_theorem_complete": set(acceptance["if_and_only_if_fields"])
        == EXPECTED_ACCEPTANCE_FIELDS
        and acceptance["selected_value_when_passed"]["alpha1_driver_verified"] is True
        and acceptance["selected_value_when_passed"]["selected_value_emitted"] is True
        and acceptance["current_evaluation"]["selected_value_emitted_now"] is False,
        "E4_retarded_alternative_classified_not_transferable": retarded["classified"]
        and retarded["kernel_pattern_available"]
        and retarded["unit_lag_ratio_closed"]
        and retarded["typed_sm_dotD_kernel_emitted"] is False
        and not any(retarded["open_transfer_checks"].values()),
        "E5_local_stationary_replay_already_closed": previous["status"]
        == "ROUTEC_TRANSPORT_SOURCE_PROMOTION_REPAIR_STATIONARY_REPLAY_CLOSED_ALPHA1_DRIVER_OPEN"
        and previous["theorem"]["proved"]
        and previous["frontier_update"]["current_next"]
        == "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1",
        "E6_protospinor_source_gate_agrees_selection_open": source_gate[
            "status"
        ]
        == "ALPHA1_SOURCE_STRENGTH_NORMALIZATION_GATE_REDUCED_SOURCEIDENTITY_OR_RETARDED_KERNEL_OPEN"
        and source_gate["closure_claimed"] is False,
        "E7_local_alpha_gate_was_value_reduction_not_closure": local_alpha_gate[
            "status"
        ]
        == "ALPHA1_SOURCESTRENGTH_VALUE_GATE_REDUCED_TO_PHIFIN_DERIVATIVE_FILL_OPEN"
        and local_alpha_gate["theorem"]["proved"]
        and local_alpha_gate["guardrails"]["does_not_claim_alpha1_driver"],
    }

    return {
        "packet": "Alpha1_TangentKernel_CrossRepo_Refinement_v1",
        "status": "ALPHA1_TANGENT_KERNEL_IMPORTED_ACCEPTANCE_REFINED_SELECTION_NORMALIZATION_OPEN",
        "inputs": {
            "local_previous": str(PREVIOUS.relative_to(ROOT)),
            "local_alpha_gate": str(LOCAL_ALPHA_GATE.relative_to(ROOT)),
            "protospinor_kernel_certificate": str(KERNEL_CERT),
            "protospinor_kernel_packet": str(KERNEL_PACKET),
            "protospinor_source_gate": str(SOURCE_GATE),
        },
        "theorem": {
            "name": "Alpha1TangentKernelCrossRepoRefinementTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The protospinor branch supplies a finite alpha1 tangent "
                "kernel and exact promotion acceptance criterion.  Imported "
                "into the current transport-repaired Route-C branch, this "
                "moves the frontier from a broad value-or-source search to "
                "a same-source alpha1 normalization packet fill.  The "
                "canonical L2 dual pins lambda_alpha1=1 only as a unit "
                "candidate; it is not yet a selected MTT normalization."
            ),
        },
        "checks": checks,
        "imported_tangent_kernel": {
            "kernel_name": kernel_packet["constructed_tangent_kernel"]["kernel_name"],
            "tangent": tangent,
            "operator_formula": kernel_packet["constructed_tangent_kernel"][
                "operator_formula"
            ],
            "normalization_functional": normalization,
        },
        "acceptance_refinement": {
            "acceptance_theorem": acceptance,
            "stale_fields_from_protospinor_current_evaluation": acceptance[
                "current_evaluation"
            ],
            "current_repo_improvement": {
                "stationary_source_projector_riesz_green_replay_closed": True,
                "source": str(PREVIOUS.relative_to(ROOT)),
                "why_this_matters": (
                    "The protospinor packet was built before the local "
                    "transport repair.  Its current_evaluation is retained "
                    "as provenance, but the current repo has already closed "
                    "the stationary replay layer."
                ),
            },
            "still_required_now": {
                "same_source_selected_normalization_functional": True,
                "source_strength_coordinate_selected_by_branch": True,
                "selected_tangent_equality_h_alpha1_equals_h_ext": True,
                "sector_dotd_equality_as_selected_theorem": True,
                "honest_dotD_replay_without_lifted_flags": True,
                "selected_C1_A_and_b": True,
            },
        },
        "retarded_alternative": retarded,
        "frontier_update": {
            "old_next": previous["frontier_update"]["current_next"],
            "current_next": "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1",
            "why": (
                "The cross-repo import supplies the finite tangent kernel, "
                "unit dual candidate, and acceptance theorem.  The current "
                "transport repair already closes stationary source replay, "
                "so the next object is the selected same-source normalization "
                "packet, not another retarded-pattern analogy."
            ),
        },
        "guardrails": {
            "does_not_claim_alpha1_driver_verified": True,
            "does_not_treat_canonical_L2_dual_as_selected_MTT_normalization": True,
            "does_not_use_diagnostic_lift_as_proof": True,
            "does_not_import_CKM_retarded_kernel_as_SM_dotD_proof": True,
            "does_not_claim_honest_dotD_full_replay": True,
            "does_not_claim_C1_A_or_b_values": True,
            "does_not_claim_full_SM_or_no_knob_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "A finite alpha1 tangent kernel, canonical unit dual, and "
                "exact promotion acceptance theorem are imported into the "
                "current transport-repaired branch."
            ),
            "what_remains": (
                "Fill the selected same-source alpha1 normalization packet "
                "and replay dotD without lifted alpha1-driver flags."
            ),
            "next_required_artifact": "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Alpha1TangentKernelCrossRepoRefinement",
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
    return f"""# Alpha1 Tangent Kernel Cross-Repo Refinement v1

## Result

Status: `{cert["status"]}`

The protospinor repo contains the useful finite alpha1 tangent kernel:
`h_ext`, `dotD_h=(dh) ad(T3)`, and the transported response identity
`D_sel(delta psi)+dotD_h psi=0`.

The canonical L2 dual
`N_alpha1(f)=<f,h_ext>/||h_ext||_L2^2` gives
`N_alpha1(h_ext)=1` and pins `lambda_alpha1=1` as the current unit candidate.
This is still not a selected MTT normalization functional, so the alpha1
driver is not verified.

## Imported Kernel

```json
{json.dumps(packet["imported_tangent_kernel"], indent=2, sort_keys=True)}
```

## Acceptance Refinement

```json
{json.dumps(packet["acceptance_refinement"], indent=2, sort_keys=True)}
```

## Retarded Alternative Boundary

```json
{json.dumps(packet["retarded_alternative"], indent=2, sort_keys=True)}
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
