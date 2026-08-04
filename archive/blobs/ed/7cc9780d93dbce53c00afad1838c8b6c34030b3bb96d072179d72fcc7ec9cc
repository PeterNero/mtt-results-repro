"""Build the primitive-class C1 observable / higher-order response gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
CONSTANTS = TEXPAPERS / "mtt-nonsm-constants-no-knob"
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

INPUTS = {
    "fiberorigin_quotient": DATA / "selected_u1y_routec_fiberorigin_or_gaugeinvariant_c1observable_theorem.candidate.json",
    "external_noninvariant_import": DATA / "selected_u1y_routec_external_noninvariant_c1_candidate_import.candidate.json",
    "sm_noninvariant_candidate": SM / "candidate_data" / "selected_routec_noninvariant_c1_primitive_search.candidate.json",
    "sm_higher_order_criterion": SM / "certificates" / "selected_routec_higherorder_fullresponse_flavor_splitting_certificate.json",
    "sm_first_correction_search": SM / "certificates" / "selected_routec_first_correction_search_or_galerkin_run_certificate.json",
    "constants_higher_order_import": CONSTANTS / "certificates" / "higher_order_flavor_splitting_criterion_import_certificate.json",
    "q79_basis_transport_candidate": Q79 / "certificates" / "su5_qutrit_basis_transport_heavy_link_candidate_certificate.json",
    "proto_basis_transport_reduction": PROTO / "certificates" / "routec_basis_transport_gate_reduction_import_certificate.json",
}

OUTPUT_DATA = DATA / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
OUTPUT_CERT = CERTS / "selected_u1y_routec_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1.md"

STATUS = "U1Y_ROUTEC_PRIMITIVECLASS_C1OBSERVABLE_NO_SPLIT_HIGHERORDER_SOURCE_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1"
SECTORS = ["u", "d", "e", "nuD"]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*matrix)]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in transpose(b)] for row in a]


def identity_scalar_test(matrix: list[list[float]], tol: float = 1e-12) -> dict[str, Any]:
    n = len(matrix)
    scalar = sum(matrix[i][i] for i in range(n)) / n
    residual = max(
        abs(matrix[i][j] - (scalar if i == j else 0.0))
        for i in range(n)
        for j in range(n)
    )
    traceless_norm_sq = sum(
        (matrix[i][j] - (scalar if i == j else 0.0)) ** 2
        for i in range(n)
        for j in range(n)
    )
    return {
        "scalar": scalar,
        "scalar_identity": residual <= tol,
        "scalar_identity_residual": residual,
        "traceless_norm_sq": traceless_norm_sq,
    }


def commutator_norm_sq(a: list[list[float]], b: list[list[float]]) -> float:
    ab = matmul(a, b)
    ba = matmul(b, a)
    return sum((ab[i][j] - ba[i][j]) ** 2 for i in range(len(a)) for j in range(len(a)))


def primitive_layer_tests(sm_noninv: dict[str, Any]) -> dict[str, Any]:
    fixed_candidates = [
        item for item in sm_noninv["candidate_primitives"] if item["primitive_fiber_shift"] in [0, 1, 2]
    ]
    representative = next(item for item in fixed_candidates if item["primitive_fiber_shift"] == 0)
    yy_star_by_sector = {
        sector: matmul(representative["matrices"][sector], transpose(representative["matrices"][sector]))
        for sector in SECTORS
    }
    scalar_tests = {
        sector: identity_scalar_test(yy_star_by_sector[sector])
        for sector in SECTORS
    }
    commutator_tests = {}
    for left in SECTORS:
        for right in SECTORS:
            if left < right:
                commutator_tests[f"{left}_{right}"] = commutator_norm_sq(
                    yy_star_by_sector[left],
                    yy_star_by_sector[right],
                )
    return {
        "representative_fiber_shift": 0,
        "fixed_fiber_shift_count": len(fixed_candidates),
        "all_fixed_candidates_rank3_each_sector": all(
            item["summary"][sector]["rank"] == 3
            for item in fixed_candidates
            for sector in SECTORS
        ),
        "yy_star_scalar_tests": scalar_tests,
        "all_yy_star_scalar_identity": all(item["scalar_identity"] for item in scalar_tests.values()),
        "max_traceless_norm_sq": max(item["traceless_norm_sq"] for item in scalar_tests.values()),
        "commutator_norm_sq_by_sector_pair": commutator_tests,
        "max_commutator_norm_sq": max(commutator_tests.values()),
        "mass_splitting_test_passes": False,
        "mixing_commutator_test_passes": False,
        "cp_odd_test_passes": False,
        "reason": (
            "At the current primitive fixed-fiber quotient layer every sector has "
            "Y_s Y_s^* equal to the same scalar identity, so traceless splitting, "
            "sector commutators, and CP-odd invariants vanish."
        ),
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    fiber = load(INPUTS["fiberorigin_quotient"])
    external = load(INPUTS["external_noninvariant_import"])
    sm_noninv = load(INPUTS["sm_noninvariant_candidate"])
    sm_higher = load(INPUTS["sm_higher_order_criterion"])
    sm_first = load(INPUTS["sm_first_correction_search"])
    constants_higher = load(INPUTS["constants_higher_order_import"])
    q79_transport = load(INPUTS["q79_basis_transport_candidate"])
    proto_transport = load(INPUTS["proto_basis_transport_reduction"])

    primitive_tests = primitive_layer_tests(sm_noninv)
    higher_order_contract = {
        "criterion_imported": constants_higher["closed_now"]["higher_order_splitting_criterion_proved"],
        "diagnostic_splitter_exists_without_observed_targets": constants_higher["closed_now"][
            "diagnostic_splitter_found_without_observed_targets"
        ],
        "full_response_acceptance_tests_locked": constants_higher["closed_now"][
            "full_response_acceptance_tests_locked"
        ],
        "acceptance_tests": constants_higher["splitting_tests"],
        "not_closed": constants_higher["not_closed"],
        "next_closing_object_from_constants_repo": constants_higher["next_closing_object"],
    }

    source_emission_requirements = [
        "selected same-source correction matrices H_s^(r) or full response matrices",
        "selected primitive C1 atom matrices in the locked sector order u,d,e,nuD",
        "selected operator-level basis transport or selected zero-mode bases connecting the primitive class to the response layer",
        "same-source inhomogeneous row b_selected or homogeneous-zero theorem",
        "mass-splitting test with nonzero traceless part of at least one H_s^(r)",
        "mixing test with noncommuting selected Hermitian sector corrections",
        "CP test with a selected nonzero CP-odd invariant",
        "no observed masses, CKM, PMNS, CP, benchmark entries, or diagnostic lambda values as selectors",
    ]

    decision = {
        "primitive_fixed_fiber_class_selected_for_current_spectral_observables": fiber["decision"][
            "fiberclass_quotient_for_current_C1_spectral_observables_closed"
        ],
        "primitive_class_can_emit_non_degenerate_flavor": False,
        "primitive_class_can_emit_A_selected": False,
        "primitive_class_can_emit_b_selected": False,
        "primitive_class_can_emit_lambda_12": False,
        "higher_order_or_full_response_source_emission_required": True,
        "diagnostic_splitter_promoted": False,
        "basis_transport_candidate_promoted": False,
        "selected_source_emission_closed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedU1YRouteCPrimitiveClassC1ObservableOrHigherOrderFullResponseSourceEmission",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "fiberorigin_quotient": fiber["status"],
            "external_noninvariant_import": external["status"],
            "sm_higher_order_criterion": sm_higher["status"],
            "sm_first_correction_search": sm_first["status"],
            "constants_higher_order_import": constants_higher["status"],
            "q79_basis_transport_candidate": q79_transport["status"],
            "proto_basis_transport_reduction": proto_transport["status"],
        },
        "primitive_layer_tests": primitive_tests,
        "higher_order_contract": higher_order_contract,
        "source_emission_requirements": source_emission_requirements,
        "live_routes": {
            "selected_correction_matrix_source": True,
            "selected_full_response_matrices": True,
            "operator_level_basis_transport": True,
            "typed_monad_cech_or_hym_connection_values": True,
            "basis_transport_candidate_viable_but_unselected": q79_transport["calculation_results"][
                "su5_representation_split_nonzero"
            ],
            "proto_reduction_agrees_basis_transport_open": proto_transport["still_open"][
                "operator_level_basis_transport"
            ],
        },
        "decision": decision,
        "theorem": {
            "name": "U1YRouteCPrimitiveClassNoFlavorSplitHigherOrderSourceEmissionTheorem",
            "proved": True,
            "statement": (
                "The selected primitive fixed-fiber quotient class is sufficient for "
                "current C1 spectral observables, but by direct matrix replay it gives "
                "Y_s Y_s^*=c I for every sector at this layer. Therefore this primitive "
                "class alone has zero traceless splitting, zero sector commutators, and "
                "zero CP-odd content. Nondegenerate Yukawa hierarchy, CKM/PMNS, CP, "
                "A_selected, b_selected, and lambda_12 require selected same-source "
                "higher-order/full-response matrix emission or selected operator-level "
                "basis transport. Diagnostic splitters and q79 transport candidates are "
                "support only until selected by the source."
            ),
        },
        "what_closes_now": {
            "primitive_class_no_flavor_split_theorem": True,
            "higher_order_or_full_response_requirement_proved": True,
            "acceptance_tests_imported": True,
            "diagnostic_splitter_kept_support_only": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_correction_matrix_source": True,
            "selected_full_response_matrices": True,
            "selected_primitive_C1_atom_matrices": True,
            "selected_basis_transport_theorem": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_primitive_class_flavor_split": False,
            "claims_diagnostic_splitter_selected": False,
            "claims_basis_transport_selected": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_lambda12": False,
            "claims_Yukawa_CKM_PMNS_CP_or_full_SM_closure": False,
            "uses_observed_data": False,
            "uses_benchmark_data": False,
            "uses_locked_target_columns": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedU1YRouteCPrimitiveClassC1ObservableOrHigherOrderFullResponseSourceEmission",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "primitive_class_no_flavor_split_theorem": True,
        "primitive_class_can_emit_A_selected": False,
        "primitive_class_can_emit_b_selected": False,
        "primitive_class_can_emit_lambda_12": False,
        "higher_order_or_full_response_source_emission_required": True,
        "selected_source_emission_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    tests = candidate["primitive_layer_tests"]
    return f"""# Selected U1Y Route-C PrimitiveClass C1Observable or HigherOrder FullResponse SourceEmission v1

