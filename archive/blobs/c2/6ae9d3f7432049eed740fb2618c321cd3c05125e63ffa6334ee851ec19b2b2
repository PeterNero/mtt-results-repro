"""Audit value-source derivation obligation kernel or external threshold import manifest."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
KERNEL = PACKET_DIR / "value_source_derivation_obligation_kernel.packet.json"
IMPORT_MANIFEST = PACKET_DIR / "external_threshold_import_manifest.packet.json"
SUPPORT_MATRIX = PACKET_DIR / "support_to_obligation_mapping.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_obligation_kernel.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_obligation_kernel.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ValueSourceDerivationObligationKernel_or_ExternalThresholdImportManifest_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_VALUESOURCEDERIVATIONOBLIGATIONKERNEL_OR_EXTERNALTHRESHOLDIMPORTMANIFEST_"
    "BUILT_KERNEL_AND_IMPORT_MANIFEST_VALUES_OPEN"
)
NEXT = "MTT_Selected_FirstValueSourceRowFill_or_ExternalThresholdSourceImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    kernel = load(KERNEL)
    import_manifest = load(IMPORT_MANIFEST)
    support = load(SUPPORT_MATRIX)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(kernel["required_row_count"] == 5, "required row count mismatch")
    require(kernel["closed_row_count"] == 0, "obligations overclosed")
    require(kernel["closure_claimed"] is False, "kernel overclaimed closure")
    require(kernel["first_attack_order"][0] == "VSD-01-selected-overlap-value-kernel", "first target mismatch")
    for row in kernel["required_rows"]:
        require(row["closed"] is False, f"required row overclosed: {row['id']}")
        require(row["required_payload"], f"required payload missing: {row['id']}")

    required_manifest_keys = ["source", "basis", "threshold_rows", "mass_scheme_rows", "profile_rows", "guardrails"]
    for key in required_manifest_keys:
        require(key in import_manifest["manifest_required_fields"], f"manifest key missing: {key}")
    require(import_manifest["accepted_external_rows_present"] is False, "external rows overimported")
    require(import_manifest["closure_claimed"] is False, "import manifest overclaimed")

    require(support["all_support_rows_have_paths"] is True, "support paths missing")
    require(support["any_obligation_closed_by_support"] is False, "support overclosed obligation")
    for row in support["support_rows"]:
        require(row["supports_obligations"], f"support row not mapped: {row['support_id']}")
        require(row["closes_obligations"] == [], f"support closes obligation unexpectedly: {row['support_id']}")

    tests = promotion["promotion_tests"]
    require(tests["obligation_kernel_built"] is True, "kernel not built")
    require(tests["external_import_manifest_built"] is True, "manifest not built")
    require(tests["support_to_obligation_mapping_built"] is True, "support mapping not built")
    for key in [
        "selected_dynamic_value_source_rows_emitted",
        "accepted_external_threshold_rows_imported",
        "no_knob_value_derivation_closed",
    ]:
        require(tests[key] is False, f"promotion overclosed {key}")
        require(key in promotion["remaining_hard_failures"], f"hard failure missing: {key}")
    require(tests["true_SM_equivalence_closed"] is False, "true equivalence overclosed")

    decision = promotion["promotion_decision"]
    require(decision["obligation_kernel_closed"] is True, "kernel closure decision missing")
    require(decision["import_manifest_closed"] is True, "manifest closure decision missing")
    require(decision["accepted_for_true_precision_equivalence"] is False, "true precision overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(promotion["closure_claimed"] is False, "promotion overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    require(data["closure_decision"]["obligation_kernel_closed"] is True, "candidate kernel not closed")
    require(data["closure_decision"]["import_manifest_closed"] is True, "candidate manifest not closed")
    require(data["closure_decision"]["selected_dynamic_value_source_rows_emitted"] is False, "candidate value rows overemitted")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require("closed rows   = 0" in note, "note missing zero-closed-row guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
