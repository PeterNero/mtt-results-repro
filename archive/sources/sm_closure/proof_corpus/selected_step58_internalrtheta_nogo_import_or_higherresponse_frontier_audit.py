"""Audit Step58 internal Rtheta no-go import / higher-response frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step58_internalrtheta_nogo_import_or_higherresponse_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT_PACKET = PACKET_DIR / "step58_internal_rtheta_nogo_import.packet.json"
CUTSET = PACKET_DIR / "step58_next_higherresponse_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step58_InternalRThetaNoGoImport_or_HigherResponseFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP58_INTERNAL_RTHETA_NOGO_IMPORTED_HIGHER_RESPONSE_REQUIRED"
NEXT = "MTT_Selected_HigherResponseRThetaFunctional_or_SourceAnchorTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    packet = load(IMPORT_PACKET)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    for item in [data, packet, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(packet["dynamic_first_response_layer_closed"] is True, "first response not closed")
    require(packet["dynamic_normal_form_rank"] == 2, "rank mismatch")
    require(packet["scalar_target_slot_count"] == 10, "scalar target mismatch")
    require(packet["accepted_selected_coefficient_rows"] == 0, "coefficient rows overaccepted")
    require(packet["first_response_sufficient_for_no_knob_value_rows"] is False, "first response overaccepted")
    require(packet["minimal_universal_parameter_selected"] is False, "minimal parameter overselected")
    require(packet["selected_higher_response_or_retarded_kernel_derivative_required"] is True, "higher response not required")
    require(cutset["closed_now"]["first_response_only_route_rejected_for_scalar_no_knob_values"] is True, "cutset no-go missing")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")

    decision = data["closure_decision"]
    require(decision["dynamic_first_response_layer_closed"] is True, "decision dynamic layer missing")
    require(decision["first_response_only_route_rejected_for_scalar_no_knob_values"] is True, "decision no-go missing")
    require(decision["accepted_internal_Rtheta_coefficient_row_count"] == 0, "internal rows overaccepted")
    require(decision["selected_universal_parameter_count"] == 0, "universal parameter overselected")
    for key in [
        "minimal_universal_parameter_selection_closed",
        "no_knob_value_derivation_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    for phrase in [
        "dynamic normal-form rank                : 2",
        "scalar target slots                     : 10",
        "accepted internal Rtheta rows           : 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
