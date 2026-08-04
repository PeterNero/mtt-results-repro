"""Audit explicit source-axiom insertion and patched dynamic-C1 closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
AXIOM = PACKET_DIR / "accepted_local_source_axiom.packet.json"
PATCHED_CLOSURE = PACKET_DIR / "patched_dynamic_c1_closure_theorem.packet.json"
UNPATCHED_EXIT = PACKET_DIR / "unpatched_exit_status.packet.json"
LOCAL_APPENDIX = PACKET_DIR / "local_paper_appendix_insert.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DifferentiatedPhiFinC1_AxiomInsertion_PatchedClosure_or_UnpatchedExit_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_DIFFERENTIATEDPHIFINC1_AXIOM_INSERTED_PATCHED_DYNAMIC_C1_CLOSED_UNPATCHED_OPEN"
NEXT = "MTT_Selected_HonestGalerkinC1Tables_or_UnpatchedSourceRuleDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    axiom = load(AXIOM)
    patched = load(PATCHED_CLOSURE)
    unpatched = load(UNPATCHED_EXIT)
    appendix = load(LOCAL_APPENDIX)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem flag missing")

    require(axiom["status"] == "LOCAL_SOURCE_AXIOM_ACCEPTED_IN_THIS_PROOF_SPINE", "axiom status mismatch")
    require(axiom["accepted_as"] == "explicit axiom/premise, not derived theorem", "axiom accepted_as mismatch")
    require(axiom["external_obsidian_papers_modified"] is False, "external paper overmodified")
    for key in ["unpatched_derivation", "true_SM_equivalence", "no_knob_flavor_constants"]:
        require(axiom["guardrails"][key] is True, f"axiom guardrail missing {key}")

    require(patched["status"] == "PATCHED_DYNAMIC_C1_PACKET_CLOSED_BY_ACCEPTED_SOURCE_AXIOM", "patched status mismatch")
    for key in [
        "phase_R_Z_source",
        "shift_R_X_source",
        "A_selected",
        "b_selected",
        "deltaTheta_C1",
        "sector_response_matrices",
        "dynamic_C1_source_owner_packet",
    ]:
        require(patched["promoted_objects"][key] is True, f"patched object not promoted: {key}")
    exact = patched["exact_values"]
    require(exact["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A mismatch")
    require(exact["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(exact["b_norm_sq"] == 24.0, "b norm mismatch")
    require(exact["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(exact["rank"] == 2, "rank mismatch")
    for key in [
        "unpatched_source_rule_derivation",
        "honest_independent_galerkin_export",
        "true_SM_equivalence",
        "no_knob_flavor_constants",
    ]:
        require(patched["does_not_close"][key] is True, f"patched guard missing {key}")

    require(unpatched["status"] == "UNPATCHED_EXIT_REMAINS_OPEN_AFTER_LOCAL_AXIOM_INSERTION", "unpatched status mismatch")
    require(unpatched["unpatched_dynamic_C1_closed"] is False, "unpatched overclosed")
    require(unpatched["honest_galerkin_table_exported"] is False, "Galerkin overexported")
    require(unpatched["source_rule_derived_unpatched"] is False, "source rule overderived")
    require(len(unpatched["remaining_exits"]) == 2, "remaining exits mismatch")

    require(appendix["status"] == "LOCAL_APPENDIX_INSERT_CREATED_EXTERNAL_PAPERS_UNTOUCHED", "appendix status mismatch")
    require(appendix["external_papers_modified"] is False, "appendix overmodified external papers")
    require(len(appendix["proof_steps"]) == 4, "appendix proof steps mismatch")
    require("A^T A=12 I_2" in appendix["theorem_statement"], "appendix theorem text missing values")

    closure = data["closure_decision"]
    require(closure["local_source_axiom_accepted"] is True, "local axiom not accepted")
    require(closure["patched_dynamic_C1_packet_closed"] is True, "patched dynamic C1 not closed")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "unpatched dynamic C1 overclosed")
    require(closure["external_papers_modified"] is False, "external papers overmodified")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(closure["no_knob_closed"] is False, "no-knob overclosed")
    require(data["closure_claimed"] is False, "global closure overclaimed")

    for key in [
        "explicit_local_source_axiom_inserted",
        "patched_dynamic_C1_packet_closed",
        "local_appendix_insert_created",
        "exact_values_promoted_inside_patched_spine",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing {key}")
    for key in [
        "derive_source_axiom_unpatched",
        "export_honest_selected_galerkin_tables",
        "insert_or_revise_external_papers_if_desired",
        "true_SM_equivalence_without_axiom",
        "no_knob_flavor_constants",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining flag missing {key}")

    require("local premise" in note, "note missing local premise guard")
    require("External Obsidian papers were not modified" in note, "note missing external paper guard")

    for packet in [data, axiom, patched, unpatched, appendix, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
