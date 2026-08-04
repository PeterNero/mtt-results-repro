"""Attempt the selected Qa/SU3 finite selected-connection source solve."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "selected_qa_su3_finite_selected_connection_solve_packet_attempt_certificate.json"
Q79_PROJECTIVE_VALIDATOR = Q79_REPO / "scripts" / "validate_iwasawa_projective_rhoE_mesh.py"
Q79_PROJECTIVE_CARRIER = Q79_REPO / "candidate_data" / "iwasawa_projective_magnetic_carrier.meshN1.json"
Q79_PROJECTIVE_VALIDATOR_CERT = Q79_REPO / "certificates" / "iwasawa_projective_rhoE_mesh_validator_certificate.json"
Q79_TWIST_HUNT = Q79_REPO / "certificates" / "iwasawa_projective_twist_source_hunt_certificate.json"
Q79_TWIST_PACKET = Q79_REPO / "certificates" / "iwasawa_twisted_source_packet_fill_attempt_certificate.json"
Q79_BLOCK_FACTORIZED = Q79_REPO / "certificates" / "iwasawa_block_factorized_twist_route_certificate.json"
Q79_OPERATOR_BLOCKER = Q79_REPO / "certificates" / "visible_operator_source_blocker_resolution_certificate.json"
Q79_GS_CURVATURE = Q79_REPO / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_finite_selected_connection_source_solve_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_projective_validator() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_PROJECTIVE_VALIDATOR), str(Q79_PROJECTIVE_CARRIER)],
        cwd=Q79_REPO / "scripts",
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    report: dict[str, Any] | None = None
    lines = [line for line in proc.stdout.strip().splitlines() if line]
    for line in lines:
        if line.startswith("projective_report="):
            report = json.loads(line.removeprefix("projective_report="))
    return {"exit_code": proc.returncode, "output": lines, "projective_report": report}


def main() -> None:
    previous = load(PREVIOUS)
    projective_cert = load(Q79_PROJECTIVE_VALIDATOR_CERT)
    twist_hunt = load(Q79_TWIST_HUNT)
    twist_packet = load(Q79_TWIST_PACKET)
    block = load(Q79_BLOCK_FACTORIZED)
    operator = load(Q79_OPERATOR_BLOCKER)
    gs = load(Q79_GS_CURVATURE)
    projective_validation = run_projective_validator()

    projective_mesh_passes = (
        projective_validation["exit_code"] == 0
        and projective_validation["projective_report"] is not None
        and projective_validation["projective_report"]["projective_gerbe_gluing_passes"] is True
        and projective_validation["projective_report"]["central_twist_is_nontrivial"] is True
    )
    twist_source_missing = (
        twist_hunt["verdict"]["selected_projective_twist_source_found"] is False
        and twist_packet["verdict"]["promotion_packet_passes"] is False
        and twist_packet["unfilled_fields"]["selected_visible_operator_source_packet"] is True
    )
    block_factorized_architecture_valid = (
        block["verdict"]["block_factorized_route_is_correct_next_architecture"] is True
        and twist_packet["block_factorized_resolution"]["finite_sector_projectors_filled"] is True
        and twist_packet["block_factorized_resolution"]["separate_higgs_line_validated"] is True
    )
    operator_source_missing = (
        operator["calculation_results"]["source_hunt_found_selected_D_E"] is False
        and operator["irreducible_cut_set"]["selected_visible_sm_bundle_model"]["currently_supplied"] is False
        and operator["irreducible_cut_set"]["matter_operator_source_constructed"]["currently_supplied"] is False
    )
    curvature_not_operator = (
        gs["calculation_results"]["visible_green_schwarz_curvature_verified"] is True
        and gs["calculation_results"]["selected_visible_operator_source_verified"] is False
    )

    attempts = {
        "ordinary_route_c_smoke": {
            "result": "REJECTED_AS_SELECTED_SOURCE",
            "reason": "Finite matrices can satisfy downstream algebra only after selected flags are lifted; honest source gate rejects selected_source_verified=false.",
            "can_close_selected_source": False,
        },
        "projective_qutrit_gerbe_rhoE": {
            "result": "PROJECTIVE_MESH_VALID_SELECTED_MAP_OPEN",
            "projective_mesh_passes": projective_mesh_passes,
            "reason": "The nontrivial qutrit carrier validates as projective gerbe gluing, but the selected Deligne/B-field-to-rhoE and operator-source map is not supplied.",
            "can_close_selected_source": False,
        },
        "block_factorized_family_plus_higgs": {
            "result": "ARCHITECTURE_VALID_OPERATOR_SOURCE_OPEN",
            "block_factorized_architecture_valid": block_factorized_architecture_valid,
            "reason": "Family qutrit and separate Higgs line solve the projector architecture, but coherent spectral projector retention still requires selected D_E/dotD.",
            "can_close_selected_source": False,
        },
        "visible_green_schwarz_curvature_route": {
            "result": "CURVATURE_CLOSED_OPERATOR_OPEN",
            "curvature_not_operator": curvature_not_operator,
            "reason": "The visible Green-Schwarz curvature row is closed, but it has not been promoted to a selected visible SM operator source.",
            "can_close_selected_source": False,
        },
    }

    output = {
        "certificate": "SelectedQaSU3FiniteSelectedConnectionSourceSolveAttempt",
        "status": "QA_SU3_SELECTED_CONNECTION_SOURCE_SOLVE_ATTEMPT_BLOCKED_BY_SELECTED_OPERATOR_SOURCE",
        "inputs": {
            "previous_packet_gate": str(PREVIOUS.relative_to(ROOT)),
            "projective_carrier": str(Q79_PROJECTIVE_CARRIER),
            "projective_validator_certificate": str(Q79_PROJECTIVE_VALIDATOR_CERT),
            "projective_twist_source_hunt": str(Q79_TWIST_HUNT),
            "twisted_source_packet_fill_attempt": str(Q79_TWIST_PACKET),
            "block_factorized_twist_route": str(Q79_BLOCK_FACTORIZED),
            "visible_operator_source_blocker": str(Q79_OPERATOR_BLOCKER),
            "visible_green_schwarz_curvature": str(Q79_GS_CURVATURE),
        },
        "projective_validator_result": projective_validation,
        "attempts": attempts,
        "closed_now": {
            "projective_qutrit_mesh_validated": projective_mesh_passes,
            "block_factorized_family_higgs_architecture_validated": block_factorized_architecture_valid,
            "visible_green_schwarz_curvature_available": gs["what_this_closes"]["selected_visible_GS_curvature_packet"] is True,
            "current_smoke_rejected_as_proof_source": previous["attempt_result"]["current_smoke_can_be_promoted"] is False,
        },
        "not_closed": {
            "selected_projective_twist_to_Deligne_B_field_map": twist_hunt["missing_for_projective_carrier_selection"][
                "explicit_projective_cocycle_to_Deligne_gerbe_map"
            ],
            "selected_twisted_Bianchi_residual_certificate": twist_hunt["missing_for_projective_carrier_selection"][
                "twisted_Bianchi_residual_certificate"
            ],
            "selected_visible_operator_source_packet": twist_packet["unfilled_fields"][
                "selected_visible_operator_source_packet"
            ],
            "selected_visible_SM_bundle_or_sheaf_model": operator["irreducible_cut_set"][
                "selected_visible_sm_bundle_model"
            ]["currently_supplied"]
            is False,
            "selected_D_E_dotD_Riesz_Green": operator["irreducible_cut_set"][
                "sector_selected_D_E_flags"
            ]["currently_supplied"]
            is False,
            "primitive_C1_contractions": True,
            "full_Qa_SU3_or_SM_closure": True,
        },
        "minimal_obstruction": {
            "name": "selected_visible_operator_source_packet",
            "statement": (
                "The finite/projective/block-factorized algebra can be made consistent, "
                "and the selected curvature source exists, but current corpus data do not "
                "supply a selected visible SM bundle/sheaf or selected D_E/dotD operator "
                "source. This is a genuine missing source object, not a numeric solve failure."
            ),
            "needed_to_close": operator["minimal_new_data_that_would_close"],
        },
        "guardrails": {
            "claims_selected_source_solved": False,
            "claims_selected_D_E_constructed": False,
            "claims_full_SM_closure": False,
            "promotes_projective_fixture_as_selected": False,
            "uses_observed_masses_or_mixings": False,
            "uses_execution_ii_benchmarks": False,
        },
        "gate_result": {
            "selected_connection_source_solved": False,
            "all_current_non_source_blockers_reduced": projective_mesh_passes
            and block_factorized_architecture_valid
            and curvature_not_operator
            and twist_source_missing
            and operator_source_missing,
            "next_step_is_new_selected_operator_source_packet": True,
            "target_fitting_used": False,
        },
    }

    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
