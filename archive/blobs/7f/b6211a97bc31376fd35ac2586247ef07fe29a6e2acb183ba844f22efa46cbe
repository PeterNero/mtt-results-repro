"""Audit selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun.candidate.json"
CERT = ROOT / "certificates" / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun_certificate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun"
MINIMAL = PACKET_DIR / "minimal_physical_source_certificate.packet.json"
TEMPLATE = PACKET_DIR / "route_a_physical_source_theorem_fill.template.json"
ROUTEB = PACKET_DIR / "route_b_independent_galerkin_provenance_run_spec.packet.json"
DECISION = PACKET_DIR / "source_fill_decision.packet.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalPhiFinC1ActionSourceTheorem_Fill_or_IndependentGalerkinProvenanceRun_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    cert = load(CERT)
    minimal = load(MINIMAL)
    template = load(TEMPLATE)
    route_b = load(ROUTEB)
    decision = load(DECISION)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_PHYSICALPHIFINC1ACTIONSOURCE_FILL_OR_INDEPENDENTGALERKINPROVENANCERUN_BUILT_MINIMAL_SOURCE_CERTIFICATE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(minimal["already_closed_or_retired"]["formal_110_row_replay"] is True, "formal replay not closed")
    require(minimal["already_closed_or_retired"]["finite_row_values"] is True, "finite values not closed")
    for key in [
        "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "no_extra_physical_boundary_or_source_term",
        "same_source_R_Z_R_X_b_selected_emission",
    ]:
        require(minimal["minimal_route_A_certificate_fields"][key] is False, f"Route A field overfilled: {key}")
    require(minimal["same_source_emission_subfields"]["same_source_b_selected_emission"] is False, "b selected overfilled")
    require(template["status"] == "TEMPLATE_READY_NOT_FILLED", "template status mismatch")
    require(template["must_prove_equalities"]["physical_b_selected_equals_formal_b"] is False, "template overfilled")
    require(route_b["current_support"]["all_72_values_exact"] is True, "Route B values missing")
    require(route_b["current_support"]["formal_110_rows_executed"] is True, "Route B rows missing")
    require(route_b["current_support"]["source_independent_of_residual_projector_replay"] is False, "Route B provenance overfilled")
    require(route_b["executed_now"] is False, "Route B overexecuted")
    require(decision["route_A_minimal_certificate_built"] is True, "Route A cert not built")
    require(decision["route_A_minimal_certificate_filled"] is False, "Route A overfilled")
    require(decision["route_B_run_executed"] is False, "Route B overfilled")
    require(decision["unpatched_A_selected_promoted"] is False, "A overpromoted")
    require(decision["true_SM_equivalence_closed"] is False, "SM equivalence overclaimed")
    require(decision["no_knob_closed"] is False, "no-knob overclaimed")
    require(cert["minimal_route_A_source_certificate_identified"] is True, "cert missing minimal certificate")
    require(cert["route_A_minimal_certificate_filled"] is False, "cert overfilled")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("No route is promoted here" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
