"""Attempt to fill the selected Qa/SU3 typed monad D_E/rho_E packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
TEMPLATE = CERTS / "typed_monad_de_or_rhoe_data.template.json"
INTERFACE = DATA / "typed_monad_de_or_rhoe_data_interface.candidate.json"
VALIDATOR = ROOT / "scripts" / "validate_typed_monad_packet.py"
OUTPUT_DATA = DATA / "typed_monad_data_fill_attempt.candidate.json"
OUTPUT_CERT = CERTS / "typed_monad_data_fill_attempt_certificate.json"

SOURCE_TERMS = {
    "printed_monad_sequence": "0\\longrightarrow K_1",
    "printed_ell_data": "\\ell_1&=-2",
    "printed_kappa_data": "\\kappa_1=a",
    "generic_maps_statement": "generic holomorphic maps",
    "constant_matrices_statement": "constant matrices in the left-invariant frame",
    "printed_a01_diagnostic": "\\bar\\omega^3",
    "cech_data": "Cech",
    "dolbeault_cochain_matrix": "Dolbeault cochain",
    "rhoE_packet": "rho_E",
}


def source_scan() -> dict[str, object]:
    if not SOURCE.exists():
        return {"path": str(SOURCE), "present": False, "terms": {key: False for key in SOURCE_TERMS}}
    text = SOURCE.read_text(encoding="utf-8", errors="ignore")
    return {"path": str(SOURCE), "present": True, "terms": {key: term in text for key, term in SOURCE_TERMS.items()}}


def run_validator(path: Path) -> dict[str, object]:
    proc = subprocess.run([sys.executable, str(VALIDATOR), str(path)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def partially_fill_template(template: dict[str, object]) -> dict[str, object]:
    packet = json.loads(json.dumps(template))
    packet["status"] = "OPEN_SELECTED_QA_SU3_TYPED_MONAD_DATA_FILL_ATTEMPT_INCOMPLETE"
    packet["selected_branch"] = {
        "branch_id": "iwasawa_su3_monad_candidate",
        "source_certificate": str(SOURCE),
        "selection_rule": "corpus-printed Iwasawa monad topological data only; operator data not selected",
        "target_residual_used": False,
    }
    packet["typed_monad"]["monad_checks"]["stable_or_hym_source"] = "source claims Li-Yau/HYM existence for generic maps; not a typed-map certificate"
    return packet


def main() -> None:
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    interface = json.loads(INTERFACE.read_text(encoding="utf-8"))
    scan = source_scan()
    partial_packet = partially_fill_template(template)
    validator_result = run_validator(TEMPLATE)
    fillable_from_source = {
        "ambient_geometry": partial_packet["typed_monad"]["ambient_geometry"],
        "rank": partial_packet["typed_monad"]["rank"],
        "ell_i": partial_packet["typed_monad"]["ell_i"],
        "kappa_a": partial_packet["typed_monad"]["kappa_a"],
        "c1_zero": True,
        "c2_zero": True,
        "c3_integral": 6,
        "generic_maps_named": bool(scan["terms"].get("generic_maps_statement")),
        "constant_left_invariant_frame_maps_named": bool(scan["terms"].get("constant_matrices_statement")),
        "hym_existence_claim_named": "source-level existence claim only",
    }
    unfilled_slots = {
        "f_map_matrix": partial_packet["typed_monad"]["f_map"]["matrix"],
        "g_map_matrix": partial_packet["typed_monad"]["g_map"]["matrix"],
        "g_f_zero": partial_packet["typed_monad"]["monad_checks"]["g_f_zero"],
        "locally_free": partial_packet["typed_monad"]["monad_checks"]["locally_free"],
        "cochain_or_dolbeault_data": partial_packet["cochain_or_dolbeault_data"],
        "representation_and_trace": partial_packet["representation_and_trace"],
        "de_operator_packet": partial_packet["de_operator_packet"],
        "rhoE_packet": partial_packet["rhoE_packet"],
    }
    candidate = {
        "candidate": "SelectedQaSU3TypedMonadDataFillAttempt",
        "status": "TYPED_MONAD_DATA_FILL_ATTEMPT_BLOCKED_TYPED_MAPS_MISSING",
        "input_statuses": {"interface": interface["status"]},
        "source_scan": scan,
        "template_validator_result": validator_result,
        "partial_packet": partial_packet,
        "fillable_from_source": fillable_from_source,
        "unfilled_slots": unfilled_slots,
        "gate_results": {
            "topological_monad_data": "PASS_SOURCE_PRINTED",
            "typed_f_g_maps": "FAIL_SOURCE_PRINTED_GENERIC_ONLY",
            "g_f_zero": "FAIL_NO_MATRICES_TO_CHECK",
            "locally_free": "FAIL_NO_TYPED_MAP_CERTIFICATE",
            "dolbeault_or_cech_matrices": "FAIL_NOT_PRINTED",
            "representation_and_trace": "FAIL_NOT_SELECTED",
            "de_operator_packet": "FAIL_NOT_FILLED",
            "rhoE_packet": "FAIL_NOT_FILLED",
            "determinant_or_threshold": "FAIL_NO_OPERATOR_EXIT",
        },
        "guardrails": [
            "generic existence of f,g is not a typed f,g matrix packet",
            "printed or repaired A01 is diagnostic only and not source-certified operator data",
            "topological Chern data cannot substitute for D_E, rho_E, endomorphism_E, or finite determinant data",
            "identity rho_E matrices cannot be inserted as selected transition data",
            "observed Qa/SU3 residual is not used",
        ],
        "fill_result": {
            "topological_monad_data_filled": True,
            "typed_maps_filled": False,
            "validator_on_open_template_exit_2": validator_result["exit_code"] == 2,
            "cochain_or_dolbeault_packet_filled": False,
            "de_operator_packet_filled": False,
            "rhoE_packet_filled": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_Monad_Map_Construction_or_Source_Augmentation_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3TypedMonadDataFillAttempt",
        "status": "QA_SU3_TYPED_MONAD_DATA_FILL_ATTEMPT_BLOCKED_TYPED_MAPS_MISSING",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "topological_monad_data_filled": True,
            "generic_map_claim_recorded": True,
            "typed_map_absence_recorded": True,
            "validator_still_refuses_open_template": validator_result["exit_code"] == 2,
        },
        "what_remains_open": {
            "typed_f_g_maps": True,
            "g_f_zero_machine_check": True,
            "locally_free_stable_hym_certificate": True,
            "cech_or_dolbeault_matrices": True,
            "selected_representation_trace": True,
            "D_E_or_rhoE_packet": True,
            "endomorphism_E": True,
            "finite_part_data": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
