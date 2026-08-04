from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_propertimemeasureandoverlapkineticmetricsource_or_strictspectralactionclosure"
STATUS = "MTT_SELECTED_TAUINT_POINT_MEASURE_CONDITIONAL_MOMENTS_CLOSED_SCALAR_MEASURE_CANNOT_SOURCE_KGAUGE_RANK_METRIC_REJECTED"
NEXT = "MTT_Selected_GaugeOverlapMetricFromLiteralHYMConnections_or_StrictSpectralActionClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "proper_time_atom_and_overlap_source_cutset.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_ProperTimeMeasureAndOverlapKineticMetricSource_or_StrictSpectralActionClosure_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(cert["tau_int_exact_source_available"] is True, "tau_int missing")
    require(cert["minimal_point_measure_moments_closed_conditionally"] is True, "point moments failed")
    require(cert["point_measure_selected_by_MTT"] is False, "conditional measure promoted")
    require(cert["scalar_measure_cannot_source_overlap_ratios"] is True, "factorization no-go failed")
    require(cert["native_rank_metric_rejected_as_exact_source"] is True, "rank near-hit promoted")
    require(cert["remaining_overlap_source_ratios"] == 2, "remaining ratio count changed")
    require(cert["strict_spectral_action_closed"] is False, "strict closure overclaimed")
    require(cert["new_continuous_parameters"] == 0, "new parameter introduced")
    require(packet["proper_time_candidate"]["moment_Hankel_rank"] == 1, "point moment rank changed")
    require(packet["overlap_metric_tests"]["best_log_residual"] > 1e-3, "rank metric became exact")
    for phrase in ["zero-new-scale/minimal-support premise", "not a selected MTT theorem", "cannot fix the gauge metric", "close but not exact", "rejected", "only numerical source object", NEXT]:
        require(phrase.lower() in note.lower(), f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("proper-time and overlap-source cutset audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
