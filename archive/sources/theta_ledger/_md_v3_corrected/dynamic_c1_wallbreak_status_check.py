"""Validate the imported Dynamic C1 wall-break status."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "selected_dynamic_c1_wallbreak_status.import.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    closure = packet["closure_claimed"]
    claims = packet["verified_claims"]
    unpatched = packet["unpatched_remaining"]
    full = packet["still_required_for_full_SM_closure"]

    require(packet["status"] == "IMPORTED_DYNAMIC_C1_PATCHED_WALL_BROKEN_UNPATCHED_OPEN", "bad status")
    require(packet["target_fitting_used"] is False, "target fitting must be false")
    require(packet["observed_physical_data_used_as_selector"] is False, "observed selector must be false")

    require(closure["patched_dynamic_C1"] is True, "patched dynamic C1 should close")
    require(closure["SM_parity_under_declared_standard"] is True, "SM parity replay should close under declared standard")
    require(closure["unpatched_dynamic_C1"] is False, "unpatched dynamic C1 must remain open")
    require(closure["true_SM_equivalence"] is False, "true SM equivalence must remain open")
    require(closure["full_no_knob_SM_closure"] is False, "full no-knob closure must remain open")

    require(claims["patched_dynamic_C1_packet_closed"] is True, "patched packet missing")
    require(claims["formal_110_rows_executed"] is True, "formal row execution missing")
    require(claims["primitive_72_postcheck_values_loaded"] is True, "primitive postcheck missing")
    require(claims["physical_measure_identity_open"] is True, "measure identity should remain open")
    require(claims["hessian_source_rows_open"] is True, "hessian source rows should remain open")

    require(unpatched["derive_source_axiom_from_unpatched_MTT"] is True, "unpatched derivation gate missing")
    require(unpatched["or_export_honest_selected_Galerkin_C1_tables"] is True, "Galerkin export gate missing")
    require(unpatched["SelectedFiniteC1SourceIdentityTheorem"] is True, "source identity theorem gate missing")

    require(full["unpatched_dynamic_C1_source_identity_theorem"] is True, "full closure source theorem gate missing")
    require(full["true_SM_equivalence"] is True, "true equivalence gate missing")
    require(full["full_no_knob_constants"] is True, "no-knob constants gate missing")

    print("Dynamic C1 wall-break status import PASS")
    print("status", packet["status"])
    print("next", packet["next_required_artifact"])


if __name__ == "__main__":
    main()
