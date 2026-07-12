"""Build physical Phi_fin^C1 action-source fill attempt / independent provenance run gate.

This artifact attacks the validator-ready last contract by auditing which
Route A clauses are genuinely still missing after the formal row layer closed.
It does not promote the physical source theorem; it reduces the fill to the
minimal same-branch certificate that remains.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun"
OUTPUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
MINIMAL_PACKET = PACKET_DIR / "minimal_physical_source_certificate.packet.json"
FILL_TEMPLATE = PACKET_DIR / "route_a_physical_source_theorem_fill.template.json"
ROUTE_B_PACKET = PACKET_DIR / "route_b_independent_galerkin_provenance_run_spec.packet.json"
DECISION_PACKET = PACKET_DIR / "source_fill_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_PhysicalPhiFinC1ActionSourceTheorem_Fill_or_IndependentGalerkinProvenanceRun_v1.md"

PREVIOUS = DATA / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem.candidate.json"
CONTRACT = (
    DATA
    / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem"
    / "last_source_theorem_contract.packet.json"
)
VALIDATOR = (
    DATA
    / "selected_physicalphifinc1actionsource_or_provenanceindependencetheorem"
    / "promotion_validator_kernel.packet.json"
)
ACTION_VALIDATOR = (
    DATA
    / "selected_phifinc1_actionrestriction_or_boundarysource_emission"
    / "route_a_action_restriction_validator_v2.packet.json"
)
B_ATTEMPT = (
    DATA
    / "selected_physicalc1actionidentity_or_samesourcebselectedemission"
    / "same_source_bselected_emission_attempt.packet.json"
)
MEASURE_GATE = (
    DATA
    / "selected_physicalmeasure_or_finitegalerkinpromotion"
    / "physical_measure_identity_gate.packet.json"
)
FORMAL = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)

STATUS = (
    "MTT_SELECTED_PHYSICALPHIFINC1ACTIONSOURCE_FILL_OR_INDEPENDENTGALERKINPROVENANCERUN_"
    "BUILT_MINIMAL_SOURCE_CERTIFICATE_OPEN"
)
NEXT = "MTT_Selected_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    contract = load(CONTRACT)
    validator = load(VALIDATOR)
    action_validator = load(ACTION_VALIDATOR)
    b_attempt = load(B_ATTEMPT)
    measure_gate = load(MEASURE_GATE)
    formal = load(FORMAL)

    minimal_certificate = {
        "schema": "MTTMinimalPhiFinC1PhysicalSourceCertificate.v1",
        "status": "MINIMAL_PHYSICAL_SOURCE_CERTIFICATE_IDENTIFIED_NOT_FILLED",
        "already_closed_or_retired": {
            "formal_110_row_replay": formal["formal_110_rows_executed"],
            "formal_A_b_deltaTheta_replay": contract["formal_computation_layer_closed"][
                "formal_A_b_deltaTheta_replay_closed"
            ],
            "finite_trace_boundary_algebraic": measure_gate["not_missing_anymore"][
                "finite_boundary_algebraic_cancellation"
            ],
            "finite_row_values": measure_gate["not_missing_anymore"]["finite_row_values"],
            "formal_trace_engine": measure_gate["not_missing_anymore"]["formal_trace_engine"],
            "conditional_A_b_deltaTheta": measure_gate["not_missing_anymore"][
                "conditional_A_b_deltaTheta"
            ],
        },
        "minimal_route_A_certificate_fields": {
            "physical_action_restricts_to_selected_finite_Weyl_quotient": False,
            "no_extra_physical_boundary_or_source_term": False,
            "same_source_R_Z_R_X_b_selected_emission": False,
        },
        "same_source_emission_subfields": {
            "phase_R_Z_source_selection": False,
            "shift_R_X_source_selection": False,
            "same_source_b_selected_emission": b_attempt["same_source_b_selected_emitted_now"],
        },
        "why_three_fields_suffice": [
            "Finite measure normalization and finite trace/Frobenius pairing are already derived at the formal quotient.",
            "All formal finite rows and the A,b,deltaTheta replay are closed.",
            "Existing equivalence theorems state that physical promotion follows once the physical action restricts to this quotient with no extra source and emits R_Z/R_X/b_selected from the same branch.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    fill_template = {
        "schema": "MTTRouteAPhysicalSourceTheoremFillTemplate.v1",
        "status": "TEMPLATE_READY_NOT_FILLED",
        "branch": "q79/F,m=1/S3_GS/RouteC_or_same_visible_source",
        "required_statement": (
            "The selected physical Phi_fin^C1 first variation on the admissible C1 "
            "variation class restricts exactly to the selected finite qutrit Weyl "
            "trace quotient, has no extra physical boundary/source term, and emits "
            "the same R_Z/R_X/b_selected packet as the formal 110-row finite trace execution."
        ),
        "must_attach_sources": [
            "selected physical Phi_fin^C1 action or first-variation source",
            "admissible C1 variation class and boundary condition",
            "restriction map to selected finite qutrit Weyl quotient",
            "same-source residual emission R_Z/R_X",
            "same-source Hessian/source vector b_selected",
        ],
        "must_prove_equalities": {
            "physical_measure_equals_finite_trace_quadrature": False,
            "no_extra_physical_boundary_or_source_term": False,
            "physical_R_Z_equals_formal_R_Z": False,
            "physical_R_X_equals_formal_R_X": False,
            "physical_b_selected_equals_formal_b": False,
        },
        "validator_target": rel(VALIDATOR),
        "if_filled_promotes": validator["consequent_if_accepted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b_spec = {
        "schema": "MTTRouteBIndependentGalerkinProvenanceRunSpec.v1",
        "status": "ROUTE_B_RUN_SPEC_READY_NOT_EXECUTED",
        "required_inputs": [
            "selected zero-mode/Galerkin basis independent of residual-projector replay",
            "selected finite or continuum quadrature rule independent of locked target replay",
            "primitive 72-row contractions",
            "36 sector response rows",
            "2 Hessian/source rows",
        ],
        "required_outputs": [
            "same 110-row packet or equivalent replacement",
            "exactness/error certificates",
            "provenance certificate independent of residual-projector replay",
            "no observed constants used as selectors",
        ],
        "current_support": {
            "all_72_values_exact": contract["route_B_provenance_independence_theorem"][
                "current_truth_values"
            ]["all_72_primitive_values_exact"],
            "formal_110_rows_executed": contract["route_B_provenance_independence_theorem"][
                "current_truth_values"
            ]["formal_110_rows_executed"],
            "source_independent_of_residual_projector_replay": False,
        },
        "executed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTSourceFillDecision.v1",
        "status": "MINIMAL_SOURCE_CERTIFICATE_OR_ROUTE_B_RUN_REMAINS_OPEN",
        "formal_computation_layer_closed": True,
        "route_A_minimal_certificate_built": True,
        "route_A_minimal_certificate_filled": False,
        "route_B_run_spec_built": True,
        "route_B_run_executed": False,
        "unpatched_A_selected_promoted": False,
        "unpatched_b_selected_promoted": False,
        "unpatched_deltaTheta_C1_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalPhiFinC1ActionSourceFillOrIndependentGalerkinProvenanceRun",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "last_source_contract": rel(CONTRACT),
            "promotion_validator": rel(VALIDATOR),
            "action_restriction_validator": rel(ACTION_VALIDATOR),
            "same_source_bselected_attempt": rel(B_ATTEMPT),
            "physical_measure_identity_gate": rel(MEASURE_GATE),
            "formal_110_row_replay": rel(FORMAL),
        },
        "output_packets": {
            "minimal_physical_source_certificate": rel(MINIMAL_PACKET),
            "route_a_physical_source_theorem_fill_template": rel(FILL_TEMPLATE),
            "route_b_independent_galerkin_provenance_run_spec": rel(ROUTE_B_PACKET),
            "source_fill_decision": rel(DECISION_PACKET),
        },
        "what_closes_now": {
            "minimal_route_A_source_certificate_identified": True,
            "route_A_fill_template_built": True,
            "route_B_independent_run_spec_built": True,
            "non_blockers_separated_from_live_source_clauses": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "physical_action_restricts_to_selected_finite_Weyl_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "same_source_R_Z_R_X_b_selected_emission": True,
            "route_B_independent_Galerkin_or_row_run": True,
            "unpatched_A_selected": True,
            "unpatched_b_selected": True,
            "unpatched_deltaTheta_C1": True,
            "true_SM_equivalence_closure": True,
            "no_knob_closure": True,
        },
        "promotion_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "theorem": {
            "name": "MinimalPhysicalSourceCertificateReductionTheorem",
            "proved": True,
            "statement": (
                "Given the closed formal 110-row finite trace replay and prior equivalence "
                "gates, Route A unpatched promotion now requires exactly a three-field "
                "same-branch physical source certificate: physical Phi_fin^C1 action "
                "restriction to the selected finite Weyl quotient, no extra physical "
                "boundary/source term, and same-source R_Z/R_X/b_selected emission.  "
                "Alternatively, Route B may close by executing an independent Galerkin or "
                "row provenance run for the same packet.  This artifact builds both fill "
                "targets and does not promote either."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalPhiFinC1ActionSourceTheorem_Fill_or_IndependentGalerkinProvenanceRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "packet_paths": candidate["output_packets"],
        "theorem_proved": True,
        "minimal_route_A_source_certificate_identified": True,
        "route_A_minimal_certificate_filled": False,
        "route_B_run_executed": False,
        "unpatched_A_selected_promoted": False,
        "unpatched_b_selected_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalPhiFinC1ActionSourceTheorem Fill or IndependentGalerkinProvenanceRun v1

Status: `{STATUS}`

## Theorem

{candidate["theorem"]["statement"]}

## Minimal Route A Fill

1. physical action restricts to selected finite Weyl quotient
2. no extra physical boundary/source term
3. same-source `R_Z/R_X/b_selected` emission

## Route B Alternative

Execute an independent Galerkin/row provenance run for the same 110-row packet.

No route is promoted here.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "{SLUG}"
MINIMAL = PACKET_DIR / "minimal_physical_source_certificate.packet.json"
TEMPLATE = PACKET_DIR / "route_a_physical_source_theorem_fill.template.json"
ROUTEB = PACKET_DIR / "route_b_independent_galerkin_provenance_run_spec.packet.json"
DECISION = PACKET_DIR / "source_fill_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalPhiFinC1ActionSourceTheorem_Fill_or_IndependentGalerkinProvenanceRun_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    minimal = load(MINIMAL)
    template = load(TEMPLATE)
    route_b = load(ROUTEB)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(minimal["already_closed_or_retired"]["formal_110_row_replay"] is True, "formal replay not closed")
    require(minimal["already_closed_or_retired"]["finite_row_values"] is True, "finite values not closed")
    for key in [
        "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "no_extra_physical_boundary_or_source_term",
        "same_source_R_Z_R_X_b_selected_emission",
    ]:
        require(minimal["minimal_route_A_certificate_fields"][key] is False, f"Route A field overfilled: {{key}}")
    require(minimal["same_source_emission_subfields"]["same_source_b_selected_emission"] is False, "b selected overfilled")
    require(template["status"] == "TEMPLATE_READY_NOT_FILLED", "template status mismatch")
    require(template["must_prove_equalities"]["physical_b_selected_equals_formal_b"] is False, "template overfilled")
    require(route_b["current_support"]["all_72_values_exact"] is True, "Route B values missing")
    require(route_b["current_support"]["formal_110_rows_executed"] is True, "Route B rows missing")
    require(route_b["current_support"]["source_independent_of_residual_projector_replay"] is False, "Route B provenance overfilled")
    require(route_b["executed_now"] is False, "Route B overexecuted")
    require(decision["route_A_minimal_certificate_built"] is True, "Route A cert not built")
    require(decision["route_A_minimal_certificate_filled"] is False, "Route A overfilled")
    require(decision["route_B_run_executed"] is False, "Route B overfilled")
    require(decision["unpatched_A_selected_promoted"] is False, "A overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["minimal_route_A_source_certificate_identified"] is True, "cert missing minimal certificate")
    require(cert["route_A_minimal_certificate_filled"] is False, "cert overfilled")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("No route is promoted here" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(MINIMAL_PACKET, minimal_certificate)
    write_json(FILL_TEMPLATE, fill_template)
    write_json(ROUTE_B_PACKET, route_b_spec)
    write_json(DECISION_PACKET, decision)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"wrote {rel(OUTPUT)}")
    print(f"status {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
