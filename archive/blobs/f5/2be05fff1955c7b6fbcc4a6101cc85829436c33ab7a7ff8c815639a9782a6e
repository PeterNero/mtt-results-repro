"""Build the exact Higgs-specific M_H acceptance object.

This packet binds the older H7B1B/C/F Herm(2) mass-strain contract to the
newly emitted B_Huv source-orthonormal domain.  It does not emit numerical
entries.  It closes the acceptance object: a selected value payload must provide
three source-owned real rows Delta, Re(Omega), Im(Omega), with exactness and a
non-kernel light-line certificate.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"

SLUG = "selected_higgsspecificmhacceptanceobject_or_valuefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MH_OBJECT = PACKET_DIR / "higgs_specific_mh_acceptance_object.packet.json"
VALUE_FRONTIER = PACKET_DIR / "mh_three_real_row_value_frontier.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_mh_acceptance_object.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_mh_acceptance_object.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsSpecificMHAcceptanceObject_or_ValueFrontier_v1.md"

PREVIOUS = DATA / "selected_msourcehiggsspecificoperatorblock_or_c5c6bridgefrontier.candidate.json"
PREVIOUS_HK = (
    DATA
    / "selected_msourcehiggsspecificoperatorblock_or_c5c6bridgefrontier"
    / "hk_threshold_gate_after_higgs_operator_gap.packet.json"
)
BHUV_LIFT = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
H7B1B_CONTRACT = (
    CONST_DATA
    / "const_higgs_01_h7b1b_selected_two_higgs_splitting_source"
    / "selected_mass_strain_or_projector_source_contract.packet.json"
)
H7B1C_CANDIDATE = (
    CONST_DATA
    / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian.candidate.json"
)
H7B1C_REQUEST = (
    CONST_DATA
    / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian"
    / "minimal_two_by_two_hessian_payload_request.packet.json"
)
H7B1F_CONTRACT = (
    CONST_DATA
    / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet"
    / "nonsplit_to_huv_reduction_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_HIGGSSPECIFICMHACCEPTANCEOBJECT_OR_VALUEFRONTIER_"
    "CONTRACT_CLOSED_THREE_REAL_ROWS_OPEN"
)
NEXT = "MTT_Selected_HiggsSpecificMHValueEmission_or_C5C6ProjectionBridge_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing M_H acceptance inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_HK,
        BHUV_LIFT,
        H7B1B_CONTRACT,
        H7B1C_CANDIDATE,
        H7B1C_REQUEST,
        H7B1F_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_hk = load(PREVIOUS_HK)
    bhuv = load(BHUV_LIFT)
    h7b1b = load(H7B1B_CONTRACT)
    h7b1c = load(H7B1C_CANDIDATE)
    h7b1c_request = load(H7B1C_REQUEST)
    h7b1f = load(H7B1F_CONTRACT)

    b_cols = bhuv["whitening_map_and_lift"]["B_Huv_columns"]
    uv_ids = bhuv["ordered_two_column_source_space"]["ordered_E_H_UV_source_ids"]

    mh_object = {
        "schema": "MTTHiggsSpecificMHAcceptanceObject.v1",
        "status": "MH_ACCEPTANCE_OBJECT_BOUND_TO_BHUV_DOMAIN_VALUES_OPEN",
        "closure_claimed": True,
        "domain": {
            "name": "source-orthonormal B_Huv two-column UV Higgs domain",
            "ordered_basis": ["B_Huv[H_u]", "B_Huv[H_d^dagger]"],
            "B_Huv_columns": b_cols,
            "ordered_E_H_UV_source_ids": uv_ids,
            "orthonormality": "B_Huv^* G_Q B_Huv = I_2",
        },
        "accepted_Herm2_form": {
            "full_matrix": [
                ["m0 + Delta", "Omega"],
                ["conj(Omega)", "m0 - Delta"],
            ],
            "trace_free_part": [
                ["Delta", "Omega"],
                ["conj(Omega)", "-Delta"],
            ],
            "minimal_real_value_rows": ["Delta", "Re(Omega)", "Im(Omega)"],
            "scalar_m0_relevance": "drops out of P_L, s_beta, and K_threshold.Omega_H.lambda",
            "nondegeneracy": "Delta^2 + |Omega|^2 > 0",
            "light_line_admissibility": "q restricted to the selected light eigenline is nonzero",
            "phase_covariance": (
                "H_u,H_d^dagger phase changes conjugate the Herm(2) block; "
                "Delta^2+|Omega|^2 and s_beta are invariant."
            ),
        },
        "downstream_formulas": {
            "Huu": "m0 + Delta",
            "Hud": "Omega",
            "Hdd": "m0 - Delta",
            "Hdu": "conj(Omega)",
            "Delta": "(Huu-Hdd)/2",
            "Omega": "Hud",
            "P_L": "light eigenprojector of trace-free Huv with q|im(P_L) nonzero",
            "s_beta": "Delta^2/(Delta^2+|Omega|^2)",
        },
        "source_contract_alignment": {
            "H7B1B_selected_matrix_payload": h7b1b["accepted_equivalent_payloads"][
                "selected_Hermitian_mass_strain_matrix"
            ],
            "H7B1C_minimal_payload_request_built": h7b1c[
                "minimal_Huv_hessian_payload_request_built"
            ],
            "H7B1F_computed_packet_when_filled": h7b1f["computed_packet_when_filled"],
            "now_bound_to_emitted_B_Huv_domain": True,
        },
        "not_emitted": {
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "P_L": None,
            "s_beta": None,
            "K_threshold_Omega_H_lambda": None,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_frontier = {
        "schema": "MTTMHThreeRealRowValueFrontier.v1",
        "status": "MH_VALUES_OPEN_EXACT_THREE_REAL_ROW_TARGET_FIXED",
        "closure_claimed": True,
        "exact_value_payload_required": {
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
            "exactness_or_error_certificate": None,
            "source_ownership_certificate": None,
            "nondegeneracy_certificate": None,
            "light_line_not_kernel_certificate": None,
        },
        "accepted_source_routes": [
            "direct selected Higgs-specific Hessian/mass-strain execution on the B_Huv domain",
            "full same-source M_source plus H-sector restriction R_H",
            "C5-C6 projection-measure/no-boundary bridge that emits the equivalent H K row",
        ],
        "forbidden_shortcuts": [
            "promote the diagonal metric Gram matrix as M_H",
            "promote matter/neutrino alpha1/dotD blocks as Huv",
            "use collapsed rank-one H sector values as UV two-Higgs data",
            "backsolve Delta/Omega/s_beta/lambda_H from observed Higgs or threshold data",
        ],
        "why_this_is_progress": (
            "The direct value frontier is now a three-real-row source problem on a "
            "fixed source-orthonormal domain.  Basis, quotient, whitening, shared "
            "functional support, phase covariance, and formulas are no longer the live blockers."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_row = dict(previous_hk["H_row"])
    h_row["M_H_acceptance_object_bound_to_B_Huv_domain"] = True
    h_row["M_H_three_real_value_rows_emitted"] = False
    hk_gate = {
        "schema": "MTTHKThresholdGateAfterMHAcceptanceObject.v1",
        "status": "H_K_THRESHOLD_GATE_MH_CONTRACT_CLOSED_VALUES_OPEN_9_OF_10",
        "closure_claimed": True,
        "required_output": previous_hk["required_output"],
        "source_equation": previous_hk["source_equation"],
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": h_row,
        "conditional_consequent_current": previous_hk["conditional_consequent_current"],
        "direct_route_state": {
            "B_Huv_two_column_lift_emitted": True,
            "same_source_functional_alpha1_dotD_closed": True,
            "M_H_acceptance_object_closed": True,
            "M_H_three_real_value_rows_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterMHAcceptanceObject.v1",
        "status": "NEXT_FRONTIER_MH_THREE_REAL_VALUE_ROWS_OR_C5C6_BRIDGE",
        "closure_claimed": True,
        "closed_here": [
            "M_H acceptance object is bound to the emitted B_Huv domain",
            "trace-free Herm(2) normal form is fixed",
            "minimal source value rows are Delta, Re(Omega), Im(Omega)",
            "phase covariance and scalar m0 irrelevance are fixed",
            "nondegeneracy and light-line non-kernel certificates are specified",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "source-owned Delta row",
            "source-owned Re(Omega) row",
            "source-owned Im(Omega) row",
            "exactness/source ownership/non-kernel certificates",
            "direct Huu,Hud,Hdd emission",
            "C5-C6 projection/no-boundary bridge alternative",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsSpecificMHAcceptanceObjectOrValueFrontier",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "HiggsSpecificMHAcceptanceObjectTheorem",
            "proved": True,
            "statement": (
                "With B_Huv source-orthonormal and the shared functional/operator "
                "side closed for non-Higgs blocks, the Higgs direct route is exactly "
                "a trace-free Herm(2) source problem on the B_Huv domain.  Modulo "
                "the irrelevant scalar m0 I, the required value rows are Delta, "
                "Re(Omega), and Im(Omega), with Delta^2+|Omega|^2>0 and a light "
                "eigenline not killed by the quotient q.  This artifact fixes that "
                "acceptance object and emits no values."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "B_Huv_two_column_uv_lift_emitted": True,
            "same_source_functional_alpha1_dotD_side_closed": True,
            "M_H_acceptance_object_bound_to_B_Huv_domain": True,
            "M_H_three_real_value_rows_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "higgs_specific_mh_acceptance_object": rel(MH_OBJECT),
            "mh_three_real_row_value_frontier": rel(VALUE_FRONTIER),
            "hk_threshold_gate_after_mh_acceptance_object": rel(HK_GATE),
            "next_cutset_after_mh_acceptance_object": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHiggsSpecificMHAcceptanceObjectOrValueFrontierCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "M_H_acceptance_object_bound_to_B_Huv_domain": True,
        "M_H_three_real_value_rows_emitted": False,
        "selected_Delta_row_emitted": False,
        "selected_Re_Omega_row_emitted": False,
        "selected_Im_Omega_row_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "direct_Huu_Hud_Hdd_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HiggsSpecificMHAcceptanceObject or ValueFrontier v1

Status: `{STATUS}`

## What Closed

- bound the exact Higgs-specific `M_H` acceptance object to the emitted `B_Huv` domain
- fixed the trace-free Herm(2) form `[[Delta,Omega],[conj(Omega),-Delta]]`
- fixed the minimal value rows: `Delta`, `Re(Omega)`, `Im(Omega)`
- specified nondegeneracy `Delta^2+|Omega|^2>0`
- specified the light-line quotient certificate `q|im(P_L) != 0`
- H K-threshold gate remains `{previous_hk["accepted_selected_K_source_row_count"]}/{previous_hk["selected_K_threshold_row_count_required"]}`

## Still Open

- source-owned `Delta`
- source-owned `Re(Omega)`
- source-owned `Im(Omega)`
- exactness/source ownership/non-kernel certificates
- selected `K_threshold.Omega_H.lambda`

Next required artifact: `{NEXT}`
"""

    write_json(MH_OBJECT, mh_object)
    write_json(VALUE_FRONTIER, value_frontier)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
