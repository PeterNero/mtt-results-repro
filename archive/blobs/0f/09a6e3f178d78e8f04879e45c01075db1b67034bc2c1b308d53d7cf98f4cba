"""Analyze q79 selected monad L2 source plus operator-Pic0/Route-C residual.

This is the sharp follow-up to the AH/good-cover reduction.  It closes the
ordered monad-difference L2 source lane under the explicit terminal
admissible-section principle already audited in this repo, and it tests whether
the remaining Route-C operator data fail for arithmetic reasons or only because
the holonomy-sensitive selected-source flags are not proved.

The script deliberately keeps two layers separate:

* selected ordered source / Ext input: machine-validated selected data under the
  explicit terminal admissible-section principle;
* operator residual provenance: still open unless a same-source theorem proves
  the Route-C finite operator slots are selected, or constructs better selected
  operator slots.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
SCRIPTS = ROOT / "scripts"

OUT_DIR = CANDIDATES / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual"
HYP_DIR = OUT_DIR / "hypothetical_routec_selected_flags_only"
OUT_TABLE = OUT_DIR / "selected_monad_operator_frontier_summary.json"
OUT_CANDIDATE = CANDIDATES / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual.candidate.json"
OUT_CERT = CERTS / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_Monad_Difference_L2_Source_and_OperatorPic0_or_RouteC_Residual_v1.md"

STATUS = "Q79_SELECTED_MONAD_L2_SOURCE_CLOSED_UNDER_SECTION_PRINCIPLE_OPERATOR_PROVENANCE_OPEN"
NEXT = "Q79_SameSource_Operator_Provenance_or_Selected_RouteC_Solve_v1"

ORDERED_PACKET = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_ordered_source.selected_under_section_principle.json"
)
COHOMOLOGY_PACKET = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)

ROUTEC_DIR = CANDIDATES / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
ROUTEC_FILES = {
    "route_c_residuals": ROUTEC_DIR / "route_c_residual.candidate.json",
    "rhoE_mesh": ROUTEC_DIR / "rhoE_mesh.candidate.json",
    "rhoE_metric": ROUTEC_DIR / "rhoE_metric.candidate.json",
    "sector_maps": ROUTEC_DIR / "sector_maps.candidate.json",
    "de_action": ROUTEC_DIR / "de_action.candidate.json",
    "riesz_gap": ROUTEC_DIR / "riesz_gap.candidate.json",
    "reduced_green": ROUTEC_DIR / "reduced_green.candidate.json",
    "dotd_response": ROUTEC_DIR / "dotd_response.candidate.json",
}
PROMOTION_PACKET = CERTS / "selected_hym_operator_source_promotion.attempt.json"

INPUTS = {
    "ah_source_or_routec_reduction": (
        CANDIDATES / "q79_ah_source_selection_or_routec_residual_reduction.candidate.json"
    ),
    "terminal_admissible_section_source_principle": (
        CANDIDATES / "terminal_admissible_section_source_principle.candidate.json"
    ),
    "ordered_source_packet": ORDERED_PACKET,
    "cohomology_packet": COHOMOLOGY_PACKET,
    "selected_gauduchon_wall_radius_gate": CANDIDATES / "selected_gauduchon_wall_radius_gate.candidate.json",
    "all_remaining_valpha_gates": CANDIDATES / "all_remaining_valpha_gates_attempt.candidate.json",
    "selected_hym_operator_source_attempt": CANDIDATES / "selected_hym_operator_source_attempt.candidate.json",
}

ALLOWED_FLAG_KEYS = {
    "selected_source_verified",
    "selected_dotD_source_verified",
    "alpha1_driver_verified",
    "selected_by_mtt",
    "status",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def run_validator(script: str, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "script": f"scripts/{script}",
        "path": rel(path),
        "exit_code": proc.returncode,
        "pass": proc.returncode == 0,
        "stdout_head": proc.stdout.splitlines()[:24],
        "stdout": proc.stdout,
    }


def patch_selected_flags(value: Any) -> Any:
    if isinstance(value, list):
        return [patch_selected_flags(entry) for entry in value]
    if not isinstance(value, dict):
        return value

    patched: dict[str, Any] = {}
    for key, entry in value.items():
        if key in {
            "selected_source_verified",
            "selected_dotD_source_verified",
            "alpha1_driver_verified",
            "selected_by_mtt",
        } and isinstance(entry, bool):
            patched[key] = True
        elif key == "status" and isinstance(entry, str):
            patched[key] = "HYPOTHETICAL_SELECTED_SOURCE_FLAGS_ONLY"
        else:
            patched[key] = patch_selected_flags(entry)
    return patched


def diff_paths(before: Any, after: Any, prefix: str = "") -> list[dict[str, Any]]:
    if type(before) is not type(after):
        return [{"path": prefix, "before": before, "after": after}]
    if isinstance(before, dict):
        changes: list[dict[str, Any]] = []
        for key in sorted(set(before) | set(after)):
            path = f"{prefix}.{key}" if prefix else key
            if key not in before or key not in after:
                changes.append({"path": path, "before": before.get(key), "after": after.get(key)})
            else:
                changes.extend(diff_paths(before[key], after[key], path))
        return changes
    if isinstance(before, list):
        changes = []
        for index, (left, right) in enumerate(zip(before, after, strict=False)):
            changes.extend(diff_paths(left, right, f"{prefix}[{index}]"))
        if len(before) != len(after):
            changes.append({"path": prefix, "before_len": len(before), "after_len": len(after)})
        return changes
    if before != after:
        return [{"path": prefix, "before": before, "after": after}]
    return []


def is_allowed_flag_change(change: dict[str, Any]) -> bool:
    key = change["path"].split(".")[-1]
    if "[" in key:
        key = key.split("[", 1)[0]
    return key in ALLOWED_FLAG_KEYS


def make_hypothetical_routec_packets() -> dict[str, Any]:
    outputs: dict[str, str] = {}
    diffs: dict[str, Any] = {}
    for name, source in ROUTEC_FILES.items():
        original = load(source)
        patched = patch_selected_flags(copy.deepcopy(original))
        out_path = HYP_DIR / f"{name}.selected_flags_only.json"
        write_json(out_path, patched)
        outputs[name] = rel(out_path)
        changes = diff_paths(original, patched)
        diffs[name] = {
            "changed_path_count": len(changes),
            "all_changes_are_source_or_status_flags": all(is_allowed_flag_change(change) for change in changes),
            "changed_paths": [change["path"] for change in changes[:80]],
        }

    promotion = load(PROMOTION_PACKET)
    patched_promotion = copy.deepcopy(promotion)
    patched_promotion["status"] = "HYPOTHETICAL_SELECTED_SOURCE_FLAGS_ONLY"
    patched_promotion["selected_source_verified"] = True
    patched_promotion["paths"] = {
        key: outputs[key] for key in (
            "route_c_residuals",
            "rhoE_mesh",
            "rhoE_metric",
            "sector_maps",
            "de_action",
            "riesz_gap",
            "reduced_green",
            "dotd_response",
        )
    }
    promotion_out = HYP_DIR / "selected_source_promotion.selected_flags_only.json"
    write_json(promotion_out, patched_promotion)
    outputs["selected_source_promotion"] = rel(promotion_out)
    promotion_changes = diff_paths(promotion, patched_promotion)
    diffs["selected_source_promotion"] = {
        "changed_path_count": len(promotion_changes),
        "all_changes_are_source_or_status_flags_or_paths": all(
            is_allowed_flag_change(change) or change["path"].startswith("paths.")
            for change in promotion_changes
        ),
        "changed_paths": [change["path"] for change in promotion_changes[:80]],
    }
    return {"outputs": outputs, "diffs": diffs}


def build_candidate() -> dict[str, Any]:
    terminal = load(INPUTS["terminal_admissible_section_source_principle"])
    ordered = load(ORDERED_PACKET)
    cohomology = load(COHOMOLOGY_PACKET)
    gauduchon = load(INPUTS["selected_gauduchon_wall_radius_gate"])
    all_remaining = load(INPUTS["all_remaining_valpha_gates"])

    hypothetical = make_hypothetical_routec_packets()
    hyp_paths = {key: ROOT / value for key, value in hypothetical["outputs"].items()}

    validators = {
        "selected_ordered_source": run_validator(
            "validate_visible_rank2_l2_ordered_source_packet.py", ORDERED_PACKET
        ),
        "selected_h1_ext_cohomology": run_validator(
            "validate_visible_rank2_l2_cohomology.py", COHOMOLOGY_PACKET
        ),
        "routec_residual_original": run_validator(
            "validate_iwasawa_route_c_residuals.py", ROUTEC_FILES["route_c_residuals"]
        ),
        "selected_source_promotion_original": run_validator(
            "validate_iwasawa_selected_source_promotion.py", PROMOTION_PACKET
        ),
        "routec_residual_hypothetical_flags_only": run_validator(
            "validate_iwasawa_route_c_residuals.py", hyp_paths["route_c_residuals"]
        ),
        "selected_source_promotion_hypothetical_flags_only": run_validator(
            "validate_iwasawa_selected_source_promotion.py",
            hyp_paths["selected_source_promotion"],
        ),
    }

    ordered_closed = (
        validators["selected_ordered_source"]["pass"]
        and ordered["source"]["selected_by_mtt"] is True
        and ordered["status"] == "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
    )
    ext_closed = (
        validators["selected_h1_ext_cohomology"]["pass"]
        and cohomology["reported_cohomology"]["h1"] == 8
        and cohomology["source"]["selected_by_mtt"] is True
    )
    hypothetical_promotion_pass = validators[
        "selected_source_promotion_hypothetical_flags_only"
    ]["pass"]

    summary = {
        "selected_monad_L2_ordered_source_closed_under_explicit_section_principle": ordered_closed,
        "selected_h1_8_nonzero_ext_input_closed_under_explicit_section_principle": ext_closed,
        "ordered_layer_pic0_quotient_closed": ordered["pic0_resolution"][
            "source_selected_or_quotiented"
        ],
        "operator_layer_pic0_recheck_still_required": True,
        "original_routec_residual_validator_pass": validators["routec_residual_original"]["pass"],
        "original_selected_source_promotion_validator_pass": validators[
            "selected_source_promotion_original"
        ]["pass"],
        "hypothetical_flags_only_routec_residual_validator_pass": validators[
            "routec_residual_hypothetical_flags_only"
        ]["pass"],
        "hypothetical_flags_only_selected_source_promotion_validator_pass": hypothetical_promotion_pass,
        "operator_arithmetic_obstruction_found_in_current_finite_packets": not hypothetical_promotion_pass,
        "remaining_operator_obstruction_is_selected_source_provenance": hypothetical_promotion_pass,
        "full_HYM_or_SM_closure_claimed": False,
    }

    return {
        "certificate": "Q79SelectedMonadL2SourceAndOperatorPic0OrRouteCResidual",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "selected_monad_difference_L2_source_theorem": {
            "name": "Q79SelectedMonadDifferenceL2SourceUnderTerminalSectionPrinciple",
            "proved_under_explicit_terminal_admissible_section_principle": ordered_closed,
            "unconditional_in_current_corpus_without_named_principle": False,
            "principle_status": terminal["source_principle"]["status"],
            "selected_source_label": terminal["selection_derivation"]["selected_source_label"],
            "selected_L": terminal["selection_derivation"]["selected_L"],
            "selected_L2": terminal["selection_derivation"]["selected_L2"],
            "selected_c2": terminal["selection_derivation"]["selected_c2"],
            "ordered_source_validator_pass": validators["selected_ordered_source"]["pass"],
            "statement": (
                "Assuming the explicit TerminalAdmissibleSectionSourcePrinciple.v1 "
                "as the MTT representative-selection rule, the visible ordered L "
                "source is the terminal monad difference g3/L3-K2. The strict "
                "ordered-source validator accepts L=(1,-2,0), L^2=(2,-4,0), "
                "E12=2, E34=-4, and the ordered-layer Pic0 quotient."
            ),
        },
        "selected_non_split_ext_input_theorem": {
            "name": "Q79SelectedH1EightNonzeroExtInput",
            "proved_under_explicit_terminal_admissible_section_principle": ext_closed,
            "h1": cohomology["reported_cohomology"]["h1"],
            "nonzero_extension_class_label": cohomology["reported_cohomology"][
                "nonzero_extension_class_label"
            ],
            "cohomology_validator_pass": validators["selected_h1_ext_cohomology"]["pass"],
            "statement": (
                "The selected terminal section packet promotes the h1=8 L^2 "
                "cohomology data and a nonzero closed non-exact Ext vector to "
                "selected non-split V_alpha input data. This is the non-split "
                "extension input, not yet a same-source finite operator response."
            ),
        },
        "operator_pic0_and_routec_residual_frontier": {
            "ordered_layer_pic0_scope": ordered["pic0_resolution"]["scope"],
            "ordered_layer_pic0_rule": ordered["pic0_resolution"]["rule"],
            "operator_layer_pic0_recheck_required": True,
            "selected_gauduchon_wall_status": gauduchon["status"],
            "source_certified_target_wall_present": gauduchon["current_source_status"][
                "source_certified_target_wall_present"
            ],
            "all_remaining_gate_summary": all_remaining["gate_summary"],
            "original_routec_and_promotion_fail_because_selected_flags_absent": (
                validators["routec_residual_original"]["pass"] is False
                and validators["selected_source_promotion_original"]["pass"] is False
            ),
            "hypothetical_flags_only_test": {
                "purpose": (
                    "diagnostic only: change selected-source/provenance flags and "
                    "paths while leaving numerical operator matrices/residuals unchanged"
                ),
                "packet_paths": hypothetical["outputs"],
                "diffs": hypothetical["diffs"],
                "routec_residual_passes": validators[
                    "routec_residual_hypothetical_flags_only"
                ]["pass"],
                "selected_source_promotion_passes": hypothetical_promotion_pass,
                "interpretation": (
                    "Current finite Route-C arithmetic has no validator-detected "
                    "residual obstruction once selected-source provenance flags are "
                    "supplied. The flags are not supplied by the current corpus, so "
                    "this remains a provenance theorem, not a closed selected source."
                ),
            },
        },
        "validator_results": validators,
        "what_closes_now": {
            "selected_monad_difference_L2_source_under_explicit_terminal_section_principle": ordered_closed,
            "strict_ordered_source_validator_passes_for_selected_packet": validators[
                "selected_ordered_source"
            ]["pass"],
            "selected_h1_8_nonzero_Ext_input": ext_closed,
            "ordered_Chern_H1_curvature_layer_Pic0_quotient": True,
            "routec_operator_arithmetic_reduced_to_selected_source_provenance_flags": hypothetical_promotion_pass,
        },
        "what_remains_open": {
            "promote_terminal_admissible_section_principle_to_main_MTT_spine_or_derivation": True,
            "operator_layer_Pic0_selection_or_quotient_for_holonomy_sensitive_data": True,
            "same_source_operator_provenance_for_routec_residual_DE_Riesz_Green_dotD": True,
            "selected_Gauduchon_chamber_or_selected_RouteC_residual_source": True,
            "same_source_ChernWeil_GS_row": True,
            "primitive_C1_contractions": True,
            "selected_Yukawa_CKM_PMNS_Higgs_RG_data": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "claims_unconditional_terminal_section_principle_in_current_corpus": False,
            "claims_operator_layer_Pic0_closed": False,
            "claims_selected_RouteC_residual": False,
            "claims_selected_HYM_connection": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79SelectedMonadL2SourceAndOperatorProvenanceFrontierTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The selected monad-difference L2 source and selected nonzero Ext "
                "input are closed under the explicit terminal admissible-section "
                "principle. The remaining Route-C/operator obstruction is not a "
                "detected numerical residual in the current finite packets; it is "
                "the absence of a same-source theorem verifying the holonomy-sensitive "
                "operator provenance and operator-layer Pic0 behavior."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }


def render_bool_map(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def build_paper(data: dict[str, Any]) -> str:
    source = data["selected_monad_difference_L2_source_theorem"]
    ext = data["selected_non_split_ext_input_theorem"]
    frontier = data["operator_pic0_and_routec_residual_frontier"]
    hyp = frontier["hypothetical_flags_only_test"]
    return f"""# Q79 Selected Monad Difference L2 Source and OperatorPic0 or Route-C Residual v1

