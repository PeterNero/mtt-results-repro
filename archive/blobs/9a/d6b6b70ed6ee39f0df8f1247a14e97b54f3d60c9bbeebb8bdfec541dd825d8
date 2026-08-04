"""Attempt to fill IwasawaTwistedSourcePromotionPacket.v1 honestly.

The current projective magnetic carrier supplies a nontrivial zeta_3 cocycle
and passes the projective rho_E and metric validators.  The block-factorized
sector-map packet now also supplies finite projectors by keeping Q,u,d,L,e,N on
the projective qutrit family block and H on a separate ordinary line.

This script checks how far those data can be pushed toward selected
twisted-source promotion, and records the first rigorous blockers.  It
intentionally does not flip selected-source flags without evidence.  The old
single-carrier obstruction is still tested as a diagnostic, but the current
block-factorized route is now blocked first by missing selected gerbe/B-field
source data, not by finite sector projectors.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DEFAULT_PACKET = ROOT / "certificates" / "iwasawa_twisted_source_promotion_packet.attempt.json"
DEFAULT_CARRIER = ROOT / "candidate_data" / "iwasawa_projective_magnetic_carrier.meshN1.json"
DEFAULT_SECTOR_MAPS = ROOT / "candidate_data" / "iwasawa_block_factorized_sector_maps.candidate.json"
DEFAULT_BLOCK_PACKET = ROOT / "candidate_data" / "iwasawa_block_factorized_twisted_packet.candidate.json"
M1_PERIOD_CERT = ROOT / "certificates" / "time_oriented_m1_gerbe_period_table_certificate.json"
M1_DECK_CECH_CERT = ROOT / "certificates" / "time_oriented_m1_deck_cech_lift_certificate.json"
M1_FLAT_GERBE_CERT = ROOT / "certificates" / "time_oriented_m1_flat_gerbe_promotion_certificate.json"
M1_FREED_WITTEN_GATE_CERT = ROOT / "certificates" / "time_oriented_m1_freed_witten_cycle_gate_certificate.json"
M1_QUTRIT_LINE_CYCLE_CERT = ROOT / "certificates" / "time_oriented_m1_qutrit_line_cycle_restrictions_certificate.json"
VISIBLE_COMPLEX_SPINC_CERT = ROOT / "certificates" / "visible_complex_worldvolume_spinc_gate_certificate.json"
VISIBLE_ACTIVE_F3_OBSTRUCTION_CERT = ROOT / "certificates" / "visible_active_f3_image_recovery_obstruction_certificate.json"
VISIBLE_TWISTED_CP_RESCUE_CERT = ROOT / "certificates" / "visible_twisted_chan_paton_rescue_certificate.json"
VISIBLE_TWISTED_D7_VOLUME_SELECTOR_CERT = ROOT / "certificates" / "visible_twisted_d7_volume_selector_attempt_certificate.json"
VISIBLE_TWISTED_D7_QUTRIT_SYMMETRY_SELECTOR_CERT = ROOT / "certificates" / "visible_twisted_d7_qutrit_symmetry_selector_certificate.json"
VISIBLE_TWISTED_D7_EQUIVARIANT_SELECTOR_CERT = ROOT / "certificates" / "visible_twisted_d7_equivariant_embedding_selector_certificate.json"
VISIBLE_TWISTED_S3_SOURCE_PACKET_CERT = ROOT / "certificates" / "visible_twisted_s3_source_packet_attempt_certificate.json"
VISIBLE_TWISTED_S3_FINITE_CP_CERT = ROOT / "certificates" / "visible_twisted_s3_finite_cp_cancellation_certificate.json"
VISIBLE_TWISTED_S3_SMOOTH_SOURCE_LIFT_CERT = ROOT / "certificates" / "visible_twisted_s3_smooth_source_lift_attempt_certificate.json"
IWASAWA_DELIGNE_COVER_GAUGE_REDUCTION_CERT = ROOT / "certificates" / "iwasawa_deligne_cover_gauge_reduction_certificate.json"
VISIBLE_TWISTED_S3_CLASS_RESTRICTION_PACKET_CERT = ROOT / "certificates" / "visible_twisted_s3_class_restriction_packet_attempt_certificate.json"
VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSURE_CERT = ROOT / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json"
M1_GREEN_SCHWARZ_GATE_CERT = ROOT / "certificates" / "time_oriented_m1_green_schwarz_gate_certificate.json"
M1_VISIBLE_GS_REQUIREMENT_CERT = ROOT / "certificates" / "time_oriented_m1_visible_green_schwarz_requirement_certificate.json"
M1_VISIBLE_GS_CURVATURE_CERT = ROOT / "certificates" / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
M1_VISIBLE_GS_SOURCE_ATTEMPT_CERT = ROOT / "certificates" / "time_oriented_m1_visible_gs_source_attempt_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def identity_matrix() -> dict[str, list[list[int]]]:
    return {"matrix": [[1, 0, 0], [0, 1, 0], [0, 0, 1]]}


def rank_one_h_projector() -> dict[str, list[list[int]]]:
    return {"matrix": [[1, 0, 0], [0, 0, 0], [0, 0, 0]]}


def attach_minimal_sector_maps(candidate: dict[str, Any]) -> dict[str, Any]:
    """Attach the natural diagnostic projectors.

    Family sectors use the full rank-three identity projector.  The Higgs slot
    uses the usual rank-one test line, which must fail for irreducible X,Z.
    """

    enriched = json.loads(json.dumps(candidate))
    family = {
        sector: {
            "kind": "family",
            "dimension": 3,
            "projector": identity_matrix(),
        }
        for sector in ("Q", "u", "d", "L", "e", "N")
    }
    family["H"] = {
        "kind": "single_higgs_carrier",
        "dimension": 1,
        "projector": rank_one_h_projector(),
    }
    enriched["sector_projection_maps"] = family
    return enriched


def validate(script: str, path: Path) -> tuple[int, str]:
    return run([sys.executable, str(SCRIPTS / script), str(path)])


def certificate_has_status(path: Path, expected: str) -> bool:
    if not path.exists():
        return False
    return load_json(path).get("status") == expected


def commutant_obstruction() -> dict[str, Any]:
    return {
        "carrier": "qutrit clock/shift magnetic translations",
        "relations": [
            "Z has three distinct eigenvalues 1, omega, omega^2",
            "commuting with Z forces any matrix A to be diagonal",
            "commuting with X then forces the diagonal entries of A to be equal",
            "therefore Comm(X,Z)=C*I_3",
        ],
        "commutant_dimension": 1,
        "hermitian_idempotents_in_commutant": ["0", "I_3"],
        "rank_one_invariant_projector_possible": False,
        "consequence": "the current irreducible qutrit projective carrier cannot satisfy the rank-one H sector-map validator without changing the carrier architecture",
        "allowed_escape_routes": [
            "supply a different selected twisted carrier with a retained rank-one Higgs subbundle",
            "use the qutrit twist only as an ambient family-Z3/twisted-boundary factor and keep Higgs in a separate selected block",
            "extend the validator/schema to a block-factorized twisted packet with separately validated family and Higgs carriers",
        ],
    }


def attempt_report(
    packet_path: Path,
    carrier_path: Path,
    sector_maps_path: Path,
    block_packet_path: Path,
) -> dict[str, Any]:
    packet_path = packet_path.resolve()
    carrier_path = carrier_path.resolve()
    sector_maps_path = sector_maps_path.resolve()
    block_packet_path = block_packet_path.resolve()
    packet = load_json(packet_path)
    carrier = load_json(carrier_path)
    partial_selected_source_progress = {
        "time_oriented_m1_finite_period_table_closed": certificate_has_status(
            M1_PERIOD_CERT,
            "TIME_ORIENTED_M1_FINITE_GERBE_PERIOD_TABLE_CLOSED_OPERATOR_SOURCE_OPEN",
        ),
        "time_oriented_m1_deck_cech_lift_closed": certificate_has_status(
            M1_DECK_CECH_CERT,
            "TIME_ORIENTED_M1_DECK_CECH_LIFT_CLOSED_GEOMETRIC_OPERATOR_SOURCE_OPEN",
        ),
        "time_oriented_m1_conditional_flat_gerbe_closed": certificate_has_status(
            M1_FLAT_GERBE_CERT,
            "TIME_ORIENTED_M1_FLAT_GERBE_PROMOTION_CONDITIONAL_CLOSED_SELECTION_OPEN",
        ),
        "time_oriented_m1_freed_witten_DD_cycle_gate_closed": certificate_has_status(
            M1_FREED_WITTEN_GATE_CERT,
            "TIME_ORIENTED_M1_FREED_WITTEN_CYCLE_GATE_FORMULATED_SELECTED_CYCLES_OPEN",
        ),
        "time_oriented_m1_qutrit_line_cycle_restrictions_closed": certificate_has_status(
            M1_QUTRIT_LINE_CYCLE_CERT,
            "TIME_ORIENTED_M1_QUTRIT_LINE_CYCLE_RESTRICTIONS_CLOSED_VISIBLE_CYCLE_LIST_OPEN",
        ),
        "visible_complex_worldvolume_spinc_gate_closed": certificate_has_status(
            VISIBLE_COMPLEX_SPINC_CERT,
            "VISIBLE_COMPLEX_WORLDVOLUME_SPINC_W3_CLOSED_DD_IMAGES_OPEN",
        ),
        "visible_active_f3_naive_coordinate_route_blocked": certificate_has_status(
            VISIBLE_ACTIVE_F3_OBSTRUCTION_CERT,
            "VISIBLE_ACTIVE_F3_IMAGE_RECOVERY_NAIVE_COORDINATE_ROUTE_BLOCKED",
        ),
        "visible_twisted_chan_paton_rescue_family_reduced": certificate_has_status(
            VISIBLE_TWISTED_CP_RESCUE_CERT,
            "VISIBLE_TWISTED_CP_MINIMAL_COORDINATE_RESCUE_REDUCED_SELECTION_OPEN",
        ),
        "visible_twisted_d7_volume_selector_attempt_s3_conditional": certificate_has_status(
            VISIBLE_TWISTED_D7_VOLUME_SELECTOR_CERT,
            "VISIBLE_TWISTED_D7_VOLUME_SELECTOR_ATTEMPT_S3_CONDITIONAL_SELECTION_OPEN",
        ),
        "visible_twisted_d7_qutrit_symmetry_selector_reduces_to_s3": certificate_has_status(
            VISIBLE_TWISTED_D7_QUTRIT_SYMMETRY_SELECTOR_CERT,
            "VISIBLE_TWISTED_D7_QUTRIT_SYMMETRY_SELECTOR_REDUCES_TO_S3_EMBEDDING_RULE_OPEN",
        ),
        "visible_twisted_d7_equivariant_embedding_selector_s3_closed": certificate_has_status(
            VISIBLE_TWISTED_D7_EQUIVARIANT_SELECTOR_CERT,
            "VISIBLE_TWISTED_D7_EQUIVARIANT_EMBEDDING_SELECTOR_S3_CLOSED_SOURCE_OPEN",
        ),
        "visible_twisted_s3_source_packet_gate_created": certificate_has_status(
            VISIBLE_TWISTED_S3_SOURCE_PACKET_CERT,
            "VISIBLE_TWISTED_S3_SOURCE_PACKET_ATTEMPT_BLOCKED_SELECTED_SOURCE_OPEN",
        ),
        "visible_twisted_s3_finite_cp_cancellation_closed": certificate_has_status(
            VISIBLE_TWISTED_S3_FINITE_CP_CERT,
            "VISIBLE_TWISTED_S3_FINITE_CP_CANCELLATION_CLOSED_SMOOTH_SOURCE_OPEN",
        ),
        "visible_twisted_s3_smooth_source_lift_gate_created": certificate_has_status(
            VISIBLE_TWISTED_S3_SMOOTH_SOURCE_LIFT_CERT,
            "VISIBLE_TWISTED_S3_SMOOTH_SOURCE_LIFT_ATTEMPT_BLOCKED_SELECTED_COVER_PROJECTORS_OPEN",
        ),
        "iwasawa_deligne_cover_gauge_reduction_closed": certificate_has_status(
            IWASAWA_DELIGNE_COVER_GAUGE_REDUCTION_CERT,
            "IWASAWA_DELIGNE_COVER_GAUGE_REDUCTION_CLOSED_CLASS_RESTRICTION_OPEN",
        ),
        "visible_twisted_s3_class_restriction_packet_gate_created": certificate_has_status(
            VISIBLE_TWISTED_S3_CLASS_RESTRICTION_PACKET_CERT,
            "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_PACKET_ATTEMPT_BLOCKED_SMOOTH_CLASS_PROJECTORS_OPEN",
        ),
        "visible_twisted_s3_class_restriction_closed": certificate_has_status(
            VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSURE_CERT,
            "VISIBLE_TWISTED_S3_CLASS_RESTRICTION_CLOSED_OPERATOR_SOURCE_OPEN",
        ),
        "time_oriented_m1_green_schwarz_preservation_gate_closed": certificate_has_status(
            M1_GREEN_SCHWARZ_GATE_CERT,
            "TIME_ORIENTED_M1_GREEN_SCHWARZ_GATE_PRESERVATION_CLOSED_VISIBLE_SOURCE_OPEN",
        ),
        "time_oriented_m1_visible_green_schwarz_requirement_derived": certificate_has_status(
            M1_VISIBLE_GS_REQUIREMENT_CERT,
            "TIME_ORIENTED_M1_VISIBLE_GS_REQUIREMENT_DERIVED_SOURCE_OPEN",
        ),
        "time_oriented_m1_visible_green_schwarz_curvature_closed": certificate_has_status(
            M1_VISIBLE_GS_CURVATURE_CERT,
            "TIME_ORIENTED_M1_VISIBLE_GS_CURVATURE_CLOSED_OPERATOR_SOURCE_OPEN",
        ),
        "time_oriented_m1_visible_green_schwarz_source_gate_created": certificate_has_status(
            M1_VISIBLE_GS_SOURCE_ATTEMPT_CERT,
            "TIME_ORIENTED_M1_VISIBLE_GS_SOURCE_ATTEMPT_BLOCKED_SELECTED_SOURCE_MISSING",
        ),
    }

    packet_code, packet_output = validate(
        "validate_iwasawa_twisted_source_promotion.py",
        packet_path,
    )
    projective_code, projective_output = validate(
        "validate_iwasawa_projective_rhoE_mesh.py",
        carrier_path,
    )
    metric_code, metric_output = validate("validate_iwasawa_rhoE_metric.py", carrier_path)
    sector_maps_code, sector_maps_output = validate(
        "validate_iwasawa_block_factorized_sector_maps.py",
        sector_maps_path,
    )
    block_packet_code, block_packet_output = validate(
        "validate_iwasawa_block_factorized_twisted_packet.py",
        block_packet_path,
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        enriched_path = Path(temp_dir) / "projective_with_rank_one_H_sector.json"
        write_json(enriched_path, attach_minimal_sector_maps(carrier))
        single_carrier_sector_code, single_carrier_sector_output = validate(
            "validate_iwasawa_sector_maps.py",
            enriched_path,
        )

    fillable_now = {
        "central_cocycle": packet.get("central_cocycle"),
        "projective_rhoE_mesh_path": packet.get("paths", {}).get("projective_rhoE_mesh"),
        "rhoE_metric_path": packet.get("paths", {}).get("rhoE_metric"),
        "block_factorized_sector_maps_path": str(sector_maps_path.relative_to(ROOT)),
        "block_factorized_twisted_packet_path": str(block_packet_path.relative_to(ROOT)),
        "period_denominator": packet.get("gerbe_source", {}).get("period_denominator"),
        "central_phase_label": packet.get("gerbe_source", {}).get("central_phase_label"),
        "no_observed_flavor_inputs": packet.get("no_observed_flavor_inputs") is True,
        "block_factorized_sector_maps_valid": sector_maps_code == 0,
        "block_factorized_twisted_packet_valid": block_packet_code == 0,
        "partial_selected_source_progress": partial_selected_source_progress,
    }
    blockers = {
        "selected_twist_verified": packet.get("selected_twist_verified") is not True,
        "fixed_topological_sector_for_this_twist": packet.get("fixed_topological_sector")
        is not True,
        "unconditional_selected_geometric_cover": True,
        "complete_selected_visible_cycle_or_worldvolume_packet": True,
        "selected_visible_operator_source_promotion": True,
        "green_schwarz_bianchi_for_visible_operator_source": packet.get("gerbe_source", {}).get(
            "green_schwarz_bianchi_verified"
        )
        is not True,
        "coherent_spectral_zero_mode_projector_retention": packet.get(
            "gerbe_source", {}
        ).get("coherent_spectral_projector_verified")
        is not True,
        "selected_D_E_dotD": True,
        "primitive_C1_contractions": True,
        "single_carrier_rank_one_H_projector": True,
    }

    return {
        "calculation": "IwasawaTwistedSourcePromotionPacketFillAttempt",
        "status": "BLOCKED_SELECTED_SOURCE_AFTER_BLOCK_SECTOR_FILL",
        "packet_path": str(packet_path),
        "carrier_path": str(carrier_path),
        "sector_maps_path": str(sector_maps_path),
        "block_packet_path": str(block_packet_path),
        "fillable_now": fillable_now,
        "partial_selected_source_progress": partial_selected_source_progress,
        "validator_results": {
            "twisted_source_promotion_packet": {
                "exit": packet_code,
                "output_head": packet_output.splitlines()[:8],
            },
            "projective_rhoE_mesh": {
                "exit": projective_code,
                "output_head": projective_output.splitlines()[:8],
            },
            "rhoE_metric": {
                "exit": metric_code,
                "output_head": metric_output.splitlines()[:8],
            },
            "block_factorized_sector_maps": {
                "exit": sector_maps_code,
                "output_head": sector_maps_output.splitlines()[:8],
            },
            "block_factorized_twisted_packet": {
                "exit": block_packet_code,
                "output_head": block_packet_output.splitlines()[:8],
            },
            "single_carrier_rank_one_H_test": {
                "exit": single_carrier_sector_code,
                "output_head": single_carrier_sector_output.splitlines()[:12],
            },
        },
        "commutant_obstruction": commutant_obstruction(),
        "block_factorized_resolution": {
            "finite_sector_projectors_filled": sector_maps_code == 0,
            "separate_higgs_line_validated": sector_maps_code == 0,
            "old_single_carrier_H_obstruction_retired_as_active_blocker": sector_maps_code == 0,
            "block_sector_projector_retention_for_selected_s3_source_closed": partial_selected_source_progress[
                "visible_twisted_s3_class_restriction_closed"
            ],
            "coherent_spectral_projector_retention_still_requires_operator_source": True,
        },
        "blockers": blockers,
        "first_hard_blocker": "finite m=1 gerbe, deck/Cech, conditional flat gerbe, DD(B) cycle-restriction, qutrit clock/shift line-cycle restrictions, visible complex-worldvolume W3/spinC, naive coordinate active-image obstruction, finite twisted Chan-Paton rescue reduction, conditional S3 volume selector, qutrit-symmetry S3 reduction, minimal equivariant S3 selector, executable selected-S3-source packet gate, finite S3 twisted-CP cancellation, conditional smooth-source lift gate, Deligne cover gauge reduction, and selected S3 class/restriction closure are now closed/formulated; promotion still needs the selected visible operator/source packet, complete visible cycle/worldvolume source, coherent spectral zero-mode projector retention, selected D_E, dotD, and C1 contractions",
        "verdict": {
            "packet_filled_as_far_as_current_evidence_allows": True,
            "packet_passes_promotion_validator": packet_code == 0,
            "current_projective_carrier_can_be_selected_without_new_data": False,
            "finite_block_factorized_sector_maps_validated": sector_maps_code == 0,
            "recommended_next_move": "use the selected S3 class/restriction closure to build the selected visible Green-Schwarz/operator-source packet, then construct selected D_E/dotD, Riesz/Green, coherent spectral projectors, and primitive C1 contractions",
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, default=DEFAULT_PACKET)
    parser.add_argument("--carrier", type=Path, default=DEFAULT_CARRIER)
    parser.add_argument("--sector-maps", type=Path, default=DEFAULT_SECTOR_MAPS)
    parser.add_argument("--block-packet", type=Path, default=DEFAULT_BLOCK_PACKET)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(
        json.dumps(
            attempt_report(args.packet, args.carrier, args.sector_maps, args.block_packet),
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
