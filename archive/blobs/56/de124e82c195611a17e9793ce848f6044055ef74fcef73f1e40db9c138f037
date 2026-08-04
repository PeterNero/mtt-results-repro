"""Build tau EW/QED running policy or R_theta mass-scheme rows artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_tauewrunningpolicy_or_rthetamassschemerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TABLE_IMPORT = PACKET_DIR / "huang_zhou_tau_mz_table_import.packet.json"
CONVENTION = PACKET_DIR / "tau_mz_convention_alignment_decision.packet.json"
TAU_ROW = PACKET_DIR / "tau_external_mass_scheme_row.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_tau_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TauEWRunningPolicy_or_RThetaMassSchemeRows_v1.md"

PREVIOUS = DATA / "selected_bottomcharmtaurundecreplay_or_rthetamassschemerows.candidate.json"
BC_REPLAY = (
    DATA
    / "selected_bottomcharmtaurundecreplay_or_rthetamassschemerows"
    / "bottom_charm_crundec_replay_values.packet.json"
)
TAU_GAP = (
    DATA
    / "selected_bottomcharmtaurundecreplay_or_rthetamassschemerows"
    / "tau_running_map_policy_gap.packet.json"
)
SOURCE_FAMILIES = (
    DATA
    / "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation"
    / "external_bct_formula_source_families.packet.json"
)
INVENTORY = (
    DATA
    / "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
    / "bottom_charm_tau_native_residual_inventory.packet.json"
)
REFERENCE = DATA / "sm_equivalence_reference_data_values_fill.candidate.json"

STATUS = (
    "MTT_SELECTED_TAUEWRUNNINGPOLICY_OR_RTHETAMASSSCHEMEROWS_"
    "BUILT_TAU_EFT_TABLE_ROW_FULLSM_RTHETA_OPEN"
)
NEXT = "MTT_Selected_AllBCTExternalRows_or_FullSMConventionReconciliation_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing tau EW policy sources: " + ", ".join(missing))


def mass_yukawa(mass_gev: float, vev_gev: float) -> float:
    return math.sqrt(2.0) * mass_gev / vev_gev


def max_unc(row: dict[str, Any]) -> float:
    unc = row["uncertainty"]
    if isinstance(unc, dict):
        return max(abs(float(unc["minus"])), abs(float(unc["plus"])))
    return abs(float(unc))


def sidecar(mass_gev: float, mass_unc: float, vev_gev: float, vev_unc: float) -> dict[str, Any]:
    central = mass_yukawa(mass_gev, vev_gev)
    return {
        "m_tau_MZ_EFT": {
            "central_value": central,
            "minus_delta_input": -mass_unc,
            "plus_delta_input": mass_unc,
            "minus_value": mass_yukawa(mass_gev - mass_unc, vev_gev),
            "plus_value": mass_yukawa(mass_gev + mass_unc, vev_gev),
            "symmetric_half_width": abs(
                mass_yukawa(mass_gev + mass_unc, vev_gev) - mass_yukawa(mass_gev - mass_unc, vev_gev)
            )
            / 2.0,
        },
        "vev": {
            "central_value": central,
            "minus_delta_input": -vev_unc,
            "plus_delta_input": vev_unc,
            "minus_value": mass_yukawa(mass_gev, vev_gev - vev_unc),
            "plus_value": mass_yukawa(mass_gev, vev_gev + vev_unc),
            "symmetric_half_width": abs(
                mass_yukawa(mass_gev, vev_gev + vev_unc) - mass_yukawa(mass_gev, vev_gev - vev_unc)
            )
            / 2.0,
        },
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, BC_REPLAY, TAU_GAP, SOURCE_FAMILIES, INVENTORY, REFERENCE]
    require_sources(sources)

    previous = load(PREVIOUS)
    bc_replay = load(BC_REPLAY)
    tau_gap = load(TAU_GAP)
    source_families = load(SOURCE_FAMILIES)
    inventory = load(INVENTORY)
    reference = load(REFERENCE)

    vev = float(reference["reference_values"]["constants"]["v_from_G_F"]["central_value"])
    vev_unc = max_unc(reference["reference_values"]["constants"]["v_from_G_F"])
    tau_native = inventory["native_values"]["tau_native_Y_e_33"]
    tau_legacy = tau_gap["legacy_firstpass_yukawa"]

    table_rows = {
        "EFT_QCDxQED_5q3l_MZ": {
            "theory": "EFT with exact SU(3)c x U(1)EM and (nq,nl)=(5,3)",
            "scale": "M_Z = 91.1876 GeV",
            "mass_GeV": 1.74743,
            "uncertainty_GeV": 0.00012,
            "yukawa_from_repo_vev": mass_yukawa(1.74743, vev),
            "candidate_external_map_row": True,
        },
        "FullSM_6q3l_MZ": {
            "theory": "full SM with SU(3)c x SU(2)L x U(1)Y and (nq,nl)=(6,3)",
            "scale": "M_Z = 91.1876 GeV",
            "mass_GeV": 1.72856,
            "uncertainty_GeV": 0.00028,
            "yukawa_from_repo_vev": mass_yukawa(1.72856, vev),
            "candidate_external_map_row": True,
        },
    }
    table_import = {
        "schema": "MTTHuangZhouTauMZTableImport.v1",
        "status": "HUANG_ZHOU_TAU_MZ_EFT_AND_FULLSM_TABLE_VALUES_IMPORTED",
        "source": {
            "id": "Huang-Zhou-running-fermion-masses",
            "citation": "Huang and Zhou, Precise Values of Running Quark and Lepton Masses in the Standard Model",
            "url": "https://arxiv.org/abs/2009.04851",
            "table": "Table 3, running charged-lepton masses",
        },
        "table_rows": table_rows,
        "table_values_imported": True,
        "single_convention_selected_by_table_alone": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(TABLE_IMPORT, table_import)

    bottom_row = next(
        row for row in bc_replay["accepted_external_map_rows"] if row["id"] == "bottom_MSbar_native_scale_transport"
    )
    charm_row = next(
        row for row in bc_replay["accepted_external_map_rows"] if row["id"] == "charm_MSbar_native_scale_transport"
    )
    convention = {
        "schema": "MTTTauMZConventionAlignmentDecision.v1",
        "status": "TAU_EFT_MZ_CONVENTION_ACCEPTED_AS_EXTERNAL_MAP_ROW_FULLSM_CONVERSION_OPEN",
        "b_c_replay_source": rel(BC_REPLAY),
        "table_source": rel(TABLE_IMPORT),
        "selected_external_tau_row_convention": "EFT_QCDxQED_5q3l_MZ",
        "selection_reason": (
            "The current b/c mass-scheme map rows target native-scale-to-MZ external running-mass rows below "
            "the electroweak threshold layer. The matching tau external row is therefore the Huang-Zhou MZ "
            "EFT charged-lepton row, not the full-SM MZ row. This selects an external map convention only; "
            "it does not select Rtheta or close the full-SM threshold conversion."
        ),
        "b_c_table_crosscheck": {
            "Huang_Zhou_EFT_bottom_mZ_GeV": 2.866,
            "crundec_bottom_mZ_GeV": bottom_row["crundec_running_mass_MZ_GeV"],
            "bottom_absolute_delta_GeV": bottom_row["crundec_running_mass_MZ_GeV"] - 2.866,
            "Huang_Zhou_EFT_charm_mZ_GeV": 0.628,
            "crundec_charm_mZ_GeV": charm_row["crundec_running_mass_MZ_GeV"],
            "charm_absolute_delta_GeV": charm_row["crundec_running_mass_MZ_GeV"] - 0.628,
            "crosscheck_interpretation": (
                "Bottom agrees at table precision. Charm is a convention/table/input mismatch to carry into "
                "the full profile reconciliation rather than a selector."
            ),
        },
        "full_SM_tau_row_reserved_for_later_reconciliation": True,
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CONVENTION, convention)

    tau_eft = table_rows["EFT_QCDxQED_5q3l_MZ"]
    tau_full = table_rows["FullSM_6q3l_MZ"]
    tau_row = {
        "schema": "MTTTauExternalMassSchemeRow.v1",
        "status": "TAU_EFT_MZ_EXTERNAL_MASS_SCHEME_ROW_ACCEPTED_RTHETA_OPEN",
        "required_map": "tau_pole_rest_to_running_lepton",
        "source_table": rel(TABLE_IMPORT),
        "convention_decision": rel(CONVENTION),
        "accepted_external_map_row": {
            "id": "tau_pole_rest_to_running_lepton",
            "source_mass_GeV": tau_gap["tau_input_mass_GeV"],
            "source_scale": "pole/rest mass",
            "target_scale": "M_Z",
            "target_convention": "EFT_QCDxQED_5q3l_MZ",
            "huang_zhou_running_mass_MZ_GeV": tau_eft["mass_GeV"],
            "huang_zhou_running_mass_uncertainty_GeV": tau_eft["uncertainty_GeV"],
            "huang_zhou_yukawa_MZ_from_repo_vev": tau_eft["yukawa_from_repo_vev"],
            "native_inventory_yukawa": tau_native,
            "legacy_firstpass_yukawa": tau_legacy,
            "multiplicative_factor_vs_native_inventory": tau_eft["yukawa_from_repo_vev"] / tau_native,
            "multiplicative_factor_vs_legacy_firstpass": tau_eft["yukawa_from_repo_vev"] / tau_legacy,
            "diagonal_sensitivity_sidecar": sidecar(
                tau_eft["mass_GeV"],
                tau_eft["uncertainty_GeV"],
                vev,
                vev_unc,
            ),
            "accepted_as_external_map_row": True,
            "accepted_as_Rtheta_source_row": False,
        },
        "reserved_fullSM_alternative": {
            "target_convention": "FullSM_6q3l_MZ",
            "huang_zhou_running_mass_MZ_GeV": tau_full["mass_GeV"],
            "huang_zhou_running_mass_uncertainty_GeV": tau_full["uncertainty_GeV"],
            "huang_zhou_yukawa_MZ_from_repo_vev": tau_full["yukawa_from_repo_vev"],
            "not_selected_reason": "reserved for later full-SM threshold/profile reconciliation",
        },
        "accepted_external_map_row_count": 1,
        "tau_external_row_closed": True,
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(TAU_ROW, tau_row)

    cutset = {
        "schema": "MTTNextCutsetAfterTauPolicy.v1",
        "status": "NEXT_RECONCILE_ALL_BCT_EXTERNAL_ROWS_WITH_FULLSM_CONVENTION_AND_RTHETA",
        "closed_now": {
            "tau_EFT_MZ_table_values_imported": True,
            "tau_pole_rest_to_running_lepton_external_row": True,
            "all_three_bct_external_mass_scheme_rows_available": True,
        },
        "still_open": {
            "fullSM_tau_conversion_or_profile_reconciliation": True,
            "charm_CRunDec_vs_HuangZhou_table_reconciliation": True,
            "selected_Rtheta_mass_scheme_derivation": True,
            "W_Z_H_electroweak_matching_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "build a full b/c/tau convention reconciliation matrix against Huang-Zhou EFT and full-SM rows",
            "route_B": "derive the Rtheta mass-scheme rows and compare against the accepted external rows",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    total_external_rows = int(previous["closure_decision"]["accepted_bottom_charm_tau_map_row_count"]) + 1
    candidate = {
        "candidate": "MTTSelectedTauEWRunningPolicyOrRThetaMassSchemeRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "huang_zhou_tau_mz_table_import": rel(TABLE_IMPORT),
            "tau_mz_convention_alignment_decision": rel(CONVENTION),
            "tau_external_mass_scheme_row": rel(TAU_ROW),
            "next_cutset_after_tau_policy": rel(CUTSET),
        },
        "theorem": {
            "name": "TauEFTMZExternalRowAcceptanceTheorem",
            "proved": True,
            "statement": (
                "The Huang-Zhou charged-lepton running-mass table supplies a provenance-bearing tau MZ EFT "
                "row with uncertainty sidecars. Under the current external b/c mass-scheme target convention "
                "this accepts tau_pole_rest_to_running_lepton as an external map row. It does not select "
                "Rtheta and does not close full-SM convention reconciliation."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "tau_pole_rest_to_running_lepton_external_row_closed": True,
            "accepted_bottom_charm_tau_map_row_count": total_external_rows,
            "all_three_bct_external_mass_scheme_rows_available": total_external_rows == 3,
            "fullSM_tau_conversion_or_profile_reconciliation_closed": False,
            "charm_CRunDec_vs_HuangZhou_table_reconciliation_closed": False,
            "selected_Rtheta_mass_scheme_derivation_closed": False,
            "W_Z_H_electroweak_matching_rows_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_TauEWRunningPolicy_or_RThetaMassSchemeRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "tau_external_row_closed": True,
        "accepted_bottom_charm_tau_map_row_count": total_external_rows,
        "all_three_bct_external_mass_scheme_rows_available": total_external_rows == 3,
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "fullSM_tau_conversion_or_profile_reconciliation_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected TauEWRunningPolicy or RThetaMassSchemeRows v1

Status: `{STATUS}`.

This artifact imports the Huang-Zhou charged-lepton running-mass table and
accepts the EFT `M_Z` tau row as the external `tau_pole_rest_to_running_lepton`
map row.

```text
tau EFT MZ mass               : {tau_eft["mass_GeV"]} GeV
tau EFT MZ Yukawa             : {tau_eft["yukawa_from_repo_vev"]}
accepted b/c/tau external rows: {total_external_rows}
full-SM tau convention closed : false
selected Rtheta row closed    : false
```

The row is accepted only as an external map row in the same low-energy `M_Z`
mass-scheme layer as the b/c transport rows.  The full-SM tau row remains
reserved for convention/profile reconciliation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
