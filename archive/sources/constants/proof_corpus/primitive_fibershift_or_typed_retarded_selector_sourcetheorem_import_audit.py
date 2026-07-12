"""Audit primitive fiber-shift or typed-retarded-selector source theorem import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "primitive_fibershift_or_typed_retarded_selector_sourcetheorem_import.candidate.json"
CERT = ROOT / "certificates" / "primitive_fibershift_or_typed_retarded_selector_sourcetheorem_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_primitive_fibershift_or_typed_retarded_selector_sourcetheorem.py"

STATUS = "PRIMITIVE_FIBERCLASS_QUOTIENT_IMPORTED_HIGHERORDER_FULLRESPONSE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


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

    selected = data["selected_primitive_class"]
    require(selected["selected_active_shift"] == [1, 1], "active shift mismatch")
    require(selected["fixed_fiber_class"] == [0, 1, 2], "fiber class mismatch")
    require(selected["representative_for_computation"] == "fiber_shift_0", "representative mismatch")
    require(selected["absolute_fiber_shift_selected"] is False, "absolute fiber shift overclaimed")
    require(selected["selected_current_C1_observable_class"] is True, "observable class not selected")
    require(selected["selected_matrix_representative"] is False, "matrix representative overclaimed")
    require(
        selected["current_layer_flavor_splitting_possible"] is False,
        "flavor splitting overclaimed",
    )

    for shift, sectors in data["invariant_spectral_observables"].items():
        require(shift in ["0", "1", "2"], "unexpected fiber shift")
        for sector in ["u", "d", "e", "nuD"]:
            obs = sectors[sector]
            require(obs["rank"] == 3, f"{shift}/{sector} rank mismatch")
            require(obs["YYstar_is_scalar_identity"] is True, f"{shift}/{sector} non-scalar")

    remains = data["what_remains_open"]
    for key in [
        "selected_higher_order_or_full_response_matrices",
        "selected_matrix_representative_for_full_C1_operator",
        "operator_level_basis_transport",
        "nondegenerate_yukawa_hierarchy",
        "CKM_PMNS_CP_from_selected_matrices",
        "selected_b_selected",
        "promote_conditional_A_to_A_selected",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    guardrails = data["guardrails"]
    require(guardrails["active_shift_selected_claimed"] is True, "active shift not claimed")
    require(guardrails["fiber_class_quotient_selected_claimed"] is True, "fiber quotient not claimed")
    require(guardrails["absolute_fiber_shift_selected_claimed"] is False, "absolute fiber overclaim")
    require(guardrails["selected_matrix_representative_claimed"] is False, "matrix overclaim")
    require(guardrails["A_selected_claimed"] is False, "A_selected overclaim")
    require(guardrails["b_selected_claimed"] is False, "b_selected overclaim")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
