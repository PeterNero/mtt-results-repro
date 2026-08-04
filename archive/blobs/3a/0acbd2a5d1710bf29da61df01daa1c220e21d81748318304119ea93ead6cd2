"""Audit b/c/tau RunDec replay or R_theta mass-scheme rows artifact."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bottomcharmtaurundecreplay_or_rthetamassschemerows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RUNTIME = PACKET_DIR / "versioned_crundec_runtime_probe.packet.json"
BC_REPLAY = PACKET_DIR / "bottom_charm_crundec_replay_values.packet.json"
TAU_GAP = PACKET_DIR / "tau_running_map_policy_gap.packet.json"
RECONCILE = PACKET_DIR / "legacy_firstpass_conflict_or_reconciliation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bct_rundec_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BottomCharmTauRunDecReplay_or_RThetaMassSchemeRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
REQUIREMENTS = ROOT / "requirements.txt"

STATUS = (
    "MTT_SELECTED_BOTTOMCHARMTAURUNDECREPLAY_OR_RTHETAMASSSCHEMEROWS_"
    "BUILT_BC_CRUNDEC_ROWS_TAU_RTHETA_OPEN"
)
NEXT = "MTT_Selected_TauEWRunningPolicy_or_RThetaMassSchemeRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(actual: float, expected: float, tol: float = 1e-15) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def require_sidecars(row: dict) -> None:
    sidecars = row["diagonal_sensitivity_sidecar"]
    require(set(sidecars) >= {"alpha_s_mz", "vev"}, f"sidecars missing common inputs for {row['id']}")
    mass_key = "mb_mb" if row["id"].startswith("bottom") else "mc_mc"
    require(mass_key in sidecars, f"sidecar missing mass key for {row['id']}")
    for key, sidecar in sidecars.items():
        for field in ["minus_value", "plus_value", "central_value", "symmetric_half_width"]:
            require(math.isfinite(float(sidecar[field])), f"nonfinite sidecar {row['id']} {key} {field}")
        require(float(sidecar["symmetric_half_width"]) >= 0.0, f"negative sidecar width {row['id']} {key}")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    runtime = load(RUNTIME)
    bc = load(BC_REPLAY)
    tau = load(TAU_GAP)
    reconcile = load(RECONCILE)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")
    reqs = REQUIREMENTS.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")
        require(cert[key] is False, f"certificate guardrail overclaimed: {key}")

    require("rundec==0.7" in reqs, "requirements do not pin rundec")
    require(runtime["status"] == "CRUNDEC_PYTHON_RUNTIME_AVAILABLE_AND_VERSIONED", "runtime status mismatch")
    require(runtime["runtime"]["python_package"] == "rundec", "runtime package mismatch")
    require(runtime["runtime"]["python_package_version"] == "0.7", "runtime version mismatch")
    require(runtime["runtime_available"] is True, "runtime unavailable")
    require(runtime["loop_order_used"] == 5, "wrong loop order")
    require(runtime["bottom_decoupling_threshold_GeV_for_charm_replay"] == 4.8, "wrong b threshold")
    require(runtime["closure_claimed"] is True, "runtime should close locally")

    require(
        bc["status"] == "BOTTOM_CHARM_CRUNDEC_REPLAY_VALUES_EMITTED_ACCEPTED_EXTERNAL_ROWS",
        "b/c replay status mismatch",
    )
    require(bc["accepted_external_map_row_count"] == 2, "wrong accepted b/c row count")
    require(bc["versioned_replay_values_imported"] is True, "replay values not imported")
    require(bc["bottom_charm_rows_closed"] is True, "b/c rows not closed")
    require(bc["tau_row_closed"] is False, "tau closed by CRunDec")
    require(bc["closure_claimed"] is True, "b/c replay should close locally")
    rows = {row["id"]: row for row in bc["accepted_external_map_rows"]}
    require(set(rows) == {"bottom_MSbar_native_scale_transport", "charm_MSbar_native_scale_transport"}, "wrong accepted row ids")
    require(close(rows["bottom_MSbar_native_scale_transport"]["crundec_running_mass_MZ_GeV"], 2.8653031219496135), "bottom mass changed")
    require(close(rows["bottom_MSbar_native_scale_transport"]["crundec_yukawa_MZ"], 0.016457462659897754), "bottom yukawa changed")
    require(close(rows["charm_MSbar_native_scale_transport"]["crundec_running_mass_MZ_GeV"], 0.6792260486838773), "charm mass changed")
    require(close(rows["charm_MSbar_native_scale_transport"]["crundec_yukawa_MZ"], 0.0039012756619756254), "charm yukawa changed")
    for row in rows.values():
        require(row["accepted_as_external_map_row"] is True, f"row not accepted external: {row['id']}")
        require(row["accepted_as_Rtheta_source_row"] is False, f"row accepted as Rtheta: {row['id']}")
        require(row["multiplicative_factor_vs_legacy_firstpass"] < 1.0, f"legacy relation unexpected: {row['id']}")
        require_sidecars(row)

    require(tau["status"] == "TAU_POLE_REST_TO_RUNNING_LEPTON_POLICY_OPEN", "tau status mismatch")
    require(tau["accepted_as_external_map_row"] is False, "tau overaccepted external")
    require(tau["accepted_as_Rtheta_source_row"] is False, "tau overaccepted Rtheta")
    require(tau["closure_claimed"] is False, "tau overclosed")
    require("RunDec/CRunDec is a QCD quark-mass" in tau["why_crundec_does_not_close_tau"], "tau reason missing")

    require(
        reconcile["status"] == "LEGACY_FIRSTPASS_COMMON_SCALE_ROWS_CONFLICT_WITH_CRUNDEC_TRANSPORT",
        "reconciliation status mismatch",
    )
    require(reconcile["old_rows_superseded_for_b_c"] is True, "old b/c rows not superseded")
    require(reconcile["tau_legacy_row_superseded"] is False, "tau legacy row superseded too early")
    require(len(reconcile["conflict_rows"]) == 2, "wrong conflict row count")
    for row in reconcile["conflict_rows"]:
        require(row["relative_delta_crundec_minus_legacy"] < 0.0, f"conflict direction wrong: {row['id']}")
    require(reconcile["closure_claimed"] is True, "reconciliation should close locally")

    require(cutset["status"] == "NEXT_ATTACK_TAU_EW_RUNNING_OR_SELECTED_RTHETA_MASS_SCHEME_ROWS", "cutset status mismatch")
    for key in [
        "versioned_crundec_runtime_available",
        "bottom_MSbar_native_scale_transport_external_row",
        "charm_MSbar_native_scale_transport_external_row",
        "legacy_firstpass_bc_conflict_recorded",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "tau_pole_rest_to_running_lepton_external_row",
        "selected_Rtheta_mass_scheme_derivation",
        "W_Z_H_electroweak_matching_rows",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["versioned_RunDec_or_table_replay_values_closed_for_bottom_charm"] is True, "b/c replay not closed")
    require(closure["bottom_MSbar_native_scale_transport_external_row_closed"] is True, "bottom row not closed")
    require(closure["charm_MSbar_native_scale_transport_external_row_closed"] is True, "charm row not closed")
    require(closure["accepted_bottom_charm_tau_map_row_count"] == 2, "candidate accepted count mismatch")
    for key in [
        "tau_pole_rest_to_running_lepton_external_row_closed",
        "selected_Rtheta_mass_scheme_derivation_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")

    require("accepted external b/c/tau rows : 2" in note, "note missing accepted count")
    require("tau QED/EW running row         : open" in note, "note missing tau open line")
    require(NEXT in note, "note missing next artifact")
    print(json.dumps({"audit": SLUG, "status": "ok"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
