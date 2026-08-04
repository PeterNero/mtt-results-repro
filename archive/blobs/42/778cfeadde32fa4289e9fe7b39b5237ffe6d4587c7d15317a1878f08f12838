"""Build adoption decision for the one-shared-physical-primitive closure standard."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
STANDARD = PACKET_DIR / "adopted_one_shared_primitive_closure_standard.packet.json"
GUARDRAILS = PACKET_DIR / "strict_noknob_upgrade_guardrails.packet.json"
DECISION = PACKET_DIR / "current_closure_standard_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_OnePrimitiveAdoptionDecision_v1.md"

PREVIOUS = DATA / "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit.candidate.json"
TIERED = (
    DATA
    / "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit"
    / "tiered_sm_closure_status.packet.json"
)
STRICT = (
    DATA
    / "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit"
    / "strict_pew_directk_source_row_audit.packet.json"
)
MIN_COUNT = (
    DATA
    / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
    / "minimal_parameter_count_summary.packet.json"
)
CLOSED_OPEN = (
    DATA
    / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
    / "closed_vs_open_parameter_slots.packet.json"
)
PHYS_AXIOM = DATA / "selected_physicalnormalizationsourceaxiom_or_directkcertificate.candidate.json"
PHYS_AXIOM_PACKET = (
    DATA
    / "selected_physicalnormalizationsourceaxiom_or_directkcertificate"
    / "physical_normalization_source_axiom.packet.json"
)
PHYS_DERIVATION = DATA / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade.candidate.json"

STATUS = (
    "MTT_SELECTED_PHYSICALNORMALIZATIONAXIOMDERIVATION_OR_ONEPRIMITIVEADOPTIONDECISION_"
    "ADOPTED_ONE_SHARED_PRIMITIVE_STANDARD"
)
NEXT = "MTT_Selected_OnePrimitiveClosurePaperUpdate_or_StrictNoKnobUpgradeProgram_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    previous = load(PREVIOUS)
    tiered = load(TIERED)
    strict = load(STRICT)
    min_count = load(MIN_COUNT)
    closed_open = load(CLOSED_OPEN)
    phys_axiom = load(PHYS_AXIOM)
    phys_axiom_packet = load(PHYS_AXIOM_PACKET)
    phys_derivation = load(PHYS_DERIVATION)

    adopted = (
        tiered["one_shared_primitive_tier_closed"]
        and tiered["shared_physical_primitive_count_under_axiom"] == 1
        and tiered["H_specific_parameter_count"] == 0
        and tiered["lambda_H_independent_parameter_replaced"]
        and phys_axiom_packet["accepted_as_premised_source_axiom"]
        and not phys_axiom_packet["accepted_as_strict_no_knob_source"]
    )

    standard = {
        "schema": "MTTAdoptedOneSharedPrimitiveClosureStandard.v1",
        "status": "ONE_SHARED_PRIMITIVE_STANDARD_ADOPTED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "adopted_closure_standard_name": "one-shared-physical-primitive SM closure",
        "adoption_decision": "adopt_as_current_closure_standard",
        "strict_no_knob_reclassified_as_upgrade_target": True,
        "adoption_basis": [
            "The physical-normalization axiom is explicit and typed.",
            "The direct-K certificate closes the H/lambda ten-K ledger under that axiom.",
            "The shared primitive is counted exactly once as P_EW.",
            "lambda_H is no longer an independent parameter.",
            "The H-specific parameter count is zero.",
        ],
        "adopted_standard_closed": adopted,
        "one_shared_primitive_tier_closed": tiered["one_shared_primitive_tier_closed"],
        "shared_physical_primitive_count": tiered["shared_physical_primitive_count_under_axiom"],
        "P_EW_parameter_count": tiered["P_EW_parameter_count"],
        "H_specific_parameter_count": tiered["H_specific_parameter_count"],
        "lambda_H_independent_parameter_replaced": tiered["lambda_H_independent_parameter_replaced"],
        "premised_selected_K_row_count": tiered["premised_selected_K_row_count"],
        "closed_non_neutrino_SM_like_count_excluding_QCD_theta": min_count[
            "closed_non_neutrino_SM_like_count_excluding_QCD_theta"
        ],
        "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta": min_count[
            "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"
        ],
        "if_QCD_theta_bar_is_admitted_as_external_slot_add": min_count[
            "if_QCD_theta_bar_is_admitted_as_external_slot_add"
        ],
        "if_absolute_neutrino_mass_is_admitted_add": min_count[
            "if_absolute_neutrino_mass_is_admitted_add"
        ],
        "if_Majorana_phases_are_admitted_add": min_count["if_Majorana_phases_are_admitted_add"],
    }

    guardrails = {
        "schema": "MTTStrictNoKnobUpgradeGuardrailsAfterOnePrimitiveAdoption.v1",
        "status": "STRICT_NOKNOB_RETAINED_AS_UPGRADE_TARGET",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_PEW_directK_source_rows_closed": False,
        "accepted_strict_P_EW_source_rows": strict["accepted_strict_P_EW_source_rows"],
        "accepted_direct_K_threshold_Omega_H_lambda_rows": strict[
            "accepted_direct_K_threshold_Omega_H_lambda_rows"
        ],
        "accepted_strict_derivation_route_count": strict["accepted_strict_derivation_route_count"],
        "physical_normalization_axiom_derived": phys_derivation["closure_decision"][
            "physical_normalization_axiom_derived"
        ],
        "strict_no_knob_closure": False,
        "forbidden_claims_under_adopted_standard": [
            "Do not call P_EW a derived strict source row.",
            "Do not call the adopted standard zero-primitive no-knob closure.",
            "Do not count lambda_H as an independent H-specific parameter.",
            "Do not use observed lambda_H as a selector for P_EW.",
        ],
        "remaining_upgrade_paths": [
            "derive the physical-normalization axiom from same-branch source data",
            "emit strict P_EW source rows",
            "emit strict direct K_threshold.Omega_H.lambda rows",
            "derive an equivalent Strominger/torsion/metrology source value",
        ],
        "open_slots_or_upgrade_targets": closed_open["open_slots_or_upgrade_targets"],
    }

    decision = {
        "schema": "MTTCurrentClosureStandardDecision.v1",
        "status": "CURRENT_STANDARD_ADOPTED_ONE_SHARED_PRIMITIVE_STRICT_NOKNOB_UPGRADE_OPEN",
        "closed_now": [
            "The current closure standard is explicitly adopted as one shared physical primitive.",
            "P_EW is counted once as the shared physical normalization primitive.",
            "lambda_H is not an independent parameter and the H-specific parameter count is zero.",
            "The premised H/lambda K ledger is closed at 10/10 under the adopted standard.",
        ],
        "not_closed": [
            "Strict zero-primitive/no-knob PEW/direct-K closure remains open.",
            "The physical-normalization axiom is not derived from current same-branch source data.",
            "True precision SM equivalence remains an upgrade target.",
        ],
        "acceptance": {
            "current_closure_standard_adopted": adopted,
            "current_closure_standard": "one_shared_physical_primitive",
            "one_shared_primitive_tier_closed": tiered["one_shared_primitive_tier_closed"],
            "strict_no_knob_closure": False,
            "strict_no_knob_is_upgrade_target": True,
            "minimal_parameter_ledger_closed_under_adopted_standard": True,
            "true_precision_equivalence_closed": False,
            "global_true_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalNormalizationAxiomDerivationOrOnePrimitiveAdoptionDecision",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_final_audit": rel(PREVIOUS),
            "tiered_closure_status": rel(TIERED),
            "strict_source_row_audit": rel(STRICT),
            "minimal_parameter_count_summary": rel(MIN_COUNT),
            "closed_vs_open_parameter_slots": rel(CLOSED_OPEN),
            "physical_normalization_axiom_candidate": rel(PHYS_AXIOM),
            "physical_normalization_axiom_packet": rel(PHYS_AXIOM_PACKET),
            "physical_normalization_derivation_candidate": rel(PHYS_DERIVATION),
        },
        "output_packets": {
            "adopted_one_shared_primitive_closure_standard": rel(STANDARD),
            "strict_noknob_upgrade_guardrails": rel(GUARDRAILS),
            "current_closure_standard_decision": rel(DECISION),
        },
        "theorem": {
            "name": "OneSharedPhysicalPrimitiveClosureStandardAdoptionTheorem",
            "proved": True,
            "statement": (
                "The current SM-closure standard is adopted as a one-shared-physical-primitive "
                "standard. Under this standard P_EW is counted once, lambda_H is replaced by "
                "the shared physical-normalization primitive, the H-specific parameter count is "
                "zero, and the H/lambda K ledger is closed at 10/10. This is not strict "
                "zero-primitive/no-knob closure; strict no-knob PEW/direct-K derivation remains "
                "an explicitly tracked upgrade target."
            ),
        },
        "key_numbers": {
            "shared_physical_primitive_count": tiered["shared_physical_primitive_count_under_axiom"],
            "P_EW_parameter_count": tiered["P_EW_parameter_count"],
            "H_specific_parameter_count": tiered["H_specific_parameter_count"],
            "premised_selected_K_row_count": tiered["premised_selected_K_row_count"],
            "accepted_strict_P_EW_source_rows": strict["accepted_strict_P_EW_source_rows"],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": strict[
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "closed_non_neutrino_SM_like_count_excluding_QCD_theta": min_count[
                "closed_non_neutrino_SM_like_count_excluding_QCD_theta"
            ],
            "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta": min_count[
                "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"
            ],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_OnePrimitiveAdoptionDecision_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "current_closure_standard_adopted": adopted,
        "current_closure_standard": "one_shared_physical_primitive",
        "one_shared_primitive_tier_closed": tiered["one_shared_primitive_tier_closed"],
        "strict_no_knob_closure": False,
        "strict_no_knob_is_upgrade_target": True,
        "shared_physical_primitive_count": tiered["shared_physical_primitive_count_under_axiom"],
        "H_specific_parameter_count": tiered["H_specific_parameter_count"],
        "lambda_H_independent_parameter_replaced": tiered["lambda_H_independent_parameter_replaced"],
        "minimal_parameter_ledger_closed_under_adopted_standard": True,
        "true_precision_equivalence_closed": False,
        "global_true_SM_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalNormalizationAxiomDerivation or OnePrimitiveAdoptionDecision v1

Status: `{STATUS}`

## Adopted Standard

The current closure standard is now:

`one-shared-physical-primitive SM closure`

This means:

- shared physical primitive count: `{tiered["shared_physical_primitive_count_under_axiom"]}`
- `P_EW` is counted once as the shared physical normalization primitive
- H-specific parameter count: `{tiered["H_specific_parameter_count"]}`
- independent `lambda_H` parameter: replaced
- premised H/lambda K ledger: `{tiered["premised_selected_K_row_count"]}/10`
- non-neutrino count excluding QCD theta: `{min_count["closed_non_neutrino_SM_like_count_excluding_QCD_theta"]}`
- count with minimal PMNS excluding QCD theta: `{min_count["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"]}`

## Guardrail

This is not strict zero-primitive no-knob closure:

- strict `P_EW` source rows: `{strict["accepted_strict_P_EW_source_rows"]}`
- strict direct-K rows: `{strict["accepted_direct_K_threshold_Omega_H_lambda_rows"]}`
- physical-normalization axiom derived: `false`

Strict no-knob remains the upgrade program.

Next required artifact: `{NEXT}`.
"""

    write_json(STANDARD, standard)
    write_json(GUARDRAILS, guardrails)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
