"""Audit Step59 higher-response contract import / payload execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step59_higherresponse_contract_import_or_payloadexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT_PACKET = PACKET_DIR / "step59_higherresponse_contract_import.packet.json"
CUTSET = PACKET_DIR / "step59_next_payloadexecution_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step59_HigherResponseContractImport_or_PayloadExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP59_HIGHER_RESPONSE_CONTRACT_IMPORTED_PAYLOAD_EXECUTION_OPEN"
NEXT = "MTT_Selected_DynamicPhiFinC1PayloadRows_or_HigherResponseExecution_v1"


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
    for item in [data, packet, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(packet["higher_response_Rtheta_functional_contract_closed"] is True, "contract not closed")
    require(packet["codomain_scalar_row_count"] == 10, "scalar count mismatch")
    require(packet["codomain_scalar_rows"][-1] == "lambda_H", "lambda_H missing")
    require(packet["execution_inputs_available_now"] is False, "execution inputs overclaimed")
    require(packet["selected_functional_executed"] is False, "functional overexecuted")
    require(packet["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")
    require(packet["source_anchor_theorem_closed"] is False, "source anchor overclosed")
    require(packet["selected_universal_parameter_count"] == 0, "universal parameter overselected")
    require(cutset["closed_now"]["ten_scalar_row_target_fixed"] is True, "ten-row target missing")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")

    decision = data["closure_decision"]
    require(decision["higher_response_Rtheta_functional_contract_closed"] is True, "decision contract missing")
    require(decision["codomain_scalar_row_count"] == 10, "decision scalar count mismatch")
    require(decision["accepted_scalar_row_count_now"] == 0, "decision scalar rows overaccepted")
    require(decision["selected_universal_parameter_count"] == 0, "decision universal parameter overselected")
    for key in [
        "higher_response_payload_rows_emitted",
        "higher_response_Rtheta_executed",
        "source_anchor_theorem_closed",
        "no_knob_value_derivation_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"candidate overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    for phrase in [
        "higher-response contract closed        : true",
        "scalar output rows                     : 10",
        "dynamic Phi_fin/C1 payload emitted     : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
