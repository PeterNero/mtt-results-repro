"""Audit integrated post-source frontier / higher-response value gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_integratedpostsourcefrontier_or_higherresponsevaluegate"
DATA = ROOT / "candidate_data"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
SOURCE_SCOPE = BASE / "source_scope_reconciliation.packet.json"
VALUE_FRONTIER = BASE / "postsource_value_frontier.packet.json"
NEXT_CUTSET = BASE / "nonlooping_next_value_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_IntegratedPostSourceFrontier_or_HigherResponseValueGate_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_INTEGRATEDPOSTSOURCEFRONTIER_OR_HIGHERRESPONSEVALUEGATE_BUILT_"
    "SOURCE_DOTD_RETIRED_VALUE_CLOSURE_OPEN"
)
NEXT = "MTT_Selected_HigherOrderFullResponseMatrices_or_SecondOrderFlavorLift_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector used")
    require(packet.get("target_fitting_used") is False, "target fitting used")
    require(packet.get("closure_claimed") is False, "closure overclaimed")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILDER)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return proc.returncode

    candidate = load(CANDIDATE)
    source_scope = load(SOURCE_SCOPE)
    frontier = load(VALUE_FRONTIER)
    cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["what_closes_now"]["source_scope_contradiction_resolved"] is True, "scope reconciliation missing")
    require(candidate["what_closes_now"]["alpha1_dotD_not_reopened_as_value_blocker"] is True, "dotD guard missing")
    require(candidate["what_closes_now"]["next_nonlooping_value_cutset_selected"] is True, "next cutset missing")

    closure = candidate["closure_decision"]
    require(closure["source_stack_closed_for_first_response"] is True, "source stack should be closed for first response")
    require(closure["dotD_alpha1_retired"] is True, "dotD should be retired")
    require(closure["higher_response_value_closure"] is False, "higher-response value overclosed")
    require(closure["accepted_Yukawa_Higgs_value_closure"] is False, "Yukawa/Higgs overclosed")
    require(closure["threshold_response_closure"] is False, "threshold overclosed")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(closure["full_no_knob_closed"] is False, "no-knob overclosed")

    closed_scope = source_scope["closed_source_scope"]
    for key in [
        "unpatched_source_promotion_replay_stack",
        "VSD01_first_response_source_scope",
        "VSD01_dynamic_tensor_subgate",
        "stationary_rho_s_transport_validator",
        "same_branch_dotD_alpha1",
        "gauge_transported_functional_Phi_fin_trace",
        "diagonal_End0_HYM_operator_payload",
    ]:
        require(closed_scope[key] is True, f"closed source scope missing: {key}")

    for key, value in source_scope["scope_guardrails"].items():
        require(value is True, f"guardrail false: {key}")

    open_frontier = frontier["still_open"]
    for key in [
        "higher_order_full_response_matrices",
        "selected_second_order_physical_matrices",
        "higher_response_Rtheta_execution",
        "full_S2_value_execution",
        "accepted_Yukawa_Higgs_value_rows",
        "threshold_matching_and_mass_scheme_rows",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(open_frontier[key] is True, f"open frontier missing: {key}")

    require(cutset["primary_internal_route"]["artifact"] == NEXT, "primary next mismatch")
    require("re-proving A_selected" in cutset["forbidden_reentries"][0], "source reentry guard missing")
    require("using observed masses" in cutset["forbidden_reentries"][2], "observed selector guard missing")
    require(len(cutset["success_criteria_for_next_gate"]) == 4, "success criteria count mismatch")

    require(cert["status"] == STATUS, "certificate status mismatch")
    require(cert["source_stack_closed_for_first_response"] is True, "cert source closure mismatch")
    require(cert["dotD_alpha1_retired"] is True, "cert dotD mismatch")
    require(cert["higher_response_value_closure"] is False, "cert value overclosed")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")

    require("Do not re-enter" in note, "note guardrail missing")
    require("active wall is value emission" in note, "note active wall missing")

    for packet in [candidate, source_scope, frontier, cutset, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
