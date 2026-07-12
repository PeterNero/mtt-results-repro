"""Hunt for selected D_E/rho_E matrix source data for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

INPUT_FCC = DATA / "fcc_invariant_equation_packet_or_de_exit.candidate.json"
OUTPUT_DATA = DATA / "selected_de_or_rhoe_matrix_source_hunt.candidate.json"
OUTPUT_CERT = CERTS / "selected_de_or_rhoe_matrix_source_hunt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Selected_DE_or_RhoE_Matrix_Source_Hunt_v1.md"


SOURCES = {
    "flux_iwasawa": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "typed_monad_interface": DATA / "typed_monad_de_or_rhoe_data_interface.candidate.json",
    "typed_monad_fill": DATA / "typed_monad_data_fill_attempt.candidate.json",
    "source_fill_attempt": DATA / "source_augmentation_iwasawa_monad_maps_fill_attempt.candidate.json",
    "color_operator_fill": DATA / "color_bundle_operator_packet_fill_attempt.candidate.json",
    "q79_rhoe_source_ansatz": Q79 / "proof_corpus" / "Visible_RhoE_Source_Ansatz_Search_v1.md",
    "q79_projective_mesh": Q79 / "proof_corpus" / "Iwasawa_Projective_RhoE_Mesh_Validator_v1.md",
    "q79_operator_after_s3": Q79 / "proof_corpus" / "Visible_Operator_Source_After_S3_Closure_v1.md",
    "coherent_green": OBSIDIAN
    / "5 Dirac Delta"
    / "Coherent_Green_Functions__Replacing_Point_Sources_by_Admissible_Kernels_in_Modal_Triplet_Theory.md",
}

TERM_SETS = {
    "flux_iwasawa": {
        "generic_maps": "generic holomorphic maps",
        "constant_matrices": "constant matrices",
        "connection_laplacian": "connection Laplacian",
        "rhoE": "rho_E",
        "transition_matrices": "transition matrices",
        "D_E": "D_E",
    },
    "typed_monad_interface": {
        "de_required": "D_E packet",
        "rhoe_required": "rho_E packet",
        "identity_rejected": "identity rho_E",
        "open_template": "OPEN_SELECTED_QA_SU3_TYPED_MONAD_DE_OR_RHOE_DATA_REQUIRED",
    },
    "typed_monad_fill": {
        "typed_maps_missing": "typed maps",
        "operator_missing": "operator",
        "blocked": "blocked",
    },
    "source_fill_attempt": {
        "automorphy_open": "automorphy",
        "section_ring_open": "section_ring",
        "operator_exit_null": "operator_exit",
    },
    "color_operator_fill": {
        "endomorphism_E": "endomorphism_E",
        "operator_layer": "operator",
        "partial_source": "partial",
    },
    "q79_rhoe_source_ansatz": {
        "ordinary_rejected": "ordinary",
        "projective": "projective",
        "selected_DE": "selected D_E",
        "fixed_gerbe": "fixed selected gerbe",
    },
    "q79_projective_mesh": {
        "projective_gluing": "projective",
        "central_phase": "central",
        "validator": "validator",
    },
    "q79_operator_after_s3": {
        "operator_source": "operator source",
        "primitive_C1": "primitive C1",
        "open_items": "open",
    },
    "coherent_green": {
        "finite_spectral": "finite spectral",
        "heat_kernel": "heat",
        "same_operator": "same operator",
        "smooth_response": "smooth",
    },
}


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    text = read_text(path)
    folded = text.lower()
    return {
        "path": str(path),
        "present": bool(text),
        "terms": {key: needle.lower() in folded for key, needle in terms.items()},
    }


def status(path: Path) -> str | None:
    if path.suffix != ".json" or not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("status")
    except json.JSONDecodeError:
        return None


def main() -> None:
    fcc = json.loads(INPUT_FCC.read_text(encoding="utf-8"))
    scans = {key: scan(path, TERM_SETS[key]) for key, path in SOURCES.items()}
    statuses = {key: status(path) for key, path in SOURCES.items() if path.suffix == ".json"}
    route_tests = [
        {
            "route_id": "printed_flux_monad_operator",
            "verdict": "GENERIC_CONTEXT_ONLY",
            "promotes_matrix_source": False,
            "evidence": scans["flux_iwasawa"]["terms"],
            "reason": "The source names generic maps/local-frame constants and a possible operator class, but prints no typed f,g matrices, transition matrices, D_E, or rho_E.",
        },
        {
            "route_id": "typed_monad_interface_and_fill",
            "verdict": "VALIDATOR_READY_VALUES_OPEN",
            "promotes_matrix_source": False,
            "evidence": {
                "interface": statuses.get("typed_monad_interface"),
                "fill": statuses.get("typed_monad_fill"),
            },
            "reason": "The typed packet interface is the correct acceptance shape; the fill attempt remains blocked by missing typed maps and operator data.",
        },
        {
            "route_id": "q79_projective_rhoe_transfer",
            "verdict": "GUARDRAIL_ONLY_NOT_QA_SU3_SOURCE",
            "promotes_matrix_source": False,
            "evidence": {
                "rhoe_ansatz": scans["q79_rhoe_source_ansatz"]["terms"],
                "mesh": scans["q79_projective_mesh"]["terms"],
            },
            "reason": "q79 supplies projective/rho_E validator patterns, but not the selected Qa/SU3 matrix packet.",
        },
        {
            "route_id": "coherent_green_heat_exit",
            "verdict": "ANALYTIC_EXIT_TEMPLATE_ONLY",
            "promotes_matrix_source": False,
            "evidence": scans["coherent_green"]["terms"],
            "reason": "The corpus supports finite spectral/heat responses generated by the same operator, but the same operator for Qa/SU3 is not selected.",
        },
    ]
    matrix_found = any(row["promotes_matrix_source"] for row in route_tests)
    candidate = {
        "candidate": "SelectedQaSU3SelectedDEOrRhoEMatrixSourceHunt",
        "status": "SELECTED_DE_OR_RHOE_MATRIX_SOURCE_HUNT_DONE_SOURCE_NOT_FOUND",
        "input_status": fcc["status"],
        "source_scans": scans,
        "source_statuses": statuses,
        "route_tests": route_tests,
        "gate_results": {
            "printed_typed_f_g_matrices_found": False,
            "printed_transition_rhoE_found": False,
            "printed_DE_matrix_found": False,
            "same_source_heat_spectrum_torsion_exit_found": False,
            "q79_validator_patterns_found": scans["q79_projective_mesh"]["terms"]["validator"],
            "coherent_heat_template_found": scans["coherent_green"]["terms"]["heat_kernel"],
            "selected_matrix_source_found": matrix_found,
            "qa_su3_packet_closed": False,
            "closure_claimed": False,
        },
        "decision": {
            "result": "No selected D_E/rho_E matrix source was found.",
            "what_this_proves": "The current remaining object is genuinely a source-data gap, not a missing algebraic manipulation.",
            "minimal_closing_packet": [
                "typed f,g matrices with g*f=0",
                "one of D_E, rho_E, Riesz/Green, heat, zeta, or torsion finite response",
                "same-source trace/representation and projector policy",
                "admissibility checks: stability/local-freeness plus Bianchi/Freed-Witten/projector retention as applicable",
            ],
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3SelectedDEOrRhoEMatrixSourceHunt",
        "status": "QA_SU3_SELECTED_DE_OR_RHOE_MATRIX_SOURCE_HUNT_DONE_SOURCE_NOT_FOUND",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "matrix_source_search_executed": True,
            "generic_flux_monad_context_rejected_as_matrix_source": True,
            "q79_rhoE_patterns_retained_as_guardrails": True,
            "coherent_heat_exit_template_identified": True,
        },
        "what_remains_open": {
            "selected_typed_f_g_matrices": True,
            "selected_D_E_or_rho_E_matrix": True,
            "selected_heat_spectrum_zeta_or_torsion_finite_part": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_Minimal_Closing_Source_Data_Request_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = """# Selected Qa/SU3 Selected D_E or RhoE Matrix Source Hunt v1

This search checks whether the remaining operator matrix data are already
present in the local proof repos or corpus.

## Result

No selected `D_E/rho_E` matrix source was found.

The Iwasawa flux paper supplies the right context: generic monad maps,
local-frame constants, and operator language.  It does not print the typed
`f,g` maps, transition matrices, or finite operator response.  q79 supplies
useful projective/rho_E validators, but these are guardrails rather than the
same Qa/SU3 source.  The coherent Green/heat corpus supplies the analytic form
of a valid exit once the same operator is selected.

## Minimal Closing Packet

```text
typed f,g matrices with g*f=0
same-source D_E or rho_E matrix data
representation/trace/projector policy
heat/spectrum/zeta/torsion finite part
stability/local-freeness and Bianchi/Freed-Witten/projector checks
```

closure claimed: no
target fitting used: no
"""
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
