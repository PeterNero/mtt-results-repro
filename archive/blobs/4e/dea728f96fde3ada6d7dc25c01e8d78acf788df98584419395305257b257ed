"""Audit physical measure or finite-Galerkin promotion theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalmeasure_or_finitegalerkinpromotion"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PROMOTION_THEOREM = PACKET_DIR / "finite_galerkin_promotion_theorem.packet.json"
MEASURE_GATE = PACKET_DIR / "physical_measure_identity_gate.packet.json"
ROUTE_B = PACKET_DIR / "routeb_conditional_promotion_packet.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalMeasureOrFiniteGalerkinPromotion_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALMEASURE_OR_FINITEGALERKINPROMOTION_BUILT_PROMOTION_THEOREM_MEASURE_IDENTITY_OPEN"
NEXT = "MTT_Selected_PhysicalMeasureIdentity_or_RouteAEmissionClosure_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    theorem = load(PROMOTION_THEOREM)
    measure = load(MEASURE_GATE)
    route_b = load(ROUTE_B)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(theorem["status"] == "CONDITIONAL_PROMOTION_THEOREM_PROVED_ANTECEDENT_OPEN", "theorem status mismatch")
    for key, value in theorem["closed_support"].items():
        require(value is True, f"closed support missing: {key}")
    for key, value in theorem["open_physical_antecedents"].items():
        require(value is False, f"physical antecedent overclaimed: {key}")
    for key, value in theorem["conditional_consequences"].items():
        require(value is True, f"conditional consequence missing: {key}")
    require(theorem["promoted_now"] is False, "conditional theorem overpromoted")

    require(measure["status"] == "PHYSICAL_MEASURE_IDENTITY_OPEN_BUT_ISOLATED", "measure status mismatch")
    require("trace/Frobenius" in measure["candidate_identity"], "candidate measure identity missing")
    for key, value in measure["still_missing"].items():
        require(value is True, f"measure missing flag absent: {key}")
    for key, value in measure["not_missing_anymore"].items():
        require(value is True, f"not-missing flag absent: {key}")
    require(measure["promoted_now"] is False, "measure identity overpromoted")

    require(route_b["status"] == "ROUTE_B_CONDITIONAL_PROMOTION_READY_PHYSICAL_MEASURE_OPEN", "route B status mismatch")
    conditional = route_b["conditional_if_measure_identity_supplied"]
    require(conditional["Route_B_physical_Galerkin_replacement_closed"] is True, "conditional route B closure missing")
    require(conditional["physical_A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "conditional A mismatch")
    require(conditional["physical_b_selected"] == [12.0, 12.0], "conditional b mismatch")
    require(conditional["physical_deltaTheta_C1"] == [1.0, 1.0], "conditional delta mismatch")
    require(conditional["physical_sector_response_matrices"] is True, "conditional sector matrices missing")
    require(conditional["unpatched_SM_parity_dynamic_packet_closed"] is True, "conditional dynamic closure missing")
    for key, value in route_b["current"].items():
        require(value is False, f"route B current overclaimed: {key}")

    for key in [
        "finite_to_physical_Galerkin_promotion_theorem_proved_conditionally",
        "selected_Galerkin_replacement_acceptance_reduced_to_measure_identity",
        "physical_measure_identity_gate_isolated",
        "route_B_conditional_promotion_packet_built",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "physical_measure_equals_finite_trace_quadrature",
        "physical_PhiFinC1_action_identity",
        "no_extra_physical_boundary_or_source_term",
        "Route_A_same_source_emission",
        "Route_B_physical_Galerkin_replacement",
        "physical_A_selected",
        "physical_b_selected",
        "physical_deltaTheta_C1",
        "physical_sector_response_matrices",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    require(data["promotion_decision"]["promotion_theorem_proved"] is True, "promotion theorem flag missing")
    for key, value in data["promotion_decision"].items():
        if key != "promotion_theorem_proved":
            require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and data["theorem"]["conditional"] is True, "conditional theorem metadata missing")
    require(cert["theorem_proved"] is True and cert["theorem_conditional"] is True, "certificate theorem metadata missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require("conditional finite-to-physical theorem proved = True" in note, "note missing theorem flag")
    require("physical measure identity promoted            = False" in note, "note missing measure guardrail")
    require("Route B physical closure now                  = False" in note, "note missing route B guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
