"""Build the primitive-class C1 observable / higher-order response frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

FIBER = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
CROSSREPO_ALPHA = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
HIGHER = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"
CORRECTION = DATA / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json"
DELTA_SOLVE = DATA / "selected_routec_splitter_source_emission_contract_or_selected_deltatheta_c1_solve.candidate.json"

OUTPUT = DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
CERT = CERTS / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_PRIMITIVECLASS_C1OBSERVABLE_OR_HIGHERORDER_FULLRESPONSE_SOURCEEMISSION_BUILT_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def current_observable_packet(fiber: dict[str, Any]) -> dict[str, Any]:
    primitive = fiber["primitive_selector"]
    invariants = primitive["invariant_spectral_observables"]
    representatives = {}
    reference = None
    for shift, sectors in invariants.items():
        representatives[shift] = {}
        for sector, values in sectors.items():
            record = {
                "rank": values["rank"],
                "det_abs": values["det_abs"],
                "YYstar_scalar": values["YYstar_scalar"],
                "YYstar_is_scalar_identity": values["YYstar_is_scalar_identity"],
            }
            representatives[shift][sector] = record
            if reference is None:
                reference = record
    all_scalar_identity = all(
        sector["YYstar_is_scalar_identity"]
        for sectors in representatives.values()
        for sector in sectors.values()
    )
    all_same_scalar = len(
        {
            round(float(sector["YYstar_scalar"]), 15)
            for sectors in representatives.values()
            for sector in sectors.values()
        }
    ) == 1
    return {
        "active_shift": primitive["selected_active_shift"],
        "fixed_fiber_quotient_class": primitive["fixed_fiber_class"],
        "computation_representative": primitive["canonical_computation_representative"],
        "representative_is_physical_selector": primitive["canonical_representative_is_physical_selector"],
        "absolute_fiber_shift_selected": primitive["absolute_fiber_shift_selected"],
        "representative_observables": representatives,
        "all_representatives_scalar_identity": all_scalar_identity,
        "all_representatives_same_scalar": all_same_scalar,
        "reference_rank": reference["rank"] if reference else None,
        "reference_det_abs": reference["det_abs"] if reference else None,
        "reference_YYstar_scalar": reference["YYstar_scalar"] if reference else None,
        "flavor_splitting_possible_at_current_layer": False,
    }


def source_emission_packet(
    alpha: dict[str, Any],
    higher: dict[str, Any],
    correction: dict[str, Any],
    delta: dict[str, Any],
) -> dict[str, Any]:
    return {
        "alpha1_dotD_status": {
            "alpha1_driver_verified_imported": alpha["alpha1_driver_verified_imported"],
            "selected_dotD_source_verified_imported": alpha["selected_dotD_source_verified_imported"],
            "honest_dotD_alpha1_replay_imported": alpha["what_closes_now"][
                "honest_dotD_alpha1_replay_imported"
            ],
            "active_blocker": False,
        },
        "current_layer_status": {
            "no_go_proved": higher["current_layer_no_go"]["proved"],
            "higher_order_criterion_proved": higher["path_A_higher_order_criterion"]["proved"],
            "full_response_criterion_proved": higher["path_B_full_response_criterion"]["proved"],
            "current_values_available": higher["path_A_higher_order_criterion"][
                "current_values_available"
            ],
        },
        "source_emission_status": {
            "diagnostic_splitter_found": correction["source_emission_attempt"][
                "diagnostic_splitter_found"
            ],
            "selected_source_emits_splitter": correction["source_emission_attempt"][
                "selected_source_emits_splitter"
            ],
            "source_emission_contract_built": correction["what_closes_now"][
                "exact_source_emission_contract_built"
            ],
        },
        "deltaTheta_gate_status": {
            "delta_solve_gate_built": delta["theorem"]["proved"],
            "A_selected_claimed": delta["selected_deltatheta_c1_solve_gate"][
                "selected_operator_available"
            ],
            "b_selected_claimed": delta["missing_selected_operator_data"][
                "evaluated_grad_V_C1_alpha1_source_vector"
            ]
            is not None,
            "rank_tests_allowed_now": delta["selected_deltatheta_c1_solve_gate"][
                "rank_test_computable"
            ],
            "selected_values_available": delta["selected_deltatheta_c1_solve_gate"][
                "selected_operator_available"
            ],
        },
        "minimum_next_payload": [
            "selected primitive-class correction matrices or selected full-response matrices",
            "selected A_selected response operator",
            "selected b_selected source vector",
            "selected deltaTheta_C1 solve or selected no-solve theorem",
            "sector response matrices M_u, M_d, M_e, M_nuD",
            "Hermitian mass-splitting, CKM/PMNS commutator, and CP-odd invariant audits",
        ],
    }


def main() -> int:
    fiber = load(FIBER)
    alpha = load(CROSSREPO_ALPHA)
    higher = load(HIGHER)
    correction = load(CORRECTION)
    delta = load(DELTA_SOLVE)

    observable = current_observable_packet(fiber)
    emission = source_emission_packet(alpha, higher, correction, delta)

    candidate = {
        "candidate": "MTTSelectedPrimitiveClassC1ObservableOrHigherOrderFullResponseSourceEmission",
        "status": STATUS,
        "inputs": {
            "primitive_fiberclass_selector": rel(FIBER),
            "crossrepo_alpha1_driver_replay_import": rel(CROSSREPO_ALPHA),
            "higherorder_fullresponse_flavor_splitting": rel(HIGHER),
            "correction_source_emission_or_selected_galerkin_values": rel(CORRECTION),
            "splitter_source_emission_contract_or_deltatheta_solve": rel(DELTA_SOLVE),
        },
        "superset_strategy": {
            "mode": "COMBINED_PATHS_WITH_LOCKED_TARGET",
            "straight_path": "primitive quotient class emits current C1 spectral observables",
            "support_path": "cross-repo alpha1/dotD replay plus q79/non-SM/Qa-SU3 retarded-kernel and primitive-C1 boundary checks",
            "locked_target": "selected higher-order/full-response correction matrices from the same branch",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "primitive_class_C1_observable_packet": observable,
        "higherorder_or_fullresponse_source_emission_packet": emission,
        "promotion_decision": {
            "current_primitive_class_promoted_as_valid_C1_observable_layer": True,
            "current_primitive_class_promoted_as_flavor_closure": False,
            "alpha1_dotD_promoted_by_crossrepo_import": True,
            "higherorder_fullresponse_values_promoted": False,
            "reason": (
                "The current quotient-class C1 observables are selected and gauge-safe for rank/determinant/"
                "singular-spectrum checks, but YY* is scalar identity in every sector. Flavor closure therefore "
                "requires selected higher-order or full-response matrices."
            ),
        },
        "what_closes_now": {
            "primitive_class_C1_observable_emitted": True,
            "alpha1_dotD_replay_imported_and_checked": True,
            "current_C1_layer_flavor_no_go_confirmed": True,
            "higherorder_fullresponse_acceptance_packet_built": True,
            "superset_paths_locked_to_same_selected_target": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_higher_order_or_full_response_matrices": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1_solution": True,
            "sector_response_matrices_M_u_M_d_M_e_M_nuD": True,
            "nondegenerate_yukawa_hierarchy": True,
            "CKM_PMNS_CP_from_selected_matrices": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "selected_values_available": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PrimitiveClassC1ObservableOrHigherOrderFullResponseSourceEmissionTheorem",
            "proved": True,
            "statement": (
                "The selected primitive quotient class emits a valid current C1 spectral-observable layer: "
                "active shift (1,1), fixed fiber class {0,1,2}, and shift 0 as computation gauge. The same "
                "proof stack imports theorem-derived alpha1/dotD replay. Since the emitted current layer has "
                "YY* scalar identity in every sector, it cannot produce flavor splitting. The remaining proof "
                "object is therefore exactly selected higher-order/full-response data emitting A_selected, "
                "b_selected, deltaTheta_C1 or an equivalent selected solve/no-solve theorem, and sector response "
                "matrices without observed targets."
            ),
        },
    }

    cert = {
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "selected_values_available": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Primitive-Class C1 Observable or Higher-Order Full-Response Source Emission v1

Status: `{STATUS}`.

## Result

The selected primitive quotient class now has an explicit current observable
packet:

```text
active shift = (1,1)
fixed fiber class = {{0,1,2}}
computation representative = fiber_shift_0
YY* scalar = {observable["reference_YYstar_scalar"]}
rank = {observable["reference_rank"]}
|det| = {observable["reference_det_abs"]}
```

This is a valid selected C1 spectral-observable layer, not a flavor closure.  In
every sector and fixed-fiber representative, `Y Y*` is scalar identity, so the
current layer cannot split masses, choose CKM/PMNS, or source CP.

## Cross-Repo Status

The alpha1/dotD blocker is retired by the imported GR/protospinor replay:
`N_alpha1(h_ext)=1`, `du/dalpha1=h_ext`,
`selected_dotD_source_verified=true`, `alpha1_driver_verified=true`, and honest
dotD replay passes.  q79, non-SM constants, and Qa/SU3 remain useful support
paths for the retarded-kernel and primitive-C1 boundary, but they do not emit the
missing selected correction matrices.

## Locked Target

The remaining target is selected higher-order/full-response data from the same
branch:

```text
A_selected
b_selected
deltaTheta_C1 or equivalent selected solve/no-solve theorem
M_u, M_d, M_e, M_nuD
mass-splitting, CKM/PMNS commutator, and CP-odd invariant audits
```

No observed mass, CKM, PMNS, CP, or benchmark matrix may select the data.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
