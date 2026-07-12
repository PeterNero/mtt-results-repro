from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_basis_transport_proof_or_counterexample_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    insertion = Path(cert["paper_insertion_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "ROUTEC_PRIMITIVE_ONLY_COUNTEREXAMPLE_IMPORTED_WEYL_PAIR_SOURCE_OPEN",
        "unexpected status",
    )
    require(cert["theorem"]["proved"] is True, "counterexample import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now claims should pass")
    require(all(cert["still_open"].values()), "all still-open gates should remain true")

    fixed = cert["span_tests"]["fixed_fiber_primitives"]
    fixed_all = cert["span_tests"]["fixed_plus_all_fiber_envelope"]
    require(fixed["target_in_span"] is False, "fixed-fiber primitive span must reject target")
    require(fixed_all["target_in_span"] is False, "fixed plus all-fiber span must reject target")
    require(fixed["relative_residual"] > 0.7, "fixed-fiber residual should remain large")
    require(fixed_all["relative_residual"] > 0.7, "fixed plus all-fiber residual should remain large")
    require(cert["refined_next_theorem"]["name"] == "SelectedWeylPairBasisTransportOrVertexSourceTheorem", "refined theorem mismatch")
    require("phase-like qutrit Z component or equivalent basis holonomy" in cert["refined_next_theorem"]["required_new_components"], "missing phase component")
    require("shift-like qutrit X component tied to active shift (1,1)" in cert["refined_next_theorem"]["required_new_components"], "missing shift component")

    no_go = packet["current_layer_no_go"]
    require(no_go["proved"] is True, "current-layer flavor no-go should be proved")
    for sector, diag in no_go["diagnostics"].items():
        require(diag["YYstar_scalar_test"]["is_scalar_identity"] is True, f"{sector} should be scalar identity")
    require(cert["verdict"]["selected_source_emission_proved"] is False, "source emission must remain open")
    require(cert["verdict"]["selected_enriched_A_or_b_emitted"] is False, "A/b must not be emitted")
    require(cert["verdict"]["selected_correction_values_computed"] is False, "correction values must remain open")
    require("primitive-only source theorem is not sufficient" in note, "note must state primitive-only counterexample")
    require("not a Standard Model closure theorem" in insertion, "insertion must preserve SM guardrail")
    require(all(cert["guardrails"].values()), "all guardrails must hold")

    print("AUDIT_PASS: primitive-only counterexample imported; Weyl-pair source theorem remains open")


if __name__ == "__main__":
    main()
