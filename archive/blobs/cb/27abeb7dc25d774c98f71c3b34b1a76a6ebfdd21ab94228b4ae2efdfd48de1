"""Audit pure-Weyl rows source-identity frontier / honest kernel export gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_pureweylrows_sourceidentityfrontier_or_honestkernelexport"
DATA = ROOT / "candidate_data"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
RECONCILIATION = PACKET_DIR / "retired_numeric_blockers_reconciliation.packet.json"
SOURCE_REDUCTION = PACKET_DIR / "pure_weyl_rows_source_identity_reduction.packet.json"
FINAL_ROUTES = PACKET_DIR / "final_two_route_after_pure_weyl.packet.json"
NEXT_ORDER = PACKET_DIR / "next_execution_order_after_source_identity_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PureWeylRows_SourceIdentityFrontier_or_HonestKernelExport_v1.md"
BUILDER = ROOT / "scripts" / "build_selected_pureweylrows_sourceidentityfrontier_or_honestkernelexport.py"

STATUS = (
    "MTT_SELECTED_PUREWEYLROWS_SOURCEIDENTITYFRONTIER_BUILT_NUMERIC_BLOCKERS_"
    "RETIRED_FINAL_TWO_ROUTE_OPEN"
)
NEXT = "MTT_Selected_HonestKernelExport_RowSourceFill_or_SourceIdentityDerivationAttempt_v1"


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
    reconciliation = load(RECONCILIATION)
    source_reduction = load(SOURCE_REDUCTION)
    final_routes = load(FINAL_ROUTES)
    next_order = load(NEXT_ORDER)
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
        ("reconciliation", reconciliation),
        ("source_reduction", source_reduction),
        ("final_routes", final_routes),
        ("next_order", next_order),
        ("certificate", cert),
    ]:
        guardrails(payload, label)

    require(
        reconciliation["status"]
        == "NUMERIC_AND_LINEAR_ALGEBRA_SUPPORT_MAXIMIZED_SOURCE_PROMOTION_OPEN",
        "reconciliation status mismatch",
    )
    old = reconciliation["old_blocker_reconciliation"]
    require(old["zero_mode_basis_values"]["model_active_values_emitted"] is True, "zero-mode values missing")
    require(
        old["zero_mode_basis_values"]["selected_HYM_source_promoted"] is False,
        "zero-mode source overpromoted",
    )
    require(old["dynamic_dotD_trace_binding"]["accepted"] is True, "dotD trace binding not retired")
    hessian = old["finite_Hessian_C1_source_blocks"]
    require(hessian["conditional_Gram"] == [[12.0, 0.0], [0.0, 12.0]], "Hessian Gram mismatch")
    require(hessian["conditional_A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(hessian["conditional_deltaTheta"] == [1.0, 1.0], "deltaTheta mismatch")
    require(hessian["no_linear_algebra_obstruction"] is True, "linear algebra obstruction not retired")
    require(hessian["selected_Hessian_b_source_emitted"] is False, "Hessian source overemitted")
    primitive = old["primitive_C1_contractions"]
    require(primitive["exact_72_rows_support_present"] is True, "72-row support missing")
    require(primitive["source_ordering_lemma_proved"] is False, "source-ordering overproved")
    require(primitive["pre_residual_normal_form_locked"] is True, "pre-residual normal form missing")
    require(primitive["route_A_validator_passes"] is False, "Route A overvalidated")
    require(primitive["route_B_honest_quadrature_emitted"] is False, "Route B overemitted")
    require(old["sector_rows"]["conditional_full_RouteB_validator_passes"] is True, "conditional Route-B fail")
    require(old["sector_rows"]["unpatched_RouteB_validator_passes"] is False, "unpatched Route-B overpassed")

    require(
        source_reduction["status"] == "PURE_WEYL_ROWS_REDUCED_TO_SOURCE_IDENTITY_OR_HONEST_EXPORT",
        "source reduction status mismatch",
    )
    boundary = source_reduction["patched_local_principle_boundary"]
    require(boundary["patched_spine_closure_claimed"] is True, "patched sufficiency missing")
    require(
        boundary["strict_110row_validator_passes_under_principle"] is True,
        "patched validator missing",
    )
    require(
        boundary["unpatched_SelectedFiniteC1SourceIdentityTheorem"] is False,
        "unpatched source identity overclaimed",
    )
    require(boundary["use_as_full_no_knob_proof"] is False, "local principle used as no-knob proof")
    unpatched = source_reduction["unpatched_requirements"]
    require(
        unpatched["derive_SelectedFiniteC1SourceIdentityPrinciple"] is False,
        "source identity overderived",
    )
    require(
        unpatched["emit_honest_independent_110row_kernel_export"] is False,
        "honest export overemitted",
    )
    require(unpatched["required_independent_rows"]["total"] == 110, "110 row count mismatch")
    require(source_reduction["pure_weyl_rows_unpatched_emitted"] is False, "pure rows overemitted")
    require(
        source_reduction["pure_weyl_rows_closed_under_local_principle_only"] is True,
        "local sufficiency not recorded",
    )

    require(final_routes["status"] == "TWO_LEGAL_FINISHING_ROUTES_OPEN", "final route status mismatch")
    require(
        final_routes["route_A_source_identity_derivation"]["current_status"] is False,
        "Route A overclosed",
    )
    require(
        final_routes["route_B_honest_independent_kernel_export"]["current_status"] is False,
        "Route B overclosed",
    )
    require(
        "use the local source identity principle as an unpatched proof"
        in final_routes["forbidden_closure_routes"],
        "local-principle guard missing",
    )
    require(
        "treat model-active zero-mode values as selected HYM/Strominger values without provenance"
        in final_routes["forbidden_closure_routes"],
        "zero-mode provenance guard missing",
    )

    require(
        next_order["status"] == "NEXT_ATTACK_SOURCE_IDENTITY_FIRST_HONEST_EXPORT_FALLBACK",
        "next order status mismatch",
    )
    require(next_order["recommended_next"]["artifact"] == NEXT, "next artifact mismatch")
    require("honest independent 110-row kernel export" in next_order["recommended_next"]["reason"], "next reason mismatch")

    closed = candidate["what_closes_now"]
    require(closed["old_zero_mode_hessian_primitive_wording_reconciled"] is True, "old wording not reconciled")
    require(closed["dynamic_dotD_trace_binding_retired_as_blocker"] is True, "dotD not retired")
    require(closed["numeric_and_linear_algebra_obstruction_retired"] is True, "numeric blocker not retired")
    require(closed["local_principle_sufficiency_boundary_recorded"] is True, "local boundary missing")
    require(closed["final_two_legal_routes_identified"] is True, "final routes missing")

    remaining = candidate["what_remains_open"]
    for key in [
        "SelectedFiniteC1SourceIdentityPrinciple_unpatched",
        "honest_independent_110row_kernel_export",
        "pure_Weyl_rows_unpatched_source_promotion",
        "lambda_representative_or_coexistence_after_rows",
        "selected_second_order_physical_matrices",
        "accepted_Yukawa_CKM_PMNS_mass_value_rows",
        "true_SM_equivalence",
        "full_no_knob_closure",
    ]:
        require(remaining[key] is True, f"remaining gate overclosed: {key}")

    decision = candidate["closure_decision"]
    require(decision["pure_Weyl_rows_emitted_unpatched"] is False, "pure rows overemitted")
    require(decision["patched_local_principle_suffices_conditionally"] is True, "patched sufficiency missing")
    require(decision["source_identity_unpatched_derived"] is False, "source identity overderived")
    require(decision["honest_kernel_export_emitted"] is False, "honest export overemitted")
    require(decision["selected_second_order_physical_matrices_promoted"] is False, "matrices overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")

    require("conditional Route-B validator passes       : true" in note, "note missing conditional pass")
    require("unpatched source identity derived          : false" in note, "note missing source guard")
    require("honest independent kernel export emitted   : false" in note, "note missing export guard")
    require("pure Weyl rows emitted unpatched           : false" in note, "note missing pure-row guard")
    require("110 rows" in note, "note missing 110-row target")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
