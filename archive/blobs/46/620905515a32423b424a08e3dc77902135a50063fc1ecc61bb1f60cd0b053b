from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "q79_coherent_zero_mode_tt_source_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    tiers = cert["claim_tiers"]
    guards = cert["guardrails"]
    matrices = cert["exact_matrices"]

    require(all(cert["checks"].values()), "one or more coherent-zero-mode checks failed")
    require(
        cert["status"]
        == "Q79_GEOMETRIC_COHERENT_ZERO_MODE_TT_ROW_AND_UNIT_INTERNAL_RESIDUE_CLOSED_PHYSICAL_ACTION_AND_KAPPA_H_OPEN",
        "zero-mode status changed",
    )
    require(cert["topology"]["component_count"] == 1, "q79 branch is not connected")
    require(cert["topology"]["scalar_harmonic_dimension"] == 1, "scalar kernel rank changed")
    require(
        matrices["canonical_internal_zero_residue"] == [["1", "0"], ["0", "1"]],
        "unit internal residue lost",
    )
    require(
        matrices["gap_massless_residue"] == [["0", "0"], ["0", "0"]],
        "positive-gap channel acquired a massless residue",
    )
    require(tiers["geometric_coherent_zero_mode_TT_source_row"] == "CLOSED", "row not closed")
    require(tiers["canonical_internal_massless_residue"] == "CLOSED_UNIT", "residue not closed")
    require(tiers["one_selected_action_fuses_zero_and_gap_channels"] == "OPEN", "action fusion overclaim")
    require(tiers["physical_kappa_h_or_Newton_normalization"] == "OPEN", "Newton normalization overclaim")
    require(guards["claims_unit_internal_residue_fixes_Newton_constant"] is False, "metrology guard failed")
    require(guards["claims_selected_Lorentzian_action_closed"] is False, "action guard failed")
    require(guards["claims_full_GR_or_QG_closed"] is False, "full-QG guard failed")

    print(
        "AUDIT_PASS: the connected q79 Fu-Yau branch canonically emits the scalar "
        "zero-mode TT row with unit internal residue; action fusion and kappa_h remain open"
    )


if __name__ == "__main__":
    main()
