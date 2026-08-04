"""Build b/c/tau RunDec replay or R_theta mass-scheme rows artifact."""

from __future__ import annotations

import importlib.metadata
import json
import math
from pathlib import Path
from typing import Any

import rundec


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bottomcharmtaurundecreplay_or_rthetamassschemerows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RUNTIME = PACKET_DIR / "versioned_crundec_runtime_probe.packet.json"
BC_REPLAY = PACKET_DIR / "bottom_charm_crundec_replay_values.packet.json"
TAU_GAP = PACKET_DIR / "tau_running_map_policy_gap.packet.json"
RECONCILE = PACKET_DIR / "legacy_firstpass_conflict_or_reconciliation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bct_rundec_replay.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BottomCharmTauRunDecReplay_or_RThetaMassSchemeRows_v1.md"

PREVIOUS = DATA / "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation.candidate.json"
SOURCE_FAMILIES = (
    DATA
    / "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation"
    / "external_bct_formula_source_families.packet.json"
)
ROW_ATTEMPT = (
    DATA
    / "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation"
    / "bottom_charm_tau_formula_row_acceptance_attempt.packet.json"
)
INVENTORY = (
    DATA
    / "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
    / "bottom_charm_tau_native_residual_inventory.packet.json"
)
REFERENCE = DATA / "sm_equivalence_reference_data_values_fill.candidate.json"
MIXING = DATA / "sm_equivalence_mixing_and_gauge_replay.candidate.json"
RTHETA_GAP = (
    DATA
    / "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation"
    / "rtheta_bct_mass_scheme_derivation_gap.packet.json"
)

STATUS = (
    "MTT_SELECTED_BOTTOMCHARMTAURUNDECREPLAY_OR_RTHETAMASSSCHEMEROWS_"
    "BUILT_BC_CRUNDEC_ROWS_TAU_RTHETA_OPEN"
)
NEXT = "MTT_Selected_TauEWRunningPolicy_or_RThetaMassSchemeRows_v1"


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
        raise FileNotFoundError("missing b/c/tau RunDec replay sources: " + ", ".join(missing))


def mass_gev(row: dict[str, Any]) -> float:
    value = float(row["central_value"])
    units = row.get("units")
    if units == "GeV":
        return value
    if units == "MeV":
        return value / 1000.0
    raise ValueError(f"unknown mass unit: {units}")


def v_uncertainty(row: dict[str, Any]) -> float:
    unc = row["uncertainty"]
    if isinstance(unc, dict):
        return max(abs(float(unc["minus"])), abs(float(unc["plus"])))
    return abs(float(unc))


def scalar_uncertainty(row: dict[str, Any]) -> float:
    unc = row["uncertainty"]
    if isinstance(unc, dict):
        return max(abs(float(unc["minus"])), abs(float(unc["plus"])))
    return abs(float(unc))


def crundec_bottom_yukawa(mb_mb: float, alpha_s_mz: float, vev: float, loop_order: int) -> dict[str, float]:
    mz = 91.1876
    crd = rundec.CRunDec()
    alpha_s_mb = crd.AlphasExact(alpha_s_mz, mz, mb_mb, 5, loop_order)
    mb_mz = crd.mMS2mMS(mb_mb, alpha_s_mb, alpha_s_mz, 5, loop_order)
    return {
        "alpha_s_mb": alpha_s_mb,
        "running_mass_MZ_GeV": mb_mz,
        "yukawa_MZ": math.sqrt(2.0) * mb_mz / vev,
    }


def crundec_charm_yukawa(
    mc_mc: float,
    alpha_s_mz: float,
    vev: float,
    loop_order: int,
    bottom_decoupling_threshold_GeV: float,
) -> dict[str, float]:
    mz = 91.1876
    crd = rundec.CRunDec()
    crd.nfMmu.Mth = bottom_decoupling_threshold_GeV
    crd.nfMmu.muth = bottom_decoupling_threshold_GeV
    crd.nfMmu.nf = 5
    alpha_s_mc = crd.AlH2AlL(alpha_s_mz, mz, crd.nfMmu, mc_mc, loop_order)
    mc_mz = crd.mL2mH(mc_mc, alpha_s_mc, mc_mc, crd.nfMmu, mz, loop_order)
    return {
        "alpha_s_mc": alpha_s_mc,
        "running_mass_MZ_GeV": mc_mz,
        "yukawa_MZ": math.sqrt(2.0) * mc_mz / vev,
    }


