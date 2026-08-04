"""Audit strict finite-H source-row construction or non-Higgs HRG prediction bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictfinitehsourcerowconstruction_or_nonhiggshrgprediction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FINITE_H_RECONCILIATION = PACKET_DIR / "finite_h_source_reconciliation.packet.json"
NONHIGGS_HRG_GATE = PACKET_DIR / "nonhiggs_hrg_prediction_gate.packet.json"
PEW_PREFACTOR_GATE = PACKET_DIR / "pew_prefactor_remaining_gate.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_strict_finite_h_reconciliation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictFiniteHSourceRowConstruction_or_NonHiggsHRGPrediction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_STRICTFINITEHSOURCEROWCONSTRUCTION_OR_NONHIGGSHRGPREDICTION_"
    "FINITE_H_RADIAL_SOURCE_CLOSED_PEW_PREFACTOR_AND_NONHIGGS_HRG_OPEN"
)
NEXT = "MTT_Selected_StrictPEWSourceTheorem_or_SMPrecisionClosureCutset_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    finite_h = load(FINITE_H_RECONCILIATION)
    nonhiggs = load(NONHIGGS_HRG_GATE)
    pew = load(PEW_PREFACTOR_GATE)
    next_cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("finite_h", finite_h),
        ("nonhiggs", nonhiggs),
        ("pew", pew),
        ("next", next_cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_cutset["next_required_artifact"] == NEXT, "next cutset next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")

    require(data["strict_finite_H_radial_source_closed"] is True, "finite H source not closed")
    require(data["minimal_one_prefactor_lane_closed"] is True, "minimal prefactor lane")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    finite = finite_h["finite_projected_H_source"]
    require(finite_h["finite_H_radial_source_closed"] is True, "finite packet closure")
    require(finite["A_N_exactness_available"] is True, "A_N exactness")
    require(finite["H_scalar_functional_on_A_N_closed"] is True, "H scalar")
    require(finite["accepted_H_scalar_source_rows"] == 1, "H scalar rows")
    require(finite["strict_tau_H_promoted"] is True, "tau_H")
    require(finite["strict_r_H_promoted"] is True, "r_H")
    require(finite["selected_R_H_RG_source_emitted"] is True, "R_H_RG")
    require(finite["H_parameter_count_after_replacement"] == 0, "H parameter count")

    old = finite_h["old_one_parameter_radial_lane"]
    require(old["previously_available"] is True, "old lane available")
    require(old["previous_H_parameter_count"] == 1, "old parameter count")
    require(old["retired_for_radial_source"] is True, "old lane retired")

    require(nonhiggs["accepted_nonHiggs_HRG_source_map_count"] == 0, "non-Higgs maps")
    require(nonhiggs["nonHiggs_HRG_source_map_emitted"] is False, "non-Higgs overemitted")
    require(nonhiggs["strict_R_H_RG_source_emitted"] is False, "HRG strict source overemitted")
    require(nonhiggs["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "HRG universal overadmitted")
    require(nonhiggs["hrg_universal_crossuse_credit_open"] is True, "HRG gate")

    require(pew["strict_prefactor_source_open"] is True, "PEW strict gate")
    require(pew["minimal_one_prefactor_lane_closed"] is True, "PEW minimal lane")
    require(pew["H_specific_parameter_count"] == 0, "PEW H count")
    require(pew["P_EW_counted_as_shared_physical_primitive"] is True, "P_EW primitive")
    require(pew["P_EW_parameter_count"] == 1, "P_EW count")
    require(pew["lambda_H_used_as_selector"] is False, "lambda selector")
    require(pew["selected_A_EW_source_emitted"] is False, "A_EW overemitted")
    require(pew["strict_K_threshold_Omega_H_lambda_emitted"] is False, "direct K overemitted")

    decision = data["closure_decision"]
    require(decision["old_H_one_parameter_lane_retired_for_radial_source"] is True, "decision old lane")
    require(decision["strict_finite_H_radial_source_closed"] is True, "decision finite H")
    require(decision["accepted_H_scalar_source_rows"] == 1, "decision H rows")
    require(decision["selected_R_H_RG_source_emitted"] is True, "decision R_H_RG")
    require(decision["H_specific_parameter_count_after_finite_H"] == 0, "decision H count")
    require(decision["minimal_one_prefactor_lane_closed"] is True, "decision minimal prefactor")
    require(decision["P_EW_parameter_count"] == 1, "decision P_EW count")
    require(decision["accepted_strict_prefactor_source_row_total"] == 0, "decision strict prefactor rows")
    require(decision["strict_P_EW_source_promoted"] is False, "decision P_EW overpromoted")
    require(decision["direct_K_threshold_Omega_H_lambda_emitted"] is False, "decision direct K")
    require(decision["accepted_nonHiggs_HRG_source_map_count"] == 0, "decision HRG count")
    require(decision["nonHiggs_HRG_source_map_emitted"] is False, "decision HRG map")
    require(decision["minimal_parameter_ledger_closed"] is True, "minimal ledger")
    require(decision["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "non-neutrino count")
    require(
        decision["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24,
        "PMNS count",
    )
    require(decision["full_no_knob_closed"] is False, "decision no-knob")
    require(decision["true_SM_equivalence_closed"] is False, "decision true SM")

    require(
        any("strict finite H radial source construction marked closed" in item for item in next_cutset["closed_here"]),
        "cutset closed",
    )
    require("strict same-branch P_EW gauge/action source row" in next_cutset["still_open"], "cutset PEW")
    require("accepted non-Higgs HRG prediction/source map" in next_cutset["still_open"], "cutset HRG")

    for phrase in [
        "StrictFiniteHSourceRowConstructionOrNonHiggsHRGPredictionTheorem",
        "old H radial one-parameter lane retired: `true`",
        "strict finite H radial source closed: `true`",
        "H-specific parameter count after finite H: `0`",
        "strict `P_EW` source rows accepted: `0`",
        "accepted non-Higgs HRG source maps: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: strict finite-H radial source is reconciled as closed; "
        "strict PEW/direct-K and non-Higgs HRG source maps remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
