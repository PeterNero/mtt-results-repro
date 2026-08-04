"""Attempt to construct the selected S3 twisted D7 source packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

TEMPLATE = CERTIFICATES / "visible_twisted_s3_source_packet.template.json"
ATTEMPT = CERTIFICATES / "visible_twisted_s3_source_packet.attempt.json"
CANDIDATE = CANDIDATE_DATA / "visible_twisted_s3_source_packet_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_twisted_s3_source_packet_attempt_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_visible_twisted_s3_source_packet.py"

S3_SELECTOR_CERT = CERTIFICATES / "visible_twisted_d7_equivariant_embedding_selector_certificate.json"
CP_RESCUE_CERT = CERTIFICATES / "visible_twisted_chan_paton_rescue_certificate.json"


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
        "schema": "VisibleTwistedS3SourcePacket.v1",
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
        "selector_evidence": {
            "equivariant_selector_certificate": "visible_twisted_d7_equivariant_embedding_selector_certificate.json",
            "minimal_equivariant_twisted_D7_stack_selector": "S3",
            "selected_stack_by_mtt": True,
            "S1_S2_require_extra_selected_orientation_breaking_source": True,
        },
        "finite_gerbe_evidence": {
            "finite_period_table_closed": True,
            "deck_cech_lift_closed": True,
            "conditional_flat_gerbe_closed": True,
            "period_denominator": 3,
            "central_phase_label": "zeta_3^2",
            "base_group": "F_3^2",
            "qutrit_commutator_matches_m1_twist": True,
            "finite_projective_CP_module_matches_m1_twist": True,
        },
        "worldvolume_evidence": {
            "twisted_projective_D7_stack": "S3",
            "active_pair": ["T1", "T2"],
            "S3_active_image_rank_over_F3": 2,
            "rank_two_DD_requires_twisted_source": True,
            "ordinary_DD_zero_D7_stacks": ["S1", "S2"],
            "ordinary_DD_zero_matter_curves": ["C12", "C23", "C31"],
            "W3_spinC_zero_for_visible_cycles": True,
        },
        "source_evidence": {
            "source_kind": "Deligne_Cech_gerbe",
            "source_selected_by_mtt": None,
            "fixed_differential_cohomology_class": None,
            "geometric_Deligne_Cech_or_worldvolume_flux_source_constructed": None,
            "physical_worldvolume_flux_or_twisted_CP_source_constructed": None,
            "map_to_central_cocycle_verified": None,
            "source_certificate": None,
        },
        "consistency_evidence": {
            "green_schwarz_flat_H_preservation_gate_closed": True,
            "green_schwarz_bianchi_verified_for_S3_source": None,
            "freed_witten_verified_for_S3_source": None,
            "twisted_projector_retention_verified": None,
        },
        "downstream_not_required_for_source_gate": {
            "selected_visible_operator_source_open": True,
            "selected_D_E_dotD_open": True,
            "primitive_C1_contractions_open": True,
        },
    }


def template_packet() -> dict[str, Any]:
    packet = base_packet("OPEN")
    packet["selected_stack"] = None
    packet["selector_evidence"]["selected_stack_by_mtt"] = None
    packet["worldvolume_evidence"]["twisted_projective_D7_stack"] = None
    return packet


def s3_assignments() -> list[dict[str, Any]]:
    cp = load_json(CP_RESCUE_CERT)
    assignments = cp.get("coordinate_rescue_enumeration", {}).get("minimal_rescue_assignments", [])
    return [
        item
        for item in assignments
        if item.get("twisted_projective_D7_stack_required") == "S3"
    ]


def attempt_packet() -> dict[str, Any]:
    packet = base_packet("ATTEMPT_BLOCKED_SELECTED_S3_SOURCE_MISSING")
    packet["source_evidence"].update(
        {
            "source_selected_by_mtt": False,
            "fixed_differential_cohomology_class": False,
            "geometric_Deligne_Cech_or_worldvolume_flux_source_constructed": False,
            "physical_worldvolume_flux_or_twisted_CP_source_constructed": False,
            "map_to_central_cocycle_verified": False,
            "source_certificate": "visible_twisted_s3_source_packet_attempt_certificate.json",
            "current_blocker": (
                "the selector and finite qutrit/gerbe/Chan-Paton facts pick S3, "
                "but no selected S3 differential-cohomology or worldvolume-flux "
                "source has been constructed"
            ),
        }
    )
    packet["consistency_evidence"].update(
        {
            "green_schwarz_bianchi_verified_for_S3_source": False,
            "freed_witten_verified_for_S3_source": False,
            "twisted_projector_retention_verified": False,
        }
    )
    packet["supporting_assignments"] = s3_assignments()
    return packet


def attempt_report() -> dict[str, Any]:
    selector = load_json(S3_SELECTOR_CERT)
    packet = attempt_packet()
    write_json(TEMPLATE, template_packet())
    write_json(ATTEMPT, packet)
    validator_exit, validator_output = run_validator(ATTEMPT)
    template_exit, template_output = run_validator(TEMPLATE)

    source_missing = validator_exit == 1
    return {
        "candidate": "VisibleTwistedS3SourcePacketAttempt",
        "status": "VISIBLE_TWISTED_S3_SOURCE_PACKET_ATTEMPT_BLOCKED_SELECTED_SOURCE_OPEN",
        "generated_by": "scripts/attempt_visible_twisted_s3_source_packet.py",
        "template": "certificates/visible_twisted_s3_source_packet.template.json",
        "attempt_packet": "certificates/visible_twisted_s3_source_packet.attempt.json",
        "validator": "scripts/validate_visible_twisted_s3_source_packet.py",
        "inputs": {
            "equivariant_selector_certificate": "visible_twisted_d7_equivariant_embedding_selector_certificate.json",
            "twisted_chan_paton_rescue_certificate": "visible_twisted_chan_paton_rescue_certificate.json",
            "time_oriented_m1_gerbe_period_table_certificate": "time_oriented_m1_gerbe_period_table_certificate.json",
            "time_oriented_m1_deck_cech_lift_certificate": "time_oriented_m1_deck_cech_lift_certificate.json",
            "visible_complex_worldvolume_spinc_gate_certificate": "visible_complex_worldvolume_spinc_gate_certificate.json",
        },
        "selected_stack": {
            "stack": "S3",
            "selector_status": selector.get("status"),
            "selected_stack_by_mtt": True,
            "selected_source_by_mtt": False,
        },
        "s3_source_attempt": {
            "active_pair": packet["worldvolume_evidence"]["active_pair"],
            "supporting_s3_assignments": packet.get("supporting_assignments", []),
            "finite_projective_CP_module_matches_m1_twist": packet["finite_gerbe_evidence"][
                "finite_projective_CP_module_matches_m1_twist"
            ],
            "source_selected_by_mtt": packet["source_evidence"]["source_selected_by_mtt"],
            "fixed_differential_cohomology_class": packet["source_evidence"][
                "fixed_differential_cohomology_class"
            ],
            "freed_witten_verified_for_S3_source": packet["consistency_evidence"][
                "freed_witten_verified_for_S3_source"
            ],
            "twisted_projector_retention_verified": packet["consistency_evidence"][
                "twisted_projector_retention_verified"
            ],
        },
        "validator_result": {
            "attempt_exit_code": validator_exit,
            "attempt_output_head": validator_output.splitlines()[:24],
            "template_exit_code": template_exit,
            "template_output_head": template_output.splitlines()[:8],
        },
        "calculation_results": {
            "source_packet_schema_and_validator_created": True,
            "template_refused_as_open": template_exit == 2,
            "attempt_refused_until_selected_source": source_missing,
            "minimal_equivariant_stack_S3_closed": True,
            "finite_S3_projective_CP_inputs_collected": len(packet.get("supporting_assignments", [])) == 2,
            "selected_S3_source_constructed": False,
            "S3_freed_witten_closed_for_source": False,
            "S3_projector_retention_closed": False,
        },
        "what_this_closes": {
            "executable_selected_S3_source_gate": True,
            "minimal_equivariant_twisted_D7_stack": "S3",
            "proof_that_selector_data_alone_do_not_promote_source": source_missing,
            "finite_projective_CP_rescue_restricted_to_S3_branch": True,
        },
        "still_open": {
            "selected_S3_Deligne_Cech_or_worldvolume_flux_source": True,
            "fixed_S3_differential_cohomology_class": True,
            "S3_map_to_qutrit_central_cocycle": True,
            "S3_Green_Schwarz_Bianchi_verification": True,
            "S3_Freed_Witten_verification": True,
            "S3_twisted_projector_retention": True,
            "selected_visible_operator_source": True,
            "selected_D_E_dotD": True,
            "primitive_C1_contractions_and_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_S3_source": False,
            "claims_Freed_Witten_closed_for_S3_source": False,
            "claims_projector_retention": False,
            "claims_visible_operator_source_constructed": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "S3 is now selected at the minimal equivariant stack level and "
                "the finite qutrit/gerbe/Chan-Paton ingredients line up on the "
                "q79/F,m=1 branch. This still does not construct the selected "
                "S3 differential-cohomology or worldvolume-flux source."
            ),
            "next_closing_object": (
                "Supply a selected S3 Deligne/Cech, B-field period, "
                "worldvolume-flux, or twisted Chan-Paton source certificate "
                "that verifies its central cocycle map, Green-Schwarz Bianchi, "
                "Freed-Witten condition, and projector retention."
            ),
        },
    }


def write_outputs(report: dict[str, Any]) -> None:
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleTwistedS3SourcePacketAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_twisted_s3_source_packet_attempt.candidate.json",
        "template": report["template"],
        "attempt_packet": report["attempt_packet"],
        "validator": report["validator"],
        "inputs": report["inputs"],
        "selected_stack": report["selected_stack"],
        "s3_source_attempt": report["s3_source_attempt"],
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
