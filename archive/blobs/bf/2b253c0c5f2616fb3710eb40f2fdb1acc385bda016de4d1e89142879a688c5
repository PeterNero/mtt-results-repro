from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from q79_y_chart_conservative_extension import audit_source_compatibility


CANDIDATE = ROOT / "candidate_data" / "selected_q79projectivechartcovariante32intervaladapter.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79projectivechartcovariante32intervaladapter.certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79ProjectiveChartCovariantE32IntervalAdapter_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    compatibility = audit_source_compatibility()
    assert candidate["schema"] == "MTTSelectedQ79ProjectiveChartCovariantE32IntervalAdapter.v1"
    for row in candidate["authority"]:
        path = ROOT / row["path"]
        assert path.exists(), row["path"]
        assert sha256(path) == row["sha256"], row["path"]
    exact = candidate["exact_projective_adapter"]
    assert exact["five_period_transition_determinant"] == -1
    assert not exact["observed_SM_values_used"]
    wall = candidate["z_chart_wall"]
    assert wall["zero_count"] == 3
    assert wall["minimum_pairwise_torus_ball_separation_lower"] > 0.355
    assert wall["minimum_torus_distance_to_critical_balls_lower"] > 0.0159
    row = candidate["first_complete_native_z_row"]
    assert row["artifact"] == "A151"
    assert row["distinguished_index"] == 48
    assert row["coefficient"] == 3
    assert row["tail_segments"] == 384
    assert row["main_accepted_steps"] == 68
    assert row["main_rejected_steps"] == 18
    assert row["full_radius_upper"] < 1.13e-7
    assert row["independent_floating_center_contained"]
    assert row["A134_uniform_fallback_met"]
    provenance = candidate["historical_y_provenance"]
    assert provenance["default_chart_remains_y"]
    assert not provenance["historical_packets_relabelled_as_new_runs"]
    assert provenance["byte_exact_conservative_extension"] == compatibility
    assert compatibility["byte_exact_historical_y_specialization_closed"]
    assert compatibility["reconstructed_historical_y_hashes"][
        "transport_engine"
    ] in provenance["historical_packet_engine_hashes"]
    scope = candidate["scope"]
    assert scope["generic_z_infrastructure_blocker_retired"]
    assert scope["historical_y_source_conservative_extension_closed"]
    assert not scope["all_remaining_z_rows_closed"]
    assert not scope["weighted_71_thimble_interval_closed"]
    assert not scope["fixed_carrier_exact_separation_closed"]
    assert certificate["candidate_sha256"] == sha256(CANDIDATE)
    assert certificate["historical_y_packet_engine_hashes"] == provenance[
        "historical_packet_engine_hashes"
    ]
    assert certificate["current_chart_parametric_engine_sha256"] == provenance[
        "current_chart_parametric_engine_hash"
    ]
    assert certificate["byte_exact_historical_y_specialization_closed"]
    assert certificate["reconstructed_historical_y_source_hashes"] == compatibility[
        "reconstructed_historical_y_hashes"
    ]
    note = NOTE.read_text(encoding="utf-8")
    assert "retires the generic z-chart infrastructure blocker" in note
    assert "byte-certified conservative extension" in note
    assert "not a claim that old packets were rerun" in note
    print("SELECTED_Q79_PROJECTIVE_CHART_COVARIANT_E32_INTERVAL_ADAPTER_AUDIT_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
