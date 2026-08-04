"""Audit selected source-row construction from corpus or Route B provenance fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sourcerowconstructionfromcorpus_or_routebprovenancefill"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EVIDENCE_INDEX = PACKET_DIR / "corpus_source_evidence_index.packet.json"
SOURCE_ROW = PACKET_DIR / "candidate_phifin_action_restriction_source_row.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "conditional_route_a_source_certificate.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "conditional_route_a_validator_result.packet.json"
ROUTE_B_STATUS = PACKET_DIR / "route_b_provenance_fill_status.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_source_row_construction.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SourceRowConstructionFromCorpus_or_RouteBProvenanceFill_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_SOURCEROWCONSTRUCTIONFROMCORPUS_OR_ROUTEBPROVENANCEFILL_"
    "BUILT_CANDIDATE_SOURCE_ROW_VALIDATES_CONDITIONAL_UNPATCHED_OPEN"
)
NEXT = "MTT_Selected_FiniteEmissionMorphismPhiFinRestrictionProof_or_RouteBProvenanceExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    evidence = load(EVIDENCE_INDEX)
    row = load(SOURCE_ROW)
    conditional = load(CONDITIONAL_PAYLOAD)
    validator = load(VALIDATOR_RESULT)
    route_b = load(ROUTE_B_STATUS)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(evidence["same_branch_evidence_count"] >= 5, "too little source evidence")
    for item in evidence["same_branch_evidence"]:
        require((ROOT / item["source"]).exists(), f"missing evidence source: {item['source']}")

    require(row["same_branch"] is True, "source row not same branch")
    fields = row["route_A_fields_constructed"]
    for key in [
        "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "no_extra_physical_boundary_or_source_term",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
    ]:
        require(fields[key] is True, f"Route A field missing: {key}")
    require(row["derivation_boundary"]["unpatched_theorem_derived"] is False, "unpatched theorem overderived")
    require(row["closure_claimed"] is False, "row closure overclaimed")

    route_a = conditional["route_A_physical_source_certificate"]
    require(route_a["same_branch"] is True, "conditional Route A not same branch")
    require(len(route_a["attached_same_branch_sources"]) >= 5, "conditional evidence too small")
    require(conditional["conditional_source_row_used"] is True, "conditional row flag missing")
    require(conditional["unpatched_theorem_closure_claimed"] is False, "conditional overclaims unpatched theorem")
    require(validator["returncode"] == 0, "conditional strict validator should pass")
    require(any("PASS" in line for line in validator["stdout"]), "validator PASS missing")

    require(route_b["all_72_primitive_rows_executed"] is True, "primitive rows not present")
    require(route_b["formal_110_rows_executed"] is True, "formal rows not present")
    require(route_b["selected_basis_independent_of_residual_projector"] is False, "Route B basis overfilled")
    require(route_b["quadrature_rule_independent_of_locked_target"] is False, "Route B quadrature overfilled")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "Route B replay overfilled")
    require(route_b["exactness_or_error_certificates_attached"] is False, "Route B exactness overfilled")
    require(route_b["ready_now"] is False, "Route B overready")

    require(cutset["status"] == "CONDITIONAL_ROUTE_A_SOURCE_ROW_VALIDATES_UNPATCHED_PROMOTION_OPEN", "cutset status mismatch")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(data["what_closes_now"]["conditional_route_A_validator_passes"] is True, "validator pass not recorded")
    require(data["promotion_decision"]["unpatched_route_A_source_theorem_proved"] is False, "unpatched Route A overproved")
    require(data["promotion_decision"]["route_B_independent_execution_valid"] is False, "Route B overvalidated")
    require("does not claim unpatched theorem closure" in note, "note missing guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
