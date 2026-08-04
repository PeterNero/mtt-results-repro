"""Audit A_EW source-operator / threshold-convention row validator."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_aewsourceoperator_or_thresholdconventionrows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TEMPLATE = PACKET_DIR / "aew_source_operator_threshold_convention_template.packet.json"
VALIDATION = PACKET_DIR / "current_packet_fill_validation.packet.json"
DEEP_SEARCH = PACKET_DIR / "expanded_source_expression_search_with_physical_anchor_symbols.packet.json"
NEXT_PACKET = PACKET_DIR / "next_physical_action_anchor_or_direct_krow_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AEWSourceOperator_or_ThresholdConventionRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_AEWSOURCEOPERATOR_OR_THRESHOLDCONVENTIONROWS_"
    "VALIDATOR_BUILT_CURRENT_PACKETS_FILL_ZERO_PHYSICAL_PREFACTOR_ROWS"
)
NEXT = "MTT_Selected_PhysicalGaugeActionAnchor_or_DirectKThresholdOmegaHLambda_v1"


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
    template = load(TEMPLATE)
    validation = load(VALIDATION)
    deep_search = load(DEEP_SEARCH)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("template", template),
        ("validation", validation),
        ("deep_search", deep_search),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "next artifact")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    decision = data["closure_decision"]
    require(decision["selected_R_H_RG_source_emitted"] is True, "R_H source")
    require(decision["H_parameter_count_after_replacement"] == 0, "H parameter count")
    require(decision["aew_source_operator_template_built"] is True, "template")
    require(decision["required_fields_filled_by_current_packets"] == 2, "filled count")
    require(decision["required_field_count"] == 7, "required count")
    require(decision["accepted_A_EW_source_operator_rows"] == 0, "A_EW overaccepted")
    require(decision["accepted_threshold_convention_rows"] == 0, "threshold overaccepted")
    require(decision["accepted_physical_prefactor_rows"] == 0, "physical prefactor overaccepted")
    require(decision["expanded_search_exact_hits_found"] == 0, "unexpected exact hit")
    require(decision["strict_lambda_H_value_row_emitted"] is False, "lambda overemitted")
    require(decision["strict_K_threshold_Omega_H_lambda_emitted"] is False, "K overemitted")

    require(template["required_field_count"] == 7, "template count")
    require(template["required_fields_filled_by_current_packets"] == 2, "template fill count")
    require(template["physical_prefactor_fields_filled_by_current_packets"] == 0, "template prefactor count")

    require(validation["accepted_A_EW_source_operator_rows"] == 0, "validation A_EW")
    require(validation["accepted_threshold_convention_rows"] == 0, "validation threshold")
    require(validation["accepted_physical_prefactor_rows"] == 0, "validation prefactor")
    require(validation["closed_support"]["H_parameter_count_after_replacement"] == 0, "validation H count")

    require(deep_search["exact_hits_found"] == 0, "deep exact hits")
    require(deep_search["accepted_selected_expression_rows"] == 0, "deep accepted")
    require(deep_search["best_expression_rows"][0]["relative_residual"] > 0, "best exact")
    require(deep_search["best_expression_rows"][0]["relative_residual"] < 1e-3, "best too weak")

    for phrase in [
        "AEWSourceOperatorThresholdConventionValidatorTheorem",
        "Accepted A_EW source rows: `0`",
        "Accepted threshold convention rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: A_EW source-operator validator built; current packets fill "
        "selected R_H/internal support but zero physical prefactor rows."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
