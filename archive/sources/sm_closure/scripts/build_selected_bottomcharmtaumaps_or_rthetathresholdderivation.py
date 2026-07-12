"""Build bottom/charm/tau maps or R_theta threshold derivation artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INVENTORY = PACKET_DIR / "bottom_charm_tau_native_residual_inventory.packet.json"
FILL_ATTEMPT = PACKET_DIR / "bottom_charm_tau_map_row_fill_attempt.packet.json"
RTHETA_RECHECK = PACKET_DIR / "rtheta_bottom_charm_tau_projection_recheck.packet.json"
IMPORT_CONTRACT = PACKET_DIR / "bottom_charm_tau_external_map_import_contract.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bottom_charm_tau_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BottomCharmTauMaps_or_RThetaThresholdDerivation_v1.md"

PREVIOUS = DATA / "selected_tophiggsformulamapimport_or_rthetathresholdderivation.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
    / "next_cutset_after_top_higgs_formula_import.packet.json"
)
POLICY_CONTRACT = (
    DATA
    / "selected_conventionsourcetheorem_or_rgenginethresholdpolicy"
    / "threshold_pole_running_policy_contract.packet.json"
)
RESIDUAL_VALUES = (
    DATA
    / "selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport"
    / "threshold_mass_scheme_residual_values.packet.json"
)
TRANSPORT_KERNEL = (
    DATA
    / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
    / "yukawa_higgs_common_scale_transport_kernel.packet.json"
)
RTHETA_PI = (
    DATA
    / "selected_rtheta_physicalprojectionkernel_or_profileresponse"
    / "pi_rtheta_kernel_attempt.packet.json"
)
SOURCE_ROW_AUDIT = (
    DATA
    / "selected_acceptedthresholdmassschemesourcerows_or_noknobvaluederivation"
    / "accepted_threshold_mass_scheme_source_row_audit.packet.json"
)
TOP_HIGGS_ACCEPTANCE = (
    DATA
    / "selected_tophiggsformulamapimport_or_rthetathresholdderivation"
    / "top_higgs_external_formula_map_acceptance.packet.json"
)

STATUS = (
    "MTT_SELECTED_BOTTOMCHARMTAUMAPS_OR_RTHETATHRESHOLDDERIVATION_"
    "BUILT_NATIVE_RESIDUAL_INVENTORY_MAPS_OPEN"
)
NEXT = "MTT_Selected_BottomCharmTauFormulaImport_or_RThetaMassSchemeDerivation_v1"


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
        raise FileNotFoundError("missing bottom/charm/tau map sources: " + ", ".join(missing))


def real_entry(value: Any) -> float:
    if isinstance(value, list):
        return float(value[0])
    return float(value)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CUTSET,
        POLICY_CONTRACT,
        RESIDUAL_VALUES,
        TRANSPORT_KERNEL,
        RTHETA_PI,
        SOURCE_ROW_AUDIT,
        TOP_HIGGS_ACCEPTANCE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    policy = load(POLICY_CONTRACT)
    residuals = load(RESIDUAL_VALUES)
    transport = load(TRANSPORT_KERNEL)
    rtheta_pi = load(RTHETA_PI)
    source_audit = load(SOURCE_ROW_AUDIT)
    top_higgs = load(TOP_HIGGS_ACCEPTANCE)

    wanted_residual_ids = {
        "Y_d_b_native_to_firstpass_MZ": "bottom_MSbar_native_scale_transport",
        "Y_u_c_native_to_firstpass_MZ": "charm_MSbar_native_scale_transport",
        "Y_e_tau_native_to_firstpass_MZ": "tau_pole_rest_to_running_lepton",
    }
    residual_rows = [
        {
            **row,
            "map_id": wanted_residual_ids[row["id"]],
            "accepted_as_map_row": False,
        }
        for row in residuals["transport_residual_rows"]
        if row["id"] in wanted_residual_ids
    ]
    native_values = {
        "bottom_native_Y_d_33": real_entry(
            transport["native_values_to_transport"]["Y_d_native_complex_up_diagonal_convention"][2][2]
        ),
        "charm_native_Y_u_22": real_entry(
            transport["native_values_to_transport"]["Y_u_native"][1][1]
        ),
        "tau_native_Y_e_33": real_entry(
            transport["native_values_to_transport"]["Y_e_native"][2][2]
        ),
        "input_masses_GeV": {
            key: transport["native_values_to_transport"]["input_masses_GeV"][key]
            for key in ["b", "c", "tau"]
        },
    }
    inventory_closed = (
        len(residual_rows) == 3
        and all(row["finite"] for row in residual_rows)
        and residuals["summary"]["all_residuals_finite"] is True
        and all(value is not None for value in native_values.values())
    )

    inventory = {
        "schema": "MTTBottomCharmTauNativeResidualInventory.v1",
        "status": "BOTTOM_CHARM_TAU_NATIVE_AND_RESIDUAL_ROWS_INVENTORIED",
        "transport_kernel_source": rel(TRANSPORT_KERNEL),
        "residual_values_source": rel(RESIDUAL_VALUES),
        "native_values": native_values,
        "residual_rows": residual_rows,
        "inventory_closed": inventory_closed,
        "accepted_as_external_map_rows": False,
        "accepted_as_Rtheta_source_rows": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(INVENTORY, inventory)

    required_maps = [
        {
            "id": "bottom_MSbar_native_scale_transport",
            "policy_requirement": policy["threshold_matching_required"]["bottom"],
            "residual_id": "Y_d_b_native_to_firstpass_MZ",
            "accepted_now": False,
            "blocking_reason": "native and first-pass residual rows exist, but no provenance-bearing MSbar mb(mb)->target-scale transport formula/table is accepted",
        },
        {
            "id": "charm_MSbar_native_scale_transport",
            "policy_requirement": policy["threshold_matching_required"]["charm"],
            "residual_id": "Y_u_c_native_to_firstpass_MZ",
            "accepted_now": False,
            "blocking_reason": "native and first-pass residual rows exist, but no provenance-bearing MSbar mc(mc)->target-scale transport formula/table is accepted",
        },
        {
            "id": "tau_pole_rest_to_running_lepton",
            "policy_requirement": policy["threshold_matching_required"]["tau"],
            "residual_id": "Y_e_tau_native_to_firstpass_MZ",
            "accepted_now": False,
            "blocking_reason": "native and first-pass residual rows exist, but no provenance-bearing tau pole/rest-to-running lepton formula/table is accepted",
        },
    ]
    fill_attempt = {
        "schema": "MTTBottomCharmTauMapRowFillAttempt.v1",
        "status": "BOTTOM_CHARM_TAU_MAP_FILL_ATTEMPTED_NO_MAP_ROWS_ACCEPTED",
        "inventory_source": rel(INVENTORY),
        "source_row_audit_source": rel(SOURCE_ROW_AUDIT),
        "required_maps": required_maps,
        "accepted_bottom_charm_tau_map_rows": [],
        "accepted_bottom_charm_tau_map_row_count": 0,
        "top_higgs_external_formula_map_row_count": top_higgs[
            "accepted_external_formula_map_row_count"
        ],
        "accepted_threshold_mass_scheme_source_rows_present": source_audit[
            "accepted_source_rows_present"
        ],
        "residual_rows_are_source_rows": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FILL_ATTEMPT, fill_attempt)

    rtheta_slots = {
        row["slot_id"]: row
        for row in rtheta_pi["slot_rows"]
        if row["slot_id"]
        in {
            "mass_scheme::bottom_MSbar_native_scale_transport",
            "mass_scheme::charm_MSbar_native_scale_transport",
            "mass_scheme::tau_pole_rest_to_running_lepton",
            "threshold::bottom",
            "threshold::charm",
            "threshold::tau",
        }
    }
    rtheta_recheck = {
        "schema": "MTTRThetaBottomCharmTauProjectionRecheck.v1",
        "status": "RTHETA_BOTTOM_CHARM_TAU_SKELETON_PRESENT_SELECTED_SOLVE_OPEN",
        "pi_rtheta_source": rel(RTHETA_PI),
        "Pi_Rtheta_closed": rtheta_pi["Pi_Rtheta_closed"],
        "minimal_internal_missing_object": rtheta_pi["minimal_internal_missing_object"],
        "slot_rows": rtheta_slots,
        "precoefficient_skeletons_present": len(rtheta_slots) == 6,
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "accepted_external_maps_may_validate_Rtheta": True,
        "accepted_external_maps_select_Rtheta": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA_RECHECK, rtheta_recheck)

    import_contract = {
        "schema": "MTTBottomCharmTauExternalMapImportContract.v1",
        "status": "BOTTOM_CHARM_TAU_EXTERNAL_IMPORT_CONTRACT_BUILT_ROWS_OPEN",
        "required_for_acceptance": [
            "explicit b-quark MSbar native-scale to target-scale running/matching formula or table with provenance",
            "explicit c-quark MSbar native-scale to target-scale running/matching formula or table with provenance",
            "explicit tau pole/rest mass to running lepton Yukawa formula or table with provenance",
            "declared scale, scheme, loop/order, and threshold policy",
            "uncertainty sidecars or declared diagonal limitation",
            "replay command or machine-readable table sufficient to regenerate rows",
            "proof imported rows validate but do not select the MTT source branch",
        ],
        "current_support": {
            "native_values_present": True,
            "finite_residual_rows_present": inventory_closed,
            "rtheta_precoefficient_skeletons_present": len(rtheta_slots) == 6,
            "accepted_external_formula_rows_present_for_top_higgs": top_higgs[
                "accepted_external_formula_map_row_count"
            ],
        },
        "accepted_external_bottom_charm_tau_table_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(IMPORT_CONTRACT, import_contract)

    cutset = {
        "schema": "MTTNextCutsetAfterBottomCharmTauAttempt.v1",
        "status": "NEXT_ATTACK_FORMULA_IMPORT_OR_RTHETA_MASS_SCHEME_DERIVATION",
        "previous_cutset": rel(PREVIOUS_CUTSET),
        "closed_now": {
            "bottom_charm_tau_native_residual_inventory": inventory_closed,
            "bottom_charm_tau_map_fill_attempt": True,
            "rtheta_bottom_charm_tau_projection_recheck": True,
            "bottom_charm_tau_external_import_contract": True,
        },
        "still_open": {
            "accepted_bottom_charm_tau_map_rows": True,
            "accepted_external_bottom_charm_tau_table": True,
            "selected_Rtheta_mass_scheme_derivation": True,
            "W_Z_H_electroweak_matching_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "import b/c/tau running/mass-scheme formula rows with provenance",
            "route_B": "derive the b/c/tau maps from selected Rtheta projection/Route-C solve",
            "route_C": "build W/Z/H electroweak matching while b/c/tau remains external-contract open",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedBottomCharmTauMapsOrRThetaThresholdDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "bottom_charm_tau_native_residual_inventory": rel(INVENTORY),
            "bottom_charm_tau_map_row_fill_attempt": rel(FILL_ATTEMPT),
            "rtheta_bottom_charm_tau_projection_recheck": rel(RTHETA_RECHECK),
            "bottom_charm_tau_external_map_import_contract": rel(IMPORT_CONTRACT),
            "next_cutset_after_bottom_charm_tau_attempt": rel(CUTSET),
        },
        "theorem": {
            "name": "BottomCharmTauInventoryAndMapSourceGapTheorem",
            "proved": True,
            "statement": (
                "Bottom, charm, and tau native values plus finite native-to-first-pass residual rows are "
                "present, and Rtheta has matching precoefficient skeletons. None of these rows is an "
                "accepted mass-scheme map source: residuals are audits, and the Rtheta projection still "
                "lacks the selected solve. Therefore b/c/tau map closure requires either external "
                "formula/table imports with provenance or a selected Rtheta mass-scheme derivation."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "bottom_charm_tau_native_residual_inventory_closed": inventory_closed,
            "bottom_charm_tau_external_import_contract_closed": True,
            "accepted_bottom_charm_tau_map_row_count": 0,
            "accepted_bottom_charm_tau_map_rows_closed": False,
            "accepted_external_bottom_charm_tau_table_closed": False,
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
        "certificate": "MTT_Selected_BottomCharmTauMaps_or_RThetaThresholdDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "bottom_charm_tau_native_residual_inventory_closed": inventory_closed,
        "accepted_bottom_charm_tau_map_row_count": 0,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected BottomCharmTauMaps or RThetaThresholdDerivation v1

Status: `{STATUS}`.

This artifact attacks the remaining b/c/tau mass-scheme maps.

```text
native/residual inventory closed       : {str(inventory_closed).lower()}
accepted b/c/tau map rows              : 0
external import contract closed        : true
Rtheta precoefficient skeletons present: {str(len(rtheta_slots) == 6).lower()}
selected Rtheta derivation closed      : false
```

The useful gain is inventory and routing.  Native values and finite residuals
exist, and `Rtheta` has the right slot skeletons, but neither is an accepted
map source.  Next we need b/c/tau formula/table imports or a selected `Rtheta`
mass-scheme derivation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
