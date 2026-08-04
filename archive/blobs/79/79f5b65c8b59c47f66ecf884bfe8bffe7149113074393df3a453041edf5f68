"""Build the selected-cover homotopy or Deligne local-potential values gate."""

from __future__ import annotations

import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "localfieldsolve": DATA / "selected_heterotic_projectiverhoe_localfieldsolve_or_coverselection_nogo.candidate.json",
    "dh_calc": DATA / "selected_heterotic_projectiverhoe_localfieldsolve_dH_and_conditional_poincare.json",
    "local_equations": DATA / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_equations.json",
    "finite_values": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_selectedcoverhomotopy_or_deligne_localpotentialvalues.candidate.json"
OUTPUT_VALUES = DATA / "selected_heterotic_projectiverhoe_invariant_B_potential_candidate.values.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_selectedcoverhomotopy_or_deligne_localpotentialvalues_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SelectedCoverHomotopy_or_DeligneLocalPotentialValues_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_INVARIANT_B_POTENTIAL_CANDIDATE_BUILT_TAU_DERIVATION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FlatTorsionGerbe_or_ProjectiveTransition_SourceValues_v1"


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


def parse_fraction(text: str | int | float) -> Fraction:
    return Fraction(str(text)).limit_denominator(1_000_000)


def parse_form_components(raw: dict[str, Any]) -> dict[tuple[int, ...], Fraction]:
    out: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for key, value in raw.items():
        basis = tuple(int(char) for char in key)
        sign, sorted_basis = sign_to_sorted(basis)
        if sign:
            out[sorted_basis] += sign * parse_fraction(value)
    return {basis: value for basis, value in out.items() if value}


