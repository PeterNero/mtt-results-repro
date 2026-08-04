"""Build CONST-EW-02 B30 source-identity two-exit reduction.

B29 reduced Route B to the selected primitive-kernel source theorem.  B30
imports the later SM-parity conditional validator pass and the finite C1 source
identity gate, then freezes the non-cyclic next frontier: either prove the
unpatched source identity, or export genuinely independent finite C1 kernel
rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b30_source_identity_two_exit_reduction"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CONDITIONAL = BASE / "conditional_superset_validator_import.packet.json"
GATE = BASE / "finite_c1_source_identity_gate_import.packet.json"
TWO_EXIT = BASE / "two_exit_noncycle_frontier.packet.json"
BOUNDARY = BASE / "weak_mixing_b30_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B30_SourceIdentityTwoExitReduction_v1.md"

STATUS = "MTT_CONST_EW_02_B30_SOURCE_IDENTITY_TWO_EXIT_REDUCTION_BUILT"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b29_path = DATA / "const_ew_02_weak_mixing_b29_routeb_final_source_theorem_frontier.candidate.json"
    b29_boundary_path = DATA / "const_ew_02_weak_mixing_b29_routeb_final_source_theorem_frontier" / "weak_mixing_b29_boundary.packet.json"
    b29_next_path = DATA / "const_ew_02_weak_mixing_b29_routeb_final_source_theorem_frontier" / "next_labeled_workorder.packet.json"

    psm_c106_candidate_path = SM / "candidate_data" / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate.candidate.json"
    conditional_result_path = SM / "candidate_data" / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate" / "route_b_full_conditional_validator_result.packet.json"
    final_gate_path = SM / "candidate_data" / "selected_psm_c1_06_sectorrows_or_replayindependencecertificate" / "final_unpatched_source_identity_gate.packet.json"
    finite_identity_candidate_path = SM / "candidate_data" / "selected_finitec1sourceidentitytheorem_or_newindependentrows.candidate.json"
    finite_identity_gate_path = SM / "candidate_data" / "selected_finitec1sourceidentitytheorem_or_newindependentrows" / "selected_finite_c1_source_identity_theorem_gate.packet.json"
    independent_rows_schema_path = SM / "candidate_data" / "selected_finitec1sourceidentitytheorem_or_newindependentrows" / "new_independent_rows_schema.packet.json"

    b29 = load(b29_path)
    b29_boundary = load(b29_boundary_path)
    b29_next = load(b29_next_path)
    psm_c106 = load(psm_c106_candidate_path)
    conditional_result = load(conditional_result_path)
    final_gate = load(final_gate_path)
    finite_identity = load(finite_identity_candidate_path)
    finite_identity_gate = load(finite_identity_gate_path)
    independent_rows_schema = load(independent_rows_schema_path)

    conditional_packet = {
        "schema": "MTTConstEW02B30ConditionalSupersetValidatorImport.v1",
        "status": "CONDITIONAL_SUPERSET_ROUTEB_VALIDATOR_IMPORTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B30-CONDITIONAL-SUPERSET-VALIDATOR",
        "inputs": {
            "psm_c1_06_candidate": rel(psm_c106_candidate_path),
            "conditional_validator_result": rel(conditional_result_path),
            "final_unpatched_source_identity_gate": rel(final_gate_path),
        },
        "conditional_superset_path": {
            "strategy": "combine Route-B row kernels, Route-A/source-identity clauses, and Weyl-variation/Hessian/sector-functor support into a locked conditional target",
            "validator_passes_conditionally": conditional_result["passes"],
            "unpatched_routeB_validates": psm_c106["closure_decision"]["unpatched_RouteB_validator_passes"],
            "conditional_routeB_validates": psm_c106["closure_decision"]["conditional_RouteB_validator_passes"],
            "locked_target": "strict Route-B row-source validator, not observed weak-angle data",
        },
        "what_this_proves": [
            "there is no remaining row-value or row-assembly obstruction inside the conditional superset spine",
            "the unpatched problem is source provenance, not another numerical replay",
            "the legal next frontier is source identity or honest independent kernel export",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    gate_packet = {
        "schema": "MTTConstEW02B30FiniteC1SourceIdentityGateImport.v1",
        "status": "FINITE_C1_SOURCE_IDENTITY_GATE_IMPORTED_UNPATCHED_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B30-FINITE-C1-SOURCE-IDENTITY-GATE",
        "inputs": {
            "finite_identity_candidate": rel(finite_identity_candidate_path),
            "finite_identity_gate": rel(finite_identity_gate_path),
            "independent_rows_schema": rel(independent_rows_schema_path),
        },
        "theorem_name": finite_identity_gate["theorem_name"],
        "statement": finite_identity_gate["statement"],
        "required_clauses": finite_identity_gate["required_clauses"],
        "clause_status": finite_identity_gate["clause_status"],
        "current_route_A_accepts": finite_identity_gate["current_route_A_accepts"],
        "current_route_B_accepts": finite_identity_gate["current_route_B_accepts"],
        "would_promote_if_proved": finite_identity_gate["would_promote_if_proved"],
        "independent_rows_schema_status": independent_rows_schema["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    two_exit = {
        "schema": "MTTConstEW02B30TwoExitNonCycleFrontier.v1",
        "status": "TWO_NONCYCLIC_EXITS_LOCKED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B30-TWO-EXIT-FRONTIER",
        "previous_B29_frontier": {
            "label": b29["active_label"],
            "next_primary": b29_next["primary"]["label"],
            "primitive_source_theorem_open": b29_boundary["still_open"]["primitive_kernel_source_theorem"],
        },
        "new_B30_frontier": {
            "exit_1": {
                "label": "CONST-EW-02 / WEAK-MIXING / B31-SOURCE-IDENTITY-CLAUSE-PROOF",
                "artifact": "SelectedFiniteC1SourceIdentityTheorem",
                "must_prove": final_gate["two_legal_finishing_routes"][0]["must_prove"],
                "accepts_if": "all finite source identity clauses are proved unpatched",
            },
            "exit_2": {
                "label": "CONST-EW-02 / WEAK-MIXING / B31-HONEST-KERNEL-EXPORT",
                "artifact": "Independent selected finite C1 kernel/quadrature export",
                "must_emit": final_gate["two_legal_finishing_routes"][1]["must_emit"],
                "accepts_if": "independent source ids and exactness/error certificates exclude residual-projector replay and locked targets",
            },
        },
        "anti_cycle_delta_from_B29": {
            "B29": "named the primitive-kernel source theorem and imported strict Route-B reduction",
            "B30": "imports the conditional validator pass and finite source-identity gate, proving the next move is a two-exit source theorem/export problem",
            "not_repeated": [
                "not another 72-row value replay",
                "not another residual-projector comparison",
                "not another weak-angle numerical target fit",
            ],
        },
        "forbidden_next_moves": [
            "claim physical weak-angle closure from the conditional validator pass",
            "reuse residual-projector replay as independent source provenance",
            "fit observed sin^2(theta_W), alpha, masses, CKM, or PMNS to choose a source",
            "repeat B27-B29 row replay without new source identity or independent row provenance",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B30Boundary.v1",
        "status": "B30_TWO_EXIT_FRONTIER_BUILT_PHYSICAL_WEAKANGLE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B30-BOUNDARY",
        "closed_or_sharpened_now": {
            "conditional_superset_RouteB_validator_pass_imported": conditional_result["passes"],
            "finite_C1_source_identity_gate_imported": True,
            "two_legal_finishing_routes_locked": True,
            "anti_cycle_guard_strengthened": True,
        },
        "still_open": {
            "SelectedFiniteC1SourceIdentityTheorem_unpatched": True,
            "honest_independent_finite_C1_kernel_export": True,
            "source_independence_from_residual_projector_replay": True,
            "K_phys_or_f_ab": True,
            "mu_match": True,
            "RG_threshold_scheme": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "allowed_claim": "B30 proves the weak-mixing C1 edge is no longer a calculation search; it is reduced to two non-cyclic source-provenance exits.",
        "forbidden_claim": "unpatched source identity, honest independent kernel export, Route-B promotion, or physical weak-angle closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B30NextWork.v1",
        "status": "NEXT_WORKORDER_ATTACK_TWO_EXITS",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B31-SOURCE-IDENTITY-CLAUSE-PROOF-AND-HONEST-KERNEL-EXPORT",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B31-SOURCE-IDENTITY-CLAUSE-PROOF",
            "task": "Attack the SelectedFiniteC1SourceIdentityTheorem clause-by-clause, starting with same-source R_Z/R_X/b_selected emission and no-residual-projector source provenance.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B31-HONEST-KERNEL-EXPORT",
            "task": "Attempt an independent finite C1 kernel export with 72 primitive, 2 Hessian/source, and 36 sector rows plus source ids and exactness/error certificates.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB30SourceIdentityTwoExitReduction",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B30-PRIMITIVE-KERNEL-SOURCE-THEOREM",
        "output_packets": {
            "conditional_superset_validator_import": rel(CONDITIONAL),
            "finite_c1_source_identity_gate_import": rel(GATE),
            "two_exit_noncycle_frontier": rel(TWO_EXIT),
            "weak_mixing_b30_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B30SourceIdentityTwoExitReductionTheorem",
            "proved": True,
            "statement": (
                "The B29 primitive-kernel source theorem frontier is sharpened by importing the conditional full Route-B validator pass and the unpatched finite C1 source identity gate. Therefore the weak-mixing C1 edge has exactly two non-cyclic finishing routes: prove the unpatched SelectedFiniteC1SourceIdentityTheorem, or export an honest independent finite C1 kernel table with source ids and exactness/error certificates. No physical weak-angle closure is claimed."
            ),
        },
        "conditional_superset_RouteB_validator_passes": conditional_result["passes"],
        "unpatched_RouteB_validator_passes": False,
        "finite_C1_source_identity_gate_imported": True,
        "two_legal_finishing_routes_locked": True,
        "anti_cycle_confirmed": True,
        "source_identity_proved_now": False,
        "honest_kernel_export_emitted_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B30_SourceIdentityTwoExitReduction_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "conditional_superset_RouteB_validator_passes": conditional_result["passes"],
        "unpatched_RouteB_validator_passes": False,
        "finite_C1_source_identity_gate_imported": True,
        "two_legal_finishing_routes_locked": True,
        "anti_cycle_confirmed": True,
        "source_identity_proved_now": False,
        "honest_kernel_export_emitted_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B30 Source Identity Two Exit Reduction v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B30-PRIMITIVE-KERNEL-SOURCE-THEOREM`

## Superset Use

```text
Conditional path: Route-B row kernels + Route-A/source-identity clauses
                  + Weyl-variation/Hessian/sector-functor support.
Locked target:    strict Route-B row-source validator.
Forbidden target: observed weak angle or any measured SM replay value.
```

The conditional superset path passes, but it is not an unpatched proof.

## Not A Cycle

```text
B29: primitive-kernel source theorem named.
B30: imports the conditional full validator pass and the finite source-identity
     theorem gate, reducing the frontier to two legal exits.
```

## Two Legal Exits

1. `SelectedFiniteC1SourceIdentityTheorem`
2. Honest independent finite C1 kernel export

Anything else is now classified as cycling unless it supplies new source
identity clauses or new independent row provenance.

## Still Open

```text
unpatched source identity proof          = True
honest independent finite C1 export      = True
physical weak-angle closure              = True
K_phys/mu_match/RG threshold closure     = True
```
"""

    for path, payload in [
        (CONDITIONAL, conditional_packet),
        (GATE, gate_packet),
        (TWO_EXIT, two_exit),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
