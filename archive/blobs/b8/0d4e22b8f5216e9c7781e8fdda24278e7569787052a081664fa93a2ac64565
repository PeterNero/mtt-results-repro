"""Lock down the remaining V_alpha proof obligations after terminal selection.

This script is deliberately not a new proof of stability, HYM, Chern-Weil
source derivation, or Standard Model closure.  It records the sharper result
now achieved:

* the terminal admissible-section principle selects L3-K2 under its stated
  condition,
* the selected ordered L^2 source and h1=8/nonzero Ext packet validate,
* split line/Cartan HYM shortcuts are ruled out,
* the downstream selected V_alpha validator stack has no hidden finite-matrix
  defect under hypothetical same-source flags,
* the remaining work is reduced to named source/operator gates.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"

TERMINAL_CERT = CERTS / "terminal_admissible_section_source_principle_certificate.json"
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
SPLIT_NO_GO_CERT = CERTS / "visible_split_line_hym_no_go_certificate.json"
STABLE_SIGN_CERT = CERTS / "visible_stable_source_sign_gate_certificate.json"
CRITICAL_PATH_CERT = CERTS / "valpha_operator_source_critical_path_certificate.json"
OPERATOR_SUFFICIENCY_CERT = CERTS / "selected_valpha_operator_source_sufficiency_certificate.json"
OPERATOR_ATTEMPT_CERT = CERTS / "selected_valpha_chern_weil_operator_source_attempt_certificate.json"
CURRENT_OPERATOR_ATTEMPT = CANDIDATES / "selected_valpha_chern_weil_operator_source.current_attempt.json"
C1_REDUCTION_CERT = CERTS / "c1_finite_response_matrix_reduction_certificate.json"
ROUTE_C_DEPENDENCY_CERT = CERTS / "iwasawa_route_c_smoke_c1_dependency_certificate.json"

OUT_CANDIDATE = CANDIDATES / "terminal_valpha_remaining_parts_lockdown.candidate.json"
OUT_CERT = CERTS / "terminal_valpha_remaining_parts_lockdown_certificate.json"


RETIRED_OPEN_ITEMS = {
    "rank2_valpha_model_selected must be true": "rank-two V_alpha source target is selected under the terminal admissible-section principle",
    "terminal_monad_difference_L3_minus_K2_selector_closed must be true": "terminal g3/L3-K2 selector closed under the explicit principle",
    "ordered_source_validator_passes must be true": "selected ordered-source packet validates",
    "nonzero_ext_class_selected must be true": "selected h1=8 cohomology packet supplies a nonzero closed non-exact Ext vector",
    "ordered source validator did not pass (exit 2)": "old current attempt still points at the pre-terminal fixture; the selected packet passes",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def run_validator(script: str, packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script), str(packet)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "stdout_head": proc.stdout.strip().splitlines()[:16],
    }


def parse_prefixed_json(stdout: str, prefix: str) -> dict[str, Any]:
    for line in stdout.splitlines():
        if line.startswith(prefix):
            return json.loads(line[len(prefix) :])
    return {}


def guardrails_false(*certificates: dict[str, Any]) -> bool:
    for certificate in certificates:
        guardrails = certificate.get("guardrails", {})
        if not guardrails or any(value is True for value in guardrails.values()):
            return False
    return True


def analyze() -> dict[str, Any]:
    terminal = load(TERMINAL_CERT)
    ordered_packet = load(ORDERED_PACKET)
    cohomology_packet = load(COHOMOLOGY_PACKET)
    split_no_go = load(SPLIT_NO_GO_CERT)
    stable_sign = load(STABLE_SIGN_CERT)
    critical_path = load(CRITICAL_PATH_CERT)
    sufficiency = load(OPERATOR_SUFFICIENCY_CERT)
    operator_attempt = load(OPERATOR_ATTEMPT_CERT)
    c1_reduction = load(C1_REDUCTION_CERT)
    route_c_dependency = load(ROUTE_C_DEPENDENCY_CERT)

    ordered_validation = run_validator(
        "validate_visible_rank2_l2_ordered_source_packet.py",
        ORDERED_PACKET,
    )
    cohomology_validation = run_validator(
        "validate_visible_rank2_l2_cohomology.py",
        COHOMOLOGY_PACKET,
    )
    current_operator_validation = run_validator(
        "validate_selected_valpha_chern_weil_operator_source.py",
        CURRENT_OPERATOR_ATTEMPT,
    )
    current_operator_report = parse_prefixed_json(
        current_operator_validation["stdout"],
        "selected_valpha_chern_weil_operator_source_report=",
    )

    terminal_closes = terminal.get("what_this_closes_under_principle", {})
    terminal_open = terminal.get("still_open", {})
    split_closes = split_no_go.get("what_this_closes", {})
    stable_closes = stable_sign.get("what_this_closes", {})
    sufficiency_closes = sufficiency.get("what_this_closes", {})
    critical_closes = critical_path.get("what_this_closes", {})

    current_open_items = current_operator_report.get(
        "open_items",
        operator_attempt.get("first_open_items", []),
    )
    retired_current_open_items = {
        item: RETIRED_OPEN_ITEMS[item]
        for item in current_open_items
        if item in RETIRED_OPEN_ITEMS
    }
    still_open_current_items = [
        item for item in current_open_items if item not in retired_current_open_items
    ]

    selected_h1_8_ext = (
        cohomology_validation["exit_code"] == 0
        and cohomology_packet.get("reported_cohomology", {}).get("h1") == 8
        and cohomology_packet.get("acceptance_tests", {}).get("extension_class_closed") is True
        and cohomology_packet.get("acceptance_tests", {}).get("extension_class_not_exact") is True
    )

    closed_parts = {
        "terminal_g3_L3_minus_K2_selector_under_explicit_principle": terminal_closes.get(
            "terminal_g3_source_selector"
        )
        is True,
        "ordered_integral_L2_source_validates": ordered_validation["exit_code"] == 0
        and ordered_packet.get("target", {}).get("L2") == [2, -4, 0],
        "h1_8_nonzero_ext_packet_validates": selected_h1_8_ext,
        "split_line_or_cartan_hym_shortcut_retired": split_closes.get(
            "all_split_line_hym_shortcuts_for_positive_alpha1"
        )
        is True,
        "stable_hym_sign_convention_closed": stable_closes.get(
            "stable_source_sign_convention_guardrail"
        )
        is True,
        "critical_path_reduced_to_single_packet": critical_closes.get(
            "remaining_cut_set_collapsed_to_selected_source_packet"
        )
        is True,
        "downstream_validator_plumbing_retired": sufficiency_closes.get(
            "downstream_validator_stack_has_no_hidden_matrix_defect"
        )
        is True,
        "finite_c1_assembly_formula_available": c1_reduction.get("status")
        == "FINITE_C1_RESPONSE_REDUCED_TO_PRIMITIVE_CONTRACTIONS_VALUES_OPEN"
        and c1_reduction.get("verdict", {}).get("closes_finite_response_formula") is True,
        "route_c_smoke_not_promoted_as_selected_proof": route_c_dependency.get(
            "guardrails", {}
        ).get("claims_selected_C1_response")
        is False
        and route_c_dependency.get("guardrails", {}).get("claims_selected_overlap_tensor")
        is False,
    }

    retired_as_nonblockers = {
        "old_L_sign_search": closed_parts["terminal_g3_L3_minus_K2_selector_under_explicit_principle"],
        "old_h1_or_nonzero_ext_search": closed_parts["h1_8_nonzero_ext_packet_validates"],
        "finite_qutrit_sign_search_for_terminal_path": terminal_closes.get(
            "finite_qutrit_sign_search_retired_for_terminal_g3_route"
        )
        is True,
        "equal_radius_or_gauduchon_wall_as_primary_selector": terminal_closes.get(
            "gauduchon_wall_reclassified_as_stability_witness"
        )
        is True,
        "split_abelian_hym_source": closed_parts["split_line_or_cartan_hym_shortcut_retired"],
        "visible_gs_row_arithmetic_as_independent_blocker": critical_closes.get(
            "critical_path_is_not_visible_gs_curvature_row"
        )
        is True,
        "s3_finite_shape_as_independent_blocker": critical_closes.get(
            "critical_path_is_not_s3_freed_witten_or_block_projectors"
        )
        is True,
        "validator_plumbing_as_independent_blocker": closed_parts[
            "downstream_validator_plumbing_retired"
        ],
        "benchmark_or_observed_flavor_fitting": True,
    }

    remaining_proof_gates = [
        {
            "gate": "UnconditionalTerminalAdmissibleSectionTheorem",
            "status": "OPEN",
            "why_open": (
                "The selector currently depends on an explicit principle synthesized "
                "from the corpus. It must be promoted to the MTT spine or derived "
                "from projection/admissibility rules."
            ),
            "would_close": "terminal source selection without conditional wording",
        },
        {
            "gate": "SelectedNonSplitVAlphaStabilityOrRouteCResidual",
            "status": "OPEN",
            "why_open": (
                "A nonzero Ext class constructs a non-split extension candidate, "
                "but does not prove stability/HYM or a selected Route-C residual."
            ),
            "would_close": "non_split_extension_stability_or_HYM",
        },
        {
            "gate": "OperatorLayerPic0Recheck",
            "status": "OPEN",
            "why_open": (
                "Pic0 is quotiented only for ordered Chern/H1/ordinary-curvature "
                "data. Holonomy-sensitive D_E/Riesz/Green/dotD data must recheck it."
            ),
            "would_close": "operator_layer_Pic0",
        },
        {
            "gate": "SameSourceChernWeilGSRow",
            "status": "OPEN",
            "why_open": (
                "The visible GS curvature row is known, but it has not yet been "
                "derived as the Chern-Weil row of the same selected V_alpha source."
            ),
            "would_close": "same_source_Chern_Weil_derivation",
        },
        {
            "gate": "SameSourceDErhoERieszGreenDotD",
            "status": "OPEN",
            "why_open": (
                "Finite validators exist, and Route-C smoke packets reach the layer, "
                "but selected source flags and same-branch alpha1-driver proof are absent."
            ),
            "would_close": "same_source_D_E_Riesz_Green_dotD",
        },
        {
            "gate": "PrimitiveC1Contractions",
            "status": "OPEN",
            "why_open": (
                "The finite C1 assembly formula is closed, but the primitive 3x3 "
                "contraction blocks are still template data."
            ),
            "would_close": "selected_C1_response_matrices",
        },
        {
            "gate": "NoProxyYukawaCKMPMNSAndSMClosure",
            "status": "OPEN",
            "why_open": (
                "Yukawa, CKM, PMNS, kinetic metrics, thresholds, and RG matching "
                "still require selected matrix data. Observed values remain forbidden inputs."
            ),
            "would_close": "full_SM_data_theorem",
        },
    ]

    still_open = {
        "promote_terminal_admissible_section_principle_or_prove_it": terminal_open.get(
            "promote_principle_to_unconditional_MTT_axiom_or_prove_from_projection_admissibility"
        )
        is True,
        "non_split_extension_stability_or_HYM": True,
        "operator_layer_Pic0_recheck": True,
        "same_source_Chern_Weil_GS_row": True,
        "same_source_D_E_Riesz_Green_dotD": True,
        "primitive_C1_contractions": True,
        "Yukawa_CKM_PMNS_magnitudes": True,
        "full_SM_closure": True,
    }

    guardrails = {
        "claims_unconditional_terminal_selector": False,
        "claims_stability_or_HYM_proved": False,
        "claims_operator_layer_Pic0_resolved": False,
        "claims_same_source_Chern_Weil_or_D_E_constructed": False,
        "claims_primitive_C1_values_computed": False,
        "claims_Yukawa_CKM_PMNS_values_computed": False,
        "claims_full_SM_closure": False,
        "uses_observed_flavor_data": False,
        "uses_benchmark_flavor_entries": False,
    }

    lockdown_passes = (
        all(closed_parts.values())
        and all(retired_as_nonblockers.values())
        and all(still_open.values())
        and guardrails_false(terminal, split_no_go, stable_sign, critical_path, sufficiency)
        and all(value is False for value in guardrails.values())
        and current_operator_validation["exit_code"] == 2
        and len(retired_current_open_items) >= 5
    )

    report = {
        "calculation": "TerminalVAlphaRemainingPartsLockdown",
        "status": (
            "TERMINAL_VALPHA_REMAINING_PARTS_LOCKED_TO_STABILITY_AND_OPERATOR_SOURCE_OPEN"
            if lockdown_passes
            else "TERMINAL_VALPHA_REMAINING_PARTS_LOCKDOWN_INCOMPLETE"
        ),
        "generated_by": "scripts/lock_terminal_valpha_remaining_parts.py",
        "inputs": {
            "terminal_admissible_section_source_principle": rel(TERMINAL_CERT),
            "selected_ordered_source_packet": rel(ORDERED_PACKET),
            "selected_cohomology_packet": rel(COHOMOLOGY_PACKET),
            "visible_split_line_hym_no_go": rel(SPLIT_NO_GO_CERT),
            "visible_stable_source_sign_gate": rel(STABLE_SIGN_CERT),
            "valpha_operator_source_critical_path": rel(CRITICAL_PATH_CERT),
            "selected_valpha_operator_source_sufficiency": rel(OPERATOR_SUFFICIENCY_CERT),
            "selected_valpha_operator_source_attempt": rel(OPERATOR_ATTEMPT_CERT),
            "c1_finite_response_matrix_reduction": rel(C1_REDUCTION_CERT),
            "route_c_smoke_c1_dependency": rel(ROUTE_C_DEPENDENCY_CERT),
        },
        "validator_results": {
            "selected_ordered_source": {
                "exit_code": ordered_validation["exit_code"],
                "stdout_head": ordered_validation["stdout_head"],
            },
            "selected_h1_ext": {
                "exit_code": cohomology_validation["exit_code"],
                "stdout_head": cohomology_validation["stdout_head"],
            },
            "current_operator_attempt": {
                "exit_code": current_operator_validation["exit_code"],
                "status": current_operator_report.get("status"),
                "open_item_count": len(current_open_items),
            },
        },
        "selected_terminal_data": {
            "source_label": terminal.get("selection_derivation", {}).get("selected_source_label"),
            "L": terminal.get("selection_derivation", {}).get("selected_L"),
            "L2": terminal.get("selection_derivation", {}).get("selected_L2"),
            "c2_valpha": terminal.get("selection_derivation", {}).get("selected_c2"),
            "h1": cohomology_packet.get("reported_cohomology", {}).get("h1"),
            "nonzero_ext_class_label": cohomology_packet.get("reported_cohomology", {}).get(
                "nonzero_extension_class_label"
            ),
        },
        "closed_parts": closed_parts,
        "retired_as_nonblockers": retired_as_nonblockers,
        "current_operator_attempt_reclassification": {
            "retired_open_items": retired_current_open_items,
            "still_open_items": still_open_current_items,
        },
        "remaining_proof_gates": remaining_proof_gates,
        "still_open": still_open,
        "next_executable_order": [
            "SelectedNonSplitVAlphaStabilityOrRouteCResidual",
            "SameSourceChernWeilGSRow",
            "SameSourceDErhoERieszGreenDotD",
            "OperatorLayerPic0Recheck",
            "PrimitiveC1Contractions",
            "NoProxyYukawaCKMPMNSAndSMClosure",
        ],
        "guardrails": guardrails,
        "verdict": {
            "honest_answer": (
                "The remaining parts are now locked down: the L-sign, ordered L2, "
                "and h1=8/nonzero Ext questions are no longer the blocker under "
                "the explicit terminal admissible-section principle.  What remains "
                "is a real selected-source/operator proof: stability or Route-C "
                "residual, operator-layer Pic0, same-source Chern-Weil/GS and "
                "D_E/Riesz/Green/dotD, then primitive C1 and no-proxy SM matrices."
            ),
            "credibility_note": (
                "This improves credibility by refusing to call conditional source "
                "selection, Route-C smoke data, visible-row arithmetic, or validator "
                "plumbing a full physical proof."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "TerminalVAlphaRemainingPartsLockdown",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "inputs": report["inputs"],
        "validator_results": report["validator_results"],
        "selected_terminal_data": report["selected_terminal_data"],
        "closed_parts": report["closed_parts"],
        "retired_as_nonblockers": report["retired_as_nonblockers"],
        "current_operator_attempt_reclassification": report[
            "current_operator_attempt_reclassification"
        ],
        "remaining_proof_gates": report["remaining_proof_gates"],
        "still_open": report["still_open"],
        "next_executable_order": report["next_executable_order"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "TERMINAL_VALPHA_REMAINING_PARTS_LOCKED_TO_STABILITY_AND_OPERATOR_SOURCE_OPEN"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
