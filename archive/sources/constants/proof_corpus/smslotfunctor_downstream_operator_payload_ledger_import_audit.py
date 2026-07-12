"""Audit the SM-slot functor downstream operator-payload ledger import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "smslotfunctor_downstream_operator_payload_ledger_import.candidate.json"
CERT = ROOT / "certificates" / "smslotfunctor_downstream_operator_payload_ledger_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "SMSlotFunctor_DownstreamOperatorPayload_Ledger_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_smslotfunctor_downstream_operator_payload_ledger.py"

STATUS = "SMSLOTFUNCTOR_DOWNSTREAM_LEDGER_IMPORTED_STATIC_PROMOTED_DYNAMIC_OPEN"
NEXT = "Selected_U1Y_RouteC_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    route = data["static_sector_route"]
    require(route["phase_route"] == ["u", "e"], "phase route mismatch")
    require(route["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(route["conditional_A_weylpair_exact"] is True, "conditional A not exact")
    require(route["promote_conditional_A_to_A_selected"] is False, "A_selected overclaimed")

    dynamic = data["dynamic_payloads_still_open"]
    for key in [
        "dynamic_visible_routec_operator_source_identity",
        "selected_D_E_Riesz_Green_dotD",
        "physical_alpha1_driver",
        "selected_dynamic_overlap_tensor_or_transfer_functor",
        "selected_primitive_C1_contractions",
        "selected_b_selected_and_Hessian_normalization",
        "promote_conditional_A_to_A_selected",
        "Yukawa_CKM_PMNS_masses_Higgs_RG",
        "full_SM_or_no_knob_closure",
    ]:
        require(dynamic[key] is True, f"dynamic blocker missing: {key}")

    guardrails = data["guardrails"]
    require(guardrails["selected_static_payloads_claimed"] is True, "static payloads not claimed")
    require(guardrails["dynamic_operator_payloads_claimed"] is False, "dynamic payload overclaim")
    require(guardrails["A_selected_claimed"] is False, "A_selected overclaim")
    require(guardrails["b_selected_claimed"] is False, "b_selected overclaim")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
