"""Audit selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
NORMAL_FORM = PACKET_DIR / "primitive_row_kernel_source_normal_form.packet.json"
CONTRACT = PACKET_DIR / "selected_source_object_contract.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "rowsource_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteB_RowKernelSource_NormalForm_or_SourceObjectContract_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    normal = load(NORMAL_FORM)
    contract = load(CONTRACT)
    validator = load(VALIDATOR_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_ROUTEB_ROWKERNELSOURCE_NORMALFORM_BUILT_SOURCE_OBJECT_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "normal form theorem not proved")
    require(normal["closed_support"]["finite_weyl_trace_measure_normalization"] is True, "measure normalization should be closed")
    require(normal["closed_support"]["all_110_strict_row_slots_present"] is True, "110 row support missing")
    require(normal["open_source_clauses"]["C1_action_restricts_to_finite_trace_measure"] is True, "action restriction gap missing")
    require(normal["open_source_clauses"]["zero_extra_boundary_or_source_terms"] is True, "boundary/source gap missing")
    require(normal["open_source_clauses"]["selected_basis_feeds_72_row_functions"] is True, "basis-to-row gap missing")
    require(normal["open_source_clauses"]["selected_phase_shift_variation_operators_before_residual_projection"] is True, "variation operator gap missing")
    require(normal["open_source_clauses"]["selected_hessian_counterterm_and_b_source"] is True, "Hessian/b gap missing")
    require(contract["minimal_source_object"] == "selected finite C1 row-kernel functional packet", "wrong minimal source object")
    require(len(contract["must_emit"]) == 5, "must_emit clause count mismatch")
    require(validator["returncode"] == 1, "validator should still reject current row-source attempt")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(cert["theorem_proved"] is True, "cert theorem missing")
    require("selected finite C1 row-kernel functional packet" in note, "note missing source object")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
