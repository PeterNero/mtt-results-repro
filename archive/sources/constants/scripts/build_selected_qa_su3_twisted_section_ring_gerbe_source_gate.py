"""Build the Qa/SU3 twisted section-ring and gerbe-source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
QA_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

PREVIOUS = CERTS / "selected_qa_su3_repair_options_external_synthesis_certificate.json"
TEMPLATE = CERTS / "selected_qa_su3_twisted_section_ring_gerbe_source.template.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_qa_su3_twisted_section_ring_gerbe_source.py"
TWIST_CANDIDATE = QA_REPO / "candidate_data" / "gerbe_twist_cancellation_packet.candidate.json"
TWIST_CERT = QA_REPO / "certificates" / "gerbe_twist_cancellation_packet_certificate.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_twisted_section_ring_gerbe_source_gate_certificate.json"


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


def twist_table(candidate: dict[str, Any]) -> dict[str, Any]:
    spaces: dict[str, Any] = {"P": candidate["P"]}
    for pair in candidate["pair_results"]:
        spaces[pair["pair"][0]] = pair["F"]
        spaces[pair["pair"][1]] = pair["G"]
    pair_products = {}
    for pair in candidate["pair_results"]:
        f_id, g_id = pair["pair"]
        pair_products[f"{f_id}_{g_id}"] = {
            "target": "P",
            "ordinary_ab_sum": [
                pair["F"]["ordinary_ab_charge"][0] + pair["G"]["ordinary_ab_charge"][0],
                pair["F"]["ordinary_ab_charge"][1] + pair["G"]["ordinary_ab_charge"][1],
            ],
            "gerbe_twist_sum": pair["F"]["gerbe_c_twist"] + pair["G"]["gerbe_c_twist"],
            "product_matches_P": pair["product_matches_P"],
            "constant": None,
        }
    return {"spaces": spaces, "pair_products": pair_products}


def main() -> None:
    previous = load(PREVIOUS)
    template = load(TEMPLATE)
    twist_candidate = load(TWIST_CANDIDATE)
    twist_cert = load(TWIST_CERT)
    validator = run_validator(TEMPLATE)
    table = twist_table(twist_candidate)

    all_pairs_cancel = all(
        product["ordinary_ab_sum"] == [-1, 1]
        and product["gerbe_twist_sum"] == 0
        and product["product_matches_P"] is True
        for product in table["pair_products"].values()
    )

    output = {
        "certificate": "SelectedQaSU3TwistedSectionRingGerbeSourceGate",
        "status": "QA_SU3_TWISTED_SECTION_RING_GERBE_SOURCE_GATE_BUILT_VALUES_OPEN",
        "input_status": {
            "repair_synthesis": previous["status"],
            "twist_cancellation": twist_cert["status"],
        },
        "template_path": str(TEMPLATE.relative_to(ROOT)),
        "validator_path": str(VALIDATOR.relative_to(ROOT)),
        "template_status": template["status"],
        "template_validator_result": validator,
        "twist_table": table,
        "what_closes_now": {
            "twist_assignments_for_all_spaces": sorted(table["spaces"]) == ["F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5", "P"],
            "all_Fi_Gi_twists_cancel_to_P": all_pairs_cancel,
            "literal_c_not_used_as_ordinary_c1": template["ordinary_ab_line_bundle_part"]["forbidden_c_as_ordinary_c1"] is True,
            "validator_built": True,
            "open_template_refuses_to_compute": validator["exit_code"] == 2,
        },
        "what_remains_open": {
            "selected_gerbe_representative": True,
            "ordinary_ab_factor_model": True,
            "twisted_section_bases": True,
            "twisted_multiplication_constants": True,
            "freed_witten_bianchi_checks": True,
            "projector_retention": True,
            "operator_exit": True,
            "qa_su3_closed": False,
        },
        "gate_result": {
            "typing_level_solution_preserved": all_pairs_cancel,
            "selected_packet_available": False,
            "operator_exit_available": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Twisted_Gerbe_Source_Packet_Fill_Attempt_v1",
            "must_attempt": [
                "import or construct a selected Deligne/Cech or B-field representative",
                "fill the period denominator and central cocycle",
                "certify Freed-Witten and Green-Schwarz/Bianchi admissibility",
                "fill twisted section bases and multiplication constants",
                "derive projective rho_E, twisted D_E, or torsion finite part",
            ],
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
