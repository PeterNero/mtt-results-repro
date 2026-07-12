"""Audit the U1/SU2 threshold-index source theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "u1_su2_threshold_index_source_theorem_certificate.json"
DATA = REPO / "candidate_data" / "u1_su2_threshold_index_source_theorem.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_SU2_Threshold_Index_Source_Selector_or_Operator_Spectrum_v1.md"
SCRIPT = REPO / "scripts" / "build_u1_su2_threshold_index_source_theorem.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def hypothesis(data: dict[str, object], hid: str) -> dict[str, object]:
    return next(item for item in data["promotion_hypotheses"] if item["id"] == hid)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    theorem = data["source_theorem"]
    decision = data["decision"]
    checks = [
        check("status", cert["status"] == "U1_SU2_TWO_THIRDS_SOURCE_THEOREM_BUILT_PROMOTION_HYPOTHESES_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("derives 2/3", theorem["derived_weight"]["U1"] == "2/3" and theorem["derived_weight"]["SU2"] == "1/1", theorem["derived_weight"]),
        check("proof uses trace quotient", any("Tr(P_perp)/Tr(I_V)" in step for step in theorem["proof_steps"]), theorem["proof_steps"]),
        check("central circle support imported", data["corpus_support"]["central_circle_neutrality"]["supports_unique_shared_channel"] is True and data["corpus_support"]["central_circle_neutrality"]["supports_gauge_neutrality"] is True, data["corpus_support"]["central_circle_neutrality"]),
        check("target not used", decision["uses_electroweak_target"] is False and data["target_fitting_used"] is False, decision),
        check("carrier hypothesis open", hypothesis(data, "H1_three_direction_u1_threshold_carrier")["current_status"] == "OPEN", hypothesis(data, "H1_three_direction_u1_threshold_carrier")),
        check("central hypothesis partial only", hypothesis(data, "H2_exactly_one_shared_central_universal_mode")["current_status"] == "PARTIAL_SUPPORT", hypothesis(data, "H2_exactly_one_shared_central_universal_mode")),
        check("quotient hypothesis open", hypothesis(data, "H3_physical_quotient_removes_shared_mode")["current_status"] == "OPEN", hypothesis(data, "H3_physical_quotient_removes_shared_mode")),
        check("SU2 branch open", hypothesis(data, "H4_SU2_unit_index_or_selected_spectrum")["current_status"] == "OPEN", hypothesis(data, "H4_SU2_unit_index_or_selected_spectrum")),
        check("not promoted", decision["promoted_to_selected_threshold_index"] is False and decision["measured_electroweak_closure"] is False, decision),
        check("later contract lists missing hypotheses", set(data["later_documentation_contract"]["must_fill_before_promotion"]) >= {"H1_three_direction_u1_threshold_carrier", "H3_physical_quotient_removes_shared_mode", "H4_SU2_unit_index_or_selected_spectrum"}, data["later_documentation_contract"]),
        check("note documents later use", "Documentation Contract For Later" in note and "must cite this theorem" in note, NOTE),
    ]
    print("\nSelected U1/SU2 threshold-index source theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
