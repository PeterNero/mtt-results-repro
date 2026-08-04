"""Audit selected_i11_routeb_rowsource_theorem_push_or_routea_fallback."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT = PACKET_DIR / "current_rowsource_theorem_push_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_rowsource_theorem_witness.packet.json"
ROUTEB_PLUG = PACKET_DIR / "conditional_routeb_physical_certificate_plug.packet.json"
FRONTIER = PACKET_DIR / "remaining_rowsource_or_routea_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_rowsource_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_rowsource_validator_result.packet.json"
ROUTEB_PLUG_RESULT = PACKET_DIR / "conditional_routeb_physical_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11_RouteBRowSourceTheoremPush_or_RouteAFallback_v1.md"
ROWSOURCE_VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(validator: Path, path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.returncode


def main() -> int:
    data = load(DATA)
    current = load(CURRENT)
    witness = load(WITNESS)
    routeb_plug = load(ROUTEB_PLUG)
    frontier = load(FRONTIER)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    routeb_plug_result = load(ROUTEB_PLUG_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11_ROUTEB_ROWSOURCE_THEOREM_PUSH_BUILT_FINAL_SOURCE_PROMOTION_GATE", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem reduction not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(current["finite_weyl_trace_rule_feeds_all_rows"] is True, "finite trace feed missing")
    require(current["sector_rows_assembled_from_primitive_rows"] is True, "sector assembly missing")
    require(current["hessian_source_rows_assembled_from_same_rows"] is True, "hessian assembly missing")
    require(current["selected_basis_feeds_72_primitive_rows"] is False, "current overclosed basis feed")
    require(current["no_residual_projector_replay_used_as_source"] is False, "current overclosed residual replay")
    require(current["row_formula_source_theorem_derived"] is False, "current overclosed formula theorem")
    require(current["source_independent_of_residual_projector_replay"] is False, "current overclosed source independence")

    require(witness["selected_basis_feeds_72_primitive_rows"] is True, "witness missing basis feed")
    require(witness["no_residual_projector_replay_used_as_source"] is True, "witness missing residual guardrail")
    require(witness["row_formula_source_theorem_derived"] is True, "witness missing formula theorem")
    require(witness["source_independent_of_residual_projector_replay"] is True, "witness missing source independence")
    require(witness["conditional_only"] is True, "witness should be conditional")

    route_b = routeb_plug["route_B_independent_execution"]
    require(route_b["source_independent_of_residual_projector_replay"] is True, "Route B plug not filled")
    require(len(route_b["attached_independent_provenance_sources"]) >= 4, "Route B plug evidence too short")
    require(routeb_plug["conditional_only"] is True, "Route B plug should be conditional")

    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(routeb_plug_result["returncode"] == 0, "recorded Route B plug validator should pass")
    require(validator_returncode(ROWSOURCE_VALIDATOR, CURRENT) == 1, "current validator should still fail")
    require(validator_returncode(ROWSOURCE_VALIDATOR, WITNESS) == 0, "witness validator should pass")
    require(validator_returncode(PHYSICAL_VALIDATOR, ROUTEB_PLUG) == 0, "Route B plug validator should pass")

    require(frontier["not_a_search_problem_anymore"] is True, "frontier should retire search framing")
    require(frontier["route_B_remaining_proof_object"]["name"] == "SelectedFiniteC1SourcePromotionLemma", "wrong Route B proof object")
    require(frontier["closed_now"]["conditional_routeb_physical_certificate_passes"] is True, "frontier missing conditional Route B pass")
    require(data["what_remains_open"]["SelectedFiniteC1SourcePromotionLemma"] is True, "candidate missing source lemma open field")
    require(cert["current_rowsource_attempt_rejected"] is True, "cert missing current rejection")
    require(cert["conditional_rowsource_witness_passes"] is True, "cert missing conditional witness pass")
    require(cert["conditional_routeb_physical_certificate_passes"] is True, "cert missing conditional Route B pass")
    require("Route B is no longer a" in note, "note missing search retirement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
