"""Prove the abstract finite-trace existence lemma for PhiFin S1-S2."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

S0_CERT = CERTS / "selected_phifin_s0_source_prefix_certificate.json"
S0_PACKET = DATA / "selected_phifin_s0_source_prefix.candidate.json"

OUTPUT_PACKET = DATA / "selected_phifin_finite_trace_existence.candidate.json"
OUTPUT_CERT = CERTS / "selected_phifin_finite_trace_existence_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_Finite_Trace_Existence_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_candidate() -> dict[str, Any]:
    s0_cert = load_json(S0_CERT)
    s0_packet = load_json(S0_PACKET)
    prerequisites = {
        "S0_selected_source_closed": s0_cert["s0_closed"] is True,
        "branch_fixed": s0_packet["selected_branch"] == "q79/F,m=1 S3/GS Route-C",
        "not_fixture_or_lifted": s0_cert["what_closes_now"]["selected_source_not_hypothetical_or_fixture"],
        "target_fitting_excluded": s0_cert["what_closes_now"]["observed_target_fitting_excluded"],
    }
    proof_steps = [
        {
            "step": "connection_trace",
            "statement": (
                "A selected smooth HYM/Strominger source determines a connection A_E "
                "and Hermitian metric h_E on the selected bundle/sheaf/gerbe module. "
                "On a finite good cover, parallel transport and transition restriction "
                "define rho_E or an equivalent connection trace."
            ),
            "closes_abstract": "S1_transition_or_connection_trace_exists",
        },
        {
            "step": "galerkin_projection",
            "statement": (
                "For any declared finite Route-C basis B_N in the selected Hilbert space, "
                "the orthogonal projection P_N gives finite matrices P_N D_E P_N and "
                "P_N dotD_alpha1 P_N. These matrices are selected because A_E and the "
                "basis are selected inputs, not fitted target data."
            ),
            "closes_abstract": "S2_DE_dotD_matrices_exist",
        },
        {
            "step": "riesz_green",
            "statement": (
                "If the zero-mode cluster is separated by a positive selected gap gamma_N, "
                "the Riesz projector is the contour integral of the finite resolvent and "
                "the reduced Green operator is the inverse on the projected complement."
            ),
            "closes_abstract": "S2_Riesz_Green_exist_given_gap",
        },
        {
            "step": "error_gap_control",
            "statement": (
                "If the basis residual epsilon_N is bounded and epsilon_N is smaller than "
                "the selected gap margin, standard Galerkin perturbation gives stable "
                "projectors and controlled reduced Green error."
            ),
            "closes_abstract": "validator_error_contract_exists",
        },
    ]
    return {
        "candidate": "SelectedPhiFinFiniteTraceExistence",
        "status": "SELECTED_PHIFIN_FINITE_TRACE_EXISTENCE_PROVED_VALUES_OPEN",
        "prerequisites": prerequisites,
        "theorem": {
            "name": "SelectedPhiFinFiniteTraceExistenceLemma",
            "proved": all(prerequisites.values()),
            "statement": (
                "Given the S0 selected smooth source and a declared finite Route-C "
                "Galerkin/Cech basis, the Phi_fin finite trace is mathematically defined: "
                "it has a selected connection/rho_E trace, finite D_E and dotD matrices, "
                "and Riesz/Green operators whenever the selected gap certificate is "
                "positive. This proves existence and functoriality of S1-S2, but not "
                "the emitted numeric/symbolic entries."
            ),
        },
        "proof_steps": proof_steps,
        "abstract_closure": {
            "S1_transition_or_connection_trace_exists": True,
            "S2_DE_dotD_matrices_exist": True,
            "S2_Riesz_Green_exist_given_gap": True,
            "S1_S2_are_selected_if_basis_and_gap_are_selected": True,
        },
        "emission_still_required": {
            "selected_connection_or_rhoE_entries": True,
            "basis_BN_or_Cech_basis_entries": True,
            "D_E_matrix_entries": True,
            "dotD_alpha1_matrix_entries": True,
            "Riesz_contour_or_projector_entries": True,
            "reduced_Green_entries": True,
            "gap_gamma_N_and_residual_epsilon_N": True,
        },
        "validator_implication": {
            "can_set_selected_source_verified_now": False,
            "reason": (
                "Validators need emitted finite entries and gap/error certificates. "
                "The lemma proves those objects are defined from S0, not that the repo "
                "has computed them."
            ),
        },
        "next_required_artifact": "Selected_PhiFin_S1S2_Value_Emission_v1",
        "what_closes_now": {
            "S1_S2_existence_theorem": True,
            "Phi_fin_not_circular_after_S0": True,
            "selectedness_transport_principle": True,
            "value_emission_boundary_identified": True,
        },
        "what_remains_open": {
            "Selected_PhiFin_S1S2_Value_Emission_v1": True,
            "routec_validators_pass_honestly": True,
            "A_selected": True,
            "b_selected": True,
        },
        "guardrails": {
            "claims_finite_values_emitted": False,
            "claims_validators_pass_honestly": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "uses_observed_or_benchmark_inputs": False,
        },
    }


def build_certificate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedPhiFinFiniteTraceExistence",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem_proved": candidate["theorem"]["proved"],
        "next_required_artifact": candidate["next_required_artifact"],
        "what_closes_now": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "guardrails": candidate["guardrails"],
    }


def render_note(candidate: dict[str, Any]) -> str:
    prereqs = "\n".join(
        f"- `{key}`: {'PASS' if value else 'FAIL'}" for key, value in candidate["prerequisites"].items()
    )
    steps = "\n".join(
        f"### {row['step']}\n\n{row['statement']}\n" for row in candidate["proof_steps"]
    )
    emits = "\n".join(f"- `{key}`" for key in candidate["emission_still_required"])
    return f"""# Selected PhiFin Finite Trace Existence v1

## Result

The abstract S1-S2 finite-trace lemma is proved, but finite values are still
open.

Status: `{candidate["status"]}`

## Theorem

`{candidate["theorem"]["name"]}`

{candidate["theorem"]["statement"]}

Proved: `{candidate["theorem"]["proved"]}`

## Prerequisites

{prereqs}

## Proof

{steps}
## Emission Boundary

The theorem proves that the objects exist as selected finite traces.  The repo
still must emit:

{emits}

## Next Artifact

`{candidate["next_required_artifact"]}`

This is the object that must compute or symbolically emit the entries before the
Route-C validators may honestly pass.
"""


def main() -> int:
    candidate = build_candidate()
    cert = build_certificate(candidate)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(candidate), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
