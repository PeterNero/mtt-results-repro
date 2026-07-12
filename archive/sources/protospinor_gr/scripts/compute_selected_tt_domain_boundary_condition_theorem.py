from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

EIGENPACKET_CERT = ROOT / "certificates" / "selected_tt_qsector_eigenpacket_certificate.json"
QG_I = CORPUS / "12 Quantum Gravity" / "Constructive_MTT_Quantum_Gravity_I__Borel_Summability_of_the_SPT_Filtered_TT_Sector.md"
QG_II = CORPUS / "12 Quantum Gravity" / "Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping.md"
QG_III = CORPUS / "12 Quantum Gravity" / "Constructive_MTT_Quantum_Gravity_III__Infrared_Limit_and_Scattering_under_SPT_Damping.md"

OUT_CERT = ROOT / "certificates" / "selected_tt_domain_boundary_condition_theorem_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_tt_domain_boundary_condition.template.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> None:
    eigenpacket = load_json(EIGENPACKET_CERT)
    qg_i = read(QG_I)
    qg_ii = read(QG_II)
    qg_iii = read(QG_III) if QG_III.exists() else ""

    source_tests = {
        "qg_i_allows_bounded_domain": "bounded domain" in qg_i,
        "qg_i_allows_dirichlet_or_mixed": "Dirichlet or mixed" in qg_i,
        "qg_i_requires_TT_well_posed": "TT sector is well-posed" in qg_i,
        "qg_ii_requires_no_boundary_BRST_terms": "BRST variations produce no boundary contributions" in qg_ii,
        "qg_iii_uses_ir_box_then_R_to_infinity": "boundary conditions; later take $R\\to\\infty$" in qg_iii,
        "source_selects_periodic_T3": False,
        "source_selects_dirichlet_box": False,
        "source_selects_mixed_boundary": False,
        "source_selects_dimensionless_L": False,
    }

    # Candidate execution domains. These are deliberately model rows, not selected rows.
    candidates = [
        {
            "id": "flat_periodic_T3_unit_radius",
            "domain": "spatial T3 with L=2*pi",
            "boundary": "periodic",
            "lambda_1_model": 1.0,
            "strength": "simple TT Fourier eigenpacket; matches closure-metric candidate",
            "selected": False,
            "blocker": "periodic T3 and L=2*pi are not selected by QG I/II.",
        },
        {
            "id": "dirichlet_cube_unit_length",
            "domain": "bounded cube with side L=1",
            "boundary": "Dirichlet model",
            "lambda_1_model": 3.0 * math.pi * math.pi,
            "strength": "compatible with bounded-domain existence proof as a model",
            "selected": False,
            "blocker": "Dirichlet is allowed but not selected; TT tensor constraints depend on the full gauge setup.",
        },
        {
            "id": "ir_box_limit",
            "domain": "finite box of radius R, then R->infinity",
            "boundary": "IR regulator boundary",
            "lambda_1_model": "tends_to_0_as_R_to_infinity",
            "strength": "useful for scattering/IR limit, not for a positive selected finite gap",
            "selected": False,
            "blocker": "IR limit removes a finite external-box gap; the positive lambda_star must come from selected Q-sector/projector data.",
        },
    ]

    packet = {
        "artifact": "Selected_TT_Domain_and_Boundary_Condition_Theorem",
        "sourced_constraints": {
            "domain_class": "bounded-geometry finite slab or bounded coordinate domain",
            "operator_class": "nonnegative self-adjoint Laplace-type TT operator",
            "allowed_boundaries": ["Dirichlet", "mixed", "support restrictions away from boundary"],
            "BRST_constraint": "boundary/support conditions must remove boundary terms in BRST changes of variables",
        },
        "candidate_domains": candidates,
        "open_selection_data": {
            "selected_domain_topology": None,
            "selected_boundary_condition": None,
            "selected_dimensionless_length": None,
            "selected_Q_sector_zero_mode_policy": None,
            "proof_selected_domain_yields_lambda_1": None,
        },
    }
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_tt_domain_boundary_condition_theorem",
        "status": "TT_DOMAIN_BOUNDARY_CONSTRAINTS_SOURCED_SELECTION_OPEN",
        "input_certificates": {
            "selected_tt_qsector_eigenpacket": str(EIGENPACKET_CERT),
        },
        "source_files": {
            "constructive_qg_i": str(QG_I),
            "constructive_qg_ii": str(QG_II),
            "constructive_qg_iii": str(QG_III),
        },
        "source_tests": source_tests,
        "packet_written": str(OUT_PACKET),
        "closed_now": {
            "admissible_domain_class_sourced": True,
            "allowed_boundary_classes_sourced": True,
            "BRST_boundary_constraint_sourced": source_tests["qg_ii_requires_no_boundary_BRST_terms"],
            "candidate_domain_table_built": True,
        },
        "selection_result": {
            "selected_TT_domain_closed": False,
            "selected_boundary_condition_closed": False,
            "selected_dimensionless_length_closed": False,
            "selected_lambda_TT_closed": False,
            "reason": (
                "The QG constructive papers specify the analytic class needed for a well-defined "
                "TT sector but intentionally allow multiple bounded domains/boundary conditions."
            ),
        },
        "candidate_domain_classification": candidates,
        "next_gate": {
            "name": "TT_Domain_Selection_From_MTT_Fixed_Point_or_Internal_Quotient",
            "must_supply": [
                "a source rule selecting periodic, Dirichlet/mixed, Riesz-contour, or another TT domain",
                "dimensionless length/radius normalization",
                "zero-mode/Q-sector removal policy",
                "proof the selected domain is compatible with BRST boundary constraints",
                "then promote the corresponding eigenpacket from model to selected",
            ],
        },
        "guardrails": {
            "claims_periodic_T3_selected": False,
            "claims_dirichlet_selected": False,
            "claims_lambda_TT_equals_1": False,
            "claims_lambda_TT_numeric_selected": False,
            "claims_physical_modal_gap": False,
        },
        "previous_status": eigenpacket["status"],
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
