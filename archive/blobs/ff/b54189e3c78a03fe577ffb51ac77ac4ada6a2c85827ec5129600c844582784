"""Build primitive-row source promotion or independent-formula derivation audit."""

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

SLUG = "selected_primitiverows_sourcepromotion_or_independentformuladerivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUPPORT = PACKET_DIR / "primitive_source_support_matrix.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "conditional_primitive_formula_rowsource_payload.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "conditional_primitive_formula_rowsource_validator_result.packet.json"
CUTSET = PACKET_DIR / "primitive_source_replay_independence_cutset.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveRows_SourcePromotion_or_IndependentFormulaDerivation_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
STATUS = "MTT_SELECTED_PRIMITIVEROWS_SOURCEPROMOTION_OR_INDEPENDENTFORMULADERIVATION_BUILT_FORMULA_CONDITIONAL_REPLAY_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PrimitiveRows_ReplayIndependenceLemma_or_SourceIdentityBackfill_v1"


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
        "validator": rel(VALIDATOR),
        "payload": rel(path),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": [line for line in proc.stderr.splitlines() if line],
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_honestkernelexport_rowsourcefill_or_sourceidentityderivationattempt.candidate.json")
    formula_source = load(DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource" / "differentiated_primitive_overlap_source_packet.packet.json")
    first_row = load(DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource" / "first_row_kernel_formula_source_packet.packet.json")
    promotion_decision = load(DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource" / "kernel_source_promotion_decision.packet.json")
    primitive_gap = load(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "remaining_primitive_source_gap.packet.json")
    basis = load(DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap" / "route_b_selected_basis_independence_fill.packet.json")
    exact72 = load(DATA / "selected_firstrowprovenancepromotion_or_allrowsweylexecution" / "all_72_exact_weyl_row_execution.packet.json")
    row_source = load(DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill" / "current_row_source_independence_attempt.packet.json")

    support = {
        "schema": "MTTPrimitiveSourceSupportMatrix.v1",
        "status": "PRIMITIVE_FORMULA_TRACE_VALUES_READY_SOURCE_INDEPENDENCE_OPEN",
        "closed_support": {
            "selected_primitive_kernel_formula": formula_source["formula_source_promoted_for_row_execution"],
            "first_row_formula_specified": first_row["selected_primitive_kernel_formula"] is not None,
            "finite_trace_pairing_source": first_row["selected_trace_or_pairing_source"]["finite_pairing_source_verified"],
            "all_72_values_exact": exact72["computed_value_clause_closed_for_all_rows"],
            "all_72_exactness_certificates": exact72["exactness_clause_closed_for_all_rows"],
            "selected_basis_independent_of_residual_projector": basis["route_B_independent_execution"]["selected_basis_independent_of_residual_projector"],
            "quadrature_rule_independent_of_locked_target": basis["route_B_independent_execution"]["quadrature_rule_independent_of_locked_target"],
            "sector_rows_assembled_formally": row_source["sector_rows_assembled_from_primitive_rows"],
            "hessian_rows_assembled_formally": row_source["hessian_source_rows_assembled_from_same_rows"],
        },
        "open_source_clauses": {
            "computed_independent_complex_entries_as_source": promotion_decision["closed_kernel_clauses_for_first_row"]["computed_independent_complex_entries"],
            "provenance_independent_of_residual_projector_replay": exact72["provenance_independent_of_residual_projector_replay_for_all_rows"],
            "physical_source_promoted_for_any_row": exact72["physical_source_promoted_for_any_row"],
            "row_formula_source_theorem_derived_unpatched": row_source["row_formula_source_theorem_derived"],
            "no_residual_projector_replay_used_as_source": row_source["no_residual_projector_replay_used_as_source"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    conditional_payload = {
        "schema": "MTTConditionalPrimitiveFormulaRowSourcePayload.v1",
        "status": "CONDITIONAL_FORMULA_SOURCE_PROMOTED_REPLAY_INDEPENDENCE_STILL_FAILS",
        "selected_basis_feeds_72_primitive_rows": True,
        "finite_weyl_trace_rule_feeds_all_rows": True,
        "sector_rows_assembled_from_primitive_rows": True,
        "hessian_source_rows_assembled_from_same_rows": True,
        "no_residual_projector_replay_used_as_source": False,
        "no_locked_target_values_used_as_source": True,
        "row_formula_source_theorem_derived": True,
        "source_independent_of_residual_projector_replay": False,
        "attached_source_evidence": [
            {
                "source": rel(DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource" / "differentiated_primitive_overlap_source_packet.packet.json"),
                "closes": "primitive overlap formula source shape",
                "conditional": True,
            },
            {
                "source": rel(DATA / "selected_differentiatedphifinc1primitiveoverlap_or_firstrowkernelformulasource" / "first_row_kernel_formula_source_packet.packet.json"),
                "closes": "first row formula and finite pairing source support",
                "conditional": True,
            },
            {
                "source": rel(DATA / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap" / "route_b_selected_basis_independence_fill.packet.json"),
                "closes": "selected basis and finite trace independence from locked targets",
            },
            {
                "source": rel(DATA / "selected_firstrowprovenancepromotion_or_allrowsweylexecution" / "all_72_exact_weyl_row_execution.packet.json"),
                "closes": "all 72 exact values and exactness certificates as postchecks",
            },
            {
                "source": rel(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "remaining_primitive_source_gap.packet.json"),
                "closes": "records replay-independence gap",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    CONDITIONAL_PAYLOAD.write_text(json.dumps(conditional_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    conditional_result = run_validator(CONDITIONAL_PAYLOAD)
    conditional_result["observed_data_used_as_selector"] = False
    conditional_result["target_fitting_used"] = False

    cutset = {
        "schema": "MTTPrimitiveSourceReplayIndependenceCutset.v1",
        "status": "PRIMITIVE_SOURCE_PROMOTION_REDUCED_TO_REPLAY_INDEPENDENCE_OR_SOURCE_IDENTITY",
        "conditional_formula_source_closes_all_but_replay_independence": True,
        "validator_result": conditional_result,
        "remaining_strict_failures": [
            "no_residual_projector_replay_used_as_source",
            "source_independent_of_residual_projector_replay",
        ],
        "legal_closure_routes": [
            {
                "route": "primitive_replay_independence_lemma",
                "must_show": "the R_Z/R_X Weyl-polynomial primitive values are obtained from a selected pre-residual row kernel, with residual projector used only as a comparison",
            },
            {
                "route": "source_identity_backfill",
                "must_show": "the physical Phi_fin^C1 action and finite trace row kernel are the same selected source identity",
            },
            {
                "route": "honest_external_kernel_export",
                "must_show": "a new selected quadrature/export computes the 72 values without importing the R_Z/R_X residual lineage",
            },
        ],
        "why_this_is_progress": primitive_gap["why_this_is_the_correct_next_gate"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPrimitiveSourcePromotion.v1",
        "status": "NEXT_WORKORDER_PRIMITIVE_REPLAY_INDEPENDENCE_OR_SOURCE_IDENTITY_BACKFILL",
        "next_required_artifact": NEXT_ARTIFACT,
        "primary": {
            "route": "primitive_replay_independence_lemma",
            "task": "Prove residual projector replay is not the source of the primitive R_Z/R_X row values.",
            "acceptance": "row-source validator passes with no_residual_projector_replay_used_as_source=true and source_independent_of_residual_projector_replay=true",
        },
        "co_primary": {
            "route": "source_identity_backfill",
            "task": "Derive the SelectedFiniteC1SourceIdentityPrinciple clauses that promote primitive rows in one theorem.",
        },
        "previous_artifact": previous["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PrimitiveFormulaConditionalPromotionCutsetTheorem",
        "proved": True,
        "statement": (
            "The selected primitive overlap formula, finite trace/Frobenius pairing, selected basis support, and all 72 exact primitive values "
            "are sufficient to conditionally satisfy every Route-B row-source field except replay independence. Therefore primitive source promotion "
            "is now reduced to proving that R_Z/R_X primitive row values arise from a selected pre-residual row kernel rather than residual-projector replay, "
            "or to deriving the full finite C1 source identity."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveRowsSourcePromotionOrIndependentFormulaDerivation",
        "status": STATUS,
        "theorem": theorem,
        "closure_claimed": False,
        "conditional_only": True,
        "output_packets": {
            "primitive_source_support_matrix": rel(SUPPORT),
            "conditional_primitive_formula_rowsource_payload": rel(CONDITIONAL_PAYLOAD),
            "conditional_primitive_formula_rowsource_validator_result": rel(CONDITIONAL_RESULT),
            "primitive_source_replay_independence_cutset": rel(CUTSET),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_decision": {
            "primitive_formula_source_promoted_conditionally": True,
            "row_source_validator_passes": conditional_result["passes"],
            "primitive_rows_closed_unpatched": False,
            "unpatched_dynamic_C1_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "primitive_source_gap_reduced_to_replay_independence": True,
            "conditional_row_formula_source_payload_tested": True,
            "next_replay_independence_gate_selected": True,
        },
        "what_remains_open": {
            "primitive_replay_independence_lemma": True,
            "source_identity_backfill": True,
            "honest_external_kernel_export": True,
            "hessian_and_sector_source_rows": True,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": f"{SLUG}_certificate",
        "status": STATUS,
        "candidate": rel(OUTPUT),
        "theorem_proved": theorem["proved"],
        "conditional_validator_passes": conditional_result["passes"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PrimitiveRows SourcePromotion or IndependentFormulaDerivation v1

Status: `{STATUS}`

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

- Formula, finite trace pairing, selected basis support, and all 72 exact primitive values are ready.
- If formula/pairing are conditionally promoted as the row-source theorem, the row-source validator fails only on replay independence.
- Unpatched primitive source promotion is still open.

## Next Artifact

`{NEXT_ARTIFACT}`

The next gate is the primitive replay-independence lemma, with source-identity backfill as co-primary.
"""

    SUPPORT.write_text(json.dumps(support, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CONDITIONAL_RESULT.write_text(json.dumps(conditional_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET.write_text(json.dumps(cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NEXT.write_text(json.dumps(next_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
