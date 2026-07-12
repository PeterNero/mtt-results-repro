"""Build the selected Qa/SU3 finite cochain construction plan artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"

INPUT = DATA / "inverse_qa_su3_first_search_run.candidate.json"
OUTPUT_DATA = DATA / "selected_qa_su3_finite_cochain_construction_plan.candidate.json"
OUTPUT_CERT = CERTS / "selected_qa_su3_finite_cochain_construction_plan_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Selected_Qa_SU3_Finite_Cochain_Construction_Plan_v1.md"

QA_INPUTS = {
    "finite_cochain_or_de_response_gate": QA / "candidate_data" / "finite_cochain_packet_or_de_response_gate.candidate.json",
    "selected_finite_source_solve_attempt": QA / "candidate_data" / "selected_finite_source_solve_attempt.candidate.json",
    "source_augmentation_packet": QA / "candidate_data" / "source_augmentation_packet.candidate.json",
    "twisted_section_ring_gate": QA / "candidate_data" / "twisted_section_ring_and_gerbe_source_gate.candidate.json",
    "full_nil_theta_cocycle_equations": QA / "candidate_data" / "full_nil_theta_cocycle_equations.candidate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
        }
        for key, path in QA_INPUTS.items()
    }


def build_lifted_packet(inputs: dict[str, dict[str, object]]) -> dict[str, object]:
    source = inputs["source_augmentation_packet"]
    twist = inputs["twisted_section_ring_gate"]
    gate = inputs["finite_cochain_or_de_response_gate"]
    return {
        "spaces": source["required_section_spaces"],
        "space_count": len(source["required_section_spaces"]),
        "typed_product_pairs": gate["typed_product_pairs"],
        "typed_product_pair_count": gate["typed_product_pair_count"],
        "product_tests": source["product_tests"],
        "twisted_section_requirements": twist["twisted_section_requirements"],
        "typed_multiplication_law": twist["typed_multiplication_law"],
        "gf_zero_equation": gate["gf_zero_equation"],
        "structural_checks": {
            "eleven_spaces_present": len(source["required_section_spaces"]) == 11,
            "five_product_pairs_present": gate["typed_product_pair_count"] == 5,
            "all_pair_charges_land_in_P": source["obstruction_tests"]["all_pair_charges_land_in_P"] is True,
            "all_twist_cancellations_verified": all(row["twist_cancellation_verified"] for row in twist["typed_multiplication_law"]),
            "basis_values_supplied": False,
            "multiplication_constants_supplied": False,
            "selected_f_g_entries_supplied": False,
        },
    }


def build_construction_steps() -> list[dict[str, object]]:
    return [
        {
            "id": "C1_select_source_convention",
            "goal": "Fix the left/right nil quotient convention and selected Gamma action.",
            "needed_output": "source_id plus generator actions g1..g6 in the selected convention",
            "status": "OPEN",
        },
        {
            "id": "C2_solve_full_nil_theta_cocycle",
            "goal": "Build Phi_q for all eleven charges, including central commutator response.",
            "needed_output": "charge-to-factor map q -> a_q(gamma,z) with cocycle and c1 proof",
            "status": "OPEN",
        },
        {
            "id": "C3_construct_section_or_cochain_bases",
            "goal": "Compute selected bases for F1..F5, G1..G5, and P.",
            "needed_output": "basis(S) or finite cochain complexes with cohomology basis extraction",
            "status": "OPEN",
        },
        {
            "id": "C4_compute_product_tables",
            "goal": "Compute m_i: F_i x G_i -> P in selected bases.",
            "needed_output": "selected product tables and mu_i read from those tables",
            "status": "OPEN",
        },
        {
            "id": "C5_extract_f_g_entries",
            "goal": "Read f_i=a_i and g_i=b_i from the same selected bases.",
            "needed_output": "selected f,g matrices with g*f=0 checked after selection",
            "status": "OPEN",
        },
        {
            "id": "C6_bridge_operator_response",
            "goal": "Tie the cochain packet to same-source D_E/dotD/rho_E.",
            "needed_output": "non-identity operator packet, projectors, Green/Riesz/heat/torsion exit",
            "status": "OPEN",
        },
        {
            "id": "C7_admissibility_retention",
            "goal": "Run Freed-Witten, GS/Bianchi, stability/local-freeness, and projector-retention checks.",
            "needed_output": "mapped-source admissibility certificate",
            "status": "OPEN",
        },
    ]


def build_attempt_result(inputs: dict[str, dict[str, object]]) -> dict[str, object]:
    solve = inputs["selected_finite_source_solve_attempt"]
    nil = inputs["full_nil_theta_cocycle_equations"]
    return {
        "attempted_now": True,
        "current_source_no_go_imported": solve["finite_solve_results"]["current_sources_close_last_part"] is False,
        "negative_scope": solve["last_part_resolution"]["proved_negative_scope"],
        "not_mathematically_impossible": solve["last_part_resolution"]["not_proved"],
        "primary_remaining_object": solve["last_part_resolution"]["primary_remaining_object"],
        "ordinary_full_nil_theta_solver_values_open": nil["status"] == "FULL_NIL_THETA_COCYCLE_EQUATIONS_BUILT_SOLVER_VALUES_OPEN",
        "blocked_reasons": [
            "selected finite bases absent",
            "selected product tables/mu_i absent",
            "selected f,g entries absent",
            "selected D_E/dotD/rho_E source absent",
            "full nil theta cocycle solver values open",
            "current corpus no-go for selected Qa/SU3 operator source",
        ],
    }


def build_candidate() -> dict[str, object]:
    input_data = load_json(INPUT)
    inputs = {key: load_json(path) for key, path in QA_INPUTS.items()}
    packet = build_lifted_packet(inputs)
    attempt = build_attempt_result(inputs)
    return {
        "candidate": "MTTSelectedQaSU3FiniteCochainConstructionPlan",
        "status": "SELECTED_QA_SU3_FINITE_COCHAIN_CONSTRUCTION_PLAN_BUILT_ATTEMPT_BLOCKED_BY_CURRENT_SOURCE_NO_GO",
        "input_status": input_data["status"],
        "source_status": source_status(),
        "lifted_packet": packet,
        "construction_steps": build_construction_steps(),
        "attempt_result": attempt,
        "candidate_primitive_ansatz_policy": {
            "primitive_one_generator_scaffold_allowed": True,
            "primitive_one_generator_scaffold_promoted": False,
            "reason": "One formal generator per typed space is useful as a computation scaffold, but selected bases and product tables are not supplied.",
            "forbidden_move": "Do not choose a_i, b_i, or mu_i merely to satisfy gf=0.",
        },
        "gate_results": {
            "construction_plan_built": True,
            "eleven_spaces_lifted": packet["structural_checks"]["eleven_spaces_present"],
            "five_product_pairs_lifted": packet["structural_checks"]["five_product_pairs_present"],
            "charge_products_land_in_P": packet["structural_checks"]["all_pair_charges_land_in_P"],
            "twist_cancellation_lifted": packet["structural_checks"]["all_twist_cancellations_verified"],
            "attempted_selected_source_solve": True,
            "current_source_no_go_imported": attempt["current_source_no_go_imported"],
            "selected_finite_cochain_packet_supplied": False,
            "selected_operator_source_supplied": False,
            "primitive_scaffold_promoted": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_Qa_SU3_Operator_Source_Import_Audit_v1",
        "target_fitting_used": False,
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTSelectedQaSU3FiniteCochainConstructionPlan",
        "status": "MTT_SELECTED_QA_SU3_FINITE_COCHAIN_CONSTRUCTION_PLAN_BUILT_ATTEMPT_BLOCKED_BY_CURRENT_SOURCE_NO_GO",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "finite_cochain_construction_plan": True,
            "eleven_space_packet_lifted": True,
            "five_product_pair_packet_lifted": True,
            "twist_cancellation_and_P_target_checks_lifted": True,
            "current_source_no_go_imported": True,
            "primitive_convenience_scaffold_not_promoted": True,
        },
        "what_remains_open": {
            "selected_nil_theta_cocycle_values": True,
            "selected_11_space_bases": True,
            "selected_product_tables_or_mu_i": True,
            "selected_f_g_matrix_entries": True,
            "selected_DE_dotD_or_rhoE_operator_source": True,
            "Freed_Witten_GS_Bianchi_and_projector_checks": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {body['path']} ({'present' if body['present'] else 'missing'})"
        for key, body in candidate["source_status"].items()
    )
    spaces = "\n".join(
        f"- `{row['id']}` charge `{row['charge']}` role `{row['role']}`"
        for row in candidate["lifted_packet"]["spaces"]
    )
    products = "\n".join(
        f"- `{row['pair'][0]} x {row['pair'][1]} -> P`, charge sum `{row['charge_sum']}`, lands in P `{row['lands_in_P']}`"
        for row in candidate["lifted_packet"]["product_tests"]
    )
    steps = "\n".join(
        f"### {row['id']}\n\n"
        f"- Goal: {row['goal']}\n"
        f"- Needed output: {row['needed_output']}\n"
        f"- Status: `{row['status']}`\n"
        for row in candidate["construction_steps"]
    )
    blocked = "\n".join(f"- {item}" for item in candidate["attempt_result"]["blocked_reasons"])
    not_proved = "\n".join(f"- {item}" for item in candidate["attempt_result"]["not_mathematically_impossible"])
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Selected Qa/SU3 Finite Cochain Construction Plan v1

## Purpose

This artifact tries the top route from the inverse Qa/SU3 first search run:
construct the selected finite Cech/Dolbeault cochain packet.

It closes the construction plan and imports the scoped current-source no-go
from the Qa/SU3 repo.

This does not claim that Qa/SU3 closure is mathematically impossible.

It also does not promote a primitive convenience scaffold as selected data.

## Source Inputs

{sources}

## Lifted Eleven-Space Packet

{spaces}

## Lifted Product Tests

{products}

## Construction Steps

{steps}

## Attempt Result

The construction was attempted against the current source record and remains
blocked.

Blocked reasons:

{blocked}

Negative scope:

```text
{candidate["attempt_result"]["negative_scope"]}
```

What is not proved:

{not_proved}

Primary remaining object:

```text
{candidate["attempt_result"]["primary_remaining_object"]}
```

## Primitive Scaffold Policy

A one-generator-per-space scaffold may be used for computation, but it is not a
selected packet.  In particular, choosing `a_i`, `b_i`, or `mu_i` merely to
satisfy:

```text
{candidate["lifted_packet"]["gf_zero_equation"]}
```

is still rejected.

## Construction Plan Theorem

The finite cochain route is the best-ranked route and has strong structural
support: eleven spaces, five typed products landing in `P`, and twisted-product
cancellation.  However, the current source record does not supply the selected
nil-theta cocycle values, selected bases, selected product tables, selected
`f,g` entries, or selected same-source operator response.

Therefore the construction plan is closed, but the selected Qa/SU3 packet
remains open.

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

```text
{candidate["next_required_artifact"]}
```
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    note_text = render_note(candidate, certificate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note_text, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
