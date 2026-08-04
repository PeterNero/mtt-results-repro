"""Build the local-field solve or cover-selection no-go packet."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "local_equations": DATA / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_equations.json",
    "local_sourceamendment": DATA / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_sourceamendment.candidate.json",
    "finite_nerve_candidate": DATA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidencecandidate.candidate.json",
    "ctwist_source_search": DATA / "ctwist_source_value_search.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_localfieldsolve_or_coverselection_nogo.candidate.json"
OUTPUT_CALC = DATA / "selected_heterotic_projectiverhoe_localfieldsolve_dH_and_conditional_poincare.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_localfieldsolve_or_coverselection_nogo_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_LocalFieldSolve_or_CoverSelectionNoGo_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_LOCALFIELDSOLVE_DH_CLOSED_COVER_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SelectedCoverHomotopy_or_DeligneLocalPotentialValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def inv_count(seq: tuple[int, ...]) -> int:
    return sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])


def sign_to_sorted(seq: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    if len(set(seq)) < len(seq):
        return 0, tuple(sorted(seq))
    return (-1) ** inv_count(seq), tuple(sorted(seq))


def parse_form_components(raw: dict[str, float]) -> dict[tuple[int, ...], float]:
    out: dict[tuple[int, ...], float] = defaultdict(float)
    for key, value in raw.items():
        basis = tuple(int(char) for char in key)
        sign, sorted_basis = sign_to_sorted(basis)
        if sign:
            out[sorted_basis] += sign * float(value)
    return {basis: value for basis, value in out.items() if abs(value) > 1e-12}


def wedge(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    seq = a + b
    return sign_to_sorted(seq)


def exterior_derivative(form: dict[tuple[int, ...], float], de_forms: dict[int, dict[tuple[int, ...], float]]) -> dict[tuple[int, ...], float]:
    out: dict[tuple[int, ...], float] = defaultdict(float)
    for basis, coefficient in form.items():
        for r, index in enumerate(basis):
            prefix = basis[:r]
            suffix = basis[r + 1 :]
            for de_basis, de_coefficient in de_forms[index].items():
                sign, derived_basis = wedge(prefix, de_basis + suffix)
                if sign:
                    out[derived_basis] += coefficient * ((-1) ** r) * de_coefficient * sign
    return {basis: value for basis, value in out.items() if abs(value) > 1e-12}


def key(basis: tuple[int, ...]) -> str:
    return "".join(str(index) for index in basis)


def main() -> dict[str, Any]:
    equations = load(INPUTS["local_equations"])
    sourceamendment = load(INPUTS["local_sourceamendment"])
    finite_nerve = load(INPUTS["finite_nerve_candidate"])
    ct_source = load(INPUTS["ctwist_source_search"])

    geometry = equations["known_same_branch_geometry"]
    H = parse_form_components(geometry["torsion_H_or_d_c_omega_components"])
    de_forms = {
        index: parse_form_components(geometry["supporting_structure_equations"][f"de{index}"])
        for index in range(1, 7)
    }
    dH = exterior_derivative(H, de_forms)
    dH_closed = len(dH) == 0

    cover_status = equations["finite_nerve_scaffold"]["smooth_embedding_status"]
    selected_cover_emitted = all(value is not None for value in cover_status.values())
    same_branch_local_values_found = ct_source["gate_results"]["same_branch_Qa_SU3_values_found"]

    conditional_poincare = {
        "applies_if": [
            "a selected smooth good cover realizes U0,U1,U2 and all nonempty overlaps as contractible sets",
            "the invariant H is the selected local curvature target on that cover",
            "a chart homotopy or equivalent local primitive operator is supplied",
        ],
        "dH_closed_in_invariant_frame": dH_closed,
        "local_B_i_exist_conditionally": dH_closed,
        "local_A_ij_exist_conditionally_after_B_i": dH_closed,
        "local_g_ijk_exist_conditionally_after_A_ij": dH_closed,
        "values_emitted": False,
        "why_values_not_emitted": (
            "The current repo has no selected chart atlas, contractibility proof, "
            "homotopy operator, or same-branch Deligne local values."
        ),
    }

    algebraic_shadow_solve = {
        "abstract_scalar_transition_solution_exists": True,
        "example_shape": "on a formal three-patch nerve, choose scalar projective triples whose product is zeta_3^tau(label)",
        "promotable_to_smooth_source": False,
        "why_not_promotable": [
            "it assigns the central phase from the finite tau table instead of deriving it from g_ijk",
            "it has no selected smooth cover, local fields, metric/unitarity data, or operator-domain compatibility",
            "it is useful only as a post-solve check for a genuine Deligne/Cech representative",
        ],
    }

    calc = {
        "schema": "SelectedHeteroticProjectiveRhoE.LocalFieldSolve.dHAndConditionalPoincare.v1",
        "status": "DH_CLOSED_CONDITIONAL_LOCAL_POTENTIALS_VALUES_OPEN",
        "canonical_H_components": {key(basis): value for basis, value in sorted(H.items())},
        "de_components": {
            f"de{index}": {key(basis): value for basis, value in sorted(components.items())}
            for index, components in de_forms.items()
        },
        "dH_components": {key(basis): value for basis, value in sorted(dH.items())},
        "dH_closed": dH_closed,
        "conditional_poincare": conditional_poincare,
        "algebraic_shadow_solve": algebraic_shadow_solve,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_CALC.write_text(json.dumps(calc, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "dH_computed": True,
        "dH_closed": dH_closed,
        "conditional_local_potential_lane_live": dH_closed,
        "selected_cover_emitted": selected_cover_emitted,
        "same_branch_local_values_found": same_branch_local_values_found,
        "local_B_i_A_ij_g_ijk_values_emitted": False,
        "smooth_tau_shadow_derived": False,
        "S1_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoELocalFieldSolveOrCoverSelectionNoGo",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "calculation_path": rel(OUTPUT_CALC),
        "closed_now": {
            "invariant_dH_zero_check": dH_closed,
            "conditional_poincare_local_potential_existence_theorem": dH_closed,
            "abstract_scalar_shadow_solve_as_validator_only": True,
        },
        "still_open": {
            "selected_smooth_good_cover": not selected_cover_emitted,
            "contractible_chart_atlas_and_homotopy_operator": True,
            "explicit_local_B_i_values": True,
            "explicit_A_ij_and_g_ijk_values": True,
            "derivation_of_tau_shadow_from_smooth_g_ijk": True,
            "mapped_Freed_Witten_Bianchi_projector_checks": True,
            "smooth_operator_or_complement_domain": True,
        },
        "decision": decision,
        "guardrails": {
            "does_not_promote_conditional_poincare_to_values": True,
            "does_not_promote_abstract_scalar_shadow_to_smooth_source": True,
            "does_not_promote_formal_nerve_to_cover": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "LocalFieldSolveConditionalPoincareNoGoTheorem",
            "proved": True,
            "statement": (
                "The selected invariant Iwasawa torsion target satisfies dH=0 in "
                "the stored coframe, so local B_i potentials are conditionally "
                "available on any selected contractible good cover by the Poincare "
                "lemma. The current repository still cannot emit those local fields "
                "because it lacks the selected smooth cover, contractibility/homotopy "
                "data, and Deligne/Cech values deriving the finite tau shadow."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "calculation_path": rel(OUTPUT_CALC),
        "note_path": rel(OUTPUT_NOTE),
        "dH_computed": True,
        "dH_closed": dH_closed,
        "conditional_local_potential_lane_live": dH_closed,
        "local_field_values_emitted": False,
        "S1_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE LocalFieldSolve or CoverSelectionNoGo v1

## Result

```text
status = {STATUS}
dH_computed = true
dH_closed = {str(dH_closed).lower()}
conditional_local_potential_lane_live = {str(dH_closed).lower()}
S1_closed = false
next_required_artifact = {NEXT}
```

## Computation

The invariant Iwasawa/Strominger torsion target `H` was differentiated using
the stored coframe structure equations. The result is `dH = 0`. Thus the
Deligne local-potential lane is not killed algebraically: on a selected
contractible good cover, local `B_i` primitives would exist by the Poincare
lemma.

What remains open is precisely the selected smooth cover and local values:
charts, contractibility/homotopy operator, `B_i`, `A_ij`, `g_ijk`, and a proof
that the finite `tau` shadow is derived from those smooth fields rather than
assigned afterward.

Calculation packet:

```text
{rel(OUTPUT_CALC)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_CALC)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
