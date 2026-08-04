"""Audit finite C1 trace-measure principle insertion / direct action derivation gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitec1tracemeasureprincipleinsertion_or_directactionderivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PATCH = PACKET_DIR / "finite_c1_trace_measure_principle_patch.packet.json"
REPLAY = PACKET_DIR / "patched_routeb_dynamic_c1_closure_replay.packet.json"
GUARDRAIL = PACKET_DIR / "unpatched_derivation_guardrail.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteC1TraceMeasurePrincipleInsertion_or_DirectActionDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_FINITEC1TRACEMEASUREPRINCIPLEINSERTION_OR_DIRECTACTIONDERIVATION_BUILT_PATCHED_DYNAMIC_C1_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_DynamicC1PatchToSMParityLedger_or_UnpatchedMeasureDerivation_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    patch = load(PATCH)
    replay = load(REPLAY)
    guardrail = load(GUARDRAIL)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(patch["status"] == "LOCAL_PROOF_SPINE_PRINCIPLE_PATCH_APPLIED", "patch status mismatch")
    require(patch["applied_to_local_proof_spine"] is True, "local patch not applied")
    require(patch["applied_to_external_obsidian_papers"] is False, "external corpus overclaimed")
    require(patch["derived_from_prior_axioms"] is False, "derivation overclaimed")
    require("observed masses" in patch["guardrail_text"], "patch guardrail missing")
    for key, value in patch["scope"].items():
        require(value is True, f"patch scope missing: {key}")

    require(replay["status"] == "PATCHED_ROUTE_B_DYNAMIC_C1_PACKET_CLOSED", "replay status mismatch")
    require(replay["formal_row_counts"]["total_rows"] == 110, "row total mismatch")
    require(replay["row_comparison_max_abs_error"] < 1e-12, "row comparison too large")
    promoted = replay["promoted_under_patched_spine"]
    require(promoted["physical_measure_equals_finite_trace_quadrature"] is True, "patched measure missing")
    require(promoted["selected_Galerkin_replacement_promotes_formal_rows"] is True, "patched Galerkin replacement missing")
    require(promoted["Route_B_physical_Galerkin_replacement_closed"] is True, "patched Route B closure missing")
    require(promoted["physical_A_selected"] == [[12.0, 0.0], [0.0, 12.0]], "patched A mismatch")
    require(promoted["physical_b_selected"] == [12.0, 12.0], "patched b mismatch")
    require(promoted["physical_deltaTheta_C1"] == [1.0, 1.0], "patched delta mismatch")
    require(promoted["physical_sector_response_matrices"] is True, "patched sector matrices missing")
    require(promoted["patched_dynamic_C1_packet_closed"] is True, "patched dynamic closure missing")
    for key, value in replay["not_promoted_under_unpatched_spine"].items():
        require(value is False, f"unpatched overclaimed: {key}")

    require(guardrail["status"] == "PATCHED_CLOSURE_SEPARATED_FROM_UNPATCHED_DERIVATION", "guardrail status mismatch")
    for key, value in guardrail["unpatched_open_items"].items():
        require(value is True, f"unpatched open item missing: {key}")
    require(guardrail["direct_derivation_available_now"] is False, "direct derivation overclaimed")
    require(guardrail["principle_derived_now"] is False, "principle derivation overclaimed")

    for key in [
        "finite_C1_trace_measure_principle_applied_to_local_spine",
        "patched_physical_measure_identity",
        "patched_Route_B_physical_Galerkin_replacement",
        "patched_A_selected",
        "patched_b_selected",
        "patched_deltaTheta_C1",
        "patched_sector_response_matrices",
        "patched_dynamic_C1_packet_closure",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "unpatched_direct_PhiFinC1_action_derivation",
        "unpatched_principle_derivation",
        "unpatched_Route_A_same_source_emission",
        "full_no_knob_flavor_constants",
        "full_SM_parity_ledger_integration",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"open flag missing: {key}")
    decision = data["promotion_decision"]
    require(decision["patched_dynamic_C1_packet_closed"] is True, "patched dynamic decision missing")
    require(decision["patched_Route_B_physical_Galerkin_replacement_closed"] is True, "patched Route B decision missing")
    for key in [
        "unpatched_dynamic_C1_packet_closed",
        "unpatched_physical_measure_identity_promoted",
        "principle_derived_from_prior_axioms",
        "Route_A_same_source_emission_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"unpatched/final overclaimed: {key}")

    require(data["theorem"]["proved"] is True and data["theorem"]["patched"] is True, "patched theorem metadata missing")
    require(cert["theorem_proved"] is True and cert["theorem_patched"] is True, "certificate patched theorem metadata missing")
    require(data["closure_claimed"] is False and cert["closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["patched_spine_closure_claimed"] is True and cert["patched_spine_closure_claimed"] is True, "patched closure not claimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require("patched dynamic C1 packet closed        = True" in note, "note missing patched closure")
    require("unpatched dynamic C1 packet closed      = False" in note, "note missing unpatched guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
