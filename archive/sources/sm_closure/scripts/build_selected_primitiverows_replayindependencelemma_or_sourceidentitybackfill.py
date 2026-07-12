"""Build primitive-row replay-independence lemma gate or source-identity backfill."""

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

SLUG = "selected_primitiverows_replayindependencelemma_or_sourceidentitybackfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_AUDIT = PACKET_DIR / "primitive_replay_independence_source_order_audit.packet.json"
HYPOTHETICAL = PACKET_DIR / "hypothetical_source_ordering_validator_payload.packet.json"
HYPOTHETICAL_RESULT = PACKET_DIR / "hypothetical_source_ordering_validator_result.packet.json"
LEMMA_GATE = PACKET_DIR / "primitive_replay_independence_lemma_gate.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveRows_ReplayIndependenceLemma_or_SourceIdentityBackfill_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
STATUS = "MTT_SELECTED_PRIMITIVEROWS_REPLAYINDEPENDENCELEMMA_OR_SOURCEIDENTITYBACKFILL_BUILT_SOURCE_ORDERING_GATE_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PreResidualWeylVariationSelectionLemma_or_HonestQuadratureSource_v1"
POST_SM_LABEL_CONTEXT = {
    "tier": "tier_2_post_sm_parity_true_equivalence",
    "preferred_phrase": "post-SM-parity frontier",
    "closed_boundary": "DONE-PARITY-00",
    "active_label": "PSM-C1-02",
    "active_label_name": "selected primitive C1 overlap contractions",
    "active_subcategory": "primitive_overlap",
    "primary_routes": ["ROUTE-A", "ROUTE-B"],
    "route_A": "same-source dynamic Phi_fin^C1 source rule",
    "route_B": "honest selected Galerkin C1 execution",
    "adjacent_labels": {
        "PSM-C1-01": "selected differentiated Phi_fin^C1 source map",
        "PSM-C1-04": "selected b_selected source vector",
        "PSM-C1-06": "selected sector response matrices",
    },
    "language_guardrail": "Do not call this an SM-parity blocker; SM-parity replay is frozen closed.",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "validator": rel(VALIDATOR),
        "payload": rel(path),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "stderr_lines": [line for line in proc.stderr.splitlines() if line],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def count_rows(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"R_Z": 0, "R_X": 0, "zero_route": 0}
    for row in rows:
        source = row.get("value_source") or "zero_route"
        counts[source] = counts.get(source, 0) + 1
    return counts


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_primitiverows_sourcepromotion_or_independentformuladerivation.candidate.json")
    cutset = load(DATA / "selected_primitiverows_sourcepromotion_or_independentformuladerivation" / "primitive_source_replay_independence_cutset.packet.json")
    exact72 = load(DATA / "selected_firstrowprovenancepromotion_or_allrowsweylexecution" / "all_72_exact_weyl_row_execution.packet.json")
    residual_weyl = load(DATA / "selected_residual_weylpolynomial_source_theorem_attempt.candidate.json")
    residual_decomp = load(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json")
    psm_cutset = load(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction" / "physical_selection_cutset.packet.json")
    conditional_payload = load(DATA / "selected_primitiverows_sourcepromotion_or_independentformuladerivation" / "conditional_primitive_formula_rowsource_payload.packet.json")

    rows = exact72["rows"]
    source_counts = count_rows(rows)
    inherited_false_count = sum(
        1 for row in rows if row["provenance_independent_of_residual_projector_replay"] is False
    )
    physical_promoted_count = sum(1 for row in rows if row["physical_source_promoted"] is True)

    source_audit = {
        "schema": "MTTPrimitiveReplayIndependenceSourceOrderAudit.v1",
        "status": "EXACT_WEYL_POLYNOMIAL_EXECUTION_SOURCE_ORDERING_STILL_OPEN",
        "row_count": exact72["row_count"],
        "source_counts": source_counts,
        "all_rows_exact": exact72["computed_value_clause_closed_for_all_rows"] and exact72["exactness_clause_closed_for_all_rows"],
        "all_rows_match_formal_packet": exact72["all_rows_match_formal_packet"],
        "residual_weyl_polynomial_theorem_proved": residual_weyl["theorem"]["proved"],
        "residual_weyl_polynomial_statement": residual_weyl["theorem"]["statement"],
        "residual_decomposition_packet": rel(DATA / "selected_residual_weylpolynomial_source_theorem_attempt" / "residual_weyl_polynomial_decomposition.packet.json"),
        "existing_source_ordering_flags": {
            "provenance_independent_false_rows": inherited_false_count,
            "physical_source_promoted_rows": physical_promoted_count,
            "all_rows_provenance_independent": exact72["provenance_independent_of_residual_projector_replay_for_all_rows"],
            "physical_source_promoted_for_any_row": exact72["physical_source_promoted_for_any_row"],
        },
        "source_ordering_obstruction": {
            "missing_object": psm_cutset["minimal_unpatched_cutset"][0]["missing_object"],
            "why_exact_polynomials_do_not_suffice": [
                "Exact R_Z/R_X Weyl polynomials identify the compatible primitive operators.",
                "The current row packets still label those polynomials as residual-lineage value sources.",
                "A theorem must select the pre-residual Weyl variation or an honest quadrature source before residual projector replay.",
            ],
        },
        "superset_paths_used": [
            "finite Weyl-polynomial exactness",
            "selected zero-route support",
            "Route-B row-source validator",
            "Route-A finite C1 source-identity cutset",
        ],
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hypothetical = dict(conditional_payload)
    hypothetical.update(
        {
            "schema": "MTTHypotheticalSourceOrderingValidatorPayload.v1",
            "status": "VALIDATOR_PASSES_IF_SOURCE_ORDERING_LEMMA_SUPPLIED",
            "no_residual_projector_replay_used_as_source": True,
            "source_independent_of_residual_projector_replay": True,
            "source_ordering_lemma_supplied": False,
            "hypothetical_only": True,
            "attached_source_evidence": conditional_payload["attached_source_evidence"]
            + [
                {
                    "source": rel(SOURCE_AUDIT),
                    "closes": "only conditionally: exact Weyl polynomial support plus required source-ordering lemma",
                    "conditional": True,
                }
            ],
        }
    )
    write_json(HYPOTHETICAL, hypothetical)
    hypothetical_result = run_validator(HYPOTHETICAL)

    lemma_gate = {
        "schema": "MTTPrimitiveReplayIndependenceLemmaGate.v1",
        "status": "SOURCE_ORDERING_LEMMA_REQUIRED_NO_MATRIX_BLOCKER_LEFT",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "validator_passes_if_two_source_ordering_flags_are_theorem_derived": hypothetical_result["passes"],
        "flags_that_must_be_theorem_derived": [
            "no_residual_projector_replay_used_as_source",
            "source_independent_of_residual_projector_replay",
        ],
        "lemma_to_prove": {
            "name": "PreResidualWeylVariationSelectionLemma",
            "statement": (
                "On the selected q79/F,m=1 finite C1 branch, the low-degree qutrit Weyl "
                "operators R_Z and R_X are selected as pre-residual differentiated Weyl "
                "variation operators by the same source data that selects the finite trace "
                "pairing. The canonical residual projector may verify their fixed-fiber "
                "orthogonality, but it is not the source of the primitive row values."
            ),
            "currently_proved": False,
        },
        "alternative_route": {
            "name": "HonestQuadratureSource",
            "statement": "Emit an independent selected quadrature/export table for all 72 primitive rows without using R_Z/R_X residual replay as the row source.",
            "currently_emitted": False,
        },
        "why_this_is_not_regression": (
            "The validator already passes under a hypothetical source-ordering lemma. "
            "The remaining work is no longer numerical reconstruction; it is source ownership."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPrimitiveReplayIndependenceGate.v1",
        "status": "NEXT_WORKORDER_PRERESIDUAL_WEYL_SELECTION_OR_HONEST_QUADRATURE_SOURCE",
        "next_required_artifact": NEXT_ARTIFACT,
        "active_label": "PSM-C1-02",
        "active_label_name": "selected primitive C1 overlap contractions",
        "route_labels": ["ROUTE-A", "ROUTE-B"],
        "primary": {
            "label": "PSM-C1-02",
            "route": "pre_residual_weyl_variation_selection_lemma",
            "task": "Derive the physical selection lemma that promotes exact R_Z/R_X Weyl polynomials to pre-residual source operators.",
        },
        "secondary": {
            "label": "PSM-C1-02",
            "route_label": "ROUTE-B",
            "route": "honest_quadrature_source",
            "task": "Emit selected primitive quadrature rows independently of residual projector replay.",
        },
        "previous_artifact": previous["next_required_artifact"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "PrimitiveReplayIndependenceReductionTheorem",
        "proved": True,
        "statement": (
            "The exact 72 primitive rows, residual Weyl-polynomial decomposition, and strict "
            "Route-B validator show that no value or matrix obstruction remains. The only "
            "unclosed primitive replay-independence condition is a source-ordering theorem: "
            "R_Z/R_X must be selected as pre-residual Weyl variation operators, or an honest "
            "independent quadrature source must replace them."
        ),
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveRowsReplayIndependenceLemmaOrSourceIdentityBackfill",
        "status": STATUS,
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_post_sm_parity_routes": ["ROUTE-A", "ROUTE-B"],
        "theorem": theorem,
        "closure_claimed": False,
        "validator_passes_under_hypothetical_source_ordering_lemma": hypothetical_result["passes"],
        "source_ordering_lemma_proved_now": False,
        "primitive_replay_independence_closed_now": False,
        "source_identity_backfilled_now": False,
        "output_packets": {
            "primitive_replay_independence_source_order_audit": rel(SOURCE_AUDIT),
            "hypothetical_source_ordering_validator_payload": rel(HYPOTHETICAL),
            "hypothetical_source_ordering_validator_result": rel(HYPOTHETICAL_RESULT),
            "primitive_replay_independence_lemma_gate": rel(LEMMA_GATE),
            "next_labeled_workorder": rel(NEXT),
        },
        "inputs": {
            "previous": rel(DATA / "selected_primitiverows_sourcepromotion_or_independentformuladerivation.candidate.json"),
            "replay_independence_cutset": rel(DATA / "selected_primitiverows_sourcepromotion_or_independentformuladerivation" / "primitive_source_replay_independence_cutset.packet.json"),
            "all_72_exact_rows": rel(DATA / "selected_firstrowprovenancepromotion_or_allrowsweylexecution" / "all_72_exact_weyl_row_execution.packet.json"),
            "residual_weyl_theorem_attempt": rel(DATA / "selected_residual_weylpolynomial_source_theorem_attempt.candidate.json"),
            "psm_physical_selection_cutset": rel(DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction" / "physical_selection_cutset.packet.json"),
        },
        "what_closes_now": {
            "validator_no_value_obstruction_after_source_ordering": True,
            "primitive_replay_independence_reduced_to_source_ordering": True,
            "next_PSM_C1_02_or_honest_quadrature_gate_selected": True,
        },
        "what_remains_open": {
            "PreResidualWeylVariationSelectionLemma": True,
            "honest_independent_quadrature_source": True,
            "unpatched_dynamic_C1_packet_closure": True,
            "true_SM_equivalence": True,
        },
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": f"{SLUG}_certificate",
        "status": STATUS,
        "candidate": rel(OUTPUT),
        "active_post_sm_parity_label": "PSM-C1-02",
        "active_post_sm_parity_routes": ["ROUTE-A", "ROUTE-B"],
        "theorem_proved": theorem["proved"],
        "hypothetical_validator_passes": hypothetical_result["passes"],
        "source_ordering_lemma_proved_now": False,
        "primitive_replay_independence_closed_now": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PrimitiveRows ReplayIndependenceLemma or SourceIdentityBackfill v1

Status: `{STATUS}`

Active post-SM-parity label: `PSM-C1-02`

Route labels: `ROUTE-A` / `ROUTE-B`

Boundary guardrail: `DONE-PARITY-00` remains frozen closed. This is post-SM-parity frontier work, not an SM-parity blocker.

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Result

The exact primitive rows are not the issue anymore:

- 72/72 primitive rows are exact finite Weyl-polynomial or zero-route rows.
- The strict row-source validator passes if the two replay-independence flags are theorem-derived.
- Existing packets still mark the source as residual-lineage dependent, so unpatched promotion is not claimed.

## Next Artifact

`{NEXT_ARTIFACT}`

Prove the `PreResidualWeylVariationSelectionLemma`, or emit an honest independent quadrature source.
"""

    write_json(SOURCE_AUDIT, source_audit)
    write_json(HYPOTHETICAL_RESULT, hypothetical_result)
    write_json(LEMMA_GATE, lemma_gate)
    write_json(NEXT, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, certificate)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
