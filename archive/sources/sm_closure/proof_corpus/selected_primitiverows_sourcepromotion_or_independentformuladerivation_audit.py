"""Audit primitive-row source promotion or independent-formula derivation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_primitiverows_sourcepromotion_or_independentformuladerivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SUPPORT = PACKET_DIR / "primitive_source_support_matrix.packet.json"
CONDITIONAL_PAYLOAD = PACKET_DIR / "conditional_primitive_formula_rowsource_payload.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "conditional_primitive_formula_rowsource_validator_result.packet.json"
CUTSET = PACKET_DIR / "primitive_source_replay_independence_cutset.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveRows_SourcePromotion_or_IndependentFormulaDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PRIMITIVEROWS_SOURCEPROMOTION_OR_INDEPENDENTFORMULADERIVATION_BUILT_FORMULA_CONDITIONAL_REPLAY_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PrimitiveRows_ReplayIndependenceLemma_or_SourceIdentityBackfill_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    support = load(SUPPORT)
    payload = load(CONDITIONAL_PAYLOAD)
    result = load(CONDITIONAL_RESULT)
    cutset = load(CUTSET)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["closure_claimed"] is False, "candidate should not claim closure")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")

    require(support["status"] == "PRIMITIVE_FORMULA_TRACE_VALUES_READY_SOURCE_INDEPENDENCE_OPEN", "support status mismatch")
    for key, value in support["closed_support"].items():
        require(value is True, f"closed support false: {key}")
    require(support["open_source_clauses"]["provenance_independent_of_residual_projector_replay"] is False, "provenance overclosed")
    require(support["open_source_clauses"]["no_residual_projector_replay_used_as_source"] is False, "replay overclosed")

    for key in [
        "selected_basis_feeds_72_primitive_rows",
        "finite_weyl_trace_rule_feeds_all_rows",
        "sector_rows_assembled_from_primitive_rows",
        "hessian_source_rows_assembled_from_same_rows",
        "no_locked_target_values_used_as_source",
        "row_formula_source_theorem_derived",
    ]:
        require(payload[key] is True, f"conditional payload field false: {key}")
    require(payload["no_residual_projector_replay_used_as_source"] is False, "payload replay overclosed")
    require(payload["source_independent_of_residual_projector_replay"] is False, "payload source independence overclosed")
    require(len(payload["attached_source_evidence"]) >= 4, "evidence count low")

    require(result["passes"] is False, "conditional row-source payload should fail")
    require(result["returncode"] == 1, "validator return mismatch")
    require(any("no_residual_projector_replay_used_as_source" in line for line in result["stderr_lines"]), "missing replay-source failure")
    require(any("source_independent_of_residual_projector_replay is not true" in line for line in result["stderr_lines"]), "missing source-independence failure")

    require(cutset["status"] == "PRIMITIVE_SOURCE_PROMOTION_REDUCED_TO_REPLAY_INDEPENDENCE_OR_SOURCE_IDENTITY", "cutset status mismatch")
    require(cutset["conditional_formula_source_closes_all_but_replay_independence"] is True, "cutset compression missing")
    require(cutset["remaining_strict_failures"] == ["no_residual_projector_replay_used_as_source", "source_independent_of_residual_projector_replay"], "remaining failures mismatch")
    require(len(cutset["legal_closure_routes"]) == 3, "closure route count mismatch")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(next_work["primary"]["route"] == "primitive_replay_independence_lemma", "primary route mismatch")
    require(next_work["co_primary"]["route"] == "source_identity_backfill", "co-primary route mismatch")

    closure = data["closure_decision"]
    require(closure["primitive_formula_source_promoted_conditionally"] is True, "conditional formula missing")
    for key in [
        "row_source_validator_passes",
        "primitive_rows_closed_unpatched",
        "unpatched_dynamic_C1_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require("fails only on replay independence" in note, "note replay cutset missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    for packet in [data, support, payload, result, cutset, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
