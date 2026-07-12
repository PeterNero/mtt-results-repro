"""Attempt to fill the selected Qa/SU3 typed monad D_E/rho_E packet.

This is a source-discipline artifact.  It records the monad data that the
corpus actually prints and refuses to promote generic existence statements,
diagnostic A01 matrices, or topological Chern data into a selected operator.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
TEMPLATE = CERTS / "selected_qa_su3_typed_monad_de_or_rhoe_data.template.json"
INTERFACE = CERTS / "selected_qa_su3_typed_monad_de_or_rhoe_data_interface_certificate.json"
TRANSFER = CERTS / "selected_qa_su3_monad_to_operator_packet_transfer_gate_certificate.json"
SOURCE_EXIT = CERTS / "selected_qa_su3_source_certified_a01_erratum_or_monad_de_operator_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_qa_su3_typed_monad_packet.py"
OUTPUT_CERT = CERTS / "selected_qa_su3_typed_monad_data_fill_attempt_certificate.json"


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


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_scan() -> dict[str, Any]:
    if not SOURCE.exists():
        return {
            "path": str(SOURCE),
            "present": False,
            "terms": {key: False for key in SOURCE_TERMS},
        }
    text = SOURCE.read_text(encoding="utf-8", errors="ignore")
    return {
        "path": str(SOURCE),
        "present": True,
        "terms": {key: term in text for key, term in SOURCE_TERMS.items()},
    }


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def partially_fill_template(template: dict[str, Any]) -> dict[str, Any]:
    packet = json.loads(json.dumps(template))
    packet["status"] = "OPEN_SELECTED_QA_SU3_TYPED_MONAD_DATA_FILL_ATTEMPT_INCOMPLETE"
    packet["selected_branch"] = {
        "branch_id": "iwasawa_su3_monad_candidate",
        "source_certificate": str(SOURCE),
        "selection_rule": "corpus-printed Iwasawa monad topological data only; operator data not selected",
        "target_residual_used": False,
    }
    packet["typed_monad"]["monad_checks"]["stable_or_hym_source"] = (
        "source claims Li-Yau/HYM existence for generic maps; not a typed-map certificate"
    )
    return packet


def main() -> None:
    template = load(TEMPLATE)
    interface = load(INTERFACE)
    transfer = load(TRANSFER)
    source_exit = load(SOURCE_EXIT)
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

    output = {
        "certificate": "SelectedQaSU3TypedMonadDataFillAttempt",
        "status": "QA_SU3_TYPED_MONAD_DATA_FILL_ATTEMPT_BLOCKED_TYPED_MAPS_MISSING",
        "input_status": {
            "interface": interface["status"],
            "monad_to_operator_transfer": transfer["status"],
            "source_certified_exit_gate": source_exit["status"],
        },
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
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Monad_Map_Construction_or_Source_Augmentation_v1",
            "must_do": [
                "construct explicit line-bundle typed f,g maps or locate them in source",
                "machine-check g*f=0",
                "certify locally-free/stable/HYM status for those exact maps",
                "derive Dolbeault/Cech matrices or a rho_E transition packet from the same data",
                "only then compute D_E/rho_E finite response",
            ],
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
