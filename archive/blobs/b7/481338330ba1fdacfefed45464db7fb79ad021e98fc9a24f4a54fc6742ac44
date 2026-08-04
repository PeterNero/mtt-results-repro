"""Gate the remaining Qa/SU3 operator exits after the monad transfer."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"

INPUTS = {
    "monad_transfer": CERTS / "selected_qa_su3_monad_to_operator_packet_transfer_gate_certificate.json",
    "erratum_scan": CERTS / "selected_qa_su3_hym_connection_erratum_or_convention_resolution_certificate.json",
    "erratum_guardrail": CERTS / "selected_qa_su3_hym_erratum_guardrail_deep_scan_certificate.json",
    "repaired_ab": CERTS / "selected_qa_su3_repaired_pipeline_ab_diagnostic_comparison_certificate.json",
    "mu_domain": CERTS / "selected_qa_su3_hym_mu_and_operator_domain_selection_certificate.json",
    "delta_a_mu": CERTS / "selected_qa_su3_hym_delta_a_mu_spectrum_certificate.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan_source() -> dict[str, Any]:
    text = SOURCE.read_text(encoding="utf-8", errors="ignore") if SOURCE.exists() else ""
    terms = {
        "generic_maps_fg": "generic holomorphic maps $f,g$",
        "constant_matrices_left_invariant": "constant matrices in the left-invariant frame",
        "A01_printed": "\\mathcal{A}^{(0,1)}",
        "B2_printed_E31": "-\\sqrt{\\mu}\\,\\bar\\omega^2",
        "B3_printed_E12": "\\mu\\,\\bar\\omega^3",
        "connection_laplacian_phrase": "connection Laplacian on a fixed Hermitian bundle",
        "rhoE": "rho_E",
        "transition_matrices": "transition matrices",
        "cech": "Cech",
    }
    found = {key: needle in text for key, needle in terms.items()}
    return {
        "path": str(SOURCE),
        "present": SOURCE.exists(),
        "found": found,
        "interpretation": {
            "monad_maps_named_but_not_printed": found["generic_maps_fg"] and found["constant_matrices_left_invariant"],
            "A01_printed_but_erratum_not_source_certified": found["A01_printed"] and found["B2_printed_E31"] and found["B3_printed_E12"],
            "finite_rhoE_or_cech_packet_printed": found["rhoE"] or found["transition_matrices"] or found["cech"],
        },
    }


def main() -> None:
    inputs = {name: load(path) for name, path in INPUTS.items()}
    source_scan = scan_source()

    exit_paths = [
        {
            "id": "source_certified_a01_erratum",
            "status": "OPEN_NOT_SOURCE_CERTIFIED",
            "available_data": [
                "minimal diagonal B3 repair identified",
                "one-entry B2 repair identified by sparse scan",
                "A/B diagnostic comparison exists",
            ],
            "blocking_data": [
                "no corpus erratum selects Repair A or Repair B",
                "no recomputed complete source-certified curvature matrix",
                "no source-selected mu",
            ],
            "can_close_now": False,
        },
        {
            "id": "direct_monad_de_operator",
            "status": "OPEN_MISSING_TYPED_MONAD_MAPS_AND_OPERATOR",
            "available_data": [
                "integer monad charges",
                "generic f,g maps named",
                "Li-Yau/HYM existence claim",
                "connection Laplacian mentioned as a possible compactification operator class",
            ],
            "blocking_data": [
                "actual typed maps f,g are not printed",
                "Cech/Dolbeault cochain matrices are absent",
                "selected representation and trace are absent",
                "D_E principal symbol plus zero-order block is absent",
            ],
            "can_close_now": False,
        },
        {
            "id": "finite_rhoE_transition_packet",
            "status": "OPEN_NO_PACKET",
            "available_data": [
                "rho_E validators exist in q79 repo",
                "monad source implies patching data should exist abstractly",
            ],
            "blocking_data": [
                "no finite transition matrices printed",
                "no Cech cocycle packet",
                "no validator input derived from the monad",
            ],
            "can_close_now": False,
        },
    ]

    output = {
        "certificate": "SelectedQaSU3SourceCertifiedA01ErratumOrMonadDEOperator",
        "status": "QA_SU3_SOURCE_CERTIFIED_OPERATOR_EXIT_GATE_BUILT_NO_EXIT_CLOSED",
        "input_status": {name: data.get("status", "UNKNOWN") for name, data in inputs.items()},
        "source_scan": source_scan,
        "exit_paths": exit_paths,
        "decision": {
            "source_certified_a01_erratum_available": False,
            "direct_monad_D_E_operator_available": False,
            "finite_rhoE_transition_packet_available": False,
            "operator_packet_fillable_now": False,
            "endomorphism_E_computable_now": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "best_next_action": {
            "name": "typed monad / Dolbeault operator data request",
            "why": (
                "It is the least speculative exit: the corpus already names generic "
                "monad maps f,g, so printing or deriving typed maps could produce "
                "a genuine D_E or Cech/rho_E packet without relying on an A01 erratum."
            ),
            "required_packet": [
                "explicit f and g maps with source/target line-bundle types",
                "proof g*f=0 and E=ker(g)/im(f) locally free/stable on selected branch",
                "Cech or Dolbeault matrices for E or End(E)",
                "selected representation and trace normalization",
                "D_E or rho_E validator input",
                "endomorphism_E / heat coefficient / spectrum data",
            ],
        },
        "guardrails": [
            "Do not turn an algebraic erratum candidate into a source-certified operator.",
            "Do not infer D_E from topological monad charges alone.",
            "Do not treat abstract existence of patching data as a finite rho_E packet.",
            "Do not select mu by convenience normalization or by target residual.",
        ],
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1",
            "must_define": [
                "typed f,g monad map schema",
                "accepted Dolbeault/Cech matrix schema",
                "representation/trace selector",
                "D_E/rho_E validation checks",
                "heat or determinant output requirements",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
