"""Audit dynamic overlap or C1-primitive source-emission import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "dynamic_overlap_or_c1primitive_source_emission_import.candidate.json"
CERT = ROOT / "certificates" / "dynamic_overlap_or_c1primitive_source_emission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "DynamicOverlap_or_C1Primitive_SourceEmission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_dynamic_overlap_or_c1primitive_source_emission.py"

STATUS = "DYNAMIC_OVERLAP_OR_C1PRIMITIVE_REDUCTION_IMPORTED_TYPED_DERIVATIVE_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1"


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

    cutset = data["dynamic_cutset"]
    for key, value in cutset["already_closed_or_reduced"].items():
        require(value is True, f"cutset item should be closed/reduced: {key}")
    require(len(cutset["remaining_minimal_objects"]) == 4, "remaining object count mismatch")

    lanes = data["lanes"]
    require(lanes["A_same_source_alpha1_strength"]["closed"] is False, "lane A overclosed")
    require(lanes["B_typed_retarded_derivative"]["closed"] is False, "lane B overclosed")
    require(lanes["C_selected_C1_primitive_or_vertex"]["closed"] is False, "lane C overclosed")
    require(
        lanes["C_selected_C1_primitive_or_vertex"]["conditional_weylpair_A_exact"] is True,
        "conditional Weyl-pair algebra not exact",
    )
    require(
        lanes["C_selected_C1_primitive_or_vertex"]["promote_to_A_selected"] is False,
        "A_selected overclaimed",
    )

    remains = data["what_remains_open"]
    for key in [
        "typed_BN_retarded_derivative_or_alpha1_source_strength",
        "selected_End0_to_sector_functor_values",
        "selected_dynamic_overlap_Hessian_normalization",
        "selected_primitive_or_vertex_response_values",
        "selected_b_selected",
        "honest_selected_deltaTheta_C1_solve",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    guardrails = data["guardrails"]
    require(guardrails["dynamic_kernel_emitted"] is False, "dynamic kernel overclaim")
    require(guardrails["selected_C1_primitive_emitted"] is False, "primitive overclaim")
    require(guardrails["A_selected_claimed"] is False, "A_selected overclaim")
    require(guardrails["b_selected_claimed"] is False, "b_selected overclaim")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
