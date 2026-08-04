"""Import Route-C C1 defect-functional formal source gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_variational_reduction_import_certificate.json"
UPSTREAM_SLUG = "selected_c1defectfunctionalsource_or_independentquadraturedatafill"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
FUNCTIONAL = UPSTREAM_DIR / "c1_defect_functional_uniqueness_source.packet.json"
PHYSICAL = UPSTREAM_DIR / "phifinc1_physical_application_source_gap.packet.json"
QUADRATURE = UPSTREAM_DIR / "independent_quadrature_data_fill_attempt.packet.json"

OUTPUT_PACKET = DATA / "routec_c1_defect_functional_source_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_c1_defect_functional_source_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_C1DefectFunctionalSource_Import_v1.md"

STATUS = "ROUTEC_C1_DEFECT_FUNCTIONAL_SOURCE_IMPORTED_PHIFINC1_BINDING_OPEN"
PREVIOUS_STATUS = "ROUTEC_VARIATIONAL_REDUCTION_IMPORTED_C1_DEFECT_SOURCE_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_C1DEFECTFUNCTIONALSOURCE_OR_INDEPENDENTQUADRATUREDATAFILL_BUILT_FUNCTIONAL_UNIQUENESS_OPEN_APPLICATION"
NEXT = "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    functional = load(FUNCTIONAL)
    physical = load(PHYSICAL)
    quadrature = load(QUADRATURE)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")
    replay = upstream["replay_if_physical_application_or_independent_data_supplied"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_C1DefectFunctionalSource_or_IndependentQuadratureDataFill_v1",
        "F1_upstream_functional_source_proved_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["patched_spine_closure_preserved"] is True
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["closure_claimed"] is False
        and cert["next_required_artifact"] == NEXT,
        "F3_formal_functional_unique_sourced": functional["status"] == "UNIQUE_QUADRATIC_DEFECT_FUNCTIONAL_SELECTED_AS_FORMAL_SOURCE"
        and all(
            functional["selection_inputs"][key] is True
            for key in [
                "selected_trace_frobenius_metric",
                "selected_fixed_fiber_response_span",
                "selected_72_real_coordinate_target",
                "selected_no_observed_target_policy",
            ]
        )
        and functional["selection_inputs"]["selected_static_sector_routing"] == ["Z->u,e", "X->d,nuD"]
        and all(functional["uniqueness_conditions"][key] is True for key in [
            "quadratic",
            "positive_semidefinite",
            "invariant_under_unitary_change_of_selected_zero_mode_basis",
            "vanishes_on_fixed_fiber_span",
            "penalizes_only_trace_frobenius_leakage_into_residual_complement",
            "no_extra_weights_or_sector_knobs",
        ])
        and functional["uniqueness_result"]["unique_up_to_overall_positive_scale"] is True
        and functional["uniqueness_result"]["overall_scale_cancels_from_euler_projection"] is True
        and functional["uniqueness_result"]["selects_Q_residual"] is True
        and functional["what_this_sources"]["selected_MTT_C1_defect_functional_is_candidate"] is True,
        "F4_physical_application_still_open": physical["status"] == "FUNCTIONAL_SOURCED_PHYSICAL_APPLICATION_RULE_OPEN"
        and physical["now_available"]["unique_formal_C1_defect_functional"] is True
        and physical["now_available"]["Euler_projection_derivation"] is True
        and physical["remaining_physical_application_rule"]["not_proved_now"] is True
        and len(physical["remaining_physical_application_rule"]["why_not_automatic"]) == 3
        and physical["if_supplied_then"]["SM_parity_dynamic_packet_closes"] is True,
        "F5_quadrature_data_not_filled": quadrature["status"] == "DATA_REQUIREMENTS_RESTATED_NO_INDEPENDENT_VALUES_FILLED"
        and len(quadrature["required_values"]) == 6
        and all(value is False for value in quadrature["input_data_available_now"].values())
        and quadrature["acceptance_tests"]["A_shape"] == [72, 2]
        and quadrature["acceptance_tests"]["b_shape"] == [72]
        and "copying b_selected from the patched replay" in quadrature["forbidden_shortcuts"],
        "F6_replay_and_remaining_gates_preserved": replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and replay["A_transpose_b"] == [12.0, 12.0]
        and replay["deltaTheta_C1"] == [1.0, 1.0]
        and all(upstream["what_remains_open"][key] is True for key in [
            "prove_PhiFinC1_minimizes_unique_C1_defect_functional",
            "bind_differentiated_PhiFinC1_to_variational_problem",
            "fill_selected_zero_mode_basis_data",
            "fill_independent_primitive_quadrature_table",
            "fill_independent_hessian_source_vector",
            "run_independent_quadrature_hessian_solve",
            "unpatched_SM_parity_dynamic_packet_closure",
            "true_SM_equivalence_closure",
        ]),
        "F7_promotion_guardrails_preserved": upstream["promotion_decision"]["selected_C1_defect_functional_formal_source_promoted"] is True
        and upstream["promotion_decision"]["physical_PhiFinC1_application_rule_proved"] is False
        and upstream["promotion_decision"]["independent_quadrature_data_filled"] is False
        and upstream["promotion_decision"]["unpatched_A_selected_promoted"] is False
        and upstream["promotion_decision"]["unpatched_b_selected_promoted"] is False
        and upstream["promotion_decision"]["unpatched_deltaTheta_C1_promoted"] is False
        and upstream["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False
        and "formal C1 defect functional" in note,
    }

    summary = {
        "formal_C1_defect_functional_sourced": True,
        "unique_up_to_positive_scale": True,
        "scale_cancels_from_euler_projection": True,
        "physical_PhiFinC1_application_rule_proved": False,
        "independent_quadrature_data_filled": False,
        "A_transpose_A": replay["A_transpose_A"],
        "A_transpose_b": replay["A_transpose_b"],
        "deltaTheta_C1": replay["deltaTheta_C1"],
    }

    return {
        "packet": "RouteC_C1DefectFunctionalSource_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_functional_source": str(FUNCTIONAL),
            "upstream_physical_application_gap": str(PHYSICAL),
            "upstream_quadrature_data_fill": str(QUADRATURE),
        },
        "theorem": {
            "name": "RouteCC1DefectFunctionalSourceImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The unique quadratic trace/Frobenius C1 defect functional is "
                "imported as a formal selected source, unique up to positive "
                "scale.  The physical PhiFinC1 minimization/application theorem "
                "and independent quadrature data remain open."
            ),
        },
        "checks": checks,
        "c1_defect_functional_source_summary": summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "c1_defect_functional_uniqueness_source": functional,
            "phifinc1_physical_application_source_gap": physical,
            "independent_quadrature_data_fill_attempt": quadrature,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_physical_PhiFinC1_application_rule": False,
            "claims_independent_quadrature_data": False,
            "claims_unpatched_A_selected": False,
            "claims_unpatched_b_selected": False,
            "claims_unpatched_deltaTheta_C1": False,
            "claims_unpatched_SM_dynamic_closure": False,
            "claims_true_SM_equivalence": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCC1DefectFunctionalSourceImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "c1_defect_functional_source_summary": packet["c1_defect_functional_source_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["c1_defect_functional_source_summary"]
    return f"""# RouteC C1 Defect Functional Source Import v1

Status: `{cert["status"]}`.

The formal C1 defect functional is now sourced: it is the unique quadratic
trace/Frobenius leakage functional under the selected fixed-fiber span, static
sector routing, and no-extra-knob policy, up to an overall positive scale.  The
scale cancels from the Euler projection.

Current replay if physical application or independent data is supplied:

```text
A^T A = {s["A_transpose_A"]}
A^T b = {s["A_transpose_b"]}
deltaTheta_C1 = {s["deltaTheta_C1"]}
```

Still not claimed: physical `Phi_fin^C1` minimization of this functional,
independent quadrature data, unpatched `A_selected`/`b_selected`/`deltaTheta_C1`,
unpatched SM dynamic closure, or true SM equivalence.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
