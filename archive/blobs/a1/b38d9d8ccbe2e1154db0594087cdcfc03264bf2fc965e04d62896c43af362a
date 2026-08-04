"""Build CONST-EW-02 B28 patched C1 bridge and minimal source-certificate frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b28_patched_c1_and_minimal_source_certificate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PATCHED = BASE / "patched_sm_parity_c1_import.packet.json"
MINIMAL = BASE / "minimal_source_certificate_import.packet.json"
GAUGE = BASE / "gaugekinetic_edge_status.packet.json"
BOUNDARY = BASE / "weak_mixing_b28_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B28_PatchedC1AndMinimalSourceCertificate_v1.md"

STATUS = "MTT_CONST_EW_02_B28_PATCHED_C1_IMPORTED_MINIMAL_SOURCE_CERT_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b27_path = DATA / "const_ew_02_weak_mixing_b27_c1_execution_stack_import.candidate.json"
    b27_boundary_path = DATA / "const_ew_02_weak_mixing_b27_c1_execution_stack_import" / "weak_mixing_b27_boundary.packet.json"

    sm_patched_path = SM / "candidate_data" / "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution.candidate.json"
    sm_patched_cert_path = SM / "certificates" / "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution_certificate.json"
    sm_patched_import_path = SM / "candidate_data" / "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution" / "patched_smparity_dynamic_c1_import.packet.json"
    sm_unpatched_gate_path = SM / "candidate_data" / "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution" / "unpatched_noknob_remaining_gate.packet.json"
    sm_minimal_path = SM / "candidate_data" / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun.candidate.json"
    sm_minimal_cert_path = SM / "certificates" / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun_certificate.json"
    sm_minimal_cert_packet_path = SM / "candidate_data" / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun" / "minimal_physical_source_certificate.packet.json"
    sm_routeb_spec_path = SM / "candidate_data" / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun" / "route_b_independent_galerkin_provenance_run_spec.packet.json"

    qa_heterotic_threshold_path = QA / "candidate_data" / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json"
    qa_heterotic_threshold_cert_path = QA / "certificates" / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload_certificate.json"
    qa_oriented_source_path = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.candidate.json"
    qa_oriented_source_cert_path = QA / "certificates" / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt_certificate.json"

    b27 = load(b27_path)
    b27_boundary = load(b27_boundary_path)
    sm_patched = load(sm_patched_path)
    sm_patched_cert = load(sm_patched_cert_path)
    sm_patched_import = load(sm_patched_import_path) if sm_patched_import_path.exists() else {}
    sm_unpatched_gate = load(sm_unpatched_gate_path) if sm_unpatched_gate_path.exists() else {}
    sm_minimal = load(sm_minimal_path)
    sm_minimal_cert = load(sm_minimal_cert_path)
    sm_minimal_cert_packet = load(sm_minimal_cert_packet_path)
    sm_routeb_spec = load(sm_routeb_spec_path)
    qa_threshold = load(qa_heterotic_threshold_path)
    qa_threshold_cert = load(qa_heterotic_threshold_cert_path)
    qa_oriented = load(qa_oriented_source_path)
    qa_oriented_cert = load(qa_oriented_source_cert_path)

    patched_packet = {
        "schema": "MTTConstEW02B28PatchedSMParityC1Import.v1",
        "status": "PATCHED_SM_PARITY_C1_IMPORTED_UNPATCHED_NOKNOB_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B28-PATCHED-C1-PARITY-LANE",
        "inputs": {
            "B27_candidate": rel(b27_path),
            "sm_patched_candidate": rel(sm_patched_path),
            "sm_patched_certificate": rel(sm_patched_cert_path),
            "sm_patched_import_packet": rel(sm_patched_import_path),
            "sm_unpatched_remaining_gate": rel(sm_unpatched_gate_path),
        },
        "patched_result": {
            "SM_parity_closed": sm_patched["SM_parity_closed"],
            "SM_parity_dynamic_C1_closed_under_local_principle": sm_patched["SM_parity_dynamic_C1_closed_under_local_principle"],
            "patched_SM_parity_dynamic_C1_source_and_value_interface_closed": sm_patched_cert["patched_SM_parity_dynamic_C1_source_and_value_interface_closed"],
            "patched_route_B_source_validator_ok": sm_patched_cert["patched_route_B_source_validator_ok"],
        },
        "unpatched_result": {
            "unpatched_no_knob_dynamic_C1_closed": sm_patched_cert["unpatched_no_knob_dynamic_C1_closed"],
            "no_knob_closed": sm_patched["no_knob_closed"],
            "true_SM_equivalence_closed": sm_patched["true_SM_equivalence_closed"],
            "remaining_gate": sm_patched["what_remains_open"],
        },
        "imported_support_packet": sm_patched_import,
        "unpatched_remaining_gate_packet": sm_unpatched_gate,
        "local_interpretation": "This may be used as SM-parity/replay support only. It is not a no-knob source derivation of the physical weak angle.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    minimal_packet = {
        "schema": "MTTConstEW02B28MinimalSourceCertificateImport.v1",
        "status": "MINIMAL_SOURCE_CERTIFICATE_IMPORTED_UNFILLED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B28-SAMEBRANCH-PHIFIN-C1-SOURCE-EMISSION",
        "inputs": {
            "sm_minimal_candidate": rel(sm_minimal_path),
            "sm_minimal_certificate": rel(sm_minimal_cert_path),
            "sm_minimal_source_certificate_packet": rel(sm_minimal_cert_packet_path),
            "sm_routeb_independent_run_spec": rel(sm_routeb_spec_path),
        },
        "minimal_route_A_certificate": sm_minimal_cert_packet,
        "route_B_independent_run_spec": sm_routeb_spec,
        "three_field_certificate": {
            "physical_action_restricts_to_selected_finite_Weyl_quotient": sm_minimal["what_remains_open"]["physical_action_restricts_to_selected_finite_Weyl_quotient"],
            "no_extra_physical_boundary_or_source_term": sm_minimal["what_remains_open"]["no_extra_physical_boundary_or_source_term"],
            "same_source_R_Z_R_X_b_selected_emission": sm_minimal["what_remains_open"]["same_source_R_Z_R_X_b_selected_emission"],
        },
        "decision": {
            "route_A_minimal_certificate_built": sm_minimal["promotion_decision"]["route_A_minimal_certificate_built"],
            "route_A_minimal_certificate_filled": sm_minimal_cert["route_A_minimal_certificate_filled"],
            "route_B_run_spec_built": sm_minimal["promotion_decision"]["route_B_run_spec_built"],
            "route_B_run_executed": sm_minimal_cert["route_B_run_executed"],
            "no_knob_closed": sm_minimal["promotion_decision"]["no_knob_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    gauge_packet = {
        "schema": "MTTConstEW02B28GaugeKineticEdgeStatus.v1",
        "status": "GAUGEKINETIC_EDGE_REMAINS_STRUCTURAL_PHYSICAL_ANCHOR_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B28-GAUGEKINETIC-ACTION-ANCHOR",
        "inputs": {
            "qa_heterotic_threshold_candidate": rel(qa_heterotic_threshold_path),
            "qa_heterotic_threshold_certificate": rel(qa_heterotic_threshold_cert_path),
            "qa_oriented_phifin_sourceownership_candidate": rel(qa_oriented_source_path),
            "qa_oriented_phifin_sourceownership_certificate": rel(qa_oriented_source_cert_path),
        },
        "heterotic_threshold_status": {
            "status": qa_threshold["status"],
            "theorem": qa_threshold["theorem"],
            "closure_claimed": qa_threshold["closure_claimed"],
            "target_fitting_used": qa_threshold["target_fitting_used"],
        },
        "oriented_phifin_sourceownership_status": {
            "status": qa_oriented["status"],
            "same_branch_source_certificate_closed": qa_oriented_cert["same_branch_source_certificate_closed"],
            "oriented_BN_carrier_emission_closed": qa_oriented_cert["oriented_BN_carrier_emission_closed"],
            "EndE_or_rhoE_to_oriented_BN_functor_closed": qa_oriented_cert["EndE_or_rhoE_to_oriented_BN_functor_closed"],
            "oriented_logdet_promoted": qa_oriented_cert["oriented_logdet_promoted"],
        },
        "local_decision": {
            "K_phys_or_f_ab_closed": False,
            "mu_match_closed": False,
            "RG_threshold_scheme_closed": False,
            "physical_electroweak_threshold_promoted": False,
            "useful_support": "heterotic f=S / threshold-operator route remains structural; oriented Phi_fin source ownership is partially filled only at branch-certificate level.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B28Boundary.v1",
        "status": "PATCHED_PARITY_C1_CLOSED_UNPATCHED_WEAKANGLE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B28-BOUNDARY",
        "preserved_from_B27": {
            "primitive_C1_algebraic_values_filled": b27["primitive_C1_algebraic_values_filled"],
            "total_C1_algebraic_values_filled": b27["total_C1_algebraic_values_filled"],
            "last_source_theorem_contract_built": b27["last_source_theorem_contract_built"],
        },
        "advanced_now": {
            "patched_SM_parity_dynamic_C1_source_value_interface_closed": sm_patched_cert["patched_SM_parity_dynamic_C1_source_and_value_interface_closed"],
            "minimal_three_field_source_certificate_identified": sm_minimal_cert["minimal_route_A_source_certificate_identified"],
            "route_B_independent_run_spec_built": sm_minimal["promotion_decision"]["route_B_run_spec_built"],
            "same_branch_heterotic_branch_certificate_partial_support": qa_oriented_cert["same_branch_source_certificate_closed"],
        },
        "still_open": {
            "unpatched_no_knob_dynamic_C1": True,
            "physical_action_restricts_to_selected_finite_Weyl_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "same_source_R_Z_R_X_b_selected_emission": True,
            "route_B_independent_Galerkin_or_row_run": True,
            "K_phys_or_f_ab": True,
            "mu_match": True,
            "RG_threshold_scheme": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "allowed_claim": "patched SM-parity C1 source/value interface is closed as a support/replay lane, and the unpatched source certificate is reduced to three fields",
        "forbidden_claim": "strict no-knob physical weak-angle closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B28NextWork.v1",
        "status": "NEXT_WORKORDER_FILL_THREE_FIELD_SOURCE_CERT_OR_RUN_ROUTEB",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B29-FILL-SOURCE-CERTIFICATE-OR-ROUTEB-RUN",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B29-THREE-FIELD-PHYSICAL-SOURCE-CERTIFICATE-FILL",
            "task": "Fill the three Route-A fields: action restriction to selected finite Weyl quotient, no extra physical boundary/source term, and same-source R_Z/R_X/b_selected emission.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B29-INDEPENDENT-GALERKIN-ROW-PROVENANCE-RUN",
            "task": "Execute Route B independent Galerkin/row provenance run for the same packet without residual-projector inheritance.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB28PatchedC1AndMinimalSourceCertificate",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B28-SAMEBRANCH-PHIFIN-C1-SOURCE-OR-GAUGEKINETIC-ACTION",
        "output_packets": {
            "patched_sm_parity_c1_import": rel(PATCHED),
            "minimal_source_certificate_import": rel(MINIMAL),
            "gaugekinetic_edge_status": rel(GAUGE),
            "weak_mixing_b28_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B28PatchedC1AndMinimalSourceCertificateTheorem",
            "proved": True,
            "statement": (
                "The patched SM-parity dynamic C1 source/value interface is imported as closed under the local source-identity principle, while the unpatched/no-knob branch remains open. "
                "The unpatched Route-A source promotion is reduced to a three-field physical source certificate, or Route-B can close by an independent Galerkin/row-provenance run. "
                "The gauge-kinetic edge remains structural with K_phys, mu_match, and RG/threshold scheme open."
            ),
        },
        "patched_SM_parity_dynamic_C1_closed": sm_patched_cert["patched_SM_parity_dynamic_C1_source_and_value_interface_closed"],
        "unpatched_no_knob_dynamic_C1_closed": sm_patched_cert["unpatched_no_knob_dynamic_C1_closed"],
        "minimal_route_A_source_certificate_identified": sm_minimal_cert["minimal_route_A_source_certificate_identified"],
        "route_A_minimal_certificate_filled": sm_minimal_cert["route_A_minimal_certificate_filled"],
        "route_B_run_executed": sm_minimal_cert["route_B_run_executed"],
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B28_PatchedC1AndMinimalSourceCertificate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "patched_SM_parity_dynamic_C1_closed": sm_patched_cert["patched_SM_parity_dynamic_C1_source_and_value_interface_closed"],
        "patched_route_B_source_validator_ok": sm_patched_cert["patched_route_B_source_validator_ok"],
        "unpatched_no_knob_dynamic_C1_closed": sm_patched_cert["unpatched_no_knob_dynamic_C1_closed"],
        "minimal_route_A_source_certificate_identified": sm_minimal_cert["minimal_route_A_source_certificate_identified"],
        "route_A_minimal_certificate_filled": sm_minimal_cert["route_A_minimal_certificate_filled"],
        "route_B_run_executed": sm_minimal_cert["route_B_run_executed"],
        "K_phys_or_f_ab_closed": False,
        "mu_match_closed": False,
        "RG_threshold_scheme_closed": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B28 Patched C1 And Minimal Source Certificate v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B28-SAMEBRANCH-PHIFIN-C1-SOURCE-OR-GAUGEKINETIC-ACTION`

## Advanced

```text
patched SM-parity dynamic C1 closed = {sm_patched_cert["patched_SM_parity_dynamic_C1_source_and_value_interface_closed"]}
unpatched no-knob dynamic C1 closed = {sm_patched_cert["unpatched_no_knob_dynamic_C1_closed"]}
minimal Route-A certificate built   = {sm_minimal_cert["minimal_route_A_source_certificate_identified"]}
minimal Route-A certificate filled  = {sm_minimal_cert["route_A_minimal_certificate_filled"]}
Route-B independent run executed    = {sm_minimal_cert["route_B_run_executed"]}
```

## Three Remaining Route-A Fields

```text
physical action restricts to selected finite Weyl quotient
no extra physical boundary/source term
same-source R_Z/R_X/b_selected emission
```

Route B remains the independent Galerkin/row-provenance run for the same packet.

## Gauge Edge

The heterotic/gauge-kinetic edge remains structural support only: `K_phys/f_ab`,
`mu_match`, and the RG/threshold scheme are still open.

## Next

`CONST-EW-02 / WEAK-MIXING / B29-FILL-SOURCE-CERTIFICATE-OR-ROUTEB-RUN`
"""

    for path, payload in [
        (PATCHED, patched_packet),
        (MINIMAL, minimal_packet),
        (GAUGE, gauge_packet),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
