from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_tt_projector_window_normalization_lemma_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(
        cert["status"] == "TT_PROJECTOR_WINDOW_STRUCTURE_SOURCED_SELECTED_NUMERIC_GAP_OPEN",
        "unexpected status",
    )

    source = cert["source_tests"]
    closed = cert["closed_structure"]
    effect = cert["effect_on_eta_gate"]
    remaining = cert["remaining_numeric_gate"]
    guards = cert["guardrails"]

    require(source["finite_projection_defines_Badm_filter"] is True, "Badm filter should be sourced")
    require(source["qg_defines_spt_factorization"] is True, "SPT factorization should be sourced")
    require(source["qg_defines_tau0_positive"] is True, "tau0 positivity should be sourced")
    require(source["qg_identifies_TT_operator_E"] is True, "TT operator E should be sourced")
    require(source["qg_identifies_projected_linearized_graviton_operator_on_TT"] is True, "projected TT operator should be sourced")
    require(source["qg_gives_numeric_lambda_star"] is False, "numeric lambda should remain open")
    require(source["qg_gives_numeric_tau0"] is False, "numeric tau0 should remain open")
    require(closed["structure_closed"] is True, "TT projector/window structure should close")
    require(effect["eta_interpreted_as_TT_Q_sector_lambda_star"] is True, "eta should be interpretable as TT Q-sector gap")
    require(effect["eta_numeric_selected"] is False, "eta numeric must remain open")
    require(effect["eta_equals_kappa_STF_rows"] is False, "eta must not equal kappa rows")
    require(effect["eta_equals_nil_or_z64"] is False, "eta must not equal nil/Z64")
    require(remaining["name"] == "Selected_TT_QSector_Spectral_Gap_Computation", "wrong remaining gate")
    require(guards["claims_numeric_eta"] is False, "must not claim numeric eta")
    require(guards["claims_tau0_numeric"] is False, "must not claim numeric tau0")
    require(guards["claims_physical_modal_gap"] is False, "must not claim physical gap")

    print("AUDIT_PASS: TT projector/window structure sourced; selected numeric gap remains open")


if __name__ == "__main__":
    main()
