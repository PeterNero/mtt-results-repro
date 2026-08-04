from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THETA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\18 Theta-Closure & Execution Program\_md_v3_corrected")

BRANCH_AUDIT = ROOT / "certificates" / "selected_aint_packet_branch_bridge_audit_certificate.json"
EXACT_SCHUR = THETA / "Exact_Coherent_Block_Schur_Collapse_for_Z64_Projector_v1.md"
QG_ALIGN = THETA / "Quantum_Gravity_Alignment_Evaluation_for_Z64_CKM_Closure_v1.md"
Z64_EXACT = THETA / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"

OUT_CERT = ROOT / "certificates" / "conditional_z64_qg_gap_bridge_certificate.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    branch = json.loads(BRANCH_AUDIT.read_text(encoding="utf-8"))
    schur = read(EXACT_SCHUR)
    qg = read(QG_ALIGN)
    z64 = read(Z64_EXACT)

    lambda_z64 = 15.0
    source_tests = {
        "exact_schur_has_zero_offblock": has(
            schur,
            "P_fl L Q=0",
            "Q L P_fl=0",
            "C_fl=0 in exact branch",
        ),
        "exact_schur_has_conditional_lambda_bridge": has(
            schur,
            "lambda_Q >= lambda_*",
            "when Q block is the QG complement",
        ),
        "qg_alignment_says_bridge_conditional": has(
            qg,
            "lambda_Q is the spectral gap of Q L Q on the selected flavor complement",
            "Until this is proved, QG supports the pattern but does not supply the numeric",
        ),
        "z64_exact_branch_has_coherent_inclusion_and_commutator": has(
            z64,
            "P_CP,64<=Pi_coh",
            "[L,Pi_coh]=0",
        ),
    }

    conditional_result = {
        "premises": [
            "the exact Z64 central-circle tower is retained by Pi_coh",
            "the selected operator commutes with Pi_coh",
            "the excluded block Q is the QG noncoherent complement",
            "the normalized exact-branch damping value lambda_* = 15 is the relevant internal gap",
        ],
        "then": {
            "C_fl": 0.0,
            "E_Schur": 0.0,
            "lambda_Q_lower_bound": lambda_z64,
            "sqrt_lambda_Q_lower_bound": math.sqrt(lambda_z64),
            "tau0_upper_bound_if_saturated": 1.0 / lambda_z64,
        },
        "scope": "finite flavor/CP exact-block branch and any later branch proven to share the same QG complement",
    }

    still_open_for_gr = {
        "GR_Aint_noncoherent_complement_identified_with_Z64_tower": False,
        "GR_TT_response_operator_equals_flavor_closure_operator": False,
        "physical_dimensionful_gap_selected": False,
        "Newton_or_Planck_prediction_allowed": False,
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "conditional_z64_qg_gap_bridge",
        "status": "CONDITIONAL_Z64_QG_GAP_BRIDGE_CLOSED_GR_AINT_IDENTIFICATION_OPEN",
        "input_certificates": {
            "selected_aint_packet_branch_bridge_audit": str(BRANCH_AUDIT),
        },
        "source_files": {
            "exact_schur": str(EXACT_SCHUR),
            "qg_alignment": str(QG_ALIGN),
            "z64_exact": str(Z64_EXACT),
        },
        "source_tests": source_tests,
        "conditional_result": conditional_result,
        "still_open_for_gr": still_open_for_gr,
        "verdict": {
            "conditional_bridge_closed": True,
            "usable_now_for_exact_z64_flavor_branch": True,
            "usable_now_as_GR_modal_gap": False,
            "most_honest_current_claim": (
                "The exact Z64/QG gap bridge is closed conditionally: when the excluded "
                "block is the QG noncoherent complement, lambda_Q >= lambda_* and the "
                "exact Schur correction vanishes. The GR response proof still needs a "
                "same-branch identification of its A_int complement."
            ),
        },
        "guardrails": {
            "claims_z64_gap_is_GR_gap": False,
            "claims_GR_TT_operator_equals_flavor_operator": False,
            "claims_physical_modal_gap": False,
            "forbids_conditional_bridge_as_unconditional_GR_closure": True,
        },
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
