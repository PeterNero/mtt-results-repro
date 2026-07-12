"""Audit selected_routeb_independentquadraturepayload_schema_or_executionworkorder."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_routeb_independentquadraturepayload_schema_or_executionworkorder"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SCHEMA = PACKET_DIR / "routeb_independent_quadrature_payload_schema.packet.json"
WORKORDER = PACKET_DIR / "routeb_independent_quadrature_execution_workorder.packet.json"
TEMPLATE = PACKET_DIR / "routeb_independent_quadrature_payload_template.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteB_IndependentQuadraturePayload_Schema_or_ExecutionWorkorder_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    schema = load(SCHEMA)
    workorder = load(WORKORDER)
    template = load(TEMPLATE)
    validator_result = load(VALIDATOR_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(TEMPLATE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_ROUTEB_INDEPENDENTQUADRATUREPAYLOAD_SCHEMA_BUILT_EXECUTION_VALUES_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "payload readiness theorem not proved")
    require(schema["required_stage_counts"]["primitive_contractions"] == 72, "primitive count mismatch")
    require(schema["required_stage_counts"]["hessian_source"] == 2, "hessian count mismatch")
    require(schema["required_stage_counts"]["sector_matrices"] == 36, "sector count mismatch")
    require(schema["required_stage_counts"]["strict_payload_rows"] == 110, "strict payload count mismatch")
    require(workorder["counts"]["basis_prerequisite_rows"] == 19, "basis prerequisite count mismatch")
    require(len(template["rows"]) == 110, "template row count mismatch")
    require(proc.returncode == 1, "unfilled template should fail")
    require(validator_result["returncode"] == 1, "recorded validator result should fail")
    require(data["validator_rejects_unfilled_template"] is True, "candidate should record validator rejection")
    require(cert["validator_rejects_unfilled_template"] is True, "cert should record validator rejection")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["locked_target_values_used_as_source"] is False, "locked target used as source")
    require("72+2+36" in note, "note missing row packet summary")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
