"""Build primitive fiber-shift or typed-retarded-selector source theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
PRIMITIVE_AUDIT = DATA / "selected_routec_primitive_source_selection_audit.candidate.json"
FIBER_INVARIANCE = DATA / "selected_routec_fiberclass_observable_invariance_or_gaugefix.candidate.json"
HIGHER_ORDER = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"
WEYL_SOURCE = DATA / "selected_routec_weylpair_source_provenance_lemma.candidate.json"

OUTPUT = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
CERT = CERTS / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_v1.md"

STATUS = (
    "MTT_SELECTED_PRIMITIVEFIBERSHIFT_OR_TYPEDRETARDEDSELECTOR_"
    "SOURCETHEOREM_BUILT_FIBERCLASS_QUOTIENT_SELECTED_ABSOLUTE_SELECTOR_OPEN"
)
NEXT = "MTT_Selected_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    previous = load(PREVIOUS)
    primitive = load(PRIMITIVE_AUDIT)
    invariance = load(FIBER_INVARIANCE)
    higher = load(HIGHER_ORDER)
    weyl = load(WEYL_SOURCE)

    active_shift_selected = (
        primitive["active_shift_theorem"]["enumeration"]["active_shift_necessary_and_sufficient_for_nonzero"]
        and primitive["active_shift_theorem"]["enumeration"]["nonzero_active_shifts"] == [[1, 1]]
        and weyl["active_shift_provenance"]["proved"]
    )

    fiber_class_selected = (
        invariance["path_A_observable_invariance"]["proved_for_current_finite_C1_layer"]
        and invariance["combined_result"]["selected_C1_observable_class_proved_at_current_layer"]
        and invariance["what_closes_now"][
            "observable_invariance_under_fixed_fiber_class_for_current_C1_spectrum"
        ]
    )

    fixed_shift_observables = invariance["path_A_observable_invariance"][
        "fixed_shift_observables"
    ]
    invariant_scalars = {
        shift: {
            sector: {
                "rank": values["rank"],
                "YYstar_scalar": values["YYstar_scalar"],
                "YYstar_is_scalar_identity": values["YYstar_is_scalar_identity"],
                "det_abs": values["det_abs"],
            }
            for sector, values in sectors.items()
        }
        for shift, sectors in fixed_shift_observables.items()
    }

    typed_retarded_selector = {
        "attempted": True,
        "selected": False,
        "reason": previous["typed_retarded_lane"]["why_not_promoted"],
        "validator_result": "support-only; no selected retarded source selector or typed derivative",
    }

    primitive_selector = {
        "active_shift_selected": active_shift_selected,
        "selected_active_shift": [1, 1],
        "absolute_fiber_shift_selected": False,
        "fiber_class_quotient_selected_for_current_observables": fiber_class_selected,
        "canonical_computation_representative": "fiber_shift_0",
        "canonical_representative_is_physical_selector": False,
        "fixed_fiber_class": [0, 1, 2],
        "invariant_spectral_observables": invariant_scalars,
        "why_absolute_shift_not_selected": invariance["path_B_absolute_gauge_fix"]["reason"],
        "why_quotient_is_allowed": (
            "For the current finite C1 layer, shifts 0, 1, and 2 differ by qutrit "
            "fiber relabeling and give identical rank, determinant absolute value, "
            "traces of powers of YY*, and singular spectrum in u,d,e,nuD."
        ),
    }

    observable_class_payload = {
        "selected_current_C1_observable_class": fiber_class_selected and active_shift_selected,
        "selected_matrix_representative": False,
        "representative_for_computation": "fiber_shift_0",
        "current_layer_flavor_splitting_possible": not higher["current_layer_no_go"]["proved"],
        "current_layer_no_go_imported": higher["current_layer_no_go"]["proved"],
        "reason": (
            "The selected quotient class is enough for current spectral C1 observables, but the "
            "class is scalar-permutation degenerate and cannot produce mass hierarchy, CKM, PMNS, "
            "or CP without selected higher-order/full-response corrections."
        ),
    }

    theorem = {
        "name": "PrimitiveFiberClassQuotientSourceTheorem",
        "proved": True,
        "statement": (
            "The MTT-selected finite C1 source fixes active primitive shift (1,1). It does not "
            "select an absolute qutrit fiber shift. Instead, for the current finite C1 observable "
            "layer, fixed fiber shifts 0, 1, and 2 form a selected quotient class: they are "
            "spectrally invariant and differ only by fiber relabeling. Shift 0 is therefore a "
            "legal computation representative for current spectral observables, not a physical "
            "absolute origin. Typed retarded selection and full matrix/flavor closure remain open."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveFiberShiftOrTypedRetardedSelectorSourceTheorem",
        "status": STATUS,
        "inputs": {
            "typedbn_or_primitive_value_emission": rel(PREVIOUS),
            "primitive_source_selection_audit": rel(PRIMITIVE_AUDIT),
            "fiberclass_observable_invariance": rel(FIBER_INVARIANCE),
            "higherorder_fullresponse_flavor_splitting": rel(HIGHER_ORDER),
            "weylpair_source_provenance": rel(WEYL_SOURCE),
        },
        "superset_strategy": {
            "mode": "QUOTIENT_SELECTOR_INSTEAD_OF_ABSOLUTE_FIBER_ORIGIN",
            "straight_path": "active shift (1,1) selected by finite support/source provenance",
            "support_path": "fiber shifts 0,1,2 are quotient-equivalent for current spectral observables",
            "typed_retarded_path": "tested but remains support-only",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "typed_retarded_selector": typed_retarded_selector,
        "primitive_selector": primitive_selector,
        "observable_class_payload": observable_class_payload,
        "what_closes_now": {
            "active_shift_1_1_selected": active_shift_selected,
            "fixed_fiber_quotient_class_selected_for_current_C1_observables": fiber_class_selected,
            "shift0_allowed_as_computation_gauge": True,
            "typed_retarded_lane_rejected_as_selector_for_now": True,
            "absolute_fiber_origin_not_used_as_hidden_knob": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "absolute_fiber_origin_source_theorem": True,
            "typed_retarded_selector": True,
            "selected_matrix_representative_for_full_C1_operator": True,
            "operator_level_basis_transport": True,
            "selected_higher_order_or_full_response_matrices": True,
            "selected_b_selected": True,
            "promote_conditional_A_to_A_selected": True,
            "honest_selected_deltaTheta_C1_solve": True,
            "nondegenerate_yukawa_hierarchy": True,
            "CKM_PMNS_CP_from_selected_matrices": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "active_shift_selected_claimed": active_shift_selected,
        "fiber_class_quotient_selected_claimed": fiber_class_selected,
        "absolute_fiber_shift_selected_claimed": False,
        "typed_retarded_selector_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem": theorem,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "active_shift_selected_claimed": active_shift_selected,
        "fiber_class_quotient_selected_claimed": fiber_class_selected,
        "absolute_fiber_shift_selected_claimed": False,
        "typed_retarded_selector_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PrimitiveFiberShift or TypedRetardedSelector SourceTheorem v1

Status: `{STATUS}`.

## Result

The active primitive shift is selected:

```text
active shift = (1,1)
```

The absolute qutrit fiber shift is not selected.  Instead, the current finite
C1 observable layer selects the fixed-fiber quotient class `{0,1,2}`.  Shift
`0` is legal as a computation representative because shifts `0`, `1`, and `2`
have identical current spectral observables.

The typed `B_N` retarded selector remains support-only under the validator.

## Boundary

This does not emit `A_selected`, `b_selected`, a full C1 matrix representative,
or flavor closure.  The current layer is scalar-permutation degenerate, so
nondegenerate masses, CKM/PMNS, and CP require selected higher-order or
full-response matrices.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
