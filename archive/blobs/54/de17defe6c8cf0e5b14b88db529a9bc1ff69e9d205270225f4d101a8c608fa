"""Audit selected_routeb_quadratureindependencefill_or_selectedbasisgap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_routeb_quadratureindependencefill_or_selectedbasisgap.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_routeb_quadratureindependencefill_or_selectedbasisgap"
QUAD = PACKET_DIR / "route_b_quadrature_independence_fill.packet.json"
GAP = PACKET_DIR / "selected_basis_source_gap.packet.json"
CERT = ROOT / "certificates" / "selected_routeb_quadratureindependencefill_or_selectedbasisgap_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBQuadratureIndependenceFill_or_SelectedBasisGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    quad = load(QUAD)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    route_b = quad["route_B_independent_execution"]
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(QUAD)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_ROUTEB_QUADRATUREINDEPENDENCEFILL_BUILT_SELECTED_BASIS_SOURCE_GAP_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(route_b["quadrature_rule_independent_of_locked_target"] is True, "quadrature not closed")
    require(route_b["selected_basis_independent_of_residual_projector"] is False, "basis overclosed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source overclosed")
    require(route_b["quadrature_independence_certificate"]["uses_locked_target_values"] is False, "target values used")
    require(gap["closed_now"]["quadrature_rule_independent_of_locked_target"] is True, "gap packet mismatch")
    require(gap["zero_mode_bridge_selected_values_emitted"] is False, "zero-mode bridge overemitted")
    require(proc.returncode == 1, "strict validator should still reject")
    require(any("Route B missing: selected_basis_independent_of_residual_projector, source_independent_of_residual_projector_replay" in line for line in proc.stderr.splitlines()), "unexpected Route B rejection")
    require(cert["quadrature_independence_closed"] is True, "cert quadrature missing")
    require(cert["selected_basis_independence_closed"] is False, "cert basis overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("strict validator still rejects" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
