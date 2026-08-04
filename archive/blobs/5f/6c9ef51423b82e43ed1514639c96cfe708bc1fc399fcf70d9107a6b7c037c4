"""Build the M_H three-row source-functional contract or C5-C6 bridge packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONST_DATA = TEXPAPERS / "mtt-individual-constants-source-search" / "candidate_data"

SLUG = "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTIONAL = PACKET_DIR / "mh_three_row_source_functional_contract.packet.json"
EXECUTION_TABLE = PACKET_DIR / "mh_three_row_execution_table_request.packet.json"
C5C6 = PACKET_DIR / "c5c6_bridge_execution_contract.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_three_row_functional.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_three_row_functional.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MHThreeRowSourceFunctional_or_C5C6BridgeExecution_v1.md"

PREVIOUS = DATA / "selected_mhvalueemissionsearch_or_c5c6bridgefrontier.candidate.json"
PREVIOUS_HK = (
    DATA
    / "selected_mhvalueemissionsearch_or_c5c6bridgefrontier"
    / "hk_threshold_gate_after_mh_value_search.packet.json"
)
MH_OBJECT = (
    DATA
    / "selected_higgsspecificmhacceptanceobject_or_valuefrontier"
    / "higgs_specific_mh_acceptance_object.packet.json"
)
UNDERDET = (
    DATA
    / "selected_mhvalueemissionsearch_or_c5c6bridgefrontier"
    / "herm2_underdetermination_no_promotion.packet.json"
)
H7B1C_REQUEST = (
    CONST_DATA
    / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian"
    / "minimal_two_by_two_hessian_payload_request.packet.json"
)
H7B1C_SEARCH = (
    CONST_DATA
    / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian"
    / "hessian_source_search.packet.json"
)
H7B1I_FUNCTOR = (
    CONST_DATA
    / "const_higgs_01_h7b1i_msource_from_selected_response_prefix"
    / "msource_acceptance_functor.packet.json"
)
H7B1J_DYNAMIC = (
    CONST_DATA
    / "const_higgs_01_h7b1j_dynamic_hessian_or_hsector_restriction_export"
    / "dynamic_hessian_edge_export_attempt.packet.json"
)
H7B1W_BINDING = (
    CONST_DATA
    / "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
    / "finite_trace_binding_attempt.packet.json"
)
H7B1Z_CUTSET = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "remaining_payload_cutset.packet.json"
)

STATUS = (
    "MTT_SELECTED_MHTHREEROWSOURCEFUNCTIONAL_OR_C5C6BRIDGEEXECUTION_"
    "ROW_FUNCTIONAL_CLOSED_SOURCE_TABLE_OPEN"
)
NEXT = "MTT_Selected_HResponseHessianTable_or_C5C6BridgeProof_v1"


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
        raise FileNotFoundError("missing three-row functional inputs: " + ", ".join(missing))


def trace2(a: list[list[complex]], b: list[list[complex]]) -> complex:
    return sum(a[i][j] * b[j][i] for i in range(2) for j in range(2))


def extraction_test() -> dict[str, Any]:
    delta, re_omega, im_omega = 3.0, -2.0, 5.0
    h = [
        [complex(delta, 0), complex(re_omega, im_omega)],
        [complex(re_omega, -im_omega), complex(-delta, 0)],
    ]
    sigma_z = [[1 + 0j, 0j], [0j, -1 + 0j]]
    sigma_x = [[0j, 1 + 0j], [1 + 0j, 0j]]
    sigma_y_mtt = [[0j, 1j], [-1j, 0j]]
    extracted = {
        "Delta": (0.5 * trace2(h, sigma_z)).real,
        "Re_Omega": (0.5 * trace2(h, sigma_x)).real,
        "Im_Omega": (0.5 * trace2(h, sigma_y_mtt)).real,
    }
    return {
        "test_matrix": "[[3,-2+5i],[-2-5i,-3]]",
        "extracted": extracted,
        "passes": extracted == {"Delta": delta, "Re_Omega": re_omega, "Im_Omega": im_omega},
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_HK,
        MH_OBJECT,
        UNDERDET,
        H7B1C_REQUEST,
        H7B1C_SEARCH,
        H7B1I_FUNCTOR,
        H7B1J_DYNAMIC,
        H7B1W_BINDING,
        H7B1Z_CUTSET,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_hk = load(PREVIOUS_HK)
    mh_object = load(MH_OBJECT)
    underdet = load(UNDERDET)
    h7b1c_request = load(H7B1C_REQUEST)
    h7b1c_search = load(H7B1C_SEARCH)
    h7b1i_functor = load(H7B1I_FUNCTOR)
    h7b1j_dynamic = load(H7B1J_DYNAMIC)
    h7b1w_binding = load(H7B1W_BINDING)
    h7b1z_cutset = load(H7B1Z_CUTSET)

    row_test = extraction_test()

    functional = {
        "schema": "MTTMHThreeRowSourceFunctionalContract.v1",
        "status": "ROW_FUNCTIONAL_EXTRACTION_CONTRACT_CLOSED_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "domain": mh_object["domain"],
        "accepted_trace_free_form": mh_object["accepted_Herm2_form"]["trace_free_part"],
        "row_basis": {
            "Delta": {
                "matrix": [[1, 0], [0, -1]],
                "functional": "Delta = (1/2) Tr(H_tf sigma_z)",
            },
            "Re_Omega": {
                "matrix": [[0, 1], [1, 0]],
                "functional": "Re(Omega) = (1/2) Tr(H_tf sigma_x)",
            },
            "Im_Omega": {
                "matrix": [[0, "i"], ["-i", 0]],
                "functional": "Im(Omega) = (1/2) Tr(H_tf sigma_y^MTT), sigma_y^MTT=[[0,i],[-i,0]]",
            },
        },
        "extraction_self_test": row_test,
        "source_functional_definition": {
            "direct_Hessian_route": (
                "Given a selected finite action/response functional S_H on the "
                "B_Huv domain, Huv_ab = d^2 S_H / dz_a d(conj z_b)|_0, "
                "H_tf = Huv - (Tr Huv/2)I, then the three row functionals above "
                "emit Delta, Re(Omega), Im(Omega)."
            ),
            "full_operator_route": h7b1i_functor["formal_construction_when_payload_exists"],
            "C5C6_bridge_route": (
                "If C5 proves trace-to-H7B1U/projection-measure equality and C6 "
                "proves no-extra-boundary/source cancellation, the bridge may emit "
                "the H K row directly without fitting Delta/Omega."
            ),
        },
        "acceptance_predicate": {
            "same_branch": "q=79/F/m=1 or a theorem-selected successor branch",
            "source_owned": "S_H, H_response, M_source, R_H, or C5-C6 bridge is selected before replay",
            "exactness": "finite exactness/residual/convergence certificate is supplied",
            "Hermitian": "Huv = Huv^* in the B_Huv source metric",
            "non_scalar": "Delta^2 + Re(Omega)^2 + Im(Omega)^2 > 0",
            "light_line": "q restricted to im(P_L) is nonzero",
            "no_target_fit": "no observed Higgs, beta, mass, Yukawa, CKM, PMNS, or threshold target selects entries",
        },
        "values_emitted": {
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "P_L": None,
            "s_beta": None,
        },
    }

    execution_table = {
        "schema": "MTTMHThreeRowExecutionTableRequest.v1",
        "status": "SELECTED_H_RESPONSE_TABLE_REQUIRED_VALUES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "minimal_table": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Hdu_equals_conj_Hud_certificate": None,
            "same_source_exactness_or_error_certificate": None,
            "source_ownership_certificate": None,
            "quotient_admissibility_certificate": None,
        },
        "row_reduction_when_table_exists": {
            "Delta": "(Huu-Hdd)/2",
            "Re_Omega": "Re(Hud)",
            "Im_Omega": "Im(Hud)",
            "s_beta": "Delta^2/(Delta^2+Re(Omega)^2+Im(Omega)^2)",
            "K_threshold_route": "selected s_beta or equivalent H quartic/threshold functional feeds K_threshold.Omega_H.lambda",
        },
        "current_sources_do_not_fill_table": {
            "H7B1C_values_currently_emitted": h7b1c_request["matrix_required"]["values_currently_emitted"],
            "H7B1C_search_selected_Huu_Hud_Hdd_found": h7b1c_search["result"][
                "selected_Huu_Hud_Hdd_found"
            ],
            "H7B1J_dynamic_exported": h7b1j_dynamic["export_decision"][
                "H_response_exported"
            ],
            "current_underdetermination_closed": underdet["theorem"]["proved"],
        },
    }

    c5c6 = {
        "schema": "MTTC5C6BridgeExecutionContract.v1",
        "status": "C5C6_EXECUTION_CONTRACT_CLOSED_PAYLOAD_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "bridge_name": h7b1w_binding["bridge_criterion"]["name"],
        "C5_required": [
            "trace-to-H7B1U grid identity for the diagonal HYM replay",
            "Higgs projection/reduction measure equals normalized finite trace",
            "same-source E_H^UV metric binding to the selected finite basis",
            "finite-to-smooth convergence, exact finite quotient identity, or residual/error certificate",
        ],
        "C6_required": [
            "no-extra-boundary/source proof",
            "proof no boundary or gauge convention term selects the H row",
        ],
        "current_closed_support": h7b1w_binding["closed_support"],
        "current_missing_payload": h7b1w_binding["missing_payload"],
        "h7b1z_remaining_cutset": h7b1z_cutset["still_open"],
        "values_emitted_by_bridge_now": {
            "trace_to_H7B1U_grid_identity": False,
            "projection_measure_equality": False,
            "no_extra_boundary_source": False,
            "K_threshold_Omega_H_lambda": False,
        },
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterThreeRowFunctional.v1",
        "status": "H_K_THRESHOLD_GATE_FUNCTIONAL_CONTRACT_CLOSED_VALUES_OPEN_9_OF_10",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            **previous_hk["H_row"],
            "three_row_source_functional_contract_closed": True,
            "selected_H_response_table_emitted": False,
            "C5C6_bridge_execution_contract_closed": True,
            "C5C6_bridge_payload_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "conditional_consequent_current": {
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterThreeRowFunctional.v1",
        "status": "NEXT_FRONTIER_H_RESPONSE_HESSIAN_TABLE_OR_C5C6_PROOF",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "Pauli/Riesz extraction functional for Delta, Re(Omega), Im(Omega)",
            "minimal H_response/Huv table request fixed",
            "full M_source+R_H route tied to H7B1I acceptance functor",
            "C5-C6 bridge execution contract fixed",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "selected H_response Hessian table Huu,Hud,Hdd",
            "or full same-source M_source plus H-sector restriction R_H",
            "or C5 trace-to-H7B1U/projection-measure proof",
            "and C6 no-extra-boundary/source proof",
            "nondegeneracy and quotient-admissibility certificates after values emit",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedMHThreeRowSourceFunctionalOrC5C6BridgeExecution",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorem": {
            "name": "MHThreeRowSourceFunctionalContractTheorem",
            "proved": True,
            "statement": (
                "On the already emitted source-orthonormal B_Huv domain, any "
                "selected trace-free Herm(2) Huv block has unique coordinates "
                "Delta, Re(Omega), Im(Omega), extracted by the three Pauli/Riesz "
                "functionals.  Therefore the remaining data burden is no longer "
                "a basis or formula question: it is exactly an emitted selected "
                "H_response/Huv table, a full M_source+R_H restriction, or a "
                "C5-C6 bridge proof feeding the H K row."
            ),
        },
        "closure_decision": {
            "B_Huv_two_column_uv_lift_emitted": True,
            "M_H_acceptance_object_bound_to_B_Huv_domain": True,
            "MH_three_row_source_functional_contract_closed": True,
            "MH_three_row_execution_table_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "C5C6_bridge_execution_contract_closed": True,
            "C5C6_bridge_payload_emitted": False,
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
            "mh_three_row_source_functional_contract": rel(FUNCTIONAL),
            "mh_three_row_execution_table_request": rel(EXECUTION_TABLE),
            "c5c6_bridge_execution_contract": rel(C5C6),
            "hk_threshold_gate_after_three_row_functional": rel(HK_GATE),
            "next_cutset_after_three_row_functional": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTTSelectedMHThreeRowSourceFunctionalOrC5C6BridgeExecutionCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "MH_three_row_source_functional_contract_closed": True,
        "extraction_self_test_passes": row_test["passes"],
        "MH_three_row_execution_table_emitted": False,
        "selected_Delta_row_emitted": False,
        "selected_Re_Omega_row_emitted": False,
        "selected_Im_Omega_row_emitted": False,
        "C5C6_bridge_execution_contract_closed": True,
        "C5C6_bridge_payload_emitted": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "accepted_internal_scalar_value_row_count": 0,
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected MHThreeRowSourceFunctional or C5C6BridgeExecution v1

Status: `{STATUS}`

## What Closed

- closed the Pauli/Riesz extraction functional for `Delta`, `Re(Omega)`, and `Im(Omega)` on the emitted source-orthonormal `B_Huv` domain
- fixed the minimal selected execution table: `Huu`, `Hud`, `Hdd`, Hermiticity, exactness/source ownership, nondegeneracy, and quotient-admissibility certificates
- tied the full-operator route to H7B1I: `Huv = B_Huv^* M_source B_Huv` after selected `M_source+R_H`
- fixed the C5-C6 bridge execution contract: C5 trace/projection equality plus C6 no-extra-boundary/source proof
- H K-threshold gate remains `{previous_hk["accepted_selected_K_source_row_count"]}/{previous_hk["selected_K_threshold_row_count_required"]}`

## Still Open

- selected `H_response`/`Huv` table values `Huu,Hud,Hdd`
- or full same-source `M_source+R_H`
- or selected C5-C6 proof emitting the H `K_threshold` row
- strict `Omega/lambda_H` scalar execution

Next required artifact: `{NEXT}`
"""

    write_json(FUNCTIONAL, functional)
    write_json(EXECUTION_TABLE, execution_table)
    write_json(C5C6, c5c6)
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
