"""Build selected source-row construction from corpus support or Route B provenance fill."""

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

SLUG = "selected_sourcerowconstructionfromcorpus_or_routebprovenancefill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EVIDENCE_INDEX = PACKET_DIR / "corpus_source_evidence_index.packet.json"
SOURCE_ROW = PACKET_DIR / "candidate_phifin_action_restriction_source_row.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "conditional_route_a_source_certificate.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "conditional_route_a_validator_result.packet.json"
ROUTE_B_STATUS = PACKET_DIR / "route_b_provenance_fill_status.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_source_row_construction.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SourceRowConstructionFromCorpus_or_RouteBProvenanceFill_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

PREVIOUS = DATA / "selected_physicalactionrestrictionsourceactualfill_or_routebindependentrun.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_physicalactionrestrictionsourceactualfill_or_routebindependentrun"
    / "next_cutset_after_actual_fill_attempt.packet.json"
)
RESTRICTION_PROBE = (
    DATA
    / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution"
    / "physical_restriction_sublemma_probe.packet.json"
)
ROUTE_B_GAP = (
    DATA
    / "selected_physicalrestrictionsublemma_or_routebindependentrowsexecution"
    / "route_b_independent_rows_execution_gap.packet.json"
)
LOCAL_WITNESS = (
    DATA
    / "selected_lastsourcelemmaproof_or_independentc1kernelsourcerows"
    / "local_principle_physical_source_witness.packet.json"
)
FINITE_TRACE_REDUCTION = (
    DATA
    / "selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill"
    / "finite_trace_measure_reduction.packet.json"
)
PHIFIN_SCHEMA = DATA / "finite_emission_morphism_phifin.candidate.json"
ROUTEC_SOURCE = DATA / "routec_selected_source_origin_lemma.candidate.json"
PHIFIN_BN_TRACE_GAP = DATA / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"

STATUS = (
    "MTT_SELECTED_SOURCEROWCONSTRUCTIONFROMCORPUS_OR_ROUTEBPROVENANCEFILL_"
    "BUILT_CANDIDATE_SOURCE_ROW_VALIDATES_CONDITIONAL_UNPATCHED_OPEN"
)
NEXT = "MTT_Selected_FiniteEmissionMorphismPhiFinRestrictionProof_or_RouteBProvenanceExecution_v1"


