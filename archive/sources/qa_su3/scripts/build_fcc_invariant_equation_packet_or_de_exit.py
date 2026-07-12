"""Build the FCC invariant-equation packet or D_E exit gate for Qa/SU3."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT_SELECTOR = DATA / "central_period_selector_search.candidate.json"
INPUT_PERIOD = DATA / "ctwist_period_normalization_or_a01_exit.candidate.json"
INPUT_BIANCHI = DATA / "chern_bianchi_source_packet_candidates.candidate.json"
INPUT_OPERATOR = DATA / "a01_de_operator_exit_gate.candidate.json"
OUTPUT_DATA = DATA / "fcc_invariant_equation_packet_or_de_exit.candidate.json"
OUTPUT_CERT = CERTS / "fcc_invariant_equation_packet_or_de_exit_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_FCC_Invariant_Equation_Packet_or_DE_Exit_v1.md"


def main() -> None:
    selector = json.loads(INPUT_SELECTOR.read_text(encoding="utf-8"))
    period = json.loads(INPUT_PERIOD.read_text(encoding="utf-8"))
    bianchi = json.loads(INPUT_BIANCHI.read_text(encoding="utf-8"))
    operator = json.loads(INPUT_OPERATOR.read_text(encoding="utf-8"))
    row = next(
        item
        for item in bianchi["candidate_packets"]
        if item["id"] == "iwasawa_abelian_two_line_flux_row"
    )

    s_required = period["scalar_period_gate"]["numeric_R4_over_alpha_prime_for_A_unit"]
    two_pi_squared = (2.0 * math.pi) ** 2
    equations = [
        {
            "id": "bianchi_invariant_alpha1",
            "equation": row["data"]["bianchi_equation"],
            "source": "iwasawa_abelian_two_line_flux_row",
            "role": "componentwise Green-Schwarz/Bianchi support in the invariant Iwasawa slice",
            "selected_values": {
                "flux_choice": row["data"]["flux_choice"],
                "u1": row["data"]["u"][0],
            },
            "free_variables_after_equation": ["R^4/alpha_prime"],
        },
        {
            "id": "ctwist_amplitude",
            "equation": "A^2 = (2*pi)^2 / (1 + 2*s), where s=R^4/alpha_prime",
            "source": "ctwist_period_normalization_or_a01_exit",
            "role": "central c-twist transgression amplitude in the isotropic Iwasawa slice",
            "free_variables_after_equation": ["A", "s"],
        },
        {
            "id": "primitive_c_unit",
            "equation": "A=1",
            "source": "complex_rotated_ctwist_normalization plus period gate",
            "role": "promotion condition for the scaled primitive central slants to absolute c=+/-1 twists",
            "implied_solution": {
                "s": "((2*pi)^2 - 1)/2",
                "numeric": s_required,
            },
            "selected_by_current_source": False,
        },
    ]
    unknown_slots = {
        "integer_flux_holonomy_variables": [
            "which integer flux/holonomy entries beyond (1,2,0)+(-1,-2,0) are selected for Qa/SU3",
            "whether those integer entries constrain s=R^4/alpha_prime",
        ],
        "primitivity_constraints": [
            "primitive period unit for the central gerbe/transgression class",
            "finite central quotient if the period unit is torsion rather than real-scaled",
        ],
        "operator_exit": [
            "same-source D_E/rho_E matrices",
            "endomorphism_E or zero-order Weitzenbock block",
            "heat/spectrum/zeta/torsion finite part",
        ],
    }
    fcc_tests = [
        {
            "test_id": "bianchi_plus_ctwist_equations",
            "passes": True,
            "closes": "The invariant Bianchi row and c-twist amplitude can be placed in one finite algebraic packet.",
            "does_not_close": "The packet still has free s=R^4/alpha_prime until A=1 or a finite quotient is selected.",
        },
        {
            "test_id": "A_unit_as_equation_not_selector",
            "passes": True,
            "closes": "Adding A=1 produces the exact scalar s=((2*pi)^2-1)/2.",
            "does_not_close": "This is a promotion condition, not a source-selected integer/flux equation.",
        },
        {
            "test_id": "integer_data_selection",
            "passes": False,
            "closes": "No closure.",
            "does_not_close": "The available integer flux row fixes support on alpha1 but does not select s or a finite central quotient.",
        },
        {
            "test_id": "DE_exit_availability",
            "passes": False,
            "closes": "No closure.",
            "does_not_close": "The operator gate remains built but selected matrices/finite response are open.",
        },
    ]
    packet_closed = all(test["passes"] for test in fcc_tests)
    candidate = {
        "candidate": "SelectedQaSU3FCCInvariantEquationPacketOrDEExit",
        "status": "FCC_INVARIANT_EQUATION_PACKET_BUILT_PERIOD_AND_OPERATOR_VALUES_OPEN",
        "input_statuses": {
            "central_period_selector": selector["status"],
            "period_gate": period["status"],
            "chern_bianchi": bianchi["status"],
            "operator_exit": operator["status"],
        },
        "finite_equation_packet": {
            "variables": ["s=R^4/alpha_prime", "A", "r3^2/R^4", "integer flux/holonomy data"],
            "equations": equations,
            "derived_if_A_unit_imposed": {
                "s": "((2*pi)^2 - 1)/2",
                "numeric_s": s_required,
                "two_pi_squared": two_pi_squared,
            },
            "unknown_slots": unknown_slots,
        },
        "fcc_tests": fcc_tests,
        "gate_results": {
            "finite_invariant_equation_packet_written": True,
            "componentwise_bianchi_row_included": True,
            "ctwist_amplitude_included": True,
            "A_unit_condition_solves_s": True,
            "A_unit_condition_source_selected": False,
            "integer_data_selects_s_or_finite_quotient": False,
            "same_source_DE_or_rhoE_exit_available": False,
            "qa_su3_packet_closed": packet_closed,
            "closure_claimed": False,
        },
        "decision": {
            "result": "FCC packet built, but it does not close the period.",
            "why": "The finite invariant equations are now explicit; the missing datum is exactly the selector that makes A=1 source-selected or replaces it with a finite central quotient.",
            "correct_next_step": "Use this packet as a validator for any amended source. Otherwise proceed through selected D_E/rho_E matrices.",
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3FCCInvariantEquationPacketOrDEExit",
        "status": "QA_SU3_FCC_INVARIANT_EQUATION_PACKET_BUILT_PERIOD_AND_OPERATOR_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "finite_equation_packet_written": True,
            "Bianchi_and_ctwist_equations_combined": True,
            "A_unit_scalar_solution_rederived": True,
            "integer_data_gap_isolated": True,
        },
        "what_remains_open": {
            "source_selected_A_unit_or_finite_quotient": True,
            "selected_integer_flux_holonomy_solution": True,
            "selected_D_E_or_rho_E_operator_exit": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_Selected_DE_or_RhoE_Matrix_Source_Hunt_v1",
        "alternative_required_artifact": "Amended_Selected_Qa_SU3_FCC_Integer_Source_Packet_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 FCC Invariant Equation Packet or D_E Exit v1

This packet instantiates the superset/FCC route suggested by the central period
selector search.

## Equations

```text
8*(2*pi)^2 - 8*r3^2/R^4 = (16/alpha_prime)*r3^2
A^2 = (2*pi)^2 / (1 + 2*s),  s = R^4/alpha_prime
A=1  =>  s = ((2*pi)^2 - 1)/2 = {s_required:.15f}
```

## Result

The finite invariant equation packet is now explicit.  It combines the same
Iwasawa Bianchi row and the complex-rotated c-twist amplitude.  But it still
does not select the period: `A=1` is the promotion condition, not an independent
source equation.

The current integer flux row fixes the invariant support, not the absolute
central period unit.  So the gerbe-period route remains conditional.

## Next

The next proof object must be selected `D_E/rho_E` matrix data, unless an
amended source supplies the missing FCC integer/finite quotient selector.

```text
Selected_Qa_SU3_Selected_DE_or_RhoE_Matrix_Source_Hunt_v1
```

closure claimed: no
target fitting used: no
"""
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
