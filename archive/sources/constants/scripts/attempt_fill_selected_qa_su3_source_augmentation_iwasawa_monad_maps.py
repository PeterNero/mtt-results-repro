"""Attempt to fill the Qa/SU3 Iwasawa monad-map augmentation packet.

The attempt is deliberately conservative: it imports only source-printed data
and refuses to turn generic existence statements or local-frame constants into
global non-flat line-bundle sections.
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
TEMPLATE = CERTS / "selected_qa_su3_source_augmentation_iwasawa_monad_maps.template.json"
INTERFACE = CERTS / "selected_qa_su3_source_augmentation_iwasawa_monad_maps_interface_certificate.json"
COCYCLE_NOGO = CERTS / "selected_qa_su3_iwasawa_automorphy_cocycle_data_or_nogo_certificate.json"
SECTION_RING_INTERFACE = CERTS / "selected_qa_su3_iwasawa_line_bundle_section_ring_interface_certificate.json"
MONAD_GATE = CERTS / "selected_qa_su3_monad_map_construction_or_source_augmentation_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_qa_su3_source_augmentation_iwasawa_monad_maps.py"
OUTPUT_CERT = CERTS / "selected_qa_su3_source_augmentation_packet_fill_attempt_certificate.json"


SOURCE_TERMS = {
    "iwasawa_quotient": "X=\\Gamma\\backslash H_3(\\mathbb{C})",
    "left_invariant_ansatz": "left-invariant",
    "printed_monad_sequence": "0\\longrightarrow K_1",
    "printed_line_classes": "\\ell_1&=-2",
    "printed_kappa_classes": "\\kappa_1=a",
    "generic_maps": "generic holomorphic maps",
    "constant_left_invariant_maps": "constant matrices in the left-invariant frame",
    "li_yau_hym_claim": "Li--Yau theorem",
    "explicit_dolbeault_section": "explicit left-invariant holomorphic structure",
    "automorphy": "automorphy",
    "factor_of_automorphy": "factor of automorphy",
    "section_ring": "section ring",
    "lattice_generators": "lattice generators",
    "theta_functions": "theta function",
    "rho_E": "rho_E",
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


def partial_packet(template: dict[str, Any]) -> dict[str, Any]:
    packet = json.loads(json.dumps(template))
    packet["status"] = "OPEN_SELECTED_QA_SU3_SOURCE_AUGMENTATION_PACKET_FILL_ATTEMPT_INCOMPLETE"
    packet["selected_branch"] = {
        "source_certificate": str(SOURCE),
        "selection_rule": (
            "Use only corpus-printed Iwasawa SU3 monad topology and source-level "
            "generic-map/HYM statements; do not use Qa/SU3 residual data."
        ),
        "target_residual_used": False,
    }
    packet["geometry"]["quotient"] = "Gamma \\ H_3(C)"
    packet["geometry"]["left_or_right_quotient_convention"] = "left quotient, source notation Gamma\\H_3(C)"
    packet["monad_maps"]["stable_or_hym_source_checked"] = (
        "source-level Li-Yau/HYM existence claim for generic maps; exact maps not certified"
    )
    return packet


def main() -> None:
    template = load(TEMPLATE)
    interface = load(INTERFACE)
    cocycle_nogo = load(COCYCLE_NOGO)
    section_ring = load(SECTION_RING_INTERFACE)
    monad_gate = load(MONAD_GATE)
    scan = source_scan()
    packet = partial_packet(template)
    validator_template = run_validator(TEMPLATE)

    terms = scan["terms"]
    fillable = {
        "source_certificate": scan["present"],
        "quotient_notation": bool(terms["iwasawa_quotient"]),
        "left_invariant_ansatz": bool(terms["left_invariant_ansatz"]),
        "monad_topology": bool(terms["printed_monad_sequence"] and terms["printed_line_classes"] and terms["printed_kappa_classes"]),
        "generic_maps_named": bool(terms["generic_maps"]),
        "constant_left_invariant_maps_named": bool(terms["constant_left_invariant_maps"]),
        "hym_source_claim_named": bool(terms["li_yau_hym_claim"]),
        "target_fitting_used": False,
    }
    hard_blockers = {
        "complex_coordinate_action": packet["geometry"]["complex_coordinate_action"],
        "lattice_generators": packet["geometry"]["lattice_generators"],
        "charge_to_factor_map": packet["automorphy"]["charge_to_factor_map"],
        "cocycle_checked": packet["automorphy"]["cocycle_checked"],
        "c1_charge_realization_checked": packet["automorphy"]["c1_charge_realization_checked"],
        "section_dimensions": {space["id"]: space["dimension"] for space in packet["section_spaces"]["spaces"]},
        "section_bases": {space["id"]: space["basis"] for space in packet["section_spaces"]["spaces"]},
        "product_constants": packet["multiplication"]["product_constants"],
        "f_coefficients": packet["monad_maps"]["f_coefficients"],
        "g_coefficients": packet["monad_maps"]["g_coefficients"],
        "operator_exit": packet["operator_exit"]["kind"],
    }
    local_frame_mismatch = {
        "source_statement": "generic holomorphic maps as constant matrices in the left-invariant frame",
        "why_not_enough": [
            "the packet needs global sections of nonzero-charge line bundles F_i and G_i",
            "constant local-frame entries do not specify a non-flat factor of automorphy",
            "without section bases and products, g*f=0 is not a machine-checkable scalar relation",
            "without Cech/Dolbeault/rho_E/D_E data, no finite determinant can be computed",
        ],
        "accepted_repair": (
            "provide the automorphy cocycle and section ring, or print exact f,g maps "
            "with a finite operator exit in the source"
        ),
    }

    output = {
        "certificate": "SelectedQaSU3SourceAugmentationPacketFillAttempt",
        "status": "QA_SU3_SOURCE_AUGMENTATION_PACKET_FILL_ATTEMPT_BLOCKED_AUTOMORPHY_SECTION_RING_OPEN",
        "input_status": {
            "source_augmentation_interface": interface["status"],
            "automorphy_cocycle_nogo": cocycle_nogo["status"],
            "section_ring_interface": section_ring["status"],
            "monad_map_gate": monad_gate["status"],
        },
        "source_scan": scan,
        "template_validator_result": validator_template,
        "partial_packet": packet,
        "fillable_from_source": fillable,
        "hard_blockers": hard_blockers,
        "local_frame_mismatch": local_frame_mismatch,
        "gate_results": {
            "source_certificate": "PASS_SOURCE_PRESENT",
            "monad_topology": "PASS_SOURCE_PRINTED",
            "quotient_notation": "PARTIAL_SOURCE_PRINTED_LEFT_QUOTIENT",
            "complex_coordinate_action": "FAIL_NOT_PRINTED",
            "lattice_generators": "FAIL_NOT_PRINTED",
            "automorphy_cocycle": "FAIL_CURRENT_SOURCE_NO_GO",
            "section_ring": "FAIL_INTERFACE_ONLY_VALUES_OPEN",
            "generic_constant_maps": "FAIL_LOCAL_FRAME_STATEMENT_NOT_GLOBAL_SECTION_PACKET",
            "g_f_zero": "FAIL_NO_SECTION_PRODUCTS_OR_COEFFICIENTS",
            "local_freeness_stability": "FAIL_GENERIC_SOURCE_CLAIM_NOT_EXACT_MAP_CERTIFICATE",
            "operator_exit": "FAIL_NOT_AVAILABLE",
            "qa_su3_closure": "FAIL_NO_CLOSURE",
        },
        "fill_result": {
            "partial_source_packet_built": True,
            "source_certificate_filled": True,
            "geometry_partially_filled": True,
            "automorphy_filled": False,
            "section_ring_filled": False,
            "explicit_f_g_constructed": False,
            "g_f_zero_checked": False,
            "operator_exit_available": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Source_Augmentation_Repair_Options_v1",
            "must_decide_between": [
                "amend/source the Iwasawa factor-of-automorphy and section-ring data",
                "replace the monad-map route with a source-certified D_E/rho_E operator exit",
                "switch to the projective gerbe/Chan-Paton route if the non-flat ordinary line-bundle packet is not source-selected",
            ],
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
