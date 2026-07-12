"""Audit typed B_N retarded-derivative or primitive-response value emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.candidate.json"
CERT = ROOT / "certificates" / "selected_typedbn_retardedderivative_or_primitiveresponse_valueemission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_typedbn_retardedderivative_or_primitiveresponse_valueemission.py"

STATUS = (
    "MTT_SELECTED_TYPEDBN_RETARDEDDERIVATIVE_OR_PRIMITIVERESPONSE_"
    "VALUEEMISSION_BUILT_PRIMITIVE_CANDIDATES_UNSELECTED"
)
NEXT = "MTT_Selected_PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_v1"


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
    require(data["next_required_artifact"] == NEXT, "candidate next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note does not record next artifact")

    typed = data["typed_retarded_lane"]
    require(typed["attempted"] is True, "typed lane not attempted")
    require(typed["selected_emitted"] is False, "typed derivative overclaimed")
    require(typed["partial_fill_closed"] is False, "typed partial fill unexpectedly closed")
    for field, values in typed["blocking_fields"].items():
        require(values["selected_emitted"] is False, f"typed lane {field} overemitted")
        require(values["theorem_derived"] is False, f"typed lane {field} theorem overclaimed")

    primitive = data["primitive_response_lane"]
    require(primitive["attempted"] is True, "primitive lane not attempted")
    require(primitive["candidate_values_emitted"] is True, "primitive candidates not emitted")
    require(primitive["selected_emitted"] is False, "selected primitive overclaimed")
    require(primitive["active_shift_forced"] is True, "active shift not confirmed")
    require(primitive["fixed_fiber_candidate_count"] == 3, "fixed fiber candidate count mismatch")
    require(primitive["all_fixed_fiber_candidates_rank_three"] is True, "rank-three condition failed")
    require(primitive["fiber_shift_selector_emitted"] is False, "fiber selector overclaimed")
    for candidate in primitive["fixed_fiber_candidates"]:
        require(candidate["primitive_active_shift"] == [1, 1], "primitive active shift mismatch")
        require(candidate["primitive_fiber_shift"] in [0, 1, 2], "primitive fiber shift mismatch")
        require(candidate["selected_by_theorem"] is False, "candidate selection overclaimed")
        for sector in ["u", "d", "e", "nuD"]:
            require(candidate["sector_ranks"][sector] == 3, f"{sector} rank mismatch")

    solver = data["conditional_solver_packet"]
    require(solver["conditional_weylpair_A_exact"] is True, "conditional A not exact")
    require(solver["conditional_A_rank"] == 2, "conditional A rank mismatch")
    require(solver["conditional_residual_norm"] < 1e-12, "conditional residual too large")
    require(solver["A_selected_claimed"] is False, "A_selected overclaimed")
    require(solver["b_selected_claimed"] is False, "b_selected overclaimed")

    alpha = data["alpha1_value_packet"]
    require(alpha["lambda_alpha1"] == 1.0, "lambda alpha1 changed")
    require(alpha["N_alpha1_h_ext"] == 1.0, "N alpha1 changed")
    require(alpha["tangent_residual_l2"] == 0.0, "tangent residual changed")
    require(alpha["selected_value_emitted"] is False, "alpha1 value overclaimed")
    require(alpha["alpha1_driver_verified"] is False, "alpha1 driver overclaimed")
    require(alpha["used_as_selector"] is False, "alpha1 value used as selector")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["typed_retarded_derivative_emitted"] is False, "typed derivative overclaimed")
    require(data["primitive_response_candidate_values_emitted"] is True, "candidate values not claimed")
    require(data["selected_primitive_response_emitted"] is False, "selected primitive overclaimed")
    require(data["A_selected_claimed"] is False, "A_selected overclaimed")
    require(data["b_selected_claimed"] is False, "b_selected overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    remains = data["what_remains_open"]
    for key in [
        "selected_typed_BN_retarded_derivative",
        "selected_retarded_source_selector",
        "selected_primitive_fiber_shift",
        "selected_primitive_or_vertex_response",
        "selected_b_selected",
        "promote_conditional_A_to_A_selected",
        "honest_selected_deltaTheta_C1_solve",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
