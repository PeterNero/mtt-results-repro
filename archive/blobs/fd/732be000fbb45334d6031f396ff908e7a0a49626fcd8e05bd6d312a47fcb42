"""Audit downstream operator-payload ledger after SM-slot functor closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
CERT = ROOT / "certificates" / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SelectedSMSlotFunctor_DownstreamOperatorPayloads_or_SMParityLedger_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.py"

STATUS = (
    "MTT_SELECTED_SMSLOTFUNCTOR_DOWNSTREAM_PAYLOAD_LEDGER_BUILT_"
    "STATIC_FIELDS_PROMOTED_DYNAMIC_C1_OPEN"
)
NEXT = "MTT_Selected_DynamicOverlapKernel_or_C1Primitive_SourceEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note does not record next artifact")

    tiers = data["payload_tiers"]
    require(tiers["static_sm_slot_tier"]["closed"] is True, "static tier not closed")
    require(tiers["dynamic_operator_c1_tier"]["closed"] is False, "dynamic tier overclosed")

    fields = data["old_contract_reclassification"]
    require(fields["matter_slot_charge"]["static_selected_emitted"] is True, "matter slot not statically promoted")
    require(
        fields["matter_slot_charge"]["c1_sector_route_independent_of_locked_target"] is True,
        "static sector route not independent of locked target",
    )
    require(fields["singlet_neutrino_rule"]["static_selected_emitted"] is True, "1M rule not statically promoted")
    require(
        fields["overlap_transfer"]["static_finite_transfer_selected"] is True,
        "static finite transfer not selected",
    )
    require(
        fields["overlap_transfer"]["dynamic_source_to_C1_transfer_functor_selected"] is False,
        "dynamic transfer overclaimed",
    )
    require(
        fields["normalization"]["static_trace_innerproduct_normalization_selected"] is True,
        "static normalization not selected",
    )
    require(
        fields["normalization"]["dynamic_hessian_or_b_selected_normalization_selected"] is False,
        "dynamic Hessian normalization overclaimed",
    )
    require(fields["operator_values"]["dynamic_selected_emitted"] is False, "operator values overclaimed")
    require(
        fields["primitive_contractions"]["dynamic_selected_emitted"] is False,
        "primitive contractions overclaimed",
    )

    effect = data["old_contract_effect"]
    require(effect["previous_required_fields"] == 7, "old contract required-field count mismatch")
    require(effect["previous_selected_emitted"] == 0, "old contract unexpectedly had selected fields")
    require(effect["current_validator_promotion_allowed"] is False, "validator promotion overclaimed")

    weyl = data["weylpair_consequence"]
    require(weyl["source_level_ZX_carrier_closed"] is True, "ZX carrier not imported")
    require(weyl["conditional_transfer_exact"] is True, "conditional transfer not exact")
    require(weyl["conditional_A_weylpair_exact"] is True, "conditional A not exact")
    require(weyl["selected_static_sector_route_now_closed"] is True, "static sector route not closed")
    require(weyl["phase_route"] == ["u", "e"], "phase route mismatch")
    require(weyl["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(weyl["promote_conditional_A_to_A_selected"] is False, "A_selected overclaimed")

    require(data["closure_claimed"] is False, "full closure overclaimed")
    require(data["selected_static_payloads_claimed"] is True, "static payload closure not claimed")
    require(data["dynamic_operator_payloads_claimed"] is False, "dynamic payload closure overclaimed")
    require(data["A_selected_claimed"] is False, "A_selected overclaimed")
    require(data["b_selected_claimed"] is False, "b_selected overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not marked proved")
    require(cert["theorem_proved"] is True, "certificate theorem not marked proved")

    remains = data["what_remains_open"]
    for key in [
        "selected_D_E_Riesz_Green_dotD",
        "physical_alpha1_driver",
        "selected_dynamic_overlap_tensor_or_transfer_functor",
        "selected_primitive_C1_contractions",
        "selected_b_selected_and_Hessian_normalization",
        "promote_conditional_A_to_A_selected",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
