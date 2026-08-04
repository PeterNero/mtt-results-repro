"""Audit universal_alpha1_frontier_handoff_import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "universal_alpha1_frontier_handoff_import"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
IMPORT = BASE / "alpha1_frontier_handoff_import.packet.json"
POLICY_UPDATE = BASE / "universal_parameter_policy_update.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_UniversalAlpha1FrontierHandoffImport_v1.md"
BUILD = ROOT / "scripts" / "build_universal_alpha1_frontier_handoff_import.py"
STATUS = "MTT_UNIVERSAL_ALPHA1_FRONTIER_HANDOFF_IMPORTED_ONE_PRIMITIVE_READY"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    imported = load(IMPORT)
    policy_update = load(POLICY_UPDATE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["selected_parameter_count_now"] == 0, "parameter overselected")
    require(candidate["imported_one_universal_primitive_ready"] is True, "primitive import missing")
    require(candidate["what_remains_open"]["unpatched_PSM_C1_02_closure"] is True, "PSM overclosed")
    require(imported["source_claims"]["strict_current_corpus_nogo"] is True, "strict no-go missing")
    require(imported["source_claims"]["strict_no_knob_alpha_phys_closed"] is False, "strict alpha overclosed")
    require(imported["source_claims"]["one_universal_primitive_extension_ready"] is True, "one primitive not ready")
    require(abs(imported["values_to_carry"]["tau_int"] - 0.40698621549433234) < 1e-15, "tau mismatch")
    require(policy_update["mapped_universal_parameter_class"] == "UP-ABS-SCALE", "class mapping mismatch")
    require(policy_update["what_this_does_not_close"]["PSM_C1_02_unpatched_source_identity"] is True, "policy overclosed PSM")
    require(next_work["primary"]["label"] == "UNIV-PARAM / SOURCE-ANCHOR / UP-1-ALPHA1", "next label mismatch")
    require(cert["selected_parameter_count_now"] == 0, "cert parameter overselected")
    require("does not select a universal parameter" in note, "note guard missing")

    for packet in [candidate, imported, policy_update, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
