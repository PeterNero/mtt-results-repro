from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_selected_source_typed_de_reduction_certificate.json"
STATUS = "POST_ALPHA_SELECTED_SOURCE_TYPED_DE_REDUCED_CONNECTION_WITNESS_OPEN"
NEXT = "Selected_U1Y_RouteC_TypedMonadCech_or_HYMConnectionWitness_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["selected_connection_witness_constructed"] is False, "witness must remain open")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    finite = packet["finite_connection_prefix"]
    require(finite["nonidentity_rhoE"]["nonidentity_projective_rhoE_candidate_built"] is True, "nonidentity rhoE candidate missing")
    require(finite["nonidentity_rhoE"]["selected_by_mtt"] is False, "rhoE must not be selected")
    require(finite["DE"]["D_E_matrix_on_27_mode_BN_emitted"] is True, "DE prefix missing")
    require(finite["dotD"]["dotD_alpha1_matrix_in_same_basis_emitted"] is True, "dotD prefix missing")
    require(finite["C1"]["primitive_C1_contraction_engine_built"] is True, "C1 engine missing")

    witness = packet["witness_search"]["selected_connection_witness_attempt"]
    require(witness["constructs_actual_selected_witness"] is False, "selected witness should not be constructed")
    require(all(value is None for value in witness["candidate_values"].values()), "witness values should be absent")
    smoke = packet["witness_search"]["routec_smoke_promotion_nogo"]
    require(smoke["verdict"]["constructs_selected_connection_witness"] is False, "smoke must not construct witness")
    require(smoke["selected_source_verified"] is False, "smoke selected source flag must remain false")

    monad = packet["monad_construction"]
    require(monad["status"] == "QA_SU3_MONAD_MAP_CONSTRUCTION_BLOCKED_SECTION_RING_OR_SOURCE_AUGMENTATION_REQUIRED", "wrong monad status")
    require(monad["gate_results"]["charge_compatibility"].startswith("PASS"), "charge compatibility should pass")
    require(monad["gate_results"]["actual_f_sections"].startswith("FAIL"), "f sections should be absent")
    require(monad["gate_results"]["actual_g_sections"].startswith("FAIL"), "g sections should be absent")

    automorphy = packet["automorphy_construction"]
    require(automorphy["status"] == "QA_SU3_IWASAWA_AUTOMORPHY_SECTION_RING_CONSTRUCTION_SYMBOLIC_ONLY_VALUES_OPEN", "wrong automorphy status")
    require(automorphy["symbolic_rank_one_relation"]["actual_closure_status"] == "SYMBOLIC_ONLY_MULTIPLICATION_CONSTANTS_AND_NONZERO_SECTIONS_OPEN", "symbolic relation should remain open")
    require(automorphy["gate_results"]["automorphy_cocycle"].startswith("FAIL"), "automorphy cocycle should be absent")

    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "typed f_i/g_i sections" in note, "note missing essentials")

    print("AUDIT_PASS: selected source/typed-DE reduced to explicit connection witness values")


if __name__ == "__main__":
    main()
