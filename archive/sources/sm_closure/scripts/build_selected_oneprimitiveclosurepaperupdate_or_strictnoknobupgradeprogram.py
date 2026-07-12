"""Build paper-update and strict-upgrade program after one-primitive adoption."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
PAPER_UPDATE = PACKET_DIR / "paper_update_claims_and_wording.packet.json"
UPGRADE = PACKET_DIR / "strict_noknob_upgrade_program.packet.json"
DECISION = PACKET_DIR / "publication_ready_closure_standard_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OnePrimitiveClosurePaperUpdate_or_StrictNoKnobUpgradeProgram_v1.md"

ADOPTION = DATA / "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision.candidate.json"
STANDARD = (
    DATA
    / "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision"
    / "adopted_one_shared_primitive_closure_standard.packet.json"
)
GUARDRAILS = (
    DATA
    / "selected_physicalnormalizationaxiomderivation_or_oneprimitiveadoptiondecision"
    / "strict_noknob_upgrade_guardrails.packet.json"
)
FINAL_AUDIT = DATA / "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit.candidate.json"
CLOSED_OPEN = (
    DATA
    / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem"
    / "closed_vs_open_parameter_slots.packet.json"
)

STATUS = (
    "MTT_SELECTED_ONEPRIMITIVECLOSUREPAPERUPDATE_OR_STRICTNOKNOBUPGRADEPROGRAM_"
    "BUILT_PUBLICATION_STANDARD_AND_UPGRADE_PROGRAM"
)
NEXT = "MTT_Selected_CorpusPaperRevisionPacket_or_StrictNoKnobUpgradeExecution_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    adoption = load(ADOPTION)
    standard = load(STANDARD)
    guardrails = load(GUARDRAILS)
    final_audit = load(FINAL_AUDIT)
    closed_open = load(CLOSED_OPEN)

    paper_update = {
        "schema": "MTTOnePrimitiveClosurePaperUpdateClaimsAndWording.v1",
        "status": "PAPER_UPDATE_CLAIMS_READY",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "adoption_candidate": rel(ADOPTION),
        "adopted_standard_packet": rel(STANDARD),
        "current_closure_standard": adoption["closure_decision"]["current_closure_standard"],
        "canonical_claim": (
            "MTT reaches SM closure at the one-shared-physical-primitive standard: "
            "one shared physical normalization primitive P_EW is counted once, "
            "lambda_H is not an independent H-specific parameter, and the H/lambda "
            "K-threshold ledger closes at 10/10 under the explicit axiom."
        ),
        "short_claim": "Closed at one-shared-physical-primitive SM standard; strict no-knob remains open.",
        "allowed_claims": [
            "The current adopted closure standard is one-shared-physical-primitive SM closure.",
            "P_EW is one shared physical normalization primitive.",
            "lambda_H is replaced by shared P_EW and is not an independent H-specific knob.",
            "The premised H/lambda K ledger is 10/10 under the physical-normalization axiom.",
            "The H-specific parameter count is zero.",
            "Strict no-knob PEW/direct-K derivation remains an upgrade target.",
        ],
        "forbidden_claims": guardrails["forbidden_claims_under_adopted_standard"],
        "required_paper_edits": [
            "Replace any claim of strict zero-primitive/no-knob SM closure with one-shared-physical-primitive SM closure.",
            "State explicitly that P_EW is counted once as a shared physical primitive.",
            "State explicitly that lambda_H is not an independent H-specific parameter.",
            "Move strict P_EW/direct-K derivation to a future-work or upgrade-theorem section.",
            "Keep observed SM values downstream of the selected source boundary.",
        ],
        "paper_abstract_sentence": (
            "We prove SM closure for MTT at a one-shared-physical-primitive standard, "
            "where a single physical normalization primitive replaces the independent "
            "Higgs quartic input while preserving the strict no-knob derivation as a "
            "separate upgrade problem."
        ),
        "paper_limitations_sentence": (
            "This result is not a strict zero-primitive/no-knob derivation of the "
            "electroweak normalization: current source data emit zero strict P_EW "
            "and direct-K rows."
        ),
    }

    upgrade = {
        "schema": "MTTStrictNoKnobUpgradeProgramAfterOnePrimitiveAdoption.v1",
        "status": "STRICT_NOKNOB_UPGRADE_PROGRAM_DEFINED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "guardrails_source": rel(GUARDRAILS),
        "strict_rows_currently_accepted": {
            "strict_P_EW_source_rows": guardrails["accepted_strict_P_EW_source_rows"],
            "strict_direct_K_threshold_Omega_H_lambda_rows": guardrails[
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "strict_derivation_route_count": guardrails["accepted_strict_derivation_route_count"],
        },
        "upgrade_paths": guardrails["remaining_upgrade_paths"],
        "ordered_upgrade_program": [
            {
                "id": "UPG-01",
                "target": "derive physical-normalization axiom from same-branch source data",
                "success_condition": "physical_normalization_axiom_derived=true",
            },
            {
                "id": "UPG-02",
                "target": "emit strict P_EW source row",
                "success_condition": "accepted_strict_P_EW_source_rows>0",
            },
            {
                "id": "UPG-03",
                "target": "emit strict direct K_threshold.Omega_H.lambda row",
                "success_condition": "accepted_direct_K_threshold_Omega_H_lambda_rows>0",
            },
            {
                "id": "UPG-04",
                "target": "derive equivalent Strominger/torsion/metrology source value",
                "success_condition": "strict threshold/metrology value row replaces adopted primitive",
            },
        ],
        "open_upgrade_targets": guardrails["open_slots_or_upgrade_targets"],
        "strict_no_knob_closure_currently_closed": False,
    }

    decision = {
        "schema": "MTTPublicationReadyClosureStandardDecision.v1",
        "status": "PUBLICATION_STANDARD_READY_STRICT_UPGRADE_PROGRAM_OPEN",
        "closed_now": [
            "A publication-ready claim standard is fixed.",
            "Paper wording and guardrails are explicit.",
            "Strict no-knob is no longer confused with the adopted standard.",
            "The strict no-knob upgrade program is ordered into four concrete paths.",
        ],
        "not_closed": [
            "No corpus papers have been rewritten in this artifact.",
            "Strict zero-primitive/no-knob PEW/direct-K derivation remains open.",
            "Full precision true-SM equivalence remains an upgrade target.",
        ],
        "acceptance": {
            "paper_update_packet_ready": True,
            "publication_standard_ready": True,
            "current_closure_standard_adopted": adoption["closure_decision"][
                "current_closure_standard_adopted"
            ],
            "current_closure_standard": adoption["closure_decision"]["current_closure_standard"],
            "one_shared_primitive_tier_closed": adoption["closure_decision"][
                "one_shared_primitive_tier_closed"
            ],
            "strict_no_knob_closure": False,
            "strict_no_knob_upgrade_program_ready": True,
            "true_precision_equivalence_closed": False,
            "global_true_SM_no_knob_closure": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedOnePrimitiveClosurePaperUpdateOrStrictNoKnobUpgradeProgram",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "adoption_candidate": rel(ADOPTION),
            "adopted_standard": rel(STANDARD),
            "guardrails": rel(GUARDRAILS),
            "final_strict_pew_audit": rel(FINAL_AUDIT),
            "closed_vs_open_slots": rel(CLOSED_OPEN),
        },
        "output_packets": {
            "paper_update_claims_and_wording": rel(PAPER_UPDATE),
            "strict_noknob_upgrade_program": rel(UPGRADE),
            "publication_ready_closure_standard_decision": rel(DECISION),
        },
        "theorem": {
            "name": "OnePrimitiveClosurePaperUpdateAndStrictUpgradeProgramTheorem",
            "proved": True,
            "statement": (
                "The adopted one-shared-physical-primitive closure standard is now converted "
                "into paper-ready claims, forbidden-claim guardrails, and an ordered strict "
                "no-knob upgrade program. This closes the wording/standard ambiguity without "
                "claiming strict zero-primitive PEW/direct-K derivation."
            ),
        },
        "key_numbers": {
            "shared_physical_primitive_count": standard["shared_physical_primitive_count"],
            "H_specific_parameter_count": standard["H_specific_parameter_count"],
            "premised_selected_K_row_count": standard["premised_selected_K_row_count"],
            "closed_non_neutrino_SM_like_count_excluding_QCD_theta": standard[
                "closed_non_neutrino_SM_like_count_excluding_QCD_theta"
            ],
            "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta": standard[
                "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"
            ],
            "strict_P_EW_source_rows": guardrails["accepted_strict_P_EW_source_rows"],
            "strict_direct_K_rows": guardrails["accepted_direct_K_threshold_Omega_H_lambda_rows"],
            "open_upgrade_target_count": len(closed_open["open_slots_or_upgrade_targets"]),
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_OnePrimitiveClosurePaperUpdate_or_StrictNoKnobUpgradeProgram_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "paper_update_packet_ready": True,
        "publication_standard_ready": True,
        "current_closure_standard": adoption["closure_decision"]["current_closure_standard"],
        "one_shared_primitive_tier_closed": True,
        "strict_no_knob_closure": False,
        "strict_no_knob_upgrade_program_ready": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected OnePrimitiveClosurePaperUpdate or StrictNoKnobUpgradeProgram v1

Status: `{STATUS}`

## Paper-Ready Claim

{paper_update["canonical_claim"]}

Short form:

`{paper_update["short_claim"]}`

## Required Paper Edits

1. Replace strict no-knob closure wording with one-shared-physical-primitive SM closure.
2. Count `P_EW` once as the shared physical normalization primitive.
3. State that `lambda_H` is not an independent H-specific parameter.
4. Put strict `P_EW`/direct-K derivation in the upgrade-program section.

## Guardrail

- strict `P_EW` source rows: `{guardrails["accepted_strict_P_EW_source_rows"]}`
- strict direct-K rows: `{guardrails["accepted_direct_K_threshold_Omega_H_lambda_rows"]}`
- strict no-knob closure: `false`

Next required artifact: `{NEXT}`.
"""

    write_json(PAPER_UPDATE, paper_update)
    write_json(UPGRADE, upgrade)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
