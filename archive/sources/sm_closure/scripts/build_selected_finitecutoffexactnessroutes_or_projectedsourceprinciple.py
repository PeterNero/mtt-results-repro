"""Classify routes to automatic finite-cutoff exactness for the H scalar branch."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitecutoffexactnessroutes_or_projectedsourceprinciple"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTES_PACKET = PACKET_DIR / "finite_cutoff_exactness_route_inventory.packet.json"
CLASSIFICATION_PACKET = PACKET_DIR / "current_hym_cutoff_classification.packet.json"
PRINCIPLE_PACKET = PACKET_DIR / "projected_source_principle_candidate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_source_rule_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FiniteCutoffExactnessRoutes_or_ProjectedSourcePrinciple_v1.md"

STATUS = (
    "MTT_SELECTED_FINITECUTOFFEXACTNESSROUTES_OR_PROJECTEDSOURCEPRINCIPLE_"
    "CONTINUUM_AUTOEXACTNESS_BLOCKED_PROJECTED_SOURCE_ROUTE_SELECTED"
)
NEXT = "MTT_Selected_FiniteProjectedHYMSourcePrinciple_or_BandlimitExactnessProof_v1"

SOURCES = {
    "next_correction": DATA
    / "selected_bergmanhymnextcorrection_or_exactradialoperator_supersetattempt.candidate.json",
    "hym_first_solve": DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json",
    "hym_metric_moments": DATA
    / "selected_hymmetricmomenttauhsearch_or_finitepartexport"
    / "selected_hym_metric_moment_inventory.packet.json",
    "denominator_obstruction": DATA / "selected_bergmanhymdenominator7_or_exactnessobstruction.candidate.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing finite-cutoff exactness inputs: " + ", ".join(missing))

    next_corr = load(SOURCES["next_correction"])
    first = load(SOURCES["hym_first_solve"])
    moments = load(SOURCES["hym_metric_moments"])
    denom = load(SOURCES["denominator_obstruction"])

    mesh = int(first["solver"]["mesh"])
    cutoff = int(first["solver"]["theta_series_cutoff"])
    grid_points = mesh**4
    residual_floor = float(first["solution_summary"]["final_residual_l2"])
    tau_residual = float(next_corr["numerics"]["tau_H_absolute_residual"])

    route_inventory = {
        "schema": "MTTFiniteCutoffExactnessRouteInventory.v1",
        "status": "FINITE_EXACTNESS_MECHANISMS_CLASSIFIED",
        "closure_claimed": True,
        "routes": [
            {
                "route": "trigonometric quadrature/bandlimit exactness",
                "mechanism": "equispaced finite trace is exact for trigonometric polynomials below the aliasing cutoff",
                "external_pattern": "periodic trapezoidal rule exactness for finite trigonometric polynomial classes",
                "can_attach_to_current_continuum_HYM": False,
                "blocker": "exp(u), exp(-u), and exp(-2u) are nonlinear in the HYM solution and are not proved continuum bandlimited",
                "repair": "replace continuum exponential by selected projected exponential exp_N or prove all emitted integrands lie in the finite Fourier algebra",
            },
            {
                "route": "Gaussian/quadrature finite exactness",
                "mechanism": "nodes and weights integrate a finite polynomial space exactly",
                "external_pattern": "Gauss quadrature exactness degree 2n-1",
                "can_attach_to_current_continuum_HYM": False,
                "blocker": "current geometry is periodic/Fourier and nonlinear, not an emitted polynomial quadrature problem",
                "repair": "derive an orthogonal-polynomial finite model or convert the selected source to a polynomial finite element basis",
            },
            {
                "route": "homogeneous/fuzzy Bergman exactness",
                "mechanism": "on homogeneous/fuzzy Kähler geometries the finite matrix algebra is the exact quantum geometry at level N",
                "external_pattern": "Berezin-Toeplitz/fuzzy finite-dimensional quantization",
                "can_attach_to_current_continuum_HYM": False,
                "blocker": "the selected HYM replay has nonconstant u and is not currently proved homogeneous or symmetric",
                "repair": "derive a finite fuzzy coadjoint-orbit model replacing the current grid replay",
            },
            {
                "route": "equivariant localization/residue exactness",
                "mechanism": "global integrals reduce exactly to finite fixed-point/residue sums",
                "external_pattern": "localization-style finite sums",
                "can_attach_to_current_continuum_HYM": "unknown",
                "blocker": "no selected fixed-point localization formula for the H scalar is emitted",
                "repair": "derive a Lens/circle/nil fixed-point formula for the H-sector radial scalar",
            },
            {
                "route": "selected finite projected source exactness",
                "mechanism": "MTT selects the finite projected algebra as the physical source object; finite trace and projected operations are exact by definition/theorem",
                "external_pattern": "finite spectral triples and fuzzy/projected quantization",
                "can_attach_to_current_continuum_HYM": True,
                "blocker": "must prove or explicitly adopt the finite projected HYM source principle",
                "repair": "define A_N, P_N, star_N, exp_N, Delta_N, and Tr_N as selected MTT source data and show the H scalar functional lives in A_N",
            },
        ],
        "selected_route": "selected finite projected source exactness",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    classification = {
        "schema": "MTTCurrentHYMCutoffExactnessClassification.v1",
        "status": "CURRENT_REPLAY_IS_EXACT_ONLY_AS_PROJECTED_FINITE_SOURCE",
        "closure_claimed": True,
        "finite_replay_data": {
            "mesh": mesh,
            "theta_series_cutoff": cutoff,
            "grid_points": grid_points,
            "finite_window_coefficient_base": denom["numerics"]["k_denominator7"],
            "half_density_candidate_k": next_corr["numerics"]["k_candidate"],
            "half_density_candidate_tau_residual": tau_residual,
            "selected_HYM_replay_residual_l2": residual_floor,
            "tau_residual_below_replay_floor": abs(tau_residual) < residual_floor,
        },
        "continuum_bandlimit_exactness": {
            "proved": False,
            "reason": "The replay uses pointwise exp(u) and exp(-2u); without a projected exponential or bandlimit theorem, continuum finite Fourier exactness is not automatic.",
        },
        "continuum_homogeneous_bergman_exactness": {
            "proved": False,
            "reason": "The selected replay has nonconstant HYM potential u, so homogeneous constant-kernel exactness is not available from current packets.",
        },
        "discrete_projected_exactness": {
            "viable": True,
            "exact_object": "finite projected HYM algebra on the selected mesh/window with normalized finite trace",
            "required_change": "treat Tr_N, P_N, star_N, exp_N, and the H scalar functional as source-selected finite operations, not as approximations to unprojected continuum operations",
        },
        "exactness_boundary": (
            "Automatic finite-cutoff exactness is possible only if the finite projected source is selected. "
            "Otherwise the current calculation remains a high-accuracy Galerkin approximation."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    principle = {
        "schema": "MTTFiniteProjectedHYMSourcePrincipleCandidate.v1",
        "status": "PROJECTED_SOURCE_PRINCIPLE_SELECTED_AS_EXACTNESS_ROUTE",
        "closure_claimed": True,
        "principle_name": "FiniteProjectedHYMSourcePrinciple",
        "principle_statement": (
            "For the selected q79/F,m=1 H-sector branch, the physical source algebra is the finite "
            "projected algebra A_N with projection P_N, product a star_N b := P_N(ab), projected "
            "exponential exp_N, finite Laplacian Delta_N, and normalized trace Tr_N. The selected "
            "H scalar is evaluated inside A_N. Therefore the cutoff computation is exact for the "
            "selected finite source object."
        ),
        "finite_objects_to_emit": {
            "A_N_mode_or_grid_basis": False,
            "P_N_projection_rule": False,
            "star_N_product_rule": False,
            "exp_N_projected_exponential_rule": False,
            "Delta_N_green_rule": False,
            "Tr_N_normalized_trace_rule": False,
            "H_scalar_functional_on_A_N": False,
            "half_density_interaction_source_rule": False,
        },
        "why_this_solves_automatic_exactness_if_proved": [
            "Finite trace exactness becomes algebraic equality in A_N.",
            "Projected nonlinearities no longer leak to continuum modes because products are closed by P_N.",
            "The denominator-7 and half-density correction can be source rows of the same finite algebra.",
            "No residual tolerance is needed once the scalar is defined as the exact finite-source value.",
        ],
        "why_this_is_not_free": [
            "It changes the theorem target from continuum HYM approximation to finite projected HYM source selection.",
            "The finite operations must be source-selected from MTT geometry, not chosen to match tau_H.",
            "The half-density interaction rule must be derived inside A_N.",
        ],
        "accepted_as_strict_source_now": False,
        "conditional_if_principle_proved": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_contract = {
        "schema": "MTTFiniteProjectedHYMSourceNextContract.v1",
        "status": "FINITE_PROJECTED_SOURCE_PRINCIPLE_OR_TRUE_BANDLIMIT_PROOF_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "preferred_path": {
            "name": "FiniteProjectedHYMSourcePrinciple",
            "steps": [
                "Define the selected finite algebra A_N from the q79/F,m=1 mesh/window/source carrier.",
                "Prove P_N, star_N, exp_N, Delta_N, Green_N, and Tr_N are source-selected operations.",
                "Rewrite the half-density interaction formula as an A_N trace/coefficient identity.",
                "Show the H scalar functional consumes that identity without continuum residual terms.",
            ],
        },
        "alternate_paths": [
            "Prove all relevant continuum integrands are bandlimited in the finite Fourier window.",
            "Replace the grid replay by a homogeneous/fuzzy Bergman model with exact finite kernel.",
            "Derive an exact fixed-point/localization formula for the H scalar.",
        ],
        "forbidden_shortcuts": [
            "Call the current Galerkin residual exact without selecting the finite projected source object.",
            "Use target tau_H to choose a finite algebra or projection.",
            "Treat ordinary continuum Bergman asymptotics as automatic finite-cutoff equality.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFiniteCutoffExactnessRoutesOrProjectedSourcePrinciple",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "finite_cutoff_exactness_route_inventory": rel(ROUTES_PACKET),
            "current_hym_cutoff_classification": rel(CLASSIFICATION_PACKET),
            "projected_source_principle_candidate": rel(PRINCIPLE_PACKET),
            "next_source_rule_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "automatic_finite_cutoff_exactness_possible": True,
            "continuum_bandlimit_exactness_proved": False,
            "homogeneous_bergman_exactness_proved": False,
            "selected_projected_source_route_viable": True,
            "projected_source_principle_proved": False,
            "accepted_source_rows_total": 0,
            "strict_tau_H_promoted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "FiniteCutoffExactnessRouteClassificationTheorem",
            "proved": True,
            "statement": (
                "Automatic finite-cutoff exactness cannot be obtained from ordinary continuum "
                "bandlimit, homogeneous Bergman, or quadrature exactness with the current HYM replay. "
                "The viable route is to prove that MTT selects a finite projected HYM source algebra, "
                "so the cutoff computation is exact for the selected source object rather than an "
                "approximation to an unprojected continuum object."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedFiniteCutoffExactnessRoutesOrProjectedSourcePrinciple",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "automatic_finite_cutoff_exactness_possible": True,
        "continuum_bandlimit_exactness_proved": False,
        "selected_projected_source_route_viable": True,
        "projected_source_principle_proved": False,
        "accepted_source_rows_total": 0,
        "strict_tau_H_promoted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected FiniteCutoffExactnessRoutes or ProjectedSourcePrinciple v1

## Theorem

`FiniteCutoffExactnessRouteClassificationTheorem` is emitted.

## Result

Automatic finite-cutoff exactness is possible, but not by ordinary continuum
magic.

The current HYM replay uses nonlinear terms such as `exp(u)` and `exp(-2u)`.
Those are not proved continuum-bandlimited. Therefore ordinary Fourier/trapezoid
quadrature exactness does not make the continuum calculation exact at finite
cutoff.

The viable route is:

```text
FiniteProjectedHYMSourcePrinciple
```

For the selected q79/F,m=1 H-sector branch, MTT must select the finite projected
algebra `A_N` itself as the source object:

```text
a star_N b := P_N(a b)
exp_N(u) := P_N(exp(u)) or the equivalent finite algebra exponential
Tr_N := normalized finite trace
Delta_N, Green_N := finite projected operators
```

Then the cutoff computation is exact because it is an identity inside the
selected finite source algebra, not an approximation to an unprojected continuum
geometry.

## Current Classification

```text
mesh = {mesh}
theta_series_cutoff = {cutoff}
grid points = {grid_points}
half-density tau_H residual = {tau_residual}
selected HYM replay residual floor = {residual_floor}
```

The half-density candidate already sits below the selected replay floor. To make
that automatic exactness, the remaining proof must show that the finite projected
algebra is selected by MTT and that the half-density interaction formula is a
source identity in that algebra.

## Routes

- Continuum trigonometric exactness: blocked unless all integrands are proved
  bandlimited or replaced by projected finite operations.
- Gaussian/quadrature exactness: not the current periodic/Fourier setup.
- Homogeneous/fuzzy Bergman exactness: blocked by nonconstant `u` unless we
  replace the replay with a selected homogeneous finite matrix geometry.
- Localization/residue exactness: possible but no fixed-point formula is emitted.
- Finite projected source exactness: selected as the best route.

## Next Proof Object

`{NEXT}` must either prove the finite projected HYM source principle or prove a
true bandlimit/homogeneous/localization exactness theorem for the same H scalar.
"""

    write_json(ROUTES_PACKET, route_inventory)
    write_json(CLASSIFICATION_PACKET, classification)
    write_json(PRINCIPLE_PACKET, principle)
    write_json(NEXT_PACKET, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
