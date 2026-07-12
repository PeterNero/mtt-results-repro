from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_su3adjointcentraltrivialfinitegaugerow_and_tenspectrumclosure"
STATUS = "MTT_SELECTED_SU3_ADJOINT_CENTRAL_TRIVIAL_FINITE_ROW_CLOSED_TEN_OF_TEN_COMMON_SPECTRUM_NOGO"
NEXT = "MTT_Selected_NonUniversalGaugeEndomorphismSource_or_CommonSpectrumNoGoFinality_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    packet = load(ROOT / "candidate_data" / SLUG / "su3_finite_row_and_ten_spectrum_closure.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_SU3AdjointCentralTrivialFiniteGaugeRow_and_TenSpectrumClosure_v1.md").read_text(encoding="utf-8")

    check(packet["status"] == cert["status"] == STATUS, "status")
    check(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(packet["checks"].values()), "source check")
    check(cert["SU3_full_row_closed"], "SU3 row")
    check(cert["spectrum_rows_closed"] == cert["spectrum_rows_required"] == 10, "row count")
    check(cert["open_spectrum_rows"] == 0, "open rows")
    check(packet["SU3_gauge_ghost_row"]["kernel_dimension"] == 8, "kernel")
    check(sum(row["multiplicity"] for row in packet["SU3_gauge_ghost_row"]["positive_spectrum"]) == 64, "positive rank")
    check(packet["central_triviality_execution"]["tracefree_commutant_dimension"] == 0, "centrality")
    check(not packet["common_spectrum_consequence"]["adds_independent_threshold_shape"], "shape overclaim")
    check(not cert["strict_spectral_action_closed"] and not cert["no_knob_gauge_coupling_prediction_closed"], "physics overclaim")
    check(cert["new_continuous_parameters"] == 0, "parameter")
    for phrase in ["center acts trivially", "All ten", "matching-scale translation", "does not derive", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("SU3 finite row and ten-spectrum closure audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
