"""Audit strict physical-normalization axiom derivation / no-knob upgrade."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade.py"

SLUG = "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1.md"

ROUTE_TESTS = PACKET_DIR / "strict_physical_normalization_derivation_route_tests.packet.json"
NO_GO = PACKET_DIR / "scale_symmetry_and_threshold_value_obstruction.packet.json"
CONDITIONAL = PACKET_DIR / "conditional_strict_pew_upgrade_witness.packet.json"
NEXT_PACKET = PACKET_DIR / "next_source_value_payload_contract.packet.json"

STATUS = (
    "MTT_SELECTED_PHYSICALNORMALIZATIONAXIOMDERIVATION_OR_STRICTPEWNOKNOBUPGRADE_"
    "DERIVATION_ATTEMPTED_SCALE_AND_THRESHOLD_VALUES_OPEN"
)
NEXT = "MTT_Selected_StromingerThresholdOperatorValue_or_MetrologyUnitSource_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    routes = load(ROUTE_TESTS)
    no_go = load(NO_GO)
    conditional = load(CONDITIONAL)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")

    for payload in [candidate, cert, routes, no_go, conditional, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["derivation_attempted"] is True, "strict derivation not attempted")
    require(decision["accepted_strict_derivation_route_count"] == 0, "strict route overaccepted")
    require(decision["physical_normalization_axiom_derived"] is False, "axiom overderived")
    require(decision["strict_P_EW_source_rows"] == 0, "strict P_EW overaccepted")
    require(decision["strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "strict direct-K overaccepted")
    require(decision["premised_axiom_lane_preserved"] is True, "premised axiom lane lost")
    require(decision["premised_ten_K_ledger_preserved"] is True, "premised ten-K ledger lost")
    require(decision["scale_symmetry_no_go_active"] is True, "scale no-go not active")
    require(decision["strominger_threshold_values_open"] is True, "threshold value blocker lost")
    require(decision["strict_no_knob_ten_row_closure"] is False, "strict ten-row overclosed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM equivalence overclosed")

    require(routes["status"] == "ALL_CURRENT_STRICT_DERIVATION_ROUTES_TESTED_ZERO_ACCEPTED", "route status mismatch")
    require(routes["accepted_strict_derivation_route_count"] == 0, "route count mismatch")
    require(len(routes["routes"]) >= 5, "route test inventory too thin")
    for route in routes["routes"]:
        require(route["accepted_as_strict_derivation"] is False, f"route overaccepted: {route['route_id']}")
        require(route["observed_data_used_as_selector"] is False, f"observed selector in {route['route_id']}")
        require(route["target_fitting_used"] is False, f"target fitting in {route['route_id']}")

    require(no_go["status"] == "STRICT_PEW_AXIOM_NOT_DERIVED_CURRENT_SOURCE_DATA", "no-go status mismatch")
    require(no_go["strict_no_knob_P_EW_source_rows"] == 0, "no-go P_EW row mismatch")
    require(no_go["strict_direct_K_threshold_Omega_H_lambda_rows"] == 0, "no-go K row mismatch")
    require(no_go["scale_symmetry_obstruction"]["status"] == "PROVED_IN_CURRENT_FORMALIZATION", "scale theorem missing")
    require(
        no_go["scale_symmetry_obstruction"]["free_parameter_count_for_absolute_units"] == 1,
        "absolute scale count mismatch",
    )
    require(
        no_go["threshold_value_obstruction"]["strict_primary_route"] == "B_flux_strominger_threshold",
        "threshold route mismatch",
    )
    require(no_go["threshold_value_obstruction"]["strict_primary_route_selected"] is True, "threshold route not selected")
    for key in [
        "gaugekinetic_normalization_closed",
        "matching_scale_closed",
        "RG_scheme_closed",
        "selected_heterotic_strominger_kernel_closed",
        "analytic_torsion_or_threshold_operator_closed",
    ]:
        require(no_go["threshold_value_obstruction"][key] is False, f"threshold blocker overclosed: {key}")

    require(
        conditional["status"] == "CONDITIONAL_WITNESS_BUILT_IF_SOURCE_VALUES_EMITTED",
        "conditional status mismatch",
    )
    require(all(value is False for value in conditional["currently_supplied"].values()), "conditional value overfilled")
    then_closes = conditional["then_closes"]
    require(then_closes["derive_SelectedPhysicalGaugeActionNormalizationAxiom"] is True, "conditional derivation lost")
    require(then_closes["strict_P_EW_source_rows"] == 1, "conditional P_EW count mismatch")
    require(then_closes["strict_direct_K_threshold_Omega_H_lambda_rows"] == 1, "conditional K count mismatch")
    require(then_closes["strict_selected_K_row_count"] == 10, "conditional ten-K count mismatch")
    require(then_closes["H_specific_parameter_count"] == 0, "conditional H knob introduced")
    require(
        then_closes["minimal_ledger_non_neutrino_excluding_QCD_theta_if_P_EW_closes"] == 17,
        "conditional non-neutrino ledger mismatch",
    )
    require(
        then_closes["minimal_ledger_PMNS_excluding_QCD_theta_if_P_EW_closes"] == 23,
        "conditional PMNS ledger mismatch",
    )

    require(
        next_packet["status"] == "NEXT_IS_STROMINGER_THRESHOLD_OPERATOR_VALUE_OR_METROLOGY_UNIT_SOURCE",
        "next packet status mismatch",
    )
    require("reuse the explicit axiom as if it were derived" in next_packet["forbidden_targets"], "axiom-reuse guard missing")
    require("physical-normalization axiom derived       : false" in note, "note missing axiom guard")
    require("strict direct K_threshold.Omega_H.lambda   : 0" in note, "note missing direct-K guard")
    require(NEXT in note, "note missing next artifact")

    print("Strict physical-normalization / PEW no-knob upgrade audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
