"""Audit physical dotD / sector-routing bridge after selected HYM first solve."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicaldotd_sectorrouting_after_hymfirstsolve"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_DECISION = PACKET_DIR / "physical_dotd_sector_routing_route_decision.packet.json"
PROJECTOR_PROGRESS = PACKET_DIR / "hym_projector_value_progress_after_first_solve.packet.json"
PROMOTION_KERNEL = PACKET_DIR / "selected_projector_source_promotion_kernel.packet.json"
CUTSET = PACKET_DIR / "phifin_trace_or_full_strominger_operator_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalDotD_SectorRouting_AfterHYMFirstSolve_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHYSICALDOTD_SECTORROUTING_AFTER_HYMFIRSTSOLVE_BUILT_PROJECTOR_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    route = load(ROUTE_DECISION)
    progress = load(PROJECTOR_PROGRESS)
    promotion = load(PROMOTION_KERNEL)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(route["after_first_solve"]["selected_diagonal_HYM_first_solve_closed"] is True, "first solve not imported")
    require(route["after_first_solve"]["rank2_End0_payload_closed"] is True, "End0 payload not imported")
    require(route["after_first_solve"]["physical_dotD_alpha1_closed"] is False, "physical dotD overclosed")
    require(route["route_A_naive_source_normalization"]["retired_for_naive_ext_scale"] is True, "naive alpha route not retired")
    require(route["route_B_sector_routing"]["primary"] is True, "sector route not primary")
    require(route["route_B_sector_routing"]["End0_functor_contract_specified"] is True, "End0 contract missing")
    require(route["route_B_sector_routing"]["existing_values_promoted"] is False, "existing values overpromoted")
    require(route["projector_bridge"]["bridge_theorem_proved"] is True, "projector bridge theorem missing")
    require(route["projector_bridge"]["selected_values_emitted"] is False, "projector bridge overemitted values")

    require(progress["finite_model_active_projector_values_emitted"] is True, "finite projectors not emitted")
    require(progress["all_projector_checks_pass"] is True, "projector checks failed")
    require(progress["End0_equivariance_on_emitted_projectors"] is True, "End0 equivariance missing")
    require(progress["positive_complement_gap"] is True, "positive gap missing")
    require(progress["complement_gap"] > 0.0, "gap not positive")
    require(progress["rho_candidate_promoted_to_selected_rho_s"] is False, "rho_s overpromoted")
    require(progress["selected_HYM_projector_values_promoted"] is False, "projectors overpromoted")
    require(progress["source_flags"]["de_action_selected_source_verified"] is False, "D_E selected flag overpromoted")
    require(progress["source_flags"]["dotd_selected_dotD_source_verified"] is False, "dotD selected flag overpromoted")
    require(progress["source_flags"]["dotd_alpha1_driver_verified"] is False, "alpha1 flag overpromoted")
    require(progress["sector_rank_summary"]["H"]["expected_rank"] == 1, "H rank mismatch")
    for sector in ["Q", "u", "d", "L", "e", "N"]:
        require(progress["sector_rank_summary"][sector]["expected_rank"] == 3, f"{sector} rank mismatch")
        require(progress["sector_rank_summary"][sector]["selected_source_verified"] is False, f"{sector} source oververified")

    route_a = promotion["route_A_source_promotion"]
    require(route_a["route_a_promotes_now"] is False, "Route A overpromoted")
    require(route_a["finite_value_side_closed"] is True, "finite value side not closed")
    require(route_a["PhiFin_selected_trace_emitted"] is False, "Phi_fin trace overemitted")
    require(route_a["honest_operator_flags_promote"] is False, "honest flags overpromoted")
    require(route_a["full_selected_operator_identified_with_BN_model_active"] is False, "BN equivalence overproved")
    route_b = promotion["route_B_matter_slot_charge"]
    require(route_b["structural_1M_rule_candidate_closed"] is True, "1M structural rule missing")
    require(route_b["selected_1M_Dirac_rule_closed"] is False, "1M rule overclosed")
    require(route_b["selected_sector_charge_closed"] is False, "sector charge overclosed")
    require(route_b["selected_transfer_normalization"] is False, "transfer normalization overclosed")
    require(route_b["selected_rho_s_emitted"] is False, "rho_s overemitted")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    require(cutset["bookkeeping_remaining"] is False, "bookkeeping incorrectly remains")
    require(cutset["source_or_value_emission_required"] is True, "source/value emission not required")
    for required in [
        "emit Phi_fin selected minimizer trace from the selected q79/F,m=1 HYM/Strominger source to finite B_N/projector data",
        "set selected_source_verified, selected_dotD_source_verified, and alpha1_driver_verified by theorem, not lifted flags",
        "promote finite projector values to selected P_s and ordered zero-mode bases K_s",
        "promote rho_candidate to selected rho_s and then physical sector dotD_alpha1",
    ]:
        require(required in cutset["remaining_minimal_payloads"], f"cutset missing: {required}")

    require(data["closure_decision"]["physical_dotD_alpha1_closed"] is False, "candidate physical dotD overclosed")
    require(data["closure_decision"]["finite_projector_values_emitted"] is True, "candidate missing finite projector values")
    require(data["closure_decision"]["finite_projector_values_promoted_to_selected"] is False, "candidate projectors overpromoted")
    require(data["closure_decision"]["PhiFin_selected_trace_emitted"] is False, "candidate Phi_fin overemitted")
    require(data["closure_decision"]["actual_QaSU3_operator_packet_promoted"] is False, "candidate Qa/SU3 overpromoted")
    require(cert["finite_projector_values_emitted"] is True, "certificate missing projector values")
    require(cert["PhiFin_selected_trace_emitted"] is False, "certificate Phi_fin overemitted")
    require("cannot be renamed physical alpha1" in note, "note missing alpha1 guardrail")

    for packet in [route, progress, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
