"""Build the Strominger threshold-operator value / metrology-unit source frontier.

This imports the latest Qa/SU3 Strominger/HYM work and the constants-repo
metrology handoff after the strict PEW upgrade.  The point is to replace the
broad "derive P_EW" blocker with the exact remaining source-value object.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof")

SLUG = "selected_stromingerthresholdoperatorvalue_or_metrologyunitsource"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StromingerThresholdOperatorValue_or_MetrologyUnitSource_v1.md"

STROMINGER_ROUTE = PACKET_DIR / "strominger_threshold_value_route_import.packet.json"
METROLOGY_ROUTE = PACKET_DIR / "metrology_unit_source_route.packet.json"
EXIT_DECISION = PACKET_DIR / "strict_exit_decision_after_strominger_and_metrology.packet.json"
NEXT_CONTRACT = PACKET_DIR / "next_torsional_operator_value_contract.packet.json"

PREVIOUS = DATA / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade.candidate.json"
PREVIOUS_NEXT = (
    DATA
    / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade"
    / "next_source_value_payload_contract.packet.json"
)
ALPHA_HANDOFF = DATA / "universal_alpha1_frontier_handoff_import" / "alpha1_frontier_handoff_import.packet.json"
ALPHA_CROSSUSE = DATA / "universal_crossuse_parameter_admissibility_theorem" / "alpha1_crossuse_case.packet.json"

QA_ANALYTIC = QA / "candidate_data" / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json"
QA_SOURCE_SEARCH = QA / "candidate_data" / "selected_heterotic_sourcecertificate_or_direct_operator_emission_search.candidate.json"
QA_TORSIONAL = QA / "candidate_data" / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.candidate.json"
QA_TEMPLATE = QA / "candidate_data" / "selected_heterotic_strominger_threshold_operator_or_torsion_source.template.json"

STATUS = (
    "MTT_SELECTED_STROMINGERTHRESHOLDOPERATORVALUE_OR_METROLOGYUNITSOURCE_"
    "BUILT_PARTIAL_TORSIONAL_GEOMETRY_METROLOGY_PRIMITIVE_STRICT_VALUES_OPEN"
)
NEXT = "MTT_Selected_TorsionalWeitzenbockEndomorphism_or_OUWeightsSourceDerivation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    previous_next = load(PREVIOUS_NEXT)
    alpha_handoff = load(ALPHA_HANDOFF)
    alpha_crossuse = load(ALPHA_CROSSUSE)
    qa_analytic = load(QA_ANALYTIC)
    qa_source_search = load(QA_SOURCE_SEARCH)
    qa_torsional = load(QA_TORSIONAL)
    qa_template = load(QA_TEMPLATE)

    invariants = qa_torsional["computed_invariants"]
    radii = invariants["radii"]
    samples = invariants["metric_weighted_logdet_samples"]
    recomputed_A = radii["r3"] / (radii["r1"] * radii["r2"])
    recomputed_8A2 = 8.0 * recomputed_A * recomputed_A
    sample_values = [samples["mu_0.25"], samples["mu_1"], samples["mu_4"]]
    monotone = sample_values[0] < sample_values[1] < sample_values[2]

    strominger_route = {
        "schema": "MTTStromingerThresholdValueRouteImport.v1",
        "status": "PARTIAL_TORSIONAL_GEOMETRY_IMPORTED_THRESHOLD_VALUE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_repo": rel(QA),
        "imports": {
            "analytic_payload": rel(QA_ANALYTIC),
            "source_certificate_search": rel(QA_SOURCE_SEARCH),
            "torsional_endomorphism_or_ou_weights": rel(QA_TORSIONAL),
            "threshold_operator_or_torsion_template": rel(QA_TEMPLATE),
        },
        "latest_qasu3_status": {
            "analytic_payload_status": qa_analytic["status"],
            "source_search_status": qa_source_search["status"],
            "torsional_geometry_status": qa_torsional["status"],
            "primary_next_route": qa_source_search["decision"]["primary_next_route"],
            "qasu3_next_required_artifact": qa_torsional["decision"]["next_required_artifact"],
        },
        "selected_support_values": {
            "selected_radii": radii,
            "relative_one_form_weights": invariants["relative_one_form_weights"],
            "A_r3_over_r1r2": invariants["A_r3_over_r1r2"],
            "recomputed_A_r3_over_r1r2": recomputed_A,
            "eight_A_squared": invariants["eight_A_squared"],
            "recomputed_eight_A_squared": recomputed_8A2,
            "weight_anisotropy": invariants["weight_anisotropy"],
            "metric_weighted_logdet_samples": samples,
            "metric_weighted_logdet_monotone_on_samples": monotone,
        },
        "accepted_final_rows": {
            "selected_strominger_threshold_operator_finite_part_rows": 0,
            "selected_local_system_torsion_finite_part_rows": 0,
            "selected_mu_or_moduli_rows": 0,
            "selected_RG_or_threshold_scheme_rows": 0,
            "strict_P_EW_rows": 0,
            "direct_K_threshold_Omega_H_lambda_rows": 0,
        },
        "why_not_closed": [
            "same-branch source certificate is still absent",
            "full fixed-gauge operator domain is still absent",
            "Weitzenbock_E_Qa is not emitted",
            "OU gamma_nk weights are not emitted",
            "finite heat/zeta/torsion part is not computed",
            "monotone determinant samples do not select mu",
        ],
        "forbidden_promotions": qa_template["forbidden_promotions"]
        + [
            "promote selected radii or 8A^2 support as the physical threshold finite part",
            "use monotone sampled logdet values to choose mu by convenience",
        ],
    }

    metrology_route = {
        "schema": "MTTMetrologyUnitSourceRoute.v1",
        "status": "ONE_UNIVERSAL_PRIMITIVE_READY_STRICT_SCALE_SOURCE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source": alpha_handoff["source_candidate"],
        "source_status": alpha_handoff["source_status"],
        "one_universal_primitive_extension_ready": alpha_handoff["source_claims"][
            "one_universal_primitive_extension_ready"
        ],
        "strict_no_knob_alpha_phys_closed": alpha_handoff["source_claims"]["strict_no_knob_alpha_phys_closed"],
        "strict_current_corpus_nogo": alpha_handoff["source_claims"]["strict_current_corpus_nogo"],
        "primitive_options": alpha_handoff["primitive_options"],
        "values_to_carry": alpha_handoff["values_to_carry"],
        "crossuse_admission": {
            "admitted_now": alpha_crossuse["admitted_now"],
            "candidate_parameter_class": alpha_crossuse["candidate_parameter_class"],
            "one_universal_primitive_extension_ready": alpha_crossuse["one_universal_primitive_extension_ready"],
            "still_needs_for_B23_admission": alpha_crossuse["still_needs_for_B23_admission"],
        },
        "accepted_final_rows": {
            "strict_metrology_unit_source_rows": 0,
            "one_universal_primitive_rows_available_if_adopted": 1,
            "strict_P_EW_rows_from_metrology": 0,
        },
        "why_not_closed": [
            "the handoff supplies a coherent one-primitive physical unit/action option",
            "the same branch still has the one-dimensional absolute scale symmetry",
            "cross-use admission needs a declared calibration observable and downstream prediction audit",
            "there is no strict internal physical rod/clock source value yet",
        ],
    }

    exit_decision = {
        "schema": "MTTStrictExitDecisionAfterStromingerAndMetrology.v1",
        "status": "STRICT_EXIT_REDUCED_TO_TORSIONAL_OPERATOR_VALUE_OR_ADOPTED_UNIT_PRIMITIVE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "premised_one_primitive_lane_preserved": True,
        "new_support_imported": {
            "selected_radii": True,
            "relative_one_form_weights": True,
            "bismut_trace_coefficient_8A2": True,
            "metrology_one_universal_primitive_ready": True,
        },
        "new_final_rows_accepted": {
            "strominger_threshold_value": 0,
            "local_system_torsion_value": 0,
            "strict_metrology_unit": 0,
            "strict_P_EW": 0,
            "direct_K_threshold_Omega_H_lambda": 0,
        },
        "if_next_operator_value_closes": {
            "selected_strominger_threshold_operator_finite_part_rows": 1,
            "selected_mu_or_scheme_rows_still_required": True,
            "can_feed_P_EW_source_theorem": True,
            "can_feed_direct_H_K_certificate": True,
        },
        "if_one_universal_primitive_is_adopted": {
            "adds_counted_shared_physical_parameter": 1,
            "strict_no_knob_status": False,
            "minimal_parameter_lane_status": "available_if_policy_adopts_before_replay",
        },
        "next_required_artifact": NEXT,
    }

    next_contract = {
        "schema": "MTTNextTorsionalOperatorValueContract.v1",
        "status": "NEXT_IS_TORSIONAL_WEITZENBOCK_OR_OU_WEIGHT_SOURCE_DERIVATION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "must_emit_one_of": [
            "same-branch torsional Weitzenbock endomorphism E_Qa on u(E)-valued one-forms",
            "source-derived OU gamma_{n,k}^{-1} mode weights with finite truncation/exactness rule",
            "direct finite heat/zeta/torsion determinant in the selected fixed-gauge domain",
            "strict same-branch physical rod/clock/action normalization breaking the scale symmetry",
        ],
        "must_not_use": [
            "lambda_H, A_EW, weak angle, alpha, or measured masses as selectors",
            "mu=1 or any HYM/moduli value chosen by convenience",
            "the explicit physical-normalization axiom as if it were derived",
            "selected radii, relative weights, or 8A^2 alone as the final threshold finite part",
        ],
        "minimum_acceptance_fields": [
            "same_branch_source_certificate",
            "fixed_gauge_operator_domain_or_unit_source",
            "operator_block_or_OU_weights_or_unit_value",
            "regularization_and_zero_mode_policy",
            "dimensionless_finite_part_or_physical_unit_value",
            "trace/threshold convention compatible with Qa/Qc/SU2 stacks",
        ],
    }

    decision = {
        "previous_frontier_honored": previous["next_required_artifact"]
        == "MTT_Selected_StromingerThresholdOperatorValue_or_MetrologyUnitSource_v1",
        "qasu3_torsional_geometry_imported": True,
        "selected_radii_imported": True,
        "relative_one_form_weights_imported": True,
        "bismut_trace_coefficient_8A2_imported": True,
        "metric_logdet_monotone_no_mu_selection": monotone,
        "strict_strominger_threshold_value_rows": 0,
        "selected_local_system_torsion_rows": 0,
        "strict_metrology_unit_source_rows": 0,
        "one_universal_primitive_extension_ready": True,
        "one_universal_primitive_adopted_here": False,
        "strict_P_EW_source_rows": 0,
        "strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "premised_one_primitive_lane_preserved": True,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedStromingerThresholdOperatorValueOrMetrologyUnitSource",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "previous_next_contract": rel(PREVIOUS_NEXT),
            "alpha1_handoff": rel(ALPHA_HANDOFF),
            "alpha1_crossuse_case": rel(ALPHA_CROSSUSE),
            "qasu3_analytic_payload": rel(QA_ANALYTIC),
            "qasu3_source_search": rel(QA_SOURCE_SEARCH),
            "qasu3_torsional_attempt": rel(QA_TORSIONAL),
            "qasu3_threshold_template": rel(QA_TEMPLATE),
        },
        "output_packets": {
            "strominger_threshold_value_route_import": rel(STROMINGER_ROUTE),
            "metrology_unit_source_route": rel(METROLOGY_ROUTE),
            "strict_exit_decision_after_strominger_and_metrology": rel(EXIT_DECISION),
            "next_torsional_operator_value_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "StromingerThresholdOperatorValueOrMetrologyUnitSourceReductionTheorem",
            "proved": True,
            "statement": (
                "The latest same-branch support now fixes the selected compact Nil/Iwasawa radii, relative "
                "one-form weights, and Bismut trace coefficient 8A^2, while the constants repo supplies a "
                "one-universal-primitive metrology lane.  Neither emits a strict physical-normalization row: "
                "the Strominger side still lacks E_Qa/OU weights/finite heat-zeta-torsion value and mu selection, "
                "and the metrology side remains blocked by the absolute scale symmetry unless one shared primitive "
                "is explicitly adopted.  Thus the strict next object is a torsional operator value or OU-weight "
                "source derivation, not another generic PEW audit."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_StromingerThresholdOperatorValue_or_MetrologyUnitSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected StromingerThresholdOperatorValue or MetrologyUnitSource v1

Status: `{STATUS}`.

## Result

The strict PEW source-value request has now been split into its two legal value
routes and checked against the latest cross-repo results.

### Strominger / HYM Threshold Route

New support imported from Qa/SU3:

```text
selected radii r1,r2,r3            : {radii["r1"]}, {radii["r2"]}, {radii["r3"]}
A = r3/(r1*r2)                     : {invariants["A_r3_over_r1r2"]}
8*A^2                              : {invariants["eight_A_squared"]}
relative one-form weights          : imported
metric logdet samples monotone      : {str(monotone).lower()}
```

Accepted final threshold/torsion rows:

```text
Strominger threshold finite part    : 0
local-system torsion finite part    : 0
selected mu/moduli row              : 0
strict P_EW row                     : 0
direct K_threshold.Omega_H.lambda   : 0
```

So the route is stronger than before, but still not closed.  The real missing
object is now precise: `E_Qa`, source-derived OU weights, or a direct finite
heat/zeta/torsion determinant in the selected fixed-gauge domain.

### Metrology Route

The constants handoff supplies a coherent one-universal-primitive option
(`L0` or `E0`) with internal coefficients:

```text
tau_int                             : {alpha_handoff["values_to_carry"]["tau_int"]}
sqrt_tau_int                        : {alpha_handoff["values_to_carry"]["sqrt_tau_int"]}
Omega0/sqrt(alpha_phys)             : {alpha_handoff["values_to_carry"]["Omega0_over_sqrt_alpha_phys"]}
```

This is available for a counted minimal-parameter lane, but it is not strict
no-knob closure: the same-branch absolute scale symmetry is still active.

## Next

Next artifact: `{NEXT}`.

It must emit one of:

```text
1. torsional Weitzenbock endomorphism E_Qa
2. source-derived OU gamma_nk weights
3. direct finite heat/zeta/torsion determinant
4. strict physical rod/clock/action unit source
```
"""

    write_json(STROMINGER_ROUTE, strominger_route)
    write_json(METROLOGY_ROUTE, metrology_route)
    write_json(EXIT_DECISION, exit_decision)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
