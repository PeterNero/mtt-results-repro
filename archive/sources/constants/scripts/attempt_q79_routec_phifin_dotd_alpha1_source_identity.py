"""Attempt q79 Route-C Phi_fin dotD/alpha1 source identity."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PHIFIN_ID = CERTS / "q79_routec_phifin_source_identity_certificate.json"
DOTD_VALUES = CERTS / "selected_phifin_dotd_alpha1_c1_response_emission_attempt_certificate.json"
DOTD_DRIVER = CERTS / "selected_dotd_alpha1_source_and_driver_theorem_attempt_certificate.json"
DOTD_DERIVATIVE = CERTS / "selected_dotd_alpha1_source_derivative_payload_attempt_certificate.json"
RETARDED_ATTEMPT = CERTS / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt_certificate.json"
ANTIUNITARY = CERTS / "antiunitary_dedotd_equivalence_test_certificate.json"
VISIBLE_ORBIT = CERTS / "visible_representative_selection_orbit_certificate.json"
FUNCTIONAL_ORBIT = CERTS / "selected_visible_source_functional_on_orbit_classification_certificate.json"

OUT_PACKET = DATA / "q79_routec_phifin_dotd_alpha1_source_identity_attempt.candidate.json"
OUT_CERT = CERTS / "q79_routec_phifin_dotd_alpha1_source_identity_attempt_certificate.json"
OUT_NOTE = CORPUS / "Q79_Selected_RouteC_PhiFin_dotD_alpha1_SourceIdentity_Attempt_v1.md"

STATUS = "Q79_ROUTEC_PHIFIN_DOTD_ALPHA1_SOURCE_IDENTITY_ATTEMPT_REDUCED_TO_RETARDED_SELECTOR"
NEXT = "Q79_Retarded_Source_Boundary_Selector_or_Selected_Source_Origin_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def local(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_packet() -> dict[str, Any]:
    phifin = load(PHIFIN_ID)
    dotd_values = load(DOTD_VALUES)
    dotd_driver = load(DOTD_DRIVER)
    dotd_derivative = load(DOTD_DERIVATIVE)
    retarded = load(RETARDED_ATTEMPT)
    antiunitary = load(ANTIUNITARY)
    visible_orbit = load(VISIBLE_ORBIT)
    functional_orbit = load(FUNCTIONAL_ORBIT)

    checks = {
        "previous_names_this_artifact": phifin["verdict"]["next_required_artifact"]
        == "Q79_Selected_RouteC_PhiFin_dotD_alpha1_SourceIdentity_v1",
        "DE_gap_layer_closed": phifin["verdict"]["source_identity_gap_layer_closed"] is True,
        "dotD_values_emitted_but_not_selected": dotd_values["closed_prefix"][
            "dotD_alpha1_value_matrices_emitted"
        ]
        is True
        and dotd_values["remaining_gates"]["retarded_overlap_source_vector_b_selected"]
        is True,
        "dotD_driver_theorem_not_proved": dotd_driver["theorem"]["proved"] is False,
        "derivative_payload_not_proved": dotd_derivative["theorem"]["proved"] is False
        and dotd_derivative["derivative_payload_checks"][
            "D6_retarded_overlap_derivative_formula"
        ]
        is False,
        "retarded_attempt_reduces_to_sector_charge": retarded["theorem"]["proved"] is False
        and retarded["transfer_checks"]["K4_selected_sector_charge_or_chirality"]
        is False,
        "antiunitary_operator_equivalence_passes": antiunitary["closed_now"][
            "operator_level_antiunitary_equivalence_for_current_finite_packets"
        ]
        is True
        and antiunitary["closed_now"][
            "dotD_alpha1_and_horizontal_response_slots_match_under_antiunitary_conjugation"
        ]
        is True,
        "visible_orbit_keeps_selector_open": visible_orbit["still_open"][
            "selected_retarded_source_functional_on_orbit"
        ]
        is True,
        "functional_orbit_classifies_next_as_cw_operator": functional_orbit[
            "next_closing_object"
        ]["name"]
        == "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1",
    }
    proved_reduction = all(checks.values())

    reduction = {
        "D_E_gap_layer_status": "closed_selected_source_identity",
        "dotD_value_packet_status": "same_basis_values_present_nonzero_but_source_unselected",
        "antiunitary_status": "q79_q369_dotD_packets_equivalent_not_independent_knobs",
        "missing_source_identity": [
            "selected alpha1 deformation parameter",
            "retarded-overlap derivative formula for Phi_fin at the selected source",
            "sector-by-sector equality from selected derivative to dotD matrices",
            "honest dotD replay without lifted flags",
        ],
        "orientation_status": (
            "q79/q369 is one antiunitary orbit at current finite operator layer; "
            "a non-observed retarded/source selector or selected source origin is "
            "still required before choosing a visible representative."
        ),
    }

    return {
        "packet": "Q79_Selected_RouteC_PhiFin_dotD_alpha1_SourceIdentity_Attempt_v1",
        "status": STATUS if proved_reduction else "Q79_ROUTEC_PHIFIN_DOTD_ALPHA1_SOURCE_IDENTITY_ATTEMPT_FAILED",
        "inputs": {
            "PhiFin_source_identity": local(PHIFIN_ID),
            "dotD_values": local(DOTD_VALUES),
            "dotD_driver_theorem_attempt": local(DOTD_DRIVER),
            "dotD_derivative_payload_attempt": local(DOTD_DERIVATIVE),
            "retarded_kernel_attempt": local(RETARDED_ATTEMPT),
            "antiunitary_DEDotD_equivalence": local(ANTIUNITARY),
            "visible_representative_orbit": local(VISIBLE_ORBIT),
            "visible_source_functional_orbit": local(FUNCTIONAL_ORBIT),
        },
        "source_identity_checks": checks,
        "theorem": {
            "name": "Q79RouteCPhiFindotDAlpha1SourceIdentityReduction",
            "proved": proved_reduction,
            "closure_claimed": False,
            "statement": (
                "The q79 Route-C Phi_fin dotD/alpha1 source-identity gate is "
                "reduced to a retarded/source boundary selector or selected "
                "source origin. The D_E gap/Riesz/Green layer is already "
                "selected-source-derived, the finite dotD matrices are present, "
                "and q79/q369 dotD packets are antiunitarily equivalent. What is "
                "not proved is the selected first-variation source that derives "
                "those dotD matrices from Phi_fin without lifted flags."
            ),
        },
        "reduction": reduction,
        "what_closes_now": {
            "dotD_gate_not_a_DE_or_Green_problem": True,
            "dotD_values_present_but_unselected": True,
            "q79_q369_dotD_not_independent_knobs": True,
            "first_variation_blocker_is_sharp": True,
            "next_selector_object_identified": True,
        },
        "what_remains_open": {
            "selected_alpha1_deformation_parameter": True,
            "retarded_overlap_derivative_formula": True,
            "sector_equality_to_dotD_matrices": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "selected_visible_representative_or_source_origin": True,
            "primitive_C1_overlap_tensors": True,
            "A_selected_and_b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_dotD_alpha1": False,
            "claims_selected_retarded_selector": False,
            "claims_q79_selected_over_q369": False,
            "claims_C1_or_Yukawa_closure": False,
            "uses_lifted_selected_flags": False,
            "uses_observed_or_benchmark_inputs": False,
        },
        "verdict": {
            "dotD_source_identity_closed": False,
            "reduction_proved": proved_reduction,
            "next_required_artifact": NEXT,
            "why_next": (
                "The next object must be a non-observed selected source or "
                "retarded-boundary functional on the antiunitary q79/q369 orbit, "
                "or an equivalent selected alpha1 tangent theorem, that makes "
                "the existing dotD packet theorem-derived."
            ),
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Selected Route-C PhiFin dotD alpha1 SourceIdentity Attempt v1

## Result

Status: `{packet["status"]}`

The `dotD/alpha1` gate did not close, but it is now narrower.  `D_E`,
Riesz, and Green are already source-derived; finite `dotD` values exist; and
q79/q369 are antiunitarily equivalent at this finite operator layer.  The
missing object is the selected first-variation source.

## Reduction

```json
{json.dumps(packet["reduction"], indent=2, sort_keys=True)}
```

## What Closes Now

```json
{json.dumps(packet["what_closes_now"], indent=2, sort_keys=True)}
```

## What Remains Open

```json
{json.dumps(packet["what_remains_open"], indent=2, sort_keys=True)}
```

Next: `{packet["verdict"]["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    if "--write" in sys.argv:
        OUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_CERT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
