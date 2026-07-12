"""Build Step47 exceptional-physics result focus ledger.

The purpose is to isolate the potential exceptional physics claim after Step46:
not "we fitted/replayed SM values", but "a selected branch plus one source-tier
anchor plus a typed Rtheta_alpha1 map may make the SM scalar sector output data
if the remaining Xi arguments are source-selected."  This artifact keeps that
claim sharp and machine-checkable.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step47_exceptional_physics_result_focus_or_xiargumentfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RESULT_LEDGER = PACKET_DIR / "step47_exceptional_result_ledger.packet.json"
CLAIM_BOUNDARY = PACKET_DIR / "step47_claim_boundary_and_nonclaims.packet.json"
XI_FRONTIER = PACKET_DIR / "step47_xi_argument_frontier.packet.json"
PAPER_ABSTRACT = PACKET_DIR / "step47_paper_result_abstract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step47_ExceptionalPhysicsResultFocus_or_XiArgumentFrontier_v1.md"

STEP41 = DATA / "selected_step41_singlebranch_solution_assembly_or_valuefunctionalfrontier.candidate.json"
STEP42 = DATA / "selected_step42_executable_value_replay_solution_or_noknobrowfrontier.candidate.json"
STEP44 = DATA / "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution.candidate.json"
STEP46 = DATA / "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution.candidate.json"
STEP46_MAP = (
    DATA
    / "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution"
    / "step46_selected_alpha1_to_rtheta_coefficient_map.packet.json"
)
STEP46_ARGS = (
    DATA
    / "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution"
    / "step46_map_argument_closure_audit.packet.json"
)
STEP46_VALUES = (
    DATA
    / "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution"
    / "step46_value_execution_attempt.packet.json"
)
STATUS_DOC = CORPUS / "MTT_TrueSMClosure_CurrentStatus_Step42_v1.md"

STATUS = "MTT_SELECTED_STEP47_EXCEPTIONAL_PHYSICS_RESULT_FOCUS_BUILT_XI_ARGUMENT_FRONTIER_OPEN"
NEXT = "MTT_Selected_Alpha1RThetaMapArgumentFill_or_InternalValueRows_v1"


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

    inputs = [STEP41, STEP42, STEP44, STEP46, STEP46_MAP, STEP46_ARGS, STEP46_VALUES, STATUS_DOC]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step47 inputs: " + ", ".join(missing))

    step41 = load(STEP41)
    step42 = load(STEP42)
    step44 = load(STEP44)
    step46 = load(STEP46)
    step46_map = load(STEP46_MAP)
    step46_args = load(STEP46_ARGS)
    step46_values = load(STEP46_VALUES)

    branch = {
        "q": 79,
        "orientation": "F",
        "torsion_m": 1,
        "source_branch_selected": step41["theorem"]["proved"] is True,
    }
    support_closed = {
        "single_selected_branch": branch["source_branch_selected"],
        "executable_admitted_replay_solution": step42["closure_decision"][
            "executable_admitted_replay_value_solution_closed"
        ],
        "one_source_tier_anchor_alpha1": step44["closure_decision"][
            "alpha1_one_universal_source_anchor_admitted_at_source_tier"
        ],
        "typed_Rtheta_alpha1_map": step46["closure_decision"][
            "selected_alpha1_to_Rtheta_coefficient_map_constructed"
        ],
        "ten_row_codomain": step46_map["codomain_row_count"] == 10,
        "observed_values_forbidden_as_selectors": (
            step46["observed_data_used_as_selector"] is False
            and step46["target_fitting_used"] is False
        ),
    }
    exceptional_focus_closed = all(support_closed.values())
    xi_missing = step46_args["missing_arguments"]

    result_ledger = {
        "schema": "MTTStep47ExceptionalPhysicsResultLedger.v1",
        "status": "POTENTIAL_EXCEPTIONAL_RESULT_ISOLATED_CONDITIONAL_ON_XI_ARGUMENTS",
        "branch": branch,
        "support_closed": support_closed,
        "potential_exceptional_claim_if_completed": (
            "A selected MTT branch with one source-tier universal anchor alpha1 and a typed "
            "Rtheta_alpha1 coefficient map emits the nine charged Yukawa scalar rows and the Higgs "
            "lambda row without observed SM values selecting the branch, source, map, or rows."
        ),
        "why_exceptional_if_completed": [
            "SM Yukawa matrices and Higgs quartic are normally empirical input data in the SM framework",
            "the current lane would turn those scalar rows into outputs of a selected finite/source branch",
            "only one universal source-tier anchor is admitted, and it is fixed before empirical replay",
            "the map is typed over ten rows and keeps Step42 values as postchecks only",
        ],
        "current_physics_status": "CONDITIONAL_PROOF_PROGRAM_RESULT_NOT_FULL_PHYSICS_CLOSURE",
        "current_machine_status": {
            "map_constructed": True,
            "accepted_internal_value_row_count": step46_values["accepted_internal_value_row_count"],
            "all_value_execution_arguments_closed": step46_args[
                "all_value_execution_arguments_closed"
            ],
            "true_SM_equivalence_closed": step46["closure_decision"]["true_SM_equivalence_closed"],
            "full_no_knob_closed": step46["closure_decision"]["full_no_knob_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": exceptional_focus_closed,
    }
    write_json(RESULT_LEDGER, result_ledger)

    claim_boundary = {
        "schema": "MTTStep47ClaimBoundaryAndNonclaims.v1",
        "status": "EXCEPTIONAL_CLAIM_BOUNDARY_LOCKED_NO_OVERCLAIM",
        "claim_now": [
            "A selected q=79/F/m=1 proof spine is assembled at the source/first-response layer.",
            "A theorem-derived alpha1 source-strength anchor is admitted at the source/operator tier.",
            "A typed selected Rtheta_alpha1 coefficient map and ten-row codomain ledger are constructed.",
            "Observed/replay values are classified as postchecks, not selectors.",
        ],
        "do_not_claim_yet": [
            "full Standard Model derivation",
            "true precision equivalence to measured SM data",
            "no-knob Yukawa/Higgs numerical prediction",
            "accepted internal scalar value rows",
            "experimental confirmation",
        ],
        "credibility_guardrails": [
            "Xi arguments must be source-selected before Step42 postcheck comparison",
            "no residual minimization against Step42 values can select Xi",
            "one anchor may remain credible only because alpha1 is source-tier and shared across all rows",
            "any additional 2-3 anchors must be independently source-selected and overdetermined",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CLAIM_BOUNDARY, claim_boundary)

    xi_rows = []
    for row in step46_map["charged_rows"]:
        xi_rows.append(
            {
                "xi_argument": row["required_unfilled_argument"],
                "coefficient_slot": row["coefficient_slot"],
                "sector": row["sector"],
                "generation": row["generation"],
                "projector": row["spectral_projector_ref"],
                "family_eigenvalue": row["family_eigenvalue"],
                "must_be_selected_by": [
                    "magnitude-bearing projection weight theorem",
                    "selected threshold-response instantiation",
                    "generation-resolved threshold source row theorem",
                    "same-branch internal threshold/mass derivation",
                ],
                "postcheck_value_available": row["admitted_replay_postcheck_value"],
                "postcheck_value_may_select": False,
                "closed_now": False,
            }
        )
    xi_rows.append(
        {
            "xi_argument": step46_map["higgs_row"]["required_unfilled_argument"],
            "coefficient_slot": "lambda_H",
            "sector": "H",
            "generation": None,
            "projector": step46_map["higgs_row"]["spectral_projector_ref"],
            "family_eigenvalue": None,
            "must_be_selected_by": [
                "same-branch Higgs/quartic source row",
                "selected threshold-response instantiation",
                "internal Higgs mass-scheme/lambda convention theorem",
            ],
            "postcheck_value_available": step46_map["higgs_row"]["admitted_replay_postcheck_value"],
            "postcheck_value_may_select": False,
            "closed_now": False,
        }
    )
    xi_frontier = {
        "schema": "MTTStep47XiArgumentFrontier.v1",
        "status": "TEN_XI_ARGUMENTS_ARE_THE_EXCEPTIONAL_RESULT_FRONTIER",
        "missing_global_argument_classes": xi_missing,
        "xi_rows": xi_rows,
        "xi_row_count": len(xi_rows),
        "accepted_xi_row_count": 0,
        "next_required_artifact": NEXT,
        "preferred_attack_order": [
            "prove source-selected magnitude-bearing projection weights",
            "instantiate selected threshold response functional",
            "emit generation-resolved threshold source rows",
            "promote same-branch internal threshold/mass derivation",
            "execute Rtheta_alpha1 and compare Step42 postchecks",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(XI_FRONTIER, xi_frontier)

    paper_abstract = {
        "schema": "MTTStep47PaperResultAbstract.v1",
        "status": "PAPER_READY_CONDITIONAL_RESULT_STATEMENT_BUILT",
        "safe_title": "A selected alpha1-normalized Rtheta map for the MTT Standard-Model scalar sector",
        "safe_abstract": (
            "We isolate a selected q=79/F/m=1 MTT branch carrying a source-tier alpha1 normalization "
            "and construct a typed Rtheta_alpha1 map with ten scalar output slots corresponding to "
            "charged Yukawa magnitudes and the Higgs quartic row. The construction uses no observed "
            "SM value as selector. The result is conditional: numerical Standard-Model closure remains "
            "open until the magnitude-bearing Xi arguments are selected from the same branch."
        ),
        "strong_title_if_xi_closes": "One-anchor MTT derivation of the Standard-Model scalar rows",
        "strong_claim_allowed_only_if": [
            "all Xi arguments close before replay comparison",
            "Rtheta_alpha1 emits all ten scalar rows internally",
            "Step42/SM values are used only as postchecks",
            "precision comparison passes with declared scale/scheme conventions",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PAPER_ABSTRACT, paper_abstract)

    candidate = {
        "candidate": "MTTSelectedStep47ExceptionalPhysicsResultFocusOrXiArgumentFrontier",
        "status": STATUS,
        "inputs": {
            "step41": rel(STEP41),
            "step42": rel(STEP42),
            "step44": rel(STEP44),
            "step46": rel(STEP46),
            "step46_map": rel(STEP46_MAP),
            "step46_args": rel(STEP46_ARGS),
            "step46_values": rel(STEP46_VALUES),
            "status_doc": rel(STATUS_DOC),
        },
        "output_packets": {
            "exceptional_result_ledger": rel(RESULT_LEDGER),
            "claim_boundary_and_nonclaims": rel(CLAIM_BOUNDARY),
            "xi_argument_frontier": rel(XI_FRONTIER),
            "paper_result_abstract": rel(PAPER_ABSTRACT),
        },
        "theorem": {
            "name": "ExceptionalPhysicsResultBoundaryTheorem",
            "proved": exceptional_focus_closed,
            "statement": (
                "The current machine-checked spine isolates one potentially exceptional physics result: "
                "a selected q=79/F/m=1 branch plus one source-tier alpha1 anchor plus a typed Rtheta_alpha1 "
                "map. This is not yet full SM closure; the exact frontier is the ten magnitude-bearing "
                "Xi arguments required for value execution."
            ),
        },
        "closure_decision": {
            "exceptional_result_focus_ledger_closed": exceptional_focus_closed,
            "selected_branch_source_spine_closed": support_closed["single_selected_branch"],
            "alpha1_source_anchor_closed": support_closed["one_source_tier_anchor_alpha1"],
            "Rtheta_alpha1_map_constructed": support_closed["typed_Rtheta_alpha1_map"],
            "accepted_internal_value_row_count": step46_values["accepted_internal_value_row_count"],
            "accepted_xi_argument_count": 0,
            "conditional_exceptional_physics_result_identified": True,
            "full_exceptional_physics_claim_allowed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": exceptional_focus_closed,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step47_ExceptionalPhysicsResultFocus_or_XiArgumentFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step47 ExceptionalPhysicsResultFocus or XiArgumentFrontier v1

Status: `{STATUS}`.

Potential exceptional physics result isolated:

```text
selected branch                       : q=79, orientation F, torsion m=1
alpha1 source-tier anchor             : true
typed Rtheta_alpha1 map constructed   : true
ten scalar output slots               : 10
accepted internal scalar value rows   : {step46_values["accepted_internal_value_row_count"]}
accepted Xi arguments                 : 0
true SM equivalence closed            : false
```

The exceptional claim is not that Step42 replay values are a proof. The
exceptional claim, if completed, would be that the same selected MTT branch plus
one source-tier `alpha1` anchor emits the SM scalar rows through `Rtheta_alpha1`
without observed values selecting the map or rows.

The live frontier is exactly the ten magnitude-bearing arguments `Xi_s,g` and
`Xi_H`.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