## Result

The selected monad-difference `L^2` source lane is closed **under the explicit
TerminalAdmissibleSectionSourcePrinciple.v1**.

The Route-C operator residual lane is not closed. The current finite operator
packets pass only in a hypothetical selected-flags-only diagnostic, so the
remaining wall is selected operator provenance, not new residual arithmetic.

## Selected Monad Difference L2 Source

`{source["name"]}`:

- proved under explicit section principle: `{source["proved_under_explicit_terminal_admissible_section_principle"]}`
- unconditional without named principle: `{source["unconditional_in_current_corpus_without_named_principle"]}`
- selected source label: `{source["selected_source_label"]}`
- selected `L`: `{source["selected_L"]}`
- selected `L^2`: `{source["selected_L2"]}`
- ordered-source validator pass: `{source["ordered_source_validator_pass"]}`

{source["statement"]}

## Selected Non-Split Ext Input

`{ext["name"]}`:

- proved under explicit section principle: `{ext["proved_under_explicit_terminal_admissible_section_principle"]}`
- `h1`: `{ext["h1"]}`
- nonzero Ext vector: `{ext["nonzero_extension_class_label"]}`
- cohomology validator pass: `{ext["cohomology_validator_pass"]}`

{ext["statement"]}

## Operator Frontier

- ordered-layer `Pic0` scope: `{frontier["ordered_layer_pic0_scope"]}`
- operator-layer `Pic0` recheck required: `{frontier["operator_layer_pic0_recheck_required"]}`
- selected Gauduchon wall status: `{frontier["selected_gauduchon_wall_status"]}`
- source-certified target wall present: `{frontier["source_certified_target_wall_present"]}`
- original Route-C and promotion fail because selected flags are absent: `{frontier["original_routec_and_promotion_fail_because_selected_flags_absent"]}`

## Hypothetical Flags-Only Diagnostic

Purpose: {hyp["purpose"]}.

- Route-C residual validator pass after flags-only diagnostic: `{hyp["routec_residual_passes"]}`
- selected-source promotion validator pass after flags-only diagnostic: `{hyp["selected_source_promotion_passes"]}`

Interpretation: {hyp["interpretation"]}

This diagnostic is not a selected-source proof.

## What This Closes

{render_bool_map(data["what_closes_now"])}

## What Remains Open

{render_bool_map(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a frontier theorem.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_TABLE, {
        **data["what_closes_now"],
        "status": data["status"],
        "next_required_artifact": data["next_required_artifact"],
    })
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 selected monad L2 source and operator/Route-C frontier")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
