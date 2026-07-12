from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_character_channel_identification_stress_test_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    common = cert["common_infrastructure_closed"]
    comparison = cert["subspace_comparison"]
    legal = cert["legal_import"]
    still_open = cert["still_open"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "SHARED_Z64_Q64_ALIGNMENT_CLOSED_LITERAL_GR_TT_NOISE_CHANNEL_OPEN",
        "unexpected stress-test status",
    )
    require(all(common.values()), "all shared infrastructure inputs must be closed")
    require(comparison["same_Z64_exact_carrier"] is True, "same Z64 carrier should be closed")
    require(comparison["same_selected_q64_label"] is True, "same q64 label should be closed")
    require(comparison["literal_same_subspace"] is False, "must not identify distinct subspaces")
    require(comparison["gr_tt_character_pair"] == [2, 62], "GR TT helicity pair changed")
    require(comparison["covariance_character"] == "q_64=15", "covariance character changed")

    require(legal["internal_scale_data_can_be_shared"] is True, "internal scale sharing should be legal")
    require(
        legal["does_not_prove_GR_TT_noise_channel_equals_E15"] is True,
        "must retain literal-channel caveat",
    )

    require(still_open["literal_GR_TT_stochastic_channel_identified_with_E15"] is False, "literal channel should remain open")
    require(still_open["physical_Omega_0_selected"] is False, "Omega_0 should remain open")
    require(still_open["physical_GR_normalization_closed"] is False, "physical GR should remain open")

    require(guards["conflates_helicity2_plane_with_E15_character_line"] is False, "must not conflate subspaces")
    require(guards["claims_literal_channel_identity"] is False, "must not claim literal identity")
    require(guards["uses_observed_target_constant"] is False, "must not use observed target")
    require(guards["revokes_internal_character_import"] is False, "must not revoke legal import")
    require(guards["claims_physical_units"] is False, "must not claim physical units")

    require("E_15 K_64" in note, "note must name covariance channel")
    require("span{c_2,s_2}" in note, "note must name GR TT plane")
    require("not literally the same" in note, "note must state distinction")
    print("AUDIT_PASS: GR TT and E15 channels aligned on shared Z64/q64 infrastructure but literal noise identity remains open")


if __name__ == "__main__":
    main()
