"""Import Route-C residual-projector insertion / Galerkin first-run spec."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_differentiated_phifinc1_contract_import_certificate.json"
UPSTREAM_SLUG = "selected_residualprojectoraxiominsertion_or_galerkinc1firstexecution"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
UPSTREAM_AXIOM = UPSTREAM_DIR / "residual_projector_axiom_insertion_package.packet.json"
UPSTREAM_GALERKIN = UPSTREAM_DIR / "galerkin_c1_first_execution_spec.packet.json"
UPSTREAM_DECISION = UPSTREAM_DIR / "route_decision_and_next_inputs.packet.json"

OUTPUT_PACKET = DATA / "routec_residual_projector_insertion_spec_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_residual_projector_insertion_spec_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_ResidualProjectorInsertionSpec_Import_v1.md"

STATUS = "ROUTEC_RESIDUAL_PROJECTOR_INSERTION_SPEC_IMPORTED_INPUTS_OPEN"
PREVIOUS_STATUS = "ROUTEC_DIFFERENTIATED_PHIFINC1_CONTRACT_IMPORTED_LANES_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_RESIDUALPROJECTORAXIOMINSERTION_OR_GALERKINC1FIRSTEXECUTION_BUILT_INSERTION_SPEC_OPEN"
NEXT = "MTT_Selected_GalerkinC1InputBasisFill_or_ResidualProjectorAxiomCorpusPatch_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def draft_text_contains_all(path_text: str, phrases: list[str]) -> bool:
    text = (SM / path_text).read_text(encoding="utf-8")
    return all(phrase in text for phrase in phrases)


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    axiom = load(UPSTREAM_AXIOM)
    galerkin = load(UPSTREAM_GALERKIN)
    decision = load(UPSTREAM_DECISION)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")
    payload = axiom["paper_ready_theorem_slot"]["payload"]
    values = axiom["paper_ready_theorem_slot"]["exact_source_values_to_emit"]
    replay = axiom["after_insertion_replay"]["numeric_replay"]

    required_inputs = galerkin["required_input_files"]
    missing_inputs = decision["route_B_honest_galerkin_execution"]["next_missing_inputs"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_ResidualProjectorAxiomInsertion_or_GalerkinC1FirstExecution_v1",
        "F1_upstream_packet_proved_not_closed": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["observed_data_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["theorem_proved"] is True
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["next_required_artifact"] == NEXT,
        "F3_axiom_appendix_ready_not_patched": axiom["status"] == "PAPER_APPENDIX_DRAFTS_READY_NOT_CORPUS_PATCHED"
        and len(axiom["target_drafts"]) == 3
        and all(
            draft_text_contains_all(
                path_text,
                ["Theorem Slot I9", "observed masses", "target residual fitting"],
            )
            for path_text in axiom["target_drafts"].values()
        )
        and payload["selected_differentiated_PhiFinC1_applies_Q_residual"] is True
        and payload["phase_R_Z_selected"] is True
        and payload["shift_R_X_selected"] is True
        and payload["b_source_emitted"] is True
        and axiom["inserted_into_main_corpus_now"] is False,
        "F4_axiom_replay_exact": values["routed_total_residual_norm_sq"] == 12.0
        and values["conditional_b_norm_sq"] == 24.0
        and replay["rank"] == 2
        and replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and replay["A_transpose_b"] == [12.0, 12.0]
        and replay["deltaTheta_C1"] == [1.0, 1.0],
        "F5_galerkin_spec_ready_inputs_missing": galerkin["status"]
        == "FIRST_EXECUTION_SPEC_READY_INPUT_BASIS_VALUES_MISSING"
        and galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72
        and galerkin["coordinate_order"]["sector_order"] == ["u", "e", "d", "nuD"]
        and set(required_inputs) == {
            "zero_mode_basis_packet",
            "primitive_contraction_terms_packet",
            "hessian_or_source_vector_packet",
            "sector_response_matrix_packet",
        }
        and len(missing_inputs) == 4
        and galerkin["first_execution_run_now"] is False
        and len(galerkin["why_not_run_now"]) == 3,
        "F6_decision_keeps_two_routes_open": decision["status"] == "TWO_ROUTES_READY_NEXT_INPUTS_SHARP"
        and decision["recommended_next"] == NEXT
        and decision["route_A_residual_projector_axiom"]["ready_as_paper_appendix_draft"] is True
        and decision["route_A_residual_projector_axiom"]["main_corpus_patched_now"] is False
        and decision["route_B_honest_galerkin_execution"]["ready_as_execution_spec"] is True
        and decision["route_B_honest_galerkin_execution"]["run_now"] is False
        and "Two superset paths" in decision["superset_strategy"],
        "F7_closed_flags_are_preparation_only": all(
            upstream["what_closes_now"][key] is True
            for key in [
                "residual_projector_axiom_appendix_drafts_written",
                "galerkin_first_execution_schema_fixed",
                "route_A_and_route_B_locked_to_same_72_real_target",
                "next_input_files_declared",
                "observed_constants_excluded_as_selectors",
            ]
        ),
        "F8_remaining_gates_preserved": all(
            upstream["what_remains_open"][key] is True
            for key in [
                "patch_main_corpus_with_residual_projector_axiom_or_prove_it",
                "fill_zero_mode_basis_packet",
                "fill_primitive_contraction_terms_packet",
                "fill_hessian_source_vector_packet",
                "fill_sector_response_matrix_packet",
                "run_first_honest_Galerkin_C1_execution",
                "promote_A_selected",
                "promote_b_selected",
                "promote_deltaTheta_C1",
                "SM_parity_dynamic_packet_closure",
                "true_SM_equivalence_closure",
            ]
        ),
        "F9_no_promotion_overclaim": all(
            upstream["promotion_decision"][key] is False
            for key in [
                "main_corpus_axiom_patch_applied_now",
                "residual_projector_axiom_proved_now",
                "first_Galerkin_C1_execution_run_now",
                "A_selected_promoted",
                "b_selected_promoted",
                "deltaTheta_C1_promoted",
                "SM_parity_dynamic_packet_closed",
                "true_SM_equivalence_closed",
            ]
        )
        and "Nothing is promoted yet" in note,
    }

    summary = {
        "route_A_appendix_drafts_ready": True,
        "route_A_main_corpus_patched_now": False,
        "route_B_execution_spec_ready": True,
        "route_B_first_execution_run_now": False,
        "strict_target_real_coordinates": galerkin["strict_coordinate_target"]["total_real_coordinates"],
        "sector_order": galerkin["coordinate_order"]["sector_order"],
        "required_input_files": required_inputs,
        "missing_input_count": len(missing_inputs),
        "conditional_A_transpose_A": replay["A_transpose_A"],
        "conditional_A_transpose_b": replay["A_transpose_b"],
        "conditional_deltaTheta_C1": replay["deltaTheta_C1"],
        "conditional_rank": replay["rank"],
        "conditional_b_norm_sq": values["conditional_b_norm_sq"],
    }

    return {
        "packet": "RouteC_ResidualProjectorInsertionSpec_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_axiom_insertion_package": str(UPSTREAM_AXIOM),
            "upstream_galerkin_first_execution_spec": str(UPSTREAM_GALERKIN),
            "upstream_route_decision": str(UPSTREAM_DECISION),
        },
        "theorem": {
            "name": "RouteCResidualProjectorInsertionSpecImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The residual-projector axiom lane is appendix-ready and the "
                "honest Galerkin lane is execution-spec-ready, both locked to "
                "the strict 72-real C1 target.  This imports the fork and the "
                "four missing input packets; it does not patch the corpus or "
                "run selected Galerkin C1 values."
            ),
        },
        "checks": checks,
        "residual_projector_insertion_spec_summary": summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "axiom_insertion_package": axiom,
            "galerkin_first_execution_spec": galerkin,
            "route_decision_and_next_inputs": decision,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_main_corpus_axiom_patch_applied": False,
            "claims_residual_projector_axiom_proved": False,
            "claims_first_Galerkin_C1_execution_run": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_deltaTheta_C1": False,
            "claims_SM_parity_dynamic_packet_closure": False,
            "claims_true_SM_equivalence_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCResidualProjectorInsertionSpecImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "residual_projector_insertion_spec_summary": packet[
            "residual_projector_insertion_spec_summary"
        ],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["residual_projector_insertion_spec_summary"]
    inputs = "\n".join(f"- `{key}`: `{value}`" for key, value in s["required_input_files"].items())
    return f"""# RouteC Residual Projector Insertion Spec Import v1

Status: `{cert["status"]}`.

The next Route-C fork is now imported as a reproducible checkpoint:

```text
Route A: residual-projector axiom appendix draft, not corpus-patched
Route B: honest Galerkin C1 first-execution spec, not run
```

Both lanes are locked to the same strict target:

```text
sectors = {s["sector_order"]}
total real coordinates = {s["strict_target_real_coordinates"]}
conditional rank = {s["conditional_rank"]}
A^T A = {s["conditional_A_transpose_A"]}
A^T b = {s["conditional_A_transpose_b"]}
deltaTheta_C1 = {s["conditional_deltaTheta_C1"]}
```

The required Galerkin input packets are:

{inputs}

Nothing is promoted yet: no main-corpus axiom patch, no selected Galerkin run,
no `A_selected`, no `b_selected`, no `deltaTheta_C1`, and no SM dynamic closure.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
