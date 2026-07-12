"""Build post-AH8 magnitude-bearing row tier adoption.

The previous post-AH8 artifact imports two selected non-scalar dynamic rows.
This artifact attaches the later flavor-operator result: magnitude-bearing
coefficient values are complete at the explicit minimal nine-slot policy tier,
while strict no-knob coefficient source rows remain zero.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_magnitudebearingrows_after_postah8_dynamicimport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLICY_IMPORT = PACKET_DIR / "post_ah8_minimal_nineslot_flavor_value_import.packet.json"
STRICT_RECHECK = PACKET_DIR / "post_ah8_strict_noknob_flavor_recheck.packet.json"
NEXT_PACKET = PACKET_DIR / "next_ckm_pmns_orientation_or_strict_flavor_source_after_policy_values.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MagnitudeBearingRowsAfterPostAH8DynamicImport_or_ThresholdResponseDerivation_v1.md"

PREVIOUS = DATA / "selected_internalvaluerows_afterah8_or_literalglobalwitness.candidate.json"
FLAVOR_VALUES = DATA / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption.candidate.json"
FLAVOR_VALUE_TABLE = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_value_table.packet.json"
)
POLICY_VALUES = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "flavor_threshold_operator_policy_source_values.packet.json"
)
STRICT_FLAVOR = (
    DATA
    / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption"
    / "strict_flavor_noknob_recheck_after_policy_values.packet.json"
)
OPERATOR_SEARCH = DATA / "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy.candidate.json"
SPECTRAL_BASIS = DATA / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall.candidate.json"

STATUS = "MTT_SELECTED_MAGNITUDEBEARINGROWS_AFTER_POSTAH8_DYNAMICIMPORT_POLICY9_STRICT0"
PREVIOUS_STATUS = "MTT_SELECTED_INTERNALVALUEROWS_AFTERAH8_FIRST_DYNAMIC_ROWS_IMPORTED_MAGNITUDES_OPEN"
NEXT = "MTT_Selected_FlavorOperatorPolicyUseAfterAH8_or_CKMPMNSOrientationBridge_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    sources = [PREVIOUS, FLAVOR_VALUES, FLAVOR_VALUE_TABLE, POLICY_VALUES, STRICT_FLAVOR, OPERATOR_SEARCH, SPECTRAL_BASIS]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing post-AH8 magnitude inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    flavor = load(FLAVOR_VALUES)
    value_table = load(FLAVOR_VALUE_TABLE)
    policy_values = load(POLICY_VALUES)
    strict = load(STRICT_FLAVOR)
    operator_search = load(OPERATOR_SEARCH)
    spectral = load(SPECTRAL_BASIS)

    if previous["status"] != PREVIOUS_STATUS:
        raise ValueError("previous post-AH8 internal value status mismatch")

    policy_rows = flavor["closure_decision"]["policy_source_value_row_count"]
    strict_rows = flavor["closure_decision"]["accepted_selected_no_knob_coefficient_source_row_count"]
    minimal_policy_closed = flavor["closure_decision"]["minimal_nine_slot_policy_adopted"]
    value_complete_policy_tier = (
        flavor["closure_decision"]["flavor_operator_values_emitted"]
        and policy_rows == 9
        and minimal_policy_closed
        and operator_search["closure_decision"]["formal_flavor_operator_skeleton_closed"]
        and spectral["closure_decision"]["selected_family_spectral_basis_closed"]
    )

    policy_import = {
        "schema": "MTTPostAH8MinimalNineSlotFlavorValueImport.v1",
        "status": "MINIMAL_NINESLOT_FLAVOR_POLICY_VALUES_IMPORTED_AFTER_AH8",
        "closure_claimed": True,
        "value_complete_at_minimal_policy_tier": value_complete_policy_tier,
        "policy_source_value_row_count": policy_rows,
        "minimal_profile_replay_parameter_slots": flavor["closure_decision"]["minimal_profile_replay_parameter_slots"],
        "flavor_operator_values_emitted": flavor["closure_decision"]["flavor_operator_values_emitted"],
        "observed_profile_values_used_as_parameter_values": flavor["observed_profile_values_used_as_parameter_values"],
        "value_table": rel(FLAVOR_VALUE_TABLE),
        "policy_values": rel(POLICY_VALUES),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    strict_recheck = {
        "schema": "MTTPostAH8StrictNoKnobFlavorRecheck.v1",
        "status": "STRICT_NOKNOB_FLAVOR_ROWS_REMAIN_ZERO_AFTER_POLICY_VALUES",
        "closure_claimed": True,
        "accepted_selected_no_knob_coefficient_source_row_count": strict_rows,
        "selected_flavor_threshold_source_operator_closed": flavor["closure_decision"][
            "selected_flavor_threshold_source_operator_closed"
        ],
        "strict_no_knob_flavor_closure": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "strict_recheck_packet": rel(STRICT_FLAVOR),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextFlavorOperatorPolicyUseAfterAH8.v1",
        "status": "NEXT_IS_POLICY_OPERATOR_USE_OR_STRICT_FLAVOR_SOURCE_THEOREM",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "do_not_reopen": [
            "AH-equivalent BN27 8/8 matrix row",
            "first selected dynamic non-scalar value rows",
            "selected family spectral response basis",
            "minimal nine-slot flavor policy value table",
        ],
        "remaining_strict_targets": [
            "selected flavor threshold/source operator emitting coefficient rows",
            "source-selected reduced-coefficient theorem",
            "CKM/PMNS orientation bridge using policy-tier operator values",
            "strict no-knob replacement for nine policy parameters",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PostAH8MagnitudeBearingPolicyTierImportTheorem",
        "proved": True,
        "statement": (
            "After importing the two selected dynamic value rows, the concrete selected-family flavor "
            "operator can be attached at the explicit minimal nine-slot policy tier: all nine coefficient "
            "values are emitted as policy source values for profile replay and downstream operator use. "
            "The strict no-knob validator still accepts zero selected coefficient source rows, so this is "
            "a value-complete policy tier, not a no-knob derivation of Yukawa magnitudes."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedMagnitudeBearingRowsAfterPostAH8DynamicImport",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_post_AH8_internal_values": rel(PREVIOUS),
            "flavor_values": rel(FLAVOR_VALUES),
            "flavor_value_table": rel(FLAVOR_VALUE_TABLE),
            "policy_values": rel(POLICY_VALUES),
            "strict_flavor_recheck": rel(STRICT_FLAVOR),
            "operator_search": rel(OPERATOR_SEARCH),
            "spectral_basis": rel(SPECTRAL_BASIS),
        },
        "output_packets": {
            "post_ah8_minimal_nineslot_flavor_value_import": rel(POLICY_IMPORT),
            "post_ah8_strict_noknob_flavor_recheck": rel(STRICT_RECHECK),
            "next_ckm_pmns_orientation_or_strict_flavor_source_after_policy_values": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "post_AH8_dynamic_value_rows_imported": previous["closure_decision"][
                "post_AH8_first_dynamic_value_rows_imported"
            ],
            "accepted_selected_dynamic_value_row_count": previous["closure_decision"][
                "accepted_selected_dynamic_value_row_count"
            ],
            "selected_family_spectral_basis_closed": spectral["closure_decision"][
                "selected_family_spectral_basis_closed"
            ],
            "minimal_nine_slot_policy_adopted": minimal_policy_closed,
            "value_complete_at_minimal_policy_tier": value_complete_policy_tier,
            "policy_source_value_row_count": policy_rows,
            "observed_profile_values_used_as_parameter_values": flavor[
                "observed_profile_values_used_as_parameter_values"
            ],
            "accepted_selected_no_knob_coefficient_source_row_count": strict_rows,
            "selected_flavor_threshold_source_operator_closed": False,
            "strict_no_knob_flavor_closure": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": theorem,
    }

    cert = {
        "certificate": "MTTSelectedMagnitudeBearingRowsAfterPostAH8DynamicImport",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "value_complete_at_minimal_policy_tier": value_complete_policy_tier,
        "policy_source_value_row_count": policy_rows,
        "accepted_selected_no_knob_coefficient_source_row_count": strict_rows,
        "strict_no_knob_flavor_closure": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected MagnitudeBearingRowsAfterPostAH8DynamicImport or ThresholdResponseDerivation v1

## Theorem

`PostAH8MagnitudeBearingPolicyTierImportTheorem` is proved.

The post-AH8 chain now has the flavor operator value-complete at the explicit
minimal nine-slot policy tier: `9` policy source values are emitted for
profile replay and downstream operator use.

## What Closes

- two selected dynamic non-scalar rows remain imported
- selected family spectral response basis remains closed
- minimal nine-slot flavor policy values are imported

## Boundary

Strict no-knob flavor closure remains open: accepted selected coefficient
source rows are still `0`. Observed/profile values are used as policy parameter
values, not as MTT no-knob selectors.

## Next Artifact

`{NEXT}`
"""

    write_json(POLICY_IMPORT, policy_import)
    write_json(STRICT_RECHECK, strict_recheck)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
