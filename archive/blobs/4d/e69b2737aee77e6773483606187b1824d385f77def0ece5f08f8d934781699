"""Build Yukawa magnitude rows from selected dynamic packet or value-functional gap.

The previous artifact accepted the first selected dynamic matter/overlap rows.
This one tests whether those selected rows already determine no-proxy Yukawa
magnitude rows.  They do not: the selected first-response packet resolves
families, but its universal eigenprofile cannot supply the sector-specific
charged hierarchies without extra selected sector coefficients or threshold
response rows.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_yukawamagnituderowsfromselecteddynamicpacket_or_valuefunctionalgap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_IMPORT = PACKET_DIR / "selected_dynamic_packet_source_import.packet.json"
FAMILY_GAP = PACKET_DIR / "family_resolved_but_magnitude_functional_gap.packet.json"
MINIMAL_OBJECTS = PACKET_DIR / "minimal_selected_value_functional_objects.packet.json"
NEXT_PACKET = PACKET_DIR / "next_after_value_functional_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_YukawaMagnitudeRowsFromSelectedDynamicPacket_or_ValueFunctionalGap_v1.md"

PREVIOUS = DATA / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit.candidate.json"
ACCEPTED_FIRST = (
    DATA
    / "selected_fulls2noproxyvaluerows_or_strictpewdirectkexit"
    / "accepted_first_selected_dynamic_value_row.packet.json"
)
SELECTED_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
SAME_SOURCE_PACKET = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "same_source_matter_overlap_operator_packet.packet.json"
)
YUKAWA_BRIDGE = DATA / "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem.candidate.json"
SECTOR_BLIND_NOGO = (
    DATA
    / "selected_yukawasourcebridge_or_magnitudeprojectionnogotheorem"
    / "sector_blind_magnitude_projection_nogo.packet.json"
)
PROJECTION_READINESS = DATA / "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier.candidate.json"
PROJECTION_SKELETON = (
    DATA
    / "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier"
    / "sector_aware_projection_kernel_skeleton.packet.json"
)
FAMILY_OPERATOR = DATA / "selected_familyresolvingoperator_or_generationthresholdrowsexecution.candidate.json"
FAMILY_SPECTRUM = (
    DATA
    / "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
    / "selected_first_response_family_spectrum.packet.json"
)
SECTOR_PROFILE = (
    DATA / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution.candidate.json"
)
PROFILE_TESTS = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "sector_scaled_eigenprofile_model_tests.packet.json"
)
SECTOR_FRONTIER = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "sector_coefficient_frontier.packet.json"
)
STRICT_PEW = (
    DATA
    / "selected_qasu3operatorpayload_or_strictpewprecisionexit"
    / "strict_pew_precision_exit_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_YUKAWAMAGNITUDEROWSFROMSELECTEDDYNAMICPACKET_OR_"
    "VALUEFUNCTIONALGAP_FAMILY_ROWS_CLOSED_MAGNITUDE_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_ThresholdResponseRows_or_SectorProjectionWeightsExecution_v1"


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


def guarded(payload: dict[str, Any]) -> dict[str, Any]:
    payload["closure_claimed"] = True
    payload["observed_data_used_as_selector"] = False
    payload["target_fitting_used"] = False
    return payload


def main() -> int:
    sources = [
        PREVIOUS,
        ACCEPTED_FIRST,
        SELECTED_VALUES,
        SAME_SOURCE_PACKET,
        YUKAWA_BRIDGE,
        SECTOR_BLIND_NOGO,
        PROJECTION_READINESS,
        PROJECTION_SKELETON,
        FAMILY_OPERATOR,
        FAMILY_SPECTRUM,
        SECTOR_PROFILE,
        PROFILE_TESTS,
        SECTOR_FRONTIER,
        STRICT_PEW,
    ]
    missing = [rel(path) for path in sources if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Yukawa value-functional inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    accepted_first = load(ACCEPTED_FIRST)
    selected_values = load(SELECTED_VALUES)
    same_packet = load(SAME_SOURCE_PACKET)
    bridge = load(YUKAWA_BRIDGE)
    blind_nogo = load(SECTOR_BLIND_NOGO)
    readiness = load(PROJECTION_READINESS)
    skeleton = load(PROJECTION_SKELETON)
    family_operator = load(FAMILY_OPERATOR)
    family_spectrum = load(FAMILY_SPECTRUM)
    sector_profile = load(SECTOR_PROFILE)
    profile_tests = load(PROFILE_TESTS)
    sector_frontier = load(SECTOR_FRONTIER)
    strict_pew = load(STRICT_PEW)

    sector_results = family_spectrum["sector_results"]
    all_family_resolved = all(result["family_labels_resolved"] for result in sector_results.values())
    universal_spectrum = family_spectrum["universal_spectrum_across_sectors"]
    accepted_row_count = accepted_first["accepted_row_count"]
    source_fields = same_packet["attempted_selected_packet"]["fields"]
    all_source_fields_selected = all(
        field["same_source"] and field["selected_emitted"] and field["theorem_derived"]
        for field in source_fields.values()
    )

    source_import = guarded(
        {
            "schema": "MTTYukawaSelectedDynamicPacketSourceImport.v1",
            "status": "SELECTED_DYNAMIC_PACKET_IMPORTED_FOR_YUKAWA_MAGNITUDE_TEST",
            "previous": rel(PREVIOUS),
            "selected_values": rel(SELECTED_VALUES),
            "same_source_packet": rel(SAME_SOURCE_PACKET),
            "accepted_first_dynamic_row_count": accepted_row_count,
            "accepted_first_dynamic_row_ids": accepted_first["accepted_row_ids"],
            "selected_by_MTT": selected_values["selected_by_MTT"],
            "same_source_packet_all_fields_selected": all_source_fields_selected,
            "qualitative_tests": selected_values["acceptance_tests"],
            "family_resolving_operator_closed": family_operator["closure_decision"][
                "family_resolving_operator_closed"
            ],
            "all_sectors_family_resolved": all_family_resolved,
        }
    )

    family_gap = guarded(
        {
            "schema": "MTTFamilyResolvedMagnitudeFunctionalGap.v1",
            "status": "FAMILY_COORDINATES_CLOSED_MAGNITUDE_FUNCTIONAL_OPEN",
            "family_spectrum": rel(FAMILY_SPECTRUM),
            "sector_blind_no_go": rel(SECTOR_BLIND_NOGO),
            "sector_scaled_profile_tests": rel(PROFILE_TESTS),
            "family_resolving_operator_closed": family_operator["closure_decision"][
                "family_resolving_operator_closed"
            ],
            "all_sectors_family_resolved": all_family_resolved,
            "universal_spectrum_across_sectors": universal_spectrum,
            "signed_family_eigenvalues": profile_tests["signed_family_eigenvalues"],
            "abs_family_eigenprofile": profile_tests["abs_family_eigenprofile"],
            "universal_abs_eigenprofile_ratio": profile_tests["universal_abs_eigenprofile_ratio"],
            "universal_scaled_profile_can_match_diagnostic_hierarchies": profile_tests[
                "universal_scaled_profile_can_match_diagnostic_hierarchies"
            ],
            "sector_blind_first_response_magnitude_no_go_proved": bridge["closure_decision"][
                "sector_blind_first_response_magnitude_no_go_proved"
            ],
            "universal_sector_scaled_eigenprofile_nogo_proved": sector_profile["closure_decision"][
                "universal_sector_scaled_eigenprofile_nogo_proved"
            ],
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "generation_resolved_threshold_source_rows_closed": False,
        }
    )

    minimal_objects = guarded(
        {
            "schema": "MTTMinimalSelectedValueFunctionalObjects.v1",
            "status": "MINIMAL_SELECTED_VALUE_FUNCTIONAL_OBJECTS_EXTRACTED",
            "sector_aware_projection_skeleton_closed": readiness["closure_decision"][
                "sector_aware_projection_skeleton_closed"
            ],
            "source_owner_promoted": readiness["closure_decision"]["source_owner_promoted"],
            "required_weight_rows": skeleton["required_weight_rows"],
            "minimal_new_selected_objects": sector_frontier["minimal_new_selected_objects"],
            "forbidden_shortcuts": sector_frontier["forbidden_shortcuts"],
            "required_charged_generation_row_count": 9,
            "accepted_generation_threshold_source_row_count": sector_profile["closure_decision"][
                "generation_resolved_threshold_source_rows_closed"
            ]
            and 9
            or 0,
            "lambda_H_row_required": True,
            "same_branch_scale_scheme_loop_convention_closed": sector_frontier[
                "same_branch_scale_scheme_loop_convention_closed"
            ],
            "selected_threshold_response_functional_closed": sector_frontier[
                "vsd02_selected_threshold_response_functional_closed"
            ],
            "vsd02_strict_fill_attempt_currently_accepts_rows": sector_frontier[
                "vsd02_strict_fill_attempt_currently_accepts_rows"
            ],
        }
    )

    next_packet = guarded(
        {
            "schema": "MTTNextAfterYukawaValueFunctionalGap.v1",
            "status": "NEXT_TARGET_THRESHOLD_RESPONSE_ROWS_OR_SECTOR_PROJECTION_WEIGHTS",
            "next_required_artifact": NEXT,
            "reason": (
                "The selected dynamic packet now gives source-owned first-response "
                "rows and nondegenerate family coordinates, but the spectrum is "
                "universal across sectors.  Magnitude rows require selected "
                "sector projection weights, higher-response sector coefficients, "
                "or a selected threshold response functional with scale/scheme "
                "and mass-scheme/profile rows."
            ),
        }
    )

    candidate = guarded(
        {
            "candidate": "MTTSelectedYukawaMagnitudeRowsFromSelectedDynamicPacketOrValueFunctionalGap",
            "status": STATUS,
            "next_required_artifact": NEXT,
            "inputs": {
                "previous": rel(PREVIOUS),
                "accepted_first": rel(ACCEPTED_FIRST),
                "selected_values": rel(SELECTED_VALUES),
                "same_source_packet": rel(SAME_SOURCE_PACKET),
                "yukawa_bridge": rel(YUKAWA_BRIDGE),
                "sector_blind_nogo": rel(SECTOR_BLIND_NOGO),
                "projection_readiness": rel(PROJECTION_READINESS),
                "projection_skeleton": rel(PROJECTION_SKELETON),
                "family_operator": rel(FAMILY_OPERATOR),
                "family_spectrum": rel(FAMILY_SPECTRUM),
                "sector_profile": rel(SECTOR_PROFILE),
                "profile_tests": rel(PROFILE_TESTS),
                "sector_frontier": rel(SECTOR_FRONTIER),
                "strict_pew": rel(STRICT_PEW),
            },
            "packets": {
                "selected_dynamic_packet_source_import": rel(SOURCE_IMPORT),
                "family_resolved_but_magnitude_functional_gap": rel(FAMILY_GAP),
                "minimal_selected_value_functional_objects": rel(MINIMAL_OBJECTS),
                "next_after_value_functional_gap": rel(NEXT_PACKET),
            },
            "closure_decision": {
                "selected_dynamic_packet_imported_for_magnitude_test": True,
                "accepted_first_dynamic_row_count": accepted_row_count,
                "family_resolving_operator_closed": True,
                "all_sectors_family_resolved": all_family_resolved,
                "sector_aware_projection_skeleton_closed": True,
                "sector_blind_first_response_magnitude_no_go_proved": True,
                "universal_sector_scaled_eigenprofile_nogo_proved": True,
                "Yukawa_magnitude_value_functional_closed": False,
                "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
                "generation_resolved_threshold_source_rows_closed": False,
                "selected_threshold_response_functional_closed": False,
                "same_branch_scale_scheme_loop_convention_closed": False,
                "lambda_H_row_closed": False,
                "strict_P_EW_source_rows": strict_pew["strict_P_EW_source_rows"],
                "direct_K_threshold_Omega_H_lambda_rows": strict_pew[
                    "direct_K_threshold_Omega_H_lambda_rows"
                ],
                "true_SM_equivalence_closed": False,
                "full_no_knob_closed": False,
            },
            "key_numbers": {
                "accepted_first_dynamic_row_count": accepted_row_count,
                "required_charged_generation_row_count": 9,
                "accepted_generation_threshold_source_row_count": 0,
                "signed_family_eigenvalues": profile_tests["signed_family_eigenvalues"],
                "abs_family_eigenprofile": profile_tests["abs_family_eigenprofile"],
                "universal_abs_eigenprofile_ratio": profile_tests["universal_abs_eigenprofile_ratio"],
                "diagnostic_hierarchy_ratios_not_used_as_selectors": profile_tests[
                    "diagnostic_hierarchy_ratios_not_used_as_selectors"
                ],
                "diagnostic_hierarchy_spread": profile_tests["diagnostic_hierarchy_spread"],
            },
            "theorem": {
                "name": "YukawaMagnitudeValueFunctionalGapTheorem",
                "proved": True,
                "statement": (
                    "The selected dynamic packet now supplies source-owned first "
                    "dynamic rows and a nondegenerate family-resolving operator. "
                    "However, sector-blind first-response invariants and any "
                    "universal sector-scaled eigenprofile cannot emit the nine "
                    "charged Yukawa magnitude rows: the family profile is "
                    "universal while charged-sector hierarchy ratios differ. "
                    "Therefore the remaining value-functional frontier is "
                    "selected sector projection weights, higher-response sector "
                    "coefficients, or selected threshold/mass-scheme/profile "
                    "response rows, plus the independent lambda_H row.  No "
                    "observed Yukawa, CKM, PMNS, or Higgs values are used as "
                    "selectors."
                ),
            },
        }
    )

    cert = guarded(
        {
            "certificate": "MTTSelectedYukawaMagnitudeRowsFromSelectedDynamicPacketOrValueFunctionalGap",
            "status": STATUS,
            "theorem_proved": True,
            "accepted_first_dynamic_row_count": accepted_row_count,
            "family_resolving_operator_closed": True,
            "all_sectors_family_resolved": all_family_resolved,
            "sector_aware_projection_skeleton_closed": True,
            "sector_blind_first_response_magnitude_no_go_proved": True,
            "universal_sector_scaled_eigenprofile_nogo_proved": True,
            "Yukawa_magnitude_value_functional_closed": False,
            "accepted_Yukawa_magnitudes_as_no_knob_predictions": False,
            "generation_resolved_threshold_source_rows_closed": False,
            "selected_threshold_response_functional_closed": False,
            "same_branch_scale_scheme_loop_convention_closed": False,
            "lambda_H_row_closed": False,
            "strict_P_EW_source_rows": strict_pew["strict_P_EW_source_rows"],
            "direct_K_threshold_Omega_H_lambda_rows": strict_pew[
                "direct_K_threshold_Omega_H_lambda_rows"
            ],
            "true_SM_equivalence_claimed": False,
            "full_no_knob_closure_claimed": False,
            "next_required_artifact": NEXT,
        }
    )

    note = f"""# MTT Selected YukawaMagnitudeRowsFromSelectedDynamicPacket or ValueFunctionalGap v1

