"""Audit selected_physicalsourceemission_patchbackimport_or_unpatchedderivation."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalsourceemission_patchbackimport_or_unpatchedderivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PATCHED = PACKET_DIR / "patched_dynamic_c1_status_after_sourcegate.packet.json"
UNPATCHED = PACKET_DIR / "unpatched_measure_derivation_frontier.packet.json"
NEXT_ACTIONS = PACKET_DIR / "next_smparity_actions_after_patch.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalSourceEmission_PatchBackimport_or_UnpatchedDerivation_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    patched = load(PATCHED)
    unpatched = load(UNPATCHED)
    next_actions = load(NEXT_ACTIONS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_PHYSICALSOURCEEMISSION_PATCHBACKIMPORT_BUILT_UNPATCHED_DERIVATION_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "backimport theorem not proved")
    require(data["patched_spine_closure_claimed"] is True, "patched spine should be claimed")
    require(data["closure_claimed"] is False, "full closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(patched["patched_dynamic_C1_packet_closed"] is True, "patched dynamic C1 not closed")
    require(patched["patched_Route_B_physical_Galerkin_replacement"] is True, "patched Route B not closed")
    require(patched["patched_A_selected"] is True, "patched A missing")
    require(patched["patched_b_selected"] is True, "patched b missing")
    require(patched["patched_deltaTheta_C1"] is True, "patched deltaTheta missing")
    require(patched["patched_sector_response_matrices"] is True, "patched sectors missing")
    require(patched["not_full_SM_parity"] is True, "full SM parity overclaimed")
    require(patched["not_full_no_knob"] is True, "full no-knob overclaimed")

    require(unpatched["unpatched_open"]["unpatched_principle_derivation"] is True, "unpatched principle not open")
    require(unpatched["unpatched_open"]["unpatched_direct_PhiFinC1_action_derivation"] is True, "direct derivation not open")
    require(unpatched["unpatched_open"]["unpatched_Route_A_same_source_emission"] is True, "Route A not open")
    require(len(unpatched["three_legal_unpatched_routes"]) == 3, "wrong unpatched route count")
    require(unpatched["closure_claimed"] is False, "unpatched closure overclaimed")

    require(next_actions["patched_spine_next"]["selected_SM_packet_certificate_integration"] is True, "global SM packet gate missing")
    require(next_actions["local_dynamic_c1_next"]["unpatched_no_knob_measure_derivation"] is True, "local no-knob gate missing")
    require(next_actions["superset_strategy"]["uses_observed_constants"] is False, "superset uses observed constants")

    require(data["what_closes_now"]["patched_dynamic_C1_status_backimported"] is True, "candidate missing patched import")
    require(data["what_remains_open"]["unpatched_no_knob_dynamic_C1_derivation"] is True, "candidate missing unpatched open")
    require(cert["patched_dynamic_C1_status_backimported"] is True, "cert missing patched import")
    require(cert["unpatched_derivation_frontier_preserved"] is True, "cert missing unpatched frontier")
    require("does **not** claim full SM parity" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
