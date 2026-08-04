"""Audit Step67 theta-overlap anchor / exponent-prefactor frontier."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EXTERNAL_PACKET = PACKET_DIR / "step67_external_inspiration_not_proof.packet.json"
ANCHOR_PACKET = PACKET_DIR / "step67_theta_overlap_suppression_anchor.packet.json"
TRIAL_PACKET = PACKET_DIR / "step67_exponent_lattice_diagnostic_trials.packet.json"
MISSING_PACKET = PACKET_DIR / "step67_next_exponent_prefactor_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step67_ThetaOverlapAnchor_or_ExponentPrefactorFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP67_THETA_OVERLAP_ANCHOR_CLOSED_EXPONENT_PREFACTOR_FRONTIER_OPEN"
NEXT = "MTT_Selected_ThetaOverlapExponentTheorem_or_HYMThresholdPrefactorRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    external = load(EXTERNAL_PACKET)
    anchor = load(ANCHOR_PACKET)
    trial = load(TRIAL_PACKET)
    missing = load(MISSING_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")

    for item in [data, external, anchor, trial, missing, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(external["used_as_proof"] is False, "external source overpromoted as proof")
    require(external["used_as_selector"] is False, "external source overpromoted as selector")
    require(len(external["external_sources"]) >= 4, "external inspiration ledger too small")

    require(anchor["epsilon_theta_closed_as_source_overlap_anchor"] is True, "epsilon anchor not closed")
    require(anchor["selected_transition_generator"] == "g4", "transition generator mismatch")
    require(abs(anchor["selected_transition_factor_at_origin"] - math.exp(-4 * math.pi)) < 1e-18, "transition factor mismatch")
    require(abs(anchor["epsilon_theta"] - math.exp(-2 * math.pi)) < 1e-18, "epsilon mismatch")
    require(anchor["epsilon_theta_exact"] == "exp(-2*pi)", "epsilon exact label mismatch")
    require(anchor["alpha1_source_anchor_available"] is True, "alpha1 source anchor missing")
    require(anchor["alpha1_value_closure_anchor"] is False, "alpha1 overaccepted as value anchor")
    require(anchor["rtheta_alpha1_map_constructed"] is True, "Rtheta alpha1 map not imported")
    require(anchor["family_resolving_operator_closed"] is True, "family operator not imported")

    require(trial["trial_count"] == 3, "trial count mismatch")
    require(trial["postcheck_values_used_as_selectors"] is False, "postcheck values used as selectors")
    require(trial["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")
    require(trial["accepted_exponent_lattice_theorem"] is False, "exponent theorem overaccepted")
    require(trial["accepted_HYM_threshold_prefactor_rows"] is False, "prefactors overaccepted")
    require(trial["smallest_postcheck_span_model"] in {
        "integer_all",
        "shared_circle_half_d_e",
        "qutrit_third_d_e",
    }, "unexpected smallest-span model")
    for model in trial["trials"]:
        require(model["accepted_as_selected_exponent_theorem"] is False, "trial overaccepted")
        for row in model["rows"]:
            require(row["accepted_as_selected_value"] is False, "trial row overaccepted")

    require(NEXT == missing["next_required_artifact"], "missing packet next mismatch")
    for phrase in [
        "selected theorem assigning charged-sector exponent lattice before postcheck",
        "selected HYM/threshold prefactor rows for u,d,e generations",
        "selected lambda_H exponent/prefactor row",
        "selected threshold response functional instantiation",
        "mass-scheme/profile convention at internal no-knob tier",
    ]:
        require(phrase in missing["still_missing"], f"missing object not listed: {phrase}")

    decision = data["closure_decision"]
    require(decision["theta_overlap_suppression_anchor_closed"] is True, "decision anchor missing")
    require(abs(decision["epsilon_theta_value"] - math.exp(-2 * math.pi)) < 1e-18, "decision epsilon mismatch")
    require(decision["alpha1_source_anchor_available"] is True, "decision alpha1 missing")
    require(decision["rtheta_alpha1_map_constructed"] is True, "decision map missing")
    require(decision["family_resolving_operator_closed"] is True, "decision family operator missing")
    require(decision["external_sources_used_as_proof"] is False, "decision external proof violation")
    require(decision["exponent_lattice_diagnostic_trials_run"] is True, "decision trials missing")
    for key in [
        "accepted_exponent_lattice_theorem",
        "accepted_HYM_threshold_prefactor_rows",
        "lambda_H_row_emitted",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_scalar_row_count_now"] == 0, "decision scalar rows overaccepted")
    require(cert["accepted_scalar_row_count_now"] == 0, "certificate scalar rows overaccepted")

    for phrase in [
        "selected transition factor       : exp(-4*pi)",
        "epsilon_Theta                    : exp(-2*pi)",
        "source-tier alpha1 available     : true",
        "accepted scalar rows             : 0",
        "lambda_H row emitted             : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
