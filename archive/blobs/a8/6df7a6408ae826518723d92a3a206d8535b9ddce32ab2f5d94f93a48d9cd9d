"""Attempt Selected_dotD_alpha1_Source_and_Driver_Theorem_v1."""

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

FRONTIER = DATA / "selected_phifin_dotd_alpha1_c1_response_emission_attempt.candidate.json"
GAP_LOCK = DATA / "selected_phifin_s2_gap_layer_honest_replay_lock.candidate.json"
S1_RHOE = DATA / "selected_phifin_s1s2_value_emission.partial_filled.json"
ALPHA1_ATTEMPT = SM / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json"
OPERATOR_IDENTITY = SM / "candidate_data" / "selected_routec_operatorsourceidentity_subpacket.candidate.json"
PRIMITIVE_SELECTION = SM / "candidate_data" / "selected_routec_primitive_source_selection_audit.candidate.json"
DOTD_CERT = SM / "candidate_data" / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"

OUTPUT_PACKET = DATA / "selected_dotd_alpha1_source_and_driver_theorem_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_dotd_alpha1_source_and_driver_theorem_attempt_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_dotD_alpha1_Source_and_Driver_Theorem_Attempt_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    frontier = load_json(FRONTIER)
    gap_lock = load_json(GAP_LOCK)
    s1 = load_json(S1_RHOE)
    alpha1 = load_json(ALPHA1_ATTEMPT)
    operator_identity = load_json(OPERATOR_IDENTITY)
    primitive = load_json(PRIMITIVE_SELECTION)
    dotd = load_json(DOTD_CERT)

    theorem_requirements = {
        "R0_selected_D_E_gap_layer": gap_lock["locked_contract"][
            "Riesz_Green_layer_closes"
        ],
        "R1_selected_projective_rhoE_trace": s1["S1_transition_or_connection_trace"][
            "nonidentity_or_equivalent_connection_trace"
        ]
        and s1["S1_transition_or_connection_trace"]["preserves_s3_gs_and_q79_f_m1"],
        "R2_same_basis_dotD_value_packet": frontier["closed_prefix"][
            "dotD_alpha1_value_matrices_emitted"
        ]
        and frontier["closed_prefix"]["same_basis_as_locked_D_E"],
        "R3_operator_level_projector_retention_for_dotD": False,
        "R4_selected_alpha1_deformation_parameter": False,
        "R5_retarded_overlap_derivative_source": False,
        "R6_honest_dotD_replay_without_lifted_flags": False,
    }

    current_support = {
        "projective_rhoE_support": {
            "source_level_selected": alpha1["projective_gerbe_support"][
                "source_level_promoted"
            ],
            "operator_level_promoted": alpha1["projective_gerbe_support"][
                "operator_level_projective_rhoE_promoted"
            ],
            "selected_twist_verified_in_attempt": alpha1["projective_gerbe_support"][
                "selected_twist_verified_in_attempt"
            ],
        },
        "operator_identity_subpacket": {
            "source_level_support_only": operator_identity["operator_identity_verdict"][
                "source_level_not_operator_level"
            ],
            "subpacket_closed": operator_identity["operator_identity_verdict"][
                "subpacket_closed"
            ],
            "operator_level_projective_rhoE_still_open": operator_identity[
                "operator_identity_verdict"
            ]["operator_level_projective_rhoE_still_open"],
            "selected_visible_operator_source_closed": operator_identity[
                "operator_identity_verdict"
            ]["selected_visible_operator_source_closed"],
        },
        "primitive_source_selection": {
            "active_shift_1_1_forced": primitive["what_closes_now"][
                "active_shift_1_1_forced_by_finite_support"
            ],
            "selected_dotD_source_verified": not primitive["what_remains_open"][
                "selected_dotD_source_verified"
            ],
            "alpha1_driver_verified": not primitive["what_remains_open"][
                "alpha1_driver_verified"
            ],
            "selected_noninvariant_C1_primitive_or_vertex": not primitive[
                "what_remains_open"
            ]["selected_noninvariant_C1_primitive_or_vertex_source"],
        },
        "honest_dotD_replay": {
            "fails_only_by_source_driver_flags": dotd["validation"][
                "honest_validator_fails_only_by_source_driver_flags"
            ],
            "diagnostic_lift_validator_passes": dotd["validation"][
                "diagnostic_lift_validator_passes"
            ],
            "closure_claimed": dotd["closure_claimed"],
        },
    }

    proved = all(theorem_requirements.values())
    return {
        "packet": "Selected_dotD_alpha1_Source_and_Driver_Theorem_Attempt_v1",
        "status": (
            "SELECTED_DOTD_ALPHA1_SOURCE_AND_DRIVER_THEOREM_PROVED"
            if proved
            else "SELECTED_DOTD_ALPHA1_SOURCE_AND_DRIVER_THEOREM_NOT_PROVED_CRITERION_SHARPENED"
        ),
        "inputs": {
            "frontier": str(FRONTIER.relative_to(ROOT)),
            "gap_lock": str(GAP_LOCK.relative_to(ROOT)),
            "S1_rhoE": str(S1_RHOE.relative_to(ROOT)),
            "alpha1_attempt": str(ALPHA1_ATTEMPT),
            "operator_identity": str(OPERATOR_IDENTITY),
            "primitive_selection": str(PRIMITIVE_SELECTION),
            "dotD_certificate": str(DOTD_CERT),
        },
        "theorem": {
            "name": "Selected_dotD_alpha1_Source_and_Driver_Theorem",
            "proved": proved,
            "statement": (
                "The selected Phi_fin source differentiates along the same "
                "q79/F,m=1 alpha1 branch, and this derivative is exactly the "
                "emitted same-basis dotD_alpha1 packet; hence "
                "selected_dotD_source_verified and alpha1_driver_verified are "
                "theorem-derived for all sectors."
            ),
        },
        "requirements": theorem_requirements,
        "current_support": current_support,
        "obstruction": {
            "not_a_shape_problem": True,
            "not_a_gap_problem": True,
            "not_a_projector_cleanliness_problem": True,
            "exact_missing_object": (
                "An operator-level selected alpha1 deformation/retarded-overlap "
                "derivative source, in the locked F3xF3 B_N basis, proving that "
                "the existing dotD matrices are the derivative of the selected "
                "Phi_fin source rather than a diagnostic source-lift."
            ),
            "why_D_E_lock_does_not_imply_dotD": (
                "The D_E theorem selects the zeroth-order finite trace and "
                "gap/Riesz/Green layer. dotD is a first variation along an "
                "alpha1 deformation; selecting the value of D_E does not by "
                "itself select the tangent vector or retarded driver."
            ),
        },
        "sufficient_next_payload": {
            "name": "Selected_dotD_alpha1_Source_Derivative_Payload_v1",
            "must_supply": [
                "operator-level selected projector retention for q79/F,m=1",
                "selected alpha1 deformation parameter from the same source",
                "retarded overlap derivative or equivalent variational formula",
                "sector-by-sector equality to existing dotD_alpha1 matrices",
                "honest dotD validator replay with no lifted source flags",
            ],
        },
        "guardrails": {
            "does_not_promote_dotD_flags": True,
            "does_not_use_diagnostic_lift_as_proof": True,
            "does_not_claim_alpha1_driver": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_Yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The selected dotD/alpha1 gate is reduced to one exact missing "
                "source-derivative payload. All finite matrix shapes, D_E/Green "
                "input, projectors, and diagnostic dotD consistency are already "
                "available."
            ),
            "what_remains": (
                "Supply the selected alpha1 tangent/retarded derivative source "
                "and prove equality to the same-basis dotD matrices."
            ),
            "next_required_artifact": "Selected_dotD_alpha1_Source_Derivative_Payload_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedDotDAlpha1SourceAndDriverTheoremAttempt",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "requirements": packet["requirements"],
        "obstruction": packet["obstruction"],
        "sufficient_next_payload": packet["sufficient_next_payload"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Selected dotD alpha1 Source and Driver Theorem Attempt v1

## Result

Status: `{cert["status"]}`

The theorem is not proved yet.  The current data close the zeroth-order
selected `D_E` gap layer and supply same-basis finite `dotD_alpha1` value
matrices, but they do not select the alpha1 tangent/driver that makes those
matrices theorem-derived.

## Requirements

```json
{json.dumps(packet["requirements"], indent=2, sort_keys=True)}
```

## Obstruction

```json
{json.dumps(packet["obstruction"], indent=2, sort_keys=True)}
```

## Next Payload

```json
{json.dumps(packet["sufficient_next_payload"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
