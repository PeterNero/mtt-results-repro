"""Audit HYM connection extraction or source-origin lemma bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hymconnectionextraction_or_sourceoriginlemma"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_ORIGIN = PACKET_DIR / "source_origin_lemma_status.packet.json"
CONNECTION = PACKET_DIR / "hym_connection_extraction_status.packet.json"
DIAGONAL = PACKET_DIR / "diagonal_connection_payload_reuse.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_connection_extraction.packet.json"
CUTSET = PACKET_DIR / "newton_galerkin_or_rank2_sector_transfer_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYMConnectionExtraction_or_SourceOriginLemma_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HYMCONNECTIONEXTRACTION_OR_SOURCEORIGINLEMMA_BUILT_DIAGONAL_PAYLOAD_FULL_TRANSFER_OPEN"
NEXT = "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    source = load(SOURCE_ORIGIN)
    connection = load(CONNECTION)
    diagonal = load(DIAGONAL)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(source["fixed_sector_support_passes"] is True, "fixed sector support missing")
    require(source["strominger_selection_available"] is True, "Strominger selection missing")
    require(source["same_source_support_converges"] is True, "same-source support missing")
    require(source["finite_emission_morphism_present"] is False, "finite emission morphism overclosed")
    require(source["operator_payload_emitted"] is False, "operator payload overemitted")
    require(source["fully_proved"] is False, "source-origin lemma overproved")
    require(source["open_sublemma"] == "FiniteEmissionMorphismLemma", "open sublemma mismatch")

    require(connection["extraction_contract"]["name"] == "Selected_HYM_Connection_to_Finite_Operator_Extraction.v1", "extraction contract mismatch")
    require(connection["gauge_fixed_problem"]["formulated"] is True, "gauge-fixed problem not formulated")
    require(connection["finite_newton_galerkin_contract"]["built"] is True, "Newton/Galerkin contract missing")
    require(connection["finite_newton_galerkin_contract"]["values_emitted"] is False, "Newton/Galerkin values overemitted")
    require(connection["actual_gauge_fixed_connection_representative_emitted"] is False, "connection representative overemitted")
    require(connection["actual_finite_operator_payload_emitted"] is False, "finite operator payload overemitted")
    require(connection["rank2_to_sector_transfer_functor_closed"] is False, "rank2 transfer overclosed")
    require(connection["accepted_as_actual_QaSU3_packet"] is False, "Qa/SU3 packet overaccepted")

    require(diagonal["diagonal_metric_payload"]["closed"] is True, "diagonal metric not closed")
    require(diagonal["diagonal_connection_payload"]["closed"] is True, "diagonal connection not closed")
    require(diagonal["curvature_residual_payload"]["closed"] is True, "curvature residual not closed")
    require(diagonal["can_reuse_as_rank2_support"] is True, "diagonal support not reusable")
    require(diagonal["can_promote_to_full_sector_payload_now"] is False, "diagonal payload overpromoted")
    require(diagonal["operator_payload_boundary"]["validator_ready"] is False, "diagonal payload should not be validator-ready")
    require(diagonal["operator_payload_boundary"]["D_E_matrix_on_selected_End0_basis_extracted"] is False, "D_E overextracted")
    require(diagonal["operator_payload_boundary"]["Riesz_Green_dotD_payload_extracted"] is False, "spectral payload overextracted")

    require(promotion["route_A_source_origin"]["finite_emission_morphism_closed"] is False, "promotion overclosed Phi_fin")
    require(promotion["route_B_connection_extraction"]["gauge_fixed_connection_representative_emitted"] is False, "promotion overemitted connection")
    require(promotion["route_B_connection_extraction"]["finite_newton_galerkin_values_emitted"] is False, "promotion overemitted solve values")
    require(promotion["route_C_diagonal_payload_reuse"]["rank2_diagonal_metric_connection_extracted"] is True, "promotion missing diagonal payload")
    require(promotion["route_C_diagonal_payload_reuse"]["full_sector_payload_promoted"] is False, "promotion overpromoted full sector")
    require(promotion["true_SM_equivalence_closed"] is False, "promotion true equivalence overclosed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    for required in [
        "emit selected A_HYM or S/H coefficient vector in fixed gauge",
        "prove coercive gauge-fixed Jacobian/Hessian lower bound",
        "construct rank2-to-sector transfer functor or prove it unnecessary",
        "derive rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap data from the selected connection",
        "replay validators without lifted flags or smoke fixtures",
    ]:
        require(required in cutset["remaining_minimal_payloads"], f"cutset missing: {required}")

    require(data["closure_decision"]["source_origin_lemma_fully_proved"] is False, "candidate source-origin overproved")
    require(data["closure_decision"]["diagonal_rank2_payload_imported"] is True, "candidate missing diagonal support")
    require(data["closure_decision"]["full_sector_operator_payload_emitted"] is False, "candidate full sector overemitted")
    require(data["closure_decision"]["actual_QaSU3_packet_promoted"] is False, "candidate Qa/SU3 overpromoted")
    require(cert["diagonal_rank2_payload_imported"] is True, "certificate missing diagonal support")
    require(cert["full_sector_operator_payload_emitted"] is False, "certificate full sector overemitted")
    require("diagonal rank-2 support is not" in note, "note missing diagonal guardrail")

    for packet in [source, connection, diagonal, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
