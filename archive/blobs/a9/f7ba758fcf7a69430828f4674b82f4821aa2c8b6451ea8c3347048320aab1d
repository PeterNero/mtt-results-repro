"""Audit perfected final DynamicC1 gate / source-axiom decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PATCHED = PACKET_DIR / "patched_spine_closure_mode.packet.json"
UNPATCHED = PACKET_DIR / "unpatched_theorem_mode.packet.json"
DECISION = PACKET_DIR / "source_axiom_decision_matrix.packet.json"
PAPER_TEXT = PACKET_DIR / "paper_ready_source_axiom_and_theorem_text.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1_FinalGate_Perfection_or_SourceAxiomDecision_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DYNAMICC1_FINALGATE_PERFECTED_PATCHED_CLOSE_UNPATCHED_PROOF_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1_SourceRule_Derivation_or_AxiomPromotion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    patched = load(PATCHED)
    unpatched = load(UNPATCHED)
    decision = load(DECISION)
    paper = load(PAPER_TEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem flag missing")

    require(patched["status"] == "PATCHED_SPINE_DYNAMIC_C1_CLOSED_BY_EXPLICIT_LOCAL_AXIOM", "patched status mismatch")
    payload = patched["patch_payload"]
    for key in [
        "Phi_fin_C1_applies_Q_residual",
        "R_Z_phase_clock_source_emitted",
        "R_X_shift_vertex_source_emitted",
        "b_selected_source_emitted",
    ]:
        require(payload[key] is True, f"patch payload missing {key}")
    for key in ["A_selected", "b_selected", "deltaTheta_C1", "SM_parity_dynamic_packet", "sector_response_matrices"]:
        require(patched["promotions_inside_patched_spine"][key] is True, f"patched promotion missing {key}")
    require(patched["guardrails"]["not_derived_from_unpatched_MTT_axioms"] is True, "patched derivation overclaim")
    require(patched["guardrails"]["does_not_close_true_SM_equivalence"] is True, "true equivalence overclaim")
    require(patched["guardrails"]["does_not_close_no_knob_flavor_constants"] is True, "no-knob overclaim")
    require(patched["guardrails"]["external_main_papers_not_modified"] is True, "external paper mutation overclaim")
    require(patched["exact_values"]["A_transpose_b"] == [12.0, 12.0], "patched ATb mismatch")
    require(patched["exact_values"]["deltaTheta_C1"] == [1.0, 1.0], "patched delta mismatch")

    require(unpatched["status"] == "UNPATCHED_THEOREM_OPEN_EXACT_VALUES_READY", "unpatched status mismatch")
    failures = unpatched["current_failures"]
    require(failures["source_rule_proved"] is False, "source rule overproved")
    require(failures["honest_galerkin_table_exported"] is False, "Galerkin table overexported")
    require(failures["honest_independent_galerkin_execution_passes"] is False, "honest Galerkin overclaimed")
    require(failures["unpatched_A_selected_promoted"] is False, "unpatched A overpromoted")
    require(failures["unpatched_b_selected_promoted"] is False, "unpatched b overpromoted")
    for key in ["A_selected", "b_selected", "deltaTheta_C1", "SM_parity_dynamic_packet", "sector_response_matrices"]:
        require(unpatched["promotions_in_unpatched_spine"][key] is False, f"unpatched promotion overclaimed {key}")
    require(len(unpatched["legal_unpatched_exits"]) == 2, "unpatched exits mismatch")

    require(decision["mode_table"]["SM_parity_with_explicit_local_source_axiom"]["dynamic_C1_packet_closed"] is True, "patched mode not closed")
    require(decision["mode_table"]["unpatched_no_knob_theorem"]["dynamic_C1_packet_closed"] is False, "unpatched mode overclosed")
    require(decision["mode_table"]["honest_galerkin_replacement"]["dynamic_C1_packet_closed"] is False, "Galerkin mode overclosed")
    require(decision["superset_strategy"]["paths_used_as_knobs"] is False, "superset path used as knobs")
    require(decision["superset_strategy"]["locked_target"] == "same exact R_Z/R_X/b_selected/deltaTheta dynamic C1 packet", "locked target mismatch")

    require(paper["status"] == "PAPER_READY_CONDITIONAL_THEOREM_TEXT_BUILT", "paper text status mismatch")
    require("Differentiated PhiFin C1 Residual-Projector Source Axiom" in paper["axiom_title"], "axiom title mismatch")
    require("Without this axiom" in paper["unpatched_status_sentence"], "unpatched sentence missing")

    closure = data["closure_decision"]
    require(closure["patched_spine_dynamic_C1_closed"] is True, "patched closure missing")
    require(closure["unpatched_dynamic_C1_closed"] is False, "unpatched closure overclaimed")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclaimed")
    require(closure["no_knob_closed"] is False, "no-knob overclaimed")
    require(closure["external_papers_modified"] is False, "external papers overmodified")
    require(data["closure_claimed"] is False, "global closure overclaimed")

    for key in [
        "final_gate_perfected",
        "patched_spine_status_made_explicit",
        "unpatched_status_made_explicit",
        "paper_ready_axiom_text_created",
        "exact_values_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing {key}")
    for key in [
        "derive_source_axiom_from_unpatched_MTT",
        "or_accept_source_axiom_into_target_papers",
        "or_export_honest_selected_Galerkin_C1_tables",
        "true_SM_equivalence_without_patch",
        "no_knob_flavor_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining flag missing {key}")

    require("Patched mode" in note and "Unpatched mode" in note, "note missing mode split")

    for packet in [data, patched, unpatched, decision, paper, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
