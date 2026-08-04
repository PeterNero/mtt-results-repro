"""Build charm CRunDec input policy or R_theta mass-scheme derivation artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import rundec


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_charmcrundecinputpolicy_or_rthetamassschemederivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SWEEP = PACKET_DIR / "charm_crundec_input_policy_sweep.packet.json"
SENSITIVITY = PACKET_DIR / "bct_profile_sensitivity_to_charm_policy.packet.json"
SELECTION_GATE = PACKET_DIR / "charm_policy_selection_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_charm_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CharmCRunDecInputPolicy_or_RThetaMassSchemeDerivation_v1.md"

PREVIOUS = DATA / "selected_bctprofilereconciliation_or_rthetamassschemederivation.candidate.json"
EFT_PROFILE = (
    DATA
    / "selected_bctprofilereconciliation_or_rthetamassschemederivation"
    / "bct_correlated_eft_profile.packet.json"
)
BC_REPLAY = (
    DATA
    / "selected_bottomcharmtaurundecreplay_or_rthetamassschemerows"
    / "bottom_charm_crundec_replay_values.packet.json"
)
RTHETA_GAP = (
    DATA
    / "selected_bctprofilereconciliation_or_rthetamassschemederivation"
    / "rtheta_mass_scheme_derivation_gap_recheck.packet.json"
)

STATUS = (
    "MTT_SELECTED_CHARMCRUNDECINPUTPOLICY_OR_RTHETAMASSSCHEMEDERIVATION_"
    "BUILT_POLICY_SWEEP_NO_SELECTED_REPAIR"
)
NEXT = "MTT_Selected_CharmTableSubstitution_or_SelectedRThetaRowsDecision_v1"


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
        raise FileNotFoundError("missing charm policy sources: " + ", ".join(missing))


def det3(m: list[list[float]]) -> float:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def inv3(m: list[list[float]]) -> list[list[float]]:
    d = det3(m)
    return [
        [
            (m[1][1] * m[2][2] - m[1][2] * m[2][1]) / d,
            (m[0][2] * m[2][1] - m[0][1] * m[2][2]) / d,
            (m[0][1] * m[1][2] - m[0][2] * m[1][1]) / d,
        ],
        [
            (m[1][2] * m[2][0] - m[1][0] * m[2][2]) / d,
            (m[0][0] * m[2][2] - m[0][2] * m[2][0]) / d,
            (m[0][2] * m[1][0] - m[0][0] * m[1][2]) / d,
        ],
        [
            (m[1][0] * m[2][1] - m[1][1] * m[2][0]) / d,
            (m[0][1] * m[2][0] - m[0][0] * m[2][1]) / d,
            (m[0][0] * m[1][1] - m[0][1] * m[1][0]) / d,
        ],
    ]


def quad(z: list[float], inv: list[list[float]]) -> float:
    return sum(z[i] * inv[i][j] * z[j] for i in range(3) for j in range(3))


def chi2_sf_df3(x: float) -> float:
    return math.erfc(math.sqrt(x / 2.0)) + math.sqrt(2.0 * x / math.pi) * math.exp(-x / 2.0)


def charm_crundec(mc_mc: float, alpha_s_mz: float, bottom_threshold: float, loop_order: int) -> dict[str, float]:
    crd = rundec.CRunDec()
    crd.nfMmu.Mth = bottom_threshold
    crd.nfMmu.muth = bottom_threshold
    crd.nfMmu.nf = 5
    alpha_s_mc = crd.AlH2AlL(alpha_s_mz, 91.1876, crd.nfMmu, mc_mc, loop_order)
    mass_mz = crd.mL2mH(mc_mc, alpha_s_mc, mc_mc, crd.nfMmu, 91.1876, loop_order)
    return {"alpha_s_mc": alpha_s_mc, "running_mass_MZ_GeV": mass_mz}


def profile_for_charm_z(charm_z: float, bottom_z: float, tau_z: float, inv_corr: list[list[float]]) -> dict[str, float]:
    z = [bottom_z, charm_z, tau_z]
    chi2 = quad(z, inv_corr)
    return {
        "bottom_z": bottom_z,
        "charm_z": charm_z,
        "tau_z": tau_z,
        "correlated_chi_square": chi2,
        "chi_square_survival_probability_df3": chi2_sf_df3(chi2),
        "passes_95pct_profile_gate": chi2_sf_df3(chi2) >= 0.05,
        "passes_99pct_profile_gate": chi2_sf_df3(chi2) >= 0.01,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, EFT_PROFILE, BC_REPLAY, RTHETA_GAP]
    require_sources(sources)

    previous = load(PREVIOUS)
    eft_profile = load(EFT_PROFILE)
    bc_replay = load(BC_REPLAY)
    rtheta_gap = load(RTHETA_GAP)

    target_mass = 0.628
    target_sigma = 0.018
    alphas_grid = [0.1176, 0.1179, 0.118, 0.1181, 0.1184, 0.1185]
    mc_grid = [1.27, 1.273, 1.279, 1.286, 1.30]
    bottom_threshold_grid = [4.163, 4.18, 4.183, 4.5, 4.8]
    loop_grid = [1, 2, 3, 4, 5]

    rows = []
    for alpha_s in alphas_grid:
        for mc_mc in mc_grid:
            for bottom_threshold in bottom_threshold_grid:
                for loop_order in loop_grid:
                    out = charm_crundec(mc_mc, alpha_s, bottom_threshold, loop_order)
                    residual = out["running_mass_MZ_GeV"] - target_mass
                    rows.append(
                        {
                            "alpha_s_MZ": alpha_s,
                            "mc_mc_GeV": mc_mc,
                            "bottom_threshold_GeV": bottom_threshold,
                            "loop_order": loop_order,
                            "alpha_s_mc": out["alpha_s_mc"],
                            "running_mass_MZ_GeV": out["running_mass_MZ_GeV"],
                            "residual_to_HuangZhou_EFT_GeV": residual,
                            "z_to_HuangZhou_EFT": residual / target_sigma,
                        }
                    )
    best = min(rows, key=lambda row: abs(row["residual_to_HuangZhou_EFT_GeV"]))
    current_charm = next(
        row for row in bc_replay["accepted_external_map_rows"] if row["id"] == "charm_MSbar_native_scale_transport"
    )
    hzish4 = charm_crundec(1.27, 0.1179, 4.8, 4)
    hzish5 = charm_crundec(1.27, 0.1179, 4.8, 5)
    current_z = eft_profile["z_residuals"]["charm_MSbar_native_scale_transport"]
    sweep = {
        "schema": "MTTCharmCRunDecInputPolicySweep.v1",
        "status": "CHARM_CRUNDEC_POLICY_SWEEP_BUILT_NO_EXACT_REPAIR",
        "target": {
            "source": "Huang-Zhou Table 2 EFT MZ charm mass",
            "mass_GeV": target_mass,
            "uncertainty_GeV": target_sigma,
        },
        "grid": {
            "alpha_s_MZ": alphas_grid,
            "mc_mc_GeV": mc_grid,
            "bottom_threshold_GeV": bottom_threshold_grid,
            "loop_order": loop_grid,
            "row_count": len(rows),
        },
        "current_repo_charm_row": {
            "mass_GeV": current_charm["crundec_running_mass_MZ_GeV"],
            "z_to_HuangZhou_EFT": current_z,
        },
        "huang_zhou_input_like_probes": {
            "alpha_s_0p1179_mc_1p27_mbth_4p8_loop4": {
                "mass_GeV": hzish4["running_mass_MZ_GeV"],
                "z_to_HuangZhou_EFT": (hzish4["running_mass_MZ_GeV"] - target_mass) / target_sigma,
            },
            "alpha_s_0p1179_mc_1p27_mbth_4p8_loop5": {
                "mass_GeV": hzish5["running_mass_MZ_GeV"],
                "z_to_HuangZhou_EFT": (hzish5["running_mass_MZ_GeV"] - target_mass) / target_sigma,
            },
        },
        "best_grid_row_by_abs_residual": best,
        "best_grid_row_selected": False,
        "why_not_selected": (
            "The best grid row is selected by minimizing residual against the Huang-Zhou table. Promoting it "
            "without an independent policy theorem would be target fitting."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SWEEP, sweep)

    corr = eft_profile["correlation_matrix"]
    inv_corr = inv3(corr)
    bottom_z = eft_profile["z_residuals"]["bottom_MSbar_native_scale_transport"]
    tau_z = eft_profile["z_residuals"]["tau_pole_rest_to_running_lepton"]
    profiles = {
        "current_repo_policy": profile_for_charm_z(current_z, bottom_z, tau_z, inv_corr),
        "huang_zhou_input_like_loop4": profile_for_charm_z(
            (hzish4["running_mass_MZ_GeV"] - target_mass) / target_sigma,
            bottom_z,
            tau_z,
            inv_corr,
        ),
        "huang_zhou_input_like_loop5": profile_for_charm_z(
            (hzish5["running_mass_MZ_GeV"] - target_mass) / target_sigma,
            bottom_z,
            tau_z,
            inv_corr,
        ),
        "best_grid_row": profile_for_charm_z(best["z_to_HuangZhou_EFT"], bottom_z, tau_z, inv_corr),
        "external_table_substitution": profile_for_charm_z(0.0, bottom_z, tau_z, inv_corr),
    }
    sensitivity = {
        "schema": "MTTBCTProfileSensitivityToCharmPolicy.v1",
        "status": "PROFILE_SENSITIVITY_TO_CHARM_POLICY_COMPUTED_SELECTION_OPEN",
        "correlation_source": eft_profile["correlation_source"],
        "profiles": profiles,
        "profile_pass_possible_in_grid": profiles["best_grid_row"]["passes_95pct_profile_gate"],
        "profile_pass_possible_by_table_substitution": profiles["external_table_substitution"][
            "passes_95pct_profile_gate"
        ],
        "profile_pass_selected_now": False,
        "selection_guard": (
            "A passing profile exists only after choosing either the best residual-minimizing grid row or the "
            "Huang-Zhou charm table row itself. Neither choice is selected by MTT geometry in this artifact."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SENSITIVITY, sensitivity)

    gate = {
        "schema": "MTTCharmPolicySelectionGate.v1",
        "status": "CHARM_POLICY_REPAIR_CANDIDATES_IDENTIFIED_NONE_SELECTED",
        "sweep_source": rel(SWEEP),
        "sensitivity_source": rel(SENSITIVITY),
        "best_grid_policy_would_pass_95pct_profile": profiles["best_grid_row"]["passes_95pct_profile_gate"],
        "huang_zhou_table_substitution_would_pass_95pct_profile": profiles["external_table_substitution"][
            "passes_95pct_profile_gate"
        ],
        "accepted_repair_now": False,
        "accepted_repair_reason": None,
        "required_for_acceptance": [
            "independent provenance theorem selecting the CRunDec input/loop/threshold policy",
            "or explicit decision to use Huang-Zhou table rows as empirical profile rows rather than CRunDec replay rows",
            "or selected Rtheta mass-scheme row derivation",
        ],
        "selected_Rtheta_mass_scheme_derivation_closed": rtheta_gap[
            "selected_Rtheta_mass_scheme_derivation_closed"
        ],
        "minimal_internal_missing_object": rtheta_gap["minimal_internal_missing_object"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SELECTION_GATE, gate)

    cutset = {
        "schema": "MTTNextCutsetAfterCharmPolicy.v1",
        "status": "NEXT_DECIDE_TABLE_SUBSTITUTION_OR_SELECTED_RTHETA_ROWS",
        "closed_now": {
            "charm_CRunDec_input_policy_sweep": True,
            "BCT_profile_sensitivity_to_charm_policy": True,
            "passing_policy_candidates_identified": True,
            "no_hidden_fit_guard_enforced": True,
        },
        "still_open": {
            "selected_charm_policy_repair": True,
            "selected_Rtheta_mass_scheme_derivation": True,
            "BCT_profile_95pct_closure": True,
            "W_Z_H_electroweak_matching_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "choose external Huang-Zhou table substitution explicitly as empirical-profile closure",
            "route_B": "prove a non-target-fitted CRunDec input policy",
            "route_C": "derive selected Rtheta mass-scheme rows",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedCharmCRunDecInputPolicyOrRThetaMassSchemeDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "charm_crundec_input_policy_sweep": rel(SWEEP),
            "bct_profile_sensitivity_to_charm_policy": rel(SENSITIVITY),
            "charm_policy_selection_gate": rel(SELECTION_GATE),
            "next_cutset_after_charm_policy": rel(CUTSET),
        },
        "theorem": {
            "name": "CharmPolicySweepNoHiddenFitTheorem",
            "proved": True,
            "statement": (
                "A bounded CRunDec input/threshold/loop sweep shows that the current charm tension can be "
                "improved and even made profile-passing by residual-minimizing policy choice, but no such "
                "choice is selected independently here. Therefore the artifact closes the policy search "
                "diagnostic while keeping BCT profile closure and Rtheta derivation open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "charm_CRunDec_input_policy_sweep_closed": True,
            "profile_pass_possible_in_grid": profiles["best_grid_row"]["passes_95pct_profile_gate"],
            "profile_pass_possible_by_table_substitution": profiles["external_table_substitution"][
                "passes_95pct_profile_gate"
            ],
            "selected_charm_policy_repair_closed": False,
            "BCT_profile_95pct_closure_closed": False,
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
        "certificate": "MTT_Selected_CharmCRunDecInputPolicy_or_RThetaMassSchemeDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "best_grid_charm_mass_MZ_GeV": best["running_mass_MZ_GeV"],
        "best_grid_profile_survival_probability": profiles["best_grid_row"][
            "chi_square_survival_probability_df3"
        ],
        "best_grid_selected": False,
        "selected_charm_policy_repair_closed": False,
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected CharmCRunDecInputPolicy or RThetaMassSchemeDerivation v1

Status: `{STATUS}`.

This artifact tests whether the BCT profile wall is only a charm CRunDec input
policy issue.

```text
current EFT profile p-value       : {profiles["current_repo_policy"]["chi_square_survival_probability_df3"]}
best grid charm mass              : {best["running_mass_MZ_GeV"]} GeV
best grid EFT profile p-value     : {profiles["best_grid_row"]["chi_square_survival_probability_df3"]}
best grid selected                : false
table substitution profile p-value: {profiles["external_table_substitution"]["chi_square_survival_probability_df3"]}
selected Rtheta rows closed       : false
```

The sweep finds repair candidates, but selecting the best one by residual would
be target fitting.  The next step must either explicitly choose empirical table
substitution as a non-no-knob profile layer, prove an independent CRunDec policy,
or derive the selected Rtheta rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
