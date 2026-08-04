"""Audit dynamic C1 parity value packet after stationary/dotD integration."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicc1parityvaluepacket_after_stationarydotd_integration"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VALUE_PACKET = PACKET_DIR / "patched_dynamic_c1_parity_value_packet.packet.json"
GUARDRAIL = PACKET_DIR / "parity_patch_vs_unpatched_guardrail.packet.json"
REMAINDER = PACKET_DIR / "unpatched_dynamic_c1_remainder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicC1ParityValuePacket_after_StationaryDotD_Integration_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_dynamicc1parityvaluepacket_after_stationarydotd_integration.py"

STATUS = "MTT_SELECTED_DYNAMICC1_PARITY_VALUEPACKET_AFTER_STATIONARYDOTD_BUILT_PATCHED_VALUES_UNPATCHED_OPEN"
NEXT = "MTT_Selected_UnpatchedFiniteC1TraceMeasureDerivation_or_TrueEquivalenceSourceUpgrade_v1"


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
    value = load(VALUE_PACKET)
    guardrail = load(GUARDRAIL)
    remainder = load(REMAINDER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["patched"] is True, "theorem patch flag missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["patched"] is True, "certificate patch flag missing")
    require("not an unpatched no-knob derivation" in note, "note misses guardrail")

    prereq = value["stationary_and_dotd_prerequisites"]
    for key in [
        "stationary_projector_source_verified",
        "validator_ready_stationary_rho_s",
        "selected_dotD_source_verified",
        "alpha1_driver_verified",
    ]:
        require(prereq[key] is True, f"stationary/dotD prerequisite missing: {key}")

    require(value["patch_used"] == "SelectedFiniteC1TraceMeasurePrinciple", "wrong patch used")
    require(value["formal_row_counts"]["primitive_rows"] == 72, "primitive row count mismatch")
    require(value["formal_row_counts"]["hessian_source_rows"] == 2, "hessian row count mismatch")
    require(value["formal_row_counts"]["sector_matrix_rows"] == 36, "sector row count mismatch")
    require(value["formal_row_counts"]["total_rows"] == 110, "total row count mismatch")

    patched = value["patched_values"]
    require(patched["A_selected_parity_tier"] == [[12.0, 0.0], [0.0, 12.0]], "A mismatch")
    require(patched["b_selected_parity_tier"] == [12.0, 12.0], "b mismatch")
    require(patched["deltaTheta_C1_parity_tier"] == [1.0, 1.0], "deltaTheta mismatch")
    require(patched["sector_response_matrices_parity_tier"] is True, "sector matrices missing")
    require(patched["row_comparison_max_abs_error"] < 1e-12, "row comparison too large")

    checks = value["patched_replay_checks"]
    for key in [
        "selected_Galerkin_replacement_promotes_formal_rows",
        "physical_measure_equals_finite_trace_quadrature",
        "Route_B_physical_Galerkin_replacement_closed",
        "patched_dynamic_C1_packet_closed",
    ]:
        require(checks[key] is True, f"patched replay check missing: {key}")

    tier = value["tier_classification"]
    require(tier["SM_parity_patched_dynamic_C1_value_packet_available"] is True, "patched parity tier missing")
    require(tier["unpatched_dynamic_C1_packet_closed"] is False, "unpatched closure overclaimed")
    require(tier["true_SM_equivalence_closed"] is False, "true SM equivalence overclaimed")
    require(tier["no_knob_closed"] is False, "no-knob overclaimed")

    strategy = guardrail["superset_strategy"]
    require(strategy["combining_paths"] is True, "superset combination not recorded")
    require(strategy["using_one_straight_way"] is False, "single-path strategy overclaimed")
    require("not unpatched no-knob derivation" in strategy["locked_target"], "locked target wrong")
    require(guardrail["ledger_alignment"]["patched_dynamic_C1_no_longer_blocks_SM_parity"] is True, "ledger not aligned")
    require(guardrail["ledger_alignment"]["patched_dynamic_C1_empirical_interface_ready"] is True, "empirical interface not ready")
    require(guardrail["ledger_alignment"]["full_SM_parity_closed"] is False, "full parity overclaimed")
    require(guardrail["ledger_alignment"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    for forbidden in [
        "the SelectedFiniteC1TraceMeasurePrinciple is derived from prior MTT axioms",
        "unpatched dynamic C1 no-knob closure is proved",
        "true SM equivalence is closed",
        "observed flavor, mass, CKM, PMNS, or Higgs values selected the source",
    ]:
        require(forbidden in guardrail["forbidden_claims"], f"forbidden claim missing: {forbidden}")

    blockers = remainder["unpatched_blockers"]
    for key in [
        "direct_PhiFinC1_action_derivation",
        "physical_measure_identity",
        "SelectedFiniteC1TraceMeasurePrinciple_derivation",
        "Route_A_same_source_emission",
        "Route_B_physical_Galerkin_replacement_without_patch",
    ]:
        require(blockers[key] is True, f"unpatched blocker missing: {key}")

    closure = data["closure_decision"]
    require(closure["SM_parity_patched_dynamic_C1_value_packet_available"] is True, "patched packet unavailable")
    require(closure["patched_A_selected_emitted"] is True, "patched A not emitted")
    require(closure["patched_b_selected_emitted"] is True, "patched b not emitted")
    require(closure["patched_deltaTheta_C1_emitted"] is True, "patched delta not emitted")
    require(closure["patched_sector_response_matrices_available"] is True, "patched sector matrices not emitted")
    require(closure["unpatched_A_selected_emitted"] is False, "unpatched A overclaimed")
    require(closure["unpatched_b_selected_emitted"] is False, "unpatched b overclaimed")
    require(closure["unpatched_dynamic_C1_packet_closed"] is False, "unpatched closure overclaimed")
    require(closure["full_SM_parity_closed"] is False, "full parity overclaimed")
    require(closure["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(closure["no_knob_closed"] is False, "no-knob overclaimed")

    for label, payload in [
        ("candidate", data),
        ("value", value),
        ("guardrail", guardrail),
        ("remainder", remainder),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
