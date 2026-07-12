"""Audit Step66 scalar-value no-go / magnitude-threshold source frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step66_scalarvalue_nogo_or_magnitudethresholdsource_frontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
NOGO_PACKET = PACKET_DIR / "step66_closed_rows_vs_scalar_value_nogo.packet.json"
MISSING_PACKET = PACKET_DIR / "step66_minimal_missing_source_object.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step66_ScalarValueNoGo_or_MagnitudeThresholdSourceFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP66_SCALAR_VALUE_NOGO_MAGNITUDE_THRESHOLD_SOURCE_FRONTIER_FIXED"
NEXT = "MTT_Selected_GenerationResolvedMagnitudeThresholdSourceRows_or_SelectedUniversalAnchorExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    nogo = load(NOGO_PACKET)
    missing = load(MISSING_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem mismatch")

    for item in [data, nogo, missing, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(nogo["pure_weyl_coefficient_rows_closed"] is True, "pure Weyl rows not closed")
    require(nogo["lambda_orbit_scaled_pure_rows_closed"] is True, "lambda orbit rows not closed")
    require(nogo["rtheta_scalar_value_functional_source_domain_closed"] is True, "Rtheta domain not closed")
    require(nogo["ten_scalar_codomain_aligned"] is True, "ten-row codomain not aligned")
    require(nogo["rank_gap_theorem_proved"] is True, "rank gap theorem not imported")
    require(nogo["source_column_count"] == 2, "source column count mismatch")
    require(nogo["source_sector_slot_count"] == 4, "source sector slot count mismatch")
    require(nogo["charged_generation_magnitude_rows"] == 9, "charged row count mismatch")
    require(nogo["charged_plus_lambda_rows"] == 10, "ten-row count mismatch")
    require(nogo["rank_gap_against_charged_rows"] == 7, "rank gap mismatch")
    require(nogo["slot_gap_against_charged_rows"] == 5, "slot gap mismatch")
    require(nogo["accepted_scalar_row_count_now"] == 0, "scalar rows overaccepted")
    require(nogo["accepted_coefficient_row_count"] == 0, "coefficient rows overaccepted")
    require(nogo["lambda_H_row_emitted"] is False, "lambda_H overemitted")
    require(nogo["lambda_H_coefficient_selected"] is False, "lambda_H coefficient overselected")
    require(nogo["diagnostic_coefficient_count"] == 9, "diagnostic coefficient count mismatch")
    require(
        nogo["diagnostic_coefficients_rejected_as_selectors"] is True,
        "diagnostic coefficients not rejected",
    )
    require(nogo["external_rows_admitted_only"] is True, "external row admission mismatch")
    require(
        nogo["selected_internal_threshold_mass_derivation_closed"] is False,
        "internal threshold derivation overclosed",
    )

    for phrase in [
        "generation-resolved magnitude-bearing projection weights",
        "selected threshold response functional instantiation",
        "selected same-branch threshold matching source rows",
        "selected same-branch mass-scheme conversion source rows",
        "selected lambda_H source row",
    ]:
        require(phrase in missing["still_missing"], f"missing route not listed: {phrase}")
    require(
        any("candidate-specific universal source anchor" in item for item in missing["still_missing"]),
        "universal anchor route not listed",
    )
    require(NEXT == missing["next_required_artifact"], "missing packet next mismatch")

    decision = data["closure_decision"]
    require(decision["pure_weyl_coefficient_source_layer_closed"] is True, "decision pure rows missing")
    require(decision["rtheta_source_domain_closed"] is True, "decision Rtheta domain missing")
    require(decision["rank_insufficiency_for_scalar_values_proved"] is True, "decision rank no-go missing")
    require(decision["diagnostic_values_rejected_as_selectors"] is True, "decision diagnostic guard missing")
    require(decision["external_rows_rejected_as_internal_no_knob_emissions"] is True, "decision external guard missing")
    for key in [
        "lambda_H_row_emitted",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed: {key}")
        require(cert[key] is False, f"certificate overclosed: {key}")
    require(decision["accepted_scalar_row_count_now"] == 0, "decision scalar rows overaccepted")
    require(cert["accepted_scalar_row_count_now"] == 0, "certificate scalar rows overaccepted")

    for phrase in [
        "pure Weyl coefficient/source layer closed : true",
        "source columns available                  : 2",
        "charged scalar rows required              : 9",
        "accepted scalar rows now                  : 0",
        "diagnostic coefficients accepted          : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
