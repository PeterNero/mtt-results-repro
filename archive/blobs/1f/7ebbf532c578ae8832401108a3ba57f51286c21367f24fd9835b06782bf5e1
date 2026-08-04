"""Audit same-source Phi_fin^C1 emission or independent rows actual-fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_samesourcephifinc1emission_or_independentrowsactualfill"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ATTEMPT = PACKET_DIR / "strongest_legal_two_lane_actual_fill.packet.json"
VALIDATION = PACKET_DIR / "strict_two_lane_validator_result.packet.json"
CUTSET = PACKET_DIR / "remaining_source_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameSourcePhiFinC1Emission_or_IndependentRowsActualFill_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCE_PHIFINC1_OR_INDEPENDENTROWS_ACTUALFILL_BUILT_SOURCE_FIELDS_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    attempt = load(ATTEMPT)
    validation = load(VALIDATION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "unexpected candidate status")
    require(cert["status"] == STATUS, "unexpected certificate status")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["target_fitting_used"] is False, "candidate uses target fitting")
    require(candidate["observed_data_used_as_selector"] is False, "candidate uses observed selector")
    require(attempt["locked_target_values_used_as_source"] is False, "locked targets used as source")
    require(attempt["target_fitting_used"] is False, "attempt uses target fitting")
    require(validation["ok"] is False, "validator should still reject current support")
    require(validation["exit_code"] == 1, "validator exit code should be 1")
    require(
        any("neither narrowed Route A nor narrowed Route B validates" in line for line in validation["stderr"]),
        "expected strict two-lane rejection missing",
    )
    require(cutset["validator_ok"] is False, "cutset should record validator rejection")
    require(
        "physical_phifin_c1_action_emitted" in cutset["route_A_missing_true_fields"],
        "Route A physical action field should remain open",
    )
    require(
        "same_source_b_selected_emitted" in cutset["route_A_missing_true_fields"],
        "Route A b_selected field should remain open",
    )
    require(
        "source_independent_of_residual_projector_replay" in cutset["route_B_missing_true_fields"],
        "Route B residual replay independence should remain open",
    )
    require(
        "selected_b_vector_source" in cutset["route_B_missing_true_fields"],
        "Route B b-source should remain open",
    )
    require(cutset["formal_support_closed"]["trace_assembly_subclaim"] is True, "trace assembly lost")
    require(cutset["formal_support_closed"]["all_rows_formal_replay"] is True, "formal rows lost")
    require("strict validator still rejects" in note, "note should record strict rejection")
    require("not a value search" in note, "note should record source nature of blocker")

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
