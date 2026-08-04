"""Audit q79 sector-charge End0 value-route import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_sectorcharge_end0_value_route_import.candidate.json"
CERT = ROOT / "certificates" / "q79_sectorcharge_end0_value_route_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_SectorCharge_End0_ValueRoute_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_q79_sectorcharge_end0_value_route.py"

STATUS = "Q79_SECTORCHARGE_END0_VALUE_ROUTE_IMPORTED_MATTERSLOT_OVERLAP_OPEN"
NEXT = "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(all(data["checks"].values()), "not all checks passed")

    part = data["structural_partition"]
    require(part["phase_route"] == ["u", "e"], "phase route mismatch")
    require(part["shift_route"] == ["d", "nuD"], "shift route mismatch")
    require(part["su5_e6_matches_required_partition"] is True, "SU5/E6 partition not imported")
    require(part["selected_sector_charge_or_chirality_table_proved"] is False, "sector table overproved")
    require(part["selected_transfer_normalization_proved"] is False, "transfer normalization overproved")
    require(part["nuD_singlet_rule_closed"] is False, "nuD singlet rule overclosed")

    q79_sector = data["q79_sector_charge_reduction"]
    require(q79_sector["closure_claimed"] is False, "q79 sector overclaims closure")
    require(q79_sector["target_fitting_used"] is False, "q79 sector target fitting")
    decision = q79_sector["sector_charge_reduction"]["decision"]
    require(decision["su5_e6_partition_matches_required_route"] is True, "q79 partition mismatch")
    require(decision["selected_sector_charge_or_chirality_table_proved"] is False, "q79 sector table overproved")
    require(decision["selected_transfer_normalization_proved"] is False, "q79 normalization overproved")

    sm_gram = data["sm_gram_transfer_packet"]
    require(sm_gram["gram_transfer_packet"]["conditional_gram_theorem_proved"] is True, "conditional Gram theorem missing")
    require(sm_gram["gram_transfer_packet"]["physical_transfer_normalization_selected"] is False, "physical normalization overselected")
    require(sm_gram["minimal_open_fields"]["selected_1M_Dirac_neutrino_rule"]["closed"] is False, "1M rule overclosed")
    require(sm_gram["minimal_open_fields"]["selected_zero_mode_bases_K_s"]["closed"] is False, "zero-mode bases overclosed")

    q79_end0 = data["q79_end0_value_route"]
    require(q79_end0["decision"]["best_next_object"] == NEXT, "wrong End0 next object")
    require(q79_end0["decision"]["naive_Ext_scale_to_alpha1_source_normalization_rejected"] is True, "naive source norm not rejected")
    require(q79_end0["decision"]["sector_routing_route_remains_primary"] is True, "sector route not primary")
    require(q79_end0["route_A_source_normalization"]["closed_as_nogo"] is True, "route A no-go missing")
    require(q79_end0["route_A_source_normalization"]["central_shared_circle_retained"] is True, "shared circle guard missing")
    require(q79_end0["route_B_end0_to_sector_routing"]["End0_row_response_available"] is True, "End0 row response missing")
    require(q79_end0["route_B_end0_to_sector_routing"]["selected_End0_to_sector_functor_values_extracted"] is False, "End0 values overextracted")

    contract = data["end0_next_contract"]
    require(contract["status"] == "OPEN_SELECTED_END0_TO_SECTOR_FUNCTOR_VALUES_REQUIRED", "End0 contract status mismatch")
    require(contract["next_required_artifact"] == NEXT, "End0 contract next mismatch")
    require("sector charge/routing table including the 1_M Dirac-neutrino rule or a replacement rule" in contract["required_fields"], "End0 contract missing 1M rule")

    closes = data["what_closes_now"]
    for key in [
        "sector_charge_reduced_to_matter_slot_overlap",
        "su5_e6_structural_partition_imported",
        "nuD_singlet_gap_identified",
        "conditional_gram_transfer_scalar_imported",
        "naive_Ext_scale_to_alpha1_source_normalization_rejected",
        "End0_sector_functor_route_selected_as_next_legal_object",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_selected_sector_charge_or_chirality_table",
        "claims_selected_transfer_normalization",
        "claims_selected_End0_to_sector_routing",
        "claims_A_selected_or_b_selected",
        "claims_C1_response_emitted",
        "uses_locked_target_columns_as_selector",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
        "full_SM_closure_claimed",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("reduced, not closed" in note, "note missing reduction guard")
    require("naive route" in note, "note missing naive no-go")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
