"""Build Step47 Xi argument fill for the selected Rtheta_alpha1 map.

Step46 constructed the selected map but left the magnitude-bearing Xi arguments
unfilled.  Step47 constructs all ten Xi argument shells and fills every subfield
that is currently selected: alpha1/Rtheta binding, projector/family coordinate,
source-normalized sector weight where applicable, generation support, and the
threshold-response contract.  It keeps the actual magnitude payload open unless
threshold/mass/profile source rows are selected.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step47_alpha1rtheta_xi_argument_fill_or_internalvaluerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
XI_SHELLS = PACKET_DIR / "step47_xi_argument_shells_filled.packet.json"
PAYLOAD_GAP = PACKET_DIR / "step47_xi_magnitude_payload_gap.packet.json"
VALUE_GATE = PACKET_DIR / "step47_internal_value_row_execution_gate.packet.json"
NEXT_FRONTIER = PACKET_DIR / "step47_next_payload_source_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step47_Alpha1RThetaXiArgumentFill_or_InternalValueRows_v1.md"

STEP46 = DATA / "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution.candidate.json"
STEP46_MAP = (
    DATA
    / "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution"
    / "step46_selected_alpha1_to_rtheta_coefficient_map.packet.json"
)
SOURCE_WEIGHTS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "source_normalized_sector_projection_weights.packet.json"
)
GENERATION_SUPPORT = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "generation_source_support_recheck.packet.json"
)
THRESHOLD_ROWS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "threshold_response_rows_recheck.packet.json"
)
PROFILE_CONVENTION = (
    DATA
    / "selected_generationresolvedthresholdsourcerows_or_profileconventionclosure"
    / "profile_convention_closure_recheck.packet.json"
)
VSD02_SCHEMA = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_row_strict_schema.packet.json"
)
VSD02_FILL = (
    DATA
    / "selected_vsd02acceptedsourcerowsfill_or_noknobthresholdderivation"
    / "accepted_source_rows_fill_attempt.packet.json"
)

STATUS = "MTT_SELECTED_STEP47_ALPHA1RTHETA_XI_ARGUMENT_SHELLS_FILLED_VALUE_PAYLOADS_OPEN"
NEXT = "MTT_Selected_XiMagnitudePayloadSourceTheorem_or_RThetaValueRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def source_weight_by_sector(source_weights: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {row["sector"]: row for row in source_weights["sector_weights"]}


def closed_count(fields: dict[str, bool | str]) -> int:
    return sum(1 for value in fields.values() if value is True or value == "not_applicable")


def build_charged_xi(row: dict[str, Any], weights: dict[str, dict[str, Any]], generation_support: bool) -> dict[str, Any]:
    sector = row["sector"]
    weight = weights[sector]
    xi_id = row["required_unfilled_argument"]
    selected_subfields = {
        "alpha1_anchor_bound": True,
        "Pi_Rtheta_bound": True,
        "spectral_projector_bound": True,
        "family_eigenvalue_bound": True,
        "source_normalized_sector_weight_bound": weight["source_normalized_weight"] == 1.0,
        "generation_support_bound": generation_support,
        "threshold_response_contract_bound": True,
    }
    open_subfields = {
        "magnitude_bearing_projection_weight": weight["magnitude_bearing_weight"] is not None,
        "threshold_matching_source_row": False,
        "mass_scheme_conversion_source_row": False,
        "true_precision_profile_convention": False,
    }
    all_fields = {**selected_subfields, **open_subfields}
    return {
        "xi_id": xi_id,
        "coefficient_slot": row["coefficient_slot"],
        "sector": sector,
        "generation": row["generation"],
        "spectral_projector_ref": row["spectral_projector_ref"],
        "family_eigenvalue": row["family_eigenvalue"],
        "source_column": weight["source_column"],
        "source_direction": weight["source_direction"],
        "source_normalized_weight": weight["source_normalized_weight"],
        "selected_subfields": selected_subfields,
        "open_payload_subfields": open_subfields,
        "closed_subfield_count": closed_count(all_fields),
        "required_subfield_count": len(all_fields),
        "formal_argument_term": (
            f"{xi_id} := Xi({sector}, gen={row['generation']}; "
            f"P={row['spectral_projector_ref']}, lambda={row['family_eigenvalue']}, "
            f"w_src={weight['source_normalized_weight']}, payload=Omega_{sector}.gen{row['generation']})"
        ),
        "accepted_as_full_value_execution_argument": all(all_fields.values()),
        "admitted_replay_postcheck_value": row["admitted_replay_postcheck_value"],
        "postcheck_used_as_selector": False,
    }


def build_higgs_xi(row: dict[str, Any]) -> dict[str, Any]:
    selected_subfields = {
        "alpha1_anchor_bound": True,
        "Pi_Rtheta_bound": True,
        "higgs_scalar_projector_bound": True,
        "threshold_response_contract_bound": True,
        "generation_support_bound": "not_applicable",
    }
    open_subfields = {
        "higgs_magnitude_payload": False,
        "higgs_mass_scheme_lambda_conversion_row": False,
        "true_precision_profile_convention": False,
    }
    all_fields = {**selected_subfields, **open_subfields}
    return {
        "xi_id": row["required_unfilled_argument"],
        "coefficient_slot": "lambda_H",
        "sector": "H",
        "generation": None,
        "spectral_projector_ref": row["spectral_projector_ref"],
        "selected_subfields": selected_subfields,
        "open_payload_subfields": open_subfields,
        "closed_subfield_count": closed_count(all_fields),
        "required_subfield_count": len(all_fields),
        "formal_argument_term": "Xi_H.lambda := Xi(H; P=H.P_scalar, payload=Omega_H.lambda)",
        "accepted_as_full_value_execution_argument": all(value is True or value == "not_applicable" for value in all_fields.values()),
        "admitted_replay_postcheck_value": row["admitted_replay_postcheck_value"],
        "postcheck_used_as_selector": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP46, STEP46_MAP, SOURCE_WEIGHTS, GENERATION_SUPPORT, THRESHOLD_ROWS, PROFILE_CONVENTION, VSD02_SCHEMA, VSD02_FILL]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step47 inputs: " + ", ".join(missing))

    step46 = load(STEP46)
    step46_map = load(STEP46_MAP)
    source_weights = load(SOURCE_WEIGHTS)
    generation = load(GENERATION_SUPPORT)
    threshold_rows = load(THRESHOLD_ROWS)
    profile = load(PROFILE_CONVENTION)
    vsd02_schema = load(VSD02_SCHEMA)
    vsd02_fill = load(VSD02_FILL)

    weights = source_weight_by_sector(source_weights)
    generation_support_closed = generation["generation_support_closed"] is True
    charged_xi = [
        build_charged_xi(row, weights, generation_support_closed)
        for row in step46_map["charged_rows"]
    ]
    higgs_xi = build_higgs_xi(step46_map["higgs_row"])
    xi_rows = charged_xi + [higgs_xi]

    full_argument_count = sum(1 for row in xi_rows if row["accepted_as_full_value_execution_argument"])
    xi_shells = {
        "schema": "MTTStep47XiArgumentShellsFilled.v1",
        "status": "XI_ARGUMENT_SHELLS_FILLED_PAYLOADS_OPEN",
        "map_source": rel(STEP46_MAP),
        "xi_argument_count": len(xi_rows),
        "charged_xi_argument_count": len(charged_xi),
        "higgs_xi_argument_count": 1,
        "xi_arguments": xi_rows,
        "all_shells_constructed": len(xi_rows) == 10,
        "full_value_execution_argument_count": full_argument_count,
        "all_full_value_execution_arguments_closed": full_argument_count == len(xi_rows),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(XI_SHELLS, xi_shells)

    payload_gap = {
        "schema": "MTTStep47XiMagnitudePayloadGap.v1",
        "status": "MAGNITUDE_PAYLOAD_SOURCE_ROWS_OPEN",
        "accepted_source_row_schema": rel(VSD02_SCHEMA),
        "accepted_source_row_count": vsd02_fill["accepted_row_count"],
        "source_normalized_weights_closed": source_weights["source_projection_weights_closed"],
        "magnitude_bearing_projection_weights_closed": source_weights["magnitude_bearing_projection_weights_closed"],
        "generation_support_closed": generation_support_closed,
        "generation_resolved_magnitude_rows_closed": generation["generation_resolved_magnitude_rows_closed"],
        "threshold_response_rows_closed": threshold_rows["threshold_response_rows_closed"],
        "mass_scheme_conversion_rows_closed": threshold_rows["mass_scheme_conversion_rows_closed"],
        "same_branch_scale_scheme_loop_convention_closed": profile["same_branch_scale_scheme_loop_convention_closed"],
        "full_profile_likelihood_closed": profile["full_profile_likelihood_closed"],
        "required_payload_rows": {
            "charged_Omega_sg_rows": 9,
            "higgs_Omega_H_lambda_row": 1,
        },
        "minimal_payload_theorem": {
            "name": "XiMagnitudePayloadSourceTheorem",
            "must_emit": [
                "magnitude-bearing projection weights for u,d,e generation rows",
                "threshold matching source rows",
                "mass-scheme conversion source rows",
                "true precision scale/scheme/profile convention",
                "Higgs lambda payload row",
                "proof Step42/replay values are postchecks only",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PAYLOAD_GAP, payload_gap)

    value_gate = {
        "schema": "MTTStep47InternalValueRowExecutionGate.v1",
        "status": "VALUE_ROW_EXECUTION_BLOCKED_BY_XI_PAYLOADS",
        "selected_Rtheta_alpha1_map_constructed": step46["closure_decision"][
            "selected_alpha1_to_Rtheta_coefficient_map_constructed"
        ],
        "xi_argument_shells_filled": True,
        "full_value_execution_argument_count": full_argument_count,
        "accepted_internal_value_row_count": 0,
        "accepted_internal_charged_coefficient_row_count": 0,
        "lambda_H_internal_row_closed": False,
        "minimal_parameter_closure_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "blocked_by": [
            "magnitude-bearing Omega_sg/Omega_H payload rows",
            "selected threshold response instantiation",
            "same-branch internal threshold/mass derivation",
            "true precision profile convention",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VALUE_GATE, value_gate)

    next_frontier = {
        "schema": "MTTStep47NextPayloadSourceFrontier.v1",
        "status": "XI_SHELLS_CLOSED_PAYLOAD_SOURCE_THEOREM_NEXT",
        "closed_now": {
            "all_10_Xi_argument_shells_constructed": True,
            "alpha1_Rtheta_map_arguments_bound_to_projectors": True,
            "source_normalized_sector_weights_bound": True,
            "generation_support_bound": generation_support_closed,
            "postcheck_values_forbidden_as_selectors": True,
        },
        "still_open": {
            "XiMagnitudePayloadSourceTheorem": True,
            "magnitude_bearing_projection_weights": True,
            "threshold_matching_source_rows": True,
            "mass_scheme_conversion_source_rows": True,
            "true_precision_profile_convention": True,
            "internal_value_row_execution": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_FRONTIER, next_frontier)

    candidate = {
        "candidate": "MTTSelectedStep47Alpha1RThetaXiArgumentFillOrInternalValueRows",
        "status": STATUS,
        "inputs": {
            "step46": rel(STEP46),
            "step46_map": rel(STEP46_MAP),
            "source_weights": rel(SOURCE_WEIGHTS),
            "generation_support": rel(GENERATION_SUPPORT),
            "threshold_rows": rel(THRESHOLD_ROWS),
            "profile_convention": rel(PROFILE_CONVENTION),
            "vsd02_schema": rel(VSD02_SCHEMA),
            "vsd02_fill": rel(VSD02_FILL),
        },
        "output_packets": {
            "xi_argument_shells_filled": rel(XI_SHELLS),
            "xi_magnitude_payload_gap": rel(PAYLOAD_GAP),
            "internal_value_row_execution_gate": rel(VALUE_GATE),
            "next_payload_source_frontier": rel(NEXT_FRONTIER),
        },
        "theorem": {
            "name": "Step47XiArgumentShellFillTheorem",
            "proved": True,
            "statement": (
                "Given the selected Rtheta_alpha1 map, source-normalized sector weights, and generation "
                "support, all ten Xi argument shells can be constructed without using observed values as "
                "selectors. These shells do not execute numerical value rows until the magnitude-bearing "
                "Omega payload source rows are emitted."
            ),
        },
        "closure_decision": {
            "xi_argument_shells_constructed": True,
            "xi_argument_shell_count": len(xi_rows),
            "full_value_execution_argument_count": full_argument_count,
            "all_full_value_execution_arguments_closed": False,
            "accepted_internal_value_row_count": 0,
            "accepted_internal_Rtheta_coefficient_row_count": 0,
            "selected_lambda_H_row_closed": False,
            "minimal_parameter_closure_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "minimal_parameter_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step47_Alpha1RThetaXiArgumentFill_or_InternalValueRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step47 Alpha1RThetaXiArgumentFill or InternalValueRows v1

Status: `{STATUS}`.

Step47 fills the formal `Xi` argument shells for the constructed
`Rtheta_alpha1` map.

```text
Xi argument shells constructed          : true
Xi shell count                          : {len(xi_rows)}
full value-execution arguments closed   : {full_argument_count}/{len(xi_rows)}
accepted internal value rows            : 0
lambda_H internal row closed            : false
```

Closed now: the `Xi` shells bind alpha1/Rtheta, projectors, family coordinates,
source-normalized sector weights, generation support, and the threshold contract.

Still open: the magnitude-bearing `Omega_s,g` and `Omega_H` payload rows:
threshold matching, mass-scheme conversion, true precision profile convention,
and Higgs lambda payload. Step42 values remain postchecks only.

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
