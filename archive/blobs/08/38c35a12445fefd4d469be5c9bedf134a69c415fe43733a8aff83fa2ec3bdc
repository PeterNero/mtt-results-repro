"""Audit selected_hessiancountertermsource_bvector_theoremtemplate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_hessiancountertermsource_bvector_theoremtemplate.candidate.json"
TARGET = ROOT / "candidate_data" / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_formal_target.packet.json"
TEMPLATE = ROOT / "candidate_data" / "selected_hessiancountertermsource_bvector_theoremtemplate" / "hessian_bvector_source_theorem.strict_template.json"
GAP = ROOT / "candidate_data" / "selected_hessiancountertermsource_bvector_theoremtemplate" / "remaining_hessian_bvector_source_gap.packet.json"
CERT = ROOT / "certificates" / "selected_hessiancountertermsource_bvector_theoremtemplate_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HessianCountertermSource_BVector_TheoremTemplate_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    target = load(TARGET)
    template = load(TEMPLATE)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_HESSIANCOUNTERTERMSOURCE_BVECTOR_TEMPLATE_BUILT_SOURCE_EMISSION_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "reduction theorem not proved")
    require(target["hessian_row_count"] == 2, "wrong hessian row count")
    require(target["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(target["b_norm_sq"] == 24.0, "b norm mismatch")
    require(target["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(target["physical_source_promoted"] is False, "target source overpromoted")
    require(template["must_prove"]["same_branch_phifin_c1_or_galerkin_source_emits_hessian_rows"] is False, "source theorem overclosed")
    require(template["must_prove"]["same_source_b_selected_emitted"] is False, "b source overclosed")
    require(template["must_prove"]["no_locked_target_values_used_as_source"] is True, "locked target guard missing")
    require(gap["closed_now"]["formal_hessian_row_count_is_two"] is True, "formal count not closed")
    require(gap["not_closed"]["selected_hessian_counterterm_source"] is True, "hessian gap missing")
    require(gap["not_closed"]["selected_b_vector_source"] is True, "b gap missing")
    require(cert["formal_target_identified"] is True, "cert target missing")
    require(cert["hessian_counterterm_source_closed"] is False, "cert hessian overclosed")
    require(cert["b_selected_source_closed"] is False, "cert b overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("This is still not source emission" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
