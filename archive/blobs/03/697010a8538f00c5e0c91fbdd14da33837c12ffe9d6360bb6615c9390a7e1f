"""Audit End0 model packet and ordinary/projective no-go import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "end0_model_packet_and_projective_nogo_import.candidate.json"
CERT = ROOT / "certificates" / "end0_model_packet_and_projective_nogo_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "End0_ModelPacket_and_ProjectiveNoGo_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_end0_model_packet_and_projective_nogo.py"

STATUS = "END0_MODEL_PACKET_IMPORTED_PROJECTIVE_ORDINARY_FUNCTOR_NOGO_OPEN"
NEXT = "MTT_Selected_GerbeTwisted_End0_SectorFunctor_or_PhysicalAlpha1_SourceTheorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(all(data["checks"].values()), "not all checks passed")

    model = data["model_packet_summary"]
    require(model["domain_basis"] == ["T1", "T2", "T3"], "domain basis mismatch")
    require(model["rank_match"]["direct_sum_total_rank"] == 19, "rank total mismatch")
    require(model["rank_match"]["matches_expected_sector_kernel_rank_sum"] is True, "rank sum mismatch")
    require(model["rank_match"]["six_matter_triplets_plus_H_singlet"] == "6*3+1", "sector shape mismatch")
    require(model["sector_T3_response_norms"]["H"]["zero_response"] is True, "H should have zero response")
    for sector in ["Q", "u", "d", "L", "e", "N"]:
        require(model["sector_T3_response_norms"][sector]["rank"] == 3, f"{sector} rank mismatch")
        require(model["sector_T3_response_norms"][sector]["frobenius_norm"] == 1.4142135623730951, f"{sector} norm mismatch")

    qa = data["qa_end0_model_packet"]
    require(qa["decision"]["End0_domain_values_filled"] is True, "End0 domain not filled")
    require(qa["decision"]["End0_tensor_product_carrier_constructed"] is True, "End0 carrier missing")
    require(qa["decision"]["selected_zero_mode_bases_emitted"] is False, "zero modes overemitted")
    require(qa["decision"]["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD overextracted")

    obstruction = data["projective_obstruction"]
    require(obstruction["closed"] is True, "projective obstruction not closed")
    require(obstruction["type"] == "ordinary-vs-projective equivariance cocycle mismatch", "obstruction type mismatch")
    require(obstruction["numerical_gap_from_ordinary_phase"] > 1.7, "projective gap too small")
    gr = data["gr_ordinary_projective_nogo"]
    require(gr["projective_BN_target"]["cocycle_nontrivial"] is True, "BN cocycle not nontrivial")
    require(gr["attempted_positive_functor"]["ordinary_End0_to_current_BN_sector_functor_proved"] is False, "ordinary functor overproved")

    sm = data["sm_end0_packet"]
    require(sm["existing_value_tests"]["passes"] is False, "existing values accepted unexpectedly")
    require(sm["existing_value_tests"]["bn_rejected_as_selected_End0_basis"] is True, "BN basis not rejected")
    require(sm["decision"]["selected_End0_to_sector_functor_values_extracted"] is False, "SM End0 values overextracted")

    closes = data["what_closes_now"]
    for key in [
        "canonical_End0_model_packet_constructed",
        "sector_projector_model_constructed",
        "rank_19_six_triplet_plus_H_singlet_shape_closed",
        "ordinary_End0_to_current_BN_functor_no_go",
        "projective_cocycle_obstruction_imported",
        "positive_routes_reduced_to_gerbe_twisted_or_physical_alpha1",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "gerbe_twisted_End0_to_BN_sector_functor",
        "operator_level_projective_source_promotion",
        "physical_dotD_alpha1_source_values",
        "selected_zero_mode_bases_K_s",
        "selected_transfer_normalization",
        "A_selected",
        "b_selected",
    ]:
        require(remains[key] is True, f"remaining flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_selected_End0_to_sector_functor_values",
        "claims_ordinary_End0_to_current_BN_functor",
        "claims_physical_dotD_alpha1_payload",
        "claims_selected_transfer_normalization",
        "claims_A_selected_or_b_selected",
        "claims_Yukawa_or_full_SM_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("concrete model packet" in note, "note missing model packet")
    require("ordinary End0-to-current-BN functor is rejected" in note, "note missing no-go")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
