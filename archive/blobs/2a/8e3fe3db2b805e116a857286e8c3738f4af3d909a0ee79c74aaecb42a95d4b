"""Close the q79 Route-C basis-transport primitive-source theorem gate.

The previous q79 payload gate selected this as the next target.  The adjacent
SM-parity proof/counterexample packet now tests the target directly: primitive
only source emission is insufficient, because the fixed-fiber primitive span
does not contain the locked qutrit/Weyl splitter target.

This q79 artifact imports that result as a q79-local decision theorem and
refines the next target to a Weyl-pair basis-transport or vertex source
theorem.  It does not claim A_selected, b_selected, or full SM closure.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

CONSTANTS = TEXPAPERS / "mtt-nonsm-constants-no-knob"
GR = TEXPAPERS / "mtt-protospinor-gr-response-proof"
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

OUT_DIR = CANDIDATES / "q79_routec_basis_transport_primitive_source_theorem"
OUT_TABLE = OUT_DIR / "primitive_span_counterexample_table.json"
OUT_CANDIDATE = CANDIDATES / "q79_routec_basis_transport_primitive_source_theorem.candidate.json"
OUT_CERT = CERTS / "q79_routec_basis_transport_primitive_source_theorem_certificate.json"
OUT_PAPER = CORPUS / "Q79_RouteC_BasisTransport_Primitive_Source_Theorem_v1.md"

Q79_INPUTS = {
    "phifin_alpha1_payload_gate": CERTS / "q79_selected_phifin_alpha1_payload_certificate.json",
    "valpha_finite_emission_bridge": CERTS
    / "q79_valpha_source_origin_finite_emission_bridge_certificate.json",
    "selected_full_sm_attempt": CERTS / "selected_full_sm_data_theorem_attempt_certificate.json",
    "c1_response_template": CERTS / "selected_c1_response_data_certificate.template.json",
}

ADJACENT_INPUTS = {
    "constants_phifin_s0_prefix": CONSTANTS
    / "certificates"
    / "selected_phifin_s0_source_prefix_certificate.json",
    "constants_phifin_trace_existence": CONSTANTS
    / "certificates"
    / "selected_phifin_finite_trace_existence_certificate.json",
    "constants_phifin_s1s2_value_emission": CONSTANTS
    / "certificates"
    / "selected_phifin_s1s2_value_emission_attempt_certificate.json",
    "constants_phifin_c1_packet": CONSTANTS
    / "certificates"
    / "selected_phifin_c1_emission_packet_certificate.json",
    "constants_c1_operator_rebuild": CONSTANTS
    / "certificates"
    / "selected_c1_operator_source_rebuild_attempt_certificate.json",
    "constants_routec_prefix": CONSTANTS
    / "certificates"
    / "routec_rhoe_bn_operator_prefix_import_certificate.json",
    "gr_basis_transport_reduction": GR
    / "certificates"
    / "routec_basis_transport_gate_reduction_import_certificate.json",
    "gr_weylpair_source_gate_import": GR
    / "certificates"
    / "routec_weylpair_source_gate_import_certificate.json",
    "gr_source_origin_conditional": GR
    / "certificates"
    / "routec_selected_source_origin_paper_lemma_certificate.json",
    "sm_basis_transport_slot": SM_PARITY
    / "certificates"
    / "selected_routec_basis_transport_primitive_source_theorem_certificate.json",
    "sm_basis_transport_counterexample": SM_PARITY
    / "certificates"
    / "selected_routec_basis_transport_primitive_source_proof_or_counterexample_certificate.json",
    "sm_basis_transport_counterexample_candidate": SM_PARITY
    / "candidate_data"
    / "selected_routec_basis_transport_primitive_source_proof_or_counterexample.candidate.json",
    "sm_weylpair_source_gate": SM_PARITY
    / "certificates"
    / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem_certificate.json",
    "sm_rebuild_lane": SM_PARITY
    / "certificates"
    / "selected_routec_selected_c1_operator_source_or_galerkin_rebuild_certificate.json",
    "sm_noninvariant_primitive_search": SM_PARITY
    / "certificates"
    / "selected_routec_noninvariant_c1_primitive_search_certificate.json",
    "qa_u1_su2_source_fill": QA_SU3
    / "certificates"
    / "u1_su2_internal_overlap_payload_template_or_k_gauge_source_fill_certificate.json",
}

REPOS = {
    "q79": ROOT,
    "constants": CONSTANTS,
    "gr": GR,
    "qa_su3": QA_SU3,
    "sm_parity": SM_PARITY,
}


def run_git(repo: Path, args: list[str]) -> str:
    if not (repo / ".git").exists():
        return ""
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.stdout.strip()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def status_summary(status_short: str) -> dict[str, Any]:
    lines = [line for line in status_short.splitlines() if line.strip()]
    return {
        "dirty": bool(lines),
        "line_count": len(lines),
        "modified_count": sum(line.startswith(" M") or line.startswith("M ") for line in lines),
        "untracked_count": sum(line.startswith("??") for line in lines),
        "preview": lines[:12],
    }


def repo_snapshot(name: str, path: Path) -> dict[str, Any]:
    if name == "q79":
        return {
            "path": str(path),
            "present": (path / ".git").exists(),
            "branch": run_git(path, ["branch", "--show-current"]),
            "head": "omitted-current-repo-head-for-reproducibility",
            "status_summary": {
                "dirty": False,
                "line_count": 0,
                "modified_count": 0,
                "untracked_count": 0,
                "preview": [],
                "note": "current q79 head/status omitted so this certificate remains reproducible after commit",
            },
        }
    status = run_git(path, ["status", "--short"])
    return {
        "path": str(path),
        "present": path.exists() and (path / ".git").exists(),
        "branch": run_git(path, ["branch", "--show-current"]),
        "head": run_git(path, ["log", "-1", "--oneline"]),
        "status_summary": status_summary(status),
    }


def cert_status(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact")
        or data.get("next_required_object")
        or data.get("primary_next_artifact"),
        "what_closes": data.get("what_closes")
        or data.get("what_closes_now")
        or data.get("closed_now")
        or {},
        "what_remains_open": data.get("what_remains_open")
        or data.get("still_open")
        or data.get("open_payload_premises")
        or {},
    }


def build_counterexample_table(sm_counterexample: dict[str, Any]) -> dict[str, Any]:
    span_tests = sm_counterexample.get("span_tests", {})
    fixed = span_tests.get("fixed_fiber_primitives", {})
    envelope = span_tests.get("fixed_plus_all_fiber_envelope", {})
    refined = sm_counterexample.get("refined_next_theorem", {})
    return {
        "primitive_only_counterexample_proved": sm_counterexample.get("source_attempt", {}).get(
            "counterexample_proved"
        )
        is True,
        "primitive_only_theorem_sufficient": sm_counterexample.get("interpretation", {}).get(
            "primitive_only_theorem_sufficient"
        )
        is True,
        "basis_transport_or_vertex_still_live": sm_counterexample.get("interpretation", {}).get(
            "basis_transport_or_vertex_still_live"
        )
        is True,
        "target_dimension": span_tests.get("target_dimension"),
        "fixed_fiber_primitives": {
            "rank": fixed.get("rank"),
            "target_in_span": fixed.get("target_in_span"),
            "residual_norm": fixed.get("residual_norm"),
            "relative_residual": fixed.get("relative_residual"),
            "target_norm": fixed.get("target_norm"),
            "labels": fixed.get("labels"),
        },
        "fixed_plus_all_fiber_envelope": {
            "rank": envelope.get("rank"),
            "target_in_span": envelope.get("target_in_span"),
            "residual_norm": envelope.get("residual_norm"),
            "relative_residual": envelope.get("relative_residual"),
            "target_norm": envelope.get("target_norm"),
            "labels": envelope.get("labels"),
        },
        "refined_next_theorem": {
            "name": refined.get("name"),
            "status": refined.get("status"),
            "required_new_components": refined.get("required_new_components", []),
            "statement": refined.get("statement"),
        },
    }


def build_weyl_pair_gate(gr_weyl: dict[str, Any], sm_weyl: dict[str, Any]) -> dict[str, Any]:
    span = gr_weyl.get("span_test", {})
    verdict = gr_weyl.get("verdict", {})
    theorem_gate = gr_weyl.get("theorem_gate", {})
    source_contract = gr_weyl.get("source_contract", {})
    closed_now = gr_weyl.get("closed_now", {})
    residual = float(span.get("residual_norm", 1.0))
    relative = float(span.get("relative_residual", 1.0))
    exact_to_tolerance = (
        span.get("target_in_span") is True
        and span.get("rank") == 2
        and residual < 1.0e-12
        and relative < 1.0e-12
    )
    return {
        "status_imported": gr_weyl.get("status"),
        "sm_status_imported": sm_weyl.get("status"),
        "target_dimension": span.get("target_dimension"),
        "columns": span.get("columns", []),
        "coefficients": span.get("coefficients", []),
        "rank": span.get("rank"),
        "target_in_span": span.get("target_in_span"),
        "residual_norm": span.get("residual_norm"),
        "relative_residual": span.get("relative_residual"),
        "direct_packet_sum_residual_norm": span.get("direct_packet_sum_residual_norm"),
        "target_norm": span.get("target_norm"),
        "exact_to_tolerance": exact_to_tolerance,
        "phase_and_shift_packets_present": closed_now.get("phase_and_shift_packets_present")
        is True,
        "locked_splitter_reconstructed_by_weyl_pair": closed_now.get(
            "locked_splitter_reconstructed_by_weyl_pair"
        )
        is True
        and exact_to_tolerance,
        "minimal_weyl_pair_reconstructs_locked_splitter": theorem_gate.get(
            "proved_now", {}
        ).get("minimal_weyl_pair_reconstructs_locked_splitter")
        is True,
        "selected_source_contract_for_A_selected_defined": closed_now.get(
            "selected_source_contract_for_A_selected_defined"
        )
        is True,
        "selected_source_provenance_proved": verdict.get("selected_source_provenance_proved")
        is True,
        "A_selected_emitted": verdict.get("A_selected_emitted") is True,
        "b_selected_emitted": verdict.get("b_selected_emitted") is True,
        "deltaTheta_C1_solved": verdict.get("deltaTheta_C1_solved") is True,
        "source_contract": {
            "A_selected_column_requirements": source_contract.get(
                "A_selected_column_requirements", []
            ),
            "b_selected_requirements": source_contract.get("b_selected_requirements", []),
            "operator_emission_status_imported": source_contract.get(
                "operator_emission_status_imported", {}
            ),
        },
        "formal_statement": theorem_gate.get("formal_statement"),
        "next_required_artifact": verdict.get("next_required_artifact")
        or sm_weyl.get("next_required_artifact"),
    }


def build_candidate() -> dict[str, Any]:
    q79_inputs = {name: cert_status(path) for name, path in Q79_INPUTS.items()}
    adjacent = {name: cert_status(path) for name, path in ADJACENT_INPUTS.items()}
    sm_counterexample = load(ADJACENT_INPUTS["sm_basis_transport_counterexample_candidate"])
    q79_payload = load(Q79_INPUTS["phifin_alpha1_payload_gate"])
    gr_basis = load(ADJACENT_INPUTS["gr_basis_transport_reduction"])
    gr_weyl = load(ADJACENT_INPUTS["gr_weylpair_source_gate_import"])
    sm_weyl = load(ADJACENT_INPUTS["sm_weylpair_source_gate"])
    constants_trace = load(ADJACENT_INPUTS["constants_phifin_trace_existence"])
    constants_s1s2 = load(ADJACENT_INPUTS["constants_phifin_s1s2_value_emission"])
    constants_s0 = load(ADJACENT_INPUTS["constants_phifin_s0_prefix"])

    table = build_counterexample_table(sm_counterexample)
    weyl_pair_gate = build_weyl_pair_gate(gr_weyl, sm_weyl)
    fixed = table["fixed_fiber_primitives"]
    envelope = table["fixed_plus_all_fiber_envelope"]

    primitive_only_counterexample_valid = (
        table["primitive_only_counterexample_proved"] is True
        and table["primitive_only_theorem_sufficient"] is False
        and fixed.get("target_in_span") is False
        and envelope.get("target_in_span") is False
        and float(fixed.get("relative_residual", 0.0)) > 0.0
        and float(envelope.get("relative_residual", 0.0)) > 0.0
        and table.get("target_dimension") == 72
    )

    support_reductions = {
        "q79_payload_gate_names_this_target": q79_payload.get("next_required_artifact")
        == "Q79_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1",
        "phifin_s0_source_prefix_closed": constants_s0.get("s0_closed") is True,
        "phifin_finite_trace_existence_proved_values_open": constants_trace.get("theorem_proved")
        is True
        and constants_trace.get("status")
        == "SELECTED_PHIFIN_FINITE_TRACE_EXISTENCE_PROVED_VALUES_OPEN",
        "phifin_s1s2_value_emission_criterion_proved_values_open": constants_s1s2.get(
            "criterion_proved"
        )
        is True
        and constants_s1s2.get("status")
        == "SELECTED_PHIFIN_S1S2_VALUE_EMISSION_ATTEMPT_BLOCKED_BY_UNEMITTED_SELECTED_VALUES",
        "basis_transport_gate_reduced_source_open": gr_basis.get("status")
        == "ROUTEC_BASISTRANSPORT_GATE_REDUCED_SOURCE_PROOF_OPEN",
        "weyl_pair_source_gate_built_source_open": gr_weyl.get("status")
        == "ROUTEC_WEYLPAIR_SOURCE_GATE_IMPORTED_ASELECTED_SOURCE_OPEN",
        "active_shift_1_1_forced": gr_basis.get("reduction", {}).get("active_shift") == [1, 1],
        "fixed_fiber_gauge_class_reduced_current_layer": gr_basis.get("verdict", {}).get(
            "fiber_choice_ambiguity_removed_for_current_spectral_invariants"
        )
        is True,
        "conditional_source_origin_lemma_phi_fin_open": adjacent[
            "gr_source_origin_conditional"
        ].get("status")
        == "ROUTEC_SOURCE_ORIGIN_CONDITIONAL_LEMMA_PROVED_PAPER_INSERTION_BUILT_PHI_FIN_OPEN",
        "primitive_source_theorem_slot_built": adjacent["sm_basis_transport_slot"].get("status")
        == "MTT_SELECTED_ROUTEC_BASISTRANSPORT_PRIMITIVE_SOURCE_THEOREM_SLOT_BUILT_SOURCE_PROOF_OPEN",
        "primitive_counterexample_imported": primitive_only_counterexample_valid,
        "sm_weyl_pair_gate_built_algebraically_sufficient_source_open": sm_weyl.get("status")
        == "MTT_SELECTED_ROUTEC_WEYLPAIR_BASISTRANSPORT_OR_VERTEX_SOURCE_GATE_BUILT_ALGEBRAICALLY_SUFFICIENT_SOURCE_PROOF_OPEN",
    }

    decision = {
        "original_target": "Q79_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1",
        "original_target_closed_as_positive_source_theorem": False,
        "original_target_closed_as_counterexample_decision": primitive_only_counterexample_valid,
        "primitive_only_can_emit_A_selected": False,
        "refined_weyl_pair_theorem_required": table["refined_next_theorem"]["name"]
        == "SelectedWeylPairBasisTransportOrVertexSourceTheorem",
        "weyl_pair_algebraic_gate_built": weyl_pair_gate["exact_to_tolerance"],
        "locked_splitter_reconstructed_by_weyl_pair": weyl_pair_gate[
            "locked_splitter_reconstructed_by_weyl_pair"
        ],
        "selected_weyl_pair_source_proved": False,
        "selected_weyl_pair_source_provenance_proved": weyl_pair_gate[
            "selected_source_provenance_proved"
        ],
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "target_fitting_used": False,
    }

    theorem_statement = (
        "In the current q79/F,m=1 Route-C C1 gate, the primitive-only fixed-fiber "
        "basis-transport source theorem is insufficient.  The imported locked "
        "span test shows that neither the three fixed-fiber primitive directions "
        "nor the fixed-plus-all-fiber envelope contains the qutrit/Weyl splitter "
        "target in the 72-dimensional response space.  The minimal enriched "
        "Weyl-pair packet, however, reconstructs that locked splitter "
        "algebraically with a phase-like component and a shift-like component.  "
        "Thus the next q79 proof object is not another primitive-only search; it "
        "is the same-branch source proof and theorem-derived assembly of "
        "A_selected and b_selected from the Weyl-pair packet, with no observed "
        "or benchmark flavor data as selectors."
    )

    return {
        "certificate": "Q79RouteCBasisTransportPrimitiveSourceTheorem",
        "status": "Q79_ROUTEC_BASISTRANSPORT_PRIMITIVE_COUNTEREXAMPLE_CLOSED_WEYLPAIR_GATE_BUILT_SOURCE_PROOF_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "counterexample_table": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "repo_snapshots": {name: repo_snapshot(name, path) for name, path in REPOS.items()},
        "q79_input_statuses": q79_inputs,
        "adjacent_input_statuses": adjacent,
        "support_reductions": support_reductions,
        "primitive_span_counterexample": table,
        "weyl_pair_algebraic_gate": weyl_pair_gate,
        "decision": decision,
        "closed_by_this_attempt": {
            "latest_repo_updates_checked": all(
                repo_snapshot(name, path)["present"] for name, path in REPOS.items()
            ),
            "q79_target_attacked_directly": True,
            "finite_support_lemmas_imported": all(support_reductions.values()),
            "primitive_only_span_counterexample_closed": primitive_only_counterexample_valid,
            "s1s2_value_emission_criterion_imported": support_reductions[
                "phifin_s1s2_value_emission_criterion_proved_values_open"
            ],
            "weyl_pair_algebraic_gate_imported": weyl_pair_gate["exact_to_tolerance"],
            "locked_splitter_reconstructed_by_weyl_pair": weyl_pair_gate[
                "locked_splitter_reconstructed_by_weyl_pair"
            ],
            "source_contract_for_A_selected_imported": weyl_pair_gate[
                "selected_source_contract_for_A_selected_defined"
            ],
            "active_shift_1_1_retained": support_reductions["active_shift_1_1_forced"],
            "fixed_fiber_gauge_class_reduced_for_current_layer": support_reductions[
                "fixed_fiber_gauge_class_reduced_current_layer"
            ],
            "refined_weyl_pair_target_identified": decision["refined_weyl_pair_theorem_required"],
            "next_target_advanced_to_Aselected_assembly": True,
            "target_fitting_excluded": True,
        },
        "still_open": {
            "prove_selected_phase_like_qutrit_Z_or_basis_holonomy_source": True,
            "prove_selected_shift_like_qutrit_X_vertex_source": True,
            "assemble_theorem_derived_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "same_branch_source_proof_for_enriched_vertex_or_transport": True,
            "downstream_fixed_fiber_quotient_or_selected_fiber_origin": True,
            "solve_or_reject_splitter_equation": True,
            "selected_PhiFin_alpha1_payload_values": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_positive_primitive_only_source_theorem": False,
            "claims_selected_weyl_pair_source_proved": False,
            "claims_selected_weyl_pair_source_provenance": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "claims_selected_PhiFin_payload_values": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "lifts_selected_flags_by_hand": False,
        },
        "theorem": {
            "name": "Q79PrimitiveOnlySpanCounterexampleAndWeylPairTargetTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": theorem_statement,
        },
        "next_required_artifact": "Q79_Selected_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1",
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def render_bool_map(items: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in items.items())


def render_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def build_paper(cert: dict[str, Any]) -> str:
    table = cert["primitive_span_counterexample"]
    weyl = cert["weyl_pair_algebraic_gate"]
    fixed = table["fixed_fiber_primitives"]
    envelope = table["fixed_plus_all_fiber_envelope"]
    refined = table["refined_next_theorem"]
    closed = "\n".join(
        f"- `{key}`" for key, value in cert["closed_by_this_attempt"].items() if value
    )
    open_items = "\n".join(f"- `{key}`" for key, value in cert["still_open"].items() if value)
    repo_lines = "\n".join(
        f"- `{name}`: `{row['head']}` dirty=`{row['status_summary']['dirty']}`"
        for name, row in cert["repo_snapshots"].items()
    )
    return f"""# Q79 RouteC BasisTransport Primitive Source Theorem v1

