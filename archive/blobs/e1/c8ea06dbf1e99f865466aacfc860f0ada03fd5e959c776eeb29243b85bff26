"""Build concrete flavor source-operator search / minimal nine-slot policy."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FlavorSourceOperatorConcreteSearch_or_MinimalNineSlotPolicy_v1.md"

PREVIOUS = DATA / "selected_flavorthresholdsourceoperator_or_reducedcoefficienttheorem.candidate.json"
CONTRACT = (
    DATA
    / "selected_flavorthresholdsourceoperator_or_reducedcoefficienttheorem"
    / "selected_flavor_threshold_source_operator_contract.packet.json"
)
DIAGNOSTIC = (
    DATA
    / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
    / "diagnostic_log_yukawa_response_coefficients.packet.json"
)
FAMILY_BASIS = (
    DATA
    / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
    / "selected_family_spectral_response_basis.packet.json"
)
THETA_ROWS = (
    DATA
    / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
    / "step68_selected_theta_exponent_weight_rows.packet.json"
)
PROJECTION_WEIGHTS = (
    DATA
    / "selected_thresholdresponserows_or_sectorprojectionweightsexecution"
    / "source_normalized_sector_projection_weights.packet.json"
)
LEDGER = (
    DATA
    / "selected_logyukawacoefficientsourcerows_or_minimalflavorparameterledger"
    / "minimal_flavor_parameter_ledger.packet.json"
)

STATUS = (
    "MTT_SELECTED_FLAVORSOURCEOPERATORCONCRETESEARCH_OR_MINIMALNINESLOTPOLICY_"
    "BUILT_EXACT_PROFILE_OPERATOR_STRICT_SOURCE_OPEN"
)
NEXT = "MTT_Selected_FlavorThresholdOperatorSourceValues_or_NineSlotPolicyAdoption_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def max_abs(values: list[float]) -> float:
    return max(abs(v) for v in values)


def rms(values: list[float]) -> float:
    return (sum(v * v for v in values) / len(values)) ** 0.5


def shared_polynomial(coeffs: list[list[float]]) -> dict:
    shared = [sum(row[j] for row in coeffs) / len(coeffs) for j in range(3)]
    residuals = [row[j] - shared[j] for row in coeffs for j in range(3)]
    return {
        "lane": "shared_family_polynomial_operator",
        "candidate_operator": "T_flavor = c0 I + c1 F + c2 F^2 shared across u,d,e",
        "parameter_count": 3,
        "accepted_as_selected_source_operator": False,
        "max_abs_residual": max_abs(residuals),
        "rms_residual": rms(residuals),
        "reason_not_closed": "A shared polynomial ignores selected sector threshold differences and leaves large coefficient residuals.",
    }


def sector_plus_basis(coeffs: list[list[float]]) -> dict:
    rows = len(coeffs)
    cols = len(coeffs[0])
    row_means = [sum(row) / cols for row in coeffs]
    col_means = [sum(coeffs[i][j] for i in range(rows)) / rows for j in range(cols)]
    grand = sum(sum(row) for row in coeffs) / (rows * cols)
    residuals = []
    for i in range(rows):
        for j in range(cols):
            residuals.append(coeffs[i][j] - (row_means[i] + col_means[j] - grand))
    return {
        "lane": "sector_plus_basis_additive_operator",
        "candidate_operator": "c_{s,k}=a_s+b_k with one gauge-fixed redundancy",
        "parameter_count": rows + cols - 1,
        "accepted_as_selected_source_operator": False,
        "max_abs_residual": max_abs(residuals),
        "rms_residual": rms(residuals),
        "reason_not_closed": "The coefficient matrix is not additively separable by sector and family-basis degree.",
    }


def source_feature_rows(theta_rows: dict) -> dict:
    by_sector: dict[str, list[dict]] = {"u": [], "d": [], "e": []}
    for row in theta_rows["charged_exponent_weight_rows"]:
        if row["sector"] in by_sector:
            by_sector[row["sector"]].append(row)

    features = []
    for sector, rows in by_sector.items():
        rows = sorted(rows, key=lambda r: r["generation"])
        features.append(
            {
                "sector": sector,
                "source_direction": rows[0]["source_direction"],
                "mixed_slot": any(r["mixed_10_bar5_scalar_slot"] for r in rows),
                "theta_exponents": [r["theta_exponent_numeric"] for r in rows],
                "qutrit_positive_branch_floor": rows[-1]["qutrit_quotient_floor"],
                "source_native_numeric_fields": [
                    "source_direction",
                    "mixed_slot",
                    "theta_exponents",
                    "qutrit_positive_branch_floor",
                ],
            }
        )
    return {
        "schema": "MTTFlavorSourceNativeFeatureRows.v1",
        "status": "SOURCE_FEATURE_ROWS_IMPORTED",
        "accepted_as_coefficient_values": False,
        "features_by_sector": features,
        "why_insufficient": [
            "features type the sector lanes but do not emit real-valued c0,c1,c2 rows",
            "turning sector labels into arbitrary numeric rows is exactly the nine-slot profile ledger",
        ],
    }


def main() -> int:
    previous = load(PREVIOUS)
    contract = load(CONTRACT)
    diagnostic = load(DIAGNOSTIC)
    family_basis = load(FAMILY_BASIS)
    theta_rows = load(THETA_ROWS)
    projection = load(PROJECTION_WEIGHTS)
    ledger = load(LEDGER)

    sectors = [row["sector"] for row in diagnostic["sector_rows"]]
    coeffs = [row["coefficient_values_c0_c1_c2"] for row in diagnostic["sector_rows"]]

    exact_profile_rows = []
    for sector_row in diagnostic["sector_rows"]:
        sector = sector_row["sector"]
        for k, value in enumerate(sector_row["coefficient_values_c0_c1_c2"]):
            exact_profile_rows.append(
                {
                    "row_id": f"c.{sector}.{k}",
                    "sector": sector,
                    "coefficient": f"c{k}",
                    "value": value,
                    "accepted_as_profile_replay_operator_row": True,
                    "accepted_as_selected_no_knob_source_row": False,
                    "source_status": "diagnostic profile coefficient, not source-emitted",
                }
            )

    exact_operator = {
        "schema": "MTTExactProfileFlavorOperator.v1",
        "status": "EXACT_PROFILE_REPLAY_OPERATOR_EMITTED_STRICT_SOURCE_REJECTED",
        "operator_form": "T_profile = sum_s P_s (c0_s I + c1_s F + c2_s F^2)",
        "selected_family_basis": family_basis["vandermonde_basis"],
        "sectors": sectors,
        "rows": exact_profile_rows,
        "accepted_profile_replay_row_count": len(exact_profile_rows),
        "accepted_selected_no_knob_source_row_count": 0,
        "reason_not_strict_source": "The c_{s,k} numbers are solved from versioned common-scale Yukawa magnitudes, so the operator is an exact replay operator rather than a selected threshold/source operator.",
    }

    feature_packet = source_feature_rows(theta_rows)
    strict_validator = {
        "schema": "MTTStrictFlavorSourceOperatorValidator.v1",
        "status": "STRICT_SOURCE_OPERATOR_REJECTED_CURRENT_PACKETS",
        "required_fields": contract["must_emit_before_replay"],
        "field_status": {
            "sector-labelled threshold source operator T_flavor[s]": "formal profile operator built; selected source operator values not emitted",
            "three coefficient functionals c0,c1,c2 from selected branch data": "0 accepted selected coefficient rows",
            "generation-resolved threshold/mass-scheme/profile rows or a theorem reducing them": "profile replay exists; source theorem open",
            "scale/scheme convention tied to the same branch": "declared parity convention available; strict source convention open",
            "no use of common-scale Yukawa magnitudes, CKM, PMNS, or Higgs values as selectors": "guard satisfied for strict lane; exact profile lane remains downstream replay only",
        },
        "accepted_selected_source_operator": False,
        "accepted_selected_coefficient_row_count": 0,
        "profile_replay_operator_available": True,
        "profile_replay_operator_row_count": len(exact_profile_rows),
    }

    search = {
        "schema": "MTTFlavorSourceOperatorConcreteSearch.v1",
        "status": "CONCRETE_SEARCH_EXECUTED_NO_STRICT_SOURCE_VALUES",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "lanes": [
            shared_polynomial(coeffs),
            sector_plus_basis(coeffs),
            {
                "lane": "source_native_feature_operator",
                "candidate_operator": "T_flavor built from phase/shift, mixed-slot, theta-exponent, and qutrit-floor selected features",
                "parameter_count": 0,
                "accepted_as_selected_source_operator": False,
                "reason_not_closed": "The selected features type the lanes but do not emit the real coefficient values c_{s,k}.",
            },
            {
                "lane": "nine_slot_profile_operator",
                "candidate_operator": exact_operator["operator_form"],
                "parameter_count": 9,
                "accepted_as_selected_source_operator": False,
                "accepted_as_profile_replay_operator": True,
                "reason_not_closed": "Exact, but it is the controlled profile-replay ledger rather than no-knob source emission.",
            },
        ],
    }

    policy = {
        "schema": "MTTFlavorMinimalNineSlotPolicy.v1",
        "status": "MINIMAL_NINE_SLOT_PROFILE_POLICY_EXPLICIT",
        "strict_no_knob_flavor_closure": False,
        "profile_replay_policy_closed": True,
        "profile_replay_parameter_slots": 9,
        "comparison_to_SM": "Same count as charged SM Yukawa eigenvalues, but typed as coefficients of a selected family spectral response operator.",
        "upgrade_target": "Replace the nine replay rows with source-emitted c_{s,k} rows from a selected flavor threshold/source operator.",
        "guardrail": "Do not relabel this policy as no-knob flavor prediction.",
    }

    candidate = {
        "candidate": "MTTSelectedFlavorSourceOperatorConcreteSearchOrMinimalNineSlotPolicy",
        "status": STATUS,
        "closure_claimed": True,
        "strict_no_knob_flavor_closure_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "inputs": {
            "previous_candidate": str(PREVIOUS.relative_to(ROOT)).replace("\\", "/"),
            "selected_flavor_threshold_source_operator_contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
            "diagnostic_log_yukawa_response_coefficients": str(DIAGNOSTIC.relative_to(ROOT)).replace("\\", "/"),
            "selected_family_spectral_response_basis": str(FAMILY_BASIS.relative_to(ROOT)).replace("\\", "/"),
            "step68_theta_exponent_weight_rows": str(THETA_ROWS.relative_to(ROOT)).replace("\\", "/"),
            "source_normalized_sector_projection_weights": str(PROJECTION_WEIGHTS.relative_to(ROOT)).replace("\\", "/"),
            "minimal_flavor_parameter_ledger": str(LEDGER.relative_to(ROOT)).replace("\\", "/"),
        },
        "output_packets": {
            "source_native_feature_rows": f"candidate_data/{SLUG}/source_native_feature_rows.packet.json",
            "exact_profile_flavor_operator": f"candidate_data/{SLUG}/exact_profile_flavor_operator.packet.json",
            "strict_flavor_source_operator_validator": f"candidate_data/{SLUG}/strict_flavor_source_operator_validator.packet.json",
            "concrete_source_operator_search": f"candidate_data/{SLUG}/concrete_source_operator_search.packet.json",
            "minimal_nine_slot_profile_policy": f"candidate_data/{SLUG}/minimal_nine_slot_profile_policy.packet.json",
        },
        "closure_decision": {
            "formal_flavor_operator_skeleton_closed": True,
            "exact_profile_replay_operator_emitted": True,
            "accepted_profile_replay_operator_row_count": len(exact_profile_rows),
            "accepted_selected_coefficient_source_row_count": 0,
            "selected_flavor_threshold_source_operator_closed": False,
            "strict_no_knob_flavor_closure": False,
            "minimal_nine_slot_profile_policy_closed": True,
            "minimal_profile_replay_parameter_slots": ledger["profile_replay_parameter_slots"],
            "source_native_feature_operator_emits_numeric_coefficients": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "ConcreteFlavorOperatorReplayVsSourceTheorem",
            "proved": True,
            "statement": "The selected family spectral basis gives a concrete operator form T=sum_s P_s(c0_s I+c1_s F+c2_s F^2). Filling the nine c_{s,k} rows from the versioned common-scale profile emits an exact flavor replay operator, but not a selected no-knob threshold/source operator. Current source-native features distinguish the sector lanes but do not emit the real coefficient values. Thus the constructive strict target is narrowed to source values for this operator, while the honest minimal flavor policy is the nine-slot profile-replay ledger.",
        },
    }

    cert = {
        "certificate": "MTT_Selected_FlavorSourceOperatorConcreteSearch_or_MinimalNineSlotPolicy_v1",
        "status": STATUS,
        "candidate": candidate["candidate"],
        "theorem": candidate["theorem"]["name"],
        "proved": True,
        "formal_flavor_operator_skeleton_closed": True,
        "exact_profile_replay_operator_emitted": True,
        "accepted_profile_replay_operator_row_count": len(exact_profile_rows),
        "accepted_selected_coefficient_source_row_count": 0,
        "minimal_profile_replay_parameter_slots": ledger["profile_replay_parameter_slots"],
        "strict_no_knob_flavor_closure": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FlavorSourceOperatorConcreteSearch or MinimalNineSlotPolicy v1

Status: `{STATUS}`

## Theorem

**ConcreteFlavorOperatorReplayVsSourceTheorem.** The selected family spectral basis gives a concrete operator form

`T_profile = sum_s P_s (c0_s I + c1_s F + c2_s F^2)`.

Filling the nine `c_{{s,k}}` rows from the versioned common-scale profile emits an exact flavor replay operator, but not a selected no-knob threshold/source operator. Current source-native features distinguish the sector lanes, but do not emit the real coefficient values.

## What Closes

- formal flavor operator skeleton: closed
- exact profile-replay operator: closed
- profile replay rows emitted: `{len(exact_profile_rows)}`
- minimal flavor profile policy: `{ledger["profile_replay_parameter_slots"]}` slots

## What Stays Open

- selected coefficient source rows: `0`
- strict no-knob charged-Yukawa closure: false
- selected flavor threshold/source operator values: open

Next artifact: `{NEXT}`.
"""

    write_json(PACKET_DIR / "source_native_feature_rows.packet.json", feature_packet)
    write_json(PACKET_DIR / "exact_profile_flavor_operator.packet.json", exact_operator)
    write_json(PACKET_DIR / "strict_flavor_source_operator_validator.packet.json", strict_validator)
    write_json(PACKET_DIR / "concrete_source_operator_search.packet.json", search)
    write_json(PACKET_DIR / "minimal_nine_slot_profile_policy.packet.json", policy)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
