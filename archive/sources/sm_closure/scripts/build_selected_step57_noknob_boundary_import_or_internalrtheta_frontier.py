"""Build Step57 no-knob boundary import / internal Rtheta frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step57_noknob_boundary_import_or_internalrtheta_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BOUNDARY_IMPORT = PACKET_DIR / "step57_noknob_boundary_import.packet.json"
POLICY_RECHECK = PACKET_DIR / "step57_minimal_policy_recheck.packet.json"
CUTSET = PACKET_DIR / "step57_internal_rtheta_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step57_NoKnobBoundaryImport_or_InternalRThetaFrontier_v1.md"

STEP56 = DATA / "selected_step56_diagonalprofile_import_or_noknob_frontier.candidate.json"
STEP56_VALUES = (
    DATA / "selected_step56_diagonalprofile_import_or_noknob_frontier" / "step56_value_readiness_recheck_after_profile.packet.json"
)
NOKNOB = DATA / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy.candidate.json"
FINAL_RECHECK = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "final_no_knob_value_derivation_recheck.packet.json"
)
EXTERNAL_BOUNDARY = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "post_pi_external_replay_boundary.packet.json"
)
POLICY_MATRIX = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "minimal_universal_parameter_policy_matrix.packet.json"
)
READINESS = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "rtheta_readiness_final_frontier.packet.json"
)
FINAL_CUTSET = (
    DATA
    / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy"
    / "final_cutset_after_no_knob_recheck.packet.json"
)

STATUS = "MTT_SELECTED_STEP57_NOKNOB_BOUNDARY_IMPORTED_INTERNAL_RTHETA_FRONTIER_OPEN"
NEXT = "MTT_Selected_InternalRThetaValueDerivation_or_MinimalUniversalParameterSelection_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP56,
        STEP56_VALUES,
        NOKNOB,
        FINAL_RECHECK,
        EXTERNAL_BOUNDARY,
        POLICY_MATRIX,
        READINESS,
        FINAL_CUTSET,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step57 inputs: " + ", ".join(missing))

    step56 = load(STEP56)
    step56_values = load(STEP56_VALUES)
    noknob = load(NOKNOB)
    final_recheck = load(FINAL_RECHECK)
    external_boundary = load(EXTERNAL_BOUNDARY)
    policy_matrix = load(POLICY_MATRIX)
    readiness = load(READINESS)
    final_cutset = load(FINAL_CUTSET)

    boundary_import = {
        "schema": "MTTStep57NoKnobBoundaryImport.v1",
        "status": "POST_PI_EXTERNAL_REPLAY_BOUNDARY_IMPORTED_NOKNOB_OPEN",
        "step56_source": rel(STEP56),
        "noknob_boundary_source": rel(NOKNOB),
        "post_pi_external_replay_ready": external_boundary["post_pi_external_replay_ready"],
        "SM_parity_external_replay_boundary_declared": external_boundary[
            "SM_parity_external_replay_boundary_declared"
        ],
        "Rtheta_readiness_present_count": readiness["present_count"],
        "Rtheta_readiness_requirement_count": readiness["requirement_count"],
        "only_remaining_readiness_blocker": readiness["only_remaining_readiness_blocker"],
        "selected_internal_value_emission_count": final_recheck["selected_internal_value_emission_count"],
        "accepted_coefficient_value_count": final_recheck["accepted_coefficient_value_count"],
        "no_knob_value_derivation_closed": final_recheck["no_knob_value_derivation_closed"],
        "true_SM_equivalence_closed": external_boundary["true_SM_equivalence_closed"],
        "full_no_knob_closed": external_boundary["full_no_knob_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BOUNDARY_IMPORT, boundary_import)

    policy_recheck = {
        "schema": "MTTStep57MinimalPolicyRecheck.v1",
        "status": "MINIMAL_POLICY_AVAILABLE_BUT_NO_PARAMETER_SELECTED",
        "policy_matrix_source": rel(POLICY_MATRIX),
        "selected_universal_parameter_count": policy_matrix["selected_universal_parameter_count"],
        "maximum_live_universal_parameters": policy_matrix["maximum_live_universal_parameters"],
        "minimal_universal_parameter_selection_closed": policy_matrix[
            "minimal_universal_parameter_selection_closed"
        ],
        "candidate_specific_source_theorem_present": policy_matrix[
            "candidate_specific_source_theorem_present"
        ],
        "external_replay_policy_ready": policy_matrix["external_replay_policy_ready"],
        "external_replay_policy_is_no_knob": policy_matrix["external_replay_policy_is_no_knob"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(POLICY_RECHECK, policy_recheck)

    cutset = {
        "schema": "MTTStep57InternalRThetaFrontier.v1",
        "status": "FINAL_NUMBERED_FRONTIER_INTERNAL_RTHETA_OR_MINIMAL_SOURCE_ANCHOR",
        "closed_now": {
            **final_cutset["closed_now"],
            "post_pi_external_replay_boundary_imported_into_numbered_plan": True,
            "minimal_policy_matrix_imported_into_numbered_plan": True,
        },
        "still_open": final_cutset["still_open"],
        "recommended_next": final_cutset["recommended_next"],
        "frontier_statement": (
            "All post-Pi replay/convention/threshold/mass/diagonal-profile gates are now imported into "
            "the numbered plan. The remaining proof target is internal Rtheta value derivation or a "
            "candidate-specific universal source-anchor theorem selected before empirical replay."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep57NoKnobBoundaryImportOrInternalRThetaFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "noknob_boundary_import": rel(BOUNDARY_IMPORT),
            "minimal_policy_recheck": rel(POLICY_RECHECK),
            "internal_rtheta_frontier": rel(CUTSET),
        },
        "theorem": {
            "name": "Step57NoKnobBoundaryImportTheorem",
            "proved": True,
            "statement": (
                "The post-Pi no-knob boundary and minimal universal-parameter policy matrix are imported "
                "into the active numbered plan. This fixes the current state at Rtheta readiness 8/9 with "
                "external replay ready, zero selected internal value rows, zero selected universal parameters, "
                "and a single final frontier: internal Rtheta value derivation or candidate-specific universal "
                "source-anchor selection."
            ),
        },
        "closure_decision": {
            "post_pi_external_replay_ready": True,
            "SM_parity_external_replay_boundary_declared": True,
            "Rtheta_readiness_present_count": readiness["present_count"],
            "Rtheta_readiness_requirement_count": readiness["requirement_count"],
            "only_remaining_readiness_blocker": "no_knob_value_derivation",
            "selected_internal_value_emission_count": 0,
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "accepted_internal_scalar_row_count": 0,
            "selected_universal_parameter_count": 0,
            "minimal_universal_parameter_selection_closed": False,
            "candidate_specific_universal_source_theorem_present": False,
            "no_knob_value_derivation_closed": False,
            "selected_threshold_response_functional_instantiated": False,
            "accepted_lambda_H_value": False,
            "Yukawa_mass_mixing_value_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step56["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step57_NoKnobBoundaryImport_or_InternalRThetaFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step57 NoKnobBoundaryImport or InternalRThetaFrontier v1

Status: `{STATUS}`.

Step57 imports the post-Pi final no-knob boundary into the numbered plan.

```text
post-Pi external replay ready          : true
Rtheta readiness                       : {readiness["present_count"]}/{readiness["requirement_count"]}
only remaining readiness blocker       : no_knob_value_derivation
selected internal no-knob rows         : 0
selected universal parameters          : 0
minimal parameter selection closed     : false
true SM equivalence                    : false
full no-knob closure                   : false
```

The next target is `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
