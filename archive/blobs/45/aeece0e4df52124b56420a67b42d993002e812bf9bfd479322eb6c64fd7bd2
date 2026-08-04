"""Audit selected_i11tracemap_dynamicextension_or_firstvariationgap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11tracemap_dynamicextension_or_firstvariationgap"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TEMPLATE = PACKET_DIR / "i11_selected_trace_map.strict_template.json"
CURRENT = PACKET_DIR / "current_trace_map_dynamic_extension_attempt.packet.json"
STATIONARY = PACKET_DIR / "stationary_trace_map_sublemma.packet.json"
WITNESS = PACKET_DIR / "conditional_dynamic_trace_map_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_dynamic_trace_map_frontier.packet.json"
PLUG = PACKET_DIR / "trace_map_field_plug_into_i11.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11TraceMap_DynamicExtension_or_FirstVariationGap_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.returncode


def main() -> int:
    data = load(DATA)
    template = load(TEMPLATE)
    current = load(CURRENT)
    stationary = load(STATIONARY)
    witness = load(WITNESS)
    frontier = load(FRONTIER)
    plug = load(PLUG)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11TRACEMAP_DYNAMICEXTENSION_BUILT_STATIONARY_TRACE_CLOSED_DYNAMIC_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "frontier theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(len(template["required_fields"]) == 5, "trace-map template field count mismatch")
    require(stationary["proved"] is True, "stationary trace-map sublemma should be proved")
    require(set(stationary["selected_sectors"]) == {"H", "L", "N", "Q", "d", "e", "u"}, "sector coverage mismatch")
    require(stationary["dynamic_flags_retained_open"]["physical_first_variation_identity"] is False, "dynamic flags overpromoted")

    for field in template["required_fields"]:
        require(current[field] is False, f"current should not close {field}")
        require(witness[field] is True, f"witness missing {field}")
    require(current["stationary_trace_map_values_proved"] is True, "current should carry stationary support")
    require(current["free_axiom_patch_used"] is False, "free patch used")
    require(witness["conditional_only"] is True, "witness should be conditional")

    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(frontier["closed_now"]["stationary_trace_map_sublemma"] is True, "stationary frontier not closed")
    require(frontier["still_open"]["selected_minimizer_identifier"]["current_support"] is False, "minimizer overpromoted")
    require(frontier["still_open"]["c1_response_coordinate_map"]["current_support"] is False, "dynamic C1 rows overpromoted")
    require(frontier["still_open"]["selected_normalization_boundary_clause"]["normalization_closed"] is True, "normalization lost")
    require(frontier["still_open"]["selected_normalization_boundary_clause"]["boundary_closed"] is False, "boundary overpromoted")
    require(plug["trace_map_validator_returncode"] == 0, "conditional plug should validate")
    require("first_variation_identity" in plug["does_not_close_i11_fields"], "plug should leave first variation open")
    require(cert["stationary_trace_map_sublemma_proved"] is True, "cert should record stationary sublemma")
    require("stationary trace-map sublemma proved = True" in note, "note missing stationary statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
