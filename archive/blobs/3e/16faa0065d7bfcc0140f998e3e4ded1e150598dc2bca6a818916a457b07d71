from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_c1_orthogonal_completion_or_independent_hessian_solve_certificate.json"
STATUS = "POST_ALPHA_C1_ORTHOGONAL_COMPLETION_OR_INDEPENDENT_HESSIAN_SOLVE_IMPORTED_VARIATIONAL_REDUCTION_OPEN"
NEXT = "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(cert["theorem"]["proved"] is True, "variational reduction theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["variational_euler_projection_derived"] is True, "Euler projection missing")
    require(decision["selected_C1_defect_functional_open"] is True, "defect functional should be open")
    require(decision["physical_PhiFinC1_minimization_open"] is True, "PhiFin minimization should be open")
    require(decision["independent_quadrature_data_open"] is True, "quadrature data should be open")
    require(decision["frontier_is_C1_defect_functional_source_or_independent_quadrature_data_fill"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    variational = packet["orthogonal_completion_variational_derivation"]
    require(variational["status"] == "EULER_PROJECTION_DERIVED_SELECTED_FUNCTIONAL_OPEN", "wrong variational status")
    require(all(variational["derived_inside_this_gate"].values()), "derived flags missing")
    require(all(variational["not_derived_inside_this_gate"].values()), "open flags missing")
    require(variational["candidate_functional"]["name"] == "C1DefectLeakageFunctional", "functional name drift")

    quadrature = packet["independent_quadrature_hessian_solve_spec"]
    require(quadrature["status"] == "NUMERICAL_SOLVE_SPEC_READY_DATA_MISSING", "wrong quadrature status")
    require(quadrature["run_now"] is False, "quadrature solve overclaimed")
    require(quadrature["acceptance_tests"]["A_shape"] == [72, 2], "A shape drift")
    require(quadrature["acceptance_tests"]["b_shape"] == [72], "b shape drift")
    require(len(quadrature["required_values"]) == 6, "required value count drift")

    sufficiency = packet["principle_or_solve_sufficiency_replay"]
    require(sufficiency["status"] == "SUFFICIENCY_PROVED_ANTECEDENT_OPEN", "wrong sufficiency status")
    require(sufficiency["antecedent_met_now"] is False, "antecedent overclaimed")
    require(sufficiency["current_replay_values"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong Gram")
    require(sufficiency["current_replay_values"]["A_transpose_b"] == [12.0, 12.0], "wrong ATb")
    require(sufficiency["current_replay_values"]["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")
    require(STATUS in note and NEXT in note and "variational source" in note, "note missing essentials")
    print("AUDIT_PASS: C1 orthogonal-completion/independent Hessian solve reduction imported; selected source remains open")


if __name__ == "__main__":
    main()