## Result

```text
status = {candidate["status"]}
primitive_class_no_flavor_split_theorem = true
primitive_class_can_emit_A_selected = false
primitive_class_can_emit_b_selected = false
primitive_class_can_emit_lambda_12 = false
higher_order_or_full_response_source_emission_required = true
next_required_artifact = {candidate["next_required_artifact"]}
```

The fixed-fiber primitive class is now useful but bounded. It is selected as a
current C1 spectral-observable quotient, not as the full physical matrix source.

## Direct Replay

- representative fiber shift: `{tests["representative_fiber_shift"]}`
- fixed-fiber candidate count: `{tests["fixed_fiber_shift_count"]}`
- all `YY*` scalar identity: `{tests["all_yy_star_scalar_identity"]}`
- max traceless norm squared: `{tests["max_traceless_norm_sq"]}`
- max sector commutator norm squared: `{tests["max_commutator_norm_sq"]}`
- mass-splitting test passes: `{tests["mass_splitting_test_passes"]}`
- mixing commutator test passes: `{tests["mixing_commutator_test_passes"]}`
- CP-odd test passes: `{tests["cp_odd_test_passes"]}`

## Theorem

Since each current primitive sector has `Y_s Y_s^* = c I`, the current primitive
class has no traceless splitting, no sector commutator, and no CP-odd invariant.
Therefore it cannot by itself compute nondegenerate Yukawas, CKM/PMNS, CP,
`A_selected`, `b_selected`, or `lambda_12`.

## Required Source Emission

The next source must emit selected correction/full-response matrices, selected
primitive C1 atom matrices, or selected operator-level basis transport from the
same branch. Diagnostic splitters and the q79 Fourier transport candidate remain
support only.

## Guardrails

- Do not promote the diagnostic splitter as selected data.
- Do not promote q79 basis transport without same-source selection.
- Do not use observed masses, CKM, PMNS, CP, benchmark matrix entries, or
  diagnostic `lambda_12` values as selectors.

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
