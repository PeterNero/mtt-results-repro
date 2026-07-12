"""Audit selected_routeb_selectedbasisindependencefill_or_rowsourcegap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
BASIS_FILL = PACKET_DIR / "route_b_selected_basis_independence_fill.packet.json"
ROW_GAP = PACKET_DIR / "row_source_independence_gap.packet.json"
CERT = ROOT / "certificates" / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBSelectedBasisIndependenceFill_or_RowSourceGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    fill = load(BASIS_FILL)
    gap = load(ROW_GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    route_b = fill["route_B_independent_execution"]
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(BASIS_FILL)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_ROUTEB_SELECTEDBASISINDEPENDENCEFILL_BUILT_ROW_SOURCE_GAP_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(route_b["selected_basis_independent_of_residual_projector"] is True, "basis not closed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source overclosed")
    cert_packet = route_b["selected_basis_independence_certificate"]
    require(cert_packet["uses_residual_projector_replay"] is False, "basis uses residual replay")
    require(cert_packet["uses_locked_C1_target_values"] is False, "basis uses locked target")
    require(cert_packet["all_sector_sources_verified_by_transport_conjugation"] is True, "transport sources not verified")
    require(gap["closed_now"]["selected_basis_independent_of_residual_projector"] is True, "gap basis mismatch")
    require(gap["not_closed"]["source_independent_of_residual_projector_replay"] is True, "gap source mismatch")
    require(proc.returncode == 1, "strict validator should still reject")
    require(any("Route B missing: source_independent_of_residual_projector_replay" in line for line in proc.stderr.splitlines()), "unexpected Route B rejection")
    require(cert["selected_basis_independence_closed"] is True, "cert basis missing")
    require(cert["source_independence_closed"] is False, "cert source overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("strict validator still rejects" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
