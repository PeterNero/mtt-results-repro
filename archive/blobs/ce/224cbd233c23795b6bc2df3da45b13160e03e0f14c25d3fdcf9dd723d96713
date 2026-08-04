"""Audit typed B_N or primitive-response value-emission import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "typedbn_retarded_derivative_or_primitive_response_valueemission_import.candidate.json"
CERT = ROOT / "certificates" / "typedbn_retarded_derivative_or_primitive_response_valueemission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_typedbn_retarded_derivative_or_primitive_response_valueemission.py"

STATUS = "TYPEDBN_OR_PRIMITIVE_RESPONSE_VALUEEMISSION_IMPORTED_SELECTOR_PROVENANCE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    summary = data["primitive_response_candidate_summary"]
    require(summary["active_shift"] == [1, 1], "active shift mismatch")
    require(summary["fixed_fiber_shifts"] == [0, 1, 2], "fixed fiber shifts mismatch")
    require(summary["rank_per_sector"] == 3, "rank per sector mismatch")
    require(summary["selected_emitted"] is False, "selected primitive response overclaimed")

    conditional = data["conditional_solver_packet"]
    require(conditional["conditional_weylpair_A_exact"] is True, "conditional A not exact")
    require(conditional["conditional_A_rank"] == 2, "conditional A rank mismatch")
    require(conditional["A_selected_claimed"] is False, "A_selected overclaimed")
    require(conditional["b_selected_claimed"] is False, "b_selected overclaimed")

    remains = data["what_remains_open"]
    for key in [
        "selected_primitive_fiber_shift",
        "selected_retarded_source_selector",
        "selected_typed_BN_retarded_derivative",
        "selected_primitive_or_vertex_response",
        "selected_b_selected",
        "alpha1_driver_verified",
        "promote_conditional_A_to_A_selected",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    guardrails = data["guardrails"]
    require(guardrails["primitive_response_candidate_values_emitted"] is True, "candidate values missing")
    require(guardrails["selected_primitive_response_emitted"] is False, "primitive response overclaim")
    require(guardrails["typed_retarded_derivative_emitted"] is False, "typed derivative overclaim")
    require(guardrails["A_selected_claimed"] is False, "A_selected overclaim")
    require(guardrails["b_selected_claimed"] is False, "b_selected overclaim")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
