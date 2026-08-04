from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugeactioncoefficienttocommonschemecouplingmapandprospectivevalidation"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_GaugeActionCoefficientToCommonSchemeCouplingMapAndProspectiveValidation_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    convention = outputs["convention"]
    reconstruction = outputs["reconstruction"]
    compatibility = outputs["compatibility"]
    prospective = outputs["prospective"]

    require(all(candidate["checks"].values()), "one or more gauge convention checks failed")
    require(convention["theorem"]["proved"], "gauge convention/type separation failed")
    require(not convention["type_separation"]["theorem_equating_P_EW_with_c"], "P_EW incorrectly equated to c")
    require(not convention["type_separation"]["P_EW_times_K_accepted_as_inverse_coupling_rows"], "P_EW*K mispromoted")
    require(reconstruction["theorem"]["proved"], "one-anchor reconstruction failed")
    require(reconstruction["parameter_accounting"]["selected_corpus_action_tier_continuous_gauge_anchors"] == 1, "anchor count changed")
    require(reconstruction["parameter_accounting"]["relative_coordinates_replaced_by_selected_K_shape"] == 2, "relative prediction count changed")
    require(compatibility["compatible_at_current_profile"], "frozen K shape is incompatible with current SMDR profile")
    require(not compatibility["held_out_validation"], "profile replay mislabeled held out")
    require(not prospective["prospective_validation_executed"], "prospective validation falsely executed")
    require(not prospective["current_profile_used_as_prospective_data"], "known profile used prospectively")
    require("no sector-relative counterterm" in prospective["test_protocol"]["no_retuning_rule"], "no-retuning rule missing")
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
