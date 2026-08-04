"""Audit the q79 physical alpha1 source-normalization/value fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "prove_q79_selected_alpha1_tangent_or_retarded_overlap_kernel.py"
SCRIPT = (
    ROOT
    / "scripts"
    / "attempt_q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill.py"
)
CERT = (
    ROOT
    / "certificates"
    / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill_certificate.json"
)
CANDIDATE = (
    ROOT
    / "candidate_data"
    / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"
)
OUT_DIR = (
    ROOT
    / "candidate_data"
    / "q79_selected_physical_alpha1_source_normalization_or_end0_sector_routing_value_fill"
)
ROUTE_A = OUT_DIR / "route_a_naive_source_normalization_nogo.json"
ROUTE_B = OUT_DIR / "route_b_end0_sector_routing_reduction.open.json"
CONTRACT = OUT_DIR / "next_end0_sector_functor_value_packet_contract.open.json"
PAPER = (
    ROOT
    / "proof_corpus"
    / "Q79_Selected_Physical_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1.md"
)

STATUS = (
    "Q79_SELECTED_PHYSICAL_ALPHA1_VALUE_FILL_ATTEMPTED_"
    "NAIVE_SOURCENORM_NOGO_END0SECTOR_VALUES_OPEN"
)
NEXT = "Q79_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, ROUTE_A, ROUTE_B, CONTRACT, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    contract = load(CONTRACT)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must remain false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    require(
        cert["input_statuses"]["q79_alpha1_retarded_kernel"]["status"]
        == "Q79_SELECTED_ALPHA1_TANGENT_KERNEL_ANALYTIC_FORMULA_PROVED_SOURCE_VALUES_OPEN",
        "previous alpha1 kernel theorem not imported",
        failures,
    )
    require(
        cert["input_statuses"]["q79_visible_rank2_l2_appell_humbert"]["status"]
        == "VISIBLE_RANK2_L2_APPELL_HUMBERT_AUTOMORPHY_CONSTRUCTED_SELECTION_OPEN",
        "visible AH support not imported",
        failures,
    )
    require(
        cert["input_statuses"]["sm_alpha1_value_fill_attempt"]["status"]
        == "MTT_SELECTED_ALPHA1_VALUE_FILL_ATTEMPTED_SOURCE_NORMALIZATION_NOGO_SECTOR_ROUTING_VALUES_OPEN",
        "SM alpha1 value-fill attempt not imported",
        failures,
    )

    require(
        route_a["schema"] == "Q79RouteAExtScaleToAlpha1SourceNormalizationNoGo.v1",
        "route A schema wrong",
        failures,
    )
    require(route_a["closed_as_nogo"] is True, "route A no-go should be closed", failures)
    require(
        route_a["topological_support_present"] is True,
        "route A should import alpha1 topological support",
        failures,
    )
    require(
        route_a["central_shared_circle_retained"] is True,
        "route A should retain shared circle guardrail",
        failures,
    )
    require(
        route_a["naive_Ext_scale_to_alpha1_source_normalization_rejected"] is True,
        "naive source normalization must be rejected",
        failures,
    )
    require(
        route_a["does_not_vary_integral_c2_alpha1"] is True,
        "route A must keep Chern row fixed",
        failures,
    )
    require(
        "dotD_alpha1 := dotD[h_ext]" in route_a["forbidden_identification"],
        "route A forbidden identification missing",
        failures,
    )
    require(
        "does not vary the integral Chern/source row" in route_a["reason"],
        "route A reason should name integral Chern/source row",
        failures,
    )

    require(
        route_b["schema"] == "Q79RouteBEnd0ToSectorRoutingReduction.v1",
        "route B schema wrong",
        failures,
    )
    require(route_b["closed"] is False, "route B must remain open", failures)
    require(route_b["End0_row_response_available"] is True, "End0 response should be available", failures)
    require(
        route_b["same_basis_dotD_matrices_exist"] is True,
        "same-basis dotD matrices should exist as support",
        failures,
    )
    require(
        route_b["sector_projector_dotd_matrices_exist_conditionally"] is True,
        "sector projector/dotD support missing",
        failures,
    )
    require(
        route_b["conditional_weyl_transfer_exact"] is True,
        "conditional Weyl transfer should be exact",
        failures,
    )
    require(
        route_b["honest_bn_validator_fails_only_by_source_flags"] is True,
        "honest validator cutset should be source flags",
        failures,
    )
    for key in (
        "selected_sector_routing_closed",
        "selected_transfer_normalization_closed",
        "selected_End0_to_sector_functor_values_extracted",
        "physical_dotD_alpha1_payload_extracted",
        "values_promoted",
    ):
        require(route_b[key] is False, f"route B overclosed: {key}", failures)
    require(len(route_b["must_emit_next"]) == 7, "route B must-emit count wrong", failures)

    require(
        contract["schema"] == "Q79SelectedEnd0ToSectorFunctorSourceAndValuePacketContract.v1",
        "contract schema wrong",
        failures,
    )
    require(
        contract["status"] == "OPEN_SELECTED_END0_TO_SECTOR_FUNCTOR_VALUES_REQUIRED",
        "contract status wrong",
        failures,
    )
    require(contract["next_required_artifact"] == NEXT, "contract next wrong", failures)
    require(contract["domain"]["basis"] == ["T1", "T2", "T3"], "domain basis wrong", failures)
    require(contract["codomain"]["sector_slots"] == ["Q", "u", "d", "L", "e", "N", "H"], "sector slots wrong", failures)
    require(len(contract["required_fields"]) == 7, "contract required field count wrong", failures)
    require(len(contract["forbidden_shortcuts"]) == 4, "contract forbidden shortcut count wrong", failures)

    for key in (
        "alpha1_value_fill_attempted_on_both_legal_routes",
        "naive_Ext_scale_to_alpha1_source_normalization_rejected",
        "integral_Chern_source_row_kept_distinct_from_continuous_Ext_scale",
        "shared_circle_retained_as_degree_zero_guardrail",
        "End0_sector_route_reduced_to_exact_functor_value_packet",
        "q79_sm_support_imported_without_promotion",
        "target_fitting_excluded",
    ):
        require(cert["what_closes_now"][key] is True, f"close flag false: {key}", failures)

    for key in (
        "selected_End0_to_sector_functor_values",
        "selected_sector_charge_or_chirality_table",
        "selected_transfer_normalization",
        "selected_dotD_source_theorem",
        "same_branch_alpha1_driver_theorem",
        "sector_equality_from_selected_derivative_to_dotD_matrices",
        "honest_dotD_replay_without_lifted_flags",
        "selected_primitive_C1_contractions",
        "A_selected",
        "b_selected",
        "Yukawa_or_full_SM_closure",
    ):
        require(cert["what_remains_open"][key] is True, f"remaining flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    theorem = cert["theorem"]
    require(theorem["proved"] is True, "no-go/reduction theorem not proved", failures)
    require(theorem["closure_claimed"] is False, "theorem overclaims closure", failures)

    for phrase in (
        "Source-Normalization No-Go",
        "does not vary the integral Chern/source row",
        "shared circle stays in the degree-zero lane",
        "End0-to-sector functor",
        "values are not promoted",
        "selected End0-to-sector routing values extracted: `False`",
        "selected transfer normalization closed: `False`",
        "Validator flags that must be theorem-derived",
        "Q79PhysicalAlpha1SourceNormalizationOrEnd0SectorRoutingValueFillAttemptTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 physical alpha1 value-fill audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 physical alpha1 value-fill audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
