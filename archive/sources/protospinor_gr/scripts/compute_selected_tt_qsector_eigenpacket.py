from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QG_I_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\12 Quantum Gravity"
) / "Constructive_MTT_Quantum_Gravity_I__Borel_Summability_of_the_SPT_Filtered_TT_Sector.md"
QG_II_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\12 Quantum Gravity"
) / "Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping.md"

GAP_CERT = ROOT / "certificates" / "selected_tt_qsector_spectral_gap_certificate.json"
OUT_CERT = ROOT / "certificates" / "selected_tt_qsector_eigenpacket_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_tt_qsector_eigenpacket.template.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def flat_periodic_rows(lengths: list[float]) -> list[dict[str, Any]]:
    rows = []
    for length in lengths:
        lam = (2.0 * math.pi / length) ** 2
        rows.append(
            {
                "spatial_torus_length_L": length,
                "lowest_nonzero_wave_number_squared": lam,
                "tt_polarizations_per_wave_vector": 2,
                "first_shell_wave_vectors_real_count": 6,
                "real_TT_first_shell_multiplicity": 12,
            }
        )
    return rows


def main() -> None:
    gap = load_json(GAP_CERT)
    qg_i = read(QG_I_SOURCE)
    qg_ii = read(QG_II_SOURCE)

    source_tests = {
        "qg_i_uses_bounded_geometry_finite_slab": "finite time slab" in qg_i
        and "bounded domain" in qg_i,
        "qg_i_uses_TT_sector": "TT" in qg_i and "SPT-filtered TT" in qg_i,
        "qg_ii_lifts_to_physical_hilbert_space": "Physical Hilbert Space" in qg_ii
        or "physical Hilbert space" in qg_ii,
        "source_selects_unique_TT_slab_size": False,
        "source_selects_boundary_conditions": False,
        "source_computes_lowest_TT_eigenvalue": False,
    }

    candidate_rows = flat_periodic_rows([2.0 * math.pi, 1.0, 4.0 * math.pi])

    packet = {
        "artifact": "Selected_TT_QSector_Eigenpacket",
        "source_closed_requirements": {
            "operator": "E = Lichnerowicz operator on TT modes",
            "context": "bounded-geometry finite time slab / bounded domain",
            "physical_projection": "TT sector, then BRST/BV physical Hilbert-space lift",
        },
        "model_eigenpacket_not_selected": {
            "model": "flat periodic spatial 3-torus Cauchy-slice TT Laplacian",
            "operator": "E = -Delta on TT tensors when background curvature is zero",
            "boundary_conditions": "periodic",
            "qsector": "remove k=0 coherent modes; retain first nonzero Fourier shell",
            "rows": candidate_rows,
        },
        "open_selected_data": {
            "selected_TT_background_or_finite_quotient": None,
            "selected_spatial_length_or_dimensionless_radius": None,
            "selected_boundary_conditions": None,
            "selected_Q_sector_projector": None,
            "proof_flat_periodic_model_is_selected": None,
            "same_branch_identity_with_Z64": None,
        },
        "promotion_rule": (
            "The flat periodic spectrum becomes the selected MTT TT eigenpacket only "
            "if the corpus supplies the selected domain/quotient and boundary conditions."
        ),
    }
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_tt_qsector_eigenpacket",
        "status": "TT_QSECTOR_MODEL_EIGENPACKET_COMPUTED_SELECTED_DOMAIN_OPEN",
        "input_certificates": {
            "selected_tt_qsector_spectral_gap": str(GAP_CERT),
        },
        "source_files": {
            "constructive_qg_i": str(QG_I_SOURCE),
            "constructive_qg_ii": str(QG_II_SOURCE),
        },
        "source_tests": source_tests,
        "packet_written": str(OUT_PACKET),
        "model_computation": {
            "flat_periodic_T3_formula": "lambda_1 = (2*pi/L)^2 after k=0 removal",
            "unit_radius_L_2pi_value": 1.0,
            "rows": candidate_rows,
            "computed_as_selected_MTT_value": False,
        },
        "candidate_status": {
            "flat_periodic_unit_radius_matches_closure_metric_1": True,
            "flat_periodic_model_explains_how_eta_TT_could_equal_1": True,
            "selected_by_current_corpus": False,
            "same_branch_with_Z64": False,
            "reason_not_selected": (
                "Constructive QG sources require bounded-geometry slabs/domains, but do "
                "not select the flat periodic domain, its length, or its boundary conditions."
            ),
        },
        "remaining_gate": {
            "name": "Selected_TT_Domain_and_Boundary_Condition_Theorem",
            "must_supply": [
                "selected finite TT domain or compact quotient",
                "boundary conditions or spectral contour",
                "Q-sector zero-mode removal rule",
                "dimensionless length/radius normalization",
                "then rerun the eigenpacket computation as selected rather than model",
            ],
        },
        "relation_to_previous_gate": {
            "previous_status": gap["status"],
            "advance": (
                "The first explicit TT eigenpacket model is computed. It shows how "
                "lambda_TT=1 arises on a unit-radius flat periodic TT quotient, but "
                "that quotient is not selected by the current corpus."
            ),
        },
        "guardrails": {
            "claims_selected_TT_domain": False,
            "claims_flat_periodic_model_selected": False,
            "claims_lambda_TT_equals_1": False,
            "claims_lambda_TT_equals_z64_15": False,
            "claims_physical_modal_gap": False,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
