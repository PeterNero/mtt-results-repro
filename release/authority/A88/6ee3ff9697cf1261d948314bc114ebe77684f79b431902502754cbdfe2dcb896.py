from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_commonkineticnormalizationscalesymmetrynogo_and_crosssectoractionexit"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_CommonKineticNormalizationScaleSymmetryNoGo_and_CrossSectorActionExit_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    orbit = outputs["scale_orbit"]
    separation = outputs["type_separation"]
    twistor = outputs["twistor_countermodel"]
    bridge = outputs["cross_sector_bridge"]

    require(all(candidate["checks"].values()), "one or more common-normalization checks failed")
    require(orbit["jacobian_rank"] == 1, "common action-amplitude orbit is not rank one")
    require(orbit["relative_log_projection_rank"] == 0, "common scale leaks into relative ratios")
    require(orbit["max_coupling_ratio_residual"] < 1e-14, "gauge ratios changed along scale orbit")
    require(separation["QG_geometric_measure"]["total_mass"] == 1.0, "QG filter not normalized")
    require(not separation["spectral_action_profile_coordinate"]["direct_identification_mu_QG_equals_mu_spectral_action_selected"], "QG filter mispromoted to spectral action")
    require(not separation["QM_normalization_guard"]["hbar_to_gauge_action_amplitude_source_map_present"], "QM normalization mispromoted")
    require(twistor["corpus_correction"]["correction_required"], "twistor correction not recorded")
    require(twistor["countermodel"]["residual"] < 1e-14, "twistor scaling countermodel failed")
    require(bridge["accepted_source_witness_count"] == 0, "unproved cross-sector witness accepted")
    require(bridge["profile_one_anchor_route_closed"], "current one-anchor route reopened")
    require(not bridge["primitive_zero_anchor_route_closed"], "primitive zero-anchor route overclaimed")
    require(len(bridge["lawful_zero_anchor_exits"]) == 3, "zero-anchor exit inventory changed")
    require(all(not row["accepted_source_witness"] for row in bridge["lawful_zero_anchor_exits"]), "unproved exit promoted")
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
