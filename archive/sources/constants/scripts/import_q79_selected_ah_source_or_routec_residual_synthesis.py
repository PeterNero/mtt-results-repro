"""Build q79 AH-source or Route-C residual route synthesis."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

PREVIOUS = CERTS / "q79_selected_ah_goodcover_hym_or_routec_residual_promotion_import_certificate.json"
Q79_HYM_ATTEMPT = Q79 / "certificates" / "selected_hym_operator_source_attempt_certificate.json"
Q79_ALL_GATES = Q79 / "certificates" / "all_remaining_valpha_gates_attempt_certificate.json"
Q79_PHIFIN = Q79 / "certificates" / "q79_selected_phifin_alpha1_payload_certificate.json"
Q79_FRONTIER = Q79 / "candidate_data" / "valpha_repo_update_source_frontier.candidate.json"
SM_AH_RESIDUAL = SM / "candidate_data" / "selected_routec_ah_source_selection_or_routec_selected_residual.candidate.json"
SM_HYM_PIPELINE = SM / "candidate_data" / "selected_routec_hym_operator_pipeline.candidate.json"
QA_README = QA / "README.md"

OUT_PACKET = DATA / "q79_selected_ah_source_or_routec_residual_synthesis.candidate.json"
OUT_CERT = CERTS / "q79_selected_ah_source_or_routec_residual_synthesis_certificate.json"
OUT_NOTE = CORPUS / "Q79_Selected_AH_Source_or_RouteC_Residual_Synthesis_v1.md"

STATUS = "Q79_SELECTED_AH_SOURCE_OR_ROUTEC_RESIDUAL_SYNTHESIS_BUILT_FINITE_EMISSION_PRIMARY_VALUES_OPEN"
NEXT = "Q79_Selected_RouteC_FiniteEmissionMorphism_PhiFin_SourceIdentity_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def qa_readme_clues() -> dict[str, Any]:
    text = QA_README.read_text(encoding="utf-8", errors="replace")
    needles = [
        "finite emission",
        "Phi_fin",
        "D_E",
        "Riesz",
        "Green",
        "dotD",
        "selected-source",
    ]
    return {
        "path": str(QA_README),
        "present": QA_README.exists(),
        "needles_present": {needle: needle in text for needle in needles},
        "recent_log_signal_present": "Build U1Y RouteC PhiFin finite emission subpacket" in text,
    }


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    q79_hym = load(Q79_HYM_ATTEMPT)
    q79_gates = load(Q79_ALL_GATES)
    q79_phifin = load(Q79_PHIFIN)
    q79_frontier = load(Q79_FRONTIER)
    sm_ah_residual = load(SM_AH_RESIDUAL)
    sm_hym_pipeline = load(SM_HYM_PIPELINE)
    qa_clues = qa_readme_clues()

    external_inspiration = [
        {
            "label": "numerical_HYM_balanced_Donaldson_algorithm",
            "url": "https://axi.lims.ac.uk/paper/2302.09622",
            "role": "finite-dimensional Hermitian matrix / equivariant quotient HYM computation pattern",
            "proof_import": False,
        },
        {
            "label": "Li_Yau_Gauduchon_HYM_correspondence_context",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0007449723000623",
            "role": "existence theorem context for stable bundles over Gauduchon manifolds",
            "proof_import": False,
        },
        {
            "label": "FEEC_Hilbert_complex_Galerkin_Hodge_laplacian",
            "url": "https://epubs.siam.org/doi/book/10.1137/1.9781611975543",
            "role": "structure-preserving finite D_E/Riesz/Green/dotD verification pattern",
            "proof_import": False,
        },
        {
            "label": "Fu_Yau_Strominger_non_Kahler_flux_container",
            "url": "https://arxiv.org/abs/hep-th/0604063",
            "role": "smooth torsionful Strominger-system container, not finite selected values",
            "proof_import": False,
        },
    ]

    checks = {
        "previous_gate_named_this_target": previous["verdict"]["best_next_artifact"]
        == "Q79_Selected_AH_Source_Selection_or_RouteC_SelectedResidual_v1",
        "AH_HYM_bridge_still_conditional": previous["what_remains_open"][
            "selected_AH_representative_or_literal_goodcover_Cech_source"
        ]
        is True
        and previous["what_remains_open"]["selected_Gauduchon_chamber_source"] is True,
        "q79_hym_operator_source_still_blocked": q79_hym["calculation_results"][
            "selected_hym_operator_source_verified"
        ]
        is False,
        "q79_all_gate_summary_still_source_open": q79_gates["gate_summary"][
            "SelectedNonSplitVAlphaStabilityOrRouteCResidual"
        ]
        == "PARTIAL_NON_SPLIT_INPUT_CLOSED_STABILITY_OPEN",
        "sm_ah_residual_promotes_ordered_layer_not_values": sm_ah_residual[
            "what_remains_open"
        ]["selected_RouteC_residual_values"]
        is True
        and sm_ah_residual["what_remains_open"]["same_source_D_E_Riesz_Green_dotD"]
        is True,
        "sm_hym_pipeline_honest_operator_fails_lifted_flags_pass": sm_hym_pipeline[
            "pipeline_evaluation"
        ]["honest_operator_pipeline_pass"]
        is False
        and sm_hym_pipeline["pipeline_evaluation"]["lifted_flags_operator_pipeline_pass"]
        is True,
        "q79_phifin_keeps_selected_payload_open": q79_phifin["closure_test"][
            "selected_payload_flags_all_true"
        ]
        is False
        and q79_phifin["still_open"]["selected_PhiFin_alpha1_payload_values"]
        is True,
        "cross_repo_frontier_points_to_finite_emission": q79_frontier[
            "repo_update_source_frontier"
        ]["next_required_artifact"]
        == "Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1",
        "qa_readme_has_finite_emission_clues": all(qa_clues["needles_present"].values()),
        "external_sources_marked_inspiration_only": all(
            item["proof_import"] is False for item in external_inspiration
        ),
    }
    proved = all(checks.values())

    route_ranking = [
        {
            "rank": 1,
            "route": "selected_finite_emission_Phi_fin_source_identity",
            "why": (
                "It directly targets the missing same-source objects: rho_E, D_E, "
                "Riesz/Green, dotD, residuals, and primitive overlaps."
            ),
            "current_status": "primary_next_executable",
            "closes_now": False,
        },
        {
            "rank": 2,
            "route": "selected_AH_goodcover_plus_Gauduchon_chamber",
            "why": (
                "It would activate the imported stability and Li-Yau/Gauduchon HYM "
                "existence bridge, but it still would not by itself emit operator values."
            ),
            "current_status": "parallel_theorem_workstream",
            "closes_now": False,
        },
        {
            "rank": 3,
            "route": "formal_lift_of_RouteC_smoke_flags",
            "why": (
                "It is useful as a validator rehearsal only. Prior audits show lifted "
                "selected flags pass while honest selected-source flags fail."
            ),
            "current_status": "diagnostic_only",
            "closes_now": False,
        },
        {
            "rank": 4,
            "route": "split_line_or_identity_rhoE_HYM_shortcut",
            "why": "It loses the non-split/source-sensitive operator payload needed for SM closure.",
            "current_status": "retired_as_proof_source",
            "closes_now": False,
        },
    ]

    return {
        "packet": "Q79_Selected_AH_Source_or_RouteC_Residual_Synthesis_v1",
        "status": STATUS if proved else "Q79_SELECTED_AH_SOURCE_OR_ROUTEC_RESIDUAL_SYNTHESIS_FAILED",
        "inputs": {
            "previous_local_promotion_import": rel(PREVIOUS, ROOT),
            "q79_hym_operator_attempt": rel(Q79_HYM_ATTEMPT, Q79),
            "q79_all_remaining_valpha_gates": rel(Q79_ALL_GATES, Q79),
            "q79_phifin_alpha1_payload": rel(Q79_PHIFIN, Q79),
            "q79_repo_update_source_frontier": rel(Q79_FRONTIER, Q79),
            "sm_ah_source_or_routec_residual": rel(SM_AH_RESIDUAL, SM),
            "sm_hym_operator_pipeline": rel(SM_HYM_PIPELINE, SM),
            "qa_su3_readme": str(QA_README),
        },
        "synthesis_checks": checks,
        "external_inspiration": external_inspiration,
        "external_guardrail": {
            "external_sources_used_as_proof_data": False,
            "external_sources_used_for_method_shape_only": True,
            "no_observed_masses_or_mixings_used": True,
            "no_benchmark_flavor_entries_used": True,
        },
        "route_ranking": route_ranking,
        "best_next_artifact": NEXT,
        "best_next_contract": {
            "must_emit": [
                "selected rho_E transition/source identity",
                "selected Hermitian metric or selected finite metric block",
                "same-source finite D_E action",
                "same-source Riesz projector and reduced Green operator",
                "same-branch dotD/alpha1 derivative",
                "Route-C residual values with selected-source flags true",
                "primitive C1 overlap tensors or a theorem explaining their zero/nonzero status",
            ],
            "must_reject": [
                "lifted selected flags",
                "identity rho_E smoke as final payload",
                "observed CKM/mass/Yukawa inputs",
                "benchmark matrix entries",
            ],
        },
        "what_closes_now": {
            "cross_repo_route_triage": True,
            "external_method_inspiration_recorded": True,
            "finite_emission_route_selected_as_primary_next": True,
            "AH_HYM_bridge_kept_as_parallel_conditional_workstream": True,
            "diagnostic_lift_not_proof_guardrail_locked": True,
        },
        "what_remains_open": {
            "selected_AH_or_goodcover_source": True,
            "selected_Gauduchon_chamber_source": True,
            "selected_HYM_connection_values": True,
            "selected_RouteC_residual_values": True,
            "selected_rho_E_source_identity": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_overlap_tensors": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_selected_AH_source": False,
            "claims_selected_goodcover_source": False,
            "claims_selected_Gauduchon_chamber": False,
            "claims_selected_HYM_values": False,
            "claims_selected_RouteC_values": False,
            "claims_selected_DE_Riesz_Green_dotD": False,
            "claims_primitive_C1_closure": False,
            "claims_full_SM_closure": False,
            "uses_external_sources_as_MTT_axioms": False,
            "uses_observed_data": False,
        },
        "theorem": {
            "name": "Q79SelectedAHSourceOrRouteCResidualSynthesisTheorem",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "Given the imported q79 AH/HYM promotion bridge, sibling SM "
                "Route-C pipeline audits, q79 Phi_fin payload gate, and QA-SU3 "
                "finite-emission clues, the correct next proof object is a selected "
                "finite-emission/source-identity packet for Phi_fin. This synthesis "
                "does not close selected values; it proves that further diagnostic "
                "flag lifts are not proof and that the AH/HYM bridge should remain "
                "a parallel conditional workstream until a selected source and "
                "operator payload are emitted."
            ),
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Selected AH Source or Route-C Residual Synthesis v1

## Result

Status: `{packet["status"]}`

The AH/HYM branch remains mathematically useful but conditional: it needs a
selected AH/good-cover source and selected Gauduchon chamber, and even then it
proves HYM existence before it proves finite operator values.

The Route-C branch is the better next executable path because it can be forced
to emit exactly the objects the remaining proof gates ask for: `rho_E`, `D_E`,
Riesz/Green, `dotD`, selected residuals, and primitive C1 overlaps.  Prior
formal-lift runs are kept only as validator rehearsals.

## Route Ranking

```json
{json.dumps(packet["route_ranking"], indent=2, sort_keys=True)}
```

## External Inspiration

These sources are method-shape inspiration only, not imported MTT proof data.

```json
{json.dumps(packet["external_inspiration"], indent=2, sort_keys=True)}
```

## Next Contract

```json
{json.dumps(packet["best_next_contract"], indent=2, sort_keys=True)}
```

## Remaining Open

```json
{json.dumps(packet["what_remains_open"], indent=2, sort_keys=True)}
```

Next: `{packet["best_next_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    if "--write" in sys.argv:
        OUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_CERT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUT_NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
