"""Type-check A70 against the actual selected Z64 tower spectrum."""
from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion"
OUT = ROOT / "candidate_data" / SLUG
SPECTRUM = OUT / "actual_z64_tower_spectrum.packet.json"
TYPING = OUT / "a70_resolvent_typing_audit.packet.json"
TRACE = OUT / "normalized_trace_routing_theorem.packet.json"
FUNCTIONALS = OUT / "typed_spectral_functional_trials.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ActualZ64TowerKineticFunctionalTyping_or_ResolventRoutingPromotion_v1.md"
STATUS = "MTT_SELECTED_ACTUAL_Z64_SPECTRUM_COMPUTED_A70_LABEL_SUM_TYPING_REJECTED_NORMALIZED_TRACE_IDENTITY_CONDITIONAL"
NEXT = "MTT_Selected_GaugeKineticFunctionalOfL64AndQ79Chord_or_StrictResidualValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compositions(total: int, prefix: tuple[int, ...] = ()) -> list[tuple[int, ...]]:
    if total == 0:
        return [prefix]
    rows: list[tuple[int, ...]] = []
    for value in range(1, total + 1):
        rows.extend(compositions(total - value, prefix + (value,)))
    return rows


def main() -> int:
    paths = {
        "A52_profile": ROOT / "candidate_data" / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization" / "product_triple_profile_normalization_and_moment_nogo.packet.json",
        "A68_tau": ROOT / "candidate_data" / "selected_quarkleptondoubletresolvedpositivedensitysource_or_kineticweightemission" / "selected_rational_cost_nearmiss.packet.json",
        "A69_residual": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "exact_residual_cost_spectrum.packet.json",
        "A70_resolvent": ROOT / "candidate_data" / "selected_residualcirclelenscostoperator_or_exactgaugekineticvalueemission" / "retarded_resolvent_cost_operator.packet.json",
        "A70_torsion": ROOT / "candidate_data" / "selected_residualcirclelenscostoperator_or_exactgaugekineticvalueemission" / "q79_shared_circle_chord_torsion.packet.json",
    }
    data = {key: load(path) for key, path in paths.items()}
    tau = float(data["A68_tau"]["tau_int"])
    torsion = float(data["A70_torsion"]["lens_quarter_log_cost"])
    residual = data["A69_residual"]["profile_inferred_values"]
    delta_q = float(residual["delta_q"])

    towers = []
    for exponent_row in compositions(5):
        degrees = [2**exponent for exponent in exponent_row]
        cost = sum(degree * degree - 1 for degree in degrees)
        towers.append({"exponents": list(exponent_row), "degrees": degrees, "cost": cost})
    multiplicities = Counter(row["cost"] for row in towers)
    eigenvalues = [float(row["cost"]) for row in towers]
    trace_l = sum(eigenvalues)
    resolvent_trace = sum(1.0 / value for value in eigenvalues)
    log_determinant = sum(math.log(value) for value in eigenvalues)
    heat_trace = sum(math.exp(-tau * value) for value in eigenvalues)
    ground_heat = math.exp(-15.0 * tau)
    spectrum = {
        "schema": "MTTActualZ64TowerSpectrum.v1",
        "status": "EXACT_SELECTED_TOWER_ARITHMETIC_SPECTRUM_COMPUTED",
        "definition": "C(d)=sum_i(d_i^2-1), d_i>=2, product d_i=32",
        "composition_count": len(towers),
        "towers": towers,
        "spectrum_with_multiplicity": [{"eigenvalue": value, "multiplicity": multiplicities[value]} for value in sorted(multiplicities)],
        "ground_eigenvalue": min(eigenvalues),
        "next_eigenvalue": sorted(set(eigenvalues))[1],
        "spectral_gap": sorted(set(eigenvalues))[1] - min(eigenvalues),
        "trace_L": trace_l,
        "normalized_trace_L": trace_l / len(eigenvalues),
        "trace_L_inverse": resolvent_trace,
        "normalized_trace_L_inverse": resolvent_trace / len(eigenvalues),
        "log_determinant_L": log_determinant,
        "heat_trace_at_tau_int": heat_trace,
        "ground_heat_weight": ground_heat,
        "ground_heat_identity": "exp(-15 tau_int)=1/448",
        "heat_tail": heat_trace - ground_heat,
        "external_theorem_authority": "mtt-q79-proof-repro/proof_corpus/MTT_Flavor_Operator_Identification_Criterion_for_Z64_Projector_v1.md",
    }

    typing = {
        "schema": "MTTA70ResolventTypingAudit.v1",
        "status": "A70_DENOMINATOR_NOT_A_CURRENT_SELECTED_HESSIAN_TRACE",
        "terms": [
            {"expression": "15", "current_type": "lowest eigenvalue of normalized L_tower", "same_operator_ready": True},
            {"expression": "second 15", "current_type": "multiplicity inferred from two hidden color channels", "same_operator_ready": False},
            {"expression": "16", "current_type": "retarded carrier/source label in 16->15, not an L_tower eigenvalue", "same_operator_ready": False},
            {"expression": "1/15", "current_type": "saturated proper time or ground resolvent scalar", "same_operator_ready": False},
        ],
        "exact_branch_facts": {
            "actual_L_tower_spectrum_contains_16": 16.0 in eigenvalues,
            "actual_L_tower_spectrum_contains_second_15": multiplicities[15] > 1,
            "Schur_leakage": 0.0,
        },
        "verdict": {
            "formal_positive_diagonal_candidate_exists": True,
            "derived_from_current_selected_L64": False,
            "strict_promotion_allowed": False,
            "A70_numerical_candidate_retained": True,
            "reason": "The proposed sum mixes an eigenvalue, a multiplicity hypothesis, a carrier label and a proper-time/resolvent scalar. The selected exact branch has a simple eigenvalue 15, no eigenvalue 16, and zero Schur leakage.",
        },
    }

    # Abstract result: any isometric embedding of diag(15,16) into C^42 has
    # normalized trace 31/42. Physical selection of that source block is separate.
    routing = (15.0 + 16.0) / 42.0
    trace_theorem = {
        "schema": "MTTNormalizedTraceRoutingTheorem.v1",
        "status": "ABSTRACT_NORMALIZED_TRACE_IDENTITY_PROVED_PHYSICAL_SOURCE_BLOCK_OPEN",
        "source_block": "A_ret=diag(15,16) on C^2",
        "target_carrier": "C^6 tensor C^7, dimension 42",
        "premise": "V:C^2->C^42 is an isometry and the routed observable is tau_42(V A_ret V^*)",
        "result": routing,
        "closed_form": "(15+16)/(6*7)=31/42",
        "basis_independent": True,
        "proof": "Tr(V A V^*)=Tr(A V^*V)=Tr(A)=31; dividing by dim(C^42)=42 gives 31/42.",
        "physical_premises_selected": {
            "six_record_carrier": True,
            "Z7_charge_carrier": True,
            "A_ret_eigenvalue_block_diag_15_16": False,
            "isometric_transfer_into_gauge_kinetic_density": False,
            "normalized_trace_is_selected_action_functional": False,
        },
        "strict_routing_promoted": False,
    }

    trials = [
        ("T79/Tr(L64)", torsion / trace_l),
        ("T79/dim(Htower)", torsion / len(eigenvalues)),
        ("T79*Tr(exp(-tau L64))", torsion * heat_trace),
        ("T79*normalized_Tr(L64^-1)", torsion * resolvent_trace / len(eigenvalues)),
        ("T79*Tr(L64^-1)", torsion * resolvent_trace),
        ("T79/(lambda0+lambda1+gap)", torsion / (15.0 + 24.0 + 9.0)),
        ("T79/(2lambda0+lambda1)", torsion / (2.0 * 15.0 + 24.0)),
        ("T79/(lambda0+lambda1+lambda0^-1)", torsion / (15.0 + 24.0 + 1.0 / 15.0)),
    ]
    trial_rows = [
        {
            "name": name,
            "value": value,
            "profile_inferred_delta_q_downstream_only": delta_q,
            "relative_residual": value / delta_q - 1.0,
            "exact": abs(value - delta_q) < 1e-13,
            "accepted": False,
        }
        for name, value in trials
    ]
    functionals = {
        "schema": "MTTTypedSpectralFunctionalTrials.v1",
        "status": "PREDECLARED_ACTUAL_L64_FUNCTIONALS_EXECUTED_NO_EXACT_RESIDUAL_SOURCE",
        "trials": trial_rows,
        "exact_match_count": sum(row["exact"] for row in trial_rows),
        "accepted_count": 0,
        "best_by_absolute_log_residual": min(trial_rows, key=lambda row: abs(math.log(row["value"] / delta_q))),
        "guardrail": "These are typed functions of the actual selected spectrum. No coefficients were tuned, and the downstream residual was used only for rejection/ranking.",
        "next_required_artifact": NEXT,
    }
    checks = {
        "sixteen_ordered_compositions": len(towers) == 16,
        "spectrum_exact": [(value, multiplicities[value]) for value in sorted(multiplicities)] == [(15, 1), (24, 4), (33, 3), (69, 3), (78, 2), (258, 2), (1023, 1)],
        "ground_next_gap_exact": spectrum["ground_eigenvalue"] == 15 and spectrum["next_eigenvalue"] == 24 and spectrum["spectral_gap"] == 9,
        "ground_heat_is_one_over_448": abs(ground_heat - 1.0 / 448.0) < 1e-15,
        "A70_16_not_actual_eigenvalue": not typing["exact_branch_facts"]["actual_L_tower_spectrum_contains_16"],
        "A70_second_15_not_actual_multiplicity": not typing["exact_branch_facts"]["actual_L_tower_spectrum_contains_second_15"],
        "A70_strict_promotion_rejected": not typing["verdict"]["strict_promotion_allowed"],
        "normalized_trace_identity_exact": abs(routing - 31.0 / 42.0) < 1e-15,
        "routing_physical_source_not_promoted": not trace_theorem["strict_routing_promoted"],
        "typed_trial_exact_match_count_zero": functionals["exact_match_count"] == 0,
    }
    candidate = {
        "schema": "MTTSelectedActualZ64TowerKineticFunctionalTypingOrResolventRoutingPromotion.v1",
        "status": STATUS,
        "results": {
            "actual_L64_spectrum_computed": True,
            "A70_denominator_strict_typing_rejected": True,
            "A70_numerical_candidate_retained": True,
            "normalized_trace_31_over_42_proved_abstractly": True,
            "physical_31_over_42_routing_selected": False,
            "typed_spectral_functional_exact_matches": 0,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "spectrum": str(SPECTRUM.relative_to(ROOT)).replace("\\", "/"),
            "typing": str(TYPING.relative_to(ROOT)).replace("\\", "/"),
            "trace": str(TRACE.relative_to(ROOT)).replace("\\", "/"),
            "functionals": str(FUNCTIONALS.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_ActualZ64TowerKineticFunctionalTyping_or_ResolventRoutingPromotion_v1",
        "status": STATUS,
        "actual_spectrum": [[value, multiplicities[value]] for value in sorted(multiplicities)],
        "ground_next_gap": [15, 24, 9],
        "ground_heat_weight": ground_heat,
        "A70_denominator_strictly_typed": False,
        "normalized_trace_31_over_42_identity_proved": True,
        "physical_routing_selected": False,
        "typed_exact_match_count": functionals["exact_match_count"],
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Actual Z64 Tower Kinetic Functional Typing or Resolvent Routing Promotion v1

## Actual selected spectrum

Enumerating all sixteen ordered compositions of `32=2^5` gives

```text
spec(L64) = 15(x1), 24(x4), 33(x3), 69(x3), 78(x2), 258(x2), 1023(x1).
```

Thus the selected eigenvalue is `15`, the next is `24`, and the exact gap is `9`. At
`tau_int=log(448)/15`, the ground heat weight is exactly `1/448`.

## A70 typing result

The A70 denominator `2*15+16+1/15` is not currently a trace of `L64`: the spectrum has one
copy of `15` and no `16`; `16` is a retarded carrier label, while `1/15` is a saturated proper
time/resolvent scalar. The exact branch also has zero Schur leakage. A70 remains a striking
target-ranked numerical candidate, but strict source promotion is rejected.

## What is proved for 31/42

For any isometry `V:C^2->C^42` and `A_ret=diag(15,16)`, normalized trace gives

```text
tau_42(V A_ret V^*) = Tr(A_ret)/42 = 31/42.
```

This identity is basis-independent. What remains open is physical selection of `A_ret`, `V`, and
the normalized trace as the gauge kinetic functional.

## Typed search

Eight predeclared heat/resolvent/determinant-scale functions of the actual `L64` spectrum were
executed. Exact matches to the profile-inferred residual: `0`. The next source must be a typed
same-action functional `F(L64,Delta79)` rather than arithmetic on retarded labels.

Next artifact: `{NEXT}`.
"""

    dump(SPECTRUM, spectrum)
    dump(TYPING, typing)
    dump(TRACE, trace_theorem)
    dump(FUNCTIONALS, functionals)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
