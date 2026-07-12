"""Audit R_theta source-owner/row-coefficient packet attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OWNER_MATRIX = PACKET_DIR / "rtheta_source_owner_candidate_matrix.packet.json"
COEFFICIENT_MANIFEST = PACKET_DIR / "rtheta_row_coefficient_slot_manifest.packet.json"
CONSTRUCTION_ATTEMPT = PACKET_DIR / "rtheta_source_owner_row_coefficient_construction_attempt.packet.json"
DECISION = PACKET_DIR / "rtheta_blocker_contraction_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_rtheta_owner_coefficient_attempt.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RThetaSourceOwnerRowCoefficientPacket_or_BlockerContraction_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_RTHETA_SOURCEOWNER_ROWCOEFFICIENTPACKET_OR_BLOCKERCONTRACTION_"
    "BUILT_PRECURSORS_ACCEPTED_PACKET_OPEN"
)
NEXT = "MTT_Selected_RThetaCoefficientFormulaDerivation_or_SelectedOwnerBridge_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    owners = load(OWNER_MATRIX)
    coeffs = load(COEFFICIENT_MANIFEST)
    construction = load(CONSTRUCTION_ATTEMPT)
    decision = load(DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")

    require(
        owners["status"] == "SOURCE_OWNER_CANDIDATES_AUDITED_PRECURSORS_ONLY",
        "owner matrix status mismatch",
    )
    require(owners["candidate_count"] == 5, "wrong source owner candidate count")
    require(owners["accepted_precursor_count"] >= 5, "expected precursors missing")
    require(owners["accepted_rtheta_source_owner_count"] == 0, "source owner overaccepted")
    require(owners["best_current_precursor"] == "same_source_dynamic_matter_overlap_packet", "wrong best precursor")
    owner_rows = {row["candidate_id"]: row for row in owners["candidate_rows"]}
    require(
        owner_rows["same_source_dynamic_matter_overlap_packet"]["accepted_as_rtheta_precursor"] is True,
        "dynamic matter overlap precursor not retained",
    )
    require(
        owner_rows["same_source_dynamic_matter_overlap_packet"]["accepted_as_rtheta_source_owner"] is False,
        "dynamic matter overlap overpromoted",
    )
    require(
        owner_rows["terminal_smslot_functor_A1_A3"]["accepted_as_rtheta_source_owner"] is False,
        "SMSlot functor overpromoted",
    )
    for row in owners["candidate_rows"]:
        require(row["missing_for_rtheta_source_owner"], f"owner row lacks missing fields: {row['candidate_id']}")
    require(owners["closure_claimed"] is False, "owner matrix overclaimed")

    require(
        coeffs["status"] == "ROW_COEFFICIENT_SLOT_MANIFEST_BUILT_VALUES_OPEN",
        "coefficient manifest status mismatch",
    )
    require(coeffs["slot_count"] == 10, "wrong coefficient slot count")
    require(coeffs["filled_slot_count"] == 0, "coefficient slots overfilled")
    require(coeffs["manifest_closed"] is True, "manifest not closed")
    for key in [
        "row_coefficients_closed",
        "basis_map_closed",
        "precision_convention_closed",
    ]:
        require(coeffs[key] is False, f"coefficient manifest overclosed: {key}")
    threshold_count = sum(1 for row in coeffs["coefficient_slots"] if row["row_family"] == "threshold_matching")
    mass_count = sum(1 for row in coeffs["coefficient_slots"] if row["row_family"] == "mass_scheme_conversion")
    require(threshold_count == 5, "wrong threshold slot count")
    require(mass_count == 5, "wrong mass-scheme slot count")
    require(coeffs["closure_claimed"] is False, "coefficient manifest overclaimed")

    require(
        construction["status"]
        == "RTHETA_PACKET_CONSTRUCTION_ATTEMPTED_SOURCE_OWNER_AND_COEFFICIENTS_OPEN",
        "construction status mismatch",
    )
    require(construction["accepted_source_owner"] is None, "construction accepted source owner")
    require(construction["accepted_threshold_coefficients"] == [], "threshold coefficients overaccepted")
    require(construction["accepted_mass_scheme_coefficients"] == [], "mass coefficients overaccepted")
    require(construction["basis_map_to_value_packet"] is None, "basis map overaccepted")
    require(construction["selected_precision_convention"] is None, "precision convention overaccepted")
    require(construction["profile_response"] is None, "profile response overaccepted")
    require(construction["construction_successful"] is False, "construction overclaimed success")
    require(construction["external_profile_workspace_imported"] is False, "external workspace overimported")
    require(construction["closure_claimed"] is False, "construction overclaimed")

    require(
        decision["status"] == "PRECURSOR_AND_SLOT_MANIFEST_CLOSED_RTHETA_PACKET_OPEN",
        "decision status mismatch",
    )
    require(decision["source_owner_candidate_matrix_closed"] is True, "owner matrix not closed")
    require(decision["best_current_precursor_identified"] is True, "best precursor not closed")
    require(decision["row_coefficient_slot_manifest_closed"] is True, "coefficient manifest not closed")
    for key in [
        "accepted_rtheta_source_owner",
        "row_coefficients_filled",
        "rtheta_packet_constructed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
    require(len(decision["contracted_frontier"]) == 4, "frontier not contracted")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closed_now"]["source_owner_candidate_matrix"] is True, "cutset missing owner closure")
    require(cutset["closed_now"]["row_coefficient_slot_manifest"] is True, "cutset missing manifest closure")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")

    final = data["closure_decision"]
    require(final["source_owner_candidate_matrix_closed"] is True, "candidate final owner matrix not closed")
    require(final["row_coefficient_slot_manifest_closed"] is True, "candidate final manifest not closed")
    for key in [
        "accepted_rtheta_source_owner_closed",
        "row_coefficients_closed",
        "selected_threshold_response_functional_instantiated",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(final[key] is False, f"candidate final overclosed: {key}")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require(cert["accepted_rtheta_source_owner_count"] == 0, "certificate owner overaccepted")
    require(cert["filled_coefficient_slot_count"] == 0, "certificate coefficients overfilled")
    require("accepted R_theta source owners  : 0" in note, "note missing zero-owner guard")
    require("row coefficient slots filled    : 0" in note, "note missing zero-slot guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
