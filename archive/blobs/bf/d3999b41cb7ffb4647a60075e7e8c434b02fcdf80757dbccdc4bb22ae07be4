"""Audit primitive fiber-shift or typed-retarded-selector source theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
CERT = ROOT / "certificates" / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_primitivefibershift_or_typedretardedselector_sourcetheorem.py"

STATUS = (
    "MTT_SELECTED_PRIMITIVEFIBERSHIFT_OR_TYPEDRETARDEDSELECTOR_"
    "SOURCETHEOREM_BUILT_FIBERCLASS_QUOTIENT_SELECTED_ABSOLUTE_SELECTOR_OPEN"
)
NEXT = "MTT_Selected_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


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

    typed = data["typed_retarded_selector"]
    require(typed["attempted"] is True, "typed selector not attempted")
    require(typed["selected"] is False, "typed selector overclaimed")

    primitive = data["primitive_selector"]
    require(primitive["active_shift_selected"] is True, "active shift not selected")
    require(primitive["selected_active_shift"] == [1, 1], "active shift mismatch")
    require(primitive["absolute_fiber_shift_selected"] is False, "absolute fiber shift overclaimed")
    require(
        primitive["fiber_class_quotient_selected_for_current_observables"] is True,
        "fiber quotient class not selected",
    )
    require(primitive["canonical_computation_representative"] == "fiber_shift_0", "wrong computation representative")
    require(
        primitive["canonical_representative_is_physical_selector"] is False,
        "computation representative treated as physical selector",
    )
    require(primitive["fixed_fiber_class"] == [0, 1, 2], "fixed fiber class mismatch")

    for shift, sectors in primitive["invariant_spectral_observables"].items():
        require(shift in ["0", "1", "2"], "unexpected shift in invariant observables")
        for sector in ["u", "d", "e", "nuD"]:
            values = sectors[sector]
            require(values["rank"] == 3, f"{shift}/{sector} rank mismatch")
            require(values["YYstar_is_scalar_identity"] is True, f"{shift}/{sector} not scalar")

    payload = data["observable_class_payload"]
    require(payload["selected_current_C1_observable_class"] is True, "observable class not selected")
    require(payload["selected_matrix_representative"] is False, "matrix representative overclaimed")
    require(payload["representative_for_computation"] == "fiber_shift_0", "wrong representative")
    require(payload["current_layer_flavor_splitting_possible"] is False, "flavor split overclaimed")
    require(payload["current_layer_no_go_imported"] is True, "current no-go not imported")

    closes = data["what_closes_now"]
    require(closes["active_shift_1_1_selected"] is True, "active shift close missing")
    require(
        closes["fixed_fiber_quotient_class_selected_for_current_C1_observables"] is True,
        "fiber quotient close missing",
    )
    require(closes["shift0_allowed_as_computation_gauge"] is True, "shift0 gauge not allowed")
    require(closes["absolute_fiber_origin_not_used_as_hidden_knob"] is True, "hidden knob guard missing")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["active_shift_selected_claimed"] is True, "active shift claim missing")
    require(data["fiber_class_quotient_selected_claimed"] is True, "fiber class claim missing")
    require(data["absolute_fiber_shift_selected_claimed"] is False, "absolute fiber shift overclaimed")
    require(data["typed_retarded_selector_claimed"] is False, "typed selector overclaimed")
    require(data["A_selected_claimed"] is False, "A_selected overclaimed")
    require(data["b_selected_claimed"] is False, "b_selected overclaimed")
    require(data["observed_data_used"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    remains = data["what_remains_open"]
    for key in [
        "absolute_fiber_origin_source_theorem",
        "typed_retarded_selector",
        "selected_matrix_representative_for_full_C1_operator",
        "operator_level_basis_transport",
        "selected_higher_order_or_full_response_matrices",
        "selected_b_selected",
        "promote_conditional_A_to_A_selected",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
