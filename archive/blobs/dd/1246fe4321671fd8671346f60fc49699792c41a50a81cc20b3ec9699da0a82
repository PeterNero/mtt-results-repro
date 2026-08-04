"""Audit finite Weyl trace uniqueness / physical boundary-source derivation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TRACE_UNIQUENESS = PACKET_DIR / "finite_weyl_trace_uniqueness_derivation.packet.json"
PRINCIPLE_SPLIT = PACKET_DIR / "finite_c1_trace_measure_principle_split.packet.json"
BOUNDARY_SOURCE = PACKET_DIR / "physical_boundary_source_remainder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteWeylTraceUniqueness_or_PhysicalBoundarySource_Derivation_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation.py"

STATUS = "MTT_SELECTED_FINITEWEYL_TRACEUNIQUENESS_BUILT_MEASURE_DERIVED_BOUNDARY_SOURCE_OPEN"
NEXT = "MTT_Selected_PhysicalPhiFinC1ActionRestriction_or_NoExtraBoundarySource_ValueEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    trace = load(TRACE_UNIQUENESS)
    split = load(PRINCIPLE_SPLIT)
    boundary = load(BOUNDARY_SOURCE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("not a new knob" in note, "note misses no-knob measure statement")
    require("physical binding clause" in note, "note misses remaining physical clause")

    algebra = trace["finite_algebra"]
    require(algebra["generators"] == ["Z/clock", "X/shift"], "Weyl generators mismatch")
    require(algebra["commutant"] == "scalar multiples of identity", "commutant mismatch")
    require(algebra["invariant_functional"] == "tau(A)=Tr(A)/3 per qutrit block", "trace law mismatch")
    require(len(trace["derivation_steps"]) == 5, "derivation step count mismatch")

    derived = trace["derived_now"]
    require(derived["finite_measure_equals_normalized_trace"] is True, "finite trace not derived")
    require(derived["trace_frobenius_pairing_for_finite_quotient"] is True, "Frobenius pairing not derived")
    require(derived["measure_choice_is_not_a_new_knob"] is True, "measure still treated as knob")
    require(derived["measured_data_used"] is False, "measured data used")

    not_derived = trace["not_derived_now"]
    for key in [
        "physical_PhiFinC1_action_restricts_to_finite_quotient",
        "no_extra_physical_boundary_or_source_term",
        "same_source_b_selected_emission",
        "unpatched_dynamic_C1_packet_closed",
    ]:
        require(not_derived[key] is True, f"unclosed clause missing: {key}")

    clauses = split["clauses"]
    require(clauses["finite_selected_C1_quotient"]["closed"] is True, "finite quotient not closed")
    require(
        clauses["admissible_variations_represented_by_selected_qutrit_Weyl_response_algebra"]["closed"] is True,
        "Weyl response variations not closed",
    )
    require(
        clauses["physical_first_variation_uses_normalized_trace_Frobenius_measure"]["closed"] is True,
        "measure clause not closed",
    )
    require(
        clauses["physical_PhiFinC1_action_restricts_exactly_to_this_finite_measure"]["closed"] is False,
        "action restriction overclosed",
    )
    require(
        clauses["continuum_or_external_boundary_source_terms_absent"]["closed"] is False,
        "boundary/source overclosed",
    )

    improved = split["what_this_improves"]
    require(improved["patch_measure_part_no_longer_axiomatic"] is True, "measure part still axiomatic")
    require(improved["remaining_patch_gap_is_not_measure_normalization"] is True, "wrong remaining gap")
    require(
        improved["remaining_patch_gap_is_physical_action_boundary_source_binding"] is True,
        "physical binding not isolated",
    )

    support = boundary["imported_support"]
    require(support["selected_trace_map_support_imported"] is True, "trace map support missing")
    require(support["dynamic_trace_binding_imported"] is True, "dynamic trace binding missing")
    require(support["finite_trace_boundary_cancellation"] is True, "finite boundary cancellation missing")
    require(support["patched_dynamic_C1_values_available"] is True, "patched values missing")

    for key in [
        "physical_PhiFinC1_action_identity",
        "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "no_extra_physical_boundary_or_source_term",
        "same_source_b_selected_emission",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
    ]:
        require(key in boundary["minimal_next_emissions"], f"minimal emission missing: {key}")

    closure = data["closure_decision"]
    require(closure["measure_normalization_derived"] is True, "measure normalization not closed")
    require(closure["SelectedFiniteC1TraceMeasurePrinciple_fully_derived"] is False, "principle overderived")
    require(closure["unpatched_A_selected_emitted"] is False, "unpatched A overclaimed")
    require(closure["unpatched_b_selected_emitted"] is False, "unpatched b overclaimed")
    require(closure["unpatched_deltaTheta_C1_emitted"] is False, "unpatched delta overclaimed")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "unpatched closure overclaimed")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclaimed")
    require(closure["no_knob_closed"] is False, "no-knob overclaimed")

    for label, payload in [
        ("candidate", data),
        ("trace", trace),
        ("split", split),
        ("boundary", boundary),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
