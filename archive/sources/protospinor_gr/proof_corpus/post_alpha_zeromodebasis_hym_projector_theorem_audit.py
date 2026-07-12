from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_zeromodebasis_hym_projector_theorem_certificate.json"
STATUS = "POST_ALPHA_ZEROMODEBASIS_HYM_PROJECTOR_THEOREM_PROVED_PAYLOAD_OPEN"
NEXT = "Selected_U1Y_RouteC_HYM_Projector_Source_Payload_Fill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def all_nulls(obj: object) -> bool:
    if isinstance(obj, dict):
        return all(all_nulls(value) for value in obj.values())
    return obj is None


def projector_values_absent(payload: dict) -> bool:
    return all(
        all(
            section[key] is None
            for key in [
                "idempotent",
                "projector_matrix",
                "selected_by_same_source",
                "self_adjoint_for_selected_Gram",
                "zero_mode_projector",
            ]
        )
        for section in payload["required_payload"]["sector_projectors"].values()
    )


def basis_values_absent(payload: dict) -> bool:
    return all(
        all(
            section[key] is None
            for key in ["Gram_matrix", "basis_vectors", "orientation_or_ordering_rule", "trace_normalization"]
        )
        for section in payload["required_payload"]["ordered_zero_mode_bases_K_s"].values()
    )


def end0_action_values_absent(payload: dict) -> bool:
    return all(
        all(
            section[key] is None
            for key in ["bracket_preserving", "preserves_K_s", "rho_s_T1", "rho_s_T2", "rho_s_T3", "same_source_action"]
        )
        for section in payload["required_payload"]["End0_action_on_zero_modes"].values()
    )


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["selected_projector_payload_filled"] is False, "payload must be open")
    require(cert["selected_zero_mode_bases_emitted"] is False, "K_s must be open")
    require(cert["selected_source_map_rho_s_emitted"] is False, "rho_s must be open")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    rule = packet["promotion_rule"]
    require("K_s=im(P_s)" in rule["rho_s_definition"], "rho_s definition should use K_s")
    require(rule["matter_sector_result"] == "Q,u,d,L,e,N become selected adjoint triplet carriers", "wrong matter result")
    require(rule["H_sector_result"] == "H becomes the selected trivial singlet carrier", "wrong H result")

    payload = packet["payload_contract"]
    require(payload["status"] == "OPEN_VALUES_REQUIRED", "payload should be open")
    require(len(payload["accepted_source_families"]) == 3, "wrong source family count")
    require(payload["reference_model_values"]["End0_basis"] == ["T1", "T2", "T3"], "wrong End0 basis")
    require(payload["reference_model_values"]["sector_order"] == ["Q", "u", "d", "L", "e", "N", "H"], "wrong sector order")
    require(payload["required_payload"]["same_source_id"] is None, "same source should be absent")
    require(payload["required_payload"]["selected_HYM_or_typed_projector_certificate"] is None, "projector certificate should be absent")
    require(projector_values_absent(payload), "projector values should be absent")
    require(basis_values_absent(payload), "basis values should be absent")
    require(end0_action_values_absent(payload), "rho values should be absent")
    require(all_nulls(payload["required_payload"]["coherence_checks"]), "coherence checks should be absent")

    sm = packet["sm_bridge_support"]
    require(sm["promotion_decision"]["bridge_theorem_closes"] is True, "SM bridge theorem should close")
    require(sm["promotion_decision"]["canonical_rho_candidate_promotes_now"] is False, "rho should not promote now")
    require(sm["promotion_decision"]["promotes_after_next_artifact_if_validator_passes"] is True, "next artifact should promote if it passes")

    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "same-source selected projectors" in note, "note missing essentials")

    print("AUDIT_PASS: zero-mode HYM/projector promotion theorem imported; selected payload remains open")


if __name__ == "__main__":
    main()
