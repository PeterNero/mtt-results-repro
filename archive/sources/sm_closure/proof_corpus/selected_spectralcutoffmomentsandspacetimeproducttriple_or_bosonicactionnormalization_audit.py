from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization"
STATUS = "MTT_PRODUCT_TRIPLE_PROFILE_MATTER_NORMALIZATION_CLOSED_OVERLAP_METRIC_EXACT_UNIVERSAL_SPECTRAL_MOMENT_CLAIM_BLOCKED_BY_GAUGE_NOGO"
NEXT = "MTT_Selected_ProperTimeMeasureAndOverlapKineticMetricSource_or_StrictSpectralActionClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "product_triple_profile_normalization_and_moment_nogo.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_SpectralCutoffMomentsAndSpacetimeProductTriple_or_BosonicActionNormalization_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(cert["profile_product_triple_interface_closed"] is True, "profile product triple open")
    require(cert["profile_bosonic_matter_normalization_closed"] is True, "profile matter normalization open")
    require(cert["universal_f0_gauge_normalization_no_go_proved"] is True, "universal no-go failed")
    require(cert["profile_overlap_metric_exact"] is True, "overlap metric reconstruction failed")
    require(cert["profile_overlap_relative_coordinates"] == 2, "profile coordinate count changed")
    require(cert["new_parameters_beyond_SM_profile"] == 0, "new profile parameter added")
    require(cert["strict_spectral_cutoff_moments_closed"] is False, "moments overclaimed")
    require(cert["strict_MTT_Wick_rotation_closed"] is False, "Wick rotation overclaimed")
    require(cert["old_5TeV_chain_used"] is False, "retired 5 TeV chain reused")
    require(packet["minimal_profile_normalization"]["residual"] < 1e-12, "profile normalization residual failed")
    require(packet["universal_gauge_relation_test"]["best_max_over_min"] > 1.04, "universal mismatch disappeared")
    require(packet["universal_gauge_relation_test"]["archived_SMDR_multiloop_grid_crosscheck"]["max_over_min"] > 1.04, "multiloop mismatch disappeared")
    for phrase in ["Universal Spectral Normalization No-Go", "larger than four percent", "Exact Profile Exit", "add zero parameters", "old `5 TeV` calibration is", "not closed", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("spectral cutoff/product-triple normalization audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
