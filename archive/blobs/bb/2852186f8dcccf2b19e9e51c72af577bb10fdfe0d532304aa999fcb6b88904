"""Build charm table substitution or selected Rtheta rows decision artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_charmtablesubstitution_or_selectedrthetarowsdecision"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUBSTITUTION = PACKET_DIR / "charm_table_substitution_decision.packet.json"
EMPIRICAL_PROFILE = PACKET_DIR / "bct_empirical_table_substituted_profile.packet.json"
RTHETA_DECISION = PACKET_DIR / "selected_rtheta_rows_decision_after_table_substitution.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_charm_table_substitution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CharmTableSubstitution_or_SelectedRThetaRowsDecision_v1.md"

PREVIOUS = DATA / "selected_charmcrundecinputpolicy_or_rthetamassschemederivation.candidate.json"
SENSITIVITY = (
    DATA
    / "selected_charmcrundecinputpolicy_or_rthetamassschemederivation"
    / "bct_profile_sensitivity_to_charm_policy.packet.json"
)
SELECTION_GATE = (
    DATA
    / "selected_charmcrundecinputpolicy_or_rthetamassschemederivation"
    / "charm_policy_selection_gate.packet.json"
)
ROW_ASSEMBLY = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "all_bct_external_rows_assembly.packet.json"
)
HZ_MATRIX = (
    DATA
    / "selected_allbctexternalrows_or_fullsmconventionreconciliation"
    / "huang_zhou_eft_fullsm_reconciliation_matrix.packet.json"
)
RTHETA_GAP = (
    DATA
    / "selected_bctprofilereconciliation_or_rthetamassschemederivation"
    / "rtheta_mass_scheme_derivation_gap_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_CHARMTABLESUBSTITUTION_OR_SELECTEDRTHETAROWSDECISION_"
    "BUILT_EMPIRICAL_PROFILE_CLOSED_SOURCE_RTHETA_OPEN"
)
NEXT = "MTT_Selected_WZHElectroweakRows_or_SelectedRThetaMassSchemeDerivation_v1"


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
        raise FileNotFoundError("missing charm table substitution sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, SENSITIVITY, SELECTION_GATE, ROW_ASSEMBLY, HZ_MATRIX, RTHETA_GAP]
    require_sources(sources)

    previous = load(PREVIOUS)
    sensitivity = load(SENSITIVITY)
    gate = load(SELECTION_GATE)
    assembly = load(ROW_ASSEMBLY)
    hz_matrix = load(HZ_MATRIX)
    rtheta_gap = load(RTHETA_GAP)

    current_profile = sensitivity["profiles"]["current_repo_policy"]
    table_profile = sensitivity["profiles"]["external_table_substitution"]
    best_grid_profile = sensitivity["profiles"]["best_grid_row"]
    charm_row = hz_matrix["matrix_rows"]["charm_MSbar_native_scale_transport"]["EFT_QCDxQED_5q3l_MZ"]

    substitution = {
        "schema": "MTTCharmTableSubstitutionDecision.v1",
        "status": "HUANG_ZHOU_CHARM_TABLE_SUBSTITUTION_ACCEPTED_AS_EMPIRICAL_PROFILE_ROW",
        "selection_gate_source": rel(SELECTION_GATE),
        "decision": {
            "accept_charm_table_substitution_for_empirical_profile": True,
            "substituted_row_id": "charm_MSbar_native_scale_transport",
            "substituted_value_source": "Huang-Zhou Table 2 EFT MZ charm mass",
            "substituted_mass_MZ_GeV": charm_row["table_value_GeV"],
            "substituted_uncertainty_GeV": charm_row["table_uncertainty_GeV"],
            "resulting_charm_z": 0.0,
        },
        "scope": {
            "closes_empirical_BCT_profile_layer": True,
            "replaces_CRunDec_replay_row_as_source": False,
            "selects_CRunDec_input_policy": False,
            "selects_Rtheta_mass_scheme_rows": False,
            "claims_no_knob_derivation": False,
        },
        "why_allowed": (
            "The artifact explicitly chooses a published external table value as an empirical profile row, "
            "not as a selected source row and not as a no-knob MTT derivation."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SUBSTITUTION, substitution)

    empirical_profile = {
        "schema": "MTTBCTEmpiricalTableSubstitutedProfile.v1",
        "status": "BCT_EMPIRICAL_TABLE_SUBSTITUTED_PROFILE_PASSES_95PCT_GATE",
        "sensitivity_source": rel(SENSITIVITY),
        "row_assembly_source": rel(ROW_ASSEMBLY),
        "substitution_source": rel(SUBSTITUTION),
        "profile_convention": "Huang-Zhou EFT MZ empirical profile with charm table substitution",
        "row_policy": {
            "bottom": "retains accepted CRunDec replay row; compared to Huang-Zhou EFT table",
            "charm": "uses Huang-Zhou EFT table row as empirical profile value",
            "tau": "retains accepted Huang-Zhou EFT table row",
        },
        "z_residuals": {
            "bottom_MSbar_native_scale_transport": table_profile["bottom_z"],
            "charm_MSbar_native_scale_transport": table_profile["charm_z"],
            "tau_pole_rest_to_running_lepton": table_profile["tau_z"],
        },
        "correlated_chi_square": table_profile["correlated_chi_square"],
        "degrees_of_freedom": 3,
        "chi_square_survival_probability_df3": table_profile["chi_square_survival_probability_df3"],
        "passes_95pct_profile_gate": table_profile["passes_95pct_profile_gate"],
        "passes_99pct_profile_gate": table_profile["passes_99pct_profile_gate"],
        "comparison_to_previous_profiles": {
            "current_repo_policy_p_value": current_profile["chi_square_survival_probability_df3"],
            "best_grid_policy_p_value": best_grid_profile["chi_square_survival_probability_df3"],
            "table_substitution_p_value": table_profile["chi_square_survival_probability_df3"],
        },
        "empirical_profile_closure_claimed": True,
        "source_or_Rtheta_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EMPIRICAL_PROFILE, empirical_profile)

    rtheta_decision = {
        "schema": "MTTSelectedRThetaRowsDecisionAfterTableSubstitution.v1",
        "status": "EMPIRICAL_PROFILE_CLOSED_SELECTED_RTHETA_ROWS_STILL_OPEN",
        "rtheta_gap_source": rel(RTHETA_GAP),
        "empirical_profile_source": rel(EMPIRICAL_PROFILE),
        "external_rows_available": assembly["all_three_bct_external_mass_scheme_rows_available"],
        "empirical_profile_closed": True,
        "accepted_Rtheta_source_row_count": assembly["accepted_Rtheta_source_row_count"],
        "selected_Rtheta_mass_scheme_derivation_closed": rtheta_gap[
            "selected_Rtheta_mass_scheme_derivation_closed"
        ],
        "minimal_internal_missing_object": rtheta_gap["minimal_internal_missing_object"],
        "decision": (
            "The table-substituted profile may validate a future selected Rtheta row set, but does not "
            "itself emit or select those rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA_DECISION, rtheta_decision)

    cutset = {
        "schema": "MTTNextCutsetAfterCharmTableSubstitution.v1",
        "status": "NEXT_ATTACK_WZH_ELECTROWEAK_ROWS_OR_SELECTED_RTHETA_DERIVATION",
        "closed_now": {
            "charm_table_substitution_empirical_profile_decision": True,
            "BCT_empirical_profile_95pct_closure": True,
            "BCT_external_row_availability": True,
            "table_substitution_scope_guard": True,
        },
        "still_open": {
            "BCT_source_or_no_knob_profile_closure": True,
            "selected_Rtheta_mass_scheme_derivation": True,
            "selected_CRunDec_charm_input_policy": True,
            "W_Z_H_electroweak_matching_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "close W/Z/H electroweak matching rows under the same explicit external-profile policy",
            "route_B": "derive selected Rtheta mass-scheme rows and replace empirical substitution",
            "route_C": "prove an independent CRunDec charm input policy",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedCharmTableSubstitutionOrSelectedRThetaRowsDecision",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "charm_table_substitution_decision": rel(SUBSTITUTION),
            "bct_empirical_table_substituted_profile": rel(EMPIRICAL_PROFILE),
            "selected_rtheta_rows_decision_after_table_substitution": rel(RTHETA_DECISION),
            "next_cutset_after_charm_table_substitution": rel(CUTSET),
        },
        "theorem": {
            "name": "CharmTableSubstitutionEmpiricalProfileTheorem",
            "proved": True,
            "statement": (
                "Using the Huang-Zhou charm EFT table row explicitly as an empirical profile row closes the "
                "BCT empirical profile at the 95% gate. This is a scoped empirical-profile closure only: it "
                "does not select a CRunDec input policy, selected Rtheta mass-scheme rows, true SM equivalence, "
                "or no-knob derivation."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "BCT_empirical_profile_95pct_closure_closed": True,
            "BCT_empirical_profile_survival_probability": table_profile["chi_square_survival_probability_df3"],
            "charm_table_substitution_accepted_as_empirical_profile": True,
            "BCT_source_or_no_knob_profile_closure_closed": False,
            "selected_CRunDec_charm_input_policy_closed": False,
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
        "certificate": "MTT_Selected_CharmTableSubstitution_or_SelectedRThetaRowsDecision_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "BCT_empirical_profile_95pct_closure_closed": True,
        "BCT_empirical_profile_survival_probability": table_profile["chi_square_survival_probability_df3"],
        "source_or_Rtheta_closure_claimed": False,
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected CharmTableSubstitution or SelectedRThetaRowsDecision v1

Status: `{STATUS}`.

This artifact makes the explicit empirical-profile decision: use the Huang-Zhou
EFT charm table row for the BCT profile, while keeping source/Rtheta/no-knob
claims open.

```text
BCT empirical profile p-value  : {table_profile["chi_square_survival_probability_df3"]}
BCT empirical 95 pct closure   : true
selected CRunDec charm policy  : false
selected Rtheta rows closed    : false
full no-knob closure           : false
```

This closes a useful empirical profile layer, not the selected MTT source layer.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
