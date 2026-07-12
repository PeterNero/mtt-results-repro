"""Import Route-C source-map selection boundary theorem."""

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

PREVIOUS = CERTS / "routec_primitive_c1_source_map_candidate_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun_certificate.json"
UPSTREAM_DIR = SM / "candidate_data" / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun"
UPSTREAM_SELECTION_TEST = UPSTREAM_DIR / "source_map_selection_theorem_test.packet.json"
UPSTREAM_IF_SELECTED = UPSTREAM_DIR / "if_selected_dynamic_packet_closure.packet.json"
UPSTREAM_GALERKIN_ROUTE = UPSTREAM_DIR / "honest_galerkin_value_run_route.packet.json"

OUTPUT_PACKET = DATA / "routec_source_map_selection_boundary_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_source_map_selection_boundary_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_SourceMapSelectionBoundary_Import_v1.md"

STATUS = "ROUTEC_SOURCE_MAP_SELECTION_BOUNDARY_IMPORTED_DYNAMIC_APPLICATION_OPEN"
PREVIOUS_STATUS = "ROUTEC_PRIMITIVE_C1_SOURCE_MAP_CANDIDATE_IMPORTED_SELECTION_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_SOURCEMAPSELECTIONTHEOREM_OR_HONESTGALERKINC1VALUERUN_BUILT_SELECTION_TEST_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    selection = load(UPSTREAM_SELECTION_TEST)
    if_selected = load(UPSTREAM_IF_SELECTED)
    galerkin = load(UPSTREAM_GALERKIN_ROUTE)
    closed = selection["already_selected_or_closed"]
    attempt = selection["selection_attempt"]
    current = if_selected["current_antecedent"]
    would = if_selected["would_promote_if_antecedent_met"]
    replay = if_selected["if_selected_numeric_replay"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_SourceMapSelectionTheorem_or_HonestGalerkinC1ValueRun_v1",
        "F1_upstream_packet_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["observed_data_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["theorem_proved"] is True
        and upstream_cert["candidate_path"].endswith(
            "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"
        ),
        "F3_closed_static_support_separated": selection["status"]
        == "SELECTION_TEST_BUILT_DYNAMIC_APPLICATION_OPEN"
        and all(
            closed[key] is True
            for key in [
                "terminal_static_source_unconditional",
                "static_source_map_candidate_constructed",
                "weyl_polynomial_residuals_exact",
                "canonical_residual_projector_unique",
                "canonical_projector_replays_RZ_RX",
                "strict_72_real_target_attached",
            ]
        ),
        "F4_dynamic_selection_attempt_still_open": all(
            attempt[key] is False
            for key in [
                "phase_R_Z_selected_now",
                "shift_R_X_selected_now",
                "b_source_emitted_now",
                "physical_projector_application_promoted_now",
                "source_map_selected_now",
            ]
        )
        and len(selection["why_selection_is_not_yet_proved"]) == 4,
        "F5_if_selected_closure_exact": if_selected["status"]
        == "IF_SELECTED_CLOSURE_EXACT_BUT_ANTECEDENT_OPEN"
        and all(
            current[key] is False
            for key in [
                "phase_R_Z_selected",
                "shift_R_X_selected",
                "b_source_emitted",
                "A_selected_promotes",
                "b_selected_promotes",
                "deltaTheta_C1_promotes",
            ]
        )
        and would["A_selected_promotes"] is True
        and would["b_selected_promotes"] is True
        and would["deltaTheta_C1_promotes"] is True
        and would["SM_parity_dynamic_packet_would_close"] is True,
        "F6_numeric_replay_exact_but_unpromoted": replay["rank"] == 2
        and replay["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]]
        and replay["A_transpose_b"] == [12.0, 12.0]
        and replay["deltaTheta_C1"] == [1.0, 1.0]
        and if_selected["promoted_now"] is False,
        "F7_galerkin_alternate_route_open": galerkin["status"] == "HONEST_GALERKIN_VALUE_RUN_ROUTE_OPEN"
        and galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72
        and galerkin["selected_source_verified"] is False
        and galerkin["can_replace_source_map_now"] is False
        and galerkin["would_close_SM_parity_dynamic_packet_if_emitted"] is True
        and galerkin["would_close_no_knob_flavor_constants_by_itself"] is False,
        "F8_no_promotion_or_target_fit": all(
            upstream["promotion_decision"][key] is False
            for key in [
                "selection_theorem_proved_now",
                "source_map_selected_by_MTT_now",
                "A_selected_promoted",
                "b_selected_promoted",
                "deltaTheta_C1_promoted",
                "sector_response_matrices_promoted",
                "honest_Galerkin_C1_value_run_promoted",
                "SM_parity_dynamic_packet_closed",
                "true_SM_equivalence_closed",
                "no_knob_flavor_constants_closed",
            ]
        ),
    }

    summary = {
        "static_support_closed": True,
        "dynamic_application_open": True,
        "phase_R_Z_selected_now": attempt["phase_R_Z_selected_now"],
        "shift_R_X_selected_now": attempt["shift_R_X_selected_now"],
        "b_source_emitted_now": attempt["b_source_emitted_now"],
        "physical_projector_application_promoted_now": attempt[
            "physical_projector_application_promoted_now"
        ],
        "if_selected_A_transpose_A": replay["A_transpose_A"],
        "if_selected_A_transpose_b": replay["A_transpose_b"],
        "if_selected_deltaTheta_C1": replay["deltaTheta_C1"],
        "honest_galerkin_route_open": True,
    }

    return {
        "packet": "RouteC_SourceMapSelectionBoundary_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_selection_test": str(UPSTREAM_SELECTION_TEST),
            "upstream_if_selected": str(UPSTREAM_IF_SELECTED),
            "upstream_galerkin_route": str(UPSTREAM_GALERKIN_ROUTE),
        },
        "theorem": {
            "name": "RouteCSourceMapSelectionBoundaryImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected-source frontier is reduced to a dynamic "
                "application rule: static terminal support, exact R_Z/R_X "
                "shapes, and unique Q_residual support are closed, but "
                "differentiated PhiFinC1 has not yet been proved to apply "
                "Q_residual and emit b_selected.  If that antecedent is "
                "supplied, A_selected, b_selected, and deltaTheta_C1 replay "
                "exactly; otherwise the honest Galerkin C1 value run remains "
                "the alternate route."
            ),
        },
        "checks": checks,
        "selection_boundary_summary": summary,
        "upstream_source_map_selection_boundary": upstream,
        "upstream_packets": {
            "selection_test": selection,
            "if_selected_closure": if_selected,
            "honest_galerkin_route": galerkin,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_selection_theorem": False,
            "claims_source_map_selected": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_deltaTheta_C1": False,
            "claims_honest_Galerkin_C1": False,
            "claims_SM_parity_dynamic_packet_closure": False,
            "claims_full_no_knob_flavor_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCSourceMapSelectionBoundaryImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "selection_boundary_summary": packet["selection_boundary_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["selection_boundary_summary"]
    return f"""# RouteC Source Map Selection Boundary Import v1

Status: `{cert["status"]}`.

The source-map selection boundary is now sharp.  Static terminal support,
`R_Z/R_X` residual shapes, canonical `Q_residual`, and the strict 72-real target
are closed.  Dynamic application is still open:

```text
phase R_Z selected now = {s["phase_R_Z_selected_now"]}
shift R_X selected now = {s["shift_R_X_selected_now"]}
b source emitted now = {s["b_source_emitted_now"]}
physical projector application promoted now = {s["physical_projector_application_promoted_now"]}
```

If those antecedents are supplied, the replay remains exact:

```text
A^T A = {s["if_selected_A_transpose_A"]}
A^T b = {s["if_selected_A_transpose_b"]}
deltaTheta_C1 = {s["if_selected_deltaTheta_C1"]}
```

This is not source-map selection.  The next proof must derive differentiated
`Phi_fin^C1` application of `Q_residual` plus `b_selected`, or run honest
selected Galerkin C1 values.

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