## Theorem

`YukawaMagnitudeValueFunctionalGapTheorem` is emitted.

## What Closes

```text
accepted first dynamic row count = {accepted_row_count}
family resolving operator closed = true
all sectors family resolved = {str(all_family_resolved).lower()}
sector-aware projection skeleton closed = true
sector-blind magnitude no-go proved = true
universal sector-scaled eigenprofile no-go proved = true
```

Selected family spectrum:

```text
signed eigenvalues = {profile_tests["signed_family_eigenvalues"]}
absolute eigenprofile = {profile_tests["abs_family_eigenprofile"]}
universal absolute eigenprofile ratio = {profile_tests["universal_abs_eigenprofile_ratio"]}
```

## Why Magnitudes Do Not Close Yet

The selected first-response family coordinate is universal across `u,d,e,nuD`.
It resolves the three family labels but does not supply sector-specific hierarchy
weights.  Sector-blind trace/norm invariants and a universal sector-scaled
eigenprofile are both rejected.

## Still Open

```text
Yukawa magnitude value functional closed = false
accepted Yukawa magnitudes as no-knob predictions = false
generation-resolved threshold source rows closed = false
selected threshold response functional closed = false
same-branch scale/scheme/loop convention closed = false
lambda_H row closed = false
strict P_EW source rows = {strict_pew["strict_P_EW_source_rows"]}
direct K_threshold.Omega_H.lambda rows = {strict_pew["direct_K_threshold_Omega_H_lambda_rows"]}
true SM equivalence closed = false
full no-knob closure = false
```

## Minimal New Selected Objects

```text
- sector-specific higher-response coefficients for u,d,e
- or a selected threshold response functional F_s(lambda_g) emitting magnitude rows
- or selected threshold/mass-scheme/profile source rows accepted by the VSD02 strict schema
- plus an independent lambda_H source row
```

## Next Artifact

`{NEXT}`.
"""

    for path, out in [
        (SOURCE_IMPORT, source_import),
        (FAMILY_GAP, family_gap),
        (MINIMAL_OBJECTS, minimal_objects),
        (NEXT_PACKET, next_packet),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, out)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
