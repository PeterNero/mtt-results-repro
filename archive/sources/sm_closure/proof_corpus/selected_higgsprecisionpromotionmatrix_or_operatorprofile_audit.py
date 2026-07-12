"""Audit the Higgs precision-promotion matrix artifact."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsprecisionpromotionmatrix_or_operatorprofile"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MATRIX = PACKET_DIR / "higgs_precision_promotion_matrix.packet.json"
DIAGONAL = PACKET_DIR / "higgs_diagonal_sidecar_profile_stress.packet.json"
OPERATOR = PACKET_DIR / "higgs_operator_profile_promotion_obligations.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsPrecisionPromotionMatrix_or_OperatorProfile_v1.md"

STATUS = "MTT_SELECTED_HIGGSPRECISIONPROMOTIONMATRIX_OR_OPERATORPROFILE_BUILT_PRECISION_PROMOTION_BLOCKERS_EXACT"
NEXT = "MTT_Selected_HiggsAcceptedFormulaRows_or_CorrelatedProfileValues_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    matrix = load(MATRIX)
    diagonal = load(DIAGONAL)
    operator = load(OPERATOR)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(matrix["summary"]["row_count"] == 10, "promotion matrix does not cover ten channels")
    require(matrix["summary"]["precision_rows_promoted"] == 0, "precision row was overpromoted")
    require(matrix["summary"]["all_rows_have_operator_obligations"] is True, "operator obligations incomplete")
    require(matrix["summary"]["all_rows_have_formula_obligations"] is True, "formula obligations incomplete")
    require(len(matrix["rows"]) == 10, "row count mismatch")
    for row in matrix["rows"]:
        require(row["accepted_for_SM_parity_replay"] is True, f"replay row not accepted: {row['channel']}")
        require(row["accepted_as_precision_width"] is False, f"precision overclaim: {row['channel']}")
        require(row["accepted_as_no_knob_or_source_derived_value"] is False, f"no-knob overclaim: {row['channel']}")
        require(len(row["precision_blockers"]) >= 4, f"blockers missing: {row['channel']}")
    require(diagonal["summary"]["term_count"] == 10, "diagonal stress not ten-channel")
    require(diagonal["summary"]["full_covariance_profile_closed"] is False, "full covariance overclaimed")
    require(diagonal["summary"]["accepted_as_precision_profile_likelihood"] is False, "precision likelihood overclaimed")
    require(operator["global_required_packets"], "global operator packets missing")
    require("selected Qa/SU3 color/operator packet" in " ".join(operator["global_required_packets"]), "Qa/SU3 obligation missing")
    require(data["closure_decision"]["precision_promotion_matrix_closed"] is True, "promotion matrix not closed")
    require(data["closure_decision"]["Higgs_precision_widths_closed"] is False, "precision widths overclaimed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true SM equivalence overclaimed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not a correlated" in note, "note missing diagonal guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