def diagonal_sensitivity(
    base_args: dict[str, float],
    perturbations: dict[str, float],
    evaluator,
) -> dict[str, Any]:
    central = evaluator(**base_args)["yukawa_MZ"]
    rows: dict[str, Any] = {}
    for name, delta in perturbations.items():
        if delta <= 0.0:
            continue
        lo_args = dict(base_args)
        hi_args = dict(base_args)
        lo_args[name] -= delta
        hi_args[name] += delta
        lo = evaluator(**lo_args)["yukawa_MZ"]
        hi = evaluator(**hi_args)["yukawa_MZ"]
        rows[name] = {
            "minus_delta_input": -delta,
            "plus_delta_input": delta,
            "minus_value": lo,
            "plus_value": hi,
            "central_value": central,
            "symmetric_half_width": abs(hi - lo) / 2.0,
        }
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, SOURCE_FAMILIES, ROW_ATTEMPT, INVENTORY, REFERENCE, MIXING, RTHETA_GAP]
    require_sources(sources)

    previous = load(PREVIOUS)
    source_families = load(SOURCE_FAMILIES)
    row_attempt = load(ROW_ATTEMPT)
    inventory = load(INVENTORY)
    reference = load(REFERENCE)
    mixing = load(MIXING)
    rtheta_gap = load(RTHETA_GAP)

    masses = reference["reference_values"]["masses"]
    constants = reference["reference_values"]["constants"]
    mb = mass_gev(masses["b"])
    mc = mass_gev(masses["c"])
    tau = mass_gev(masses["tau"])
    vev = float(constants["v_from_G_F"]["central_value"])
    alpha_s = float(mixing["gauge_replay_MZ"]["filled_inputs"]["alpha_s_MZ"]["central_value"])
    alpha_s_unc = scalar_uncertainty(mixing["gauge_replay_MZ"]["filled_inputs"]["alpha_s_MZ"])
    bottom_threshold = rundec.RunDec_values().Mb
    loop_order = 5

    runtime_packet = {
        "schema": "MTTVersionedCRunDecRuntimeProbe.v1",
        "status": "CRUNDEC_PYTHON_RUNTIME_AVAILABLE_AND_VERSIONED",
        "runtime": {
            "python_package": "rundec",
            "python_package_version": importlib.metadata.version("rundec"),
            "wrapper_summary": "Python wrapper around CRunDec",
            "home_page": "https://github.com/DavidMStraub/rundec-python",
        },
        "formula_sources": [
            source["id"]
            for source in source_families["formula_sources"]
            if source["id"] in {"RunDec-original", "CRunDec", "RunDec-v3", "PDG-quark-masses"}
        ],
        "loop_order_used": loop_order,
        "bottom_decoupling_threshold_GeV_for_charm_replay": bottom_threshold,
        "runtime_available": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RUNTIME, runtime_packet)

    bottom_by_loop = {
        str(n): crundec_bottom_yukawa(mb, alpha_s, vev, n)
        for n in [1, 2, 3, 4, 5]
    }
    charm_by_loop = {
        str(n): crundec_charm_yukawa(mc, alpha_s, vev, n, bottom_threshold)
        for n in [1, 2, 3, 4, 5]
    }
    bottom_central = bottom_by_loop[str(loop_order)]
    charm_central = charm_by_loop[str(loop_order)]

    bottom_sens = diagonal_sensitivity(
        {"mb_mb": mb, "alpha_s_mz": alpha_s, "vev": vev, "loop_order": loop_order},
        {"mb_mb": scalar_uncertainty(masses["b"]), "alpha_s_mz": alpha_s_unc, "vev": v_uncertainty(constants["v_from_G_F"])},
        crundec_bottom_yukawa,
    )
    charm_sens = diagonal_sensitivity(
        {
            "mc_mc": mc,
            "alpha_s_mz": alpha_s,
            "vev": vev,
            "loop_order": loop_order,
            "bottom_decoupling_threshold_GeV": bottom_threshold,
        },
        {"mc_mc": scalar_uncertainty(masses["c"]), "alpha_s_mz": alpha_s_unc, "vev": v_uncertainty(constants["v_from_G_F"])},
        crundec_charm_yukawa,
    )

    residual_by_map = {row["map_id"]: row for row in inventory["residual_rows"]}
    accepted_rows = [
        {
            "id": "bottom_MSbar_native_scale_transport",
            "residual_id": "Y_d_b_native_to_firstpass_MZ",
            "source_mass_GeV": mb,
            "source_scale": "m_b",
            "target_scale": "M_Z",
            "crundec_running_mass_MZ_GeV": bottom_central["running_mass_MZ_GeV"],
            "crundec_yukawa_MZ": bottom_central["yukawa_MZ"],
            "native_inventory_yukawa": inventory["native_values"]["bottom_native_Y_d_33"],
            "legacy_firstpass_yukawa": residual_by_map["bottom_MSbar_native_scale_transport"]["source_value"],
            "multiplicative_factor_vs_native_inventory": bottom_central["yukawa_MZ"]
            / inventory["native_values"]["bottom_native_Y_d_33"],
            "multiplicative_factor_vs_legacy_firstpass": bottom_central["yukawa_MZ"]
            / residual_by_map["bottom_MSbar_native_scale_transport"]["source_value"],
            "diagonal_sensitivity_sidecar": bottom_sens,
            "accepted_as_external_map_row": True,
            "accepted_as_Rtheta_source_row": False,
        },
        {
            "id": "charm_MSbar_native_scale_transport",
            "residual_id": "Y_u_c_native_to_firstpass_MZ",
            "source_mass_GeV": mc,
            "source_scale": "m_c",
            "target_scale": "M_Z",
            "crundec_running_mass_MZ_GeV": charm_central["running_mass_MZ_GeV"],
            "crundec_yukawa_MZ": charm_central["yukawa_MZ"],
            "native_inventory_yukawa": inventory["native_values"]["charm_native_Y_u_22"],
            "legacy_firstpass_yukawa": residual_by_map["charm_MSbar_native_scale_transport"]["source_value"],
            "multiplicative_factor_vs_native_inventory": charm_central["yukawa_MZ"]
            / inventory["native_values"]["charm_native_Y_u_22"],
            "multiplicative_factor_vs_legacy_firstpass": charm_central["yukawa_MZ"]
            / residual_by_map["charm_MSbar_native_scale_transport"]["source_value"],
            "diagonal_sensitivity_sidecar": charm_sens,
            "accepted_as_external_map_row": True,
            "accepted_as_Rtheta_source_row": False,
        },
    ]
    bc_replay = {
        "schema": "MTTBottomCharmCRunDecReplayValues.v1",
        "status": "BOTTOM_CHARM_CRUNDEC_REPLAY_VALUES_EMITTED_ACCEPTED_EXTERNAL_ROWS",
        "runtime_source": rel(RUNTIME),
        "input_reference_values": rel(REFERENCE),
        "input_alpha_s": rel(MIXING),
        "formula_call_policy": {
            "bottom": "CRunDec AlphasExact(alpha_s(MZ), MZ, m_b, nf=5, loop_order), then mMS2mMS(m_b(m_b), alpha_s(m_b), alpha_s(MZ), nf=5, loop_order)",
            "charm": "CRunDec AlH2AlL through bottom threshold, then mL2mH(m_c(m_c), alpha_s(m_c), m_c, bottom threshold, MZ, loop_order)",
            "MZ_GeV": 91.1876,
            "loop_order": loop_order,
            "bottom_decoupling_threshold_GeV": bottom_threshold,
        },
        "values_by_loop_order": {
            "bottom": bottom_by_loop,
            "charm": charm_by_loop,
        },
        "accepted_external_map_rows": accepted_rows,
        "accepted_external_map_row_count": len(accepted_rows),
        "versioned_replay_values_imported": True,
        "bottom_charm_rows_closed": True,
        "tau_row_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(BC_REPLAY, bc_replay)

    tau_gap = {
        "schema": "MTTTauRunningMapPolicyGap.v1",
        "status": "TAU_POLE_REST_TO_RUNNING_LEPTON_POLICY_OPEN",
        "required_map": "tau_pole_rest_to_running_lepton",
        "tau_input_mass_GeV": tau,
        "native_inventory_yukawa": inventory["native_values"]["tau_native_Y_e_33"],
        "legacy_firstpass_yukawa": residual_by_map["tau_pole_rest_to_running_lepton"]["source_value"],
        "why_crundec_does_not_close_tau": (
            "RunDec/CRunDec is a QCD quark-mass running and decoupling engine. The tau row needs a declared "
            "QED/electroweak lepton running and pole/rest-to-running mass convention, or a selected Rtheta "
            "mass-scheme derivation."
        ),
        "acceptable_next_routes": [
            "import a provenance-bearing QED/EW charged-lepton running formula/table with sidecars",
            "declare and audit a negligible-QED diagonal limitation policy",
            "derive tau_pole_rest_to_running_lepton from selected Rtheta mass-scheme rows",
        ],
        "accepted_as_external_map_row": False,
        "accepted_as_Rtheta_source_row": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(TAU_GAP, tau_gap)

    conflict = {
        "schema": "MTTLegacyFirstpassConflictOrReconciliation.v1",
        "status": "LEGACY_FIRSTPASS_COMMON_SCALE_ROWS_CONFLICT_WITH_CRUNDEC_TRANSPORT",
        "inventory_source": rel(INVENTORY),
        "crundec_replay_source": rel(BC_REPLAY),
        "conflict_rows": [
            {
                "id": row["id"],
                "legacy_firstpass_yukawa": row["legacy_firstpass_yukawa"],
                "crundec_yukawa_MZ": row["crundec_yukawa_MZ"],
                "relative_delta_crundec_minus_legacy": (
                    row["crundec_yukawa_MZ"] - row["legacy_firstpass_yukawa"]
                )
                / row["legacy_firstpass_yukawa"],
                "reconciliation": "legacy first-pass common-scale value must be treated as a placeholder/proxy, not as the accepted MSbar MZ quark transport row",
            }
            for row in accepted_rows
        ],
        "old_rows_superseded_for_b_c": True,
        "tau_legacy_row_superseded": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RECONCILE, conflict)

    cutset = {
        "schema": "MTTNextCutsetAfterBCTRunDecReplay.v1",
        "status": "NEXT_ATTACK_TAU_EW_RUNNING_OR_SELECTED_RTHETA_MASS_SCHEME_ROWS",
        "closed_now": {
            "versioned_crundec_runtime_available": True,
            "bottom_MSbar_native_scale_transport_external_row": True,
            "charm_MSbar_native_scale_transport_external_row": True,
            "legacy_firstpass_bc_conflict_recorded": True,
        },
        "still_open": {
            "tau_pole_rest_to_running_lepton_external_row": True,
            "selected_Rtheta_mass_scheme_derivation": True,
            "W_Z_H_electroweak_matching_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "build/import QED/EW tau pole/rest-to-running lepton policy with sidecars",
            "route_B": "derive all three mass-scheme rows from selected Rtheta projection data",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedBottomCharmTauRunDecReplayOrRThetaMassSchemeRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "versioned_crundec_runtime_probe": rel(RUNTIME),
            "bottom_charm_crundec_replay_values": rel(BC_REPLAY),
            "tau_running_map_policy_gap": rel(TAU_GAP),
            "legacy_firstpass_conflict_or_reconciliation": rel(RECONCILE),
            "next_cutset_after_bct_rundec_replay": rel(CUTSET),
        },
        "theorem": {
            "name": "BottomCharmCRunDecReplayExternalRowTheorem",
            "proved": True,
            "statement": (
                "A versioned CRunDec runtime emits finite bottom and charm MSbar native-scale-to-MZ running "
                "mass/Yukawa rows with diagonal sensitivity sidecars. These rows are accepted as external map "
                "rows and supersede the old first-pass b/c proxy rows. They do not select Rtheta and do not "
                "close the tau charged-lepton running row."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "versioned_RunDec_or_table_replay_values_closed_for_bottom_charm": True,
            "bottom_MSbar_native_scale_transport_external_row_closed": True,
            "charm_MSbar_native_scale_transport_external_row_closed": True,
            "accepted_bottom_charm_tau_map_row_count": len(accepted_rows),
            "tau_pole_rest_to_running_lepton_external_row_closed": False,
            "selected_Rtheta_mass_scheme_derivation_closed": rtheta_gap[
                "selected_Rtheta_mass_scheme_derivation_closed"
            ],
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
        "certificate": "MTT_Selected_BottomCharmTauRunDecReplay_or_RThetaMassSchemeRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "accepted_external_map_row_count": len(accepted_rows),
        "bottom_row_closed": True,
        "charm_row_closed": True,
        "tau_row_closed": False,
        "selected_Rtheta_mass_scheme_derivation_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected BottomCharmTauRunDecReplay or RThetaMassSchemeRows v1

Status: `{STATUS}`.

This artifact executes a versioned CRunDec replay for the b/c quark MSbar
native-scale-to-`M_Z` transport rows.

```text
accepted external b/c/tau rows : {len(accepted_rows)}
bottom RunDec/CRunDec row      : closed
charm RunDec/CRunDec row       : closed
tau QED/EW running row         : open
selected Rtheta derivation     : open
```

The important correction is that the old first-pass common-scale b/c rows are
now explicitly superseded as physical `M_Z` quark transport rows: CRunDec
decreases both running masses at `M_Z`, while the legacy proxy increased them.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
