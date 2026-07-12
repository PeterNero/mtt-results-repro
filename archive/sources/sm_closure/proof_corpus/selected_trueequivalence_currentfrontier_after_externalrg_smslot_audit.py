"""Audit current true-equivalence frontier after external RG and SM-slot closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_trueequivalence_currentfrontier_after_externalrg_smslot"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FRONTIER = PACKET_DIR / "current_true_equivalence_frontier.packet.json"
ROUTES = PACKET_DIR / "dual_route_execution_matrix.packet.json"
NEXT_ACTIONS = PACKET_DIR / "next_actions.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TrueEquivalence_CurrentFrontier_AfterExternalRG_SMSlot_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_TRUEEQUIVALENCE_CURRENTFRONTIER_AFTER_EXTERNALRG_SMSLOT_BUILT_OPEN"
NEXT = "MTT_Selected_PrecisionProfileLoopValues_or_ActualQaSU3OperatorPayload_CurrentExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    frontier = load(FRONTIER)
    routes = load(ROUTES)
    next_actions = load(NEXT_ACTIONS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")

    require(frontier["SM_parity_closed"] is True, "SM parity not locked closed")
    require(frontier["external_rg_local_benchmark_done"] is True, "local RG benchmark not imported")
    require(frontier["external_literature_rg_rows_done"] is True, "external literature RG rows not imported")
    require(frontier["local_qft_functor_interface_done"] is True, "local QFT functor interface not imported")
    require(frontier["static_smslot_source_closed"] is True, "static SM-slot source not imported")
    require(
        frontier["static_sector_route_and_trace_normalization_closed"] is True,
        "static route/trace normalization not imported",
    )
    require(frontier["hym_diagonal_first_solve_closed"] is True, "HYM diagonal first solve not imported")
    require(
        frontier["stationary_projector_dotd_reconciled"] is True,
        "stationary projector/dotD reconciliation not imported",
    )
    require(frontier["true_SM_equivalence_closed"] is False, "true SM equivalence overclosed")
    require(frontier["no_knob_closed"] is False, "no-knob closure overclosed")

    route_a = routes["route_A_precision_profile_loop_values"]
    require(route_a["surrogate_profile_matrix_reconstructed"] is True, "surrogate profile not imported")
    require(route_a["accepted_as_full_profile"] is False, "surrogate profile overaccepted")
    require(route_a["closed_now"] is False, "route A overclosed")
    require(
        "published or independently reconstructed non-Higgs profile likelihood" in route_a["must_emit"],
        "route A missing profile-likelihood target",
    )

    route_b = routes["route_B_actual_qasu3_hym_operator_payload"]
    require(route_b["closed_now"] is False, "route B overclosed")
    for harvested in [
        "selected diagonal HYM first solve",
        "diagonal End0 D_E formula",
        "full diagonal End0 Riesz/Green",
        "static SM-slot six-arrow source",
        "static 1_M Dirac neutrino shift rule",
        "stationary projector/dotD reconciliation",
    ]:
        require(harvested in route_b["already_harvested"], f"route B missing harvested result: {harvested}")
    require("actual selected Qa/SU3 operator packet" in route_b["must_emit"], "route B missing Qa/SU3 target")
    require(
        "selected primitive C1 contractions" in route_b["must_emit"],
        "route B missing primitive C1 target",
    )

    route_c = routes["route_C_interfaces"]
    require(route_c["closed_now"] is False, "route C overclosed")
    require(
        any("QM/GR measurement" in item for item in route_c["must_emit"]),
        "route C missing QM/GR interface target",
    )

    require(next_actions["recommended_next_artifact"] == NEXT, "next action artifact mismatch")
    guard = next_actions["why_this_is_not_a_regression"]
    require("starts after external RG" in guard, "regression guard missing external RG boundary")
    require("only true-equivalence value/operator exits" in guard, "regression guard missing true-equivalence exit boundary")

    closes = data["what_closes_now"]
    for key in [
        "external_rg_rung_confirmed_done",
        "external_literature_rg_rung_confirmed_done",
        "static_smslot_source_closure_confirmed_done",
        "true_equivalence_dual_route_frontier_locked",
        "SM_parity_not_reopened",
        "observed_constants_excluded_as_selectors",
    ]:
        require(closes[key] is True, f"candidate close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "published_or_reconstructed_profile_likelihood",
        "precision_local_QFT_loop_values",
        "actual_QaSU3_operator_packet",
        "dynamic_sector_ready_operator_payload",
        "QM_GR_measurement_response_interfaces",
        "true_SM_equivalence",
        "no_knob_closure",
    ]:
        require(remains[key] is True, f"candidate open flag missing: {key}")

    require(data["closure_decision"]["SM_parity_closed"] is True, "candidate SM parity not closed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclosed")
    require(data["closure_claimed"] is False, "candidate incorrectly claims closure")
    require("not SM-parity repair" in note, "note missing SM-parity repair guard")
    require("precision profile/loop/covariance" in note, "note missing precision frontier")

    for packet in [data, frontier, routes, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
