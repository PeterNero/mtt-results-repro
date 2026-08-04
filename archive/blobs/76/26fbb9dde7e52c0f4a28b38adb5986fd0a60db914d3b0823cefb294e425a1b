"""Audit the H K-threshold source object / RG Hessian transport construction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hkthresholdsourceobject_or_rghessiantransportconstruction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
IMPORT_LEDGER = PACKET_DIR / "qa_su3_internal_threshold_import_ledger.packet.json"
RG_TRANSPORT = PACKET_DIR / "h_rg_hessian_transport_source_gate.packet.json"
STRICT_GATE = PACKET_DIR / "strict_h_k_row_gate_after_rg_import.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_h_rg_transport_import.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HKThresholdSourceObject_or_RGHessianTransportConstruction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HKTHRESHOLDSOURCEOBJECT_OR_RGHESSIANTRANSPORTCONSTRUCTION_"
    "QA_INTERNAL_THRESHOLD_IMPORTED_PHYSICAL_RG_OPEN"
)
NEXT = "MTT_Selected_HGaugeKineticNormalizationMuMatch_or_DirectHKThresholdRow_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure flag")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    import_ledger = load(IMPORT_LEDGER)
    rg_transport = load(RG_TRANSPORT)
    strict_gate = load(STRICT_GATE)
    next_cutset = load(NEXT_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("import ledger", import_ledger),
        ("RG transport", rg_transport),
        ("strict gate", strict_gate),
        ("next cutset", next_cutset),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "candidate theorem")
    require(cert["theorem_proved"] is True, "certificate theorem")
    require(data["full_no_knob_closure_claimed"] is False, "candidate no-knob")
    require(data["true_SM_equivalence_claimed"] is False, "candidate true SM")

    decision = data["closure_decision"]
    require(decision["qa_internal_threshold_imported"] is True, "internal threshold imported")
    require(decision["same_scheme_SU2_blocker_retired"] is True, "SU2 blocker retired")
    require(decision["qa_internal_p_a_value"] == 29.201650332199108, "p_a value")
    require(decision["qa_internal_lambda_12_value"] == 2.6179362173268497, "lambda12 value")
    require(decision["qa_internal_Delta_G12_value"] == 0.08450302790361214, "Delta value")
    for key in [
        "physical_gauge_action_anchor_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "selected_R_H_RG_emitted",
        "selected_A_EW_emitted",
        "selected_mu_match_emitted",
        "strict_H_K_threshold_row_emitted",
        "strict_Omega_lambda_scalar_execution_closed",
        "full_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
    require(decision["accepted_selected_K_source_row_count"] == 9, "strict K count")
    require(decision["selected_K_threshold_row_count_required"] == 10, "required K count")

    imported = import_ledger["imported_closures"]
    require(imported["qa_internal_finitepart_p_a_closed"] is True, "import p_a")
    require(imported["same_scheme_SU2_row_or_cancellation_closed"] is True, "import SU2")
    require(imported["internal_lambda_12_closed"] is True, "import lambda12")
    require(imported["typed_hypercharge_map_closed"] is True, "import hypercharge")
    does_not = import_ledger["does_not_close"]
    for key in [
        "physical_gauge_action_anchor",
        "matching_scale_mu_match",
        "RG_scheme",
        "measured_electroweak_closure",
        "strict_H_K_threshold_row",
    ]:
        require(does_not[key] is False, f"import overclosed {key}")

    require(
        rg_transport["status"] == "INTERNAL_THRESHOLD_SUPPORT_CLOSED_PHYSICAL_RG_TRANSPORT_NOT_EMITTED",
        "RG transport status",
    )
    current_rows = rg_transport["current_source_rows"]
    for key in [
        "selected_A_EW",
        "selected_mu_match",
        "selected_R_H_RG",
        "selected_K_threshold_Omega_H_lambda",
    ]:
        require(current_rows[key] is False, f"RG row overclosed {key}")
    for phrase in [
        "selected internal Qa finite part p_a",
        "same-scheme SU2/Qc weak-split rows",
        "internal lambda_12 and Delta_G12",
        "typed hypercharge threshold map",
    ]:
        require(phrase in rg_transport["newly_closed_for_path_2"], f"missing closed phrase {phrase}")
    for phrase in [
        "physical gauge/action normalization K_phys or f_ab",
        "matching scale mu_match",
        "RG and threshold scheme",
        "same-scheme Omega_H.lambda transport certificate",
        "selected R_H^RG determinant/index/provenance row",
    ]:
        require(phrase in rg_transport["still_missing_for_H_transport"], f"missing open phrase {phrase}")

    require(
        strict_gate["status"] == "STRICT_H_ROW_STILL_9_OF_10_AFTER_QA_INTERNAL_RG_IMPORT",
        "strict gate status",
    )
    require(strict_gate["accepted_selected_K_source_row_count"] == 9, "gate K count")
    require(strict_gate["selected_K_threshold_row_count_required"] == 10, "gate required")
    require(strict_gate["strict_H_K_threshold_row_emitted"] is False, "gate H row")
    require(strict_gate["path_2_progress"]["internal_threshold_support_closed"] is True, "path support")
    require(strict_gate["path_2_progress"]["same_scheme_SU2_blocker_retired"] is True, "path SU2")
    require(strict_gate["path_2_progress"]["physical_anchor_RG_blocker_active"] is True, "path physical")
    require(strict_gate["full_no_knob_closed"] is False, "gate no-knob")
    require(strict_gate["true_SM_equivalence_closed"] is False, "gate true SM")

    require(
        next_cutset["status"] == "NEXT_FRONTIER_H_GAUGEKINETIC_MUMATCH_OR_DIRECT_HK_ROW",
        "next cutset status",
    )
    require(next_cutset["next_required_artifact"] == NEXT, "next artifact")
    for phrase in [
        "Qa/SU3 internal finite-part p_a imported",
        "same-scheme SU2 cancellation imported",
        "internal lambda_12/Delta_G12 imported",
        "path #2 reduced to physical gauge kinetic normalization plus mu_match/RG scheme",
    ]:
        require(phrase in next_cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "direct source-native K_threshold.Omega_H.lambda",
        "physical gauge/action normalization K_phys or f_ab",
        "matching scale mu_match",
        "RG and threshold scheme",
        "selected R_H^RG row and same-scheme Omega_H.lambda certificate",
    ]:
        require(phrase in next_cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "HKThresholdSourceObjectOrRGHessianTransportConstructionTheorem",
        "selected internal finite determinant row",
        "The strict row remains `9/10`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: path #2 imported Qa/SU3 internal threshold closure; physical RG/H transport remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
