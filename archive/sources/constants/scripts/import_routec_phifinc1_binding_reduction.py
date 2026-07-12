"""Import Route-C PhiFinC1 minimizer binding reduction gate."""

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

PREVIOUS = CERTS / "routec_c1_defect_functional_source_import_certificate.json"
UPSTREAM_SLUG = "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
BINDING = UPSTREAM_DIR / "phifinc1_minimizer_binding_reduction.packet.json"
QUADRATURE = UPSTREAM_DIR / "independent_quadrature_table_template.packet.json"
PAPER_DRAFT = SM / "proof_corpus" / "paper_appendix_drafts" / "selected_source" / "theta_execution_flavor__i10_phifinc1_minimizes_c1_defect_functional.md"

OUTPUT_PACKET = DATA / "routec_phifinc1_binding_reduction_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_phifinc1_binding_reduction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_PhiFinC1BindingReduction_Import_v1.md"

STATUS = "ROUTEC_PHIFINC1_BINDING_REDUCTION_IMPORTED_I10_OR_QUADRATURE_OPEN"
PREVIOUS_STATUS = "ROUTEC_C1_DEFECT_FUNCTIONAL_SOURCE_IMPORTED_PHIFINC1_BINDING_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_PHIFINC1MINIMIZESDEFECTFUNCTIONAL_OR_INDEPENDENTQUADRATURETABLE_BUILT_BINDING_REDUCTION_OPEN"
NEXT = "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    binding = load(BINDING)
    quadrature = load(QUADRATURE)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")
    draft = PAPER_DRAFT.read_text(encoding="utf-8")
    replay = upstream["replay_if_I10_or_quadrature_table_proved"]
    slots = binding["existing_source_theorem_slots"]
    new_slot = binding["new_binding_theorem_slot"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1",
        "F1_upstream_binding_reduction_proved_open": upstream["status"] == UPSTREAM_STATUS
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
        "F3_binding_reduced_to_I1_I5_I10": binding["status"] == "REDUCED_TO_MINIMIZER_TRACE_AND_C1_RESPONSE_THEOREM_SLOTS"
        and slots["I1_selected_strominger_minimizer_to_phifin_trace"]["status"] == "APPENDIX_DRAFT_PROOF_SLOT_OPEN"
        and slots["I5_dotD_alpha1_and_C1_response"]["status"] == "APPENDIX_DRAFT_PROOF_SLOT_OPEN"
        and new_slot["id"] == "I10_phifinc1_minimizes_c1_defect_functional"
        and new_slot["dependencies"] == [
            "I1_selected_strominger_minimizer_to_phifin_trace",
            "I5_dotD_alpha1_and_C1_response",
            "C1DefectFunctionalUniquenessTheorem",
        ]
        and binding["proved_now"] is False
        and len(binding["why_not_proved_now"]) == 3
        and binding["would_close_if_proved"]["SM_parity_dynamic_packet_closes"] is True,
        "F4_quadrature_template_ready_empty": quadrature["status"] == "TEMPLATE_READY_VALUES_EMPTY"
        and len(quadrature["required_values"]) == 6
        and quadrature["values_filled_now"] is False
        and quadrature["acceptance_tests"]["A_shape"] == [72, 2]
        and quadrature["acceptance_tests"]["b_shape"] == [72]
        and "copying b_selected from the patched replay" in quadrature["forbidden_shortcuts"]
        and quadrature["would_close_if_filled"]["honest_independent_Galerkin_C1_closes"] is True,
        "F5_draft_and_note_guardrails_present": "Theorem Slot I10" in draft
        and "target residuals" in draft
        and "I10 theorem slot created" in note,
        "F6_replay_and_remaining_gates_preserved": replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and replay["A_transpose_b"] == [12.0, 12.0]
        and replay["deltaTheta_C1"] == [1.0, 1.0]
        and all(upstream["what_remains_open"][key] is True for key in [
            "prove_I1_selected_minimizer_to_PhiFin_trace",
            "prove_I5_selected_dotD_C1_response",
            "prove_I10_PhiFinC1_minimizes_defect_functional",
            "fill_independent_quadrature_table_values",
            "unpatched_SM_parity_dynamic_packet_closure",
            "true_SM_equivalence_closure",
        ]),
        "F7_no_promotion_overclaim": upstream["promotion_decision"]["PhiFinC1_minimizes_defect_functional_proved"] is False
        and upstream["promotion_decision"]["independent_quadrature_table_values_filled"] is False
        and upstream["promotion_decision"]["unpatched_A_selected_promoted"] is False
        and upstream["promotion_decision"]["unpatched_b_selected_promoted"] is False
        and upstream["promotion_decision"]["unpatched_deltaTheta_C1_promoted"] is False
        and upstream["promotion_decision"]["unpatched_SM_parity_dynamic_packet_closed"] is False
        and upstream["promotion_decision"]["true_SM_equivalence_closed"] is False,
    }

    summary = {
        "I10_theorem_slot_created": True,
        "I10_proved_now": False,
        "I1_minimizer_trace_open": True,
        "I5_dotD_C1_response_open": True,
        "independent_quadrature_template_created": True,
        "independent_quadrature_values_filled": False,
        "A_transpose_A": replay["A_transpose_A"],
        "A_transpose_b": replay["A_transpose_b"],
        "deltaTheta_C1": replay["deltaTheta_C1"],
    }

    return {
        "packet": "RouteC_PhiFinC1BindingReduction_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_binding_reduction": str(BINDING),
            "upstream_quadrature_template": str(QUADRATURE),
            "upstream_I10_draft": str(PAPER_DRAFT),
        },
        "theorem": {
            "name": "RouteCPhiFinC1BindingReductionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The physical PhiFinC1 minimization gate is reduced to I10, "
                "depending on I1 selected minimizer-to-PhiFin trace, I5 selected "
                "dotD/C1 response, and C1 defect functional uniqueness; alternatively "
                "an independent quadrature table can bypass I10.  Neither route is closed."
            ),
        },
        "checks": checks,
        "phifinc1_binding_reduction_summary": summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "phifinc1_minimizer_binding_reduction": binding,
            "independent_quadrature_table_template": quadrature,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_I10_proved": False,
            "claims_I1_proved": False,
            "claims_I5_proved": False,
            "claims_independent_quadrature_values": False,
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
        "certificate": "RouteCPhiFinC1BindingReductionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "phifinc1_binding_reduction_summary": packet["phifinc1_binding_reduction_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["phifinc1_binding_reduction_summary"]
    return f"""# RouteC PhiFinC1 Binding Reduction Import v1

Status: `{cert["status"]}`.

The physical `Phi_fin^C1` minimization gate is now reduced to a named I10
theorem slot, depending on I1, I5, and the C1 defect-functional uniqueness
theorem.  An independent quadrature table remains the bypass route.

Current status:

```text
I10 theorem slot created = {s["I10_theorem_slot_created"]}
I10 proved now = {s["I10_proved_now"]}
I1 minimizer trace open = {s["I1_minimizer_trace_open"]}
I5 dotD/C1 response open = {s["I5_dotD_C1_response_open"]}
independent quadrature values filled = {s["independent_quadrature_values_filled"]}
```

Replay if I10 or independent quadrature closes:

```text
A^T A = {s["A_transpose_A"]}
A^T b = {s["A_transpose_b"]}
deltaTheta_C1 = {s["deltaTheta_C1"]}
```

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
