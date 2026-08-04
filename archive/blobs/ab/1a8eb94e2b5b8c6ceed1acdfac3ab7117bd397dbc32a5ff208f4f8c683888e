"""Attempt to fill the selected S3 class/restriction packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

TEMPLATE = CERTIFICATES / "visible_twisted_s3_class_restriction_packet.template.json"
ATTEMPT = CERTIFICATES / "visible_twisted_s3_class_restriction_packet.attempt.json"
CANDIDATE = CANDIDATE_DATA / "visible_twisted_s3_class_restriction_packet_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_twisted_s3_class_restriction_packet_attempt_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_visible_twisted_s3_class_restriction_packet.py"

COVER_GAUGE_CERT = CERTIFICATES / "iwasawa_deligne_cover_gauge_reduction_certificate.json"
FINITE_CP_CERT = CERTIFICATES / "visible_twisted_s3_finite_cp_cancellation_certificate.json"
SPINC_CERT = CERTIFICATES / "visible_complex_worldvolume_spinc_gate_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def base_packet(status: str) -> dict[str, Any]:
    return {
        "schema": "VisibleTwistedS3ClassRestrictionPacket.v1",
        "status": status,
        "selected_stack": "S3",
        "branch": {
            "q": 79,
            "orientation": "F",
            "torsion_label_m": 1,
            "same_branch_q79_f_m1": True,
        },
        "fixture_only": False,
        "uses_observed_flavor_data": False,
        "uses_benchmark_flavor_entries": False,
        "uses_projective_prototype_as_selected": False,
        "class_data": {
            "cover_choice_auxiliary_not_selected_knob": None,
            "fixed_smooth_flat_gerbe_class": None,
            "same_class_as_finite_m1_deck_cocycle": None,
            "map_to_qutrit_central_cocycle_verified": None,
            "curvature_H_form": "0",
            "central_phase_label": "zeta_3^2",
            "differential_cohomology_class_certificate": None,
        },
        "s3_restriction": {
            "S3_pullback_table_supplied": None,
            "S3_active_image_rank_over_F3": None,
            "S3_B_restriction_nonzero_ordinary_DD": None,
            "twisted_CP_module_supplied": None,
            "twisted_CP_DD_matches_B_restriction": None,
            "finite_total_twisted_DD_class_zero": None,
            "W3_spinC_zero": None,
            "smooth_Freed_Witten_cancellation_verified": None,
        },
        "projector_retention": {
            "block_factorized_projectors_supplied": None,
            "projector_retention_proved_for_selected_source": None,
            "family_higgs_blocks_retained": None,
        },
    }


def template_packet() -> dict[str, Any]:
    packet = base_packet("OPEN")
    packet["selected_stack"] = None
    return packet


def attempt_packet() -> dict[str, Any]:
    cover = load_json(COVER_GAUGE_CERT)
    finite = load_json(FINITE_CP_CERT)
    spinc = load_json(SPINC_CERT)
    report = finite.get("s3_cancellation_reports", [{}])[0]
    packet = base_packet("ATTEMPT_BLOCKED_SMOOTH_CLASS_RESTRICTION_PROJECTORS_OPEN")
    packet["class_data"].update(
        {
            "cover_choice_auxiliary_not_selected_knob": cover.get("what_this_closes", {}).get(
                "good_cover_is_execution_scaffold_not_physical_knob"
            )
            is True,
            "fixed_smooth_flat_gerbe_class": False,
            "same_class_as_finite_m1_deck_cocycle": False,
            "map_to_qutrit_central_cocycle_verified": False,
            "differential_cohomology_class_certificate": "visible_twisted_s3_class_restriction_packet_attempt_certificate.json",
        }
    )
    packet["s3_restriction"].update(
        {
            "S3_pullback_table_supplied": False,
            "S3_active_image_rank_over_F3": report.get("S3_active_image_rank_over_F3"),
            "S3_B_restriction_nonzero_ordinary_DD": report.get("ordinary_DD_gate_for_S3")
            is False,
            "twisted_CP_module_supplied": report.get("finite_twisted_CP_module_on_S3") is True,
            "twisted_CP_DD_matches_B_restriction": report.get(
                "finite_twisted_CP_DD_class_matches_B_restriction"
            )
            is True,
            "finite_total_twisted_DD_class_zero": report.get("finite_total_twisted_DD_class_zero")
            is True,
            "W3_spinC_zero": spinc.get("worldvolume_class", {})
            .get("gauge_stack_divisors", [{}])[2]
            .get("W3_zero")
            is True,
            "smooth_Freed_Witten_cancellation_verified": False,
        }
    )
    packet["projector_retention"].update(
        {
            "block_factorized_projectors_supplied": True,
            "projector_retention_proved_for_selected_source": False,
            "family_higgs_blocks_retained": False,
        }
    )
    return packet


def attempt_report() -> dict[str, Any]:
    write_json(TEMPLATE, template_packet())
    packet = attempt_packet()
    write_json(ATTEMPT, packet)
    template_exit, template_output = run_validator(TEMPLATE)
    attempt_exit, attempt_output = run_validator(ATTEMPT)
    finite = load_json(FINITE_CP_CERT)

    return {
        "candidate": "VisibleTwistedS3ClassRestrictionPacketAttempt",
        "status": "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_PACKET_ATTEMPT_BLOCKED_SMOOTH_CLASS_PROJECTORS_OPEN",
        "generated_by": "scripts/attempt_visible_twisted_s3_class_restriction_packet.py",
        "validator": "scripts/validate_visible_twisted_s3_class_restriction_packet.py",
        "template": "certificates/visible_twisted_s3_class_restriction_packet.template.json",
        "attempt_packet": "certificates/visible_twisted_s3_class_restriction_packet.attempt.json",
        "inputs": {
            "cover_gauge_reduction_certificate": "iwasawa_deligne_cover_gauge_reduction_certificate.json",
            "finite_cp_cancellation_certificate": "visible_twisted_s3_finite_cp_cancellation_certificate.json",
            "spinc_certificate": "visible_complex_worldvolume_spinc_gate_certificate.json",
        },
        "attempt_summary": {
            "cover_choice_auxiliary_closed": packet["class_data"][
                "cover_choice_auxiliary_not_selected_knob"
            ],
            "finite_S3_CP_cancellation_closed": finite.get("calculation_results", {}).get(
                "finite_S3_CP_cancellation_closed"
            ),
            "S3_active_image_rank_over_F3": packet["s3_restriction"][
                "S3_active_image_rank_over_F3"
            ],
            "finite_twisted_DD_cancellation_zero": packet["s3_restriction"][
                "finite_total_twisted_DD_class_zero"
            ],
            "W3_spinC_zero": packet["s3_restriction"]["W3_spinC_zero"],
            "fixed_smooth_flat_gerbe_class": packet["class_data"][
                "fixed_smooth_flat_gerbe_class"
            ],
            "S3_pullback_table_supplied": packet["s3_restriction"][
                "S3_pullback_table_supplied"
            ],
            "smooth_Freed_Witten_cancellation_verified": packet["s3_restriction"][
                "smooth_Freed_Witten_cancellation_verified"
            ],
            "projector_retention_proved": packet["projector_retention"][
                "projector_retention_proved_for_selected_source"
            ],
        },
        "validator_result": {
            "template_exit_code": template_exit,
            "template_output_head": template_output.splitlines()[:8],
            "attempt_exit_code": attempt_exit,
            "attempt_output_head": attempt_output.splitlines()[:30],
        },
        "calculation_results": {
            "class_restriction_schema_and_validator_created": True,
            "template_refused_as_open": template_exit == 2,
            "attempt_refused_until_smooth_class_and_projectors": attempt_exit == 1,
            "finite_S3_inputs_carried_forward": True,
            "selected_smooth_S3_class_restriction_packet_constructed": False,
            "smooth_Freed_Witten_cancellation_closed": False,
            "projector_retention_closed": False,
        },
        "what_this_closes": {
            "executable_selected_S3_class_restriction_gate": True,
            "finite_S3_CP_and_W3_inputs_inserted_into_gate": True,
            "proof_that_cover_gauge_reduction_does_not_yet_imply_smooth_source": attempt_exit == 1,
        },
        "still_open": {
            "fixed_smooth_flat_gerbe_class": True,
            "S3_pullback_restriction_table": True,
            "map_to_qutrit_central_cocycle_at_smooth_level": True,
            "smooth_Freed_Witten_cancellation": True,
            "block_sector_projector_retention": True,
            "selected_visible_operator_source": True,
            "selected_D_E_dotD": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_smooth_S3_source": False,
            "claims_smooth_Freed_Witten_closed": False,
            "claims_projector_retention": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The finite S3 twisted-CP cancellation, W3/spinC input, and "
                "cover-gauge reduction now fit into one executable selected "
                "S3 class/restriction gate. The attempt is still blocked "
                "because the fixed smooth S3 class, its pullback table, smooth "
                "Freed-Witten cancellation, and projector retention are not "
                "supplied."
            ),
            "next_closing_object": (
                "Supply the smooth S3 pullback/restriction table and prove "
                "projector retention for the block-factorized family/Higgs "
                "sectors on that same selected source."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleTwistedS3ClassRestrictionPacketAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_twisted_s3_class_restriction_packet_attempt.candidate.json",
        "validator": report["validator"],
        "template": report["template"],
        "attempt_packet": report["attempt_packet"],
        "inputs": report["inputs"],
        "attempt_summary": report["attempt_summary"],
        "validator_result": report["validator_result"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)


def main() -> int:
    report = attempt_report()
    write_outputs(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
