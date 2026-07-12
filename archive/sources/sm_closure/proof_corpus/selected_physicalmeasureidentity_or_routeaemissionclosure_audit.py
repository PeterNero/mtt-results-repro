"""Audit physical measure-identity or Route A emission closure gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalmeasureidentity_or_routeaemissionclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IDENTITY = PACKET_DIR / "physical_measure_identity_theorem_slot.packet.json"
AXIOM = PACKET_DIR / "finite_c1_trace_measure_principle_draft.packet.json"
ROUTE_A = PACKET_DIR / "routea_same_source_emission_closure_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalMeasureIdentity_or_RouteAEmissionClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALMEASUREIDENTITY_OR_ROUTEAEMISSIONCLOSURE_BUILT_THEOREM_SLOT_AXIOM_DRAFT_OPEN"
NEXT = "MTT_Selected_FiniteC1TraceMeasurePrincipleInsertion_or_DirectActionDerivation_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    identity = load(IDENTITY)
    axiom = load(AXIOM)
    route_a = load(ROUTE_A)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(identity["status"] == "PHYSICAL_MEASURE_IDENTITY_THEOREM_SLOT_BUILT_NOT_PROVED", "identity status mismatch")
    for key, value in identity["closed_support"].items():
        require(value is True, f"identity support missing: {key}")
    for key, value in identity["missing_for_direct_proof"].items():
        require(value is True, f"direct-proof gap missing: {key}")
    require(identity["direct_derivation_available_now"] is False, "direct derivation overclaimed")
    require(identity["principle_inserted_now"] is False, "principle insertion overclaimed")
    require(identity["route_A_closed_now"] is False, "route A overclaimed in identity")
    require(identity["identity_promoted_now"] is False, "identity overpromoted")

    require(axiom["status"] == "INSERTION_READY_PRINCIPLE_DRAFT_NOT_APPLIED", "axiom status mismatch")
    require("normalized trace/Frobenius measure" in axiom["principle_text"], "principle text missing measure")
    require(len(axiom["why_this_principle_is_minimal"]) == 4, "minimality reasons incomplete")
    would = axiom["would_promote_if_inserted_or_derived"]
    require(would["physical_measure_equals_finite_trace_quadrature"] is True, "measure conditional missing")
    require(would["Route_B_physical_Galerkin_replacement_closed"] is True, "Route B conditional missing")
    require(would["physical_A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "conditional A mismatch")
    require(would["physical_b_selected"] == [12.0, 12.0], "conditional b mismatch")
    require(would["physical_deltaTheta_C1"] == [1.0, 1.0], "conditional delta mismatch")
    require(would["unpatched_SM_parity_dynamic_packet_closed"] is True, "conditional dynamic closure missing")
    require(axiom["applied_now"] is False, "axiom applied overclaimed")

    require(route_a["status"] == "ROUTE_A_RECHECKED_STILL_OPEN", "route A status mismatch")
    for key, value in route_a["current_emissions"].items():
        require(value is False, f"Route A emission overclaimed: {key}")
    require(route_a["all_required_emitted_now"] is False, "Route A all-emitted overclaimed")
    require(route_a["route_A_closes_now"] is False, "Route A closure overclaimed")
    require(len(route_a["why_not_closed"]) == 3, "Route A guardrails incomplete")

    for key in [
        "physical_measure_identity_theorem_slot_built",
        "finite_C1_trace_measure_principle_drafted",
        "route_A_rechecked",
        "closure_routes_reduced_to_three_legal_options",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "direct_PhiFinC1_action_derivation",
        "principle_insertion_or_derivation",
        "Route_A_same_source_emission",
        "physical_measure_identity",
        "Route_B_physical_Galerkin_replacement",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    for key, value in data["promotion_decision"].items():
        require(value is False, f"promotion overclaimed: {key}")

    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "closure overclaimed")
    require("finite C1 trace-measure principle applied     = False" in note, "note missing principle guardrail")
    require("physical measure identity promoted            = False" in note, "note missing identity guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
