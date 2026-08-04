"""Gate A01 repair, monad D_E, and rho_E exits for the Qa/SU3 operator source."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

PREVIOUS = DATA / "monad_to_operator_packet_transfer_gate.candidate.json"
SOURCE = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
OUTPUT_DATA = DATA / "source_certified_a01_erratum_or_monad_de_operator.candidate.json"
OUTPUT_CERT = CERTS / "source_certified_a01_erratum_or_monad_de_operator_certificate.json"


def scan_source() -> dict[str, object]:
    found = {
        "A01_printed": False,
        "B2_printed_E31": False,
        "B3_printed_E12": False,
        "constant_matrices_left_invariant": False,
        "generic_maps_fg": False,
        "connection_laplacian_phrase": False,
        "transition_matrices": False,
        "rhoE": False,
        "cech": False,
    }
    if not SOURCE.exists():
        return {"path": str(SOURCE), "present": False, "found": found, "interpretation": {}}
    text = SOURCE.read_text(encoding="utf-8", errors="ignore")
    low = text.lower()
    found.update(
        {
            "A01_printed": "a^{(0,1)}" in low or "a^(0,1)" in low,
            "B2_printed_E31": "e31" in low or "e_{31}" in low,
            "B3_printed_E12": "e12" in low or "e_{12}" in low,
            "constant_matrices_left_invariant": "left-invariant" in low and "constant" in low,
            "generic_maps_fg": "monad" in low and "f" in low and "g" in low,
            "connection_laplacian_phrase": "connection laplacian" in low or "laplacian" in low,
            "transition_matrices": "transition matrices" in low or "transition matrix" in low,
            "rhoE": "rho_e" in low or "rhoe" in low or "rho_e" in low,
            "cech": "cech" in low or "čech" in low,
        }
    )
    return {
        "path": str(SOURCE),
        "present": True,
        "found": found,
        "interpretation": {
            "A01_printed_but_erratum_not_source_certified": found["A01_printed"],
            "monad_maps_named_but_not_printed": found["generic_maps_fg"],
            "finite_rhoE_or_cech_packet_printed": found["rhoE"] or found["cech"] or found["transition_matrices"],
        },
    }


def main() -> None:
    previous = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    source_scan = scan_source()
    exit_paths = [
        {
            "id": "source_certified_a01_erratum",
            "status": "OPEN_NOT_SOURCE_CERTIFIED",
            "available_data": [
                "minimal diagonal B3 repair identified in older diagnostic artifacts",
                "one-entry B2 repair identified by sparse scan in older diagnostic artifacts",
                "A/B diagnostic comparison exists as external context",
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
                "connection Laplacian mentioned as a possible operator class",
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
                "rho_E validators exist in adjacent q79 work",
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
    decision = {
        "source_certified_a01_erratum_available": False,
        "direct_monad_D_E_operator_available": False,
        "finite_rhoE_transition_packet_available": False,
        "operator_packet_fillable_now": False,
        "endomorphism_E_computable_now": False,
        "determinant_computable_now": False,
        "qa_su3_closed": False,
        "target_fitting_used": False,
    }
    best_next_action = {
        "name": "typed monad / Dolbeault operator data request",
        "why": "It follows the actual monad construction instead of choosing an A01 repair by hand.",
        "required_packet": [
            "explicit f and g maps with source/target line-bundle types",
            "proof g*f=0 and E=ker(g)/im(f) locally free/stable on selected branch",
            "Cech or Dolbeault matrices for E or End(E)",
            "selected representation and trace normalization",
            "D_E or rho_E validator input",
            "endomorphism_E / heat coefficient / spectrum data",
        ],
    }
    candidate = {
        "candidate": "SelectedQaSU3SourceCertifiedA01ErratumOrMonadDEOperator",
        "status": "SOURCE_CERTIFIED_OPERATOR_EXIT_GATE_BUILT_NO_EXIT_CLOSED",
        "input_statuses": {"monad_transfer": previous["status"]},
        "source_scan": source_scan,
        "exit_paths": exit_paths,
        "decision": decision,
        "best_next_action": best_next_action,
        "guardrails": [
            "Do not turn an algebraic erratum candidate into a source-certified operator.",
            "Do not infer D_E from topological monad charges alone.",
            "Do not treat abstract existence of patching data as a finite rho_E packet.",
            "Do not select mu by convenience normalization or by target residual.",
        ],
        "next_required_artifact": "Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3SourceCertifiedA01ErratumOrMonadDEOperator",
        "status": "QA_SU3_SOURCE_CERTIFIED_OPERATOR_EXIT_GATE_BUILT_NO_EXIT_CLOSED",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "three_operator_exits_tested": True,
            "a01_erratum_rejected_without_source_certification": True,
            "monad_de_route_identified_as_best_next": True,
            "rhoE_route_requires_actual_packet": True,
        },
        "what_remains_open": {
            "typed_monad_maps": True,
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
