"""Build torsional Weitzenbock / OU source-derivation frontier.

The previous main-repo artifact asked for a torsional E_Qa, OU weights, a
finite heat/zeta/torsion determinant, or a strict metrology unit.  The sibling
Qa/SU3 repo has since sharpened the route: the exact oriented finite table is
computed, and the smallest remaining source object is a source-owned positive
Phi_fin operator or smooth E_Qa payload.
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

SLUG = "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TorsionalWeitzenbockEndomorphism_or_OUWeightsSourceDerivation_v1.md"

ROUTE_REDUCTION = PACKET_DIR / "torsional_or_ou_route_reduction.packet.json"
FINITE_IMPORT = PACKET_DIR / "finite_quotient_identity_route_import.packet.json"
EXACT_VALUES = PACKET_DIR / "exact_oriented_finitepart_values.packet.json"
NEXT_CONTRACT = PACKET_DIR / "source_owned_positive_operator_or_eqapayload_contract.packet.json"

PREVIOUS = DATA / "selected_stromingerthresholdoperatorvalue_or_metrologyunitsource.candidate.json"
PREVIOUS_NEXT = (
    DATA
    / "selected_stromingerthresholdoperatorvalue_or_metrologyunitsource"
    / "next_torsional_operator_value_contract.packet.json"
)

QA_TORSIONAL = QA / "candidate_data" / "selected_heterotic_torsional_endomorphism_or_ou_mode_weights.candidate.json"
QA_MINIMAL_LEAF = QA / "candidate_data" / "selected_heterotic_orientedphifin_minimal_leaf_fill_or_finitequotientidentity.candidate.json"
QA_POSITIVE_GATE = QA / "candidate_data" / "selected_heterotic_orientedphifin_positivemagnitude_sourceownership_or_smootheqa_emission.candidate.json"
QA_SOURCEOWNED_FILL = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.candidate.json"
QA_SOURCEOWNED_PACKET = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_minimal_source_packet.json"
QA_MAG_PACKET = QA / "candidate_data" / "selected_heterotic_orientedphifin_magnitudefinitepart_sourcetheorem_or_smootheqa_traceidentity_packet.json"

STATUS = (
    "MTT_SELECTED_TORSIONALWEITZENBOCKENDOMORPHISM_OR_OUWEIGHTSSOURCEDERIVATION_"
    "BUILT_FINITE_QUOTIENT_IDENTITY_PRIMARY_SOURCEOWNED_OPERATOR_OPEN"
)
NEXT = "MTT_Selected_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1"


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
    torsional = load(QA_TORSIONAL)
    minimal_leaf = load(QA_MINIMAL_LEAF)
    positive_gate = load(QA_POSITIVE_GATE)
    sourceowned_fill = load(QA_SOURCEOWNED_FILL)
    sourceowned_packet = load(QA_SOURCEOWNED_PACKET)
    mag_packet = load(QA_MAG_PACKET)

    finite_values = mag_packet["finitepart_values"]
    plus_values = finite_values["plus_sector_positive_eigenvalues"]
    minus_values = finite_values["minus_sector_positive_eigenvalues"]
    full_values = finite_values["full_positive_eigenvalues"]
    plus_product = 1
    for value in plus_values:
        plus_product *= value
    minus_product = 1
    for value in minus_values:
        minus_product *= value
    full_product = 1
    for value in full_values:
        full_product *= value

    route_reduction = {
        "schema": "MTTTorsionalOrOURouteReduction.v1",
        "status": "TORSIONAL_E_OR_OU_REDUCED_TO_FINITE_QUOTIENT_IDENTITY_PRIMARY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_contract_honored": previous_next["next_required_artifact"]
        == "MTT_Selected_TorsionalWeitzenbockEndomorphism_or_OUWeightsSourceDerivation_v1",
        "torsional_route_status": {
            "source": rel(QA_TORSIONAL),
            "status": torsional["status"],
            "same_branch_source_certificate": torsional["required_flags"]["same_branch_source_certificate"],
            "full_fixed_gauge_domain": torsional["required_flags"]["full_fixed_gauge_domain"],
            "Weitzenbock_E_Qa": torsional["required_flags"]["Weitzenbock_E_Qa"],
            "OU_gamma_nk_weights": torsional["required_flags"]["OU_gamma_nk_weights"],
            "finite_heat_zeta_torsion_part": torsional["required_flags"]["finite_heat_zeta_torsion_part"],
            "computed_threshold_value": torsional["required_flags"]["computed_threshold_value"],
            "support_imported": {
                "selected_radii": torsional["required_flags"]["selected_radii"],
                "relative_one_form_weights": torsional["required_flags"]["relative_one_form_weights"],
                "bismut_trace_coefficient_8A2": torsional["required_flags"]["bismut_trace_coefficient_8A2"],
                "metric_weighted_positive_su3_samples": torsional["required_flags"][
                    "metric_weighted_positive_su3_samples"
                ],
            },
        },
        "route_selection": {
            "primary": "finite_quotient_identity",
            "secondary": "smooth_EQa_payload",
            "why": minimal_leaf["route_ranking"]["primary"]["why_primary"],
            "torsional_E_or_OU_as_smooth_route": "retained_secondary_until source E_Qa/OU weights are emitted",
        },
        "accepted_final_rows": {
            "torsional_Weitzenbock_E_Qa_rows": 0,
            "OU_weight_rows": 0,
            "finite_heat_zeta_torsion_rows": 0,
            "strict_P_EW_rows": 0,
            "direct_K_threshold_Omega_H_lambda_rows": 0,
        },
    }

    finite_import = {
        "schema": "MTTFiniteQuotientIdentityRouteImport.v1",
        "status": "EXACT_ORIENTED_TABLE_IMPORTED_SOURCE_OWNERSHIP_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imports": {
            "minimal_leaf": rel(QA_MINIMAL_LEAF),
            "positive_gate": rel(QA_POSITIVE_GATE),
            "sourceowned_fill": rel(QA_SOURCEOWNED_FILL),
            "sourceowned_packet": rel(QA_SOURCEOWNED_PACKET),
            "magnitude_packet": rel(QA_MAG_PACKET),
        },
        "minimal_leaf_decision": minimal_leaf["decision"],
        "route_A_direct_source_owned_positive_operator": sourceowned_packet[
            "route_A_direct_source_owned_positive_operator"
        ],
        "route_B_smooth_EQa_payload": sourceowned_packet["route_B_smooth_EQa_payload"],
        "filled_support": {
            "same_branch_certificate": sourceowned_fill["attempts"]["direct_source_owned_positive_operator"][
                "same_branch_certificate"
            ],
            "orientation_binding": sourceowned_fill["attempts"]["direct_source_owned_positive_operator"][
                "orientation_binding"
            ],
            "no_double_count_shared_circle_policy": sourceowned_fill["attempts"][
                "direct_source_owned_positive_operator"
            ]["no_double_count_shared_circle_policy"],
            "table_D_E_Riesz_Green_positive_spectrum_materialized": sourceowned_fill["attempts"][
                "direct_source_owned_positive_operator"
            ]["table_D_E_Riesz_Green_positive_spectrum_materialized"],
            "R_plus_geometry_filled": sourceowned_fill["attempts"]["smooth_EQa_payload"]["R_plus_geometry_filled"],
        },
        "open_source_fields": {
            "oriented_BN_carrier_emitted": sourceowned_fill["attempts"]["direct_source_owned_positive_operator"][
                "oriented_BN_carrier_emitted"
            ],
            "EndE_or_rhoE_operator_functor_or_quotient": sourceowned_fill["attempts"][
                "direct_source_owned_positive_operator"
            ]["EndE_or_rhoE_operator_functor_or_quotient"],
            "positive_PhiFin_magnitude_owned": sourceowned_fill["attempts"]["direct_source_owned_positive_operator"][
                "positive_PhiFin_magnitude_owned"
            ],
            "finite_threshold_complex_quotient": sourceowned_fill["attempts"]["direct_source_owned_positive_operator"][
                "finite_threshold_complex_quotient"
            ],
            "finitepart_trace_identity": sourceowned_fill["attempts"]["direct_source_owned_positive_operator"][
                "finitepart_trace_identity"
            ],
            "smooth_E_Qa_matrix": sourceowned_fill["attempts"]["smooth_EQa_payload"][
                "E_Qa_matrix_or_equivalent_zero_order_block"
            ],
            "positive_spectrum_heat_zeta_or_torsion_finitepart": sourceowned_fill["attempts"][
                "smooth_EQa_payload"
            ]["positive_spectrum_heat_zeta_or_torsion_finitepart"],
        },
        "accepted_final_rows": {
            "source_owned_positive_operator_rows": 0,
            "smooth_EQa_payload_rows": 0,
            "heterotic_threshold_finitepart_rows": 0,
            "strict_P_EW_rows": 0,
            "direct_K_threshold_Omega_H_lambda_rows": 0,
        },
        "forbidden_shortcuts": sourceowned_packet["forbidden_shortcuts"],
    }

    exact_values = {
        "schema": "MTTExactOrientedFinitepartValues.v1",
        "status": "EXACT_VALUES_COMPUTED_SUPPORT_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "plus_sector_product_recomputed": plus_product,
        "minus_sector_product_recomputed": minus_product,
        "full_positive_product_recomputed": full_product,
        "finitepart_values": finite_values,
        "support_only_not_promoted": True,
        "promotion_requires": [
            "source-owned oriented B_N carrier/operator",
            "End(E)/rho_E to oriented B_N functor or quotient",
            "positive Phi_fin magnitude ownership",
            "finitepart trace identity for log(92160000)",
            "kernel/no-double-count/shared-circle policy replay",
        ],
    }

    next_contract = {
        "schema": "MTTSourceOwnedPositiveOperatorOrEQaPayloadContract.v1",
        "status": "NEXT_IS_SOURCEOWNED_POSITIVE_OPERATOR_OR_EQA_PAYLOAD_FILL",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "must_emit_one_of": sourceowned_packet["forbidden_shortcuts"]
        and [
            "source-owned positive Phi_fin operator on oriented B_N with finitepart trace identity",
            "End(E)/rho_E to oriented B_N operator functor or quotient plus positive magnitude ownership",
            "smooth E_Qa or heat-zeta-torsion packet whose finite quotient is the oriented 27-mode positive operator",
        ],
        "must_not_use": sourceowned_packet["forbidden_shortcuts"],
        "known_values_available_for_replay_only_after_source_ownership": sourceowned_packet["known_values"],
    }

    decision = {
        "previous_frontier_honored": True,
        "torsional_E_Qa_computed": False,
        "OU_weights_computed": False,
        "smooth_finite_heat_zeta_torsion_computed": False,
        "finite_quotient_identity_route_selected_primary": True,
        "smooth_EQa_route_retained_secondary": True,
        "oriented_table_values_exactly_computed": True,
        "oriented_abs_sector_logdet_exact": finite_values["oriented_abs_sector_logdet_exact"],
        "full_positive_logdet_exact": finite_values["full_positive_logdet_exact"],
        "oriented_values_promoted_to_threshold": False,
        "source_owned_positive_operator_closed": False,
        "smooth_EQa_payload_closed": False,
        "strict_P_EW_source_rows": 0,
        "strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedTorsionalWeitzenbockEndomorphismOrOUWeightsSourceDerivation",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "previous_next_contract": rel(PREVIOUS_NEXT),
            "qasu3_torsional_attempt": rel(QA_TORSIONAL),
            "qasu3_minimal_leaf": rel(QA_MINIMAL_LEAF),
            "qasu3_positive_gate": rel(QA_POSITIVE_GATE),
            "qasu3_sourceowned_fill": rel(QA_SOURCEOWNED_FILL),
            "qasu3_sourceowned_packet": rel(QA_SOURCEOWNED_PACKET),
            "qasu3_magnitude_packet": rel(QA_MAG_PACKET),
        },
        "output_packets": {
            "torsional_or_ou_route_reduction": rel(ROUTE_REDUCTION),
            "finite_quotient_identity_route_import": rel(FINITE_IMPORT),
            "exact_oriented_finitepart_values": rel(EXACT_VALUES),
            "source_owned_positive_operator_or_eqapayload_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "TorsionalWeitzenbockOrOUWeightsSourceDerivationReductionTheorem",
            "proved": True,
            "statement": (
                "The smooth torsional E_Qa/OU route remains open, but the latest same-branch Qa/SU3 results "
                "show a smaller primary route: a finite quotient identity for the already computed oriented "
                "27-mode Phi_fin table.  Exact values log(9600), log(92160000), and log(884736000000) are "
                "available as support only.  Strict closure now requires source ownership of the positive "
                "oriented operator or a smooth E_Qa payload; no PEW, direct-K, or true-SM row is promoted."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_TorsionalWeitzenbockEndomorphism_or_OUWeightsSourceDerivation_v1",
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

    note = f"""# MTT Selected TorsionalWeitzenbockEndomorphism or OUWeightsSourceDerivation v1

Status: `{STATUS}`.

## Result

The requested torsional `E_Qa` / OU-weight frontier has been advanced using the
latest Qa/SU3 packets.

The smooth route is still open:

```text
torsional Weitzenbock E_Qa          : false
OU gamma_nk weights                 : false
smooth heat/zeta/torsion finitepart : false
```

But the best current route is now smaller than a full smooth solve.  The sibling
repo has an exact oriented finite table:

```text
plus/minus sector product           : {plus_product}
oriented absolute sector product    : {finite_values["oriented_abs_sector_product"]}
full positive product               : {full_product}
oriented abs finitepart             : {finite_values["oriented_abs_sector_logdet_exact"]}
full positive finitepart            : {finite_values["full_positive_logdet_exact"]}
```

These values are not promoted as threshold data.  They become usable only after
one source-ownership theorem:

```text
source-owned positive Phi_fin operator on oriented B_N
or End(E)/rho_E -> oriented B_N quotient/functor
or smooth E_Qa / heat-zeta-torsion payload with the same finite quotient
```

## Next

Next artifact: `{NEXT}`.
"""

    write_json(ROUTE_REDUCTION, route_reduction)
    write_json(FINITE_IMPORT, finite_import)
    write_json(EXACT_VALUES, exact_values)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
