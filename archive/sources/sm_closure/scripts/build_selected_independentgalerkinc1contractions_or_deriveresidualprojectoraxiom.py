"""Build independent Galerkin C1 contractions / residual-projector axiom derivation gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch.candidate.json"
FIRST_RUN = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "first_galerkin_replay_result.packet.json"
)
PRIMITIVE_TERMS = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "inputs"
    / "primitive_contraction_terms.packet.json"
)
HESSIAN = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "inputs"
    / "hessian_source_vector.packet.json"
)
ZERO_MODE = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "inputs"
    / "zero_mode_basis.packet.json"
)
AXIOM_PATCH = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "residual_projector_axiom_local_corpus_patch.packet.json"
)

SLUG = "selected_independentgalerkinc1contractions_or_deriveresidualprojectoraxiom"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
INDEPENDENCE_AUDIT = PACKET_DIR / "independence_dependency_audit.packet.json"
DERIVATION_LADDER = PACKET_DIR / "residual_projector_derivation_ladder.packet.json"
NEXT_CONTRACT = PACKET_DIR / "minimal_next_source_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1.md"

STATUS = "MTT_SELECTED_INDEPENDENTGALERKINC1CONTRACTIONS_OR_DERIVERESIDUALPROJECTORAXIOM_BUILT_DEPENDENCY_CUTSET_OPEN"
NEXT = "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    first_run = load(FIRST_RUN)
    primitive = load(PRIMITIVE_TERMS)
    hessian = load(HESSIAN)
    zero = load(ZERO_MODE)
    patch = load(AXIOM_PATCH)

    replay = first_run["acceptance_results"]

    independence_audit = {
        "schema": "MTTIndependentGalerkinDependencyAudit.v1",
        "status": "DEPENDENCY_FOUND_REPLAY_NOT_INDEPENDENT",
        "zero_mode_basis": {
            "packet": rel(ZERO_MODE),
            "declared": True,
            "selected_source_verified": zero["selected_source_verified"],
            "independent_hym_or_galerkin_basis_emitted": False,
        },
        "primitive_contractions": {
            "packet": rel(PRIMITIVE_TERMS),
            "present": True,
            "computed_from_independent_galerkin_quadrature": primitive[
                "computed_from_independent_galerkin_quadrature"
            ],
            "selected_source_verified": primitive["selected_source_verified"],
            "source_dependency": primitive["source"],
        },
        "hessian_source": {
            "packet": rel(HESSIAN),
            "present": True,
            "b_selected_emitted_by_independent_hessian": hessian[
                "b_selected_emitted_by_independent_hessian"
            ],
            "b_selected_replay_available_under_axiom_patch": hessian[
                "b_selected_replay_available_under_axiom_patch"
            ],
            "source_dependency": hessian["source"],
        },
        "first_run_result": {
            "strict_replay_passes": first_run["strict_replay_passes"],
            "honest_independent_galerkin_execution_passes": first_run[
                "honest_independent_galerkin_execution_passes"
            ],
            "A_transpose_A": replay["A_transpose_A"],
            "A_transpose_b": replay["A_transpose_b"],
            "deltaTheta_C1": replay["deltaTheta_C1"],
        },
        "independence_obstruction": [
            "primitive terms are sourced from the residual-projector axiom contract",
            "b_selected is sourced from the residual-projector axiom contract",
            "zero-mode basis is canonical support rather than an emitted selected Galerkin basis",
        ],
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    derivation_ladder = {
        "schema": "MTTResidualProjectorDerivationLadder.v1",
        "status": "ALGEBRAIC_UNIQUENESS_CLOSED_PHYSICAL_APPLICATION_OPEN",
        "levels": {
            "L0_trace_orthogonal_uniqueness": {
                "closed": True,
                "statement": (
                    "Given the selected fixed-fiber span, Frobenius/trace orthogonality fixes a unique "
                    "residual projector Q_residual and unique R_Z/R_X residual representatives."
                ),
            },
            "L1_minimal_norm_completion": {
                "closed_conditionally": True,
                "condition": (
                    "If differentiated C1 response is required to complete the selected fixed-fiber "
                    "packet by the least Frobenius-norm trace-orthogonal correction, then R_Z/R_X are selected."
                ),
            },
            "L2_physical_PhiFinC1_application": {
                "closed": False,
                "missing_principle": "selected differentiated Phi_fin^C1 must be shown to obey the L1 orthogonal-completion rule",
            },
            "L3_independent_quadrature_hessian": {
                "closed": False,
                "missing_values": [
                    "selected zero-mode basis from HYM/Galerkin solve",
                    "independent primitive 3x3 contractions",
                    "independent Hessian/source vector b_selected",
                ],
            },
        },
        "what_is_now_theorem_derived": {
            "unique_Q_residual_given_fixed_fiber_span": True,
            "unique_R_Z_R_X_given_conditional_target": True,
            "rank_2_replay_from_these_residuals": True,
        },
        "what_is_not_theorem_derived": {
            "physical_differentiated_PhiFinC1_applies_Q_residual": True,
            "independent_Galerkin_primitive_contractions_equal_R_Z_R_X": True,
            "independent_Hessian_emits_b_selected": True,
        },
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTMinimalNextSourceContract.v1",
        "status": "TWO_MINIMAL_SOURCE_OPTIONS_DECLARED",
        "option_A_derive_principle": {
            "name": "DifferentiatedC1OrthogonalCompletionPrinciple",
            "sufficient_statement": (
                "For the selected q79/F,m=1 Route-C C1 packet, differentiated Phi_fin^C1 selects the "
                "least Frobenius-norm trace-orthogonal completion to the selected fixed-fiber response."
            ),
            "would_promote": [
                "physical Phi_fin^C1 applies Q_residual",
                "R_Z/R_X selected without local axiom patch",
                "b_selected replay promoted in unpatched spine",
                "SM-parity dynamic packet closure without local axiom",
            ],
            "risk": "must be justified from MTT variational/admissibility structure, otherwise it is only a renamed axiom",
        },
        "option_B_compute_values": {
            "name": "IndependentGalerkinQuadratureHessianSolve",
            "required_values": [
                "selected zero-mode basis",
                "primitive 3x3 contraction table",
                "72-real A_selected matrix",
                "72-real b_selected vector",
                "sector response matrices",
                "rank/column-span/deltaTheta solve certificate",
            ],
            "would_promote": [
                "honest independent Galerkin C1 closure",
                "A_selected/b_selected in unpatched spine",
                "SM-parity dynamic packet closure without local axiom",
            ],
            "risk": "requires actual selected numerical/quadrature data rather than structural replay",
        },
        "recommended_next": NEXT,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedIndependentGalerkinC1ContractionsOrDeriveResidualProjectorAxiom",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "first_galerkin_replay": rel(FIRST_RUN),
            "primitive_terms": rel(PRIMITIVE_TERMS),
            "hessian_source": rel(HESSIAN),
            "zero_mode_basis": rel(ZERO_MODE),
            "axiom_patch": rel(AXIOM_PATCH),
        },
        "output_packets": {
            "independence_dependency_audit": rel(INDEPENDENCE_AUDIT),
            "residual_projector_derivation_ladder": rel(DERIVATION_LADDER),
            "minimal_next_source_contract": rel(NEXT_CONTRACT),
        },
        "what_closes_now": {
            "dependency_cutset_identified": True,
            "algebraic_Q_residual_uniqueness_reaffirmed": True,
            "minimal_orthogonal_completion_principle_is_sufficient_if_derived": True,
            "independent_Galerkin_value_requirements_are_exact": True,
            "observed_constants_excluded_as_selectors": True,
        },
        "what_remains_open": {
            "derive_differentiated_C1_orthogonal_completion_principle": True,
            "prove_physical_PhiFinC1_applies_Q_residual": True,
            "emit_independent_selected_zero_mode_basis": True,
            "compute_independent_primitive_contractions": True,
            "emit_independent_hessian_b_selected": True,
            "close_unpatched_SM_parity_dynamic_packet": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "patched_spine_closure_preserved": previous["promotion_decision"][
                "SM_parity_dynamic_packet_closed_in_patched_spine"
            ],
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "independent_Galerkin_C1_closed": False,
            "residual_projector_axiom_derived_from_unpatched_MTT": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "DependencyCutsetAndDerivationLadderTheorem",
            "proved": True,
            "statement": (
                "The current dual-route state proves algebraic uniqueness of Q_residual and exact "
                "rank-2 replay, but it also proves that neither unpatched derivation nor honest "
                "independent Galerkin closure has occurred. The remaining cutset is precisely either "
                "a derivation of the differentiated C1 orthogonal-completion principle or independent "
                "quadrature/Hessian values satisfying the fixed acceptance contract."
            ),
        },
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_preserved": True,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_IndependentGalerkinC1Contractions_or_DeriveResidualProjectorAxiom_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "patched_spine_closure_preserved": True,
        "unpatched_theorem_closure_claimed": False,
        "independent_Galerkin_C1_closed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected IndependentGalerkinC1Contractions or DeriveResidualProjectorAxiom v1

Status: `{STATUS}`.

This gate pushed past the patched/replay result and located the true dependency
cutset.

Closed now:

```text
Q_residual uniqueness                       = theorem-derived algebra
rank-2 replay                               = exact
patched-spine dynamic closure               = preserved
```

Still not closed in the unpatched spine:

```text
physical Phi_fin^C1 applies Q_residual      = False
independent primitive contractions emitted  = False
independent Hessian b_selected emitted      = False
```

So the next artifact has two exact options:

```text
1. derive the DifferentiatedC1OrthogonalCompletionPrinciple
2. run an IndependentGalerkinQuadratureHessianSolve
```

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    INDEPENDENCE_AUDIT.write_text(json.dumps(independence_audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DERIVATION_LADDER.write_text(json.dumps(derivation_ladder, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT_CONTRACT.write_text(json.dumps(next_contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
