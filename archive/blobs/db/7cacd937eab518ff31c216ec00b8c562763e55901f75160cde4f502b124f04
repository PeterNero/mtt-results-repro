"""Build Step 44 alpha1 universal source-anchor admission or Rtheta row execution frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ANCHOR = PACKET_DIR / "step44_alpha1_source_anchor_admission.packet.json"
FRONTIER = PACKET_DIR / "step44_rtheta_row_execution_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step44_Alpha1UniversalAnchorAdmission_or_RThetaRowExecution_v1.md"

STEP43 = DATA / "selected_step43_minimaluniversalparameter_readiness_or_internalrowclosure.candidate.json"
STEP42 = DATA / "selected_step42_executable_value_replay_solution_or_noknobrowfrontier.candidate.json"
STEP40 = DATA / "selected_step40_dotdtransport_alpha1import_or_primitivec1frontier.candidate.json"
ALPHA_IMPORT = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
UNIVERSAL_POLICY = DATA / "universal_source_parameter_policy.candidate.json"
CROSSUSE = DATA / "universal_crossuse_parameter_admissibility_theorem.candidate.json"

STATUS = "MTT_SELECTED_STEP44_ALPHA1_UNIVERSAL_SOURCE_ANCHOR_ADMITTED_RTHETA_ROW_EXECUTION_OPEN"
NEXT = "MTT_Selected_RThetaRowsFromAlpha1Anchor_or_InternalCoefficientRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dig(data: dict[str, Any], dotted: str, default: Any = None) -> Any:
    cur: Any = data
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP43, STEP42, STEP40, ALPHA_IMPORT, UNIVERSAL_POLICY, CROSSUSE]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 44 inputs: " + ", ".join(missing))

    step43 = load(STEP43)
    step42 = load(STEP42)
    step40 = load(STEP40)
    alpha_import = load(ALPHA_IMPORT)
    policy = load(UNIVERSAL_POLICY)
    crossuse = load(CROSSUSE)
    alpha = alpha_import["alpha1_driver_replay_import"]

    admission_checks = {
        "policy_allows_universal_source_parameters": dig(
            policy, "what_closes_now.minimal_universal_parameter_tier_named"
        )
        is True,
        "crossuse_guard_built": dig(crossuse, "what_closes_now.cross_use_universal_parameter_policy_theorem") is True,
        "step43_one_anchor_nearest": dig(step43, "closure_decision.nearest_allowed_fallback")
        == "one_universal_source_anchor",
        "step42_executable_replay_solution_closed": dig(
            step42, "closure_decision.executable_admitted_replay_value_solution_closed"
        )
        is True,
        "alpha1_same_branch_source_selected": alpha["selected_N_alpha1_h_ext_value"] is True
        and alpha["selected_dotD_source_verified"] is True
        and alpha["alpha1_driver_verified"] is True,
        "alpha1_value_fixed_without_observed_selector": alpha["lambda_alpha1"] == 1.0
        and alpha["N_alpha1_h_ext"] == 1.0
        and alpha_import["target_fitting_used"] is False,
        "honest_dotd_replay_closed": alpha["honest_dotD_alpha1_replay"] is True
        and dig(step40, "closure_decision.honest_dotD_alpha1_replay_closed") is True,
        "tangent_residual_zero": alpha["tangent_residual_l2"] == 0.0,
    }
    anchor_admitted = all(admission_checks.values())

    anchor_packet = {
        "schema": "MTTStep44Alpha1SourceAnchorAdmission.v1",
        "status": "ALPHA1_ADMITTED_AS_ONE_UNIVERSAL_SOURCE_ANCHOR_FOR_OPERATOR_BRANCH",
        "anchor": {
            "name": "alpha1_source_strength_anchor",
            "parameter_count": 1,
            "lambda_alpha1": alpha["lambda_alpha1"],
            "N_alpha1_h_ext": alpha["N_alpha1_h_ext"],
            "du_dalpha1_equals_h_ext": alpha["du_dalpha1_equals_h_ext"],
            "selected_dotD_source_verified": alpha["selected_dotD_source_verified"],
            "alpha1_driver_verified": alpha["alpha1_driver_verified"],
            "honest_dotD_alpha1_replay": alpha["honest_dotD_alpha1_replay"],
            "tangent_residual_l2": alpha["tangent_residual_l2"],
        },
        "admission_checks": admission_checks,
        "admitted_at_source_tier": anchor_admitted,
        "admitted_as_value_closure_anchor": False,
        "guardrail": (
            "alpha1 is admitted as the nearest one-universal source anchor for the selected operator "
            "branch. It is not a Yukawa/Higgs value fit and does not close internal Rtheta coefficient "
            "rows until a row-execution theorem maps this anchor through Rtheta."
        ),
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(ANCHOR, anchor_packet)

    frontier = {
        "schema": "MTTStep44RThetaRowExecutionFrontier.v1",
        "status": "ONE_ANCHOR_SOURCE_TIER_ADMITTED_VALUE_ROW_EXECUTION_OPEN",
        "readiness_after_step44": {
            "one_anchor_source_tier_admitted": anchor_admitted,
            "one_anchor_lane_readiness": "5/6",
            "selected_value_anchor_count": 0,
            "accepted_internal_scalar_row_count": 0,
            "accepted_Rtheta_coefficient_value_count": 0,
        },
        "remaining_single_missing_gate": {
            "name": "RthetaRowsFromAlpha1AnchorExecution",
            "required": True,
            "description": (
                "Execute or prove the selected map from the alpha1 source-strength anchor through "
                "the Rtheta coefficient/value functional to the nine charged magnitude rows and "
                "lambda_H, without using observed values as selectors."
            ),
        },
        "still_open": {
            "selected_internal_Rtheta_coefficient_rows_closed": False,
            "selected_lambda_H_row_closed": False,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_payload": NEXT,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedStep44Alpha1UniversalAnchorAdmissionOrRThetaRowExecution",
        "status": STATUS,
        "inputs": {
            "step43": rel(STEP43),
            "step42": rel(STEP42),
            "step40": rel(STEP40),
            "alpha1_import": rel(ALPHA_IMPORT),
            "universal_policy": rel(UNIVERSAL_POLICY),
            "crossuse": rel(CROSSUSE),
        },
        "output_packets": {
            "alpha1_source_anchor_admission": rel(ANCHOR),
            "rtheta_row_execution_frontier": rel(FRONTIER),
        },
        "theorem": {
            "name": "Step44Alpha1SourceAnchorAdmissionTheorem",
            "proved": anchor_admitted,
            "statement": (
                "The theorem-derived same-branch alpha1 source-strength normalization can be admitted "
                "as the nearest one-universal source anchor at the operator/source tier. This advances "
                "the one-anchor route from readiness 4/6 to 5/6. It does not close minimal-parameter "
                "SM value closure until an Rtheta row-execution theorem maps the anchor to the scalar "
                "coefficient rows."
            ),
        },
        "closure_decision": {
            "alpha1_one_universal_source_anchor_admitted_at_source_tier": anchor_admitted,
            "one_anchor_lane_readiness": "5/6",
            "selected_universal_source_anchor_count_at_source_tier": 1,
            "selected_value_anchor_count": 0,
            "effective_fitted_parameter_count": 0,
            "Rtheta_rows_from_alpha1_anchor_executed": False,
            "selected_internal_Rtheta_coefficient_rows_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "accepted_Rtheta_coefficient_value_count": 0,
            "selected_lambda_H_row_closed": False,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": anchor_admitted,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step44_Alpha1UniversalAnchorAdmission_or_RThetaRowExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step44 Alpha1UniversalAnchorAdmission or RThetaRowExecution v1

Status: `{STATUS}`.

Step44 admits the nearest one-anchor fallback at the source/operator tier:

- anchor: `alpha1_source_strength_anchor`
- `lambda_alpha1 = 1`
- `N_alpha1(h_ext) = 1`
- `du/dalpha1 = h_ext`
- `selected_dotD_source_verified = true`
- `alpha1_driver_verified = true`
- honest `dotD_alpha1` replay: true

This moves the one-anchor lane from `4/6` to `5/6`.

It does not close minimal-parameter SM value closure. The single remaining gate
is now:

`{NEXT}`

That gate must map the admitted `alpha1` source anchor through the selected
`Rtheta` coefficient/value functional to the nine charged magnitude rows and
`lambda_H`, without observed values selecting the map.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
