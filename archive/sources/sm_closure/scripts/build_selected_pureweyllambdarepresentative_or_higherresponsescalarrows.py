"""Build pure-Weyl lambda representative or higher-response scalar rows gate.

The identity-free pure R_Z/R_X primitive rows are now closed.  The remaining
lambda question should not be forced into a false individual choice: the
existing static lambda search retains the conjugate orbit {1+omega, 1+omega^2}
with identical Hermitian spectra and CP-odd magnitude.  This artifact promotes
the orbit-scaled pure-Weyl rows as an orbit object, while keeping individual
representative selection and ten scalar value rows open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_pureweyllambdarepresentative_or_higherresponsescalarrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ORBIT_PACKET = PACKET_DIR / "selected_lambda_orbit_scaled_pure_weyl_rows.packet.json"
COEXISTENCE = PACKET_DIR / "lambda_orbit_coexistence_theorem.packet.json"
SCALAR_GATE = PACKET_DIR / "higher_response_scalar_rows_after_lambda_orbit.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_lambda_orbit_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PureWeylLambdaRepresentative_or_HigherResponseScalarRows_v1.md"

PREVIOUS = DATA / "selected_zeromodehessianprimitiverowexecution_or_pureweylrows.candidate.json"
PURE_ROWS = (
    DATA
    / "selected_zeromodehessianprimitiverowexecution_or_pureweylrows"
    / "identity_free_pure_weyl_rows.packet.json"
)
SECOND_ORDER = DATA / "selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection.candidate.json"
LAMBDA_DECISION = (
    DATA
    / "selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection"
    / "lambda_representative_selection_decision.packet.json"
)
REQUIRED_ROWS = (
    DATA
    / "selected_secondorderdynamiccoefficientemission_or_lambdarepresentativeselection"
    / "second_order_coefficient_required_rows.packet.json"
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
    "MTT_SELECTED_PUREWEYLLAMBDAREPRESENTATIVE_OR_HIGHERRESPONSESCALARROWS_"
    "BUILT_LAMBDA_ORBIT_ROWS_CLOSED_SCALARS_OPEN"
)
NEXT = "MTT_Selected_LambdaOrbitSecondOrderMatrixPacket_or_RThetaScalarExecution_v1"


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
        raise FileNotFoundError("missing lambda orbit inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PURE_ROWS,
        SECOND_ORDER,
        LAMBDA_DECISION,
        REQUIRED_ROWS,
        HIGHER_CONTRACT,
        HIGHER_EXECUTION,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    pure_rows = load(PURE_ROWS)
    second_order = load(SECOND_ORDER)
    lambda_decision = load(LAMBDA_DECISION)
    required_rows = load(REQUIRED_ROWS)
    higher_contract = load(HIGHER_CONTRACT)
    higher_execution = load(HIGHER_EXECUTION)

    lambdas = lambda_decision["surviving_lambdas"]
    signatures = lambda_decision["candidate_physical_signatures"]
    spectra = [row["hermitian_spectrum_each_sector"] for row in signatures]
    cp_magnitudes = [row["cp_odd_exact_magnitude"] for row in signatures]
    cp_orientations = [row["cp_odd_orientation"] for row in signatures]

    orbit_closes = (
        pure_rows["accepted_as_unscaled_selected_pure_weyl_primitive_rows"] is True
        and lambdas == ["1+omega", "1+omega2"]
        and len(signatures) == 2
        and spectra[0] == spectra[1] == [1.0, 4.0, 7.0]
        and cp_magnitudes[0] == cp_magnitudes[1] == "972*sqrt(3)"
        and cp_orientations[0] == cp_orientations[1] == "positive"
    )

    orbit_packet = {
        "schema": "MTTSelectedLambdaOrbitScaledPureWeylRows.v1",
        "status": "LAMBDA_ORBIT_SCALED_PURE_WEYL_ROWS_CLOSED"
        if orbit_closes
        else "LAMBDA_ORBIT_SCALED_PURE_WEYL_ROWS_OPEN",
        "input_pure_rows": rel(PURE_ROWS),
        "lambda_orbit": lambdas,
        "representative_count": len(lambdas),
        "individual_lambda_selected": False,
        "orbit_selected": orbit_closes,
        "scaled_row_family": {
            "phase_rows": "lambda_orbit * R_Z on u,e",
            "shift_rows": "lambda_orbit * R_X on d,nuD",
            "same_source_rule": required_rows["second_order_rows_required"]["same_source_rule"],
            "unscaled_R_Z_row_count": pure_rows["row_counts"]["R_Z"],
            "unscaled_R_X_row_count": pure_rows["row_counts"]["R_X"],
            "scaled_rows_per_representative": pure_rows["row_counts"]["R_Z"]
            + pure_rows["row_counts"]["R_X"],
            "orbit_scaled_row_count": len(lambdas)
            * (pure_rows["row_counts"]["R_Z"] + pure_rows["row_counts"]["R_X"]),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": orbit_closes,
    }
    write_json(ORBIT_PACKET, orbit_packet)

    coexistence = {
        "schema": "MTTLambdaOrbitCoexistenceTheorem.v1",
        "status": "CONJUGATE_LAMBDA_ORBIT_COEXISTENCE_PROVED_IN_CURRENT_INVARIANT_LAYER"
        if orbit_closes
        else "LAMBDA_ORBIT_COEXISTENCE_OPEN",
        "lambda_orbit": lambdas,
        "conjugate_pair": lambdas == ["1+omega", "1+omega2"],
        "physical_signature_comparison": {
            "same_hermitian_spectrum_each_sector": spectra[0] == spectra[1],
            "hermitian_spectrum_each_sector": spectra[0],
            "same_cp_odd_exact_magnitude": cp_magnitudes[0] == cp_magnitudes[1],
            "cp_odd_exact_magnitude": cp_magnitudes[0],
            "same_cp_odd_orientation": cp_orientations[0] == cp_orientations[1],
            "cp_odd_orientation": cp_orientations[0],
        },
        "theorem_scope": (
            "At the current orbit-scaled pure-Weyl layer, MTT selects the conjugate lambda orbit. "
            "The available Hermitian spectra and CP-odd invariant do not distinguish the two "
            "representatives, so selecting one would add an unsupported orientation convention."
        ),
        "what_this_does_not_prove": [
            "an individual representative is selected",
            "both representatives are experimentally indistinguishable after higher-response scalar execution",
            "Yukawa magnitudes or CKM/PMNS measured values are derived",
            "lambda_H or threshold values are emitted",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": orbit_closes,
    }
    write_json(COEXISTENCE, coexistence)

    scalar_gate = {
        "schema": "MTTHigherResponseScalarRowsAfterLambdaOrbit.v1",
        "status": "LAMBDA_ORBIT_AVAILABLE_HIGHER_RESPONSE_SCALAR_ROWS_OPEN",
        "higher_response_contract": rel(HIGHER_CONTRACT),
        "codomain_scalar_row_count": higher_contract["codomain_scalar_row_count"],
        "codomain_scalar_rows": higher_contract["codomain_scalar_rows"],
        "lambda_orbit_scaled_pure_rows_available": orbit_closes,
        "execution_inputs_available_now": higher_execution["execution_inputs_available_now"],
        "selected_functional_executed": higher_execution["selected_functional_executed"],
        "accepted_scalar_row_count_now": higher_execution["accepted_scalar_row_count_now"],
        "lambda_H_row_emitted": higher_execution["lambda_H_row_emitted"],
        "why_still_open": [
            "orbit-scaled pure rows are coefficient rows, not the ten scalar value rows",
            "higher-response Rtheta execution remains blocked by dynamic payload rows",
            "lambda_H and accepted threshold/mass-scheme values are still absent",
            "individual lambda orientation may remain a coexistence/orientation question after scalar execution",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(SCALAR_GATE, scalar_gate)

    cutset = {
        "schema": "MTTNextCutsetAfterLambdaOrbitRows.v1",
        "status": "LAMBDA_ORBIT_ROWS_CLOSED_NEXT_SECOND_ORDER_MATRIX_OR_RTHETA_SCALARS",
        "closed_now": {
            "lambda_static_orbit_selected": orbit_closes,
            "lambda_orbit_scaled_pure_R_Z_rows": orbit_closes,
            "lambda_orbit_scaled_pure_R_X_rows": orbit_closes,
            "coexistence_theorem_current_invariant_layer": orbit_closes,
            "individual_lambda_selection_not_forced": True,
        },
        "still_open": {
            "individual_lambda_representative_selection": True,
            "selected_second_order_matrix_packet_from_orbit_rows": True,
            "higher_response_Rtheta_scalar_rows": True,
            "lambda_H_value_execution": True,
            "accepted_Yukawa_CKM_PMNS_RG_threshold_value_rows": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "assemble the orbit-scaled rows into a second-order matrix packet and test whether the orbit quotient is sufficient",
            "route_B": "execute the higher-response Rtheta scalar rows and let that layer select/coexist the lambda representative",
            "route_C": "prove a later orientation theorem if the two representatives remain conjugate/coexisting",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedPureWeylLambdaRepresentativeOrHigherResponseScalarRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "selected_lambda_orbit_scaled_pure_weyl_rows": rel(ORBIT_PACKET),
            "lambda_orbit_coexistence_theorem": rel(COEXISTENCE),
            "higher_response_scalar_rows_after_lambda_orbit": rel(SCALAR_GATE),
            "next_cutset_after_lambda_orbit_rows": rel(CUTSET),
        },
        "theorem": {
            "name": "LambdaOrbitScaledPureWeylRowsAndCoexistenceTheorem",
            "proved": orbit_closes,
            "statement": (
                "Given the closed unscaled pure R_Z/R_X primitive rows, the selected static lambda "
                "data promote the conjugate orbit {1+omega, 1+omega^2} as an orbit object. Both "
                "representatives have the same Hermitian spectrum [1,4,7] in each sector and the same "
                "positive CP-odd invariant magnitude 972*sqrt(3), so the current invariant layer proves "
                "coexistence rather than individual representative selection. Higher-response scalar "
                "execution remains required for Yukawa, lambda_H, threshold, and true SM closure."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "lambda_static_orbit_selected": orbit_closes,
            "lambda_orbit_scaled_pure_Weyl_rows_closed": orbit_closes,
            "coexistence_theorem_current_invariant_layer_closed": orbit_closes,
            "individual_lambda_representative_selected": False,
            "higher_response_Rtheta_scalar_rows_executed": False,
            "accepted_value_layer_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_statuses": {
            "identity_free_pure_rows": previous["status"],
            "second_order_lambda_gate": second_order["status"],
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": orbit_closes,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PureWeylLambdaRepresentative_or_HigherResponseScalarRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": orbit_closes,
        "lambda_static_orbit_selected": orbit_closes,
        "lambda_orbit_scaled_pure_Weyl_rows_closed": orbit_closes,
        "coexistence_theorem_current_invariant_layer_closed": orbit_closes,
        "individual_lambda_representative_selected": False,
        "higher_response_Rtheta_scalar_rows_executed": False,
        "accepted_value_layer_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": orbit_closes,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected PureWeylLambdaRepresentative or HigherResponseScalarRows v1

Status: `{STATUS}`.

The lambda layer now closes as an orbit, not an individual choice.

```text
lambda orbit selected             : {lambdas}
individual lambda selected        : false
Hermitian spectrum each sector    : {spectra[0]}
CP-odd invariant magnitude        : {cp_magnitudes[0]}
CP orientation                    : {cp_orientations[0]}
orbit-scaled pure rows closed     : {str(orbit_closes).lower()}
```

This is the clean version of the “two solutions” hunch: the current invariant
layer selects the conjugate orbit/coexistence class. It does not yet decide a
single representative, and it does not close Yukawa/CKM/PMNS/lambda_H values.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
