"""Audit denominator-7 Bergman/HYM structural proof and exactness obstruction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bergmanhymdenominator7_or_exactnessobstruction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DENOMINATOR = PACKET_DIR / "denominator7_structural_count.packet.json"
OBSTRUCTION = PACKET_DIR / "exactness_error_obstruction.packet.json"
NEXT_PACKET = PACKET_DIR / "next_correction_or_exact_operator_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BergmanHYMDenominator7_or_ExactnessObstruction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_BERGMANHYMDENOMINATOR7_OR_EXACTNESSOBSTRUCTION_"
    "DENOMINATOR_STRUCTURED_ERROR_CERTIFICATE_NOT_STRICT_CLOSURE"
)
NEXT = "MTT_Selected_BergmanHYMNextCorrectionOrExactRadialOperator_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    denominator = load(DENOMINATOR)
    obstruction = load(OBSTRUCTION)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("denominator", denominator),
        ("obstruction", obstruction),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    count = denominator["structural_count"]
    require(count["CY_dim"] == 3, "CY dim")
    require(count["End0_rank"] == 3, "End0 rank")
    require(count["trace_unit"] == 1, "trace unit")
    require(count["denominator"] == 7, "denominator")
    require(denominator["denominator_count_identity_proved"] is True, "count identity")
    require(denominator["denominator_as_tau_coefficient_source_proved"] is False, "denominator overpromotion")

    window = denominator["window_count"]
    require(window["bergman_window_2N_plus_1"] == 25, "window numerator")
    require(abs(window["coefficient"] - 25 / 7) < 1e-15, "coefficient")

    require(obstruction["exact_tau_equality_with_25_over_7"] is False, "exactness overclaim")
    require(obstruction["error_certificate_can_close_strict_no_knob"] is False, "error overclaim")
    require(obstruction["accepted_value_source_rows"] == 0, "accepted rows")
    require(obstruction["k_required_for_exact_tau_H"] > obstruction["k_denominator7"], "delta sign")
    require(obstruction["delta_k_required_after_25_over_7"] > 0.008, "delta magnitude")
    require(abs(obstruction["tau_H_absolute_residual"]) > 2e-7, "tau residual nonzero")
    require(obstruction["tau_H_relative_residual"] < 1e-7, "tau residual no longer sharp")
    require(abs(data["numerics"]["r_H_absolute_residual"]) > 2e-5, "r_H residual nonzero")

    require(data["closure_decision"]["denominator_7_structural_count_proved"] is True, "structural count")
    require(data["closure_decision"]["error_certificate_can_close_strict_no_knob"] is False, "strict error")
    require(data["closure_decision"]["accepted_source_rows_total"] == 0, "source rows")

    for phrase in [
        "BergmanHYMDenominator7StructuralCountAndExactnessObstructionTheorem",
        "delta_k",
        "cannot by itself convert a nonzero",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: denominator 7 is structurally proved; "
        "25/7 remains a non-exact value; strict no-knob error closure is rejected."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
