"""Audit paper update and strict no-knob upgrade program after one-primitive adoption."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PAPER_UPDATE = PACKET_DIR / "paper_update_claims_and_wording.packet.json"
UPGRADE = PACKET_DIR / "strict_noknob_upgrade_program.packet.json"
DECISION = PACKET_DIR / "publication_ready_closure_standard_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_OnePrimitiveClosurePaperUpdate_or_StrictNoKnobUpgradeProgram_v1.md"

STATUS = (
    "MTT_SELECTED_ONEPRIMITIVECLOSUREPAPERUPDATE_OR_STRICTNOKNOBUPGRADEPROGRAM_"
    "BUILT_PUBLICATION_STANDARD_AND_UPGRADE_PROGRAM"
)
NEXT = "MTT_Selected_CorpusPaperRevisionPacket_or_StrictNoKnobUpgradeExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    paper = load(PAPER_UPDATE)
    upgrade = load(UPGRADE)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(data["closure_claimed"] is True, "candidate should close update packet")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")

    require(paper["status"] == "PAPER_UPDATE_CLAIMS_READY", "paper status")
    require(paper["observed_data_used_as_selector"] is False, "paper observed selector")
    require(paper["target_fitting_used"] is False, "paper target fitting")
    require(paper["current_closure_standard"] == "one_shared_physical_primitive", "paper standard")
    require("one-shared-physical-primitive" in paper["canonical_claim"], "canonical claim")
    require("strict no-knob remains open" in paper["short_claim"], "short claim")
    require(len(paper["allowed_claims"]) == 6, "allowed claims")
    require(len(paper["forbidden_claims"]) == 4, "forbidden claims")
    require(len(paper["required_paper_edits"]) == 5, "paper edits")
    require("not a strict zero-primitive" in paper["paper_limitations_sentence"], "limitations")

    require(upgrade["status"] == "STRICT_NOKNOB_UPGRADE_PROGRAM_DEFINED", "upgrade status")
    require(upgrade["observed_data_used_as_selector"] is False, "upgrade observed selector")
    require(upgrade["target_fitting_used"] is False, "upgrade target fitting")
    require(upgrade["strict_rows_currently_accepted"]["strict_P_EW_source_rows"] == 0, "strict PEW")
    require(
        upgrade["strict_rows_currently_accepted"]["strict_direct_K_threshold_Omega_H_lambda_rows"] == 0,
        "strict K",
    )
    require(upgrade["strict_rows_currently_accepted"]["strict_derivation_route_count"] == 0, "routes")
    require(len(upgrade["upgrade_paths"]) == 4, "upgrade paths")
    require(len(upgrade["ordered_upgrade_program"]) == 4, "ordered program")
    require(upgrade["strict_no_knob_closure_currently_closed"] is False, "strict overclosed")

    require(
        decision["status"] == "PUBLICATION_STANDARD_READY_STRICT_UPGRADE_PROGRAM_OPEN",
        "decision status",
    )
    require(len(decision["closed_now"]) == 4, "closed count")
    require(len(decision["not_closed"]) == 3, "not closed count")
    acceptance = decision["acceptance"]
    require(acceptance["paper_update_packet_ready"] is True, "paper ready")
    require(acceptance["publication_standard_ready"] is True, "publication ready")
    require(acceptance["current_closure_standard_adopted"] is True, "standard adopted")
    require(acceptance["current_closure_standard"] == "one_shared_physical_primitive", "standard")
    require(acceptance["one_shared_primitive_tier_closed"] is True, "tier")
    require(acceptance["strict_no_knob_closure"] is False, "strict")
    require(acceptance["strict_no_knob_upgrade_program_ready"] is True, "upgrade ready")
    require(acceptance["true_precision_equivalence_closed"] is False, "precision")
    require(acceptance["global_true_SM_no_knob_closure"] is False, "global")
    require(decision["next_exact_target"] == NEXT, "decision next")

    require(data["theorem"]["name"] == "OnePrimitiveClosurePaperUpdateAndStrictUpgradeProgramTheorem", "theorem")
    require(data["theorem"]["proved"] is True, "theorem proved")
    key = data["key_numbers"]
    require(key["shared_physical_primitive_count"] == 1, "primitive")
    require(key["H_specific_parameter_count"] == 0, "H count")
    require(key["premised_selected_K_row_count"] == 10, "K count")
    require(key["closed_non_neutrino_SM_like_count_excluding_QCD_theta"] == 18, "non-neutrino")
    require(key["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"] == 24, "PMNS")
    require(key["strict_P_EW_source_rows"] == 0, "key PEW")
    require(key["strict_direct_K_rows"] == 0, "key K")
    require(key["open_upgrade_target_count"] >= 4, "upgrade target count")

    require(cert["paper_update_packet_ready"] is True, "cert paper")
    require(cert["publication_standard_ready"] is True, "cert publication")
    require(cert["current_closure_standard"] == "one_shared_physical_primitive", "cert standard")
    require(cert["one_shared_primitive_tier_closed"] is True, "cert tier")
    require(cert["strict_no_knob_closure"] is False, "cert strict")
    require(cert["strict_no_knob_upgrade_program_ready"] is True, "cert upgrade")

    for phrase in [
        "Paper-Ready Claim",
        "one-shared-physical-primitive SM closure",
        "strict `P_EW` source rows: `0`",
        "strict no-knob closure: `false`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
