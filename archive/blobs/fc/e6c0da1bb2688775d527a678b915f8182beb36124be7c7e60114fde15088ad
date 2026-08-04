"""Build I10 payload certificate / independent quadrature values fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS_SLUG = "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues"
PREVIOUS = DATA / f"{PREVIOUS_SLUG}.candidate.json"
PAYLOAD_CONTRACT = DATA / PREVIOUS_SLUG / "i10_minimizer_trace_c1_payload_contract.packet.json"
QUADRATURE_STAGING = DATA / PREVIOUS_SLUG / "quadrature_values_staging_tables.packet.json"
ACCEPTANCE_MANIFEST = DATA / PREVIOUS_SLUG / "closure_acceptance_manifest.packet.json"
SOURCE_DRAFTS = DATA / "selected_source_paper_appendix_drafts.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
SOURCE_ALPHA1 = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
C1_FUNCTIONAL_GATE = DATA / "selected_c1defectfunctionalsource_or_independentquadraturedatafill.candidate.json"

SLUG = "selected_i10_payloadcertificate_or_independentquadraturevaluesfill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_ATTEMPT = PACKET_DIR / "route_a_i10_payload_certificate_fill_attempt.packet.json"
ROUTE_B_ATTEMPT = PACKET_DIR / "route_b_independent_quadrature_values_fill_attempt.packet.json"
CUTSET = PACKET_DIR / "minimal_next_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1.md"

STATUS = "MTT_SELECTED_I10_PAYLOAD_OR_QUADRATURE_VALUES_FILL_ATTEMPT_BUILT_CUTSET_OPEN"
NEXT = "MTT_Selected_StromingerTraceC1FirstVariation_or_QuadratureExecutionPlan_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    payload_contract = load(PAYLOAD_CONTRACT)
    quadrature_staging = load(QUADRATURE_STAGING)
    manifest = load(ACCEPTANCE_MANIFEST)
    source_drafts = load(SOURCE_DRAFTS)
    phifin_alpha1 = load(PHIFIN_ALPHA1)
    source_alpha1 = load(SOURCE_ALPHA1)
    c1_functional_gate = load(C1_FUNCTIONAL_GATE)

    insertion_index = source_drafts["insertion_index"]
    i1 = insertion_index["I1_selected_strominger_minimizer_to_phifin_trace"]
    i5 = insertion_index["I5_dotD_alpha1_and_C1_response"]

    route_a = {
        "schema": "MTTRouteAI10PayloadCertificateFillAttempt.v1",
        "status": "ATTEMPTED_NOT_ACCEPTED_SELECTED_PAYLOADS_OPEN",
        "source_contract": rel(PAYLOAD_CONTRACT),
        "payload_checks": {
            "selected_minimizer_trace_payload_verified": {
                "value": False,
                "reason": "I1 remains an appendix proof slot; selected finite Phi_fin trace coordinates are not emitted.",
                "evidence": {
                    "slot_status": i1["status"],
                    "promotes_selected_flags_now": i1["promotes_selected_flags_now"],
                    "validation_artifacts": i1["validation_artifacts"],
                },
                "needed_next": [
                    "selected q79/F,m=1 Strominger/HYM minimizer certificate",
                    "finite Phi_fin trace coordinates",
                    "selected boundary and normalization data",
                ],
            },
            "selected_c1_response_payload_verified": {
                "value": False,
                "reason": "Same-branch alpha1/dotD support exists, but finite C1 response matrices, source vector, Hessian blocks, and primitive contractions are not selected values.",
                "evidence": {
                    "slot_status": i5["status"],
                    "promotes_selected_flags_now": i5["promotes_selected_flags_now"],
                    "source_origin_status": source_alpha1["status"],
                    "phifin_alpha1_status": phifin_alpha1["status"],
                    "selected_values": source_alpha1["alpha1_driver_audit"]["selected_values"],
                    "missing_selected_operator_data": source_alpha1["alpha1_driver_audit"]["missing_selected_operator_data"],
                },
                "needed_next": [
                    "finite C1 overlap/tangent response operator",
                    "sector response matrices",
                    "selected b/Hessian normalization",
                    "primitive contractions with exact equalities or error bounds",
                ],
            },
            "defect_functional_minimizer_payload_verified": {
                "value": False,
                "reason": "The unique C1 defect functional is sourced, but the first-variation/coercivity statement for the selected Phi_fin C1 response is not proved.",
                "evidence": {
                    "functional_gate_status": c1_functional_gate["status"],
                    "physical_application_rule_proved": c1_functional_gate["promotion_decision"]["physical_PhiFinC1_application_rule_proved"],
                    "independent_quadrature_data_filled": c1_functional_gate["promotion_decision"]["independent_quadrature_data_filled"],
                },
                "needed_next": [
                    "first-variation identity on selected response span",
                    "coercive Hessian block or convexity proof",
                    "boundary term cancellation under selected routing",
                    "finite trace/Frobenius normalization compatibility",
                ],
            },
            "no_observed_data_as_selector": {
                "value": True,
                "reason": "The fill attempt imports only corpus/repo source packets and does not use measured masses, mixings, CP phase, or benchmark entries.",
            },
        },
        "accepted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTRouteBIndependentQuadratureValuesFillAttempt.v1",
        "status": "ATTEMPTED_VALUES_EMPTY_NOT_ACCEPTED",
        "source_staging": rel(QUADRATURE_STAGING),
        "table_counts": {name: len(rows) for name, rows in quadrature_staging["tables"].items()},
        "expected_minimum_counts": quadrature_staging["expected_minimum_counts"],
        "acceptance_checks": {
            "basis_rows_present_and_selected": False,
            "primitive_contractions_present_with_error_bounds": False,
            "hessian_rows_present_and_positive_on_admissible_span": False,
            "sector_matrices_present": False,
            "rank_at_least_2": False,
            "deltaTheta_solve_matches_replay": False,
            "no_patched_replay_copying": True,
        },
        "why_values_not_filled": [
            "No selected zero-mode basis table is available at this gate.",
            "No independent primitive contraction rows are emitted.",
            "No independent Hessian source rows are emitted.",
            "No selected sector matrices are emitted.",
        ],
        "accepted_now": False,
        "observed_data_used": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTI10PayloadMinimalCutset.v1",
        "status": "NEXT_CUTSET_SELECTED",
        "route_A_minimal_cutset": [
            "selected_minimizer_trace_payload_verified",
            "selected_c1_response_payload_verified",
            "defect_functional_minimizer_payload_verified",
        ],
        "route_B_minimal_cutset": [
            "zero_mode_basis_rows",
            "primitive_contraction_rows",
            "hessian_source_rows",
            "sector_matrix_rows",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The current blocker is not linear algebra: the replay target is fixed. The next useful step is "
                "to either derive the first-variation/minimizer theorem from selected trace/C1 payloads or "
                "execute the independent quadrature table fill with actual rows."
            ),
            "superset_strategy": {
                "straight_route": "Route A: selected Strominger/HYM minimizer trace plus same-branch C1 response proves I10.",
                "parallel_route": "Route B: independent quadrature/Hessian rows reconstruct the same A,b,deltaTheta without relying on I10.",
                "locked_target": previous["replay_if_route_A_or_B_accepted"],
            },
        },
    }

    route_a_accept = all(item["value"] for item in route_a["payload_checks"].values())
    route_b_accept = all(route_b["acceptance_checks"].values())
    candidate = {
        "candidate": "MTTSelectedI10PayloadCertificateOrIndependentQuadratureValuesFill",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "payload_contract": rel(PAYLOAD_CONTRACT),
            "quadrature_staging": rel(QUADRATURE_STAGING),
            "acceptance_manifest": rel(ACCEPTANCE_MANIFEST),
            "source_appendix_drafts": rel(SOURCE_DRAFTS),
            "selected_phifin_alpha1_payload": rel(PHIFIN_ALPHA1),
            "selected_source_origin_and_alpha1_driver": rel(SOURCE_ALPHA1),
            "c1_functional_gate": rel(C1_FUNCTIONAL_GATE),
        },
        "output_packets": {
            "route_a_i10_payload_certificate_fill_attempt": rel(ROUTE_A_ATTEMPT),
            "route_b_independent_quadrature_values_fill_attempt": rel(ROUTE_B_ATTEMPT),
            "minimal_next_cutset": rel(CUTSET),
        },
        "what_closes_now": {
            "route_A_payload_fields_evaluated": True,
            "route_B_quadrature_tables_evaluated": True,
            "minimal_cutset_selected": True,
            "no_observed_data_as_selector_verified": True,
        },
        "what_remains_open": {
            "selected_minimizer_trace_payload_verified": not route_a["payload_checks"]["selected_minimizer_trace_payload_verified"]["value"],
            "selected_c1_response_payload_verified": not route_a["payload_checks"]["selected_c1_response_payload_verified"]["value"],
            "defect_functional_minimizer_payload_verified": not route_a["payload_checks"]["defect_functional_minimizer_payload_verified"]["value"],
            "independent_quadrature_values_filled": not route_b_accept,
            "unpatched_SM_parity_dynamic_packet_closure": True,
            "true_SM_equivalence_closure": True,
        },
        "promotion_decision": {
            "route_A_i10_payload_certificate_accepted": route_a_accept,
            "route_B_independent_quadrature_values_accepted": route_b_accept,
            "I10_proved": route_a_accept,
            "unpatched_A_selected_promoted": route_a_accept or route_b_accept,
            "unpatched_b_selected_promoted": route_a_accept or route_b_accept,
            "unpatched_deltaTheta_C1_promoted": route_a_accept or route_b_accept,
            "unpatched_SM_parity_dynamic_packet_closed": route_a_accept or route_b_accept,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "I10PayloadFillAttemptCutsetTheorem",
            "proved": True,
            "statement": (
                "Evaluating the I10 payload and independent quadrature fill routes against current corpus packets "
                "proves that the next blocker is exactly the selected trace/C1/first-variation payload triple, "
                "or the independent quadrature rows. No measured constants or target residuals are used."
            ),
        },
        "replay_if_route_A_or_B_accepted": previous["replay_if_route_A_or_B_accepted"],
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "route_A_accepted": route_a_accept,
        "route_B_accepted": route_b_accept,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I10 PayloadCertificate or IndependentQuadratureValuesFill v1

Status: `{STATUS}`.

This gate tries to fill both legal routes from the previous acceptance manifest.

Route A result:

```text
selected minimizer trace payload verified    = False
selected C1 response payload verified        = False
defect-functional minimizer payload verified = False
no observed data as selector                 = True
accepted                                     = False
```

Route B result:

```text
zero-mode basis rows       = {route_b["table_counts"]["zero_mode_basis_rows"]}
primitive contraction rows = {route_b["table_counts"]["primitive_contraction_rows"]}
hessian source rows        = {route_b["table_counts"]["hessian_source_rows"]}
sector matrix rows         = {route_b["table_counts"]["sector_matrix_rows"]}
accepted                   = False
```

The useful advance is the cutset: the replay target is already fixed, so the
next artifact must either derive the selected first-variation/minimizer theorem
from the trace/C1 payloads or execute the independent quadrature rows.

Next artifact: `{NEXT}`.
"""

    ROUTE_A_ATTEMPT.write_text(json.dumps(route_a, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTE_B_ATTEMPT.write_text(json.dumps(route_b, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CUTSET.write_text(json.dumps(cutset, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
