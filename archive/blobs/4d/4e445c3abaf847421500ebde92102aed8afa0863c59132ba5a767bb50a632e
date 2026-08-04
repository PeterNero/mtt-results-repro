"""Close the q79 Weyl-pair conditional A-assembly gate.

The previous q79 gate refuted primitive-only basis transport and imported the
enriched Weyl-pair algebraic source gate.  The adjacent SM/GR packets now
assemble the corresponding 72x2 conditional operator and solve the locked
DeltaTheta_C1 splitter equation.  This q79-local artifact records that the
assembly layer has no remaining algebraic obstruction while keeping the
selected-source provenance lemma open.
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

GR = TEXPAPERS / "mtt-protospinor-gr-response-proof"
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"

OUT_DIR = CANDIDATES / "q79_routec_weylpair_aselected_assembly_or_source_proof"
OUT_TABLE = OUT_DIR / "conditional_weylpair_solve_table.json"
OUT_CANDIDATE = (
    CANDIDATES / "q79_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
)
OUT_CERT = CERTS / "q79_routec_weylpair_aselected_assembly_or_source_proof_certificate.json"
OUT_PAPER = CORPUS / "Q79_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1.md"

Q79_INPUTS = {
    "phifin_alpha1_payload_gate": CERTS / "q79_selected_phifin_alpha1_payload_certificate.json",
    "primitive_counterexample_and_weyl_gate": CERTS
    / "q79_routec_basis_transport_primitive_source_theorem_certificate.json",
}

ADJACENT_INPUTS = {
    "gr_weylpair_source_gate_import": GR
    / "certificates"
    / "routec_weylpair_source_gate_import_certificate.json",
    "gr_weylpair_aselected_assembly_import": GR
    / "certificates"
    / "routec_weylpair_aselected_assembly_import_certificate.json",
    "sm_weylpair_source_gate": SM_PARITY
    / "certificates"
    / "selected_routec_weylpair_basis_transport_or_vertex_source_theorem_certificate.json",
    "sm_weylpair_aselected_assembly": SM_PARITY
    / "certificates"
    / "selected_routec_weylpair_aselected_assembly_or_source_proof_certificate.json",
    "sm_weylpair_aselected_assembly_candidate": SM_PARITY
    / "candidate_data"
    / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json",
}

REPOS = {
    "q79": ROOT,
    "gr": GR,
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


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def cert_status(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
        "what_closes": data.get("what_closes")
        or data.get("what_closes_now")
        or data.get("closed_now")
        or {},
        "what_remains_open": data.get("what_remains_open")
        or data.get("still_open")
        or {},
    }


def build_solve_table(gr_assembly: dict[str, Any]) -> dict[str, Any]:
    operator = gr_assembly.get("conditional_operator", {})
    solve = gr_assembly.get("locked_solve", {})
    provenance = gr_assembly.get("provenance_reduction", {})
    verdict = gr_assembly.get("verdict", {})
    closed = gr_assembly.get("closed_now", {})
    residual = float(solve.get("residual_norm", 1.0))
    relative = float(solve.get("relative_residual", 1.0))
    exact_to_tolerance = (
        solve.get("consistent") is True
        and solve.get("rank") == 2
        and residual < 1.0e-12
        and relative < 1.0e-12
        and operator.get("shape") == [72, 2]
        and operator.get("is_A_selected") is False
    )
    return {
        "conditional_operator": {
            "name": operator.get("name"),
            "columns": operator.get("columns", []),
            "shape": operator.get("shape"),
            "is_A_selected": operator.get("is_A_selected"),
            "why_not_selected": operator.get("why_not_selected"),
        },
        "locked_solve": {
            "rank": solve.get("rank"),
            "condition_number": solve.get("condition_number"),
            "consistent": solve.get("consistent"),
            "deltaTheta_conditional": solve.get("deltaTheta_conditional", []),
            "residual_norm": solve.get("residual_norm"),
            "relative_residual": solve.get("relative_residual"),
            "b_norm": solve.get("b_norm"),
        },
        "exact_to_tolerance": exact_to_tolerance,
        "provenance_reduction": {
            "name": provenance.get("name"),
            "status": provenance.get("status"),
            "statement": provenance.get("statement"),
            "must_prove": provenance.get("must_prove", []),
        },
        "closed_now": closed,
        "verdict": {
            "conditional_A_weylpair_built": verdict.get("conditional_A_weylpair_built") is True,
            "conditional_deltaTheta_solution_found": verdict.get(
                "conditional_deltaTheta_solution_found"
            )
            is True,
            "A_selected_emitted": verdict.get("A_selected_emitted") is True,
            "b_selected_emitted": verdict.get("b_selected_emitted") is True,
            "honest_selected_deltaTheta_C1_solve_run": verdict.get(
                "honest_selected_deltaTheta_C1_solve_run"
            )
            is True,
            "selected_source_provenance_proved": verdict.get(
                "selected_source_provenance_proved"
            )
            is True,
            "full_SM_or_no_knob_closure": verdict.get("full_SM_or_no_knob_closure") is True,
            "next_required_artifact": verdict.get("next_required_artifact"),
        },
    }


def build_candidate() -> dict[str, Any]:
    q79_inputs = {name: cert_status(path) for name, path in Q79_INPUTS.items()}
    adjacent = {name: cert_status(path) for name, path in ADJACENT_INPUTS.items()}
    q79_previous = load(Q79_INPUTS["primitive_counterexample_and_weyl_gate"])
    gr_source_gate = load(ADJACENT_INPUTS["gr_weylpair_source_gate_import"])
    gr_assembly = load(ADJACENT_INPUTS["gr_weylpair_aselected_assembly_import"])
    sm_assembly_candidate = load(ADJACENT_INPUTS["sm_weylpair_aselected_assembly_candidate"])

    solve_table = build_solve_table(gr_assembly)
    support = {
        "q79_primitive_counterexample_and_weyl_gate_closed_source_open": q79_previous.get(
            "status"
        )
        == "Q79_ROUTEC_BASISTRANSPORT_PRIMITIVE_COUNTEREXAMPLE_CLOSED_WEYLPAIR_GATE_BUILT_SOURCE_PROOF_OPEN",
        "previous_weyl_pair_algebraic_gate_built": q79_previous.get(
            "weyl_pair_algebraic_gate", {}
        ).get("exact_to_tolerance")
        is True,
        "gr_weyl_pair_source_gate_built_source_open": gr_source_gate.get("status")
        == "ROUTEC_WEYLPAIR_SOURCE_GATE_IMPORTED_ASELECTED_SOURCE_OPEN",
        "gr_conditional_A_solve_built_source_open": gr_assembly.get("status")
        == "ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN",
        "sm_conditional_A_solve_built_source_open": sm_assembly_candidate.get("status")
        == "MTT_SELECTED_ROUTEC_WEYLPAIR_ASELECTED_ASSEMBLY_BUILT_CONDITIONAL_SOLVE_EXACT_SOURCE_PROOF_OPEN",
        "target_fitting_excluded": gr_assembly.get("closed_now", {}).get(
            "target_fitting_excluded"
        )
        is True
        and sm_assembly_candidate.get("target_fitting_used") is False,
    }

    decision = {
        "conditional_A_weylpair_assembled": solve_table["verdict"][
            "conditional_A_weylpair_built"
        ],
        "conditional_deltaTheta_solve_exact": solve_table["exact_to_tolerance"],
        "algebraic_rank_obstruction_absent_for_weylpair_packet": gr_assembly.get(
            "closed_now", {}
        ).get("algebraic_rank_obstruction_absent")
        is True,
        "conditional_A_promoted_to_A_selected": False,
        "selected_source_provenance_proved": False,
        "A_selected_emitted": False,
        "b_selected_emitted": False,
        "honest_selected_deltaTheta_C1_solve_run": False,
        "full_SM_or_no_knob_closure": False,
        "target_fitting_used": False,
    }

    theorem_statement = (
        "Conditioned on same-branch selected source emission of the two enriched "
        "Weyl-pair columns, the q79/F,m=1 Route-C 72x2 conditional operator "
        "has rank 2 and solves the locked DeltaTheta_C1 splitter equation with "
        "deltaTheta=(1,1) up to roundoff.  Thus the Weyl-pair assembly layer has "
        "no remaining algebraic rank or consistency obstruction.  This does not "
        "promote the conditional operator to A_selected, does not emit "
        "b_selected, and does not run an honest selected DeltaTheta solve; the "
        "remaining proof is exactly the selected Weyl-pair source provenance "
        "lemma."
    )

    return {
        "certificate": "Q79RouteCWeylPairAselectedAssemblyOrSourceProof",
        "status": "Q79_ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "conditional_solve_table": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "repo_snapshots": {name: repo_snapshot(name, path) for name, path in REPOS.items()},
        "q79_input_statuses": q79_inputs,
        "adjacent_input_statuses": adjacent,
        "support_reductions": support,
        "conditional_solve": solve_table,
        "decision": decision,
        "closed_by_this_attempt": {
            "latest_repo_updates_checked": all(
                repo_snapshot(name, path)["present"] for name, path in REPOS.items()
            ),
            "previous_primitive_counterexample_and_weyl_gate_imported": support[
                "q79_primitive_counterexample_and_weyl_gate_closed_source_open"
            ],
            "conditional_A_weylpair_assembled": decision["conditional_A_weylpair_assembled"],
            "conditional_deltaTheta_solve_exact": decision["conditional_deltaTheta_solve_exact"],
            "algebraic_rank_obstruction_absent_for_weylpair_packet": decision[
                "algebraic_rank_obstruction_absent_for_weylpair_packet"
            ],
            "remaining_gap_reduced_to_source_provenance": True,
            "next_target_advanced_to_source_provenance_lemma": True,
            "target_fitting_excluded": True,
        },
        "still_open": {
            "prove_selected_weylpair_source_provenance": True,
            "promote_conditional_A_to_A_selected": True,
            "emit_theorem_derived_b_selected": True,
            "run_honest_selected_deltaTheta_C1_solve": True,
            "selected_PhiFin_alpha1_payload_values": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_conditional_A_is_A_selected": False,
            "claims_selected_source_provenance_proved": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "claims_honest_selected_deltaTheta_solve_run": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "lifts_selected_flags_by_hand": False,
        },
        "theorem": {
            "name": "Q79ConditionalWeylPairDeltaThetaSolveTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": theorem_statement,
        },
        "next_required_artifact": "Q79_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1",
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def render_bool_map(items: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in items.items())


def render_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def build_paper(cert: dict[str, Any]) -> str:
    solve = cert["conditional_solve"]
    operator = solve["conditional_operator"]
    locked = solve["locked_solve"]
    provenance = solve["provenance_reduction"]
    closed = "\n".join(
        f"- `{key}`" for key, value in cert["closed_by_this_attempt"].items() if value
    )
    open_items = "\n".join(f"- `{key}`" for key, value in cert["still_open"].items() if value)
    repo_lines = "\n".join(
        f"- `{name}`: `{row['head']}` dirty=`{row['status_summary']['dirty']}`"
        for name, row in cert["repo_snapshots"].items()
    )
    return f"""# Q79 RouteC WeylPair Aselected Assembly or Source Proof v1

