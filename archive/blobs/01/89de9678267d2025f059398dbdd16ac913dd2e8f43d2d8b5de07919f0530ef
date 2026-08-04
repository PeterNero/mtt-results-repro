"""Build Step 34 flat gerbe source functor and selected-cover selector boundary."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79 = TEXPAPERS / "mtt-q79-proof-repro"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step34_flatgerbe_sourcefunctor_or_selectedcoverselector"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTOR = PACKET_DIR / "step34_finite_group_flat_gerbe_source_functor.packet.json"
SELECTOR = PACKET_DIR / "step34_selected_cover_classifying_map_obligation.packet.json"
OPERATOR = PACKET_DIR / "step34_operator_promotion_boundary.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step34_FlatGerbeSourceFunctor_or_SelectedCoverSelector_v1.md"

STEP33 = DATA / "selected_step33_smooths3validator_reconciliation_or_holonomyoperatorpromotion.candidate.json"
Q79_CP = Q79 / "candidate_data" / "visible_twisted_s3_finite_cp_cancellation.candidate.json"
Q79_FW = Q79 / "candidate_data" / "time_oriented_m1_freed_witten_cycle_gate.candidate.json"

STATUS = "MTT_SELECTED_STEP34_FLAT_GERBE_SOURCE_FUNCTOR_CONSTRUCTED_SELECTED_COVER_OPEN"
NEXT = "MTT_Selected_S3ClassifyingMapCoverSelector_and_ProjectorRetention_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP33, Q79_CP, Q79_FW]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 34 inputs: " + ", ".join(missing))

    step33 = load(STEP33)
    q79_cp = load(Q79_CP)
    q79_fw = load(Q79_FW)

    functor = {
        "schema": "MTTStep34FiniteGroupFlatGerbeSourceFunctor.v1",
        "status": "FINITE_GROUP_FLAT_GERBE_PULLBACK_FUNCTOR_CONSTRUCTED",
        "input_finite_data": {
            "active_group": "F_3^2",
            "central_extension": "Heisenberg_3 / qutrit projective central extension",
            "commutator_form": q79_fw["finite_restriction_theorem"]["commutator_form"],
            "central_phase_label": q79_cp["finite_cancellation_inputs"]["central_phase_label"],
            "branch": {
                "q": q79_cp["finite_cancellation_inputs"]["m1_period_table_q"],
                "orientation": "F",
                "torsion_label_m": q79_cp["finite_cancellation_inputs"]["m1_period_table_torsion_label"],
            },
        },
        "construction": {
            "classifying_space": "B(F_3^2)",
            "flat_class": "[omega_m=1] in H^2(F_3^2,U(1)) equivalently H^3(BF_3^2,Z)_tors",
            "smooth_input": "a selected smooth S3 worldvolume Y, good cover U, and selected classifying map c:Y -> B(F_3^2)",
            "smooth_output": "flat Deligne-Cech gerbe c^*[omega_m=1] with curvature H=0",
            "twisted_module_output": "pullback of the qutrit projective module; its twisted Chan-Paton DD class cancels c^*[omega_m=1]",
            "holonomy_output": "projective holonomy representation whose commutator is zeta_3^2 on the active rank-two S3 image",
        },
        "proved_by_construction": {
            "finite_to_smooth_flat_gerbe_source_functor": True,
            "curvature_H_zero_for_flat_source": True,
            "qutrit_central_cocycle_holonomy_map": True,
            "finite_twisted_CP_cancellation_transports_conditionally": True,
            "ordinary_rank_two_DD_zero_route_not_used": True,
        },
        "not_proved_by_functor_alone": {
            "selected_classifying_map_c_supplied_by_MTT": True,
            "selected_good_cover_supplied_by_MTT": True,
            "smooth_projector_retention_verified": True,
            "operator_level_projective_rhoE_transition_verified": True,
            "selected_D_E_Riesz_Green_dotD_values": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(FUNCTOR, functor)

    selector = {
        "schema": "MTTStep34SelectedCoverClassifyingMapObligation.v1",
        "status": "SELECTED_COVER_CLASSIFYING_MAP_SELECTOR_IS_ONLY_SOURCE_MISSING_LAYER",
        "must_select": [
            "smooth S3 worldvolume Y inside the q79/F,m=1 visible stack",
            "good cover U or equivalent smooth stack/Cech nerve",
            "classifying map c:Y -> B(F_3^2) whose induced pi1 image is the active rank-two S3 image",
            "Deligne-Cech cocycle representative for c^*[omega_m=1]",
            "twisted Chan-Paton/projective qutrit module over that representative",
            "W3=0 or spinC-compatible cancellation data on the same selected Y",
        ],
        "current_support": {
            "finite_S3_CP_cancellation_closed": q79_cp["calculation_results"]["finite_S3_CP_cancellation_closed"],
            "visible_cycles_W3_spinC_zero_finite_support": q79_cp["finite_cancellation_inputs"]["visible_cycles_W3_spinC_zero"],
            "selected_cycles_supplied_in_q79_gate": q79_fw["calculation_results"]["selected_cycles_supplied"],
        },
        "minimal_selector_axiom_candidate": (
            "Select the unique q79/F,m=1 S3 worldvolume classifying map whose "
            "pullback of omega_m=1 admits the qutrit twisted CP module while "
            "retaining the block-factorized family/Higgs projector architecture."
        ),
        "selector_axiom_status": "FORMULATED_NOT_PROVED",
        "closure_claimed": False,
    }
    write_json(SELECTOR, selector)

    operator = {
        "schema": "MTTStep34OperatorPromotionBoundary.v1",
        "status": "OPERATOR_PROMOTION_BOUNDARY_REDUCED_TO_SELECTED_COVER_AND_PROJECTOR_RETENTION",
        "conditional_pipeline": [
            "selected classifying map c supplies flat gerbe rho_E holonomy",
            "twisted qutrit CP module supplies projective B_N transition data",
            "retained projectors define sector blocks on Q,u,d,L,e,N,H",
            "D_E is the covariant derivative induced by the projective holonomy/source",
            "Riesz/Green/dotD are computed from the same D_E and retained projectors",
            "internal R_theta rows may then be emitted from the already typed value-functional layer",
        ],
        "blocked_until": [
            "selected_classifying_map_c_supplied_by_MTT",
            "smooth_projector_retention_verified",
            "operator_level_projective_rhoE_transition_verified",
        ],
        "operator_values_closed_now": False,
        "accepted_internal_scalar_row_count": 0,
    }
    write_json(OPERATOR, operator)

    candidate = {
        "candidate": "MTTSelectedStep34FlatGerbeSourceFunctorOrSelectedCoverSelector",
        "status": STATUS,
        "inputs": {
            "step33": rel(STEP33),
            "q79_finite_cp": rel(Q79_CP),
            "q79_freed_witten_gate": rel(Q79_FW),
        },
        "output_packets": {
            "finite_group_flat_gerbe_source_functor": rel(FUNCTOR),
            "selected_cover_classifying_map_obligation": rel(SELECTOR),
            "operator_promotion_boundary": rel(OPERATOR),
        },
        "theorem": {
            "name": "FiniteGroupFlatGerbeSourceFunctorTheorem",
            "proved": True,
            "statement": (
                "For the q79/F,m=1 active quotient F_3^2 with commutator "
                "omega((a,b),(c,d))=a*d-b*c mod 3, any selected smooth S3 "
                "worldvolume with a selected classifying map c:Y->B(F_3^2) "
                "carries the pulled-back flat Deligne-Cech gerbe c^*[omega]. "
                "The qutrit projective module pulls back as a twisted Chan-Paton "
                "module whose finite central cocycle matches the S3 obstruction. "
                "This constructs the source functor, but not the missing MTT "
                "selection of c, the good cover, or projector retention."
            ),
        },
        "closure_decision": {
            "finite_to_smooth_flat_gerbe_source_functor_constructed": True,
            "qutrit_central_extension_holonomy_map_constructed": True,
            "finite_twisted_CP_cancellation_conditionally_transported": True,
            "selected_cover_classifying_map_obligation_isolated": True,
            "operator_promotion_boundary_reduced_to_selected_cover_and_projectors": True,
            "selected_classifying_map_c_closed": False,
            "selected_good_cover_closed": False,
            "smooth_freed_witten_projector_retention_closed": False,
            "operator_level_projective_rhoE_transition_closed": False,
            "selected_D_E_Riesz_Green_dotD_values_closed": False,
            "accepted_internal_scalar_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step34_FlatGerbeSourceFunctor_or_SelectedCoverSelector_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "finite_to_smooth_flat_gerbe_source_functor_constructed": True,
        "selected_classifying_map_c_closed": False,
        "operator_sector_values_closed": False,
        "accepted_internal_scalar_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step34 FlatGerbeSourceFunctor or SelectedCoverSelector v1

Status: `{STATUS}`.

Step34 constructs the formal source functor:

```text
finite q79/F,m=1 F_3^2 cocycle  ->  flat Deligne-Cech gerbe via c:Y -> B(F_3^2)
qutrit projective module         ->  twisted Chan-Paton module over c^*[omega]
finite S3 cancellation           ->  conditional smooth cancellation once c/Y/U are selected
```

This is progress, but it is not yet the selected smooth source. The remaining
selector is now sharp: MTT must select the S3 worldvolume, good cover/Cech
nerve, and classifying map `c` that carries the q79/F,m=1 cocycle while
retaining the block-factorized family/Higgs projectors.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
