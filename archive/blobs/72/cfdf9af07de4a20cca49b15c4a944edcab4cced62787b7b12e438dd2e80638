"""Decide the next Qa/SU3 route after the local A01 repair guardrail."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "a01_repair": DATA / "a01_repair_guardrail_local_recompute.candidate.json",
    "minimal_request": DATA / "minimal_closing_source_data_request.candidate.json",
    "operator_fill": DATA / "color_bundle_operator_packet_fill_attempt.candidate.json",
    "typed_monad_fill": DATA / "typed_monad_data_fill_attempt.candidate.json",
    "repair_options": DATA / "repair_options_external_synthesis.candidate.json",
}

OUTPUT_DATA = DATA / "endomorphism_or_local_system_torsion_decision.candidate.json"
OUTPUT_CERT = CERTS / "endomorphism_or_local_system_torsion_decision_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Endomorphism_or_Local_System_Torsion_Decision_v1.md"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def build() -> tuple[dict[str, object], dict[str, object], str]:
    inputs = {name: load(path) for name, path in INPUTS.items()}
    a01 = inputs["a01_repair"]
    operator_fill = inputs["operator_fill"]
    typed_monad = inputs["typed_monad_fill"]
    repair_options = inputs["repair_options"]

    lanes = [
        {
            "id": "source_certified_A01_repair_B",
            "status": "BLOCKED_SOURCE_CERTIFICATION_MISSING",
            "can_close_now": False,
            "evidence": [
                "Repair B passes the full invariant Maurer-Cartan equations.",
                "The correction changes a printed matrix entry and is not selected by the current source.",
                "No stability/HYM/Bianchi or finite response packet is attached to the repair.",
            ],
            "acceptance_condition": "A source erratum or same-branch derivation selects B2=-E32 and supplies admissibility plus finite D_E/rho_E response.",
        },
        {
            "id": "endomorphism_E_threshold_operator",
            "status": "LIVE_BUT_OPERATOR_LAYER_OPEN",
            "can_close_now": False,
            "evidence": [
                "The color-bundle/operator interface is already typed.",
                "The fill attempt imports domain/Strominger/HYM context but reports missing endomorphism_E, curvature data, trace normalization, and finite heat/spectrum/torsion data.",
                "This lane is mathematically standard for a Weitzenbock or threshold operator, but the current corpus has not selected its matrix blocks.",
            ],
            "acceptance_condition": "A selected Qa/SU3 bundle/sheaf/twist plus explicit endomorphism_E and finite heat/zeta/torsion response.",
        },
        {
            "id": "selected_local_system_torsion",
            "status": "LIVE_AS_FINITE_RESPONSE_EXIT_NOT_SOURCE_FILLED",
            "can_close_now": False,
            "evidence": [
                "The minimal request allows analytic/Reidemeister torsion as the finite response.",
                "q79 finite torsion patterns remain guardrails only, not direct Qa/SU3 proof imports.",
                "No selected Qa/SU3 local system representation rho_E is currently printed or derived.",
            ],
            "acceptance_condition": "A same-branch rho_E/local-system representation, quotient policy, acyclicity or zero-mode policy, and torsion finite part.",
        },
        {
            "id": "projective_gerbe_twisted_module_response",
            "status": "PRIMARY_NEXT_CONSTRUCTIVE_ROUTE_SOURCE_VALUES_OPEN",
            "can_close_now": False,
            "evidence": [
                "The gerbe/twisted-module route solves the literal nonclosed c-axis problem at product typing level.",
                "It keeps ordinary a,b line-bundle charges while canceling opposite c twists in every F_i G_i product.",
                "It still needs selected Deligne/Cech or B-field data, twisted section constants, Freed-Witten/Bianchi checks, projector retention, and D_E/rho_E/torsion response.",
            ],
            "acceptance_condition": "Selected gerbe/local-system packet with twisted multiplication constants and one finite response operator.",
        },
    ]
    decision = {
        "primary_next_lane": "projective_gerbe_twisted_module_response",
        "parallel_fallback_lanes": [
            "endomorphism_E_threshold_operator",
            "selected_local_system_torsion",
        ],
        "retained_as_erratum_candidate_only": "source_certified_A01_repair_B",
        "reason": "The projective gerbe lane is the only lane that already removes a structural obstruction without changing printed matrix entries or importing off-branch torsion data.",
        "next_required_artifact": "Selected_Qa_SU3_Gerbe_Twisted_Local_System_Response_Interface_v1",
    }
    checks = {
        "repair_B_full_MC_integrable": a01["decisions"]["repair_B_full_MC_integrable"],
        "repair_B_source_certified": a01["decisions"]["repair_B_source_certified"],
        "operator_packet_computable_now": operator_fill["fill_result"]["determinant_computable_now"],
        "typed_monad_maps_filled": typed_monad["fill_result"]["typed_maps_filled"],
        "gerbe_route_primary_in_prior_synthesis": repair_options["recommendation"]["primary_next_route"] == "projective_gerbe_twisted_module",
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3EndomorphismOrLocalSystemTorsionDecision",
        "status": "QA_SU3_ENDOMORPHISM_OR_LOCAL_SYSTEM_TORSION_DECISION_BUILT_GERBE_RESPONSE_PRIMARY",
        "input_status": {name: data.get("status", "UNKNOWN") for name, data in inputs.items()},
        "checks": checks,
        "lanes": lanes,
        "decision": decision,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": decision["next_required_artifact"],
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "a01_repair_B_reclassified_as_erratum_candidate": True,
            "endomorphism_E_lane_kept_live_but_open": True,
            "local_system_torsion_lane_kept_live_but_open": True,
            "gerbe_twisted_response_lane_promoted_primary": True,
        },
        "what_remains_open": {
            "selected_gerbe_or_local_system_representation": True,
            "twisted_section_constants": True,
            "endomorphism_E_or_rhoE_blocks": True,
            "finite_heat_zeta_torsion_response": True,
            "qa_su3_packet_closed": False,
        },
        "decision": decision,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Endomorphism or Local System Torsion Decision v1

## Inputs

The local A01 repair guardrail gives one important algebraic fact:

```text
repair B: B1=E13, B2=-E32, B3=E12 passes full Maurer-Cartan.
```

But it is not source-certified. It therefore stays an erratum candidate, not a
proof source.

## Lane Decision

| lane | status | reason |
|---|---|---|
| A01 repair B | blocked | full-MC integrable, but source selection and finite response are absent |
| endomorphism_E threshold operator | live/open | correct operator style, but matrix blocks and finite part are absent |
| selected local-system torsion | live/open | allowed finite response, but no selected Qa/SU3 `rho_E` is present |
| projective gerbe/twisted module response | primary/open | already solves the literal `c` obstruction at typing level |

## Correct Way Forward

Build the selected gerbe/twisted local-system response interface. It must combine

```text
selected Deligne/Cech or B-field class,
ordinary a,b section factors,
c-twisted F_i/G_i modules,
twisted multiplication constants,
Freed-Witten and Bianchi admissibility,
projector and zero-mode policy,
and one finite response: D_E, rho_E, heat/zeta, or torsion.
```

The endomorphism_E and local-system torsion lanes stay live as fallback exits.
They should not be filled by observed constants or off-branch q79 data.

Next required artifact:

```text
{candidate["next_required_artifact"]}
```

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, note


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
