"""Audit the physical gauge/action anchor or direct H K-row frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_RECHECK = PACKET_DIR / "strict_physical_anchor_and_direct_k_recheck.packet.json"
DIRECT_K_ATTEMPT = PACKET_DIR / "direct_kthreshold_omega_h_lambda_attempt.packet.json"
ONE_PRIMITIVE = PACKET_DIR / "one_physical_action_primitive_fork.packet.json"
SOURCE_TEMPLATE = PACKET_DIR / "same_branch_physical_source_packet_template.packet.json"
NEXT_PACKET = PACKET_DIR / "next_samebranch_action_or_primitive_declaration_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalGaugeActionAnchor_or_DirectKThresholdOmegaHLambda_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_PHYSICALGAUGEACTIONANCHOR_OR_DIRECTKTHRESHOLDOMEGAHLAMBDA_"
    "STRICT_OPEN_ONE_PRIMITIVE_FORK_EXPLICIT"
)
NEXT = "MTT_Selected_SameBranchGaugeActionSource_or_OnePrimitivePolicy_v1"


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
    strict = load(STRICT_RECHECK)
    direct_k = load(DIRECT_K_ATTEMPT)
    one_primitive = load(ONE_PRIMITIVE)
    template = load(SOURCE_TEMPLATE)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("strict", strict),
        ("direct_k", direct_k),
        ("one_primitive", one_primitive),
        ("template", template),
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
    require(decision["strict_fields_filled"] == 1, "strict filled count")
    require(decision["strict_field_count"] == 6, "strict field count")
    require(decision["accepted_physical_prefactor_rows"] == 0, "physical rows overaccepted")
    require(decision["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K overaccepted")
    require(decision["strict_lambda_H_value_row_emitted"] is False, "lambda overemitted")
    require(decision["strict_K_threshold_Omega_H_lambda_emitted"] is False, "K overemitted")
    require(decision["one_physical_action_primitive_fork_available"] is True, "one primitive fork")
    require(decision["one_primitive_parameter_increment_if_adopted"] == 1, "one primitive count")
    require(decision["full_no_knob_closed"] is False, "full no-knob closed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM closed")

    require(strict["strict_fields_filled"] == 1, "strict packet fill")
    require(strict["accepted_physical_prefactor_rows"] == 0, "strict packet prefactor")
    require(strict["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "strict packet K")

    require(direct_k["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct packet K")
    require(direct_k["closed_prerequisites"]["selected_R_H_RG"] is True, "direct packet R_H")
    require(direct_k["missing_for_strict_direct_K"]["selected_A_EW_or_equivalent_prefactor"] is False, "A_EW missing")

    require(one_primitive["primitive_policy"]["allowed_by_current_corpus_packets"] is True, "primitive allowed")
    require(one_primitive["primitive_policy"]["counted_parameter_increment"] == 1, "primitive count")
    require(one_primitive["primitive_policy"]["cannot_be_counted_as_strict_no_knob"] is True, "primitive guard")

    fields = template["required_source_fields"]
    require(len(fields) == 5, "template field count")
    require(sum(1 for field in fields if field["current_fill"]) == 0, "template overfilled")

    for phrase in [
        "PhysicalGaugeActionAnchorOrDirectKThresholdOmegaHLambdaTheorem",
        "physical prefactor rows = 0",
        "direct K_threshold.Omega_H.lambda rows = 0",
        "counted parameter increment = 1",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: physical anchor/direct-K frontier rechecked; strict rows remain "
        "0 while the one-primitive fork is explicit and counted."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
