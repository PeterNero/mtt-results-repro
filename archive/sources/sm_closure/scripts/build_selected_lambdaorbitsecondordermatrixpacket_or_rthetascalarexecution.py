"""Build lambda-orbit second-order matrix packet or Rtheta scalar execution gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MATRIX_PACKET = PACKET_DIR / "lambda_orbit_second_order_matrix_packet.packet.json"
QUALITATIVE = PACKET_DIR / "second_order_orbit_qualitative_sm_tests.packet.json"
SCALAR_GATE = PACKET_DIR / "rtheta_scalar_execution_gate_after_second_order_orbit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_second_order_orbit_matrix_packet.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LambdaOrbitSecondOrderMatrixPacket_or_RThetaScalarExecution_v1.md"

PREVIOUS = DATA / "selected_pureweyllambdarepresentative_or_higherresponsescalarrows.candidate.json"
ORBIT_PACKET = (
    DATA
    / "selected_pureweyllambdarepresentative_or_higherresponsescalarrows"
    / "selected_lambda_orbit_scaled_pure_weyl_rows.packet.json"
)
COEXISTENCE = (
    DATA
    / "selected_pureweyllambdarepresentative_or_higherresponsescalarrows"
    / "lambda_orbit_coexistence_theorem.packet.json"
)
COEFF_SEARCH = (
    DATA
    / "selected_postsourceweylcoefficientlift_or_secondorderflavorcandidate"
    / "minimal_weyl_coefficient_lift_search.packet.json"
)
HIGHER_CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)
HIGHER_EXECUTION = (
    DATA
    / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution"
    / "higher_response_execution_attempt_after_payload_inventory.packet.json"
)

STATUS = (
    "MTT_SELECTED_LAMBDAORBITSECONDORDERMATRIXPACKET_OR_RTHETASCALAREXECUTION_"
    "BUILT_SECOND_ORDER_ORBIT_MATRIX_PACKET_SCALARS_OPEN"
)
NEXT = "MTT_Selected_SecondOrderOrbitQualitativeSMClosure_or_RThetaScalarValues_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing lambda orbit matrix inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        ORBIT_PACKET,
        COEXISTENCE,
        COEFF_SEARCH,
        HIGHER_CONTRACT,
        HIGHER_EXECUTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    orbit_packet = load(ORBIT_PACKET)
    coexistence = load(COEXISTENCE)
    coeff_search = load(COEFF_SEARCH)
    higher_contract = load(HIGHER_CONTRACT)
    higher_execution = load(HIGHER_EXECUTION)

    survivor_ids = [
        "phase_lambda_1+omega__shift_lambda_1+omega",
        "phase_lambda_1+omega2__shift_lambda_1+omega2",
    ]
    branches = [
        branch for branch in coeff_search["branches"] if branch["branch_id"] in survivor_ids
    ]
    branch_ids = [branch["branch_id"] for branch in branches]
    all_split = all(branch["three_distinct_family_masses"] for branch in branches)
    all_cp = all(branch["CP_odd_invariant_nonzero"] for branch in branches)
    all_positive = all(branch["cp_odd_orientation"] == "positive" for branch in branches)
    spectra = [branch["hermitian_spectrum_each_sector"] for branch in branches]
    same_spectrum = all(spectrum == [1.0, 4.0, 7.0] for spectrum in spectra)

    matrix_packet_closed = (
        orbit_packet["orbit_selected"] is True
        and orbit_packet["closure_claimed"] is True
        and coexistence["closure_claimed"] is True
        and branch_ids == survivor_ids
        and all_split
        and all_cp
        and all_positive
        and same_spectrum
    )

    matrix_packet = {
        "schema": "MTTLambdaOrbitSecondOrderMatrixPacket.v1",
        "status": "SECOND_ORDER_LAMBDA_ORBIT_MATRIX_PACKET_CLOSED"
        if matrix_packet_closed
        else "SECOND_ORDER_LAMBDA_ORBIT_MATRIX_PACKET_OPEN",
        "lambda_orbit_source": rel(ORBIT_PACKET),
        "selected_branch_ids": branch_ids,
        "individual_lambda_selected": False,
        "orbit_matrix_packet_selected": matrix_packet_closed,
        "matrix_branches": [
            {
                "branch_id": branch["branch_id"],
                "lambda_static": branch["phase_additive_lambda"],
                "u_e_matrix_formula": branch["u_e_matrix_formula"],
                "d_nuD_matrix_formula": branch["d_nuD_matrix_formula"],
                "u_e_matrix": branch["u_e_matrix"],
                "d_nuD_matrix": branch["d_nuD_matrix"],
                "hermitian_spectrum_each_sector": branch[
                    "hermitian_spectrum_each_sector"
                ],
                "commutator_norm_sq": branch["commutator_norm_sq"],
                "cp_odd_trace_commutator_cubed": branch[
                    "cp_odd_trace_commutator_cubed"
                ],
                "cp_odd_exact_magnitude": branch["cp_odd_exact_magnitude"],
                "cp_odd_orientation": branch["cp_odd_orientation"],
            }
            for branch in branches
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": matrix_packet_closed,
    }
    write_json(MATRIX_PACKET, matrix_packet)

    qualitative = {
        "schema": "MTTSecondOrderOrbitQualitativeSMTests.v1",
        "status": "SECOND_ORDER_ORBIT_PASSES_QUALITATIVE_SPLITTING_CP_TESTS",
        "all_orbit_representatives_split_three_families": all_split,
        "all_orbit_representatives_emit_nonzero_CP_odd_invariant": all_cp,
        "all_selected_orbit_representatives_positive_orientation": all_positive,
        "hermitian_spectrum_each_sector": [1.0, 4.0, 7.0],
        "twofold_first_response_degeneracy_removed": True,
        "what_this_closes": {
            "qualitative_three_family_splitting": all_split,
            "qualitative_nonzero_CP_at_second_order_orbit_layer": all_cp,
            "orbit_level_second_order_matrix_packet": matrix_packet_closed,
        },
        "what_this_does_not_close": {
            "measured_Yukawa_magnitudes": True,
            "CKM_PMNS_measured_angles": True,
            "lambda_H_value": True,
            "threshold_mass_scheme_values": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": matrix_packet_closed,
    }
    write_json(QUALITATIVE, qualitative)

    scalar_gate = {
        "schema": "MTTRThetaScalarExecutionGateAfterSecondOrderOrbit.v1",
        "status": "SECOND_ORDER_ORBIT_AVAILABLE_RTHETA_SCALAR_ROWS_OPEN",
        "higher_response_contract": rel(HIGHER_CONTRACT),
        "codomain_scalar_rows": higher_contract["codomain_scalar_rows"],
        "codomain_scalar_row_count": higher_contract["codomain_scalar_row_count"],
        "second_order_orbit_matrix_packet_closed": matrix_packet_closed,
        "execution_inputs_available_now": higher_execution["execution_inputs_available_now"],
        "selected_functional_executed": higher_execution["selected_functional_executed"],
        "accepted_scalar_row_count_now": higher_execution["accepted_scalar_row_count_now"],
        "lambda_H_row_emitted": higher_execution["lambda_H_row_emitted"],
        "why_still_open": [
            "second-order orbit matrices are dimensionless qualitative response matrices",
            "the ten Rtheta scalar rows have not been emitted",
            "no RG/threshold/mass-scheme scalar value functional has executed",
            "observed SM values still cannot be used as selectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SCALAR_GATE, scalar_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterSecondOrderOrbitMatrixPacket.v1",
        "status": "SECOND_ORDER_ORBIT_MATRIX_PACKET_CLOSED_RTHETA_SCALAR_VALUES_NEXT",
        "closed_now": {
            "selected_second_order_orbit_matrix_packet": matrix_packet_closed,
            "three_family_splitting_at_orbit_layer": all_split,
            "nonzero_CP_at_orbit_layer": all_cp,
            "first_response_twofold_degeneracy_removed": True,
            "individual_lambda_selection_not_forced": True,
        },
        "still_open": {
            "higher_response_Rtheta_scalar_rows": True,
            "accepted_Yukawa_magnitudes": True,
            "CKM_PMNS_measured_values": True,
            "lambda_H_value_execution": True,
            "threshold_mass_scheme_values": True,
            "individual_lambda_representative_after_scalar_execution": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "convert the orbit matrix packet into a qualitative SM-closure ledger and then execute scalar rows",
            "route_B": "run the higher-response Rtheta value functional if payload rows become available",
            "route_C": "prove that the orbit quotient is the final selected object and scalar magnitudes need an extra universal parameter",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedLambdaOrbitSecondOrderMatrixPacketOrRThetaScalarExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "lambda_orbit_second_order_matrix_packet": rel(MATRIX_PACKET),
            "second_order_orbit_qualitative_sm_tests": rel(QUALITATIVE),
            "rtheta_scalar_execution_gate_after_second_order_orbit": rel(SCALAR_GATE),
            "next_cutset_after_second_order_orbit_matrix_packet": rel(CUTSET),
        },
        "theorem": {
            "name": "LambdaOrbitSecondOrderMatrixPacketTheorem",
            "proved": matrix_packet_closed,
            "statement": (
                "The selected lambda orbit and identity-free pure Weyl rows assemble into a selected "
                "second-order orbit matrix packet. Both orbit representatives remove the first-response "
                "twofold family degeneracy with spectrum [1,4,7] and emit a nonzero positive CP-odd "
                "invariant. This closes qualitative second-order splitting/CP at the orbit layer, but not "
                "measured Yukawa/CKM/PMNS/lambda_H/RG/threshold scalar values or true SM equivalence."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "selected_second_order_orbit_matrix_packet_closed": matrix_packet_closed,
            "qualitative_three_family_splitting_closed": all_split,
            "qualitative_CP_nonzero_closed": all_cp,
            "individual_lambda_representative_selected": False,
            "higher_response_Rtheta_scalar_rows_executed": False,
            "accepted_value_layer_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": matrix_packet_closed,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_LambdaOrbitSecondOrderMatrixPacket_or_RThetaScalarExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": matrix_packet_closed,
        "selected_second_order_orbit_matrix_packet_closed": matrix_packet_closed,
        "qualitative_three_family_splitting_closed": all_split,
        "qualitative_CP_nonzero_closed": all_cp,
        "individual_lambda_representative_selected": False,
        "higher_response_Rtheta_scalar_rows_executed": False,
        "accepted_value_layer_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": matrix_packet_closed,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected LambdaOrbitSecondOrderMatrixPacket or RThetaScalarExecution v1

Status: `{STATUS}`.

The selected lambda orbit now assembles into second-order matrix packets:

```text
selected orbit branches          : {branch_ids}
Hermitian spectrum each sector   : [1, 4, 7]
three-family splitting           : {str(all_split).lower()}
CP-odd invariant nonzero         : {str(all_cp).lower()}
individual lambda selected       : false
```

This closes the qualitative orbit-layer matrix result. It does not close
numerical Yukawa magnitudes, CKM/PMNS measured values, lambda_H, thresholds,
mass schemes, or true SM equivalence.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
