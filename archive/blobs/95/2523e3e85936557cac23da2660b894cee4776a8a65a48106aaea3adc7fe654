"""Audit pure Weyl coefficient rows / primitive C1 formula execution gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pureweylcoefficientrows_or_primitivec1formulaexecution"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
DECOMP = PACKET_DIR / "pure_weyl_row_algebraic_decomposition.packet.json"
IDENTITY_BOUNDARY = PACKET_DIR / "dynamic_identity_row_source_boundary.packet.json"
PRIMITIVE_CUTSET = PACKET_DIR / "primitive_c1_formula_execution_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PureWeylCoefficientRows_or_PrimitiveC1FormulaExecution_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_pureweylcoefficientrows_or_primitivec1formulaexecution.py"

STATUS = "MTT_SELECTED_PURE_WEYL_COEFFICIENT_ROWS_BUILT_IDENTITY_SUBTRACTION_BLOCKED_PRIMITIVE_EXECUTION_OPEN"
NEXT = "MTT_Selected_ZeroModeHessianPrimitiveRowExecution_or_PureWeylRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guardrails(payload: dict, label: str) -> None:
    require(payload["observed_data_used_as_selector"] is False, f"{label}: observed selector used")
    require(payload["target_fitting_used"] is False, f"{label}: target fitting used")
    require(payload["closure_claimed"] is False, f"{label}: closure overclaimed")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    decomp = load(DECOMP)
    identity = load(IDENTITY_BOUNDARY)
    cutset = load(PRIMITIVE_CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for label, payload in [
        ("candidate", candidate),
        ("decomp", decomp),
        ("identity", identity),
        ("cutset", cutset),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    require(
        decomp["status"] == "ALGEBRAIC_DECOMPOSITION_AVAILABLE_SELECTED_SOURCE_NOT_YET",
        "decomposition status mismatch",
    )
    require(decomp["algebraic_identities"]["phase_pure_Z"] == "Z = (I + Z) - I", "Z identity mismatch")
    require(decomp["algebraic_identities"]["shift_pure_X"] == "X = (I + X) - I", "X identity mismatch")
    require(decomp["dynamic_identity_row_required"] is True, "dynamic identity not marked required")
    require(decomp["dynamic_identity_row_emitted"] is False, "dynamic identity overemitted")
    require(decomp["identity_subtraction_promoted_as_selected_now"] is False, "identity subtraction overpromoted")

    require(
        identity["status"] == "STATIC_UNIT_NORMALIZATION_DOES_NOT_EMIT_DYNAMIC_C1_IDENTITY_ROW",
        "identity boundary status mismatch",
    )
    static = identity["static_support_closed"]
    require(static["smslot_all_six_arrows_closed"] is True, "SM-slot arrows not closed")
    require(static["selected_static_overlap_kernel"] is True, "static overlap kernel missing")
    require(static["selected_ext_unit_row_closed"] is True, "Ext unit row missing")
    require(static["selected_hodge_projector_row_closed"] is True, "Hodge projector missing")
    dynamic = identity["dynamic_payload_status"]
    require(dynamic["accepted_dynamic_payload_row_count"] == 0, "dynamic payload row count mismatch")
    require(dynamic["same_source_dynamic_payload_closed"] is False, "dynamic payload overclosed")
    require(dynamic["primitive_row_formula_executed"] is False, "primitive formula overexecuted")
    require(dynamic["selected_functional_executed"] is False, "selected functional overexecuted")
    require(dynamic["dynamic_identity_row_emitted"] is False, "dynamic identity overemitted")

    require(
        cutset["status"] == "PRIMITIVE_EXECUTION_REQUIRED_FOR_SELECTED_PURE_WEYL_ROWS",
        "cutset status mismatch",
    )
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(
        "selected dynamic C1 identity/unit row or an identity-free formula for pure Z/X"
        in cutset["must_emit"],
        "must-emit identity/formula row missing",
    )
    require(
        "subtract static identity or trace normalization as if it were a dynamic C1 row"
        in cutset["forbidden_shortcuts"],
        "forbidden shortcut missing",
    )

    closed = candidate["what_closes_now"]
    require(closed["pure_Z_X_algebraic_decomposition_recorded"] is True, "decomposition not closed")
    require(closed["identity_subtraction_shortcut_rejected"] is True, "shortcut not rejected")
    require(closed["static_unit_vs_dynamic_identity_boundary_built"] is True, "boundary not built")
    require(closed["primitive_execution_cutset_for_pure_weyl_rows_built"] is True, "cutset not built")

    remaining = candidate["what_remains_open"]
    for key in [
        "selected_dynamic_C1_identity_or_identity_free_pure_weyl_formula",
        "selected_zero_mode_basis_values",
        "selected_finite_Hessian_C1_source_blocks",
        "primitive_C1_contractions",
        "pure_Weyl_coefficient_rows_lambda_Z_lambda_X",
        "individual_lambda_representative_selection_or_coexistence",
        "selected_second_order_physical_matrix_promotion",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["pure_Weyl_rows_emitted"] is False, "pure rows overemitted")
    require(decision["identity_subtraction_promoted"] is False, "identity subtraction overpromoted")
    require(decision["primitive_C1_formula_executed"] is False, "primitive formula overexecuted")
    require(decision["individual_lambda_value_selected"] is False, "lambda overselected")
    require(decision["selected_second_order_physical_matrices_promoted"] is False, "matrices overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require("Z = (I + Z) - I" in note, "note missing Z identity")
    require("dynamic C1 identity row emitted        : false" in note, "note missing identity guard")
    require("identity subtraction promoted          : false" in note, "note missing subtraction guard")
    require("full SM closure                        : false" in note, "note missing closure guard")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
