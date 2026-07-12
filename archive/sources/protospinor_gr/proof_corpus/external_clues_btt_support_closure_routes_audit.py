from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "external_clues_btt_support_closure_routes_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    clues = cert["internal_clues"]
    external = cert["external_clues"]
    routes = cert["routes"]
    best = cert["best_route"]
    decision = cert["decision"]
    guards = cert["guardrails"]

    require(
        cert["status"] == "EXTERNAL_CLUES_REDUCE_GATE_TO_EQUIVARIANT_CENTRAL_SELECTOR",
        "unexpected status",
    )
    require(clues["correct_adjoint_support_nonzero"] is True, "adjoint support nonzero clue missing")
    require(clues["exact_support_independence_no_go"] is True, "independence no-go missing")
    require(clues["z64_weight2_uniqueness_ready"] is True, "Z64 uniqueness missing")
    require(clues["central_unique_shared_channel"] is True, "central shared-channel clue missing")
    require(clues["qg_spin2_tt_projected_operator"] is True, "QG spin-2 TT clue missing")
    require(clues["finite_zero_mode_gravity_shadow"] is True, "finite zero-mode gravity clue missing")
    require(clues["kk_projection_zero_mode_equivalence"] is True, "KK zero-mode equivalence clue missing")
    require(clues["string_massless_spin2_universal_coupling"] is True, "string spin-2 clue missing")
    require(clues["b1_universal_geometry_coupling"] is True, "B1 universal coupling clue missing")

    require("weinberg_soft_graviton" in external, "Weinberg external clue missing")
    require("deser_self_interaction" in external, "Deser external clue missing")
    require("kk_zero_mode_logic" in external, "KK external clue missing")
    require("does not select Pi_exact64" in external["weinberg_soft_graviton"]["closure_power_for_mtt"], "Weinberg guard weakened")

    require(routes["R1_universal_spin2_bookkeeping_selector"]["closes_exact_support_now"] is False, "R1 must remain open")
    require(routes["R2_equivariant_central_character_selector"]["closes_exact_support_now"] is False, "R2 must remain open")
    require(routes["R3_zero_mode_shadow_plus_finite_helicity"]["closes_exact_support_now"] is False, "R3 must remain open")
    require(routes["R4_string_closed_bookkeeping_analogy"]["closes_exact_support_now"] is False, "R4 must remain open")
    require(routes["R5_direct_matrix_reconstruction"]["closes_exact_support_now"] is False, "R5 must remain open")

    require(best["name"] == "R2_equivariant_central_character_selector", "wrong best route")
    require(best["new_theorem_to_write"] == "EquivariantCentralCircleTTSupportTheorem.v1", "wrong next theorem")
    require("central-circle U(1)" in best["statement"], "best theorem statement weakened")

    require(decision["exact_support_proved_now"] is False, "must not claim exact support is proved")
    require(decision["support_premise_replaced_by_sharper_theorem"] is True, "must sharpen premise")
    require("equivariance/same-angle" in decision["why_not_closed"], "decision should name remaining gate")

    require(guards["uses_external_sources_as_inspiration_only"] is True, "external source guard missing")
    require(guards["claims_weinberg_or_deser_selects_Z64"] is False, "must not overclaim external sources")
    require(guards["claims_KK_zero_mode_equals_k2_character"] is False, "must not conflate zero-mode and k=2")
    require(guards["uses_observed_GR_data"] is False, "must not use observed GR data")
    require(guards["adds_new_numeric_knob"] is False, "must not add numeric knob")

    require("R2 Equivariant Central-Character Selector" in note, "note should include best route")
    require("k=2` does not contradict zero-mode gravity" in note, "note should separate zero-mode and helicity")

    print("AUDIT_PASS: external clues reduce BTT support closure to equivariant central selector")


if __name__ == "__main__":
    main()
