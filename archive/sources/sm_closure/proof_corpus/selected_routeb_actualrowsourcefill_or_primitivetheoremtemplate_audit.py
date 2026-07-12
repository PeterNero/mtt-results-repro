"""Audit selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate"
ATTEMPT = PACKET_DIR / "current_actual_row_source_fill_attempt.packet.json"
TEMPLATE = PACKET_DIR / "primitive_kernel_source_theorem.strict_template.json"
GAP = PACKET_DIR / "remaining_primitive_source_gap.packet.json"
CERT = ROOT / "certificates" / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBActualRowSourceFill_or_PrimitiveTheoremTemplate_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    template = load(TEMPLATE)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_ROUTEB_ACTUALROWSOURCEFILL_ATTEMPT_BUILT_PRIMITIVE_SOURCE_THEOREM_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "reduction theorem not proved")
    require(attempt["finite_weyl_trace_rule_feeds_all_rows"] is True, "trace rule missing")
    require(attempt["sector_rows_assembled_from_primitive_rows"] is True, "sector assembly missing")
    require(attempt["hessian_source_rows_assembled_from_same_rows"] is True, "hessian assembly missing")
    require(attempt["selected_basis_feeds_72_primitive_rows"] is False, "basis feed overclosed")
    require(attempt["no_residual_projector_replay_used_as_source"] is False, "residual source overclosed")
    require(attempt["row_formula_source_theorem_derived"] is False, "formula theorem overclosed")
    require(attempt["source_independent_of_residual_projector_replay"] is False, "source independence overclosed")
    require(template["must_prove"]["selected_basis_feeds_row_functions"] is False, "template overclosed")
    require(template["must_prove"]["selected_hessian_counterterm_source"] is False, "hessian source overclosed")
    require(gap["validator_rejects_current_attempt"] is True, "gap should record validator rejection")
    require(gap["not_closed"]["selected_basis_to_all_72_row_functions"] is True, "basis gap missing")
    require(gap["not_closed"]["selected_hessian_counterterm_source"] is True, "hessian gap missing")
    require(proc.returncode == 1, "validator should still reject")
    require(any("source_independent_of_residual_projector_replay is not true" in line for line in proc.stderr.splitlines()), "missing source rejection")
    require(cert["strict_validator_still_rejects"] is True, "cert should reject")
    require(cert["source_independence_closed"] is False, "cert overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("intentionally rejected" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
