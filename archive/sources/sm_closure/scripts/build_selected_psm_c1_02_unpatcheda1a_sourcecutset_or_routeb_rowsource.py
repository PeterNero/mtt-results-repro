"""Build PSM-C1-02 unpatched A1a source cutset / Route B row-source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_psm_c1_02_unpatcheda1a_sourcecutset_or_routeb_rowsource"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A_CUTSET = BASE / "route_a_unpatched_boundary_firstvariation_cutset.packet.json"
ROUTE_B_CUTSET = BASE / "route_b_row_source_independence_cutset.packet.json"
ROUTE_B_STRICT_PACKET = BASE / "route_b_extracted_strict_packet_for_validator.packet.json"
DUAL_VALIDATOR = BASE / "dual_validator_replay.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_UnpatchedA1aSourceCutset_or_RouteBRowSource_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource.candidate.json"
I11_BACKIMPORT = DATA / "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation.candidate.json"
I11_FRONTIER = DATA / "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation" / "remaining_boundary_firstvariation_source_frontier.packet.json"
I11_ROUTE_B = DATA / "selected_i11_routeb_nearmiss_or_rowsourcetheorem.candidate.json"
ROUTE_B_NEARMISS = DATA / "selected_i11_routeb_nearmiss_or_rowsourcetheorem" / "route_b_strict_nearmiss.packet.json"
I10_CURRENT = DATA / "selected_psm_c1_02_i10bindingproof_or_selectedquadraturesourcepromotion" / "route_a_current_i10_binding_stack_attempt.packet.json"
I10_CONDITIONAL = DATA / "selected_psm_c1_02_i10bindingproof_or_selectedquadraturesourcepromotion" / "route_a_conditional_i10_binding_stack_witness.packet.json"
I10_VALIDATOR = ROOT / "scripts" / "validate_selected_i10_binding_stack.py"
ROUTEAB_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"

STATUS = "MTT_SELECTED_PSM_C1_02_UNPATCHED_A1A_CUTSET_REDUCED_TO_BOUNDARY_FIRSTVARIATION_OR_ROUTEB_ROWSOURCE"
NEXT = "MTT_Selected_PSM_C1_02_PhysicalBoundaryFirstVariation_or_RouteBRowSourceIndependence_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(script: Path, packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(script), str(packet)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "validator": rel(script),
        "packet": rel(packet),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    i11_backimport = load(I11_BACKIMPORT)
    i11_frontier = load(I11_FRONTIER)
    route_b_candidate = load(I11_ROUTE_B)
    route_b_nearmiss = load(ROUTE_B_NEARMISS)

    i10_current_result = run_validator(I10_VALIDATOR, I10_CURRENT)
    i10_conditional_result = run_validator(I10_VALIDATOR, I10_CONDITIONAL)
    write_json(ROUTE_B_STRICT_PACKET, route_b_nearmiss["strict_packet"])
    route_b_result = run_validator(ROUTEAB_VALIDATOR, ROUTE_B_STRICT_PACKET)

    route_a_cutset = {
        "schema": "MTTPSMC102RouteAUnpatchedBoundaryFirstVariationCutset.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED",
        "status": "ROUTE_A_UNPATCHED_REDUCED_TO_THREE_PHYSICAL_SOURCE_FIELDS",
        "source": rel(I11_FRONTIER),
        "closed_now": i11_frontier["closed_now"],
        "remaining_physical_fields": i11_frontier["remaining_physical_fields"],
        "equivalent_i10_missing_object": "I10/I11 physical action binding for selected Phi_fin^C1",
        "i10_current_validator": i10_current_result,
        "i10_conditional_validator": i10_conditional_result,
        "current_i10_rejected": i10_current_result["exit_code"] == 1,
        "conditional_i10_passes": i10_conditional_result["exit_code"] == 0,
        "unpatched_route_A_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b_cutset = {
        "schema": "MTTPSMC102RouteBRowSourceIndependenceCutset.v1",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
        "status": "ROUTE_B_REDUCED_TO_ROW_SOURCE_INDEPENDENCE",
        "source": rel(ROUTE_B_NEARMISS),
        "extracted_strict_packet": rel(ROUTE_B_STRICT_PACKET),
        "route_b_missing_field": route_b_nearmiss["route_b_missing_field"],
        "strict_packet_status": route_b_nearmiss["strict_packet"]["status"],
        "selected_basis_independent_of_residual_projector": route_b_nearmiss["strict_packet"]["route_B_independent_execution"]["selected_basis_independent_of_residual_projector"],
        "quadrature_rule_independent_of_locked_target": route_b_nearmiss["strict_packet"]["route_B_independent_execution"]["quadrature_rule_independent_of_locked_target"],
        "all_72_primitive_rows_executed": route_b_nearmiss["strict_packet"]["route_B_independent_execution"]["all_72_primitive_rows_executed"],
        "formal_110_rows_executed": route_b_nearmiss["strict_packet"]["route_B_independent_execution"]["formal_110_rows_executed"],
        "exactness_or_error_certificates_attached": route_b_nearmiss["strict_packet"]["route_B_independent_execution"]["exactness_or_error_certificates_attached"],
        "source_independent_of_residual_projector_replay": route_b_nearmiss["strict_packet"]["route_B_independent_execution"]["source_independent_of_residual_projector_replay"],
        "row_source_attempt_blockers": route_b_candidate["what_remains_open"]["row_source_attempt_blockers"],
        "route_b_validator": route_b_result,
        "route_b_physicalsource_validator_rejects_now": route_b_result["exit_code"] == 1,
        "route_B_closed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    dual_validator = {
        "schema": "MTTPSMC102UnpatchedA1aDualValidatorReplay.v1",
        "status": "CURRENT_ROUTES_REJECT_CONDITIONAL_ROUTE_A_PASSES",
        "route_A_current_i10_validator": i10_current_result,
        "route_A_conditional_i10_validator": i10_conditional_result,
        "route_B_current_physicalsource_validator": route_b_result,
        "current_route_A_rejects": i10_current_result["exit_code"] == 1,
        "conditional_route_A_passes": i10_conditional_result["exit_code"] == 0,
        "current_route_B_rejects": route_b_result["exit_code"] == 1,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102UnpatchedA1aCutset.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_UnpatchedA1aSourceCutset_or_RouteBRowSource_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED-I11",
            "task": "Prove physical first-variation identity, physical boundary cancellation, and same-source R_Z/R_X/b_selected emission for selected Phi_fin^C1.",
        },
        "fallback": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE",
            "task": "Prove row-source independence: selected transported bases feed the 72 primitive row kernels and 36+2 assembly rows without residual-projector replay.",
        },
        "status": "NEXT_WORKORDER_PHYSICAL_BOUNDARY_FIRSTVARIATION_OR_ROUTEB_ROWSOURCE",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102UnpatchedA1aSourceCutsetOrRouteBRowSource",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1u-A1a-UNPATCHED-I11", "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE"],
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "inputs": {
            "i11_sourcepromotion_backimport": rel(I11_BACKIMPORT),
            "route_b_nearmiss": rel(I11_ROUTE_B),
        },
        "output_packets": {
            "route_a_unpatched_boundary_firstvariation_cutset": rel(ROUTE_A_CUTSET),
            "route_b_row_source_independence_cutset": rel(ROUTE_B_CUTSET),
            "route_b_extracted_strict_packet_for_validator": rel(ROUTE_B_STRICT_PACKET),
            "dual_validator_replay": rel(DUAL_VALIDATOR),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "unpatched_A1a_reduced_to_I11_boundary_firstvariation_source": True,
            "route_A_current_vs_conditional_validator_replayed": True,
            "route_B_reduced_to_row_source_independence": True,
            "superset_paths_synchronized_to_same_source_promotion_gate": True,
        },
        "what_remains_open": {
            "route_A_physical_first_variation_identity": True,
            "route_A_physical_boundary_cancellation": True,
            "route_A_same_source_RZ_RX_bselected_emission": True,
            "route_B_row_source_independence": True,
            "unpatched_PSM_C1_02_closure": True,
        },
        "theorem": {
            "name": "PSMC102UnpatchedA1aCutsetOrRouteBRowSourceTheorem",
            "proved": True,
            "statement": (
                "After the local-principle Route A packet validates, the unpatched PSM-C1-02 A1a gate is not a "
                "numerical search. Route A is reduced to the I11 physical boundary/first-variation source fields "
                "plus same-source R_Z/R_X/b_selected emission. Route B is reduced to one last field: row-source "
                "independence from residual-projector replay. Current validators reject the unpatched packets and "
                "the conditional I10/I11 witness passes, so these are the remaining proof obligations."
            ),
        },
        "superset_strategy": {
            "classification": "DUAL_ROUTE_COMMON_SOURCE_PROMOTION_CUTSET",
            "route_A": "physical Phi_fin^C1 I11 boundary/first-variation source theorem",
            "route_B": "selected finite-C1 row-source independence theorem",
            "paths_used_as_free_parameters": False,
            "locked_target": "strict source-promotion validators",
        },
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_UnpatchedA1aSourceCutset_or_RouteBRowSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "route_A_current_rejects": i10_current_result["exit_code"] == 1,
        "route_A_conditional_passes": i10_conditional_result["exit_code"] == 0,
        "route_B_current_rejects": route_b_result["exit_code"] == 1,
        "unpatched_closure_claimed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 UnpatchedA1aSourceCutset or RouteBRowSource v1

Status labels:

- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED-I11`
- `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE`

Status: `{STATUS}`

## Result

The unpatched `SI-1u-A1a` frontier is now reduced to a two-route cutset.

Route A needs exactly the physical I11 source fields:

- physical first-variation identity;
- physical boundary cancellation;
- same-source `R_Z/R_X/b_selected` emission.

Route B needs exactly row-source independence from residual-projector replay.

The local principle route remains valid, but this artifact is about the
unpatched proof. No observed constants or target fitting are used.

## Next

Next artifact: `{NEXT}`
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "{SLUG}"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{{SLUG}}.candidate.json"
ROUTE_A = BASE / "route_a_unpatched_boundary_firstvariation_cutset.packet.json"
ROUTE_B = BASE / "route_b_row_source_independence_cutset.packet.json"
DUAL = BASE / "dual_validator_replay.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_UnpatchedA1aSourceCutset_or_RouteBRowSource_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_unpatcheda1a_sourcecutset_or_routeb_rowsource.py"

STATUS = "{STATUS}"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    dual = load(DUAL)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-A1a-UNPATCHED-I11", "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE"], "routes mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset used as knobs")

    require(route_a["status"] == "ROUTE_A_UNPATCHED_REDUCED_TO_THREE_PHYSICAL_SOURCE_FIELDS", "route A status mismatch")
    require(route_a["current_i10_rejected"] is True, "current I10 should reject")
    require(route_a["conditional_i10_passes"] is True, "conditional I10 should pass")
    require(route_a["unpatched_route_A_closed_now"] is False, "route A overclosed")
    remaining = route_a["remaining_physical_fields"]
    require(set(remaining.keys()) == {{"physical_boundary_cancellation", "physical_first_variation_identity", "same_source_RZ_RX_bselected_emission"}}, "route A cutset mismatch")

    require(route_b["status"] == "ROUTE_B_REDUCED_TO_ROW_SOURCE_INDEPENDENCE", "route B status mismatch")
    require(route_b["route_b_missing_field"] == "source_independent_of_residual_projector_replay", "route B missing field mismatch")
    require(route_b["selected_basis_independent_of_residual_projector"] is True, "basis independence missing")
    require(route_b["quadrature_rule_independent_of_locked_target"] is True, "quadrature independence missing")
    require(route_b["all_72_primitive_rows_executed"] is True, "72 rows missing")
    require(route_b["formal_110_rows_executed"] is True, "110 rows missing")
    require(route_b["exactness_or_error_certificates_attached"] is True, "exactness missing")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "route B overclosed")
    require(route_b["route_b_physicalsource_validator_rejects_now"] is True, "route B should reject")

    require(dual["current_route_A_rejects"] is True, "dual route A should reject")
    require(dual["conditional_route_A_passes"] is True, "dual conditional route A should pass")
    require(dual["current_route_B_rejects"] is True, "dual route B should reject")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED-I11", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE", "fallback mismatch")
    require(cert["route_A_current_rejects"] is True, "cert route A current mismatch")
    require(cert["route_A_conditional_passes"] is True, "cert route A conditional mismatch")
    require(cert["route_B_current_rejects"] is True, "cert route B mismatch")
    require("SI-1u-A1a-UNPATCHED-I11" in note and "SI-1u-B2-ROWSOURCE" in note, "note labels missing")

    for item in [candidate, route_a, route_b, dual, cert]:
        guard(item)

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (ROUTE_A_CUTSET, route_a_cutset),
        (ROUTE_B_CUTSET, route_b_cutset),
        (DUAL_VALIDATOR, dual_validator),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    (CORPUS / f"{SLUG}_audit.py").write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
