"""Audit first honest-kernel row-source fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_honestkernelexport_rowsourcefill_or_sourceidentityderivationattempt"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRIMITIVE_ATTEMPT = PACKET_DIR / "primitive_stage_postcheck_fill_attempt.packet.json"
PRIMITIVE_VALIDATION = PACKET_DIR / "primitive_stage_postcheck_fill_validator_result.packet.json"
SOURCE_IDENTITY = PACKET_DIR / "source_identity_derivation_attempt_status.packet.json"
ROW_PROGRESS = PACKET_DIR / "row_source_fill_progress_ledger.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HonestKernelExport_RowSourceFill_or_SourceIdentityDerivationAttempt_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HONESTKERNELEXPORT_ROWSOURCEFILL_OR_SOURCEIDENTITYDERIVATIONATTEMPT_BUILT_PRIMITIVE_POSTCHECK_FILLED_SOURCE_OPEN"
NEXT_ARTIFACT = "MTT_Selected_PrimitiveRows_SourcePromotion_or_IndependentFormulaDerivation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    attempt = load(PRIMITIVE_ATTEMPT)
    validation = load(PRIMITIVE_VALIDATION)
    source_identity = load(SOURCE_IDENTITY)
    progress = load(ROW_PROGRESS)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["closure_claimed"] is False, "candidate should not claim closure")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")

    require(attempt["status"] == "PRIMITIVE_72_VALUES_FILLED_AS_POSTCHECK_SOURCE_PROVENANCE_OPEN", "attempt status mismatch")
    require(attempt["primitive_rows_filled_with_postcheck_values"] == 72, "primitive fill count mismatch")
    require(attempt["strict_rows_total"] == 110, "strict row total mismatch")
    require(attempt["source_promotion"]["primitive_independent_source_emitted"] is False, "primitive source overclosed")
    require(attempt["source_promotion"]["provenance_independent_of_residual_projector_replay"] is False, "provenance overclosed")
    primitive_rows = [row for row in attempt["rows"] if row["stage"] == "primitive_contractions"]
    require(len(primitive_rows) == 72, "primitive row length mismatch")
    require(all(row["value"] is not None for row in primitive_rows), "primitive value missing")
    require(all(row["independent_source_emitted"] is False for row in primitive_rows), "primitive independent source overclosed")
    require(all(row["residual_replay_dependency"] is True for row in primitive_rows), "primitive replay guardrail missing")

    require(validation["passes"] is False, "validator should fail")
    require(validation["returncode"] == 1, "validator return mismatch")
    require(any("independent_source_emitted must be true" in line for line in validation["stderr_lines"]), "expected independent-source failure missing")
    require(any("residual_replay_dependency must be false" in line for line in validation["stderr_lines"]), "expected replay failure missing")

    require(source_identity["proved_now"] is False, "source identity overproved")
    require(source_identity["route_A_accepts"] is False, "Route A overaccepted")
    require(source_identity["route_B_accepts"] is False, "Route B overaccepted")
    require(len(source_identity["open_clauses"]) >= 1, "source identity open clauses missing")

    require(progress["status"] == "PRIMITIVE_VALUES_AVAILABLE_SOURCE_FLAGS_OPEN", "progress status mismatch")
    require(progress["postcheck_value_progress"]["primitive_contractions"]["values_available"] == 72, "progress primitive values mismatch")
    require(progress["postcheck_value_progress"]["primitive_contractions"]["independent_source_rows_closed"] == 0, "progress source overclosed")
    require(progress["validator_passes"] is False, "progress validator mismatch")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(next_work["primary"]["route"] == "HONEST_KERNEL_EXPORT", "primary route mismatch")
    require(next_work["co_primary"]["route"] == "SOURCE_IDENTITY", "co-primary route mismatch")

    closure = data["closure_decision"]
    for key in [
        "honest_kernel_export_validates",
        "primitive_source_rows_closed",
        "source_identity_unpatched_derived",
        "unpatched_dynamic_C1_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require("Loaded all 72 primitive row values as postcheck values" in note, "note primitive fill missing")
    require("strict honest-kernel validator still fails" in note, "note validator failure missing")
    require("not proof of source provenance" in note, "note provenance guardrail missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    for packet in [data, attempt, validation, source_identity, progress, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
