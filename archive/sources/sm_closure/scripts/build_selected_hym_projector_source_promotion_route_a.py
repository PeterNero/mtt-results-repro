"""Attempt Route A: promote model-active B_N projector values to selected HYM data.

Route A asks whether the finite projector values already emitted on the smooth
B_N scaffold can be proved to be the selected HYM/Strominger truncation.  The
answer in the current repository is still no, but the failure is now sharply
localized: finite values and equivariance pass; selected-source provenance via
Phi_fin/full minimizer trace is still absent.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

VALUE_EMISSION = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
SOURCE_ORIGIN = DATA / "routec_selected_source_origin_lemma.candidate.json"
PHIFIN = DATA / "finite_emission_morphism_phifin.candidate.json"
HYM_VALUES_GATE = DATA / "selected_routec_hym_operator_values_gate.candidate.json"
HYM_EXTRACTION = DATA / "selected_hym_connection_to_finite_operator_extraction.candidate.json"
GAUGEFIXED = DATA / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json"

OUTPUT = DATA / "selected_hym_projector_source_promotion_route_a.candidate.json"
CERT = CERTS / "selected_hym_projector_source_promotion_route_a_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYM_Projector_SourcePromotion_Route_A_v1.md"

STATUS = "MTT_SELECTED_HYM_PROJECTOR_SOURCE_PROMOTION_ROUTE_A_REDUCED_TO_PHIFIN_TRACE"
NEXT = "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    value = load(VALUE_EMISSION)
    source_origin = load(SOURCE_ORIGIN)
    phifin = load(PHIFIN)
    hym_values = load(HYM_VALUES_GATE)
    extraction = load(HYM_EXTRACTION)
    gaugefixed = load(GAUGEFIXED)

    validator = value["validator_result"]
    flags = validator["selected_source_flags"]

    route_a_gate_matrix = {
        "A1_selected_topological_branch_fixed": {
            "passes": source_origin["gate_matrix"]["G1_fixed_topological_sector_named"]["passes"],
            "evidence": source_origin["gate_matrix"]["G1_fixed_topological_sector_named"]["evidence"],
        },
        "A2_strominger_selection_available": {
            "passes": source_origin["gate_matrix"]["G2_MTT_Strominger_selection_available"]["passes"],
            "evidence": source_origin["gate_matrix"]["G2_MTT_Strominger_selection_available"]["evidence"],
        },
        "A3_finite_BN_projector_values_clean": {
            "passes": (
                validator["finite_projector_values_emitted"]
                and validator["all_projector_checks_pass"]
                and validator["all_basis_counts_pass"]
                and validator["positive_complement_gap"]
                and validator["End0_equivariance_on_emitted_projectors"]
            ),
            "evidence": {
                "ambient_dimension": value["finite_value_payload"]["ambient_dimension"],
                "basis_id": value["finite_value_payload"]["basis_id"],
                "zero_cluster": value["finite_value_payload"]["zero_cluster"],
                "complement_gap": value["finite_value_payload"]["complement_gap"],
            },
        },
        "A4_PhiFin_selected_trace_emitted": {
            "passes": phifin["obstruction"]["selected_payload_closed"],
            "missing": phifin["obstruction"]["minimum_new_selected_data"],
        },
        "A5_honest_operator_flags_promote": {
            "passes": all(flags.values()),
            "flags": flags,
        },
        "A6_full_selected_strominger_operator_identified_with_BN_model_active": {
            "passes": False,
            "reason": (
                "Existing HYM extraction and gauge-fixed solve artifacts still request selected "
                "connection representative, finite basis/quadrature/error contract, and actual "
                "operator values; they do not prove equality with the model-active B_N operator."
            ),
            "extraction_status": extraction["status"],
            "gaugefixed_status": gaugefixed["status"],
        },
    }

    route_a_promotes = all(gate["passes"] for gate in route_a_gate_matrix.values())

    theorem_attempt = {
        "name": "SelectedHYMProjectorSourcePromotionRouteA",
        "route_A_statement": (
            "If Phi_fin proves that the selected q79/F,m=1 S3/GS HYM/Strominger minimizer "
            "has the emitted smooth B_N model-active operator as its finite Galerkin trace, "
            "then selected_source_verified, selected_dotD_source_verified, and alpha1_driver_verified "
            "may be set true for the corresponding finite projector packet."
        ),
        "proved_now": False,
        "why_not_proved_now": [
            "Phi_fin schema is built but selected payload is still open",
            "honest D_E, Riesz/Green, and dotD validators still fail on selected-source flags",
            "the full selected HYM/Strominger operator has not been proved equal to the model-active B_N operator",
            "alpha1_driver_verified is not theorem-derived from the selected Hessian/C1 source",
        ],
        "conditional_promotion_rule": {
            "recorded": True,
            "condition": (
                "Phi_fin emits a selected minimizer trace whose D_E, Riesz/Green, projectors, "
                "dotD_alpha1, and gap/error contracts agree with the finite B_N packet."
            ),
            "then": (
                "the finite projector packet promotes to selected HYM projector values, and the "
                "previous bridge theorem promotes rho_candidate to selected rho_s."
            ),
        },
    }

    superset_strategy = {
        "classification": "ROUTE_A_SUPERSET_PROMOTION_ATTEMPT_REDUCED_NOT_CLOSED",
        "straight_End0_BN_value_path": {
            "role": "validates projector ranks, zero-mode bases, positive gap, and End0 equivariance",
            "status": "closed at finite model-active level",
        },
        "HYM_Strominger_selection_path": {
            "role": "supplies the selected smooth minimizer/source",
            "status": "existence and fixed-sector support present, finite trace not emitted",
        },
        "PhiFin_trace_path": {
            "role": "the only legal bridge from selected minimizer to finite B_N operator values",
            "status": "schema built, selected values open",
        },
        "q79_S3_GS_Theta_SU5_constraints": {
            "role": "constrain branch, gerbe/source class, orientation, and later matter routing",
            "status": "support only; not used to flip source flags",
        },
        "uses_observed_constants": False,
    }

    data = {
        "candidate": "MTTSelectedHYMProjectorSourcePromotionRouteA",
        "status": STATUS,
        "inputs": {
            "value_emission": rel(VALUE_EMISSION),
            "source_origin": rel(SOURCE_ORIGIN),
            "phifin": rel(PHIFIN),
            "hym_values_gate": rel(HYM_VALUES_GATE),
            "hym_extraction": rel(HYM_EXTRACTION),
            "gaugefixed": rel(GAUGEFIXED),
        },
        "route_a_gate_matrix": route_a_gate_matrix,
        "route_a_promotes_now": route_a_promotes,
        "theorem_attempt": theorem_attempt,
        "honest_source_flags": flags,
        "validator_status": {
            "finite_projector_values_pass": route_a_gate_matrix["A3_finite_BN_projector_values_clean"]["passes"],
            "hym_operator_values_closed": hym_values["selected_operator_values_closed"],
            "phifin_selected_payload_closed": phifin["obstruction"]["selected_payload_closed"],
            "routec_source_origin_fully_proved": source_origin["lemma_evaluation"]["fully_proved"],
        },
        "superset_strategy": superset_strategy,
        "what_closes_now": {
            "route_A_finite_value_side_closed": True,
            "route_A_source_promotion_blocker_localized": True,
            "conditional_source_promotion_rule_recorded": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "Phi_fin_selected_minimizer_trace": True,
            "full_selected_HYM_Strominger_operator_values": True,
            "selected_source_verified": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "selected_rho_s_actual_promotion": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_HYM_Projector_SourcePromotion_Route_A_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "route_A_promotes_now": route_a_promotes,
        "finite_value_side_closed": True,
        "source_promotion_closed": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected HYM Projector SourcePromotion Route A v1

Status: `{STATUS}`.

## Route A Question

Can the clean model-active `B_N` projector packet be promoted to the selected
HYM/Strominger projector packet?

Current answer: not yet.

## What Route A Closes

The finite side is closed:

```text
ambient dimension = {value["finite_value_payload"]["ambient_dimension"]}
basis = {value["finite_value_payload"]["basis_id"]}
zero cluster = {value["finite_value_payload"]["zero_cluster"]["basis_ids"]}
gap = {value["finite_value_payload"]["complement_gap"]}
projector checks pass = {validator["all_projector_checks_pass"]}
End0 equivariance passes = {validator["End0_equivariance_on_emitted_projectors"]}
```

So the obstruction is not rank, basis, gap, or equivariance.

## What Blocks Promotion

The selected-source side is still open:

```text
selected_source_verified = {flags["de_action_selected_source_verified"]}
selected_dotD_source_verified = {flags["dotd_selected_dotD_source_verified"]}
alpha1_driver_verified = {flags["dotd_alpha1_driver_verified"]}
Phi_fin selected payload closed = {phifin["obstruction"]["selected_payload_closed"]}
```

Therefore Route A reduces to the selected `Phi_fin` trace/equivalence theorem:
prove that the selected q79/F,m=1 S3/GS HYM/Strominger minimizer has the emitted
smooth `B_N` model-active packet as its finite Galerkin trace, including
`D_E`, Riesz/Green, projectors, `dotD_alpha1`, and gap/error contracts.

## Superset Use

This uses the superset correctly:

- `End0` plus `B_N` closes the finite value side,
- HYM/Strominger supplies the selected minimizer,
- `Phi_fin` must bridge the selected minimizer to finite values,
- q79/S3/GS/Theta/SU5 data constrain the branch and later routing but do not
  flip source flags.

No measured constants, benchmark matrices, residual target fitting, or lifted
flags are used as proof.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
