"""Audit H-response row-source emission or direct Herm(2) certificate payload."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hresponserowsourceemission_or_directherm2certificatepayload"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HResponseRowSourceEmission_or_DirectHerm2CertificatePayload_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

MANIFEST = BASE / "row_source_certificate_payload_manifest.packet.json"
SUPPORT = BASE / "certificate_support_imports_rechecked.packet.json"
ATTEMPT = BASE / "primitive_hresponse_source_emission_attempt.packet.json"
CUTSET = BASE / "next_cutset_after_source_certificate_payload.packet.json"

STATUS = (
    "MTT_SELECTED_HRESPONSEROWSOURCEEMISSION_OR_DIRECTHERM2CERTIFICATEPAYLOAD_"
    "SUPPORT_SPLIT_PRIMITIVE_FORMULA_OPEN"
)
NEXT = "MTT_Selected_HuvPrimitiveFormulaOrFiniteErrorBoundExecution_v1"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_no_selector(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label}: observed selector")
    require(packet.get("target_fitting_used") is False, f"{label}: target fitting")


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    manifest = load(MANIFEST)
    support = load(SUPPORT)
    attempt = load(ATTEMPT)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require_no_selector(candidate, "candidate")

    decision = candidate["closure_decision"]
    for key in [
        "payload_manifest_fixed",
        "certificate_support_split_closed",
        "B_Huv_support_imported",
        "current_routes_rechecked",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_primitive_formula_emitted",
        "selected_H_response_value_rows_emitted",
        "direct_Herm2_certificate_payload_emitted",
        "finite_error_bound_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(nums["payload_slots_required"] == 8, "payload slots")
    require(nums["support_slots_available"] == 4, "support slots")
    require(nums["accepted_payload_slot_count"] == 0, "accepted payload")
    require(nums["accepted_value_row_count"] == 0, "accepted values")
    require(nums["accepted_final_certificate_count"] == 0, "accepted certs")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["payload_slots_required"] == 8, "cert payload slots")
    require(cert["support_slots_available"] == 4, "cert support slots")
    for key in [
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "selected_primitive_formula_emitted",
        "selected_H_response_value_rows_emitted",
        "direct_Herm2_certificate_payload_emitted",
        "finite_error_bound_emitted",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(support["status"] == "CERTIFICATE_SUPPORT_IMPORTED_FINAL_ROW_CERTIFICATES_NOT_EMITTED", "support status")
    for value in support["support_closed"].values():
        require(value is True or isinstance(value, dict), "support not closed")
    sdec = support["decision"]
    require(sdec["certificate_support_split_closed"] is True, "support split")
    require(sdec["final_row_source_ownership_certificate_emitted"] is False, "source cert overclosed")
    require(sdec["final_same_source_exactness_or_error_certificate_emitted"] is False, "exactness overclosed")
    require(sdec["final_quotient_admissibility_certificate_emitted"] is False, "quotient overclosed")
    require_no_selector(support, "support")

    require(manifest["status"] == "ROW_SOURCE_CERTIFICATE_PAYLOAD_MANIFEST_FIXED_SUPPORT_SPLIT", "manifest status")
    slots = manifest["required_payload_slots"]
    require(len(slots) == 8, "manifest slot count")
    for row_id in ["Huu", "Hud_re", "Hud_im", "Hdd"]:
        require(slots[row_id]["kind"] == "primitive_value_row", f"value row {row_id}")
        require(slots[row_id]["accepted"] is False, f"value accepted {row_id}")
        require(slots[row_id]["support_available"] is False, f"value support {row_id}")
    for row_id in [
        "Hdu_equals_conj_Hud_certificate",
        "source_ownership_certificate",
        "same_source_exactness_or_error_certificate",
        "quotient_admissibility_certificate",
    ]:
        require(slots[row_id]["accepted"] is False, f"cert accepted {row_id}")
        require(slots[row_id]["support_available"] is True, f"cert support {row_id}")
    mdec = manifest["decision"]
    require(mdec["manifest_fixed"] is True, "manifest fixed")
    require(mdec["support_vs_final_certificate_split_closed"] is True, "split closed")
    require(mdec["accepted_payload_slot_count"] == 0, "manifest accepted")
    require_no_selector(manifest, "manifest")

    require(attempt["status"] == "PRIMITIVE_HRESPONSE_SOURCE_EMISSION_ATTEMPTED_ZERO_VALUES", "attempt status")
    adec = attempt["decision"]
    require(adec["primitive_source_emission_attempted"] is True, "attempted")
    for key in [
        "selected_primitive_formula_emitted",
        "finite_error_bound_emitted",
        "selected_H_response_value_rows_emitted",
        "direct_Herm2_certificate_payload_emitted",
    ]:
        require(adec[key] is False, f"attempt false {key}")
    require(adec["accepted_value_row_count"] == 0, "attempt rows")
    require(adec["accepted_final_certificate_count"] == 0, "attempt certs")
    for value in attempt["emitted_values"].values():
        require(value is None, "attempt value emitted")
    require_no_selector(attempt, "attempt")

    require(cutset["status"] == "NEXT_FRONTIER_HUV_PRIMITIVE_FORMULA_OR_FINITE_ERROR_BOUND_EXECUTION", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "row-source/certificate payload slots fixed",
        "B_Huv quotient/provenance/exactness support separated from final row certificates",
        "current primitive/direct/projection candidate routes rechecked with zero accepted values",
    ]:
        require(phrase in cutset["closed_here"], f"closed {phrase}")
    for phrase in [
        "selected primitive H-sector Hessian or overlap row formula for Huu,Hud_re,Hud_im,Hdd",
        "finite exactness proof or rigorous error bound for those row formulas",
        "same-source owner theorem binding the primitive formula to the selected MTT branch",
    ]:
        require(phrase in cutset["still_open"], f"open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "The certificate layer is now split correctly:",
        "required payload slots: `8`",
        "support slots available: `4`",
        "accepted final payload slots: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: row-source/certificate payload manifest fixed; "
        "B_Huv support split from final row certificates; primitive formula remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
