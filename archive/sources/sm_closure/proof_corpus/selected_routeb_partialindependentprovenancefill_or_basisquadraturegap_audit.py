"""Audit selected_routeb_partialindependentprovenancefill_or_basisquadraturegap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_routeb_partialindependentprovenancefill_or_basisquadraturegap.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_routeb_partialindependentprovenancefill_or_basisquadraturegap"
PARTIAL = PACKET_DIR / "route_b_partial_independent_provenance_fill.packet.json"
GAP = PACKET_DIR / "basis_quadrature_independence_gap.packet.json"
CERT = ROOT / "certificates" / "selected_routeb_partialindependentprovenancefill_or_basisquadraturegap_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBPartialIndependentProvenanceFill_or_BasisQuadratureGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    partial = load(PARTIAL)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    route_b = partial["route_B_independent_execution"]
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PARTIAL)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_ROUTEB_PARTIALINDEPENDENTPROVENANCEFILL_BUILT_BASIS_QUADRATURE_GAP_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(route_b["all_72_primitive_rows_executed"] is True, "72 rows not closed")
    require(route_b["formal_110_rows_executed"] is True, "110 rows not closed")
    require(route_b["exactness_or_error_certificates_attached"] is True, "exactness not attached")
    require(route_b["selected_basis_independent_of_residual_projector"] is False, "basis overclosed")
    require(route_b["quadrature_rule_independent_of_locked_target"] is False, "quadrature overclosed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source independence overclosed")
    require(len(route_b["attached_independent_provenance_sources"]) >= 3, "support sources missing")
    require(gap["closed_now"]["finite_Weyl_trace_measure_derived"] is True, "finite trace support missing")
    require(proc.returncode == 1, "strict validator should reject partial fill")
    require(any("Route B missing" in line for line in proc.stderr.splitlines()), "missing Route B rejection")
    require(cert["strict_validator_still_rejects"] is True, "cert validator mismatch")
    require(cert["route_B_exactness_or_error_certificates_attached"] is True, "cert exactness missing")
    require(cert["route_B_basis_independence_closed"] is False, "cert basis overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("strict validator still rejects" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
