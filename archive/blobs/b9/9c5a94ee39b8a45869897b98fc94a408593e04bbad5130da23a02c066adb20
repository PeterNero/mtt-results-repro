"""Audit qualitative SM closure ledger after the selected second-order orbit packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_secondorderorbitqualitativesmclosure_or_rthetascalarvalues"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
QUAL_LEDGER = PACKET_DIR / "qualitative_sm_orbit_closure_ledger.packet.json"
SCALAR_OBLIGATION = PACKET_DIR / "rtheta_scalar_value_obligation.packet.json"
LEGACY_QUARANTINE = PACKET_DIR / "legacy_value_replay_quarantine.packet.json"
NO_KNOB = PACKET_DIR / "no_knob_status_after_qualitative_closure.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_qualitative_sm_orbit_closure.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SecondOrderOrbitQualitativeSMClosure_or_RThetaScalarValues_v1.md"

STATUS = (
    "MTT_SELECTED_SECONDORDERORBITQUALITATIVESMCLOSURE_OR_RTHETASCALARVALUES_"
    "BUILT_QUALITATIVE_SM_ORBIT_CLOSURE_SCALAR_VALUES_OPEN"
)
NEXT = "MTT_Selected_RThetaScalarValueFunctionalSource_or_NoKnobNumericalRows_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def expect(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def guard(packet: dict[str, Any], errors: list[str], label: str, *, closure: bool = False) -> None:
    expect(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation", errors)
    expect(packet.get("target_fitting_used") is False, f"{label} target fitting violation", errors)
    expect(packet.get("closure_claimed") is closure, f"{label} closure flag mismatch", errors)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    qual = load(QUAL_LEDGER)
    obligation = load(SCALAR_OBLIGATION)
    quarantine = load(LEGACY_QUARANTINE)
    no_knob = load(NO_KNOB)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")
    errors: list[str] = []

    expect(data.get("status") == STATUS, "candidate status mismatch", errors)
    expect(cert.get("status") == STATUS, "certificate status mismatch", errors)
    expect(data.get("next_required_artifact") == NEXT, "candidate next mismatch", errors)
    expect(cert.get("next_required_artifact") == NEXT, "certificate next mismatch", errors)
    expect(data.get("theorem", {}).get("proved") is True, "theorem should be proved", errors)
    expect(cert.get("theorem_proved") is True, "certificate theorem should be proved", errors)

    guard(data, errors, "candidate", closure=False)
    guard(cert, errors, "certificate", closure=False)
    guard(qual, errors, "qualitative ledger", closure=True)
    guard(obligation, errors, "scalar obligation", closure=False)
    guard(quarantine, errors, "legacy quarantine", closure=False)
    guard(no_knob, errors, "no-knob status", closure=False)
    guard(cutset, errors, "cutset", closure=False)

    features = qual.get("qualitative_features_closed", {})
    for key in [
        "three_generations",
        "family_splitting",
        "first_response_twofold_degeneracy_removed",
        "nonzero_CP_odd_structure",
        "positive_CP_orientation_on_selected_same_lambda_orbit",
        "conjugate_lambda_orbit_retained",
    ]:
        expect(features.get(key) is True, f"qualitative feature missing: {key}", errors)
    expect(qual.get("qualitative_invariants", {}).get("hermitian_spectrum_each_sector") == [1.0, 4.0, 7.0], "qualitative spectrum mismatch", errors)
    expect(qual.get("qualitative_invariants", {}).get("cp_odd_exact_magnitude") == "972*sqrt(3)", "CP magnitude mismatch", errors)
    expect(qual.get("qualitative_invariants", {}).get("commutator_norm_sq") == 324.0, "commutator norm mismatch", errors)
    expect("true numerical SM equivalence" in qual.get("scope", {}).get("does_not_prove", []), "scope overclaims numerical equivalence", errors)

    expect(obligation.get("codomain_scalar_row_count") == 10, "scalar row count mismatch", errors)
    expect(len(obligation.get("missing_value_rows", [])) == 10, "missing value row list mismatch", errors)
    expect(obligation.get("execution_inputs_available_now") is False, "execution inputs overclaimed", errors)
    expect(obligation.get("selected_functional_executed") is False, "functional overexecuted", errors)
    expect(obligation.get("accepted_scalar_row_count_now") == 0, "scalar row count overaccepted", errors)
    inventory = obligation.get("domain_inventory_now", {})
    for key in [
        "selected_finite_Hessian_C1_source_blocks",
        "primitive_C1_contractions_and_sector_response_matrices",
    ]:
        expect("absent" in inventory.get(key, ""), f"missing absent domain marker: {key}", errors)

    expect(quarantine.get("imported_or_empirical_value_artifacts_present") is True, "legacy artifacts should be detected", errors)
    expect(quarantine.get("usable_for_current_no_knob_proof") is False, "legacy artifacts overused", errors)
    expect("backfilling missing Rtheta rows" in quarantine.get("disallowed_use", []), "quarantine disallowed use missing", errors)

    expect(no_knob.get("knobs_used_for_qualitative_orbit_closure") == 0, "qualitative knob count mismatch", errors)
    expect(no_knob.get("qualitative_orbit_closure_no_knob") is True, "qualitative no-knob should close", errors)
    expect(no_knob.get("numerical_scalar_value_closure_no_knob") is False, "numerical no-knob overclosed", errors)

    closed = cutset.get("closed_now", {})
    for key in [
        "qualitative_SM_orbit_closure",
        "three_generation_family_splitting",
        "nonzero_CP_odd_structure",
        "legacy_value_replay_quarantined",
        "scalar_value_obligation_fully_typed",
    ]:
        expect(closed.get(key) is True, f"cutset close missing: {key}", errors)
    remains = cutset.get("still_open", {})
    for key in [
        "selected_Rtheta_value_functional_source",
        "finite_Hessian_C1_source_blocks_for_values",
        "primitive_C1_contractions_sector_response_matrices_for_values",
        "ten_Rtheta_scalar_rows",
        "Yukawa_CKM_PMNS_lambdaH_threshold_values",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        expect(remains.get(key) is True, f"remaining blocker missing: {key}", errors)
    expect(cutset.get("recommended_next", {}).get("artifact") == NEXT, "cutset next mismatch", errors)

    decision = data.get("closure_decision", {})
    for key in [
        "qualitative_SM_orbit_closure_closed",
        "scalar_value_obligation_typed",
        "legacy_value_replay_quarantined",
    ]:
        expect(decision.get(key) is True, f"decision close missing: {key}", errors)
        expect(cert.get(key) is True, f"certificate close missing: {key}", errors)
    for key in [
        "selected_Rtheta_scalar_rows_emitted",
        "accepted_value_layer_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        expect(decision.get(key) is False, f"decision overclosed: {key}", errors)
        expect(cert.get(key) is False, f"certificate overclosed: {key}", errors)

    expect("three-generation splitting     : true" in note, "note missing qualitative close", errors)
    expect("ten scalar value rows emitted  : false" in note, "note missing scalar-open guard", errors)

    if errors:
        print("Second-order qualitative SM closure audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Second-order qualitative SM closure audit passed")
    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
