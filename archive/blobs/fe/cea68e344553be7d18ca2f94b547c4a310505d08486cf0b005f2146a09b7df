"""Audit the SM-slot functor overlap-kernel source emission import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "smslotfunctor_overlapkernel_source_emission_import.candidate.json"
CERT = ROOT / "certificates" / "smslotfunctor_overlapkernel_source_emission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "SMSlotFunctor_OverlapKernel_SourceEmission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_smslotfunctor_overlapkernel_source_emission.py"

STATUS = "SMSLOTFUNCTOR_OVERLAPKERNEL_SOURCE_PACKET_IMPORTED_DOWNSTREAM_OPERATOR_PAYLOADS_OPEN"
NEXT = "Selected_U1Y_RouteC_Downstream_OperatorPayload_Ledger_v1"


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
    require(NEXT in note, "note does not name next artifact")

    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "full closure overclaimed")
    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    closed = data["closed_source_fields"]
    for key in [
        "selected_terminal_to_SU5_E6_slot_packet",
        "selected_10M_clock_readout",
        "selected_bar5M_shift_readout",
        "selected_1M_Dirac_shift_readout",
        "selected_U10_Ubar5_source_outputs",
        "selected_overlap_transfer_normalization",
        "same_source_consistency_map",
    ]:
        require(closed[key] is True, f"source field not closed: {key}")

    kernel = data["imported_overlap_kernel"]
    require("rho_s(T_i)/sqrt(2)" in kernel["definition"], "kernel definition mismatch")
    require(kernel["normalization_values"]["matter_triplet_rank"] == 3, "rank mismatch")
    require(kernel["normalization_values"]["eta_00_unit_L2_norm"] == 1, "unit Ext row missing")
    require(kernel["preconditions"]["all_matter_projectors_selected"] is True, "projectors not selected")

    same_source = data["imported_same_source_consistency"]
    require(same_source["selected_same_source_consistency_map"] is True, "same-source map not selected")
    require(same_source["status"] == "EMITTED_SOURCE_ARROW", "same-source arrow not emitted")

    downstream = data["downstream_open_fields"]
    for key in [
        "same_source_D_E_Riesz_Green_dotD",
        "primitive_C1_overlap_contractions",
        "operator_layer_Pic0_recheck",
        "physical_alpha1_driver",
        "Yukawa_CKM_PMNS_masses",
        "full_SM_or_no_knob_closure",
    ]:
        require(downstream[key] is True, f"downstream field should remain open: {key}")

    guardrails = data["guardrails"]
    require(guardrails["does_not_claim_downstream_operator_payloads"] is True, "operator overclaim")
    require(guardrails["does_not_claim_C1_response_or_full_response_matrix"] is True, "C1 overclaim")
    require(guardrails["does_not_claim_Yukawa_CKM_PMNS_masses_or_full_SM"] is True, "SM overclaim")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
