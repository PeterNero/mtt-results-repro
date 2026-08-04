from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_source_map_selection_boundary_certificate.json"
STATUS = "POST_ALPHA_SOURCE_MAP_SELECTION_BOUNDARY_BUILT_DYNAMIC_APPLICATION_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1ResidualProjectorAxiom_or_GalerkinC1Execution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "boundary theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["selection_test_built"] is True, "selection test missing")
    require(decision["selection_theorem_proved_now"] is False, "selection theorem overclaimed")
    require(decision["if_selected_closure_exact"] is True, "if-selected replay lost")
    require(decision["frontier_is_differentiated_PhiFinC1_application_or_Galerkin_execution"] is True, "wrong frontier")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    selection = packet["selection_test"]
    require(selection["selection_attempt"]["source_map_selected_now"] is False, "source map selected")
    require(selection["selection_attempt"]["physical_projector_application_promoted_now"] is False, "projector application promoted")
    require(selection["selection_attempt"]["b_source_emitted_now"] is False, "b source emitted")
    require("canonical Q_residual is a unique mathematical projector" in " ".join(selection["why_selection_is_not_yet_proved"]), "Q_residual guard missing")

    replay = packet["if_selected_dynamic_packet_closure"]
    require(replay["promoted_now"] is False, "if-selected packet promoted")
    require(replay["if_selected_numeric_replay"]["rank"] == 2, "rank drift")
    require(replay["if_selected_numeric_replay"]["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong Gram")
    require(replay["if_selected_numeric_replay"]["A_transpose_b"] == [12.0, 12.0], "wrong ATb")
    require(replay["if_selected_numeric_replay"]["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")

    galerkin = packet["honest_galerkin_value_run_route"]
    require(galerkin["can_replace_source_map_now"] is False, "Galerkin route overclaimed")
    require(galerkin["strict_coordinate_target"]["total_real_coordinates"] == 72, "coordinate drift")
    require(galerkin["would_close_SM_parity_dynamic_packet_if_emitted"] is True, "Galerkin closure implication lost")
    require(STATUS in note and NEXT in note and "Still open" in note, "note missing essentials")
    print("AUDIT_PASS: source-map selection boundary built; differentiated PhiFinC1 application remains open")


if __name__ == "__main__":
    main()
