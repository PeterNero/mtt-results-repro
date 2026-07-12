from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_fiberclass_observable_invariance_import_certificate.json"
STATUS = "ROUTEC_FIBERCLASS_OBSERVABLE_INVARIANCE_IMPORTED_GAUGEFIX_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_HigherOrder_or_FullResponse_FlavorSplitting_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "fiber-class invariance import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["spectral_checks"].values()), "all spectral checks should pass")
    require(all(cert["gaugefix_checks"].values()), "all gauge-fix checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open-gate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(
        cert["verdict"]["selected_C1_observable_class_proved_at_current_layer"] is True,
        "current observable class should be proved",
    )
    require(cert["verdict"]["selected_unique_C1_matrix_proved"] is False, "unique C1 matrix must remain open")
    require(cert["verdict"]["shift0_computation_gauge_allowed"] is True, "shift 0 should be a computation gauge")
    require(cert["verdict"]["absolute_fiber_origin_selected"] is False, "absolute fiber origin must remain open")
    require(
        cert["verdict"]["current_layer_has_degenerate_singular_spectrum"] is True,
        "current layer should be degenerate",
    )
    require(cert["verdict"]["physical_flavor_closure_claimed"] is False, "physical flavor closure must not be claimed")
    require(cert["verdict"]["observed_flavor_data_used"] is False, "observed flavor data must not be used")
    require(cert["verdict"]["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    path_a = packet["path_A_observable_invariance"]
    obs = path_a["fixed_shift_observables"]
    require(obs["0"] == obs["1"] == obs["2"], "fixed shifts should have identical observables")
    require(
        packet["what_remains_open"]["higher_order_or_full_strominger_response_support"] is True,
        "higher-order/full response support must remain open",
    )
    require("does not close physical flavor" in note, "note must state flavor boundary")
    require("No observed flavor data were used" in note, "note must state no target fitting")

    print("AUDIT_PASS: fixed-fiber spectral invariance imported; higher-order flavor splitting remains open")


if __name__ == "__main__":
    main()
