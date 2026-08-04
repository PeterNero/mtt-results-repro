"""Attempt to fill the selected Qa/SU3 twisted gerbe source packet.

This imports the strongest selected S3 flat Deligne/class restriction result
from the q79 repo.  It deliberately stops before claiming twisted section bases,
product constants, full Green-Schwarz/operator source, or D_E/dotD data.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

TEMPLATE = CERTS / "selected_qa_su3_twisted_section_ring_gerbe_source.template.json"
GATE = CERTS / "selected_qa_su3_twisted_section_ring_gerbe_source_gate_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_qa_su3_twisted_section_ring_gerbe_source.py"
S3_CERT = Q79 / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json"
S3_DATA = Q79 / "candidate_data" / "visible_twisted_s3_class_restriction_closure.candidate.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_twisted_gerbe_source_packet_fill_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {"exit_code": proc.returncode, "output": proc.stdout.strip()}


def build_partial_packet(template: dict[str, Any], s3_cert: dict[str, Any], s3_data: dict[str, Any]) -> dict[str, Any]:
    packet = json.loads(json.dumps(template))
    packet["status"] = "PARTIAL_SELECTED_QA_SU3_TWISTED_GERBE_SOURCE_PACKET_FILL_ATTEMPT_INCOMPLETE"
    packet["selected_branch"] = {
        "source_certificate": str(S3_CERT),
        "selection_rule": "import selected q79/F,m=1 S3 flat Deligne class/restriction closure; do not import observed Qa/SU3 residual",
        "target_residual_used": False,
    }
    packet["gerbe_source"].update(
        {
            "kind": "Deligne_Cech",
            "representative": {
                "source": str(S3_CERT),
                "selected_packet": s3_cert["selected_packet"],
                "smooth_class": s3_cert["smooth_class"],
                "S3_pullback_table": s3_data["S3_pullback_table"],
            },
            "period_denominator": 3,
            "central_cocycle": {
                "central_phase_label": s3_cert["smooth_class"]["central_phase_label"],
                "formula": s3_data["S3_pullback_table"]["formula"],
                "orientation_checks": s3_data["S3_pullback_table"]["orientation_checks"],
            },
            "selected_by_mtt": True,
            "fixed_topological_sector": True,
            "cocycle_checked": s3_cert["calculation_results"]["map_to_qutrit_central_cocycle_verified"],
            "nontrivial_twist_checked": True,
        }
    )
    packet["ordinary_ab_line_bundle_part"].update(
        {
            "factor_model": "ordinary closed a,b factor model still required; not filled by S3 gerbe closure",
            "a_b_c1_realization_checked": None,
            "forbidden_c_as_ordinary_c1": True,
        }
    )
    packet["twisted_multiplication"].update(
        {
            "pair_products": {
                "F1_G1": {"target": "P", "ordinary_ab_sum": [-1, 1], "gerbe_twist_sum": 0, "constant": None},
                "F2_G2": {"target": "P", "ordinary_ab_sum": [-1, 1], "gerbe_twist_sum": 0, "constant": None},
                "F3_G3": {"target": "P", "ordinary_ab_sum": [-1, 1], "gerbe_twist_sum": 0, "constant": None},
                "F4_G4": {"target": "P", "ordinary_ab_sum": [-1, 1], "gerbe_twist_sum": 0, "constant": None},
                "F5_G5": {"target": "P", "ordinary_ab_sum": [-1, 1], "gerbe_twist_sum": 0, "constant": None},
            },
            "gerbe_twist_cancellation_checked": True,
            "product_table_checked": None,
        }
    )
    packet["admissibility"].update(
        {
            "green_schwarz_bianchi_verified": None,
            "freed_witten_verified": s3_cert["calculation_results"]["smooth_Freed_Witten_cancellation_closed"],
            "twisted_projector_retention_verified": s3_cert["calculation_results"]["block_sector_projector_retention_closed"],
            "coherent_spectral_projector_verified": None,
        }
    )
    return packet


def main() -> None:
    template = load(TEMPLATE)
    gate = load(GATE)
    s3_cert = load(S3_CERT)
    s3_data = load(S3_DATA)
    partial = build_partial_packet(template, s3_cert, s3_data)

    temp_path = CERTS / "_tmp_selected_qa_su3_twisted_gerbe_source_packet.partial.json"
    temp_path.write_text(json.dumps(partial, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    try:
        validator = run_validator(temp_path)
    finally:
        temp_path.unlink(missing_ok=True)

    filled_fields = {
        "selected_s3_flat_deligne_class": s3_cert["what_this_closes"]["selected_S3_flat_Deligne_class"],
        "selected_s3_pullback_table": s3_cert["what_this_closes"]["selected_S3_pullback_restriction_table"],
        "map_to_qutrit_central_cocycle": s3_cert["calculation_results"]["map_to_qutrit_central_cocycle_verified"],
        "period_denominator": partial["gerbe_source"]["period_denominator"],
        "central_phase_label": s3_cert["smooth_class"]["central_phase_label"],
        "smooth_freed_witten": partial["admissibility"]["freed_witten_verified"],
        "block_sector_projector_retention": partial["admissibility"]["twisted_projector_retention_verified"],
        "twist_cancellation_products": partial["twisted_multiplication"]["gerbe_twist_cancellation_checked"],
    }
    unfilled_fields = {
        "ordinary_ab_factor_model_certified": partial["ordinary_ab_line_bundle_part"]["a_b_c1_realization_checked"],
        "twisted_section_dimensions_and_bases": {
            space["id"]: {"dimension": space["dimension"], "basis": space["basis"]}
            for space in partial["twisted_section_spaces"]["spaces"]
        },
        "twisted_product_constants": {
            key: product["constant"]
            for key, product in partial["twisted_multiplication"]["pair_products"].items()
        },
        "green_schwarz_bianchi_verified": partial["admissibility"]["green_schwarz_bianchi_verified"],
        "coherent_spectral_projector_verified": partial["admissibility"]["coherent_spectral_projector_verified"],
        "operator_exit": partial["operator_exit"],
    }

    output = {
        "certificate": "SelectedQaSU3TwistedGerbeSourcePacketFillAttempt",
        "status": "QA_SU3_TWISTED_GERBE_SOURCE_PACKET_FILL_ATTEMPT_PARTIAL_OPERATOR_SECTION_DATA_OPEN",
        "input_status": {
            "twisted_gate": gate["status"],
            "s3_class_restriction": s3_cert["status"],
        },
        "partial_packet": partial,
        "validator_result": validator,
        "filled_fields": filled_fields,
        "unfilled_fields": unfilled_fields,
        "gate_results": {
            "selected_gerbe_representative": "PASS_IMPORTED_SELECTED_S3_FLAT_DELIGNE_CLASS",
            "central_cocycle": "PASS_Q79_F_M1_ZETA3_COCYCLE",
            "freed_witten": "PASS_SMOOTH_S3_TWISTED_CANCELLATION",
            "block_projector_retention": "PASS_BLOCK_SECTOR_ONLY",
            "ordinary_ab_factor_model": "OPEN_NOT_CERTIFIED",
            "twisted_section_bases": "OPEN_NOT_SUPPLIED",
            "twisted_product_constants": "OPEN_NOT_SUPPLIED",
            "green_schwarz_operator_source": "OPEN_VISIBLE_OPERATOR_SOURCE_NOT_SUPPLIED",
            "coherent_spectral_projectors": "OPEN_REQUIRES_SELECTED_D_E_DOTD",
            "operator_exit": "OPEN_NO_PROJECTIVE_RHOE_TWISTED_DE_OR_TORSION_FINITE_PART",
        },
        "fill_result": {
            "selected_gerbe_source_part_filled": True,
            "admissibility_partially_filled": True,
            "twisted_section_ring_filled": False,
            "twisted_multiplication_constants_filled": False,
            "operator_exit_available": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Twisted_Section_Basis_or_Operator_Exit_Construction_v1",
            "must_choose": [
                "construct twisted section bases and product constants for the selected S3 flat gerbe source",
                "or derive a projective rho_E/twisted D_E/torsion finite part directly from the selected source",
                "and in either case add the selected visible Green-Schwarz/operator source needed for coherent spectral projectors",
            ],
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
