"""Audit primitive-C1 contractions / Weyl-pair sector-routing reconciliation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_primitivec1_contractions_or_weylpairsectorrouting_sourceemission"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTING_BRIDGE = PACKET_DIR / "sector_routing_and_contraction_bridge.packet.json"
HANDOFF = PACKET_DIR / "dynamic_value_gate_handoff.packet.json"
GUARDRAIL = PACKET_DIR / "promotion_guardrail.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1.md"

STATUS = (
    "MTT_SELECTED_PRIMITIVEC1_CONTRACTIONS_OR_WEYLPAIRSECTORROUTING_SOURCEEMISSION_"
    "BUILT_ROUTING_AND_ENVELOPE_RECONCILED_DYNAMIC_VALUE_GATE_OPEN"
)
NEXT = "MTT_Selected_DynamicOverlapTensor_HessianNormalization_or_GalerkinC1Contractions_ValueEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], label: str, errors: list[str]) -> None:
    expect(packet.get("observed_data_used") is False, f"{label} observed data used", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting used", errors)
    expect(packet.get("closure_claimed") is False, f"{label} closure overclaimed", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    routing = load(ROUTING_BRIDGE)
    handoff = load(HANDOFF)
    guardrail = load(GUARDRAIL)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "theorem should be proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem should be proved", errors)
    expect(NEXT in note, "note missing next artifact", errors)

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("routing bridge", routing),
        ("handoff", handoff),
        ("guardrail", guardrail),
    ]:
        guard(packet, label, errors)

    expect(routing.get("static_routing_closed") is True, "static routing not closed", errors)
    expect(routing.get("phase_route") == ["u", "e"], "phase route mismatch", errors)
    expect(routing.get("shift_route") == ["d", "nuD"], "shift route mismatch", errors)
    expect(routing.get("finite_trace_transfer_selected") is True, "finite trace transfer missing", errors)
    expect(
        routing.get("primitive_contraction_envelope_constructed") is True,
        "primitive envelope not constructed",
        errors,
    )
    expect(routing.get("active_shift") == [1, 1], "active shift mismatch", errors)
    expect(routing.get("fixed_fiber_class") == [0, 1, 2], "fixed fiber class mismatch", errors)
    expect(routing.get("all_fixed_fiber_rank_three") is True, "rank-three envelope missing", errors)
    expect(
        routing.get("current_layer_promoted_as_flavor_closure") is False,
        "current layer overpromoted",
        errors,
    )

    expect(handoff.get("status") == "HANDOFF_TO_NONSCALAR_DYNAMIC_VALUE_GATE", "handoff status mismatch", errors)
    expect(handoff.get("next_required_artifact") == NEXT, "handoff next mismatch", errors)
    expect(handoff.get("current_layer_value_packet_emitted") is True, "current packet missing", errors)
    expect(
        handoff.get("current_layer_degeneracy_no_go_proved") is True,
        "degeneracy no-go missing",
        errors,
    )
    minimum = handoff.get("minimum_next_value_packet", {})
    for key in [
        "selected_non_scalar_dynamic_overlap_tensor",
        "selected_Hessian_blocks_and_b_selected",
        "selected_sector_response_matrices",
        "selected_deltaTheta_C1_solution_or_consistency_rejection",
    ]:
        expect(minimum.get(key) is True, f"minimum packet missing {key}", errors)

    for key in [
        "A_selected_claimed",
        "b_selected_claimed",
        "deltaTheta_C1_claimed",
        "dynamic_overlap_tensor_claimed",
        "primitive_C1_contractions_claimed",
        "sector_response_matrices_claimed",
    ]:
        expect(guardrail.get(key) is False, f"guardrail overclaimed {key}", errors)
    expect(guardrail.get("rank_or_consistency_test_allowed") is False, "rank test overenabled", errors)
    expect(
        guardrail.get("delta_gate_selected_operator_available") is False,
        "delta gate operator overavailable",
        errors,
    )

    closes = data.get("what_closes_now", {})
    for key in [
        "missing_spine_bridge_constructed",
        "static_weylpair_sector_routing_imported",
        "primitive_contraction_envelope_imported",
        "degenerate_current_layer_guard_preserved",
        "next_dynamic_value_gate_selected",
    ]:
        expect(closes.get(key) is True, f"close flag missing {key}", errors)
    for key in ["A_selected_claimed", "b_selected_claimed", "selected_values_available"]:
        expect(data.get(key) is False, f"candidate overclaimed {key}", errors)

    if errors:
        print("Primitive-C1/Weyl-pair bridge audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Primitive-C1/Weyl-pair bridge audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
