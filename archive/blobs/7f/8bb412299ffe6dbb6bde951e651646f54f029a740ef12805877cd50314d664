"""Audit strict PEW/direct-K source-row and final SM no-knob status."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT_AUDIT = PACKET_DIR / "strict_pew_directk_source_row_audit.packet.json"
TIERED_CLOSURE = PACKET_DIR / "tiered_sm_closure_status.packet.json"
DECISION = PACKET_DIR / "final_sm_noknob_or_oneprimitive_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_StrictPEWDirectKSourceRows_or_FinalSMNoKnobAudit_v1.md"

STATUS = (
    "MTT_SELECTED_STRICTPEWDIRECTKSOURCEROWS_OR_FINALSMNOKNOBAUDIT_"
    "BUILT_STRICT_OPEN_ONEPRIMITIVE_TIER_CLOSED"
)
NEXT = "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_OnePrimitiveAdoptionDecision_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    strict = load(STRICT_AUDIT)
    tiered = load(TIERED_CLOSURE)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is False, "candidate overclosed")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(strict["status"] == "STRICT_SOURCE_ROWS_ZERO_ALL_CURRENT_ROUTES_TESTED", "strict status")
    require(strict["observed_data_used_as_selector"] is False, "strict observed selector")
    require(strict["target_fitting_used"] is False, "strict target fitting")
    require(strict["accepted_strict_P_EW_source_rows"] == 0, "strict PEW rows")
    require(strict["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "strict direct K")
    require(strict["accepted_strict_derivation_route_count"] == 0, "strict routes")
    require(strict["physical_normalization_axiom_derived"] is False, "axiom overderived")
    require(strict["strict_no_knob_ten_row_closure"] is False, "ten-row overclosed")
    require(strict["strict_no_knob_closed"] is False, "strict no-knob overclosed")

    require(tiered["status"] == "ONE_SHARED_PRIMITIVE_TIER_CLOSED_STRICT_NOKNOB_OPEN", "tiered status")
    require(tiered["observed_data_used_as_selector"] is False, "tiered observed selector")
    require(tiered["target_fitting_used"] is False, "tiered target fitting")
    require(tiered["physical_normalization_source_axiom_constructed"] is True, "axiom constructed")
    require(tiered["direct_K_certificate_constructed_under_axiom"] is True, "K cert")
    require(tiered["minimal_one_primitive_H_lambda_lane_closed"] is True, "one primitive lane")
    require(tiered["premised_selected_K_row_count"] == 10, "premised K")
    require(tiered["shared_physical_primitive_count_under_axiom"] == 1, "shared primitive")
    require(tiered["P_EW_counted_as_shared_physical_primitive"] is True, "P_EW counted")
    require(tiered["P_EW_parameter_count"] == 1, "P_EW count")
    require(tiered["H_specific_parameter_count"] == 0, "H parameter")
    require(tiered["lambda_H_independent_parameter_replaced"] is True, "lambda replaced")
    require(tiered["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "non-neutrino count")
    require(tiered["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24, "PMNS count")
    require(tiered["one_shared_primitive_tier_closed"] is True, "one primitive not closed")
    require(tiered["strict_no_knob_closed"] is False, "tiered strict overclosed")
    require(tiered["true_precision_equivalence_closed"] is False, "precision overclosed")

    require(decision["status"] == "STRICT_NOKNOB_OPEN_ONE_SHARED_PRIMITIVE_TIER_CLOSED", "decision status")
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    counts = decision["source_row_counts"]
    require(counts["accepted_strict_P_EW_source_rows"] == 0, "decision PEW")
    require(counts["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "decision K")
    require(counts["accepted_strict_derivation_route_count"] == 0, "decision routes")
    require(counts["premised_P_EW_source_rows"] == 1, "decision premised PEW")
    require(counts["premised_direct_K_threshold_Omega_H_lambda_rows"] == 1, "decision premised K")
    require(counts["premised_selected_K_row_count"] == 10, "decision ten K")
    require(counts["shared_physical_primitive_count_under_axiom"] == 1, "decision primitive")
    require(counts["H_specific_parameter_count"] == 0, "decision H param")
    acceptance = decision["acceptance"]
    require(acceptance["strict_PEW_directK_source_rows_closed"] is False, "accept strict")
    require(acceptance["physical_normalization_axiom_derived"] is False, "accept axiom")
    require(acceptance["strict_no_knob_closure"] is False, "accept no-knob")
    require(acceptance["one_shared_primitive_tier_closed"] is True, "accept one primitive")
    require(acceptance["minimal_parameter_ledger_closed"] is True, "accept ledger")
    require(acceptance["lambda_H_independent_parameter_replaced"] is True, "accept lambda")
    require(acceptance["H_specific_parameter_count_zero"] is True, "accept H zero")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global overclosed")
    require(acceptance["true_precision_equivalence_closed"] is False, "precision overclosed")
    require(acceptance["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(
        data["theorem"]["name"] == "StrictPEWDirectKSourceRowsOrFinalSMNoKnobAuditTheorem",
        "theorem",
    )
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["accepted_strict_P_EW_source_rows"] == 0, "key PEW")
    require(key["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "key K")
    require(key["accepted_strict_derivation_route_count"] == 0, "key routes")
    require(key["premised_selected_K_row_count"] == 10, "key K")
    require(key["shared_physical_primitive_count_under_axiom"] == 1, "key primitive")
    require(key["H_specific_parameter_count"] == 0, "key H")
    require(key["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "key non-neutrino")
    require(key["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24, "key PMNS")

    require(cert["strict_PEW_directK_source_rows_closed"] is False, "cert strict")
    require(cert["accepted_strict_P_EW_source_rows"] == 0, "cert PEW")
    require(cert["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "cert K")
    require(cert["physical_normalization_axiom_derived"] is False, "cert axiom")
    require(cert["strict_no_knob_closure"] is False, "cert no-knob")
    require(cert["one_shared_primitive_tier_closed"] is True, "cert one primitive")
    require(cert["minimal_parameter_ledger_closed"] is True, "cert ledger")
    require(cert["lambda_H_independent_parameter_replaced"] is True, "cert lambda")
    require(cert["shared_physical_primitive_count_under_axiom"] == 1, "cert primitive")
    require(cert["H_specific_parameter_count"] == 0, "cert H")
    require(cert["global_true_SM_no_knob_closure"] is False, "cert global")
    require(cert["true_precision_equivalence_closed"] is False, "cert precision")

    for phrase in [
        "strict `P_EW` source rows: `0`",
        "one-shared-physical-primitive tier: closed",
        "non-neutrino SM-like count excluding QCD theta: `18`",
        "with minimal PMNS oscillation policy excluding QCD theta: `24`",
        "strict no-knob PEW/direct-K closure",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
