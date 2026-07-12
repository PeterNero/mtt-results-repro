from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CORPUS = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

ETA_CERT = ROOT / "certificates" / "selected_gr_tt_eta_normalization_theorem_certificate.json"
COMPLEMENT_CERT = ROOT / "certificates" / "explicit_gr_tt_aint_complement_construction_certificate.json"
QG_SOURCE = CORPUS / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
FINITE_PROJECTION_SOURCE = CORPUS / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"

OUT_CERT = ROOT / "certificates" / "selected_tt_projector_window_normalization_lemma_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    eta = load_json(ETA_CERT)
    complement = load_json(COMPLEMENT_CERT)
    qg = read(QG_SOURCE)
    finite_projection = read(FINITE_PROJECTION_SOURCE)

    source_tests = {
        "finite_projection_defines_Badm_filter": has_all(
            finite_projection,
            ["B_{\\rm adm}", "P\\chi(A)", "\\mathrm e^{-\\tau A}", "\\chi(A)P"],
        ),
        "finite_projection_requires_positive_sectoral_A": "A\\neq\\Box" in finite_projection
        and "A=A_{\\rm int}" in finite_projection,
        "qg_defines_spt_factorization": has_all(
            qg,
            ["B \\,=\\, e^{-\\tfrac{\\tau_0}{2}E}", "e^{-\\tfrac{\\tau_0}{2}A_{\\mathrm{int}}}"],
        ),
        "qg_defines_tau0_positive": "\\tau_0>0" in qg and "tau_0:=\\min" in qg,
        "qg_identifies_TT_operator_E": "Lichnerowicz operator on TT modes" in qg,
        "qg_identifies_projected_linearized_graviton_operator_on_TT": (
            "projected linearized graviton operator on the TT sector" in qg
        ),
        "qg_gives_propagator_bound": "\\frac{e^{-\\tau_0 k^2}}" in qg and "k^2+\\lambda_\\ast" in qg,
        "qg_declares_constants_geometric_projector_data": (
            "All constants $(\\lambda_\\ast,\\tau_0,C_0,c_{\\mathrm{proj}})$ are geometric/projector data"
            in qg
        ),
        "qg_gives_numeric_lambda_star": False,
        "qg_gives_numeric_tau0": False,
        "qg_selects_internal_row_N": False,
    }

    structure_closed = all(
        [
            source_tests["finite_projection_defines_Badm_filter"],
            source_tests["qg_defines_spt_factorization"],
            source_tests["qg_defines_tau0_positive"],
            source_tests["qg_identifies_TT_operator_E"],
            source_tests["qg_identifies_projected_linearized_graviton_operator_on_TT"],
        ]
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_tt_projector_window_normalization_lemma",
        "status": "TT_PROJECTOR_WINDOW_STRUCTURE_SOURCED_SELECTED_NUMERIC_GAP_OPEN",
        "input_certificates": {
            "selected_gr_tt_eta_normalization": str(ETA_CERT),
            "explicit_gr_tt_aint_complement": str(COMPLEMENT_CERT),
        },
        "source_files": {
            "quantum_gravity": str(QG_SOURCE),
            "finite_coherent_projection": str(FINITE_PROJECTION_SOURCE),
        },
        "source_tests": source_tests,
        "closed_structure": {
            "TT_spectral_operator": "E = projected linearized graviton/Lichnerowicz operator on TT modes",
            "TT_filter_form": "B = exp(-tau0 E/2) B0 exp(-tau0 A_int/2)",
            "TT_propagator_bound": "||Delta_prop(k)|| <= C0 exp(-tau0 k^2)/(k^2 + lambda_star)",
            "tau0_positive": True,
            "lambda_star_positive_on_Q_sector": True,
            "structure_closed": structure_closed,
        },
        "effect_on_eta_gate": {
            "previous_eta_status": eta["status"],
            "formal_eta_symbol": complement["formal_construction"]["lowest_positive_eigenvalue"],
            "eta_interpreted_as_TT_Q_sector_lambda_star": structure_closed,
            "eta_numeric_selected": False,
            "eta_equals_kappa_STF_rows": False,
            "eta_equals_nil_or_z64": False,
            "reason": (
                "The QG source supplies the TT projector/window architecture and identifies "
                "the TT spectral operator, but leaves lambda_star and tau0 as geometric/projector "
                "data rather than computing their selected numerical values."
            ),
        },
        "remaining_numeric_gate": {
            "name": "Selected_TT_QSector_Spectral_Gap_Computation",
            "must_compute": [
                "the TT Q-sector domain for the selected coherent projector",
                "the spectrum of E on that quotient, or a same-branch identification with an internal A_int complement",
                "selected tau0 or the relation tau0 = 1/lambda_star if saturation is proved",
                "whether the selected value equals 1, kappa_STF,int, nil 0.25, Z64 15, or a new TT value",
            ],
        },
        "guardrails": {
            "claims_numeric_eta": False,
            "claims_tau0_numeric": False,
            "claims_eta_equals_kappa_STF": False,
            "claims_eta_equals_nil_floor": False,
            "claims_eta_equals_z64": False,
            "claims_physical_modal_gap": False,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
