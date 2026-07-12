"""Audit H-response table value rows or direct Herm(2) value rows packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hresponsetablevaluerows_or_directherm2valuerows"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HResponseTableValueRows_or_DirectHerm2ValueRows_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

TABLE_INTERFACE = BASE / "hresponse_table_value_row_interface.packet.json"
HRESPONSE_ATTEMPT = BASE / "hresponse_value_row_execution_attempt.packet.json"
DIRECT_ATTEMPT = BASE / "direct_herm2_value_row_execution_attempt.packet.json"
SHORTCUTS = BASE / "shortcut_rejection_after_hresponse_value_rows.packet.json"
CUTSET = BASE / "next_cutset_after_hresponse_value_rows.packet.json"

STATUS = (
    "MTT_SELECTED_HRESPONSETABLEVALUEROWS_OR_DIRECTHERM2VALUEROWS_"
    "EXECUTED_ZERO_ROWS_SOURCE_EMISSION_OPEN"
)
NEXT = "MTT_Selected_HResponseRowSourceEmission_or_DirectHerm2CertificatePayload_v1"


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
    interface = load(TABLE_INTERFACE)
    hresponse = load(HRESPONSE_ATTEMPT)
    direct = load(DIRECT_ATTEMPT)
    shortcuts = load(SHORTCUTS)
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
        "active_domain_imported",
        "hresponse_table_interface_fixed",
        "direct_Herm2_interface_fixed",
        "hresponse_table_execution_attempted",
        "direct_Herm2_value_row_execution_attempted",
        "shortcut_recheck_executed",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "selected_H_response_table_emitted",
        "selected_H_response_spectrum_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "Huv_values_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "source_ownership_certificate_emitted",
        "same_source_exactness_or_error_certificate_emitted",
        "quotient_admissibility_certificate_emitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(nums["required_H_response_table_row_or_certificate_count"] == 7, "H response required")
    require(nums["accepted_H_response_source_row_count"] == 0, "H response accepted")
    require(nums["emitted_H_response_table_row_count"] == 0, "H response emitted")
    require(nums["required_direct_Herm2_row_or_certificate_count"] == 8, "direct required")
    require(nums["accepted_direct_Herm2_row_or_certificate_count"] == 0, "direct accepted")
    require(nums["emitted_direct_Herm2_row_or_certificate_count"] == 0, "direct emitted")
    require(nums["accepted_value_source_routes"] == 0, "route accepted")
    require(nums["accepted_shortcut_value_sources"] == 0, "shortcut accepted")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(cert["required_H_response_table_row_or_certificate_count"] == 7, "cert H response required")
    require(cert["accepted_H_response_source_row_count"] == 0, "cert H response accepted")
    require(cert["required_direct_Herm2_row_or_certificate_count"] == 8, "cert direct required")
    require(cert["accepted_direct_Herm2_row_or_certificate_count"] == 0, "cert direct accepted")
    for key in [
        "true_SM_equivalence_claimed",
        "full_no_knob_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
        "selected_H_response_table_emitted",
        "selected_Hermitian_M_source_emitted",
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "source_ownership_certificate_emitted",
        "same_source_exactness_or_error_certificate_emitted",
        "quotient_admissibility_certificate_emitted",
    ]:
        require(cert[key] is False, f"cert false {key}")

    require(interface["status"] == "HRESPONSE_AND_DIRECT_HERM2_VALUE_ROW_INTERFACES_FIXED", "interface status")
    require(interface["active_domain_imports"]["M_source_contract_reconciled"] is True, "M source imported")
    require(interface["active_domain_imports"]["B_Huv_R_H_domain_available"] is True, "domain imported")
    require(interface["active_domain_imports"]["Herm2_row_extractors_closed"] is True, "extractors imported")
    require(interface["hresponse_table_interface"]["required_row_count"] == 7, "interface H rows")
    require(interface["direct_herm2_interface"]["required_row_or_certificate_count"] == 8, "interface direct rows")
    require(interface["decision"]["basis_domain_blocker_remaining"] is False, "domain reopened")
    require(interface["decision"]["value_row_source_emission_required"] is True, "source emission not required")
    require_no_selector(interface, "interface")

    expected_hresponse = {
        "Huu",
        "Hud_re",
        "Hud_im",
        "Hdd",
        "source_ownership_certificate",
        "same_source_exactness_or_error_certificate",
        "quotient_admissibility_certificate",
    }
    require(set(interface["hresponse_table_interface"]["required_rows"]) == expected_hresponse, "H row ids")
    expected_direct = {
        "Hdd",
        "Hdu_equals_conj_Hud_certificate",
        "Hud_im",
        "Hud_re",
        "Huu",
        "quotient_admissibility_certificate",
        "same_source_exactness_or_error_certificate",
        "source_ownership_certificate",
    }
    require(set(interface["direct_herm2_interface"]["required_rows"]) == expected_direct, "direct row ids")

    require(hresponse["status"] == "HRESPONSE_TABLE_VALUE_ROW_EXECUTION_ZERO_ACCEPTED_ROWS", "H status")
    hdec = hresponse["decision"]
    require(hdec["execution_attempted"] is True, "H attempted")
    require(hdec["required_row_count"] == 7, "H required")
    require(hdec["accepted_source_row_count"] == 0, "H accepted")
    require(hdec["emitted_row_count"] == 0, "H emitted")
    for value in hresponse["computed_values"].values():
        require(value is None, "H value emitted")
    require(hdec["selected_H_response_table_emitted"] is False, "H table emitted")
    require(hdec["selected_H_response_spectrum_emitted"] is False, "spectrum emitted")
    require(hdec["selected_logdet_from_H_response_emitted"] is False, "logdet emitted")
    require(hdec["source_ownership_certificate_emitted"] is False, "H owner cert")
    require_no_selector(hresponse, "hresponse")

    require(direct["status"] == "DIRECT_HERM2_VALUE_ROW_EXECUTION_ZERO_ACCEPTED_ROWS", "direct status")
    ddec = direct["decision"]
    require(ddec["execution_attempted"] is True, "direct attempted")
    require(ddec["required_row_count"] == 8, "direct required")
    require(ddec["accepted_row_count"] == 0, "direct accepted")
    require(ddec["emitted_row_count"] == 0, "direct emitted")
    for value in direct["computed_values"].values():
        require(value is None, "direct value emitted")
    for key in [
        "direct_Huu_Hud_Hdd_emitted",
        "direct_Herm2_Huv_payload_emitted",
        "source_ownership_certificate_emitted",
        "same_source_exactness_or_error_certificate_emitted",
        "quotient_admissibility_certificate_emitted",
        "selected_Hermitian_M_source_emitted",
        "M_source_plus_R_H_values_emitted",
        "Huv_values_emitted",
    ]:
        require(ddec[key] is False, f"direct false {key}")
    require_no_selector(direct, "direct")

    require(shortcuts["status"] == "SHORTCUTS_RECHECKED_NOT_VALUE_ROW_SOURCES", "shortcut status")
    require(len(shortcuts["rows"]) == 6, "shortcut count")
    for row in shortcuts["rows"]:
        require(row["accepted_as_value_row_source"] is False, f"shortcut accepted {row['candidate_id']}")
    require(shortcuts["decision"]["accepted_shortcut_value_sources"] == 0, "shortcut accepted count")
    require_no_selector(shortcuts, "shortcuts")

    require(
        cutset["status"]
        == "NEXT_FRONTIER_HRESPONSE_ROW_SOURCE_EMISSION_OR_DIRECT_HERM2_CERTIFICATE_PAYLOAD",
        "cutset status",
    )
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "H_response table value-row interface fixed and executed",
        "direct Herm(2) Huv row/certificate interface fixed and executed",
        "active B_Huv/R_H/M_source domain imported without reopening old domain blockers",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed {phrase}")
    for phrase in [
        "selected primitive source rows for Huu,Hud_re,Hud_im,Hdd",
        "source ownership certificate for the H-response/direct Herm(2) rows",
        "same-source exactness or finite error certificate",
        "quotient admissibility certificate for the light line",
    ]:
        require(phrase in cutset["still_open"], f"cutset open {phrase}")
    require_no_selector(cutset, "cutset")

    for phrase in [
        "The remaining gate is the value-row source itself.",
        "required `H_response` table rows/certificates: `7`",
        "accepted `H_response` rows/certificates: `0`",
        "required direct Herm(2) rows/certificates: `8`",
        "accepted direct Herm(2) rows/certificates: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: H-response/direct Herm(2) value-row interfaces executed; "
        "zero accepted rows; primitive source/certificate payload remains."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
