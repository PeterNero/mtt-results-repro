from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samesourcegaugehessiancrossuse_or_sectorendomorphismvalueemission"
STATUS = "MTT_SELECTED_SAME_SOURCE_GAUGE_HESSIAN_CROSSUSE_TEST_CLOSED_DIRECT_K_PROMOTION_REJECTED_NATIVE_GAUGE_FUNCTIONAL_REMAINS"
NEXT = "MTT_Selected_CircleLensNilGaugeQuadraticFunctional_or_NonUniversalKineticValueRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    crossuse = load(ROOT / "candidate_data" / SLUG / "spectral_action_crossuse_decision.packet.json")
    routes = load(ROOT / "candidate_data" / SLUG / "remaining_gauge_source_routes.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_SameSourceGaugeHessianCrossUse_or_SectorEndomorphismValueEmission_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == routes["next_payload"]["artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "source checks")
    check(crossuse["tree_level_asymptotic_spectral_action"]["selected_GUT_normalized_trace_rows"] == [6.0, 6.0, 6.0], "gauge traces")
    check(not crossuse["tree_level_asymptotic_spectral_action"]["dependence_on_charged_K_threshold_rows"], "cross-use")
    check(crossuse["quantum_mass_threshold_alternative"]["mathematically_legitimate"], "threshold legitimacy")
    check(not crossuse["quantum_mass_threshold_alternative"]["selects_absolute_gauge_boundary_condition"], "boundary overclaim")
    check(cert["direct_K_to_tree_gauge_crossuse_rejected"], "rejection")
    check(cert["native_gauge_functional_rows_emitted"] == 0 and cert["native_gauge_functional_rows_required"] == 3, "row count")
    check(not cert["no_knob_gauge_coupling_prediction_closed"], "prediction overclaim")
    check(cert["new_continuous_parameters"] == 0, "parameter")
    for phrase in ["Direct cross-use test", "promotion is rejected", "Legitimate threshold route", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("same-source gauge Hessian cross-use audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
