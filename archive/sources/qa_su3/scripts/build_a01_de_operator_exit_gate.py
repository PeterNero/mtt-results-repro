"""Build the selected A01/D_E operator-exit gate for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

PERIOD_GATE = DATA / "ctwist_period_normalization_or_a01_exit.candidate.json"
CORPUS_AUDIT = DATA / "full_corpus_dependency_audit.candidate.json"
SOURCE_PACKET = DATA / "source_augmentation_packet.candidate.json"
OUTPUT_DATA = DATA / "a01_de_operator_exit_gate.candidate.json"
OUTPUT_CERT = CERTS / "a01_de_operator_exit_gate_certificate.json"

SOURCES = {
    "nonsm_typed_monad_interface": NONSM / "proof_corpus" / "Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1.md",
    "nonsm_typed_monad_fill": NONSM / "proof_corpus" / "Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1.md",
    "nonsm_color_operator": NONSM / "proof_corpus" / "Selected_Qa_SU3_Color_Bundle_Connection_or_Global_Section_Determinant_v1.md",
    "q79_rhoe_mesh": Q79 / "proof_corpus" / "Iwasawa_Rotated_Phase_Mesh_RhoE_Sector_Prototype_v1.md",
    "q79_riesz_gap": Q79 / "proof_corpus" / "Iwasawa_Riesz_Gap_Validator_v1.md",
    "q79_visible_valpha_candidates": Q79 / "proof_corpus" / "Visible_VAlpha_Chern_Bianchi_Source_Packet_Candidates_v1.md",
    "quantum_gravity": Path(
        r"C:\Users\nero_\Downloads\TEXPAPERS\12 Quantum Gravity\_work\Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4\main.tex"
    ),
}


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {"path": str(path), "present": True, "terms": {key: term.lower() in text for key, term in terms.items()}}


def requirement(name: str, present: bool, source: str, reason: str) -> dict[str, object]:
    return {"name": name, "present_now": present, "source": source, "reason": reason}


def route_test(route_id: str, verdict: str, closes: list[str], missing: list[str]) -> dict[str, object]:
    return {"route_id": route_id, "verdict": verdict, "what_it_closes": closes, "missing_for_promotion": missing}


def main() -> None:
    period_gate = json.loads(PERIOD_GATE.read_text(encoding="utf-8"))
    corpus = json.loads(CORPUS_AUDIT.read_text(encoding="utf-8"))
    source = json.loads(SOURCE_PACKET.read_text(encoding="utf-8"))
    scans = {
        "nonsm_typed_monad_interface": scan(
            SOURCES["nonsm_typed_monad_interface"],
            {"validator_built": "validator", "de_required": "D_E", "rhoe_required": "rho_E", "closed_no": "not closed"},
        ),
        "nonsm_typed_monad_fill": scan(
            SOURCES["nonsm_typed_monad_fill"],
            {"topology_filled": "topology", "maps_open": "maps", "generic_not_enough": "generic", "operator_open": "operator"},
        ),
        "nonsm_color_operator": scan(
            SOURCES["nonsm_color_operator"],
            {"selected_connection_route": "connection", "operator_data_missing": "operator data", "local_system_torsion": "local system"},
        ),
        "q79_rhoe_mesh": scan(
            SOURCES["q79_rhoe_mesh"],
            {"validator_stack": "validator", "not_selected": "not selected", "noncommuting_needed": "noncommuting"},
        ),
        "q79_riesz_gap": scan(
            SOURCES["q79_riesz_gap"],
            {"validator_gate": "validator", "selected_spectral_needed": "selected spectral", "selected_operator_not_proved": "not prove the selected operator"},
        ),
        "q79_visible_valpha_candidates": scan(
            SOURCES["q79_visible_valpha_candidates"],
            {"finite_cochain_packet": "finite Cech or Dolbeault cochain packet", "same_source_DE": "same-source D_E operator block", "dotD_response": "same-source dotD_alpha1 response"},
        ),
        "quantum_gravity": scan(
            SOURCES["quantum_gravity"],
            {"harmonic_projector": "harmonic projector", "ward_bianchi": "Bianchi", "operator_context": "operator"},
        ),
    }
    required_spaces = source["required_section_spaces"]
    acceptance_interface = [
        requirement("selected_source_certificate", False, "Qa/SU3 same-branch source", "Must be selected by MTT for this Qa/SU3 branch."),
        requirement("typed_section_or_cochain_bases_for_11_spaces", False, "Cech/Dolbeault or twisted section packet", "The 11 spaces F1..F5, G1..G5, P need explicit bases or finite cochain blocks."),
        requirement("selected_f_and_g_matrices", False, "typed monad map packet", "Symbolic charge matching must be promoted to actual f and g matrices with g*f=0."),
        requirement("selected_DE_or_rhoE_matrix", False, "operator packet", "A selected D_E, rho_E, Riesz, Green, heat, zeta, or torsion finite-part operator must be supplied."),
        requirement("spectral_or_heat_exit", False, "operator packet", "The operator must have reproducible spectral/heat/rho_E/Riesz output."),
        requirement("admissibility_checks", False, "source and operator packet", "Freed-Witten, Green-Schwarz/Bianchi, stability/local-freeness, and projector retention must pass when applicable."),
    ]
    rejected_shortcuts = [
        "identity rho_E",
        "simultaneously diagonal scalar phase table as physical mixing",
        "generic existence of f,g without matrices",
        "direct q79/S3 finite torsion import",
        "Chern/Bianchi row without same-source operator data",
        "observed residual or measured constants as inputs",
    ]
    route_tests = [
        route_test(
            "nonsm_typed_monad_interface",
            "VALIDATOR_SHAPE_AVAILABLE_VALUES_OPEN",
            ["Gives the right interface shape for D_E/rho_E acceptance.", "Confirms closure requires selected matrices."],
            ["No selected Qa/SU3 f,g matrix entries are present.", "No selected D_E/rho_E operator matrix is supplied."],
        ),
        route_test(
            "q79_rhoe_and_riesz_validators",
            "PORT_VALIDATOR_SHAPE_ONLY",
            ["Provides reusable validation concepts: nontrivial operator, spectral/Riesz checks, no identity rho_E."],
            ["These are q79 validators/prototypes, not selected Qa/SU3 operator data."],
        ),
        route_test(
            "visible_valpha_same_source_pattern",
            "USE_AS_ACCEPTANCE_PATTERN_ONLY",
            ["Names the required source kind: finite Cech/Dolbeault packet plus same-source D_E/dotD."],
            ["The same-source packet is visible-sector/q79 context, not the selected Qa/SU3 matrix packet."],
        ),
        route_test(
            "quantum_gravity_harmonic_projector",
            "STRUCTURAL_SUPPORT_ONLY",
            ["Supports operator/harmonic-projector exits in the wider MTT corpus."],
            ["Does not provide selected Qa/SU3 finite matrices."],
        ),
    ]
    all_required_present = all(row["present_now"] for row in acceptance_interface)
    candidate = {
        "candidate": "SelectedQaSU3A01DEOperatorExitGate",
        "status": "A01_DE_OPERATOR_EXIT_ACCEPTANCE_GATE_BUILT_SELECTED_MATRICES_OPEN",
        "input_statuses": {"period_gate": period_gate["status"], "full_corpus_dependency_audit": corpus["status"], "source_packet": source["status"]},
        "source_scans": scans,
        "required_section_space_count": len(required_spaces),
        "required_section_spaces": required_spaces,
        "acceptance_interface": acceptance_interface,
        "route_tests": route_tests,
        "rejected_shortcuts": rejected_shortcuts,
        "gate_results": {
            "A01_DE_exit_required_by_period_gate": period_gate["gate_results"]["A01_DE_exit_required"],
            "validator_shapes_available": True,
            "selected_typed_matrices_supplied": False,
            "selected_operator_matrix_supplied": False,
            "spectral_or_heat_exit_supplied": False,
            "all_required_operator_exit_inputs_present": all_required_present,
            "operator_exit_promoted": False,
            "closure_claimed": False,
        },
        "decision": {
            "result": "Gate built; selected operator exit not yet supplied.",
            "why": "The corpus contains validator shapes and same-source acceptance patterns, but not the Qa/SU3 selected f,g matrices or D_E/rho_E operator packet.",
            "next_move": "Construct the selected 11-space finite Cech/Dolbeault cochain packet and same-source f,g,D_E/dotD matrices, then run this acceptance gate.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Cech_Dolbeault_Matrix_Packet_v1",
        "parallel_search_artifact": "Selected_Qa_SU3_Central_Period_Selector_Search_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3A01DEOperatorExitGate",
        "status": "QA_SU3_A01_DE_OPERATOR_EXIT_ACCEPTANCE_GATE_BUILT_SELECTED_MATRICES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "operator_exit_acceptance_interface_built": True,
            "eleven_required_section_spaces_carried_forward": len(required_spaces) == 11,
            "validator_shapes_identified_as_reusable_only": True,
            "unsafe_operator_shortcuts_rejected": True,
            "A01_DE_exit_confirmed_required": period_gate["gate_results"]["A01_DE_exit_required"],
        },
        "what_remains_open": {
            "selected_Cech_Dolbeault_cochain_packet": True,
            "selected_f_and_g_matrices": True,
            "selected_DE_or_rhoE_operator_matrix": True,
            "spectral_heat_riesz_or_torsion_exit": True,
            "Freed_Witten_Bianchi_and_projector_retention": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "parallel_search_artifact": candidate["parallel_search_artifact"],
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
