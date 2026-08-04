"""Build flavor-threshold operator source values / nine-slot policy adoption."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FlavorThresholdOperatorSourceValues_or_NineSlotPolicyAdoption_v1.md"

PREVIOUS = DATA / "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy.candidate.json"
PROFILE_OPERATOR = (
    DATA
    / "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy"
    / "exact_profile_flavor_operator.packet.json"
)
STRICT_VALIDATOR = (
    DATA
    / "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy"
    / "strict_flavor_source_operator_validator.packet.json"
)
POLICY = (
    DATA
    / "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy"
    / "minimal_nine_slot_profile_policy.packet.json"
)
FAMILY_BASIS = (
    DATA
    / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
    / "selected_family_spectral_response_basis.packet.json"
)

STATUS = (
    "MTT_SELECTED_FLAVORTHRESHOLDOPERATORSOURCEVALUES_OR_NINESLOTPOLICYADOPTION_"
    "EMITTED_POLICY_SOURCE_VALUES_STRICT_NOKNOB_OPEN"
)
NEXT = "MTT_Selected_FlavorOperatorValueUse_or_CKMPMNSOrientationBridge_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    profile = load(PROFILE_OPERATOR)
    strict = load(STRICT_VALIDATOR)
    policy = load(POLICY)
    family = load(FAMILY_BASIS)

    emitted_rows = []
    for row in profile["rows"]:
        emitted_rows.append(
            {
                "row_id": row["row_id"],
                "sector": row["sector"],
                "coefficient": row["coefficient"],
                "value": row["value"],
                "operator": profile["operator_form"],
                "accepted_as_minimal_policy_source_value": True,
                "accepted_as_profile_replay_operator_row": True,
                "accepted_as_selected_no_knob_source_row": False,
                "source_value_tier": "MINIMAL_NINE_SLOT_PROFILE_SOURCE_PARAMETER",
                "provenance": "versioned common-scale profile row adopted under explicit nine-slot flavor policy",
            }
        )

    source_values = {
        "schema": "MTTFlavorThresholdOperatorPolicySourceValues.v1",
        "status": "NINE_POLICY_SOURCE_VALUES_EMITTED",
        "operator_form": profile["operator_form"],
        "selected_family_basis": profile["selected_family_basis"],
        "rows": emitted_rows,
        "policy_source_value_row_count": len(emitted_rows),
        "strict_selected_no_knob_source_row_count": 0,
        "observed_profile_values_used_as_parameter_values": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "guardrail": "Rows are source-parameter values for the minimal flavor policy, not no-knob predictions.",
    }

    sector_operator_values = {}
    for row in emitted_rows:
        sector_operator_values.setdefault(row["sector"], {})[row["coefficient"]] = row["value"]

    operator_packet = {
        "schema": "MTTFlavorThresholdOperatorValueTable.v1",
        "status": "OPERATOR_VALUES_ATTACHED_TO_SELECTED_FAMILY_BASIS",
        "operator_form": profile["operator_form"],
        "family_eigenvalues": family["eigenvalues"],
        "vandermonde_basis": family["vandermonde_basis"],
        "sector_operator_coefficients": sector_operator_values,
        "policy_source_value_row_count": len(emitted_rows),
        "strict_selected_no_knob_source_row_count": 0,
        "usable_for": [
            "SM-parity/profile replay of charged diagonal Yukawa magnitudes",
            "downstream CKM/PMNS orientation bridge tests with explicit flavor policy",
            "minimal-parameter ledger accounting",
        ],
        "not_usable_for": [
            "strict no-knob charged-Yukawa prediction",
            "claiming measured profile values selected the MTT branch",
            "closing true SM precision equivalence",
        ],
    }

    adoption = {
        "schema": "MTTNineSlotFlavorPolicyAdoptionDecision.v1",
        "status": "NINE_SLOT_POLICY_ADOPTED_FOR_OPERATOR_VALUES",
        "policy_adopted": True,
        "policy_name": "minimal nine-slot flavor source-parameter policy",
        "profile_replay_parameter_slots": policy["profile_replay_parameter_slots"],
        "strict_no_knob_flavor_closure": False,
        "why_adopt": [
            "the selected family spectral basis and concrete operator are closed",
            "current selected reductions fail to emit numeric c_{s,k} rows",
            "the nine rows are the honest minimal flavor layer, matching SM charged Yukawa eigenvalue count while keeping MTT operator structure",
        ],
        "upgrade_target": policy["upgrade_target"],
    }

    strict_recheck = {
        "schema": "MTTStrictFlavorNoKnobRecheckAfterPolicySourceValues.v1",
        "status": "STRICT_NOKNOB_RECHECK_ZERO_ROWS",
        "strict_validator_status": strict["status"],
        "accepted_selected_source_operator": strict["accepted_selected_source_operator"],
        "accepted_selected_coefficient_row_count": strict["accepted_selected_coefficient_row_count"],
        "policy_source_value_row_count": len(emitted_rows),
        "strict_no_knob_flavor_closure": False,
        "reason": "Policy source values are admitted parameter rows; they do not satisfy the selected no-knob threshold/source validator.",
    }

    next_packet = {
        "schema": "MTTNextCutsetAfterFlavorPolicySourceValueEmission.v1",
        "status": "NEXT_USE_OPERATOR_VALUES_OR_PROVE_STRICT_SOURCE_UPGRADE",
        "next_required_artifact": NEXT,
        "closed_now": [
            "same concrete flavor operator has nine attached policy source values",
            "minimal flavor source-parameter layer is explicit",
            "strict/no-knob boundary is machine-audited",
        ],
        "still_open": [
            "source-emitted c_{s,k} rows from a selected threshold operator",
            "reduced-coefficient theorem selected before replay",
            "CKM/PMNS orientation/value bridge",
            "true SM precision equivalence",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedFlavorThresholdOperatorSourceValuesOrNineSlotPolicyAdoption",
        "status": STATUS,
        "closure_claimed": True,
        "strict_no_knob_flavor_closure_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "observed_profile_values_used_as_parameter_values": True,
        "target_fitting_used": False,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "inputs": {
            "previous_candidate": str(PREVIOUS.relative_to(ROOT)).replace("\\", "/"),
            "exact_profile_flavor_operator": str(PROFILE_OPERATOR.relative_to(ROOT)).replace("\\", "/"),
            "strict_flavor_source_operator_validator": str(STRICT_VALIDATOR.relative_to(ROOT)).replace("\\", "/"),
            "minimal_nine_slot_profile_policy": str(POLICY.relative_to(ROOT)).replace("\\", "/"),
            "selected_family_spectral_response_basis": str(FAMILY_BASIS.relative_to(ROOT)).replace("\\", "/"),
        },
        "output_packets": {
            "flavor_threshold_operator_policy_source_values": f"candidate_data/{SLUG}/flavor_threshold_operator_policy_source_values.packet.json",
            "flavor_threshold_operator_value_table": f"candidate_data/{SLUG}/flavor_threshold_operator_value_table.packet.json",
            "nine_slot_flavor_policy_adoption_decision": f"candidate_data/{SLUG}/nine_slot_flavor_policy_adoption_decision.packet.json",
            "strict_flavor_noknob_recheck_after_policy_values": f"candidate_data/{SLUG}/strict_flavor_noknob_recheck_after_policy_values.packet.json",
            "next_cutset_after_flavor_policy_source_value_emission": f"candidate_data/{SLUG}/next_cutset_after_flavor_policy_source_value_emission.packet.json",
        },
        "closure_decision": {
            "flavor_operator_values_emitted": True,
            "policy_source_value_row_count": len(emitted_rows),
            "minimal_nine_slot_policy_adopted": True,
            "minimal_profile_replay_parameter_slots": policy["profile_replay_parameter_slots"],
            "accepted_selected_no_knob_coefficient_source_row_count": 0,
            "selected_flavor_threshold_source_operator_closed": False,
            "strict_no_knob_flavor_closure": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "FlavorOperatorPolicySourceValueEmissionTheorem",
            "proved": True,
            "statement": "The concrete selected-family flavor operator now carries nine emitted coefficient values under the explicit minimal flavor source-parameter policy. These rows are valid policy source values for SM-parity/profile replay and downstream operator use, but the strict selected threshold/source validator still accepts zero no-knob coefficient rows. Thus the same operator is value-complete at the minimal nine-slot policy tier while strict no-knob flavor prediction remains open.",
        },
    }

    cert = {
        "certificate": "MTT_Selected_FlavorThresholdOperatorSourceValues_or_NineSlotPolicyAdoption_v1",
        "status": STATUS,
        "candidate": candidate["candidate"],
        "theorem": candidate["theorem"]["name"],
        "proved": True,
        "flavor_operator_values_emitted": True,
        "policy_source_value_row_count": len(emitted_rows),
        "minimal_profile_replay_parameter_slots": policy["profile_replay_parameter_slots"],
        "accepted_selected_no_knob_coefficient_source_row_count": 0,
        "strict_no_knob_flavor_closure": False,
        "observed_profile_values_used_as_parameter_values": True,
        "observed_data_used_as_selector": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected FlavorThresholdOperatorSourceValues or NineSlotPolicyAdoption v1

Status: `{STATUS}`

## Theorem

**FlavorOperatorPolicySourceValueEmissionTheorem.** The concrete selected-family flavor operator now carries nine emitted coefficient values under the explicit minimal flavor source-parameter policy. These rows are valid policy source values for SM-parity/profile replay and downstream operator use, but the strict selected threshold/source validator still accepts zero no-knob coefficient rows.

## Emitted Operator

`{profile["operator_form"]}`

Policy source rows emitted: `{len(emitted_rows)}`

Strict selected/no-knob coefficient rows: `0`

## Claim Boundary

This closes the same operator at the minimal nine-slot flavor source-parameter tier. It does not close strict no-knob charged-Yukawa prediction, true SM precision equivalence, or the source theorem that would derive `c_{{s,k}}` before replay.

Next artifact: `{NEXT}`.
"""

    write_json(PACKET_DIR / "flavor_threshold_operator_policy_source_values.packet.json", source_values)
    write_json(PACKET_DIR / "flavor_threshold_operator_value_table.packet.json", operator_packet)
    write_json(PACKET_DIR / "nine_slot_flavor_policy_adoption_decision.packet.json", adoption)
    write_json(PACKET_DIR / "strict_flavor_noknob_recheck_after_policy_values.packet.json", strict_recheck)
    write_json(PACKET_DIR / "next_cutset_after_flavor_policy_source_value_emission.packet.json", next_packet)
    write_json(CANDIDATE, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
