"""Audit PSM-C1-02 SI-1u-A1 physical source-certificate reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution.py"

SLUG = "selected_psm_c1_02_physicalphifinc1actionrestriction_or_honestfinitec1execution"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
THREE_FIELD = BASE / "si1u_a1_three_field_physical_source_certificate.packet.json"
ROUTE_A_TEMPLATE = BASE / "route_a_physical_source_theorem_template_import.packet.json"
ROUTE_B_SPEC = BASE / "route_b_honest_finite_c1_execution_spec_import.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PhysicalPhiFinC1ActionRestriction_or_HonestFiniteC1Execution_v1.md"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_A1_THREE_FIELD_PHYSICAL_SOURCE_CERTIFICATE_READY_NOT_FILLED"
NEXT = "MTT_Selected_PSM_C1_02_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "global closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    three = load(THREE_FIELD)
    route_a = load(ROUTE_A_TEMPLATE)
    route_b = load(ROUTE_B_SPEC)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_label"] == "PSM-C1-02", "active label mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-A1", "SOURCE-IDENTITY/SI-1u-B2"], "routes mismatch")
    require(candidate["closed_boundary"] == "DONE-PARITY-00", "closed boundary mismatch")
    require(candidate["next_required_artifact"] == NEXT, "next mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")

    require(three["status"] == "THREE_FIELD_PHYSICAL_SOURCE_CERTIFICATE_IDENTIFIED_NOT_FILLED", "three-field status mismatch")
    require(set(three["fields"].keys()) == {
        "physical_action_restricts_to_selected_finite_Weyl_quotient",
        "no_extra_physical_boundary_or_source_term",
        "same_source_R_Z_R_X_b_selected_emission",
    }, "three fields mismatch")
    require(all(value is False for value in three["fields"].values()), "three-field overfilled")
    require(three["filled_now"] is False, "three-field filled unexpectedly")

    require(route_a["status"] == "ROUTE_A_TEMPLATE_IMPORTED_NOT_FILLED", "route A status mismatch")
    require(route_a["filled_now"] is False, "route A overfilled")
    require(len(route_a["must_attach_sources"]) == 5, "route A source list incomplete")
    require(all(value is False for value in route_a["must_prove_equalities"].values()), "route A equality overproved")

    require(route_b["status"] == "ROUTE_B_INDEPENDENT_RUN_SPEC_IMPORTED_NOT_EXECUTED", "route B status mismatch")
    require(route_b["executed_now"] is False, "route B overexecuted")
    require(route_b["current_support"]["formal_110_rows_executed"] is True, "route B support missing")
    require(route_b["current_support"]["source_independent_of_residual_projector_replay"] is False, "route B independence overclaimed")

    closes = candidate["what_closes_now"]
    require(closes["SI1u_A1_three_field_certificate_reduction"] is True, "certificate reduction missing")
    require(closes["route_A_fill_template_imported"] is True, "route A import missing")
    require(closes["route_B_independent_run_spec_imported"] is True, "route B import missing")
    require(closes["support_only_countermodel_respected"] is True, "countermodel guard missing")

    remains = candidate["what_remains_open"]
    require(remains["SI1u_A1a_physical_action_restricts_to_selected_finite_Weyl_quotient"] is True, "A1a not open")
    require(remains["SI1u_A1b_no_extra_physical_boundary_or_source_term"] is True, "A1b not open")
    require(remains["SI1u_A1c_same_source_R_Z_R_X_b_selected_emission"] is True, "A1c not open")
    require(remains["route_B_independent_Galerkin_or_row_run"] is True, "Route B not open")

    decision = candidate["closure_decision"]
    require(decision["route_A_minimal_certificate_built"] is True, "decision certificate missing")
    require(decision["route_A_minimal_certificate_filled"] is False, "decision overfilled")
    require(decision["route_B_run_executed"] is False, "decision route B overexecuted")
    require(decision["unpatched_A_selected_promoted"] is False, "A overpromoted")
    require(decision["unpatched_b_selected_promoted"] is False, "b overpromoted")
    require(decision["unpatched_deltaTheta_C1_promoted"] is False, "delta overpromoted")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a", "next primary mismatch")
    require(next_work["replacement"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "replacement mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["three_field_certificate_ready"] is True, "cert reduction missing")
    require(cert["route_A_minimal_certificate_filled"] is False, "cert overfilled")
    require(cert["route_B_run_executed"] is False, "cert route B overexecuted")

    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1`" in note, "note label missing")
    require("SI-1u-A1a" in note and "SI-1u-A1b" in note and "SI-1u-A1c" in note, "note sublabels missing")
    require("not knobs" in note, "note superset guard missing")

    for item in [candidate, three, route_a, route_b, cert]:
        guard(item)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
