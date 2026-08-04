from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_dynamic_c1_value_emission_cutset_certificate.json"
STATUS = "POST_ALPHA_DYNAMIC_C1_VALUE_EMISSION_CUTSET_IDENTIFIED_VALUES_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Tensor_HessianSourceMap_or_HonestGalerkinC1Execution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "cutset theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed import checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["frontier_is_selected_value_emission_cutset"] is True, "wrong frontier")
    require(decision["frontier_is_HYM_existence"] is False, "HYM existence should not reopen")
    require(decision["frontier_is_alpha1_driver"] is False, "alpha1 driver should not reopen")
    require(decision["frontier_is_conditional_rank2_arithmetic"] is False, "conditional arithmetic promoted")
    require(decision["frontier_is_observed_fit"] is False, "observed fit frontier not allowed")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    manifest = packet["strict_acceptance_manifest"]
    coords = manifest["coordinate_system"]
    require(coords["name"] == "fixed_72_real_C1_coordinate_system", "coordinate system drift")
    require(coords["sectors"] == ["u", "e", "d", "nuD"], "sector order drift")
    require(coords["total_real_coordinates"] == 72, "dimension drift")
    require(coords["real_coordinates_per_sector"] == 18, "per-sector coordinate drift")
    require(coords["per_sector_matrix_shape"] == [3, 3], "matrix-shape drift")
    require(manifest["A_selected_72_real_columns_required"] is True, "A requirement lost")
    require(manifest["b_selected_72_real_source_vector_required"] is True, "b requirement lost")
    require(manifest["sector_response_matrices_required"] is True, "sector matrices requirement lost")

    ref = packet["conditional_reference_arithmetic"]
    require(ref["reference_is_selected"] is False, "conditional arithmetic promoted")
    require(ref["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong reference A^T A")
    require(ref["A_transpose_b"] == [12.0, 12.0], "wrong reference A^T b")
    require(ref["deltaTheta_C1"] == [1.0, 1.0], "wrong reference DeltaTheta")
    require(ref["rank"] == 2, "rank reference drift")

    fields = packet["field_status"]
    require(fields["A_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED", "A status drift")
    require(fields["b_selected"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED", "b status drift")
    require(fields["deltaTheta_C1"] == "CONDITIONAL_REFERENCE_ONLY_NOT_SELECTED", "DeltaTheta status drift")
    require(fields["sector_response_matrices"] == "NOT_EMITTED_BY_SELECTED_VALUE_SOURCE", "sector response status drift")
    require(packet["conditional_nonscalar_support"]["promoted"] is False, "conditional nonscalar support promoted")

    required_cutset = {
        "selected primitive C1 tensor or differentiated Phi_fin^C1 source map",
        "selected Hessian/source vector b_selected or equivalent source coefficients",
        "sector response matrices in fixed 72-real coordinates",
        "honest selected Galerkin C1 execution values as replacement route",
    }
    require(set(packet["minimal_live_cutset"]) == required_cutset, "minimal live cutset drift")
    require("A^T A = 12 I_2" in note and STATUS in note and NEXT in note, "note missing essentials")
    print("AUDIT_PASS: dynamic C1 value-emission cutset imported; selected values remain open")


if __name__ == "__main__":
    main()