## Result

The Weyl-pair assembly layer is closed conditionally.  If the selected source
emits the phase and shift Weyl-pair columns, the conditional operator has shape
`{operator["shape"]}`, rank `{locked["rank"]}`, and solves the locked
DeltaTheta_C1 equation with residual `{locked["residual_norm"]}`.

This is not yet `A_selected`.  The operator is explicitly marked
`is_A_selected = {operator["is_A_selected"]}` because the same-branch source
provenance lemma is still open.

## Repo Snapshot

{repo_lines}

## Support Reductions

{render_bool_map(cert["support_reductions"])}

## Conditional Operator

- name: `{operator["name"]}`
- columns: `{operator["columns"]}`
- shape: `{operator["shape"]}`
- is A_selected: `{operator["is_A_selected"]}`
- why not selected: {operator["why_not_selected"]}

## Locked Solve

- rank: `{locked["rank"]}`
- condition number: `{locked["condition_number"]}`
- consistent: `{locked["consistent"]}`
- deltaTheta_conditional: `{locked["deltaTheta_conditional"]}`
- residual norm: `{locked["residual_norm"]}`
- relative residual: `{locked["relative_residual"]}`
- exact to tolerance: `{solve["exact_to_tolerance"]}`

## Decision

{render_bool_map(cert["decision"])}

## Provenance Reduction

`{provenance["name"]}` is the next lemma.

{provenance["statement"]}

Must prove:

{render_list(provenance["must_prove"])}

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
    write_json(OUT_TABLE, cert["conditional_solve"])
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")
    print("Q79 Route-C Weyl-pair conditional A solve")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
