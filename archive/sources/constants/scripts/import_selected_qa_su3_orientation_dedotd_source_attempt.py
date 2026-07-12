"""Import the q79 orientation-carrying D_E/dotD source attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
Q79_CERTS = Q79 / "certificates"
Q79_CANDIDATES = Q79 / "candidate_data"

TERMINAL_SOURCE = CERTS / "selected_terminal_monad_lane_source_selector_attempt_certificate.json"
COMMON_PAYLOAD = CERTS / "common_de_dotd_riesz_green_payload_map_certificate.json"
SYMMETRY_TRIAGE = CERTS / "selected_qa_su3_symmetry_breaking_route_triage_certificate.json"

Q79_ATTEMPT = Q79_CERTS / "selected_qa_su3_orientation_dedotd_source_attempt_certificate.json"
Q79_PACKET = Q79_CANDIDATES / "selected_qa_su3_orientation_dedotd_source.current_attempt.json"
Q79_VALIDATOR = Q79 / "scripts" / "validate_selected_qa_su3_orientation_dedotd_source_packet.py"
Q79_DE_VALIDATOR = Q79_CERTS / "iwasawa_de_action_validator_certificate.json"
Q79_DOTD_VALIDATOR = Q79_CERTS / "iwasawa_dotd_response_validator_certificate.json"
Q79_ORIENTATION = Q79_CERTS / "iwasawa_orientation_de_dotd_bridge_certificate.json"

OUTPUT_CERT = CERTS / "selected_qa_su3_orientation_dedotd_source_attempt_import_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_packet() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(Q79_VALIDATOR), str(Q79_PACKET)],
        cwd=Q79,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    prefix = "selected_qa_su3_orientation_dedotd_source_report="
    parsed = None
    for line in proc.stdout.splitlines():
        if line.startswith(prefix):
            parsed = json.loads(line[len(prefix) :])
            break
    return {"exit_code": proc.returncode, "stdout": proc.stdout, "parsed_report": parsed}


def main() -> None:
    terminal = load(TERMINAL_SOURCE)
    common = load(COMMON_PAYLOAD)
    triage = load(SYMMETRY_TRIAGE)
    q79_attempt = load(Q79_ATTEMPT)
    q79_packet = load(Q79_PACKET)
    de_validator = load(Q79_DE_VALIDATOR)
    dotd_validator = load(Q79_DOTD_VALIDATOR)
    orientation = load(Q79_ORIENTATION)
    validation = validate_packet()
    parsed = validation["parsed_report"] or {}

    first_open = q79_attempt["first_open_items"]
    source_origin_open = all(
        item in first_open
        for item in [
            "selected_by_mtt must be true",
            "visible_bundle_or_twisted_gerbe_source must be true",
            "pic0_selected_or_quotiented must be true",
            "selection_justified_by_source must be true",
            "same_branch_derivative_verified must be true",
        ]
    )
    finite_validators_exist = (
        de_validator["what_this_closes"]["finite_D_E_action_validator"] is True
        and dotd_validator["what_this_closes"]["finite_dotD_response_validator"] is True
    )
    branch_pair_reaches_operator_layer = (
        q79_attempt["calculation_results"]["both_branch_packets_exist"] is True
        and q79_attempt["calculation_results"]["q79_finite_equations_blocked_only_by_source_flags"] is True
        and q79_attempt["calculation_results"]["q369_finite_equations_blocked_only_by_source_flags"] is True
    )

    output = {
        "certificate": "SelectedQaSU3OrientationDEDotDSourceAttemptImport",
        "status": "QA_SU3_ORIENTATION_DEDOTD_SOURCE_ATTEMPT_IMPORTED_SOURCE_ORIGIN_OPEN",
        "inputs": {
            "terminal_lane_source_selector_reduction": str(TERMINAL_SOURCE.relative_to(ROOT)),
            "common_payload_map": str(COMMON_PAYLOAD.relative_to(ROOT)),
            "local_symmetry_breaking_triage": str(SYMMETRY_TRIAGE.relative_to(ROOT)),
            "q79_orientation_dedotd_attempt": str(Q79_ATTEMPT),
            "q79_orientation_dedotd_packet": str(Q79_PACKET),
            "q79_orientation_dedotd_validator": str(Q79_VALIDATOR),
            "q79_de_action_validator": str(Q79_DE_VALIDATOR),
            "q79_dotd_response_validator": str(Q79_DOTD_VALIDATOR),
            "q79_orientation_bridge": str(Q79_ORIENTATION),
        },
        "closed_now": {
            "orientation_dedotd_validator_available": q79_attempt["what_this_closes"][
                "orientation_dedotd_packet_validator_created"
            ],
            "finite_branch_data_reaches_DE_Green_dotD_layer": q79_attempt["what_this_closes"][
                "finite_branch_data_reaches_validator_layer"
            ],
            "q79_and_q369_branch_packets_checked": q79_attempt["what_this_closes"][
                "conjugate_q369_branch_checked_in_parallel"
            ],
            "finite_DE_and_dotD_validator_schemas_closed": finite_validators_exist,
            "source_flags_identified_as_blocker": q79_attempt["what_this_closes"][
                "source_flags_identified_as_blocker"
            ],
            "local_terminal_source_gate_knows_DE_dotD_is_live_route": terminal["candidate_routes"][
                "R4_same_source_DE_dotD_Riesz_Green"
            ]["status"]
            == "OPEN_REQUIRED_BREAKING_SOURCE",
        },
        "validator_replay": {
            "exit_code": validation["exit_code"],
            "status": parsed.get("status"),
            "first_open_items": parsed.get("open_items", [])[:12],
            "subvalidator_exit_codes": {
                key: value.get("exit_code")
                for key, value in parsed.get("subvalidators", {}).items()
            },
        },
        "branch_status": {
            "current_q79_orientation": {
                "torsion_label_m": 1,
                "global_cp_label": 79,
                "finite_equations_blocked_only_by_source_flags": q79_attempt["calculation_results"][
                    "q79_finite_equations_blocked_only_by_source_flags"
                ],
            },
            "conjugate_q369_orientation": {
                "torsion_label_m": 2,
                "global_cp_label": 369,
                "finite_equations_blocked_only_by_source_flags": q79_attempt["calculation_results"][
                    "q369_finite_equations_blocked_only_by_source_flags"
                ],
            },
            "orientation_bridge_status": orientation["status"],
            "unique_branch_selected_now": orientation["calculation_results"][
                "unique_branch_selected_now"
            ],
        },
        "why_it_does_not_close": {
            "source_origin_open": source_origin_open,
            "validator_exit_code_open": validation["exit_code"] == 2,
            "selected_source_origin_constructed": q79_attempt["calculation_results"][
                "selected_source_origin_constructed"
            ],
            "unique_m_label_selected_by_source": q79_attempt["calculation_results"][
                "unique_m_label_selected_by_source"
            ],
            "selected_D_E_or_dotD_source_flags": q79_attempt["what_this_does_not_close"][
                "selected_D_E_or_dotD_source_flags"
            ]
            is False,
        },
        "next_closing_object": {
            "name": "Selected_Source_Origin_or_Antiunitary_DEDotD_Equivalence_v1",
            "route_A_selected_source_origin": [
                "construct a genuine selected visible bundle/twisted-gerbe/Route-C source certificate",
                "turn selected_by_mtt, visible_bundle_or_twisted_gerbe_source, Pic0 quotient/selection, and projector-retention flags on from source proof",
                "verify same_branch_derivative for the alpha1 dotD driver",
                "rerun q79 orientation D_E/dotD packet validator to PASS for exactly one branch",
            ],
            "route_B_equivalence_then_retarded_selection": [
                "prove q79 and q369 packets are antiunitarily equivalent before retarded boundary selection",
                "show all D_E, Green, Riesz, dotD, and primitive C1 contractions transform by conjugation",
                "supply a non-observed retarded/source boundary condition selecting one orientation",
            ],
            "reason": (
                "The matrix-shape layer is no longer the main obstruction. "
                "The source origin and same-branch alpha1-driver proof are."
            ),
        },
        "not_closed": {
            "selected_source_origin": True,
            "unique_m1_vs_m2_selection": True,
            "selected_D_E_or_dotD_source_flags": True,
            "same_source_base_order_breaker": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_source_origin": False,
            "claims_unique_m_label_now": False,
            "claims_selected_D_E_or_dotD": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
            "uses_lifted_selected_flags_as_proof": False,
        },
        "honest_answer": (
            "The D_E/dotD route is now executable but still open: q79 and q369 "
            "finite packets reach the selected D_E, Green, and dotD validators, "
            "yet both are rejected at selected-source and same-branch driver flags. "
            "The next proof is therefore source-origin selection, or antiunitary "
            "equivalence plus a non-observed retarded selector."
        ),
    }

    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
