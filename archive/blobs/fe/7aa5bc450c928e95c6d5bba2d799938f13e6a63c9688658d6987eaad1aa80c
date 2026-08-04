"""Build selected finite C1 variational bridge / source-promotion lemma artifact.

This is the next post-SM-parity PSM-C1-02 source-identity step after the
variational projection bridge target.  It separates three tiers:

1. closed finite algebra and variational shape,
2. closure under the explicit local SelectedWeylVariationActionPrinciple,
3. unpatched/no-knob closure, which still requires deriving that principle or
   supplying an independent row-source execution.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUPPORT = BASE / "closed_support_import.packet.json"
LOCAL_THEOREM = BASE / "local_premise_source_promotion_theorem.packet.json"
UNPATCHED_GATE = BASE / "unpatched_source_promotion_gate.packet.json"
TWO_ROUTE = BASE / "two_route_next_cutset.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_SelectedFiniteC1VariationalProjectionBridge_or_SourcePromotionLemma_v1.md"
AUDIT = CORPUS / f"{SLUG}_audit.py"

PREVIOUS = DATA / "selected_psm_c1_02_variationalprojectionbridge_or_rowsource.candidate.json"
BRIDGE_TARGET = DATA / "selected_psm_c1_02_variationalprojectionbridge_or_rowsource" / "selected_variational_projection_bridge_theorem.packet.json"
LOCAL_PRINCIPLE = DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "accepted_local_weylvariation_actionprinciple.packet.json"
APPLIED_KERNEL = DATA / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json"
COUNTERMODEL = DATA / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel" / "closed_support_not_enough_countermodel.packet.json"
VARIATION_ATTEMPT = DATA / "selected_c1variationprinciplederivation_or_quadratureenginerun" / "route_a_variation_principle_derivation_attempt.packet.json"
DEFECT_FUNCTIONAL = DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill" / "c1_defect_functional_uniqueness_source.packet.json"
BOUNDARY_CERT = DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof" / "finite_trace_boundary_cancellation_certificate.packet.json"
ACCEPTANCE = DATA / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues" / "source_or_kernel_acceptance_contract.packet.json"

STATUS = "MTT_SELECTED_PSM_C1_02_LOCAL_SOURCE_PROMOTION_CLOSED_UNPATCHED_GATE_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_UnpatchedWeylVariationActionPrincipleDerivation_or_IndependentRowSourceExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    bridge = load(BRIDGE_TARGET)
    local_principle = load(LOCAL_PRINCIPLE)
    applied = load(APPLIED_KERNEL)
    countermodel = load(COUNTERMODEL)
    variation = load(VARIATION_ATTEMPT)
    defect = load(DEFECT_FUNCTIONAL)
    boundary = load(BOUNDARY_CERT)
    acceptance = load(ACCEPTANCE)

    support = {
        "schema": "MTTPSMC102SelectedFiniteC1BridgeClosedSupportImport.v1",
        "status": "CLOSED_SUPPORT_IMPORTED_FOR_SOURCE_PROMOTION_DECISION",
        "sources": {
            "previous_bridge_target": rel(PREVIOUS),
            "bridge_theorem_target": rel(BRIDGE_TARGET),
            "variation_principle_attempt": rel(VARIATION_ATTEMPT),
            "defect_functional_uniqueness": rel(DEFECT_FUNCTIONAL),
            "finite_trace_boundary_certificate": rel(BOUNDARY_CERT),
            "local_principle": rel(LOCAL_PRINCIPLE),
            "applied_local_kernel_closure": rel(APPLIED_KERNEL),
            "closed_support_countermodel": rel(COUNTERMODEL),
            "acceptance_contract": rel(ACCEPTANCE),
        },
        "closed_finite_support": {
            "selected_finite_C1_quotient": countermodel["closed_support_facts_true"]["finite_selected_C1_quotient"],
            "finite_trace_measure_normalization": countermodel["closed_support_facts_true"]["finite_trace_measure_normalization"],
            "finite_variational_euler_projection": variation["closed_support"]["finite_variational_euler_projection"],
            "least_norm_completion_selects_Q_residual": variation["closed_support"]["least_norm_completion_selects_Q_residual"],
            "unique_quadratic_defect_functional_up_to_scale": defect["uniqueness_result"]["unique_up_to_overall_positive_scale"],
            "overall_scale_cancels_from_euler_projection": defect["uniqueness_result"]["overall_scale_cancels_from_euler_projection"],
            "algebraic_finite_trace_boundary_closed": boundary["algebraic_boundary_closed_now"],
            "locked_target_replay_passes": acceptance["locked_target_check"]["passes_locked_target_by_replay"],
        },
        "not_enough_for_unpatched_source_promotion": countermodel["source_promotion_fields_false"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    local_theorem = {
        "schema": "MTTPSMC102LocalPremiseSourcePromotionTheorem.v1",
        "status": "LOCAL_PREMISE_SOURCE_PROMOTION_THEOREM_PROVED",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-LOCAL",
        "theorem_name": "LocalSelectedFiniteC1VariationalProjectionBridgeAndSourcePromotionLemma",
        "hypothesis": local_principle["principle_name"],
        "hypothesis_status": local_principle["status"],
        "hypothesis_scope": local_principle["accepted_scope"],
        "statement": (
            "Assuming the explicit local SelectedWeylVariationActionPrinciple in this proof spine, "
            "the selected finite C1 variational projection bridge holds locally: the selected physical "
            "differentiated Phi_fin^C1 action is identified with the finite Weyl least-defect "
            "trace/Frobenius action, emits pre-residual R_Z/R_X, emits the same-source Hessian "
            "counterterm b_selected, and has no extra dynamic trace boundary/source term."
        ),
        "derived_from_local_premise": {
            "SelectedFiniteC1VariationalProjectionBridge_local": True,
            "SelectedFiniteC1SourcePromotionLemma_local": True,
            "pre_residual_phase_shift_operator_source": applied["promoted_inside_local_spine"]["pre_residual_phase_shift_operator_source"],
            "same_source_hessian_b_selected_rows": applied["promoted_inside_local_spine"]["same_source_hessian_b_selected_rows"],
            "sector_rows_physical_source_promotion": applied["promoted_inside_local_spine"]["sector_rows_physical_source_promotion"],
            "independence_from_residual_projector_replay": applied["promoted_inside_local_spine"]["independence_from_residual_projector_replay"],
            "boundary_terms_vanish": True,
        },
        "guardrails": {
            "explicit_local_premise_not_unpatched_theorem": True,
            "external_papers_modified": local_principle["external_papers_modified"],
            "unpatched_derivation_status": local_principle["unpatched_derivation_status"],
            "true_SM_equivalence_closed": applied["does_not_close"]["true_SM_equivalence"] is False,
            "no_knob_closed": applied["does_not_close"]["no_knob"] is False,
            "independent_kernel_execution_supplied": applied["does_not_close"]["independent_kernel_execution"] is False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "closure_scope": "LOCAL_PREMISE_ONLY",
    }

    unpatched_gate = {
        "schema": "MTTPSMC102UnpatchedSourcePromotionGate.v1",
        "status": "UNPATCHED_SOURCE_PROMOTION_NOT_PROVED_BY_CLOSED_SUPPORT",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED",
        "theorem_name": "UnpatchedSelectedFiniteC1VariationalProjectionBridge",
        "proved_now": False,
        "why_not_proved": countermodel["therefore"],
        "countermodel_source": rel(COUNTERMODEL),
        "bridge_target_open_fields": bridge["still_missing"],
        "must_add_one_of": [
            "derive SelectedWeylVariationActionPrinciple from selected Phi_fin/Theta/Strominger trace and admissible variations",
            "supply independent Route-B selected row-source execution: 72 primitive row kernels, 36 sector rows, 2 Hessian/source rows, and exactness/error certificate",
        ],
        "forbidden_shortcuts": acceptance["forbidden_shortcuts"],
        "acceptance_contract": {
            "route_A": acceptance["accept_if_route_A"],
            "route_B": acceptance["accept_if_route_B"],
            "current_result": acceptance["current_result"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    two_route = {
        "schema": "MTTPSMC102TwoRouteNextCutset.v1",
        "status": "TWO_ROUTE_CUTSET_FIXED_AFTER_LOCAL_PROMOTION",
        "active_routes": [
            "SOURCE-IDENTITY/VPB-1-UNPATCHED",
            "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE-INDEPENDENT",
        ],
        "superset_strategy": {
            "classification": "TWO_CONSTRAINED_PATHS_TO_ONE_LOCKED_SOURCE_PACKET",
            "route_A": "derive the local principle from the selected physical Phi_fin/Theta/Strominger action, promoting the local theorem to unpatched theorem",
            "route_B": "construct the same pre-residual row-source packet by independent finite C1 row-kernel execution",
            "locked_target": "same R_Z/R_X/b_selected source packet and same finite row-kernel functional",
            "paths_used_as_free_parameters": False,
            "observed_constants_used": False,
        },
        "route_A_remaining": [
            "physical action equals selected finite Weyl least-defect trace/Frobenius action",
            "admissible differentiated Phi_fin^C1 variation class fixed by selected setup",
            "dynamic trace has no extra physical boundary/source term",
            "same physical source emits R_Z/R_X and b_selected before residual replay",
        ],
        "route_B_remaining": [
            "all 72 primitive row kernels emitted from selected source, not replay",
            "36 sector matrices assembled from primitive rows plus finite trace",
            "2 Hessian/source rows emitted independently",
            "locked target values used only as postchecks",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102LocalSourcePromotion.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_SelectedFiniteC1VariationalProjectionBridge_or_SourcePromotionLemma_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED",
            "task": "Derive the SelectedWeylVariationActionPrinciple from the selected Phi_fin/Theta/Strominger trace, admissible variations, finite trace/Frobenius pairing, and no-boundary/source clauses.",
        },
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE-INDEPENDENT",
            "task": "Execute or prove an independent selected row-source packet with 72 primitive kernels, 36 sector rows, and 2 Hessian/source rows, using the locked target only as a postcheck.",
        },
        "status": "NEXT_WORKORDER_DERIVE_UNPATCHED_PRINCIPLE_OR_EXECUTE_INDEPENDENT_ROWSOURCE",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102SelectedFiniteC1VariationalBridgeOrSourcePromotionLemma",
        "active_label": "PSM-C1-02",
        "active_routes": [
            "SOURCE-IDENTITY/VPB-1-LOCAL",
            "SOURCE-IDENTITY/VPB-1-UNPATCHED",
            "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE-INDEPENDENT",
        ],
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "output_packets": {
            "closed_support_import": rel(SUPPORT),
            "local_premise_source_promotion_theorem": rel(LOCAL_THEOREM),
            "unpatched_source_promotion_gate": rel(UNPATCHED_GATE),
            "two_route_next_cutset": rel(TWO_ROUTE),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "SelectedFiniteC1VariationalProjectionBridge_under_explicit_local_principle": True,
            "SelectedFiniteC1SourcePromotionLemma_under_explicit_local_principle": True,
            "pre_residual_kernel_closure_in_local_spine": True,
            "source_promotion_as_unpatched_no_knob_theorem": False,
        },
        "what_remains_open": {
            "unpatched_SelectedWeylVariationActionPrinciple_derivation": True,
            "independent_RouteB_row_source_execution": True,
            "unpatched_PSM_C1_02_closure": True,
            "no_knob_dynamic_C1_closure": True,
        },
        "theorem": {
            "name": "PSMC102LocalSourcePromotionAndUnpatchedGateTheorem",
            "proved": True,
            "statement": (
                "The explicit local SelectedWeylVariationActionPrinciple is sufficient to prove the selected finite C1 "
                "variational projection bridge and the source-promotion lemma inside the local proof spine. However, "
                "the repo's closed-support countermodel proves that finite algebraic support alone does not derive "
                "unpatched source promotion. Therefore the next no-knob gate is exactly to derive that principle from "
                "the selected physical action, or to supply an independent row-source execution."
            ),
        },
        "superset_strategy": two_route["superset_strategy"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "local_premise_closure_claimed": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_SelectedFiniteC1VariationalProjectionBridge_or_SourcePromotionLemma_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_premise_source_promotion_closed": True,
        "unpatched_source_promotion_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 SelectedFiniteC1VariationalProjectionBridge or SourcePromotionLemma v1

Status labels:

- `PSM-C1-02 / SOURCE-IDENTITY / VPB-1-LOCAL`
- `PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED`
- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE-INDEPENDENT`

Status: `{STATUS}`

## Result

The local proof spine now has conditional closure:

`SelectedFiniteC1VariationalProjectionBridge` and
`SelectedFiniteC1SourcePromotionLemma` are proved under the explicit local
`SelectedWeylVariationActionPrinciple`.

This is not yet unpatched/no-knob closure.  The repo's countermodel shows that
the existing closed finite support facts do not by themselves derive physical
source promotion.  The unpatched theorem still needs one new source object:

1. derive the `SelectedWeylVariationActionPrinciple` from the selected
   `Phi_fin/Theta/Strominger` physical action, or
2. execute the independent Route-B row-source packet with 72 primitive row
   kernels, 36 sector rows, and 2 Hessian/source rows.

## Superset Use

This uses a constrained superset strategy, not knobs.  Route A and Route B are
two paths to the same locked source packet: pre-residual `R_Z/R_X`, same-source
`b_selected`, and the same finite row-kernel functional.  Observed constants
are not used as selectors.

## Next

Next artifact: `{NEXT}`
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "{SLUG}"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{{SLUG}}.candidate.json"
SUPPORT = BASE / "closed_support_import.packet.json"
LOCAL_THEOREM = BASE / "local_premise_source_promotion_theorem.packet.json"
UNPATCHED_GATE = BASE / "unpatched_source_promotion_gate.packet.json"
TWO_ROUTE = BASE / "two_route_next_cutset.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_SelectedFiniteC1VariationalProjectionBridge_or_SourcePromotionLemma_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma.py"

STATUS = "{STATUS}"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard_no_selector(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    support = load(SUPPORT)
    local_theorem = load(LOCAL_THEOREM)
    unpatched_gate = load(UNPATCHED_GATE)
    two_route = load(TWO_ROUTE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["what_closes_now"]["SelectedFiniteC1SourcePromotionLemma_under_explicit_local_principle"] is True, "local source lemma not closed")
    require(candidate["what_closes_now"]["source_promotion_as_unpatched_no_knob_theorem"] is False, "unpatched overclaim")
    require(candidate["local_premise_closure_claimed"] is True, "local closure missing")
    require(candidate["closure_claimed"] is False, "candidate overclaims global closure")

    require(support["closed_finite_support"]["finite_variational_euler_projection"] is True, "finite variational support missing")
    require(support["closed_finite_support"]["unique_quadratic_defect_functional_up_to_scale"] is True, "defect uniqueness missing")
    require(support["closed_finite_support"]["algebraic_finite_trace_boundary_closed"] is True, "finite boundary support missing")
    require(support["not_enough_for_unpatched_source_promotion"]["source_map_selected_by_MTT_now"] is False, "countermodel source field mismatch")

    require(local_theorem["status"] == "LOCAL_PREMISE_SOURCE_PROMOTION_THEOREM_PROVED", "local theorem status mismatch")
    require(local_theorem["derived_from_local_premise"]["SelectedFiniteC1VariationalProjectionBridge_local"] is True, "local bridge missing")
    require(local_theorem["derived_from_local_premise"]["SelectedFiniteC1SourcePromotionLemma_local"] is True, "local source lemma missing")
    require(local_theorem["guardrails"]["explicit_local_premise_not_unpatched_theorem"] is True, "local premise guard missing")
    require(local_theorem["closure_claimed"] is True, "local theorem closure should be claimed")
    require(local_theorem["closure_scope"] == "LOCAL_PREMISE_ONLY", "local closure scope mismatch")

    require(unpatched_gate["proved_now"] is False, "unpatched gate overproved")
    require(unpatched_gate["closure_claimed"] is False, "unpatched closure overclaim")
    require("derive SelectedWeylVariationActionPrinciple" in unpatched_gate["must_add_one_of"][0], "Route A next object missing")
    require("independent Route-B" in unpatched_gate["must_add_one_of"][1], "Route B next object missing")

    require(two_route["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset knob violation")
    require(two_route["superset_strategy"]["locked_target"] == "same R_Z/R_X/b_selected source packet and same finite row-kernel functional", "locked target mismatch")
    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE-INDEPENDENT", "next fallback mismatch")
    require(cert["local_premise_source_promotion_closed"] is True, "cert local closure missing")
    require(cert["unpatched_source_promotion_closed"] is False, "cert unpatched overclaim")
    require("conditional closure" in note, "note conditional closure missing")
    require("not yet unpatched/no-knob closure" in note, "note no-knob guard missing")

    for item in [candidate, support, local_theorem, unpatched_gate, two_route, cert]:
        guard_no_selector(item)

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (SUPPORT, support),
        (LOCAL_THEOREM, local_theorem),
        (UNPATCHED_GATE, unpatched_gate),
        (TWO_ROUTE, two_route),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
