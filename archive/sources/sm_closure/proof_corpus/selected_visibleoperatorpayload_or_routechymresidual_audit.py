"""Audit visible operator payload or Route-C/HYM residual bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_visibleoperatorpayload_or_routechymresidual"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PIPELINE = PACKET_DIR / "routec_hym_pipeline_replay.packet.json"
VALUE_SEARCH = PACKET_DIR / "selected_value_search_replay.packet.json"
EXTRACTION = PACKET_DIR / "hym_operator_extraction_contract.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_operator_payload.packet.json"
CUTSET = PACKET_DIR / "connection_extraction_or_source_origin_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VisibleOperatorPayload_or_RouteCHYMResidual_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_VISIBLEOPERATORPAYLOAD_OR_ROUTEC_HYM_RESIDUAL_BUILT_EXTRACTION_CONTRACT_OPEN"
NEXT = "MTT_Selected_HYMConnectionExtraction_or_SourceOriginLemma_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    pipeline = load(PIPELINE)
    values = load(VALUE_SEARCH)
    extraction = load(EXTRACTION)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(pipeline["honest_mesh_metric_sector_pass"] is True, "honest mesh/metric/sector support missing")
    require(pipeline["honest_operator_pipeline_pass"] is False, "honest operator pipeline overpassed")
    require(pipeline["lifted_flags_operator_pipeline_pass"] is True, "lifted flags diagnostic missing")
    require(pipeline["actual_selected_route_c_values_supplied"] is False, "selected Route-C values overclaimed")
    require(
        pipeline["actual_selected_D_E_dotD_Riesz_Green_supplied"] is False,
        "D_E/Riesz/Green/dotD overclaimed",
    )
    require(pipeline["selected_source_verified"] is False, "selected source oververified")
    require(pipeline["primitive_C1_contractions_supplied"] is False, "C1 contractions overclaimed")

    require(values["zero_residual_smoke_exists"] is True, "zero residual smoke missing")
    require(values["zero_residual_smoke_promoted"] is False, "zero residual smoke overpromoted")
    require(values["selected_values_closed"] is False, "selected values overclosed")
    require(values["selected_source_origin_found"] is False, "source origin overfound")
    require(values["selected_D_E_dotD_Riesz_Green_closed"] is False, "selected operator values overclosed")
    require(values["last_remaining_lemma"]["currently_proved"] is False, "last lemma overproved")
    require("RouteCSelectedSourceOriginLemma" == values["last_remaining_lemma"]["name"], "last lemma mismatch")

    require(extraction["abstract_HYM_import"]["selected_equalradius_HYM_existence"] is True, "abstract HYM bridge missing")
    require(extraction["selected_operator_values_closed"] is False, "operator values overclosed")
    require(extraction["actual_extraction_theorem_supplied"] is False, "extraction theorem overclaimed")
    require(extraction["actual_visible_operator_payload_emitted"] is False, "visible operator payload overemitted")
    require(extraction["accepted_as_actual_QaSU3_packet"] is False, "Qa/SU3 packet overaccepted")
    require(extraction["accepted_for_true_SM_equivalence"] is False, "true equivalence overaccepted")
    require(
        "lifted selected flags prove schema sufficiency only" in extraction["lifted_flag_diagnostic"]["guardrail"],
        "lifted flag guardrail missing",
    )
    for validator in ["de_action", "dotd_response", "reduced_green", "riesz_gap"]:
        require(extraction["lifted_flag_diagnostic"]["validators"][validator]["pass"] is True, f"lifted {validator} not passing")
    for validator in ["de_action", "dotd_response", "reduced_green", "riesz_gap", "route_c_residuals"]:
        require(
            extraction["validator_results_on_honest_smoke"][validator]["pass"] is False,
            f"honest {validator} overpassed",
        )

    require(
        promotion["route_A_visible_operator_payload"]["D_E_Riesz_Green_dotD_payload_emitted"] is False,
        "promotion overemitted operator payload",
    )
    require(promotion["route_B_routec_hym_residual"]["honest_operator_pipeline_pass"] is False, "promotion overpassed pipeline")
    require(promotion["route_B_routec_hym_residual"]["lifted_flags_operator_pipeline_pass"] is True, "promotion missing lifted diagnostic")
    require(promotion["route_B_routec_hym_residual"]["finite_operator_extraction_required"] is True, "promotion missing extraction requirement")
    require(promotion["true_SM_equivalence_closed"] is False, "promotion true equivalence overclosed")
    require(promotion["no_knob_closed"] is False, "promotion no-knob overclosed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    for required in [
        "prove RouteCSelectedSourceOriginLemma for q79/F,m=1",
        "extract a transition/connection representative for the selected HYM connection",
        "derive rho_E and metric tables from that connection, not smoke fixtures",
        "derive D_E action matrices and stiffness matrices from the same connection",
        "derive Riesz projectors, complement gaps, and reduced Green operators with truncation proof",
        "derive dotD_alpha1 as the same-branch derivative",
    ]:
        require(required in cutset["remaining_minimal_payloads"], f"cutset missing: {required}")

    require(data["closure_decision"]["finite_operator_extraction_contract_active"] is True, "candidate extraction contract missing")
    require(data["closure_decision"]["visible_operator_payload_emitted"] is False, "candidate visible payload overemitted")
    require(data["closure_decision"]["routec_hym_residual_promoted"] is False, "candidate residual overpromoted")
    require(data["closure_decision"]["actual_QaSU3_packet_promoted"] is False, "candidate Qa/SU3 overpromoted")
    require(cert["finite_operator_extraction_contract_active"] is True, "certificate extraction contract missing")
    require(cert["actual_QaSU3_packet_promoted"] is False, "certificate Qa/SU3 overpromoted")
    require("lifted flags are not values" in note, "note missing lifted-flag guardrail")

    for packet in [pipeline, values, extraction, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
