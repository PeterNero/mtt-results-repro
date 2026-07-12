"""Attempt the smooth selected lift of the finite S3 twisted source."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

TEMPLATE = CERTIFICATES / "visible_twisted_s3_smooth_source_lift.template.json"
ATTEMPT = CERTIFICATES / "visible_twisted_s3_smooth_source_lift.attempt.json"
CANDIDATE = CANDIDATE_DATA / "visible_twisted_s3_smooth_source_lift_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_visible_twisted_s3_smooth_source_lift.py"

FINITE_CP_CERT = CERTIFICATES / "visible_twisted_s3_finite_cp_cancellation_certificate.json"
FLAT_GERBE_CERT = CERTIFICATES / "time_oriented_m1_flat_gerbe_promotion_certificate.json"
STANDARD_DECK_CERT = CERTIFICATES / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
VISIBLE_SOURCE_PACKET_CERT = CERTIFICATES / "visible_twisted_s3_source_packet_attempt_certificate.json"


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
        "schema": "VisibleTwistedS3SmoothSourceLift.v1",
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
        "finite_inputs": {
            "finite_S3_CP_cancellation_closed": True,
            "conditional_flat_gerbe_representative_exists": True,
            "qutrit_projective_module_compatible": True,
            "ordinary_matter_curves_retained": True,
            "central_phase_label": "zeta_3^2",
        },
        "smooth_source": {
            "source_kind": "flat_Deligne_Cech_gerbe_plus_twisted_CP",
            "source_selected_by_mtt": None,
            "selected_cover_or_scaffold_verified": None,
            "good_cover_data_supplied": None,
            "deligne_cech_representative_constructed": None,
            "fixed_differential_cohomology_class": None,
            "restricts_to_selected_S3_worldvolume": None,
            "map_to_qutrit_central_cocycle_verified": None,
            "smooth_twisted_CP_or_worldvolume_flux_constructed": None,
            "curvature_H_form": "0",
            "source_certificate": None,
        },
        "consistency": {
            "green_schwarz_flat_H_preservation_closed": True,
            "green_schwarz_bianchi_verified_for_smooth_S3_source": None,
            "freed_witten_verified_for_smooth_S3_source": None,
            "twisted_projector_retention_verified": None,
            "block_factorized_family_higgs_projectors_retained": None,
        },
        "downstream_not_required_for_lift_gate": {
            "selected_visible_operator_source_open": True,
            "selected_D_E_dotD_open": True,
            "primitive_C1_contractions_open": True,
        },
    }


def template_packet() -> dict[str, Any]:
    packet = base_packet("OPEN")
    packet["selected_stack"] = None
    return packet


def attempt_packet() -> dict[str, Any]:
    flat = load_json(FLAT_GERBE_CERT)
    deck = load_json(STANDARD_DECK_CERT)
    packet = base_packet("ATTEMPT_BLOCKED_SELECTED_COVER_PROJECTORS_OPEN")
    scaffold_selected = (
        flat.get("aspherical_nilmanifold_route", {}).get(
            "standard_deck_scaffold_selected_by_current_certificates"
        )
        is True
        or deck.get("guardrails", {}).get("claims_Gamma0_is_MTT_selected") is True
    )
    packet["smooth_source"].update(
        {
            "source_selected_by_mtt": False,
            "selected_cover_or_scaffold_verified": scaffold_selected,
            "good_cover_data_supplied": False,
            "deligne_cech_representative_constructed": flat.get("calculation_results", {}).get(
                "conditional_flat_gerbe_representative_exists"
            )
            is True,
            "fixed_differential_cohomology_class": False,
            "restricts_to_selected_S3_worldvolume": False,
            "map_to_qutrit_central_cocycle_verified": False,
            "smooth_twisted_CP_or_worldvolume_flux_constructed": False,
            "source_certificate": "visible_twisted_s3_smooth_source_lift_attempt_certificate.json",
            "current_blocker": (
                "finite S3 cancellation plus conditional flat gerbe exists, "
                "but the selected cover/good-cover data, fixed smooth "
                "differential-cohomology class, S3 restriction, Freed-Witten "
                "verification, and projector retention are not supplied"
            ),
        }
    )
    packet["consistency"].update(
        {
            "green_schwarz_bianchi_verified_for_smooth_S3_source": False,
            "freed_witten_verified_for_smooth_S3_source": False,
            "twisted_projector_retention_verified": False,
            "block_factorized_family_higgs_projectors_retained": False,
        }
    )
    return packet


def attempt_report() -> dict[str, Any]:
    finite = load_json(FINITE_CP_CERT)
    flat = load_json(FLAT_GERBE_CERT)
    source_packet = load_json(VISIBLE_SOURCE_PACKET_CERT)
    deck = load_json(STANDARD_DECK_CERT)
    write_json(TEMPLATE, template_packet())
    packet = attempt_packet()
    write_json(ATTEMPT, packet)
    validator_exit, validator_output = run_validator(ATTEMPT)
    template_exit, template_output = run_validator(TEMPLATE)

    conditional_smooth_model = (
        flat.get("calculation_results", {}).get("conditional_flat_gerbe_representative_exists")
        is True
        and finite.get("calculation_results", {}).get("finite_S3_CP_cancellation_closed") is True
    )

    return {
        "candidate": "VisibleTwistedS3SmoothSourceLiftAttempt",
        "status": "VISIBLE_TWISTED_S3_SMOOTH_SOURCE_LIFT_ATTEMPT_BLOCKED_SELECTED_COVER_PROJECTORS_OPEN",
        "generated_by": "scripts/attempt_visible_twisted_s3_smooth_source_lift.py",
        "template": "certificates/visible_twisted_s3_smooth_source_lift.template.json",
        "attempt_packet": "certificates/visible_twisted_s3_smooth_source_lift.attempt.json",
        "validator": "scripts/validate_visible_twisted_s3_smooth_source_lift.py",
        "inputs": {
            "finite_cp_cancellation_certificate": "visible_twisted_s3_finite_cp_cancellation_certificate.json",
            "flat_gerbe_promotion_certificate": "time_oriented_m1_flat_gerbe_promotion_certificate.json",
            "standard_deck_scaffold_certificate": "iwasawa_standard_lattice_deck_scaffold_certificate.json",
            "visible_s3_source_packet_attempt_certificate": "visible_twisted_s3_source_packet_attempt_certificate.json",
        },
        "smooth_lift_attempt": {
            "conditional_flat_gerbe_representative_exists": flat.get("calculation_results", {}).get(
                "conditional_flat_gerbe_representative_exists"
            ),
            "finite_S3_CP_cancellation_closed": finite.get("calculation_results", {}).get(
                "finite_S3_CP_cancellation_closed"
            ),
            "standard_deck_scaffold_valid": deck.get("verified_algebra", {}).get(
                "coframe_invariant_under_left_deck_action"
            )
            is True,
            "standard_deck_scaffold_selected": flat.get("aspherical_nilmanifold_route", {}).get(
                "standard_deck_scaffold_selected_by_current_certificates"
            ),
            "source_packet_status": source_packet.get("status"),
            "source_selected_by_mtt": packet["smooth_source"]["source_selected_by_mtt"],
            "selected_cover_or_scaffold_verified": packet["smooth_source"][
                "selected_cover_or_scaffold_verified"
            ],
            "fixed_differential_cohomology_class": packet["smooth_source"][
                "fixed_differential_cohomology_class"
            ],
            "freed_witten_verified_for_smooth_S3_source": packet["consistency"][
                "freed_witten_verified_for_smooth_S3_source"
            ],
            "twisted_projector_retention_verified": packet["consistency"][
                "twisted_projector_retention_verified"
            ],
        },
        "validator_result": {
            "attempt_exit_code": validator_exit,
            "attempt_output_head": validator_output.splitlines()[:30],
            "template_exit_code": template_exit,
            "template_output_head": template_output.splitlines()[:8],
        },
        "calculation_results": {
            "smooth_source_lift_schema_and_validator_created": True,
            "template_refused_as_open": template_exit == 2,
            "attempt_refused_until_selected_cover_and_projectors": validator_exit == 1,
            "conditional_smooth_flat_S3_model_available": conditional_smooth_model,
            "finite_S3_CP_cancellation_carried_into_lift": True,
            "selected_smooth_S3_source_constructed": False,
            "smooth_S3_Freed_Witten_closed": False,
            "smooth_S3_projector_retention_closed": False,
        },
        "what_this_closes": {
            "executable_smooth_S3_source_lift_gate": True,
            "conditional_flat_Deligne_Cech_model_attached_to_S3_finite_CP": conditional_smooth_model,
            "proof_that_finite_cancellation_does_not_yet_promote_smooth_source": validator_exit == 1,
        },
        "still_open": {
            "MTT_selected_cover_or_scaffold": True,
            "actual_good_cover_data": True,
            "fixed_smooth_S3_differential_cohomology_class": True,
            "S3_restriction_of_smooth_gerbe_or_flux": True,
            "smooth_S3_Green_Schwarz_Bianchi_verification": True,
            "smooth_S3_Freed_Witten_verification": True,
            "smooth_S3_twisted_projector_retention": True,
            "selected_visible_operator_source": True,
            "selected_D_E_dotD": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_smooth_S3_source": False,
            "claims_selected_cover": False,
            "claims_full_Freed_Witten_closed": False,
            "claims_projector_retention": False,
            "claims_visible_operator_source_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The finite S3 twisted-CP cancellation and conditional flat "
                "Deligne/Cech gerbe now combine into a precise conditional "
                "smooth-source model. It is not selected yet because the "
                "cover/scaffold, good-cover data, smooth S3 restriction, "
                "Freed-Witten check, and projector retention are absent."
            ),
            "next_closing_object": (
                "Select the Iwasawa cover/scaffold or provide an equivalent "
                "good-cover Deligne/Cech representative, then verify its S3 "
                "restriction, smooth Freed-Witten condition, and block-sector "
                "projector retention."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleTwistedS3SmoothSourceLiftAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_twisted_s3_smooth_source_lift_attempt.candidate.json",
        "template": report["template"],
        "attempt_packet": report["attempt_packet"],
        "validator": report["validator"],
        "inputs": report["inputs"],
        "smooth_lift_attempt": report["smooth_lift_attempt"],
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
