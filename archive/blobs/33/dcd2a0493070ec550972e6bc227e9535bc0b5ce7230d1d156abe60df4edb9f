"""Audit selected PhiFin C1 physical variation source theorem proof attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinc1_physicalvariation_sourcetheorem_proof_attempt_or_countermodel"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SUPPORT = PACKET_DIR / "support_closure_synthesis.packet.json"
ATTEMPT = PACKET_DIR / "selected_phifinc1_physicalvariation_theorem_attempt.packet.json"
COUNTERMODEL = PACKET_DIR / "closed_support_countermodel_lift.packet.json"
DECISION = PACKET_DIR / "proof_attempt_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1_PhysicalVariationSourceTheorem_ProofAttempt_or_Countermodel_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHIFINC1_PHYSICALVARIATION_SOURCETHEOREM_PROOF_ATTEMPT_COUNTERMODEL_OPEN"
NEXT = "MTT_Selected_PreResidualVariationOperator_and_HessianSourceKernel_Emission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    support = load(SUPPORT)
    attempt = load(ATTEMPT)
    countermodel = load(COUNTERMODEL)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")

    require(support["status"] == "MAXIMAL_CLOSED_SUPPORT_SYNTHESIZED_FOR_THEOREM_ATTEMPT", "support status mismatch")
    require(support["all_support_flags_closed"] is True, "not all support flags closed")
    require(support["support_is_sufficient_for_theorem"] is False, "support sufficiency overclaimed")
    for key, value in support["closed_support"].items():
        require(value is True, f"closed support flag false: {key}")

    require(attempt["status"] == "THEOREM_ATTEMPT_REJECTED_SOURCE_KERNEL_STILL_OPEN", "attempt status mismatch")
    require(attempt["theorem_proved_now"] is False, "theorem overproved")
    require(attempt["conditional_witness_would_validate"] is True, "conditional witness should validate")
    require(attempt["new_source_kernel_found_now"] is False, "new source kernel overclaimed")

    fields = attempt["theorem_fields"]
    require(fields["same_branch"] is True, "same branch should hold")
    for key in [
        "physical_action_equals_c1_defect_functional",
        "admissible_differentiated_variations_fixed",
        "physical_measure_equals_trace_frobenius_pairing",
        "physical_first_variation_identity",
        "selected_PhiFinC1_applies_Q_residual",
        "same_source_RZ_RX_bselected_emission",
        "physical_boundary_source_terms_vanish",
    ]:
        require(fields[key] is False, f"field unexpectedly promoted: {key}")
    for key, value in attempt["conditional_theorem_fields"].items():
        require(value is True, f"conditional field false: {key}")
    for key, value in attempt["current_route_A_emissions"].items():
        require(value is False, f"current Route A emission unexpectedly true: {key}")

    require(
        countermodel["status"] == "COUNTERMODEL_LIFT_PROVES_CLOSED_SUPPORT_ALONE_CANNOT_DERIVE_THEOREM",
        "countermodel status mismatch",
    )
    require(countermodel["countermodel_valid_for_current_support"] is True, "countermodel invalid")
    for key, value in countermodel["closed_support_facts_true"].items():
        require(value is True, f"countermodel closed fact false: {key}")
    for key, value in countermodel["additional_structural_support_true"].items():
        require(value is True, f"countermodel structural support false: {key}")
    for key, value in countermodel["source_promotion_fields_false"].items():
        require(value is False, f"countermodel source field unexpectedly true: {key}")
    for key, value in countermodel["lifted_to_theorem_fields_false"].items():
        require(value is True, f"lifted theorem false-field missing: {key}")

    require(
        decision["status"] == "PROOF_ATTEMPT_FAILED_PRODUCTIVELY_COUNTERMODEL_AND_NEXT_KERNEL_IDENTIFIED",
        "decision status mismatch",
    )
    require(decision["theorem_proved_now"] is False, "decision overproved theorem")
    require(decision["conditional_witness_would_validate"] is True, "decision lost conditional witness")
    require(decision["closed_support_countermodel_blocks_support_only_proof"] is True, "countermodel block missing")
    require(decision["unpatched_dynamic_C1_closed"] is False, "unpatched dynamic C1 overclosed")
    require(decision["next_required_artifact"] == NEXT, "decision next mismatch")
    require(decision["superset_strategy"]["locked_target_used_only_as_postcheck"] is True, "locked target misuse")
    require(decision["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset paths treated as knobs")

    kernel = decision["next_kernel"]
    require(kernel["name"] == "PreResidualVariationOperatorAndHessianSourceKernelEmission", "kernel name mismatch")
    require(kernel["already_proved_sublemma"]["basis_to_rows"] is True, "basis sublemma lost")
    for key, value in kernel["must_emit"].items():
        require(value is False, f"next kernel emission unexpectedly true: {key}")

    require(data["theorem_attempt"]["proved"] is False, "candidate theorem overproved")
    require(data["theorem_attempt"]["conditional_witness_would_validate"] is True, "candidate conditional lost")
    require(data["closure_decision"]["closed_support_alone_sufficient"] is False, "candidate support sufficiency overclaimed")
    require(data["closure_decision"]["unpatched_dynamic_C1_closed"] is False, "candidate unpatched overclosed")
    for key in [
        "maximal_closed_support_synthesized",
        "theorem_attempt_executed",
        "support_only_derivation_refuted",
        "next_source_kernel_identified",
    ]:
        require(data["what_was_achieved"][key] is True, f"achievement missing: {key}")

    require("not** proved" in note, "note missing failed proof guard")
    require("countermodel" in note, "note missing countermodel")
    require(NEXT in note, "note missing next target")

    for packet in [data, support, attempt, countermodel, decision, cert]:
        guard(packet)

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
