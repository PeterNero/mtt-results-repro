"""Audit adoption of the one-shared-physical-primitive closure standard."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STANDARD = PACKET_DIR / "adopted_one_shared_primitive_closure_standard.packet.json"
GUARDRAILS = PACKET_DIR / "strict_noknob_upgrade_guardrails.packet.json"
DECISION = PACKET_DIR / "current_closure_standard_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_OnePrimitiveAdoptionDecision_v1.md"
)

STATUS = (
    "MTT_SELECTED_PHYSICALNORMALIZATIONAXIOMDERIVATION_OR_ONEPRIMITIVEADOPTIONDECISION_"
    "ADOPTED_ONE_SHARED_PRIMITIVE_STANDARD"
)
NEXT = "MTT_Selected_OnePrimitiveClosurePaperUpdate_or_StrictNoKnobUpgradeProgram_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    standard = load(STANDARD)
    guardrails = load(GUARDRAILS)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is True, "adoption closure should be claimed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(standard["status"] == "ONE_SHARED_PRIMITIVE_STANDARD_ADOPTED", "standard status")
    require(standard["observed_data_used_as_selector"] is False, "standard observed selector")
    require(standard["target_fitting_used"] is False, "standard target fitting")
    require(standard["adopted_closure_standard_name"] == "one-shared-physical-primitive SM closure", "name")
    require(standard["adoption_decision"] == "adopt_as_current_closure_standard", "decision")
    require(standard["strict_no_knob_reclassified_as_upgrade_target"] is True, "strict upgrade")
    require(standard["adopted_standard_closed"] is True, "standard not closed")
    require(standard["one_shared_primitive_tier_closed"] is True, "tier not closed")
    require(standard["shared_physical_primitive_count"] == 1, "primitive count")
    require(standard["P_EW_parameter_count"] == 1, "P_EW count")
    require(standard["H_specific_parameter_count"] == 0, "H count")
    require(standard["lambda_H_independent_parameter_replaced"] is True, "lambda replaced")
    require(standard["premised_selected_K_row_count"] == 10, "K count")
    require(standard["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "non-neutrino")
    require(standard["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24, "PMNS count")

    require(guardrails["status"] == "STRICT_NOKNOB_RETAINED_AS_UPGRADE_TARGET", "guard status")
    require(guardrails["observed_data_used_as_selector"] is False, "guard observed selector")
    require(guardrails["target_fitting_used"] is False, "guard target fitting")
    require(guardrails["strict_PEW_directK_source_rows_closed"] is False, "strict overclosed")
    require(guardrails["accepted_strict_P_EW_source_rows"] == 0, "strict PEW rows")
    require(guardrails["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(guardrails["accepted_strict_derivation_route_count"] == 0, "derivation count")
    require(guardrails["physical_normalization_axiom_derived"] is False, "axiom overderived")
    require(guardrails["strict_no_knob_closure"] is False, "no-knob overclosed")
    require(len(guardrails["forbidden_claims_under_adopted_standard"]) == 4, "forbidden claims")
    require(len(guardrails["remaining_upgrade_paths"]) == 4, "upgrade paths")

    require(
        decision["status"] == "CURRENT_STANDARD_ADOPTED_ONE_SHARED_PRIMITIVE_STRICT_NOKNOB_UPGRADE_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    acceptance = decision["acceptance"]
    require(acceptance["current_closure_standard_adopted"] is True, "accept adopted")
    require(acceptance["current_closure_standard"] == "one_shared_physical_primitive", "accept standard")
    require(acceptance["one_shared_primitive_tier_closed"] is True, "accept tier")
    require(acceptance["strict_no_knob_closure"] is False, "accept strict")
    require(acceptance["strict_no_knob_is_upgrade_target"] is True, "accept upgrade")
    require(acceptance["minimal_parameter_ledger_closed_under_adopted_standard"] is True, "ledger")
    require(acceptance["true_precision_equivalence_closed"] is False, "precision overclosed")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "OneSharedPhysicalPrimitiveClosureStandardAdoptionTheorem", "theorem")
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["shared_physical_primitive_count"] == 1, "key primitive")
    require(key["P_EW_parameter_count"] == 1, "key P_EW")
    require(key["H_specific_parameter_count"] == 0, "key H")
    require(key["premised_selected_K_row_count"] == 10, "key K")
    require(key["accepted_strict_P_EW_source_rows"] == 0, "key PEW")
    require(key["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "key direct K")
    require(key["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "key non-neutrino")
    require(key["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24, "key PMNS")

    require(cert["current_closure_standard_adopted"] is True, "cert adopted")
    require(cert["current_closure_standard"] == "one_shared_physical_primitive", "cert standard")
    require(cert["one_shared_primitive_tier_closed"] is True, "cert tier")
    require(cert["strict_no_knob_closure"] is False, "cert strict")
    require(cert["strict_no_knob_is_upgrade_target"] is True, "cert upgrade")
    require(cert["shared_physical_primitive_count"] == 1, "cert primitive")
    require(cert["H_specific_parameter_count"] == 0, "cert H")
    require(cert["lambda_H_independent_parameter_replaced"] is True, "cert lambda")
    require(cert["minimal_parameter_ledger_closed_under_adopted_standard"] is True, "cert ledger")
    require(cert["true_precision_equivalence_closed"] is False, "cert precision")

    for phrase in [
        "`one-shared-physical-primitive SM closure`",
        "strict `P_EW` source rows: `0`",
        "physical-normalization axiom derived: `false`",
        "Strict no-knob remains the upgrade program.",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
