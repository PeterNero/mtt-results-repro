"""Import Route-C independent Galerkin / residual-projector dependency cutset."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_dual_attempt_patched_spine_import_certificate.json"
UPSTREAM_SLUG = "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
INDEPENDENCE = UPSTREAM_DIR / "independence_dependency_audit.packet.json"
LADDER = UPSTREAM_DIR / "residual_projector_derivation_ladder.packet.json"
CONTRACT = UPSTREAM_DIR / "minimal_next_source_contract.packet.json"

OUTPUT_PACKET = DATA / "routec_dependency_cutset_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_dependency_cutset_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_DependencyCutset_Import_v1.md"

STATUS = "ROUTEC_DEPENDENCY_CUTSET_IMPORTED_ORTHOGONAL_COMPLETION_OR_INDEPENDENT_SOLVE_OPEN"
PREVIOUS_STATUS = "ROUTEC_DUAL_ATTEMPT_PATCHED_SPINE_IMPORTED_UNPATCHED_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_INDEPENDENTGALERKINC1CONTRACTIONS_OR_DERIVERESIDUALPROJECTORAXIOM_BUILT_DEPENDENCY_CUTSET_OPEN"
NEXT = "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    independence = load(INDEPENDENCE)
    ladder = load(LADDER)
    contract = load(CONTRACT)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")
    levels = ladder["levels"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1",
        "F1_upstream_cutset_proved_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["patched_spine_closure_preserved"] is True
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["patched_spine_closure_preserved"] is True
        and cert["independent_Galerkin_C1_closed"] is False
        and cert["unpatched_theorem_closure_claimed"] is False,
        "F3_dependency_audit_rejects_independence": independence["status"] == "DEPENDENCY_FOUND_REPLAY_NOT_INDEPENDENT"
        and independence["zero_mode_basis"]["declared"] is True
        and independence["zero_mode_basis"]["selected_source_verified"] is False
        and independence["primitive_contractions"]["present"] is True
        and independence["primitive_contractions"]["computed_from_independent_galerkin_quadrature"] is False
        and independence["primitive_contractions"]["selected_source_verified"] is False
        and independence["hessian_source"]["present"] is True
        and independence["hessian_source"]["b_selected_emitted_by_independent_hessian"] is False
        and independence["first_run_result"]["strict_replay_passes"] is True
        and independence["first_run_result"]["honest_independent_galerkin_execution_passes"] is False
        and len(independence["independence_obstruction"]) == 3,
        "F4_ladder_closes_only_algebra": ladder["status"] == "ALGEBRAIC_UNIQUENESS_CLOSED_PHYSICAL_APPLICATION_OPEN"
        and levels["L0_trace_orthogonal_uniqueness"]["closed"] is True
        and levels["L1_minimal_norm_completion"]["closed_conditionally"] is True
        and levels["L2_physical_PhiFinC1_application"]["closed"] is False
        and levels["L3_independent_quadrature_hessian"]["closed"] is False
        and ladder["what_is_now_theorem_derived"]["unique_Q_residual_given_fixed_fiber_span"] is True
        and ladder["what_is_not_theorem_derived"]["physical_differentiated_PhiFinC1_applies_Q_residual"] is True,
        "F5_minimal_next_contract_declares_two_exits": contract["status"] == "TWO_MINIMAL_SOURCE_OPTIONS_DECLARED"
        and contract["option_A_derive_principle"]["name"] == "DifferentiatedC1OrthogonalCompletionPrinciple"
        and len(contract["option_A_derive_principle"]["would_promote"]) == 4
        and contract["option_B_compute_values"]["name"] == "IndependentGalerkinQuadratureHessianSolve"
        and len(contract["option_B_compute_values"]["required_values"]) == 6
        and contract["recommended_next"] == NEXT,
        "F6_remaining_gates_preserved": all(
            upstream["what_remains_open"][key] is True
            for key in [
                "derive_differentiated_C1_orthogonal_completion_principle",
                "prove_physical_PhiFinC1_applies_Q_residual",
                "emit_independent_selected_zero_mode_basis",
                "compute_independent_primitive_contractions",
                "emit_independent_hessian_b_selected",
                "close_unpatched_SM_parity_dynamic_packet",
                "true_SM_equivalence_closure",
            ]
        ),
        "F7_promotion_guardrails_preserved": upstream["promotion_decision"]["patched_spine_closure_preserved"] is True
        and upstream["promotion_decision"]["unpatched_A_selected_promoted"] is False
        and upstream["promotion_decision"]["unpatched_b_selected_promoted"] is False
        and upstream["promotion_decision"]["independent_Galerkin_C1_closed"] is False
        and upstream["promotion_decision"]["residual_projector_axiom_derived_from_unpatched_MTT"] is False
        and upstream["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False
        and "true dependency" in note,
    }

    summary = {
        "patched_spine_closure_preserved": True,
        "unpatched_theorem_closure_claimed": False,
        "independent_galerkin_closed": False,
        "algebraic_Q_residual_uniqueness_closed": True,
        "physical_PhiFinC1_application_open": True,
        "strict_replay_passes": independence["first_run_result"]["strict_replay_passes"],
        "A_transpose_A": independence["first_run_result"]["A_transpose_A"],
        "A_transpose_b": independence["first_run_result"]["A_transpose_b"],
        "deltaTheta_C1": independence["first_run_result"]["deltaTheta_C1"],
        "minimal_exits": [
            contract["option_A_derive_principle"]["name"],
            contract["option_B_compute_values"]["name"],
        ],
    }

    return {
        "packet": "RouteC_DependencyCutset_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_independence_audit": str(INDEPENDENCE),
            "upstream_derivation_ladder": str(LADDER),
            "upstream_next_contract": str(CONTRACT),
        },
        "theorem": {
            "name": "RouteCDependencyCutsetImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The exact replay and algebraic Q_residual uniqueness are no "
                "longer the blocker.  The unpatched route now has exactly two "
                "minimal exits: derive the differentiated C1 orthogonal-completion "
                "principle, or compute independent Galerkin quadrature/Hessian values."
            ),
        },
        "checks": checks,
        "dependency_cutset_summary": summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "independence_dependency_audit": independence,
            "residual_projector_derivation_ladder": ladder,
            "minimal_next_source_contract": contract,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_unpatched_SM_dynamic_closure": False,
            "claims_unpatched_A_selected": False,
            "claims_unpatched_b_selected": False,
            "claims_independent_Galerkin_C1": False,
            "claims_true_SM_equivalence": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCDependencyCutsetImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "dependency_cutset_summary": packet["dependency_cutset_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["dependency_cutset_summary"]
    return f"""# RouteC Dependency Cutset Import v1

Status: `{cert["status"]}`.

The dependency cutset is now sharp.  The patched-spine closure is preserved,
but unpatched MTT closure is not claimed.

Closed algebraic layer:

```text
Q_residual uniqueness = {s["algebraic_Q_residual_uniqueness_closed"]}
strict replay passes = {s["strict_replay_passes"]}
A^T A = {s["A_transpose_A"]}
A^T b = {s["A_transpose_b"]}
deltaTheta_C1 = {s["deltaTheta_C1"]}
```

The remaining unpatched exits are:

```text
1. {s["minimal_exits"][0]}
2. {s["minimal_exits"][1]}
```

No unpatched `A_selected`, `b_selected`, independent Galerkin C1 closure, true
SM equivalence, observed-data selector, or target fitting is imported here.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