SAME_BRANCH_EVIDENCE = [
    {
        "source": "candidate_data/selected_physicalactionbindingandsamesourceemission_or_independentkernelsourceexport/minimal_last_source_lemma_contract.packet.json",
        "role": "last source lemma contract",
        "supports": "same_source_b_selected_emission",
    },
    {
        "source": "candidate_data/selected_weylvariation_actionprinciple_apply_or_independentkernelexecution/accepted_local_weylvariation_actionprinciple.packet.json",
        "role": "local Weyl variation action principle",
        "supports": "physical action variation source selection",
    },
    {
        "source": "candidate_data/selected_weylvariation_actionprinciple_apply_or_independentkernelexecution/applied_principle_kernel_closure.packet.json",
        "role": "pre-residual kernel closure under the local principle",
        "supports": "finite C1 source emission after applying the principle",
    },
    {
        "source": "candidate_data/selected_actionkernelfourclauseproof_or_independentkernelvaluesrun/route_a_four_clause_partial_proof.packet.json",
        "role": "admissible differentiated variation space",
        "supports": "phase_R_Z_source_selection and shift_R_X_source_selection",
    },
    {
        "source": "candidate_data/selected_weylvariation_actionprinciple_derivation_or_explicitinsertion/explicit_weylvariation_actionprinciple_insertion_package.packet.json",
        "role": "principle text and guardrails",
        "supports": "no observed constants and no target fitting",
    },
    {
        "source": "candidate_data/selected_physicalactionbindingandsamesourceemission_or_independentkernelsourceexport.candidate.json",
        "role": "three-validator alignment",
        "supports": "same source binding and physical action emission compatibility",
    },
    {
        "source": "candidate_data/selected_physicalrestrictionsublemma_or_routebindependentrowsexecution/physical_restriction_sublemma_probe.packet.json",
        "role": "closed support for the finite quotient and trace measure",
        "supports": "finite selected C1 quotient, finite trace measure, Weyl variation algebra, and boundary support",
    },
    {
        "source": "candidate_data/selected_unpatchedweylvariationprinciplederivation_or_routebsourcerowsfill/finite_trace_measure_reduction.packet.json",
        "role": "finite trace measure reduction",
        "supports": "measure normalization no longer axiomatic; physical action restriction remains the exact frontier",
    },
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources_exist() -> None:
    required = [
        PREVIOUS,
        PREVIOUS_CUTSET,
        RESTRICTION_PROBE,
        ROUTE_B_GAP,
        LOCAL_WITNESS,
        FINITE_TRACE_REDUCTION,
        PHIFIN_SCHEMA,
        ROUTEC_SOURCE,
        PHIFIN_BN_TRACE_GAP,
        VALIDATOR,
    ]
    required.extend(ROOT / item["source"] for item in SAME_BRANCH_EVIDENCE)
    missing = [rel(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("missing source evidence: " + ", ".join(missing))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(VALIDATOR),
        "payload": rel(path),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr_lines": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)
    require_sources_exist()

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    restriction_probe = load(RESTRICTION_PROBE)
    route_b_gap = load(ROUTE_B_GAP)
    local_witness = load(LOCAL_WITNESS)
    finite_trace = load(FINITE_TRACE_REDUCTION)
    phifin_schema = load(PHIFIN_SCHEMA)
    routec_source = load(ROUTEC_SOURCE)
    phifin_bn_gap = load(PHIFIN_BN_TRACE_GAP)

    evidence_index = {
        "schema": "MTTSelectedSourceRowConstructionEvidenceIndex.v1",
        "status": "SAME_BRANCH_SUPPORT_ASSEMBLED_CONDITIONAL_PROMOTION_REQUIRED",
        "same_branch_evidence_count": len(SAME_BRANCH_EVIDENCE),
        "same_branch_evidence": SAME_BRANCH_EVIDENCE,
        "auxiliary_phi_fin_chain": [
            {
                "source": rel(PHIFIN_SCHEMA),
                "status": phifin_schema["status"],
                "role": "finite codomain and validator schema for Phi_fin",
            },
            {
                "source": rel(ROUTEC_SOURCE),
                "status": routec_source["status"],
                "role": "source-origin lemma reduced to finite emission morphism",
            },
            {
                "source": rel(PHIFIN_BN_TRACE_GAP),
                "status": phifin_bn_gap["status"],
                "role": "untransported BN equivalence rejected; gauge-transported trace still required",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_row = {
        "schema": "MTTCandidatePhiFinC1ActionRestrictionSourceRow.v1",
        "status": "CONSTRUCTED_CANDIDATE_ROW_VALIDATES_IF_ACCEPTED_AS_SAME_BRANCH_SOURCE",
        "source_row_name": "PhysicalPhiFinC1ActionRestrictionSourceRow",
        "construction_type": "corpus-supported conditional Route A source row",
        "same_branch": True,
        "restriction_map_to_selected_finite_Weyl_quotient": {
            "name": "res_C1_to_selected_finite_Weyl_quotient",
            "domain": "selected physical Phi_fin^C1 first-variation/action row",
            "codomain": "selected finite C1/Weyl quotient with finite trace/Frobenius measure",
            "formula": (
                "res_C1_to_selected_finite_Weyl_quotient(delta S_phys) = "
                "Tr_Frob(Phi_fin(delta S_phys)|Q_sel)"
            ),
            "support": {
                "finite_selected_C1_quotient": restriction_probe["closed_support"][
                    "finite_selected_C1_quotient"
                ],
                "finite_measure_normalization_trace_Frobenius": restriction_probe["closed_support"][
                    "finite_measure_normalization_trace_Frobenius"
                ],
                "selected_Weyl_variation_algebra": restriction_probe["closed_support"][
                    "selected_Weyl_variation_algebra"
                ],
                "algebraic_finite_boundary_cancellation": restriction_probe["closed_support"][
                    "algebraic_finite_boundary_cancellation"
                ],
            },
        },
        "route_A_fields_constructed": {
            "physical_action_restricts_to_selected_finite_Weyl_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
        },
        "attached_same_branch_sources": SAME_BRANCH_EVIDENCE,
        "derivation_boundary": {
            "finite_trace_measure_derived": finite_trace["measure_normalization_derived"],
            "local_principle_witness_validates": local_witness["status"]
            == "VALIDATES_IF_LOCAL_WEYLVARIATION_PRINCIPLE_IS_ACCEPTED",
            "unpatched_theorem_derived": False,
            "why_unpatched_still_open": (
                "The row validates only after accepting the constructed source row/local Weyl-variation "
                "principle. The missing unpatched step is to derive the same row from the selected "
                "Phi_fin finite emission morphism and selected Strominger/HYM minimizer, without using "
                "the row itself as a premise."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }

    conditional_payload = {
        "schema": "MTTConditionalRouteAPhysicalSourceCertificate.v1",
        "status": "VALIDATES_CONDITIONALLY_ON_CONSTRUCTED_SOURCE_ROW",
        "route_A_physical_source_certificate": {
            "same_branch": True,
            "physical_action_restricts_to_selected_finite_Weyl_quotient": True,
            "no_extra_physical_boundary_or_source_term": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "attached_same_branch_sources": SAME_BRANCH_EVIDENCE,
            "source_row": rel(SOURCE_ROW),
            "acceptance": "conditional corpus construction, not unpatched theorem",
        },
        "route_B_independent_execution": {
            "selected_basis_independent_of_residual_projector": route_b_gap[
                "selected_basis_independent_of_residual_projector"
            ],
            "quadrature_rule_independent_of_locked_target": route_b_gap[
                "quadrature_rule_independent_of_locked_target"
            ],
            "all_72_primitive_rows_executed": route_b_gap["all_72_primitive_rows_executed"],
            "formal_110_rows_executed": route_b_gap["formal_110_rows_executed"],
            "source_independent_of_residual_projector_replay": route_b_gap[
                "source_independent_of_residual_projector_replay"
            ],
            "exactness_or_error_certificates_attached": route_b_gap[
                "exactness_or_error_certificates_attached"
            ],
            "attached_independent_provenance_sources": route_b_gap[
                "attached_independent_provenance_sources"
            ],
        },
        "conditional_source_row_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }

    route_b_status = {
        "schema": "MTTRouteBProvenanceFillStatus.v1",
        "status": "ROUTE_B_PROVENANCE_STILL_OPEN_ROUTE_A_CONDITIONAL_ROW_AVAILABLE",
        "all_72_primitive_rows_executed": route_b_gap["all_72_primitive_rows_executed"],
        "formal_110_rows_executed": route_b_gap["formal_110_rows_executed"],
        "selected_basis_independent_of_residual_projector": route_b_gap[
            "selected_basis_independent_of_residual_projector"
        ],
        "quadrature_rule_independent_of_locked_target": route_b_gap[
            "quadrature_rule_independent_of_locked_target"
        ],
        "source_independent_of_residual_projector_replay": route_b_gap[
            "source_independent_of_residual_projector_replay"
        ],
        "exactness_or_error_certificates_attached": route_b_gap[
            "exactness_or_error_certificates_attached"
        ],
        "attached_independent_provenance_sources_count": len(
            route_b_gap["attached_independent_provenance_sources"]
        ),
        "ready_now": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    write_json(EVIDENCE_INDEX, evidence_index)
    write_json(SOURCE_ROW, source_row)
    write_json(CONDITIONAL_PAYLOAD, conditional_payload)
    write_json(ROUTE_B_STATUS, route_b_status)

    validator_result = run_validator(CONDITIONAL_PAYLOAD)
    write_json(VALIDATOR_RESULT, validator_result)

    next_cutset = {
        "schema": "MTTNextCutsetAfterSourceRowConstruction.v1",
        "status": "CONDITIONAL_ROUTE_A_SOURCE_ROW_VALIDATES_UNPATCHED_PROMOTION_OPEN",
        "closed_now": [
            "constructed candidate PhysicalPhiFinC1ActionRestrictionSourceRow",
            "constructed restriction map to selected finite Weyl quotient",
            "attached at least five filesystem-present same-branch evidence entries",
            "strict source-certificate validator passes when the constructed row is accepted",
        ],
        "still_open_for_unpatched_theorem": [
            "derive the constructed row from the selected Phi_fin finite emission morphism",
            "derive Phi_fin from the selected Strominger/HYM minimizer and finite trace without inserting the source row",
            "or complete Route B independent basis/quadrature/provenance and exactness certificates",
        ],
        "previous_frontier": previous_cutset["recommended_next"]["artifact"],
        "recommended_next": {
            "artifact": NEXT,
            "route_A": [
                "prove FiniteEmissionMorphismPhiFinRestrictionProof",
                "show the selected minimizer emits the same restriction map",
                "then promote conditional Route A to unpatched theorem",
            ],
            "route_B": [
                "fill independent basis and quadrature provenance",
                "attach exactness/error certificates",
                "replay strict validator through Route B",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    conditional_pass = validator_result["returncode"] == 0
    candidate = {
        "candidate": "MTTSelectedSourceRowConstructionFromCorpusOrRouteBProvenanceFill",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "previous_cutset": rel(PREVIOUS_CUTSET),
            "physical_restriction_probe": rel(RESTRICTION_PROBE),
            "local_principle_witness": rel(LOCAL_WITNESS),
            "finite_trace_measure_reduction": rel(FINITE_TRACE_REDUCTION),
            "finite_emission_morphism_schema": rel(PHIFIN_SCHEMA),
            "routec_source_origin_reduction": rel(ROUTEC_SOURCE),
            "phifin_bn_trace_gap": rel(PHIFIN_BN_TRACE_GAP),
            "route_b_gap": rel(ROUTE_B_GAP),
        },
        "output_packets": {
            "corpus_source_evidence_index": rel(EVIDENCE_INDEX),
            "candidate_phifin_action_restriction_source_row": rel(SOURCE_ROW),
            "conditional_route_a_source_certificate": rel(CONDITIONAL_PAYLOAD),
            "conditional_route_a_validator_result": rel(VALIDATOR_RESULT),
            "route_b_provenance_fill_status": rel(ROUTE_B_STATUS),
            "next_cutset_after_source_row_construction": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "candidate_same_branch_physical_action_restriction_row_constructed": True,
            "restriction_map_to_selected_finite_Weyl_quotient_constructed": True,
            "same_branch_source_evidence_attached": len(SAME_BRANCH_EVIDENCE) >= 5,
            "conditional_route_A_validator_passes": conditional_pass,
            "route_B_provenance_status_recorded": True,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "promote_candidate_row_to_unpatched_theorem": True,
            "derive_selected_phi_fin_restriction_from_strominger_hym_minimizer": True,
            "construct_gauge_transported_phi_fin_trace": True,
            "route_B_independent_basis_quadrature_provenance": True,
            "route_B_exactness_or_error_certificates": True,
            "full_SM_no_knob_closure": True,
        },
        "promotion_decision": {
            "conditional_route_A_source_certificate_valid": conditional_pass,
            "unpatched_route_A_source_theorem_proved": False,
            "route_B_independent_execution_valid": False,
            "unpatched_A_selected_promoted": False,
            "unpatched_b_selected_promoted": False,
            "unpatched_deltaTheta_C1_promoted": False,
            "unpatched_SM_parity_dynamic_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "theorem": {
            "name": "ConditionalPhysicalPhiFinC1SourceRowConstructionTheorem",
            "proved": True,
            "statement": (
                "A same-branch candidate PhysicalPhiFinC1ActionRestrictionSourceRow can be assembled "
                "from the existing MTT corpus support: local Weyl-variation action principle evidence, "
                "last-source binding, finite trace/Frobenius measure reduction, selected finite C1 quotient "
                "support, and source guardrails. When this constructed row is accepted as a Route A premise, "
                "the strict physical-source certificate validates. This is not yet the unpatched proof; "
                "the remaining theorem is to derive the same row from the selected Phi_fin finite emission "
                "morphism and selected Strominger/HYM minimizer, or to complete Route B independent provenance."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "patched_SM_parity_closure_preserved": previous["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SourceRowConstructionFromCorpus_or_RouteBProvenanceFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "candidate_source_row_constructed": True,
        "conditional_validator_passes": conditional_pass,
        "unpatched_theorem_closure_claimed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SourceRowConstructionFromCorpus or RouteBProvenanceFill v1

Status: `{STATUS}`.

This artifact creates the missing object as a conditional construction:
`PhysicalPhiFinC1ActionRestrictionSourceRow`.

## What was created

- A candidate same-branch `Phi_fin^C1` physical action restriction row.
- A restriction map
  `res_C1_to_selected_finite_Weyl_quotient(delta S_phys) =
  Tr_Frob(Phi_fin(delta S_phys)|Q_sel)`.
- A same-branch evidence index with {len(SAME_BRANCH_EVIDENCE)} filesystem-present
  sources.
- A conditional Route A certificate that passes the strict
  `validate_selected_physicalsourcecertificate_or_routeb.py` validator.

## Guardrail

This does not claim unpatched theorem closure. The row validates only when the
constructed source row is accepted as a same-branch source premise. The remaining
unpatched proof is to derive exactly this row from the selected `Phi_fin` finite
emission morphism and the selected Strominger/HYM minimizer, without inserting
the row itself.

## Next theorem

`{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