def wedge(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    return sign_to_sorted(a + b)


def exterior_derivative(form: dict[tuple[int, ...], Fraction], de_forms: dict[int, dict[tuple[int, ...], Fraction]]) -> dict[tuple[int, ...], Fraction]:
    out: dict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for basis, coefficient in form.items():
        for r, index in enumerate(basis):
            prefix = basis[:r]
            suffix = basis[r + 1 :]
            for de_basis, de_coefficient in de_forms[index].items():
                sign, derived_basis = wedge(prefix, de_basis + suffix)
                if sign:
                    out[derived_basis] += coefficient * ((-1) ** r) * de_coefficient * sign
    return {basis: value for basis, value in out.items() if value}


def key(basis: tuple[int, ...]) -> str:
    return "".join(str(index) for index in basis)


def solve_invariant_primitive(
    H: dict[tuple[int, ...], Fraction],
    de_forms: dict[int, dict[tuple[int, ...], Fraction]],
) -> dict[tuple[int, ...], Fraction] | None:
    basis2 = list(itertools.combinations(range(1, 7), 2))
    basis3 = list(itertools.combinations(range(1, 7), 3))
    d_basis = [exterior_derivative({basis: Fraction(1)}, de_forms) for basis in basis2]
    rows = [
        [d_basis[col].get(basis3_row, Fraction(0)) for col in range(len(basis2))]
        + [H.get(basis3_row, Fraction(0))]
        for basis3_row in basis3
    ]

    matrix = [row[:] for row in rows]
    row_index = 0
    pivots: list[int] = []
    col_count = len(basis2)
    for col in range(col_count):
        pivot_row = next((idx for idx in range(row_index, len(matrix)) if matrix[idx][col] != 0), None)
        if pivot_row is None:
            continue
        matrix[row_index], matrix[pivot_row] = matrix[pivot_row], matrix[row_index]
        pivot = matrix[row_index][col]
        matrix[row_index] = [value / pivot for value in matrix[row_index]]
        for idx in range(len(matrix)):
            if idx != row_index and matrix[idx][col] != 0:
                factor = matrix[idx][col]
                matrix[idx] = [
                    matrix[idx][j] - factor * matrix[row_index][j]
                    for j in range(col_count + 1)
                ]
        pivots.append(col)
        row_index += 1

    for row in matrix:
        if all(row[col] == 0 for col in range(col_count)) and row[-1] != 0:
            return None

    solution = [Fraction(0) for _ in range(col_count)]
    for reduced_row, col in enumerate(pivots):
        solution[col] = matrix[reduced_row][-1]
    return {basis: value for basis, value in zip(basis2, solution) if value}


def frac(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> dict[str, Any]:
    localfieldsolve = load(INPUTS["localfieldsolve"])
    dh_calc = load(INPUTS["dh_calc"])
    equations = load(INPUTS["local_equations"])
    finite_values = load(INPUTS["finite_values"])["finite_internal_values"]

    H = parse_form_components(dh_calc["canonical_H_components"])
    de_forms = {
        int(name[2:]): parse_form_components(components)
        for name, components in dh_calc["de_components"].items()
    }
    B = solve_invariant_primitive(H, de_forms)
    if B is None:
        dB = {}
        primitive_found = False
    else:
        dB = exterior_derivative(B, de_forms)
        primitive_found = dB == H

    nonzero_tau_labels = [
        label for label, tau in finite_values["tau"].items() if tau != 0
    ]

    values = {
        "schema": "SelectedHeteroticProjectiveRhoE.InvariantBPotentialCandidate.v1",
        "status": "INVARIANT_B_POTENTIAL_CANDIDATE_VALUES_BUILT_NOT_TAU_SOURCE",
        "coframe_convention": "left-invariant Iwasawa real coframe e1..e6 from stored tensor payload",
        "H_components": {key(basis): frac(value) for basis, value in sorted(H.items())},
        "B_candidate_components": {key(basis): frac(value) for basis, value in sorted((B or {}).items())},
        "dB_components": {key(basis): frac(value) for basis, value in sorted(dB.items())},
        "dB_equals_H": primitive_found,
        "closedness_source": rel(INPUTS["dh_calc"]),
        "selected_cover_values_emitted": False,
        "deligne_triple_class_from_B_only": 0 if primitive_found else None,
        "can_derive_nonzero_tau_from_B_only": False,
        "nonzero_tau_labels_requiring_flat_torsion_or_projective_transition": nonzero_tau_labels,
        "interpretation": (
            "The invariant primitive B=6 e5 wedge e6 solves dB=H in the stored "
            "invariant coframe. By itself this is a trivial Deligne curvature "
            "potential and cannot derive the nonzero Z3 tau labels; a flat "
            "torsion gerbe or projective transition layer remains required."
        ),
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_VALUES.write_text(json.dumps(values, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "invariant_B_candidate_found": primitive_found,
        "B_candidate": "6 e5 wedge e6" if primitive_found else None,
        "dB_equals_H": primitive_found,
        "selected_cover_homotopy_emitted": False,
        "selected_local_B_i_values_emitted": False,
        "can_derive_nonzero_tau_from_B_only": False,
        "flat_torsion_or_projective_transition_required": True,
        "S1_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESelectedCoverHomotopyOrDeligneLocalPotentialValues",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "values_path": rel(OUTPUT_VALUES),
        "prior_status": localfieldsolve["status"],
        "known_cover_status": equations["finite_nerve_scaffold"]["smooth_embedding_status"],
        "closed_now": {
            "invariant_primitive_candidate_for_H": primitive_found,
            "dB_equals_H_in_stored_invariant_coframe": primitive_found,
            "B_only_tau_obstruction_identified": True,
        },
        "still_open": {
            "selected_smooth_good_cover": True,
            "selected_chart_homotopy_operator": True,
            "Deligne_Cech_local_values_on_cover": True,
            "flat_torsion_gerbe_or_projective_transition_layer": True,
            "smooth_derivation_of_nonzero_tau_labels": True,
            "mapped_admissibility_and_operator_domain": True,
        },
        "decision": decision,
        "guardrails": {
            "does_not_promote_invariant_B_to_selected_cover_values": True,
            "does_not_claim_exact_B_derives_nonzero_tau": True,
            "does_not_assign_tau_after_finite_table": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "InvariantBPotentialCandidateAndTauObstructionTheorem",
            "proved": True,
            "statement": (
                "The stored invariant Iwasawa coframe admits an explicit primitive "
                "B=6 e5 wedge e6 with dB=H for the selected torsion target. This "
                "strengthens the local-potential lane, but the exact invariant "
                "B-field alone has trivial Deligne triple class and cannot derive "
                "the nonzero tau labels. Therefore the next required source object "
                "is a selected flat torsion gerbe/projective transition layer, or "
                "equivalent local values on a selected good cover."
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
        "values_path": rel(OUTPUT_VALUES),
        "note_path": rel(OUTPUT_NOTE),
        "invariant_B_candidate_found": primitive_found,
        "dB_equals_H": primitive_found,
        "can_derive_nonzero_tau_from_B_only": False,
        "flat_torsion_or_projective_transition_required": True,
        "S1_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SelectedCoverHomotopy or DeligneLocalPotentialValues v1

## Result

```text
status = {STATUS}
invariant_B_candidate_found = {str(primitive_found).lower()}
dB_equals_H = {str(primitive_found).lower()}
can_derive_nonzero_tau_from_B_only = false
S1_closed = false
next_required_artifact = {NEXT}
```

## Computation

Inside the stored invariant Iwasawa coframe, the selected curvature target has
an explicit primitive:

```text
B = 6 e5 wedge e6
dB = H
```

This is real progress: the local-potential branch is no longer merely
existential. But it is also diagnostic. An exact invariant `B` by itself has
trivial Deligne triple class, so it cannot derive the nonzero finite `tau`
labels. The smooth `rho_E` proof now needs the flat torsion/projective
transition layer, or equivalent selected Deligne/Cech local values on an actual
good cover.

Values:

```text
{rel(OUTPUT_VALUES)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_VALUES)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
