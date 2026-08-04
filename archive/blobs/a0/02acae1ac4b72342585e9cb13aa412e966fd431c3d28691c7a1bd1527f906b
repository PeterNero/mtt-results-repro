"""Audit final unpatched finite-C1 source identity or honest-kernel export contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_AUDIT = PACKET_DIR / "source_identity_route_audit.packet.json"
KERNEL_AUDIT = PACKET_DIR / "honest_kernel_export_route_audit.packet.json"
ROW_MANIFEST = PACKET_DIR / "honest_kernel_export_row_manifest.packet.json"
DECISION = PACKET_DIR / "final_two_route_decision.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_UnpatchedFiniteC1SourceIdentityPrinciple_or_HonestIndependentKernelExport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_UNPATCHEDFINITEC1SOURCEIDENTITY_OR_HONESTINDEPENDENTKERNELEXPORT_BUILT_FINAL_TWO_ROUTE_CONTRACT"
NEXT_ARTIFACT = "MTT_Selected_HonestKernelExport_RowSourceFill_or_SourceIdentityDerivationAttempt_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    source = load(SOURCE_AUDIT)
    kernel = load(KERNEL_AUDIT)
    manifest = load(ROW_MANIFEST)
    decision = load(DECISION)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["closure_claimed"] is False, "candidate should not claim closure")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "certificate next mismatch")

    require(source["status"] == "SOURCE_IDENTITY_CONDITIONAL_READY_UNPATCHED_NOT_DERIVED", "source route status mismatch")
    require(source["unpatched_closed_now"] is False, "source route overclosed")
    require(source["principle"]["insertion_status"]["conditional_validator_would_pass_if_inserted"] is True, "conditional source not ready")
    require(source["principle"]["insertion_status"]["current_unpatched_mtt_derivation"] is False, "source derivation overclaimed")
    require(source["theorem_gate"]["proved_now"] is False, "theorem gate overproved")
    require(source["conditional_source_id_validator"]["ok"] is True, "conditional source validator should pass")

    require(kernel["status"] == "HONEST_KERNEL_EXPORT_SCHEMA_READY_VALUES_NOT_EMITTED", "kernel route status mismatch")
    require(kernel["export_closed_now"] is False, "kernel route overclosed")
    require(kernel["strict_payload_rows_required"] == 110, "strict row count mismatch")
    require(kernel["current_template_validation"]["passes"] is False, "unfilled template should fail")
    require(kernel["current_template_validation"]["returncode"] == 1, "template validation return mismatch")

    require(manifest["status"] == "ROW_MANIFEST_BUILT_110_STRICT_ROWS_OPEN", "manifest status mismatch")
    require(manifest["strict_payload_rows"] == 110, "manifest row count mismatch")
    require(manifest["counts"] == {"hessian_source": 2, "primitive_contractions": 72, "sector_matrices": 36}, "manifest stage counts mismatch")
    require(len(manifest["basis_prerequisites"]) == 19, "basis prerequisite count mismatch")
    require(len(manifest["rows"]) == 110, "manifest rows length mismatch")
    require(all(row["status"] == "OPEN_SOURCE_VALUE_REQUIRED" for row in manifest["rows"]), "manifest row status mismatch")
    require(manifest["postcheck_oracle_not_source"]["oracle_is_not_independent_execution"] is True, "postcheck guardrail mismatch")

    require(decision["status"] == "FINAL_UNPATCHED_C1_GATE_HAS_TWO_LEGAL_ROUTES_BOTH_OPEN", "decision status mismatch")
    require(decision["previous_conditional_routeB_validates"] is True, "previous conditional pass missing")
    require(decision["source_identity_route"]["closed_now"] is False, "source route closed in decision")
    require(decision["honest_kernel_export_route"]["closed_now"] is False, "kernel route closed in decision")
    require(decision["honest_kernel_export_route"]["strict_rows_required"] == 110, "decision row count mismatch")
    require(decision["honest_kernel_export_route"]["template_validator_passes"] is False, "decision template validation mismatch")

    require(next_work["next_required_artifact"] == NEXT_ARTIFACT, "next artifact mismatch")
    require(next_work["primary"]["route"] == "HONEST_KERNEL_EXPORT", "primary route mismatch")
    require(next_work["co_primary"]["route"] == "SOURCE_IDENTITY", "co-primary route mismatch")

    closure = data["closure_decision"]
    for key in [
        "source_identity_unpatched_derived",
        "honest_kernel_export_emitted",
        "unpatched_dynamic_C1_packet_closed",
        "true_SM_equivalence_closed",
        "no_knob_closed",
    ]:
        require(closure[key] is False, f"overclosed: {key}")

    require("exact 110-row manifest" in note, "note manifest missing")
    require("postcheck-only" in note, "note postcheck guardrail missing")
    require("Superset Use" in note, "note superset missing")
    require(NEXT_ARTIFACT in note, "note next missing")

    for packet in [data, source, kernel, manifest, decision, next_work, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
