from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_unitinstantonmodalactionquantumbridge_or_twistorcouplingsource"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_UnitInstantonToModalActionQuantumBridge_or_TwistorCouplingSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    factorization = outputs["factorization"]
    source_typing = outputs["source_typing"]
    prequantization = outputs["prequantization"]
    exits = outputs["exit_status"]
    finality = outputs["finality"]

    require(all(candidate["checks"].values()), "one or more instanton-bridge checks failed")
    require(factorization["max_factorization_residual"] < 1e-13, "BPS factorization failed")
    require(not factorization["identifiability"]["positive_c_selected_by_topology"], "topology mispromoted to c")
    require(source_typing["QA_SU3_latest_selected_result"]["selected_value_emitted"], "latest QA result missing")
    require(not source_typing["Q79_integral_candidate"]["selected_visible_source_constructed"], "q79 source overpromoted")
    require(not source_typing["same_source_composition"]["composition_accepted"], "cross-repo type mix accepted")
    require(prequantization["candidate_construction"]["hypothesized_level_N"] == 120.0, "level-120 arithmetic changed")
    require(not prequantization["comparison_to_A87_profile_not_used_as_selector"]["exact_match"], "near-hit mislabeled exact")
    require(not prequantization["decision"]["candidate_promoted"], "level-120 candidate overpromoted")
    require(not prequantization["one_loop_reverse_engineered_scale_diagnostic"]["admissible_as_evidence"], "inverse-fit scale promoted")
    require(exits["accepted_zero_anchor_source_witnesses"] == 0, "unproved zero-anchor witness accepted")
    require(finality["theorem"]["proved"], "one-shared-primitive finality not proved")
    require(finality["accepted_current_standard"]["common_continuous_gauge_anchors"] == 1, "anchor count changed")
    require(not finality["accepted_current_standard"]["strict_zero_anchor_claimed"], "zero anchor overclaimed")
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
