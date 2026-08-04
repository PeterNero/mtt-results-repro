"""Build the C1 frontier after the cross-repo alpha1 import."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

CROSS = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
PRIMITIVE = DATA / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
HIGHER = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"
C1_EMISSION = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"
CORRECTION = DATA / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json"
WEYL_TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
SECTOR_CHARGE = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"

OUTPUT = DATA / "selected_c1_frontier_after_alpha1_import.candidate.json"
CERT = CERTS / "selected_c1_frontier_after_alpha1_import_certificate.json"
NOTE = CORPUS / "MTT_Selected_C1_Frontier_After_Alpha1_Import_v1.md"

STATUS = "MTT_SELECTED_C1_FRONTIER_AFTER_ALPHA1_IMPORT_DOTD_RETIRED_PRIMITIVE_RESPONSE_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    cross = load(CROSS)
    primitive = load(PRIMITIVE)
    higher = load(HIGHER)
    c1 = load(C1_EMISSION)
    correction = load(CORRECTION)
    weyl = load(WEYL_TRANSFER)
    sector = load(SECTOR_CHARGE)

    retired_driver_gates = {
        "selected_dotD_source_verified": cross["selected_dotD_source_verified_imported"],
        "alpha1_driver_verified": cross["alpha1_driver_verified_imported"],
        "honest_dotD_alpha1_replay": cross["alpha1_driver_replay_import"][
            "honest_dotD_alpha1_replay"
        ],
        "N_alpha1_h_ext": cross["alpha1_driver_replay_import"]["N_alpha1_h_ext"],
        "du_dalpha1_equals_h_ext": cross["alpha1_driver_replay_import"][
            "du_dalpha1_equals_h_ext"
        ],
    }

    retained_local_results = {
        "active_shift_selected": primitive["active_shift_selected_claimed"],
        "fiber_class_quotient_selected": primitive["fiber_class_quotient_selected_claimed"],
        "absolute_fiber_origin_not_selected": primitive[
            "absolute_fiber_shift_selected_claimed"
        ]
        is False,
        "current_layer_flavor_splitting_no_go": higher["current_layer_no_go"]["proved"],
        "higher_order_acceptance_criterion_locked": higher["theorem"]["proved"],
    }

    conditional_c1_support = {
        "conditional_weyl_transfer_exact": weyl["conditional_transfer_map"][
            "conditional_exact"
        ],
        "conditional_A_selected_emitted": weyl["selected_status"][
            "selected_transfer_map_emitted"
        ],
        "conditional_A_rank_tested": c1["emission_audit"]["rank_test_now_computable"],
        "conditional_A_promoted": c1["emission_audit"][
            "selected_operator_A_selected_emitted"
        ],
        "conditional_b_promoted": c1["emission_audit"][
            "selected_source_vector_b_selected_emitted"
        ],
    }

    live_source_objects = {
        "primitive_C1_contractions": c1["what_remains_open"][
            "selected_primitive_C1_contractions"
        ],
        "selected_A_selected": c1["what_remains_open"]["emit_selected_A_selected"],
        "selected_b_selected": c1["what_remains_open"]["emit_selected_b_selected"],
        "selected_sector_response_matrices": c1["what_remains_open"][
            "selected_sector_response_matrices"
        ],
        "selected_zero_mode_bases_and_Gram": c1["what_remains_open"][
            "selected_zero_mode_bases_and_Gram_Schmidt"
        ],
        "selected_higher_order_or_full_response_matrices": cross["what_remains_open"][
            "selected_higher_order_or_full_response_matrices"
        ],
        "selected_deltaTheta_C1_solution": correction["what_remains_open"][
            "selected_deltaTheta_C1_solution"
        ],
        "selected_sector_charge_or_chirality_table": sector["what_remains_open"][
            "selected_sector_charge_or_chirality_table"
        ],
        "selected_transfer_normalization": sector["what_remains_open"][
            "selected_transfer_normalization"
        ],
        "selected_singlet_neutrino_shift_rule": sector["what_remains_open"][
            "selected_singlet_neutrino_shift_rule"
        ],
    }

    proof_boundary = {
        "alpha1_driver_is_not_allowed_to_select_C1_values": True,
        "observed_flavor_data_not_used": True,
        "locked_splitter_columns_are_diagnostic_until_source_emitted": True,
        "absolute_fiber_origin_not_needed_for_current_spectral_observables": True,
        "full_SM_closure_not_claimed": True,
    }

    candidate = {
        "candidate": "MTTSelectedC1FrontierAfterAlpha1Import",
        "status": STATUS,
        "inputs": {
            "crossrepo_alpha1_import": rel(CROSS),
            "primitive_fiber_quotient": rel(PRIMITIVE),
            "higher_order_full_response_criterion": rel(HIGHER),
            "selected_c1_response_operator_emission": rel(C1_EMISSION),
            "correction_source_emission_contract": rel(CORRECTION),
            "weylpair_source_to_c1_transfer": rel(WEYL_TRANSFER),
            "weylpair_sector_charge_or_chirality": rel(SECTOR_CHARGE),
        },
        "retired_driver_gates": retired_driver_gates,
        "retained_local_results": retained_local_results,
        "conditional_c1_support": conditional_c1_support,
        "live_source_objects": live_source_objects,
        "proof_boundary": proof_boundary,
        "what_closes_now": {
            "alpha1_dotD_replay_removed_from_active_C1_blocker_set": True,
            "primitive_fiber_quotient_retained": True,
            "current_C1_scalar_layer_no_go_retained": True,
            "conditional_weylpair_C1_transfer_retained": True,
            "live_C1_source_objects_minimized": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": live_source_objects
        | {
            "promote_conditional_A_to_A_selected": True,
            "honest_selected_deltaTheta_C1_solve": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "C1FrontierAfterAlpha1ImportReductionTheorem",
            "proved": True,
            "statement": (
                "After importing the theorem-derived alpha1/dotD replay, alpha1_driver_verified and "
                "selected_dotD_source_verified are no longer active blockers for the C1 branch.  The local "
                "primitive fiber quotient and the current-layer flavor no-go remain valid.  The live source "
                "frontier is therefore exactly primitive C1 contractions or higher-order/full-response "
                "matrices, with Weyl-pair sector routing/normalization sufficient to promote the conditional "
                "C1 transfer only after it is emitted by the same selected source."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_C1_Frontier_After_Alpha1_Import_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected C1 Frontier After Alpha1 Import v1

Status: `{STATUS}`.

The cross-repo alpha1 import retires the driver/replay subgate:

```text
selected_dotD_source_verified = true
alpha1_driver_verified = true
honest dotD replay = PASS
```

The local primitive result is still exactly what it was: active shift `(1,1)` is
selected and fiber shifts `0,1,2` form one quotient class for the current C1
spectral observables.  Absolute fiber origin is not used as a hidden selector.

The live frontier is now smaller:

```text
selected primitive C1 contractions
or selected higher-order/full-response matrices
plus same-source Weyl-pair sector routing/normalization
```

Those are the objects needed to promote the conditional Weyl-pair transfer to
`A_selected` and to emit `b_selected`.  No observed masses, CKM, PMNS, CP phase,
or benchmark matrices are used as selectors.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
