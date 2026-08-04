"""Audit PSM-C1-02 SI-1u-A selected-action derivation frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution.py"

SLUG = "selected_psm_c1_02_unpatchedselectedactionderivation_or_honestfinitec1execution"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
ACTION_SPLIT = BASE / "si1u_a_selected_action_derivation_split.packet.json"
MEASURE_IMPORT = BASE / "finite_weyl_trace_measure_sublemma_import.packet.json"
REMAINDER = BASE / "physical_action_boundary_source_remainder.packet.json"
HONEST_EXECUTION = BASE / "honest_finite_c1_execution_replacement_contract.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_UnpatchedSelectedActionDerivation_or_HonestFiniteC1Execution_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_A_MEASURE_SUBLEMMA_DERIVED_ACTION_BOUNDARY_SOURCE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_PhysicalPhiFinC1ActionRestriction_or_HonestFiniteC1Execution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "global closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    split = load(ACTION_SPLIT)
    measure = load(MEASURE_IMPORT)
    remainder = load(REMAINDER)
    honest = load(HONEST_EXECUTION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-A", "SOURCE-IDENTITY/SI-1u-B2"], "routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")

    require(split["route_label"] == "SOURCE-IDENTITY/SI-1u-A", "split route mismatch")
    require(split["closed_clause_count"] == 3, "closed clause count mismatch")
    require(split["open_clause_count"] == 2, "open clause count mismatch")
    require(split["local_principle_psm_packet_passes"] is True, "local PSM packet should pass")
    require(split["unpatched_derivation_complete_now"] is False, "split overclosed")

    require(measure["theorem_proved"] is True, "measure theorem missing")
    require(measure["measure_normalization_derived"] is True, "measure not derived")
    require(measure["finite_trace_boundary_cancellation"] is True, "algebraic boundary missing")
    require(measure["measure_part_no_longer_axiomatic"] is True, "measure still axiom")
    require(measure["not_enough_for_unpatched_source_identity"] is True, "measure overclaimed")

    require(remainder["status"] == "MINIMAL_PHYSICAL_ACTION_RESTRICTION_REMAINDER_EMITTED", "remainder status mismatch")
    require(remainder["unpatched_closed_now"] is False, "remainder overclosed")
    require(remainder["remaining_core_lemma"]["name"] == "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma", "lemma name mismatch")
    require(len(remainder["remaining_core_lemma"]["must_prove"]) == 4, "lemma obligations mismatch")
    require(remainder["route_A_current_emissions"]["physical_action_identity"] is False, "physical action overclosed")
    require(remainder["route_A_current_emissions"]["same_source_b_selected_emission"] is False, "b_selected overclosed")

    require(honest["route_label"] == "SOURCE-IDENTITY/SI-1u-B2", "honest route mismatch")
    require(len(honest["must_emit"]) == 5, "honest execution contract incomplete")

    closes = candidate["what_closes_now"]
    require(closes["SI1u_A_measure_normalization_sublemma_derived"] is True, "measure close missing")
    require(closes["finite_trace_frobenius_pairing_not_free_knob"] is True, "knob guard missing")
    require(closes["physical_action_remainder_minimized"] is True, "remainder not minimized")

    remains = candidate["what_remains_open"]
    require(remains["SI1u_A1_physical_PhiFinC1_finite_quotient_restriction"] is True, "A1 not open")
    require(remains["no_extra_physical_boundary_or_source_term"] is True, "boundary not open")
    require(remains["pre_residual_R_Z_R_X_source_emission"] is True, "R source not open")
    require(remains["same_source_b_selected_second_variation"] is True, "b source not open")
    require(remains["unpatched_SelectedFiniteC1SourceIdentityTheorem"] is True, "unpatched theorem not open")

    decision = candidate["closure_decision"]
    require(decision["measure_sublemma_derived"] is True, "decision measure missing")
    require(decision["unpatched_action_derivation_complete"] is False, "decision overclosed")
    require(decision["honest_finite_c1_execution_closed"] is False, "honest execution overclosed")
    require(decision["global_closure_claimed"] is False, "global closure overclaimed")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1", "next primary mismatch")
    require(next_work["replacement"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "replacement mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["measure_sublemma_derived"] is True, "cert measure missing")
    require(cert["unpatched_action_derivation_complete"] is False, "cert overclosed")
    require(cert["honest_finite_c1_execution_closed"] is False, "cert honest overclosed")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A`" in note, "note label missing")
    require("no longer one opaque patch" in note, "note progress missing")
    require("not knobs" in note, "note superset guard missing")
    require("SI-1u-A1" in note, "note next label missing")

    for item in [candidate, split, measure, remainder, honest, cert]:
        guard(item)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
