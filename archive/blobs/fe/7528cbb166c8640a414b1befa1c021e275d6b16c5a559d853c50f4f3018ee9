"""Audit diagonal QCD profile block fallback."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BLOCK = PACKET_DIR / "qcd_diagonal_profile_block.packet.json"
PSD = PACKET_DIR / "qcd_profile_psd_and_chisquare_check.packet.json"
REPAIR = PACKET_DIR / "qcd_repair_values_status_after_profile_block.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsQCDRepairValues_or_ProfileCovarianceBlock_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDREPAIRVALUES_OR_PROFILECOVARIANCEBLOCK_BUILT_DIAGONAL_QCD_PROFILE_FALLBACK"
NEXT = "MTT_Selected_HiggsQCDFormulaRepairValues_or_QaSU3OperatorAttachment_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    block = load(BLOCK)
    psd = load(PSD)
    repair = load(REPAIR)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["target_fitting_used"] is False, "target fitting overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector guard missing")
    require(block["summary"]["dimension"] == 4, "QCD block dimension mismatch")
    require(block["channels"] == ["H_to_bb", "H_to_cc", "H_to_ss", "H_to_gg"], "channel order mismatch")
    require(block["summary"]["diagonal_only"] is True, "block should be diagonal only")
    require(block["summary"]["accepted_as_parity_profile_fallback"] is True, "fallback not accepted")
    require(block["summary"]["accepted_as_full_correlated_profile"] is False, "full correlation overclaimed")
    require(block["summary"]["accepted_as_precision_profile"] is False, "precision overclaimed")
    require(psd["all_eigenvalues_nonnegative"] is True, "PSD check failed")
    require(psd["all_eigenvalues_positive"] is True, "positive diagonal variances failed")
    require(psd["full_correlated_profile_closed"] is False, "correlated profile overclaimed")
    require(psd["precision_profile_closed"] is False, "precision profile overclaimed")
    require(repair["repair_values_filled"] is False, "repair values overfilled")
    require(repair["values_promotable_now"] is False, "values overpromoted")
    require(repair["qcd_profile_block_filled_as_diagonal_fallback"] is True, "profile fallback status missing")
    require(repair["full_correlated_profile_filled"] is False, "full profile overfilled")
    require(repair["selected_QaSU3_operator_attachment_closed"] is False, "Qa/SU3 overclaimed")
    require(data["closure_decision"]["diagonal_profile_fallback_closed"] is True, "fallback not closed")
    require(data["closure_decision"]["full_correlated_profile_closed"] is False, "candidate full profile overclaimed")
    require(data["closure_decision"]["repair_values_filled"] is False, "candidate repair overfilled")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("does not claim a full correlated precision profile" in note, "note missing precision guard")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
