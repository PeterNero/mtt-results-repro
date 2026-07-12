"""Build PSM-C1-01 source-rule emission test with PSM-C1-04 sidecar."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_01_sourceruleemission_or_psm_c1_04_bselectedsidecar"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
UNPATCHED = PACKET_DIR / "route_a_unpatched_source_rule_validator.packet.json"
PATCHED_PAYLOAD = PACKET_DIR / "route_a_patched_axiom_validator_payload.packet.json"
PATCHED_RESULT = PACKET_DIR / "route_a_patched_axiom_validator_result.packet.json"
B_SIDECAR = PACKET_DIR / "psm_c1_04_bselected_sidecar.packet.json"
LABEL_STATUS = PACKET_DIR / "label_status_after_source_rule_sidecar.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_01_SourceRuleEmission_or_PSM_C1_04_bSelectedSidecar_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"
STATUS = "MTT_SELECTED_PSM_C1_01_SOURCERULEEMISSION_OR_PSM_C1_04_BSELECTEDSIDECAR_BUILT_PATCHED_PASS_UNPATCHED_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_01_UnpatchedSourceLemma_or_ROUTE_B_RowKernelExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": [line for line in proc.stderr.splitlines() if line],
        "passes": proc.returncode == 0,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    route_test = load(DATA / "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest.candidate.json")
    next_work = load(DATA / "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest" / "next_labeled_workorder.packet.json")
    current_fail = load(DATA / "selected_sourcetheorem_push_attempt_or_minimalnewlemma" / "current_validator_result.packet.json")
    current_attempt = load(DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem" / "current_two_exit_source_attempt.packet.json")
    axiom = load(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "accepted_local_source_axiom.packet.json")
    patched = load(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "patched_dynamic_c1_closure_theorem.packet.json")
    unpatched_exit = load(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "unpatched_exit_status.packet.json")
    same_source_status = load(DATA / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement" / "same_source_physical_emission_status.packet.json")
    route_b_status = load(DATA / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement" / "unpatched_galerkin_replacement_status.packet.json")
    minimal_lemma = load(DATA / "selected_sourcetheorem_push_attempt_or_minimalnewlemma" / "minimal_selected_finitec1_source_promotion_lemma.packet.json")

    unpatched_validator = {
        "schema": "MTTRouteAUnpatchedSourceRuleValidator.v1",
        "status": "UNPATCHED_ROUTE_A_STRICT_VALIDATOR_STILL_FAILS",
        "active_labels": ["PSM-C1-01", "PSM-C1-04"],
        "current_attempt_payload": rel(
            DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem" / "current_two_exit_source_attempt.packet.json"
        ),
        "validator_result": current_fail,
        "strict_missing_route_A": current_attempt["route_A_physical_action_restriction"]["still_required"],
        "strict_missing_route_B": {
            "selected_basis_feeds_all_72_row_functionals": True,
            "pre_residual_phase_shift_variation_operators": True,
            "independent_hessian_counterterm_source_rows": True,
            "sector_rows_assembled_from_source_rows": True,
            "no_residual_projector_replay_or_locked_target_as_source": True,
        },
        "unpatched_PSM_C1_01_closed": False,
        "unpatched_PSM_C1_04_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    patched_payload = {
        "schema": "MTTPatchedRouteAPhiFinC1SourceRuleValidatorPayload.v1",
        "status": "PATCHED_ROUTE_A_PAYLOAD_FROM_EXPLICIT_LOCAL_AXIOM",
        "closure_claimed": False,
        "scientific_status": "axiom-conditional validator pass, not unpatched derivation",
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "route_A_physical_action_restriction": {
            "same_branch": True,
            "physical_action_restricts_to_finite_weyl_quotient": True,
            "zero_extra_boundary_or_source_term": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "attached_source_evidence": [
                {
                    "source": rel(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "accepted_local_source_axiom.packet.json"),
                    "closes": "explicit local axiom states the physical action restriction and residual-projector application",
                },
                {
                    "source": rel(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "patched_dynamic_c1_closure_theorem.packet.json"),
                    "closes": "axiom-conditional replay promotes R_Z, R_X, A_selected, b_selected, deltaTheta_C1, and sector response matrices",
                },
                {
                    "source": rel(CORPUS / "MTT_DifferentiatedPhiFinC1ResidualProjectorAxiom_LocalCorpusPatch_v1.md"),
                    "closes": "local proof-corpus patch records the accepted premise and guardrails",
                },
                {
                    "source": rel(DATA / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement" / "same_source_physical_emission_status.packet.json"),
                    "closes": "identifies exactly the same physical R_Z/R_X/b_selected emissions needed by the unpatched branch",
                },
                {
                    "source": rel(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "unpatched_exit_status.packet.json"),
                    "closes": "keeps unpatched derivation and honest Galerkin exits open while the patched validator passes",
                },
            ],
        },
        "route_B_independent_rowkernel_source": {
            "same_branch": True,
            "selected_basis_feeds_all_72_row_functionals": False,
            "pre_residual_phase_shift_variation_operators": False,
            "independent_hessian_counterterm_source_rows": False,
            "sector_rows_assembled_from_source_rows": False,
            "no_residual_projector_replay_or_locked_target_as_source": False,
            "attached_source_evidence": [],
        },
    }
    PATCHED_PAYLOAD.write_text(json.dumps(patched_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    patched_result = run_validator(PATCHED_PAYLOAD)
    patched_result["observed_data_used_as_selector"] = False
    patched_result["target_fitting_used"] = False

    b_sidecar = {
        "schema": "MTTPSMC104BSelectedSidecar.v1",
        "status": "B_SELECTED_SIDECAR_SPLIT_PATCHED_PASS_UNPATCHED_OPEN",
        "label": "PSM-C1-04",
        "patched_status": {
            "local_axiom_accepted": axiom["status"] == "LOCAL_SOURCE_AXIOM_ACCEPTED_IN_THIS_PROOF_SPINE",
            "patched_b_selected_emitted": patched["promoted_objects"]["b_selected"],
            "patched_A_transpose_b": patched["exact_values"]["A_transpose_b"],
            "patched_deltaTheta_C1": patched["exact_values"]["deltaTheta_C1"],
            "patched_dynamic_C1_packet_closed": patched["status"] == "PATCHED_DYNAMIC_C1_PACKET_CLOSED_BY_ACCEPTED_SOURCE_AXIOM",
        },
        "unpatched_status": {
            "source_rule_derived_unpatched": unpatched_exit["source_rule_derived_unpatched"],
            "same_source_b_selected_emission": same_source_status["b_selected_replay"]["same_source_emitted"],
            "honest_galerkin_table_exported": unpatched_exit["honest_galerkin_table_exported"],
            "route_B_can_replace_now": route_b_status["current_route_state"]["can_replace_source_map_now"],
        },
        "interpretation": (
            "PSM-C1-04 is closed only inside the explicit local axiom/patched proof spine. "
            "For unpatched post-SM-parity work it remains open and must be derived from the same physical branch "
            "or replaced by independent selected Galerkin rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    label_status = {
        "schema": "MTTLabelStatusAfterPSMC101SourceRuleEmission.v1",
        "status": "PATCHED_PSM_C1_01_C1_04_AVAILABLE_UNPATCHED_LABELS_OPEN",
        "labels": [
            {
                "id": "PSM-C1-01",
                "patched_status": "PATCHED_CLOSED_BY_EXPLICIT_LOCAL_AXIOM",
                "unpatched_status": "OPEN_NEEDS_SELECTED_PHYSICAL_ACTION_RESTRICTION",
                "next_required_unpatched_field": "physical_action_restricts_to_finite_weyl_quotient",
            },
            {
                "id": "PSM-C1-04",
                "patched_status": "PATCHED_CLOSED_BY_EXPLICIT_LOCAL_AXIOM",
                "unpatched_status": "OPEN_NEEDS_SAME_SOURCE_B_SELECTED_EMISSION",
                "next_required_unpatched_field": "same_source_b_selected_emission",
            },
            {
                "id": "PSM-C1-03",
                "patched_status": "PATCHED_CLOSED_BY_EXPLICIT_LOCAL_AXIOM",
                "unpatched_status": "OPEN_DEPENDS_ON_PSM-C1-01_AND_PSM-C1-04",
                "next_required_unpatched_field": "A_selected_from_same_source_or_independent_rows",
            },
            {
                "id": "PSM-C1-05",
                "patched_status": "PATCHED_DELTA_THETA_1_1_AVAILABLE",
                "unpatched_status": "OPEN_CONDITIONAL_VALUE_NOT_SELECTED",
                "next_required_unpatched_field": "selected_A_selected_and_b_selected",
            },
            {
                "id": "PSM-C1-06",
                "patched_status": "PATCHED_SECTOR_RESPONSE_MATRICES_PROMOTED",
                "unpatched_status": "OPEN_NEEDS_SELECTED_SECTOR_ROWS_OR_GALERKIN_EXPORT",
                "next_required_unpatched_field": "sector_rows_assembled_from_source_rows",
            },
        ],
        "closed_labels_preserved": ["DONE-PARITY-00", "DONE-SOURCE-00", "DONE-DYN-SUPPORT-00"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC101Sidecar.v1",
        "status": "NEXT_WORK_UNPATCHED_SOURCE_LEMMA_OR_ROUTE_B_ROWKERNEL_EXECUTION",
        "next_required_artifact": NEXT_ARTIFACT,
        "primary_unpatched_label": "PSM-C1-01",
        "sidecar_unpatched_label": "PSM-C1-04",
        "route_A_minimal_lemma": {
            "name": "SelectedPhysicalPhiFinC1ActionRestrictionLemma",
            "required_fields": [
                "physical_action_restricts_to_finite_weyl_quotient",
                "zero_extra_boundary_or_source_term",
                "phase_R_Z_source_selection",
                "shift_R_X_source_selection",
                "same_source_b_selected_emission",
            ],
        },
        "route_B_minimal_lemma": minimal_lemma,
        "work_items": [
            {
                "id": "A2a",
                "labels": ["PSM-C1-01", "PSM-C1-04"],
                "route": "ROUTE-A",
                "task": "Derive the five Route-A strict validator fields from unpatched MTT/Theta/Strominger physical action.",
                "success_condition": "Unpatched validator payload passes with five same-branch evidence entries.",
            },
            {
                "id": "B2a",
                "labels": ["PSM-C1-02", "PSM-C1-03", "PSM-C1-04", "PSM-C1-06"],
                "route": "ROUTE-B",
                "task": "Execute independent row-kernel/Galerkin source rows satisfying the five Route-B strict validator fields.",
                "success_condition": "Route B validator passes without residual-projector replay or locked target values as source.",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    UNPATCHED.write_text(json.dumps(unpatched_validator, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    PATCHED_RESULT.write_text(json.dumps(patched_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    B_SIDECAR.write_text(json.dumps(b_sidecar, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    LABEL_STATUS.write_text(json.dumps(label_status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(next_work, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    theorem_proved = (
        route_test["closure_decision"]["PSM-C1-01_closed"] is False
        and patched_result["passes"]
        and not b_sidecar["unpatched_status"]["source_rule_derived_unpatched"]
        and not b_sidecar["unpatched_status"]["same_source_b_selected_emission"]
        and not b_sidecar["unpatched_status"]["route_B_can_replace_now"]
    )

    candidate = {
        "candidate": "MTTSelectedPSMC101SourceRuleEmissionOrPSMC104BSelectedSidecar",
        "status": STATUS,
        "inputs": {
            "previous_route_test": rel(DATA / "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest.candidate.json"),
            "current_two_exit_attempt": rel(
                DATA / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem" / "current_two_exit_source_attempt.packet.json"
            ),
            "local_axiom": rel(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "accepted_local_source_axiom.packet.json"),
            "patched_closure": rel(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "patched_dynamic_c1_closure_theorem.packet.json"),
            "unpatched_exit": rel(DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit" / "unpatched_exit_status.packet.json"),
        },
        "output_packets": {
            "route_a_unpatched_source_rule_validator": rel(UNPATCHED),
            "route_a_patched_axiom_validator_payload": rel(PATCHED_PAYLOAD),
            "route_a_patched_axiom_validator_result": rel(PATCHED_RESULT),
            "psm_c1_04_bselected_sidecar": rel(B_SIDECAR),
            "label_status_after_source_rule_sidecar": rel(LABEL_STATUS),
            "next_labeled_workorder": rel(NEXT),
        },
        "theorem": {
            "name": "PSMC101PSMC104PatchedVsUnpatchedSeparationTheorem",
            "proved": theorem_proved,
            "statement": (
                "The explicit local DifferentiatedPhiFinC1ResidualProjectorAxiom supplies a Route-A validator "
                "pass and emits PSM-C1-01/PSM-C1-04 only inside the patched proof spine. The unpatched branch "
                "still fails the strict Route-A/Route-B validator: it lacks physical action restriction, zero "
                "extra boundary/source, phase/shift source selection, same-source b_selected, and independent "
                "Route-B row-kernel source fields."
            ),
        },
        "what_closes_now": {
            "patched_Route_A_validator_payload_passes": patched_result["passes"],
            "PSM_C1_01_patched_closure_available": True,
            "PSM_C1_04_patched_sidecar_available": True,
            "unpatched_strict_validator_gap_preserved": True,
        },
        "what_remains_open": {
            "PSM-C1-01_unpatched": True,
            "PSM-C1-04_unpatched": True,
            "PSM-C1-03_unpatched": True,
            "PSM-C1-05_unpatched": True,
            "PSM-C1-06_unpatched": True,
            "ROUTE-B_independent_rows": True,
            "PSM-DYN-01": True,
            "PSM-S2-01": True,
            "PSM-QFT-01": True,
            "PSM-NK-01": True,
        },
        "closure_decision": {
            "patched_dynamic_C1_packet_closed": True,
            "unpatched_dynamic_C1_packet_closed": False,
            "PSM-C1-01_closed_unpatched": False,
            "PSM-C1-04_closed_unpatched": False,
            "ROUTE_B_ready_now": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_01_SourceRuleEmission_or_PSM_C1_04_bSelectedSidecar_v1",
        "candidate_path": rel(OUTPUT),
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "patched_Route_A_validator_passes": patched_result["passes"],
        "unpatched_dynamic_C1_packet_closed": False,
        "patched_dynamic_C1_packet_closed": True,
        "PSM_C1_01_closed_unpatched": False,
        "PSM_C1_04_closed_unpatched": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "note_path": rel(NOTE),
    }

    note = f"""# MTT Selected PSM C1 01 SourceRuleEmission or PSM C1 04 bSelectedSidecar v1

Active labels: `PSM-C1-01` and `PSM-C1-04`.

This artifact separates the patched and unpatched statuses.

Patched lane:

- the explicit local `DifferentiatedPhiFinC1ResidualProjectorAxiom` supplies the
  physical application rule
- `R_Z`, `R_X`, `b_selected`, `A_selected`, `deltaTheta_C1=[1,1]`, and sector
  response matrices are available inside the patched proof spine
- the Route-A strict validator passes for the patched payload

Unpatched lane:

- `PSM-C1-01` remains open
- `PSM-C1-04` remains open
- Route A still needs the five strict fields:
  physical action restriction, zero extra boundary/source, phase `R_Z`, shift
  `R_X`, and same-source `b_selected`
- Route B still needs independent row-kernel/Galerkin source execution

So this is progress, but not an unpatched true-equivalence closure.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
