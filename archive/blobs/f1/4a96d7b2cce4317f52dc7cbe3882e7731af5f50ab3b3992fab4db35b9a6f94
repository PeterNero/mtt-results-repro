from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QG_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\12 Quantum Gravity"
) / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
QG_Z64_EVAL = (
    ROOT.parent
    / "18 Theta-Closure & Execution Program"
    / "_md_v3_corrected"
    / "Quantum_Gravity_Alignment_Evaluation_for_Z64_CKM_Closure_v1.md"
)
Z64_DAMPING = ROOT.parent / "mtt-nonsm-constants-no-knob" / "proof_corpus" / "Damping_Hessian_Z64_Block_Identification_v1.md"

TT_WINDOW_CERT = ROOT / "certificates" / "selected_tt_projector_window_normalization_lemma_certificate.json"
Z64_BRIDGE_CERT = ROOT / "certificates" / "conditional_z64_qg_gap_bridge_certificate.json"
STIFFNESS_CERT = ROOT / "certificates" / "gr_tt_stiffness_modal_gap_interface_certificate.json"

OUT_CERT = ROOT / "certificates" / "selected_tt_qsector_spectral_gap_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_tt_qsector_spectral_gap.template.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    tt_window = load_json(TT_WINDOW_CERT)
    z64_bridge = load_json(Z64_BRIDGE_CERT)
    stiffness = load_json(STIFFNESS_CERT)
    qg = read(QG_SOURCE)
    qg_z64 = read(QG_Z64_EVAL)
    z64 = read(Z64_DAMPING)

    source_tests = {
        "qg_defines_E_external_TT": has(qg, "Lichnerowicz operator on TT modes", "external block"),
        "qg_defines_Aint_internal_gap_block": has(
            qg,
            "$A_{\\mathrm{int}}$         operator      Internal block",
            "spectral gap",
        ),
        "qg_defines_full_A_as_direct_sum": "Full Hessian at the fixed point: $A=E\\oplus A_{\\mathrm{int}}$" in qg,
        "qg_states_blocks_commute": "[E,A_{\\mathrm{int}}]=0" in qg,
        "qg_states_TT_Q_gap_positive": has(
            qg,
            "projected linearized graviton operator on the TT sector",
            "spectrum bounded below by $\\lambda_\\ast>0$",
            "on the $Q$-sector",
        ),
        "qg_computes_numeric_TT_gap": False,
        "qg_selects_background_geometry_for_TT_spectrum": False,
        "qg_z64_alignment_conditional_not_identity": has(
            qg_z64,
            "mostly support it",
            "Identify the selected flavor Q-sector",
        ),
        "z64_numeric_gap_sourced": "lambda_* = 15." in z64,
    }

    candidate_rows = []
    for row in stiffness["computed_internal_tt_stiffness"]["rows"]:
        candidate_rows.append(
            {
                "N": row["N"],
                "kappa_STF_response_candidate": row["kappa_STF_int"],
                "closure_metric_candidate": 1.0,
                "z64_same_branch_candidate": 15.0,
                "selected_now": False,
            }
        )

    packet = {
        "artifact": "Selected_TT_QSector_Spectral_Gap_Computation",
        "closed_operator_data": {
            "external_TT_operator": "E = Lichnerowicz operator on TT modes",
            "internal_operator": "A_int with positive Q-sector gap",
            "full_fixed_point_Hessian": "A = E op A_int",
            "block_commutation": "[E, A_int] = 0",
            "TT_Q_gap_symbol": "lambda_star_TT",
        },
        "candidate_values": candidate_rows,
        "open_required_data": {
            "selected_TT_background_or_finite_quotient": None,
            "boundary_conditions_or_compact_slab_domain": None,
            "Q_sector_projector_for_TT": None,
            "eigenvalue_computation_for_E_on_Q_TT": None,
            "same_branch_identity_with_Z64_or_internal_Aint": None,
        },
        "forbidden_promotions": [
            "using positive lower bound lambda_star>0 as a numeric value",
            "using kappa_STF response rows as spectral gap",
            "using closure metric lambda=1 as selected gap",
            "using Z64 lambda=15 without same-branch TT Q-sector identity",
        ],
    }
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "selected_tt_qsector_spectral_gap",
        "status": "TT_QSECTOR_GAP_REDUCED_TO_OPERATOR_SPECTRUM_NUMERIC_VALUE_OPEN",
        "input_certificates": {
            "selected_tt_projector_window_normalization": str(TT_WINDOW_CERT),
            "conditional_z64_qg_gap_bridge": str(Z64_BRIDGE_CERT),
            "gr_tt_stiffness_modal_gap_interface": str(STIFFNESS_CERT),
        },
        "source_files": {
            "quantum_gravity": str(QG_SOURCE),
            "qg_z64_alignment": str(QG_Z64_EVAL),
            "z64_damping": str(Z64_DAMPING),
        },
        "source_tests": source_tests,
        "packet_written": str(OUT_PACKET),
        "closed_now": {
            "TT_Q_sector_operator_identified": True,
            "full_block_structure_identified": source_tests["qg_defines_full_A_as_direct_sum"],
            "block_commutation_sourced": source_tests["qg_states_blocks_commute"],
            "positive_gap_assumption_sourced": source_tests["qg_states_TT_Q_gap_positive"],
            "candidate_values_classified": True,
        },
        "candidate_gap_classification": {
            "closure_metric_1": {
                "available_as_formal_normalization": True,
                "selected_as_TT_Q_gap": False,
                "reason": "No source says the TT Q-sector spectral inner product is normalized to make the first eigenvalue one.",
            },
            "kappa_STF_rows": {
                "available_as_response_stiffness": True,
                "selected_as_TT_Q_gap": False,
                "rows": [
                    {"N": row["N"], "kappa_STF_int": row["kappa_STF_response_candidate"]}
                    for row in candidate_rows
                ],
                "reason": "Response stiffness is not the same datum as the Q-sector spectral bottom.",
            },
            "z64_15": {
                "available_as_exact_branch_gap": source_tests["z64_numeric_gap_sourced"],
                "conditional_bridge_closed": z64_bridge["verdict"]["conditional_bridge_closed"],
                "selected_as_TT_Q_gap": False,
                "reason": "The same-branch identity between TT Q-sector and exact Z64 central-circle tower is still not sourced.",
            },
            "new_TT_value": {
                "allowed": True,
                "selected_as_TT_Q_gap": False,
                "reason": "This is the honest route if the TT operator spectrum is computed directly.",
            },
        },
        "remaining_exact_gate": {
            "name": "Selected_TT_QSector_Eigenpacket",
            "must_supply": [
                "selected bounded-geometry TT background or finite quotient/slab",
                "TT Q-sector projector and boundary conditions",
                "explicit matrix/operator for E on the quotient",
                "lowest positive eigenvalue and multiplicity",
                "proof whether this eigenpacket is same-branch with internal A_int or Z64",
            ],
        },
        "guardrails": {
            "claims_numeric_TT_gap": False,
            "claims_tau0_numeric": False,
            "claims_gap_equals_1": False,
            "claims_gap_equals_kappa_STF": False,
            "claims_gap_equals_z64_15": False,
            "claims_physical_modal_gap": False,
        },
        "interpretation": {
            "advance": (
                "The TT modal-gap problem has been reduced from a normalization ambiguity "
                "to a concrete spectral eigenpacket for the projected Lichnerowicz operator "
                "on the selected TT Q-sector."
            ),
            "blocker": (
                "The current corpus does not provide the selected TT background/domain or "
                "a same-branch identity that would import the exact Z64 gap."
            ),
        },
        "previous_status": tt_window["status"],
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
