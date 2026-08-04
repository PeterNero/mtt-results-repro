from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_su2transportclosedfinitegaugerow_and_su3nativecolorsourcereduction"
STATUS = "MTT_SELECTED_SU2_TRANSPORT_FINITE_GAUGE_ROW_CLOSED_NINE_OF_TEN_SU3_NATIVE_COLOR_SOURCE_REDUCED"
NEXT = "MTT_Selected_SU3NativeColorAdjointNilHodgeSourceIdentity_or_NewEndomorphismOperator_v1"


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
    packet = load(ROOT / "candidate_data" / SLUG / "su2_row_closure_and_su3_source_reduction.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_SU2TransportClosedFiniteGaugeRow_and_SU3NativeColorSourceReduction_v1.md").read_text(encoding="utf-8")

    check(packet["status"] == cert["status"] == STATUS, "status mismatch")
    check(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next mismatch")
    check(all(packet["checks"].values()), "one or more source checks failed")
    check(cert["SU2_full_row_closed"] and not cert["SU3_full_row_closed"], "row boundary")
    check(cert["spectrum_rows_closed"] == 9 and cert["final_open_row_obligations"] == 1, "frontier count")
    check(packet["SU2_gauge_ghost_row"]["kernel_dimension"] == 3, "SU2 kernel")
    check(sum(row["multiplicity"] for row in packet["SU2_gauge_ghost_row"]["positive_spectrum"]) == 24, "SU2 positive rank")
    check(packet["heterotic_printed_route_audit"]["unique_minimal_repair"][0]["formula"] == "-E32", "repair")
    check(packet["heterotic_printed_route_audit"]["holomorphic_commutant_dimension"] == 2, "commutant")
    check(not packet["withdrawn_numeric_guard"]["usable_as_selected_SU3_metric"], "withdrawn scale promoted")
    check(packet["epistemic_policy"]["new_continuous_parameters"] == 0, "new parameter")
    for phrase in ["transport-closed finite quotient", "complex-gauge orbit", "withdrawn 5 TeV", "Exactly one spectrum row", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("SU2 row closure and SU3 source reduction audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
