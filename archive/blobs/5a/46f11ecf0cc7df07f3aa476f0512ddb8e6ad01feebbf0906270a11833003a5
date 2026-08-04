from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phic1positivedensitypromotionfromclosedrouteasource_or_strictgaugerows"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiC1PositiveDensityPromotionFromClosedRouteASource_or_StrictGaugeRows_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    gram = outputs["gram_density"]
    promotion = outputs["source_promotion"]
    gauge = outputs["gauge_rows"]
    frontier = outputs["frontier"]

    require(all(candidate["checks"].values()), "one or more PhiC1 promotion checks failed")
    require(gram["theorem"]["proved"], "positive Gram functor lemma failed")
    require(gram["finite_execution"]["positive_semidefinite"], "density is not positive")
    require(promotion["theorem"]["proved"], "PhiC1 source promotion theorem failed")
    require(promotion["promoted_source_status"]["new_source_axiom_used"] is False, "new source axiom introduced")
    require(gauge["acceptance"]["selected_gauge_action_rows_at_corpus_action_tier"] == 3, "three gauge rows not promoted")
    require(gauge["acceptance"]["independent_relative_shape_coordinates"] == 2, "relative gauge rank changed")
    require(gauge["acceptance"]["primitive_MTT_core_no_assumption_gauge_rows"] == 0, "primitive-core tier overclaimed")
    require(not gauge["scope_guard"]["P_EW_times_K_accepted_as_inverse_gauge_couplings"], "P_EW*K misidentified as inverse couplings")
    require(gauge["scope_guard"]["kinetic_normalization_requires_separate_c_equals_6f0_map"], "separate gauge kinetic normalization lost")
    require(frontier["closed_now"]["old_A67_axiom_conditional_density_status_superseded"], "stale A67 condition remains")
    require(len(frontier["not_reopened"]) == 5, "locked result guard changed")
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
