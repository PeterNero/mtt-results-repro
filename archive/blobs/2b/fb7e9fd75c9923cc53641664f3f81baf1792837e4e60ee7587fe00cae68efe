from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_posta89minimalparameterledger_and_nextfrontier"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostA89MinimalParameterLedger_and_NextFrontier_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    sectors = outputs["sector_ledger"]
    counts = outputs["count_summary"]
    ckm = outputs["CKM_scope"]
    dependencies = outputs["dependencies"]
    plan = outputs["plan"]

    require(all(candidate["checks"].values()), "one or more A90 parameter checks failed")
    require(counts["predecessor_counts"]["non_neutrino_excluding_QCD_theta"] == 18, "old count changed")
    require(counts["current_counts"]["non_neutrino_excluding_QCD_theta"] == 13, "new non-neutrino count")
    require(counts["current_counts"]["minimal_PMNS_excluding_QCD_theta"] == 19, "new PMNS count")
    require(counts["coordinate_reductions"]["gauge_3_to_1"] == 2, "gauge reduction")
    require(counts["coordinate_reductions"]["CKM_4_to_1"] == 3, "CKM reduction")
    require(ckm["A14_result"]["predicted_coordinates"] == ["s12", "s13", "s23"], "CKM angle scope")
    require(not ckm["phase_result"]["accepted_prediction_profile_closed"], "CKM phase overpromoted")
    require(sectors["guardrails"]["P_EW_and_gauge_c_merged"] is False, "P_EW/c merged")
    require(sectors["sector_rows"]["charged_yukawa_magnitudes"]["counted_coordinates"] == 9, "Yukawa count")
    require(dependencies["counts"] == {"closed": 2, "partial": 6, "open_or_dependency_blocked": 1}, "upgrade counts")
    require(plan["ordered_steps"][0]["target"] == "U5 neutral determinant-line phase", "next target")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")
    require(cert["status"] == candidate["status"], "certificate status mismatch")
    require(cert["next_required_artifact"] == candidate["next_required_artifact"], "next artifact mismatch")
    require(NOTE.exists(), "theorem note missing")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
