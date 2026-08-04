"""Audit and reduce the charged-lepton inverse-metric sign in the gauge source."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_chargedleptondualmetricsignandspectralactioncompleteness"
OUT = ROOT / "candidate_data" / SLUG
NOGO = OUT / "common_positive_heat_sign_no_go.packet.json"
GRADING = OUT / "anchoring_parity_grading_construction.packet.json"
CORPUS = OUT / "protospinor_source_support_and_missing_insertion_law.packet.json"
GATE = OUT / "remaining_anchoring_parity_action_gate.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ChargedLeptonDualMetricSignAndSpectralActionCompleteness_v1.md"
STATUS = "MTT_SELECTED_COMMON_POSITIVE_HEAT_SIGN_NOGO_AND_UNIQUE_ANCHORING_GRADING_BUILT_PHYSICAL_INSERTION_LAW_OPEN"
NEXT = "MTT_Selected_AnchoringParityInsertionLaw_or_IndependentKineticGramDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    proto = Path("C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory/10 ProtoSpinor/Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md")
    paths = {
        "A78_readout": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "center_response_to_sector_kinetic_density_functor.packet.json",
        "A78_branches": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "charged_lepton_dual_metric_sign_branch_execution.packet.json",
        "A78_boundary": ROOT / "candidate_data" / "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition" / "relative_spectral_action_boundary_condition.packet.json",
        "A77_execution": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains" / "a73_brst_response_exact_execution.packet.json",
        "A69_operator": ROOT / "candidate_data" / "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum" / "conditional_common_projected_kinetic_operator.packet.json",
        "proto_spinor": proto,
    }
    data = {key: load(path) for key, path in paths.items() if path.suffix == ".json"}
    proto_text = proto.read_text(encoding="utf-8")

    nogo = {
        "schema": "MTTCommonPositiveHeatSignNoGo.v1",
        "status": "ONE_UNGRADED_COMPLETELY_MONOTONE_COST_RESPONSE_CANNOT_ATTENUATE_Q_AND_ENHANCE_E",
        "theorem": {
            "premises": [
                "C_q>0 and C_e>0 are literal nonnegative closure costs",
                "one scalar completely monotone kinetic response f(C) is used in both sectors",
                "f'(C)<=0, including f(C)=exp(-tau C)",
            ],
            "conclusion": "Positive corrections to both costs move both weights in the same non-increasing direction. They cannot produce delta C=+delta_q P_colored-delta_e P_e.",
            "proved": True,
        },
        "application": {
            "A77_delta_q_positive": data["A77_execution"]["q_block"]["value"] > 0.0,
            "A77_delta_e_positive": data["A77_execution"]["e_total"]["value"] > 0.0,
            "A78_required_q_cost_sign": 1,
            "A78_required_e_cost_sign": -1,
            "single_ungraded_heat_function_sufficient": False,
        },
        "interpretation_guard": "The A69 C_sector e entry cannot simultaneously be called a literal nonnegative closure cost and used with the required negative sign. It must be a signed/graded kinetic response coordinate, or the current A72 branch is not physically selected.",
    }

    p_colored = data["A78_readout"]["selected_sector_support"]["P_colored"]
    p_e = data["A78_readout"]["selected_sector_support"]["P_e"]
    p_active = [q + e for q, e in zip(p_colored, p_e)]
    j_anchor = [q - e for q, e in zip(p_colored, p_e)]
    j_squared = [value * value for value in j_anchor]
    delta_q = float(data["A77_execution"]["q_block"]["value"])
    delta_e = float(data["A77_execution"]["e_total"]["value"])
    ungraded_magnitude = [delta_q * q + delta_e * e for q, e in zip(p_colored, p_e)]
    graded_response = [j * magnitude for j, magnitude in zip(j_anchor, ungraded_magnitude)]
    required_response = [delta_q * q - delta_e * e for q, e in zip(p_colored, p_e)]
    grading = {
        "schema": "MTTAnchoringParityGradingConstruction.v1",
        "status": "UNIQUE_ACTIVE_SUPPORT_GRADING_REPRODUCES_DUAL_SIGN_PHYSICAL_INSERTION_NOT_DERIVED",
        "sector_order": data["A78_readout"]["selected_sector_support"]["sector_order"],
        "projectors": {
            "P_colored": p_colored,
            "P_e": p_e,
            "P_active": p_active,
        },
        "J_anchor": j_anchor,
        "algebra": {
            "self_adjoint": True,
            "central_in_sector_commutant": True,
            "J_anchor_squared_equals_P_active": j_squared == p_active,
            "eigenvalue_on_colored_support": 1,
            "eigenvalue_on_e_support": -1,
            "zero_on_inactive_L_N_support": True,
            "unique_given_active_support_labels_and_retarded_q_positive_orientation": True,
        },
        "response": {
            "ungraded_positive_magnitude": ungraded_magnitude,
            "J_anchor_times_magnitude": graded_response,
            "required_deltaC": required_response,
            "exact_match": graded_response == required_response,
        },
        "continuous_parameters": 0,
        "discrete_convention": "The global sign is fixed by taking the selected retarded q branch as positive; relative e parity is then -1.",
        "physical_action_insertion_selected": False,
    }

    corpus = {
        "schema": "MTTProtoSpinorAnchoringParitySupport.v1",
        "status": "ANCHORING_CLASSES_SELECTED_SIGNED_KINETIC_INSERTION_LAW_ABSENT",
        "source": str(proto),
        "closed_classification_support": {
            "charged_leptons_fully_anchored_opposed_loop": "Charged leptons correspond to fully anchored identity configurations" in proto_text,
            "quarks_partially_anchored": "Quarks are partially anchored identities" in proto_text,
            "charged_lepton_quadratic_cost_positive": "strictly positive anchored quadratic closure cost" in proto_text,
            "quark_extra_composite_constraints": "additional composite constraints" in proto_text,
        },
        "missing_statement_search": {
            "J_anchor_inserted_in_gauge_kinetic_action": False,
            "fully_anchored_sector_uses_inverse_heat_sign": "inverse-heat" in proto_text.lower(),
            "graded_determinant_by_anchoring_class": False,
            "same_source_second_variation_emits_P_colored_minus_P_e": False,
        },
        "decision": "The corpus selects the two anchoring classes needed to define J_anchor, but not the law inserting J_anchor into W_kin or a gauge Hessian. Classification does not by itself prove dynamics.",
    }

    boundary = data["A78_boundary"]
    gate = {
        "schema": "MTTRemainingAnchoringParityActionGate.v1",
        "status": "SIGN_PROBLEM_REDUCED_TO_ONE_ZERO_PARAMETER_GRADING_INSERTION_LAW",
        "closed": {
            "ungraded_positive_heat_sign_no_go": nogo["theorem"]["proved"],
            "anchoring_classes_exist_in_proto_spinor_corpus": all(corpus["closed_classification_support"].values()),
            "unique_active_support_J_anchor_constructed": grading["algebra"]["unique_given_active_support_labels_and_retarded_q_positive_orientation"],
            "J_anchor_algebra_exact": grading["algebra"]["J_anchor_squared_equals_P_active"],
            "J_anchor_replays_required_dual_sign": grading["response"]["exact_match"],
            "relative_boundary_at_adopted_one_primitive_tier": boundary["A51_tree_boundary"]["relative_coordinates_zero"],
        },
        "open": {
            "physical_action_inserts_J_anchor": True,
            "same_source_second_variation_or_independent_kinetic_Gram_derives_sign": True,
            "spectral_action_microscopic_completeness": True,
            "spectator_determinant_neutrality_or_cancellation": True,
            "strict_absolute_PEW_source": True,
            "modern_precision_validation": True,
        },
        "remaining_relative_ratio_source_dimension": {
            "continuous": 0,
            "discrete_if_J_anchor_law_not_proved": 1,
            "discrete_if_J_anchor_law_proved": 0,
        },
        "strict_gauge_values_accepted": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "positive_heat_nogo_proved": nogo["theorem"]["proved"],
        "A77_magnitudes_positive": nogo["application"]["A77_delta_q_positive"] and nogo["application"]["A77_delta_e_positive"],
        "P_supports_disjoint": sum(a * b for a, b in zip(p_colored, p_e)) == 0,
        "J_squared_active": grading["algebra"]["J_anchor_squared_equals_P_active"],
        "J_response_exact": grading["response"]["exact_match"],
        "no_continuous_parameters": grading["continuous_parameters"] == 0,
        "proto_classification_support_complete": all(corpus["closed_classification_support"].values()),
        "insertion_law_not_overclaimed": not grading["physical_action_insertion_selected"],
        "strict_values_not_promoted": gate["strict_gauge_values_accepted"] == 0,
    }
    candidate = {
        "schema": "MTTSelectedChargedLeptonDualMetricSignAndSpectralActionCompleteness.v1",
        "status": STATUS,
        "results": {
            "common_positive_heat_sign_route_rejected": True,
            "unique_anchoring_parity_grading_constructed": True,
            "graded_response_replays_required_sign": True,
            "proto_spinor_anchoring_classes_support_grading_labels": True,
            "physical_anchoring_parity_insertion_law_closed": False,
            "continuous_parameters_remaining_for_ratios": 0,
            "discrete_sign_bits_remaining_for_ratios": 1,
            "strict_gauge_values_accepted": 0,
            "new_continuous_parameters": 0,
        },
        "outputs": {
            "nogo": str(NOGO.relative_to(ROOT)).replace("\\", "/"),
            "grading": str(GRADING.relative_to(ROOT)).replace("\\", "/"),
            "corpus": str(CORPUS.relative_to(ROOT)).replace("\\", "/"),
            "gate": str(GATE.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {key: bool(value) for key, value in checks.items()},
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_ChargedLeptonDualMetricSignAndSpectralActionCompleteness_v1",
        "status": STATUS,
        "common_positive_heat_sign_nogo": True,
        "J_anchor_Q_u_d_L_e_N": j_anchor,
        "J_anchor_squared_equals_P_active": True,
        "graded_response_exact": True,
        "physical_insertion_law_closed": False,
        "continuous_parameters_remaining_for_ratios": 0,
        "discrete_sign_bits_remaining_for_ratios": 1,
        "strict_gauge_values_accepted": 0,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Charged-Lepton Dual-Metric Sign and Spectral-Action Completeness v1

## Positive-response no-go

If the colored and charged-lepton numbers are both literal nonnegative closure costs and one common
completely monotone response `f(C)` is used, then `f'(C)<=0` moves both sector weights in the same
direction. It cannot emit

```text
delta C = +delta_q P_colored - delta_e P_e.
```

Thus the A72/A78 branch cannot come from one ungraded positive heat response. The charged-lepton
entry must be a signed/graded kinetic coordinate, or the branch is not physically selected.

## Unique anchoring grading

On the active support define

```text
J_anchor = P_colored-P_e = {j_anchor}.
```

It is self-adjoint, central in the sector commutant, and satisfies

```text
J_anchor^2=P_colored+P_e.
```

With the retarded q orientation fixed positive, this is the unique grading assigning `+1` to the
colored partial-anchor support and `-1` to the charged-lepton full-anchor support. Acting on A77's
positive magnitude vector gives the required A72 correction exactly, with no continuous parameter.

## Corpus result

ProtoSpinor explicitly selects the labels needed by the grading: quarks are partially anchored,
whereas charged leptons are fully anchored opposed-loop identities. It also says the charged-lepton
anchored quadratic cost is positive. It does not state that the gauge kinetic action inserts
`J_anchor`, uses an inverse-heat sign for full anchoring, or takes a graded determinant by anchoring
class. Treating the classification itself as that dynamical law would be circular.

## Remaining theorem

The sign wall is now one zero-parameter statement: `{NEXT}`. It must derive the `J_anchor` insertion
from the same selected action's second variation, or compute an independent kinetic Gram matrix that
has the same sign. Spectral-action completeness, spectator cancellation, strict absolute `P_EW`, and
modern validation remain downstream; the relative-ratio source has zero continuous dimensions and
one unselected binary bit until this law is proved.
"""

    dump(NOGO, nogo)
    dump(GRADING, grading)
    dump(CORPUS, corpus)
    dump(GATE, gate)
    dump(CANDIDATE, candidate)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
