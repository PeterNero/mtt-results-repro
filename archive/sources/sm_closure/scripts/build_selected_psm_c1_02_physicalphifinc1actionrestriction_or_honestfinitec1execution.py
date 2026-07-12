"""Build PSM-C1-02 SI-1u-A1 physical source-certificate frontier.

This binds the existing physical Phi_fin^C1 source-certificate reduction into
the PSM-C1-02 label system: the remaining unpatched action lemma is exactly a
three-field same-branch certificate, with honest finite-C1 execution retained
as the replacement route.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
THREE_FIELD = BASE / "si1u_a1_three_field_physical_source_certificate.packet.json"
ROUTE_A_TEMPLATE = BASE / "route_a_physical_source_theorem_template_import.packet.json"
ROUTE_B_SPEC = BASE / "route_b_honest_finite_c1_execution_spec_import.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PhysicalPhiFinC1ActionRestriction_or_HonestFiniteC1Execution_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution.candidate.json"
SOURCE_FILL = DATA / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun.candidate.json"
MIN_CERT = DATA / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun" / "minimal_physical_source_certificate.packet.json"
ROUTE_A_FILL = DATA / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun" / "route_a_physical_source_theorem_fill.template.json"
ROUTE_B_RUN = DATA / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun" / "route_b_independent_galerkin_provenance_run_spec.packet.json"
DECISION = DATA / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun" / "source_fill_decision.packet.json"
PSM_OWNERSHIP = DATA / "selected_psm_c1_02_physicalactionowns_finitetracekernel_proof_or_countermodel.candidate.json"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_A1_THREE_FIELD_PHYSICAL_SOURCE_CERTIFICATE_READY_NOT_FILLED"
NEXT = "MTT_Selected_PSM_C1_02_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    source_fill = load(SOURCE_FILL)
    min_cert = load(MIN_CERT)
    route_a = load(ROUTE_A_FILL)
    route_b = load(ROUTE_B_RUN)
    decision = load(DECISION)
    ownership = load(PSM_OWNERSHIP)

    three_field = {
        "schema": "MTTPSMC102SI1uA1ThreeFieldPhysicalSourceCertificate.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-A1",
        "status": "THREE_FIELD_PHYSICAL_SOURCE_CERTIFICATE_IDENTIFIED_NOT_FILLED",
        "source": rel(MIN_CERT),
        "fields": min_cert["minimal_route_A_certificate_fields"],
        "same_source_emission_subfields": min_cert["same_source_emission_subfields"],
        "already_closed_or_retired": min_cert["already_closed_or_retired"],
        "why_three_fields_suffice": min_cert["why_three_fields_suffice"],
        "filled_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_a_template = {
        "schema": "MTTPSMC102RouteAPhysicalSourceTheoremTemplateImport.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-A1",
        "status": "ROUTE_A_TEMPLATE_IMPORTED_NOT_FILLED",
        "source": rel(ROUTE_A_FILL),
        "required_statement": route_a["required_statement"],
        "must_attach_sources": route_a["must_attach_sources"],
        "must_prove_equalities": route_a["must_prove_equalities"],
        "if_filled_promotes": route_a["if_filled_promotes"],
        "validator_target": route_a["validator_target"],
        "filled_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b_spec = {
        "schema": "MTTPSMC102RouteBHonestFiniteC1ExecutionSpecImport.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B2",
        "status": "ROUTE_B_INDEPENDENT_RUN_SPEC_IMPORTED_NOT_EXECUTED",
        "source": rel(ROUTE_B_RUN),
        "required_inputs": route_b["required_inputs"],
        "required_outputs": route_b["required_outputs"],
        "current_support": route_b["current_support"],
        "executed_now": route_b["executed_now"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1uA1CertificateReady.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_PhysicalPhiFinC1ActionRestriction_or_HonestFiniteC1Execution_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a",
            "task": "Fill the physical action restriction source: selected Phi_fin^C1 restricts to selected finite Weyl quotient.",
        },
        "then": [
            "SI-1u-A1b: prove no extra physical boundary/source term",
            "SI-1u-A1c: emit same-source R_Z/R_X/b_selected",
        ],
        "replacement": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
            "task": "Execute the independent finite-C1/Galerkin provenance run if Route A certificate cannot be filled.",
        },
        "status": "NEXT_WORKORDER_FILL_PHYSICAL_SOURCE_CERTIFICATE_OR_ROUTEB_RUN",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102PhysicalPhiFinC1ActionRestrictionOrHonestFiniteC1Execution",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1u-A1", "SOURCE-IDENTITY/SI-1u-B2"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "inputs": {
            "source_fill_reduction": rel(SOURCE_FILL),
            "psm_ownership_countermodel": rel(PSM_OWNERSHIP),
        },
        "output_packets": {
            "three_field_physical_source_certificate": rel(THREE_FIELD),
            "route_a_physical_source_theorem_template_import": rel(ROUTE_A_TEMPLATE),
            "route_b_honest_finite_c1_execution_spec_import": rel(ROUTE_B_SPEC),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "PSMC102SI1uA1ThreeFieldPhysicalSourceCertificateReductionTheorem",
            "proved": True,
            "statement": (
                "Given the derived finite trace/Frobenius measure, algebraic finite boundary cancellation, "
                "formal 110-row replay, and support-only countermodel, the remaining Route-A unpatched proof is "
                "exactly a three-field same-branch certificate: physical action restriction to the selected finite "
                "Weyl quotient, no extra physical boundary/source term, and same-source R_Z/R_X/b_selected emission. "
                "Route B remains the honest independent finite-C1 execution replacement."
            ),
        },
        "what_closes_now": {
            "SI1u_A1_three_field_certificate_reduction": True,
            "route_A_fill_template_imported": True,
            "route_B_independent_run_spec_imported": True,
            "support_only_countermodel_respected": True,
            "non_blockers_separated": source_fill["what_closes_now"]["non_blockers_separated_from_live_source_clauses"],
        },
        "what_remains_open": {
            "SI1u_A1a_physical_action_restricts_to_selected_finite_Weyl_quotient": True,
            "SI1u_A1b_no_extra_physical_boundary_or_source_term": True,
            "SI1u_A1c_same_source_R_Z_R_X_b_selected_emission": True,
            "route_B_independent_Galerkin_or_row_run": True,
            "unpatched_A_selected_b_selected_deltaTheta_C1": True,
            "true_equivalence_closure": True,
        },
        "closure_decision": {
            "route_A_minimal_certificate_built": decision["route_A_minimal_certificate_built"],
            "route_A_minimal_certificate_filled": decision["route_A_minimal_certificate_filled"],
            "route_B_run_executed": decision["route_B_run_executed"],
            "unpatched_A_selected_promoted": decision["unpatched_A_selected_promoted"],
            "unpatched_b_selected_promoted": decision["unpatched_b_selected_promoted"],
            "unpatched_deltaTheta_C1_promoted": decision["unpatched_deltaTheta_C1_promoted"],
            "global_closure_claimed": False,
        },
        "superset_strategy": {
            "classification": "SUPERSET_ROUTE_CERTIFICATE_REDUCTION",
            "route_A": "physical Phi_fin^C1 source certificate",
            "route_B": "honest independent finite-C1/Galerkin provenance run",
            "support_countermodel": "prevents using closed formal support as proof of physical ownership",
            "knob_policy": "No observed constants, target fitting, or adjustable coefficients are used.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_PhysicalPhiFinC1ActionRestriction_or_HonestFiniteC1Execution_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "three_field_certificate_ready": True,
        "route_A_minimal_certificate_filled": False,
        "route_B_run_executed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 PhysicalPhiFinC1ActionRestriction or HonestFiniteC1Execution v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1`

Replacement label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Result

The physical action frontier is reduced to exactly three same-branch fields:

- `SI-1u-A1a`: physical `Phi_fin^C1` action restricts to the selected finite Weyl quotient.
- `SI-1u-A1b`: no extra physical boundary/source term survives.
- `SI-1u-A1c`: same-source `R_Z/R_X/b_selected` emission.

This uses the support-only countermodel as a guardrail: closed formal support and
the validated local-principle packet are not themselves a physical ownership
proof.

## Superset Use

This is a certificate reduction, not knobs.  Route A is the physical
`Phi_fin^C1` source certificate; Route B is honest independent finite-C1
execution. Both are constrained to the same target, but neither uses observed
constants or target fitting.

## Next

`SI-1u-A1a`: fill the physical action restriction source.

Next artifact: `{NEXT}`
"""

    for path, obj in [
        (THREE_FIELD, three_field),
        (ROUTE_A_TEMPLATE, route_a_template),
        (ROUTE_B_SPEC, route_b_spec),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
