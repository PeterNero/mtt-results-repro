"""Audit DifferentiatedPhiFinC1 source-rule derivation or axiom promotion."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DERIVATION = PACKET_DIR / "unpatched_source_rule_derivation_attempt.packet.json"
AXIOM_PROMOTION = PACKET_DIR / "explicit_axiom_promotion_package.packet.json"
PAPER_INSERTION = PACKET_DIR / "paper_insertion_workorder.packet.json"
DECISION = PACKET_DIR / "derivation_or_axiom_promotion_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_Derivation_or_AxiomPromotion_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_SOURCERULE_DERIVATION_OPEN_AXIOMPROMOTION_READY"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_Derivation_Attack_or_PaperAxiomInsertion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    derivation = load(DERIVATION)
    axiom = load(AXIOM_PROMOTION)
    paper = load(PAPER_INSERTION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "decision theorem missing")

    require(derivation["status"] == "UNPATCHED_DERIVATION_ATTEMPT_SUPPORT_COMPLETE_REQUIRED_CLAUSES_OPEN", "derivation status mismatch")
    require(derivation["unpatched_source_rule_proved_now"] is False, "unpatched source rule overproved")
    for key in [
        "physical_C1_variation_principle",
        "selected_PhiFinC1_applies_Q_residual",
        "selected_dynamic_trace_boundary_cancellation",
        "same_source_b_selected_physical_emission",
    ]:
        clause = derivation["required_clauses"][key]
        require(clause["closed_now"] is False, f"{key} overclosed")
        require(clause["conditional_witness_value"] is True, f"{key} conditional witness missing")
    require(len(derivation["why_not_proved"]) == 3, "why-not-proved list mismatch")

    require(axiom["status"] == "EXPLICIT_AXIOM_PROMOTION_PACKAGE_READY_NOT_INSERTED", "axiom package status mismatch")
    require("DifferentiatedPhiFinC1ResidualProjectorAxiom" == axiom["axiom_name"], "axiom name mismatch")
    for key in ["patched_spine_dynamic_C1_closed", "A_selected_promoted", "b_selected_promoted", "deltaTheta_C1_promoted", "sector_response_matrices_promoted"]:
        require(axiom["if_inserted_then"][key] is True, f"axiom consequence missing {key}")
    for key in ["unpatched_derivation", "true_SM_equivalence", "no_knob_flavor_constants"]:
        require(axiom["does_not_by_itself_close"][key] is True, f"axiom guard missing {key}")
    require("declared source axiom" in axiom["acceptance_guardrail"], "axiom guardrail text missing")

    require(paper["status"] == "PAPER_INSERTION_WORKORDER_READY_AWAITING_APPROVAL_OR_DERIVATION", "paper workorder status mismatch")
    require(len(paper["targets"]) == 3, "paper target count mismatch")
    require(paper["external_papers_modified_now"] is False, "external papers overmodified")
    require("A^T A=12 I_2" in paper["theorem_text"], "paper theorem text missing values")

    require(decision["status"] == "DERIVATION_NOT_CLOSED_AXIOM_PROMOTION_READY", "decision status mismatch")
    require(decision["decision"]["unpatched_derivation_closes_now"] is False, "decision overclosed")
    require(decision["decision"]["axiom_promotion_package_ready"] is True, "axiom package not ready")
    require(decision["decision"]["honest_galerkin_replacement_still_available"] is True, "Galerkin exit missing")
    require(decision["superset_strategy"]["paths_used_as_knobs"] is False, "superset paths used as knobs")

    closure = data["closure_decision"]
    require(closure["unpatched_source_rule_proved"] is False, "unpatched closure overclaimed")
    require(closure["axiom_promotion_ready"] is True, "axiom readiness missing")
    require(closure["patched_spine_dynamic_C1_closed_if_axiom_inserted"] is True, "patched consequence missing")
    require(closure["external_papers_modified"] is False, "external paper mutation overclaimed")
    require(closure["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(closure["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "global closure overclaimed")

    for key in [
        "four_clause_derivation_failure_matrix_built",
        "explicit_axiom_promotion_package_ready",
        "paper_insertion_workorder_ready",
        "conditional_witness_retained",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing {key}")
    for key in [
        "derive_axiom_unpatched",
        "or_insert_axiom_into_target_papers",
        "or_export_honest_selected_galerkin_tables",
        "true_SM_equivalence_without_axiom",
        "no_knob_flavor_constants",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining flag missing {key}")

    require("unpatched derivation is still open" in note, "note missing unpatched guard")
    require("paper insertion workorder is ready but not applied" in note, "note missing paper guard")

    for packet in [data, derivation, axiom, paper, decision, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
