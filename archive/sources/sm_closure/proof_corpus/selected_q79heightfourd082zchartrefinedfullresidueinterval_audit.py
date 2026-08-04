from __future__ import annotations

import hashlib
import json
from pathlib import Path

from q79_height4_target_refined_full_residue_audit_common import audit_target


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
ADAPTER = ROOT / "scripts" / "certify_q79_height4_d082_zchart_full_residue_interval.py"
DEEP_SEED = (
    ROOT
    / "scripts"
    / "certify_q79_selected_alignment_single_E32_thimble_nodal_factor_deep_seed.py"
)
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD082ZChartRefinedFullResidueInterval_A234_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    summary = audit_target(
        index=82,
        root_id="selected_082",
        coefficient=-2,
        artifact="A234",
        line_chart="z",
    )
    main_packet = load(VALIDATED / "d082.n3.main8.refined.json")
    checkpoint = load(VALIDATED / "d082.n3.main8.refined.checkpoint.json")
    full = load(VALIDATED / "d082.n3.full8.refined.json")
    adapter_hash = sha256(ADAPTER)
    assert checkpoint["line_chart"] == "z"
    assert checkpoint["z_chart_adapter_source_sha256"] == adapter_hash
    assert checkpoint["deep_radial_pair_seed_engine_sha256"] == sha256(DEEP_SEED)
    assert checkpoint["cutoff_pair_zero_based"] == [4, 5]
    assert checkpoint["A123_sha256"] == full["authority"][
        "A123_projective_chart_covariance"
    ]["sha256"]
    assert main_packet["numerics"]["interval_system_diagnostics"][
        "minimum_chart_scale_lower"
    ] > 0.0
    assert main_packet["selected_target"][
        "near_node_colliding_pair_zero_based"
    ] == [4, 5]
    tail_packet = load(VALIDATED / "d082.n3.tail8.refined.json")
    assert tail_packet["selected_target"]["cutoff_pair_zero_based"] == [4, 5]
    assert full["chart_adapter"]["five_period_transition_determinant"] == -1
    assert full["strict_scope"]["A123_projective_z_chart_covariance_consumed"]
    assert full["strict_scope"]["native_z_chart_interval_system_used"]
    note = NOTE.read_text(encoding="utf-8")
    assert "native-z conservative extension" in note
    assert "interval-separated midpoint" in note
    print("q79 A234 d082 z-chart refined full-residue interval audit: PASS")
    print(
        "closed: native-z node/main/tail splice and coefficient-minus-two chain "
        f"ball; max row radius={summary['maximum_full_radius']:.6e}"
    )
    print("open: remaining exact chain, moving handle/beta intervals, and interval Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