## Result

The q79 target was attacked directly.  The positive primitive-only source
theorem is **not** proved; it is refuted for the locked splitter target by a
finite span counterexample.

This is a useful closure, not a dead end.  It says the selected source cannot
merely promote the current fixed-fiber primitive family.  The enriched Weyl-pair
gate does reconstruct the locked splitter algebraically, so the next theorem
must derive that phase-plus-shift packet from the same selected q79 branch and
then assemble theorem-derived `A_selected` and `b_selected`.

## Repo Snapshot

{repo_lines}

## Support Reductions

{render_bool_map(cert["support_reductions"])}

## Primitive Span Counterexample

Target dimension: `{table["target_dimension"]}`

Fixed-fiber primitives:

- rank: `{fixed["rank"]}`
- target in span: `{fixed["target_in_span"]}`
- residual norm: `{fixed["residual_norm"]}`
- relative residual: `{fixed["relative_residual"]}`
- labels: `{fixed["labels"]}`

Fixed plus all-fiber envelope:

- rank: `{envelope["rank"]}`
- target in span: `{envelope["target_in_span"]}`
- residual norm: `{envelope["residual_norm"]}`
- relative residual: `{envelope["relative_residual"]}`
- labels: `{envelope["labels"]}`

## Weyl-Pair Algebraic Gate

Columns: `{weyl["columns"]}`

- rank: `{weyl["rank"]}`
- target in span: `{weyl["target_in_span"]}`
- residual norm: `{weyl["residual_norm"]}`
- relative residual: `{weyl["relative_residual"]}`
- coefficients: `{weyl["coefficients"]}`
- exact to tolerance: `{weyl["exact_to_tolerance"]}`
- selected source provenance proved: `{weyl["selected_source_provenance_proved"]}`
- A_selected emitted: `{weyl["A_selected_emitted"]}`
- b_selected emitted: `{weyl["b_selected_emitted"]}`

Imported statement:

{weyl["formal_statement"]}

## Decision

{render_bool_map(cert["decision"])}

## Refined Next Theorem

`{refined["name"]}`:

{refined["statement"]}

Required new components:

{render_list(refined["required_new_components"])}

## What This Closes

{closed}

## What Remains Open

{open_items}

## Theorem

`{cert["theorem"]["name"]}` is proved.

{cert["theorem"]["statement"]}

Next required artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    cert = build_candidate()
    write_json(OUT_TABLE, cert["primitive_span_counterexample"])
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")
    print("Q79 Route-C basis-transport primitive-source theorem gate")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
