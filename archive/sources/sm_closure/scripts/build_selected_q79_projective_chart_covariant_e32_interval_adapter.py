from __future__ import annotations

import hashlib
import json
from pathlib import Path

from q79_y_chart_conservative_extension import audit_source_compatibility


ROOT = Path(__file__).resolve().parents[1]
DATA = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIODS = DATA / "selected_alignment_thimble_periods"
A123 = (
    ROOT
    / "candidate_data"
    / "selected_q79projectivelinechartcovarianceandellzerocontinuation"
    / "projective_line_chart_covariance_theorem.packet.json"
)
Z_FIBRATION = DATA / "selected_alignment_zchart_genus2_fibration_seed.interval.packet.json"
Z_WALL = DATA / "selected_alignment_zchart_wall.interval.packet.json"
SOURCE = PERIODS / "d048_selected_046.thimble_period.candidate.json"
NODAL = PERIODS / "d048_selected_046.nodal_factor.interval.packet.json"
TAIL = PERIODS / "d048_selected_046.E32_tail.interval.packet.json"
MAIN = PERIODS / "d048_selected_046.E32_main.interval.packet.json"
FULL = PERIODS / "d048_selected_046.E32_full.interval.packet.json"
A151 = PERIODS / "selected_alignment_E32_clearance_ranked_successor_A151.packet.json"
HISTORICAL_Y = PERIODS / "d057_selected_008.E32_main.interval.packet.json"
ENGINE = ROOT / "scripts" / "certify_q79_selected_side_beta_defect_transport.py"
NODAL_ENGINE = ROOT / "scripts" / "certify_q79_selected_alignment_single_E32_thimble_nodal_factor.py"
TAIL_ENGINE = ROOT / "scripts" / "certify_q79_selected_alignment_single_E32_thimble_tail_interval.py"
MAIN_ENGINE = ROOT / "scripts" / "certify_q79_selected_alignment_E32_thimble_polygonal_main_interval.py"
WALL_BUILDER = ROOT / "scripts" / "build_q79_selected_alignment_zchart_wall.py"
COMPATIBILITY_CHECKER = ROOT / "scripts" / "q79_y_chart_conservative_extension.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79ProjectiveChartCovariantE32IntervalAdapter_v1.md"
CANDIDATE = ROOT / "candidate_data" / "selected_q79projectivechartcovariante32intervaladapter.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79projectivechartcovariante32intervaladapter.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    a123 = load(A123)
    z_fibration = load(Z_FIBRATION)
    z_wall = load(Z_WALL)
    source = load(SOURCE)
    nodal = load(NODAL)
    tail = load(TAIL)
    main_interval = load(MAIN)
    full = load(FULL)
    a151 = load(A151)
    historical = load(HISTORICAL_Y)
    compatibility = audit_source_compatibility()
    if not a123["theorem"]["proved"]:
        raise AssertionError("A123 covariance theorem is unavailable")
    if z_fibration["source"]["line_chart"] != "z":
        raise AssertionError("native z fibration seed changed")
    if z_wall["selected_z_line_chart_zeros"]["count"] != 3:
        raise AssertionError("z-chart wall count changed")
    if source["line_chart"] != "z":
        raise AssertionError("d048 is not the frozen z-chart row")
    if nodal["selected_thimble"]["line_chart"] != "z":
        raise AssertionError("z-chart nodal certificate missing")
    if tail["selected_thimble"]["line_chart"] != "z":
        raise AssertionError("z-chart tail certificate missing")
    if main_interval["selected_thimble"]["line_chart"] != "z":
        raise AssertionError("z-chart main certificate missing")
    if not full["full_E32_thimble"]["floating_candidate_contained"]:
        raise AssertionError("independent z-chart center is outside the interval")
    if not a151["scope"]["covariant_z_chart_interval_adapter_closed"]:
        raise AssertionError("A151 did not promote the adapter")

    historical_engine_hash = historical["authority"][
        "validated_transport_engine_sha256"
    ]
    current_engine_hash = sha256(ENGINE)
    candidate = {
        "schema": "MTTSelectedQ79ProjectiveChartCovariantE32IntervalAdapter.v1",
        "status": "SELECTED_Q79_PROJECTIVE_YZ_CHART_COVARIANT_E32_INTERVAL_ADAPTER_CLOSED_FIRST_Z_ROW_A151_CLOSED",
        "authority": [
            {"path": relative(path), "sha256": sha256(path)}
            for path in (
                A123,
                Z_FIBRATION,
                Z_WALL,
                SOURCE,
                NODAL,
                TAIL,
                MAIN,
                FULL,
                A151,
                HISTORICAL_Y,
                ENGINE,
                NODAL_ENGINE,
                TAIL_ENGINE,
                MAIN_ENGINE,
                WALL_BUILDER,
                COMPATIBILITY_CHECKER,
                Path(__file__),
            )
        ],
        "exact_projective_adapter": {
            "A123_transition": "t_z=-(L0+L2*t_y)/L1",
            "fiber_scaling": "U_z=(L2/L1)^3*U_y",
            "five_period_transition_determinant": -1,
            "native_chart_parameter": "SelectedQ79IntervalSystem(line_chart in {y,z})",
            "native_z_residue_constant": "L2*(dL0*L2-dL2*L0)",
            "native_z_residue_linear": "L2*(dL1*L2-dL2*L1)",
            "observed_SM_values_used": False,
        },
        "z_chart_wall": {
            "zero_count": 3,
            "minimum_pairwise_torus_ball_separation_lower": float(
                z_wall["selected_z_line_chart_zeros"][
                    "minimum_pairwise_torus_ball_separation_lower"
                ]
            ),
            "minimum_torus_distance_to_critical_balls_lower": float(
                z_wall["selected_z_line_chart_zeros"][
                    "minimum_torus_distance_to_critical_balls_lower"
                ]
            ),
        },
        "first_complete_native_z_row": {
            "artifact": "A151",
            "distinguished_index": 48,
            "root_id": "selected_046",
            "coefficient": 3,
            "nodal_Jacobian_absolute_lower": nodal["certified_node"][
                "jacobian_determinant_absolute_lower"
            ],
            "tail_segments": len(tail["regular_segments"]),
            "tail_radius_upper": tail["E32_endpoint_tail"]["interval_radius_upper"],
            "main_accepted_steps": main_interval["validated_main_transport"][
                "accepted_step_count"
            ],
            "main_rejected_steps": main_interval["validated_main_transport"][
                "rejected_step_count"
            ],
            "main_radius_upper": main_interval["E32_main_segment"][
                "interval_radius_upper"
            ],
            "base_center_difference": main_interval["orientation"][
                "selected_base_center_maximum_difference"
            ],
            "full_radius_upper": full["full_E32_thimble"]["interval_radius_upper"],
            "independent_floating_center_difference": full["full_E32_thimble"][
                "floating_candidate_center_difference"
            ],
            "independent_floating_center_contained": True,
            "A134_uniform_fallback_met": full["A134_radius_ledger"]["fallback_met"],
        },
        "historical_y_provenance": {
            "historical_packet_engine_hashes": [historical_engine_hash],
            "current_chart_parametric_engine_hash": current_engine_hash,
            "default_chart_remains_y": True,
            "historical_packets_relabelled_as_new_runs": False,
            "byte_exact_conservative_extension": compatibility,
            "interpretation": (
                "Legacy y packets retain their recorded historical engine hash. "
                "Reversing only the explicit chart parameterization and strict chart guards "
                "reconstructs the recorded historical y source hashes byte for byte. The old "
                "packets remain historical runs rather than being relabelled as new runs."
            ),
        },
        "scope": {
            "exact_projective_formula_adapter_closed": True,
            "z_chart_regular_domain_interval_certified": True,
            "native_z_node_tail_main_full_pipeline_closed": True,
            "generic_z_infrastructure_blocker_retired": True,
            "historical_y_source_conservative_extension_closed": True,
            "all_remaining_z_rows_closed": False,
            "weighted_71_thimble_interval_closed": False,
            "fixed_carrier_exact_separation_closed": False,
            "observed_SM_values_used": False,
        },
        "next_required_artifact": "continue the remaining 55 selected y/z rows and weighted exact branch decision",
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "schema": "MTTCertificate.v1",
        "certificate": "MTTSelectedQ79ProjectiveChartCovariantE32IntervalAdapter",
        "status": candidate["status"],
        "candidate_path": relative(CANDIDATE),
        "candidate_sha256": sha256(CANDIDATE),
        "historical_y_packet_engine_hashes": [historical_engine_hash],
        "current_chart_parametric_engine_sha256": current_engine_hash,
        "byte_exact_historical_y_specialization_closed": compatibility[
            "byte_exact_historical_y_specialization_closed"
        ],
        "reconstructed_historical_y_source_hashes": compatibility[
            "reconstructed_historical_y_hashes"
        ],
        "first_native_z_artifact": "A151",
        "generic_z_infrastructure_blocker_retired": True,
        "weighted_interval_closed": False,
        "observed_SM_values_used": False,
    }
    dump(CERTIFICATE, certificate)

    note = f"""# MTT Selected q79 Projective-Chart-Covariant E32 Interval Adapter v1

## Theorem

A123 already proves the exact overlap formulas

```text
t_z=-(L0+L2*t_y)/L1,
U_z=(L2/L1)^3 U_y,
det(T_5)=-1.
```

The validated system now consumes the selected chart as an explicit source
coordinate.  In the native `z` chart it uses the exact homogeneous sextic,
quadratic splitting factor, Gauss-Manin reduction, and residue numerator

```text
constant = L2 (dL0 L2-dL2 L0),
linear   = L2 (dL1 L2-dL2 L1).
```

The three `L2=0` chart walls are interval-isolated.  Their minimum pairwise
torus separation is `{candidate['z_chart_wall']['minimum_pairwise_torus_ball_separation_lower']:.16g}`
and their minimum clearance from all 90 nodal values is
`{candidate['z_chart_wall']['minimum_torus_distance_to_critical_balls_lower']:.16g}`.

## First complete native z execution

The frozen z-queue head `d048/selected_046`, coefficient `+3`, is certified
through the entire independent pipeline:

```text
node Jacobian lower = {candidate['first_complete_native_z_row']['nodal_Jacobian_absolute_lower']:.16g}
tail segments       = {candidate['first_complete_native_z_row']['tail_segments']}
tail radius         = {candidate['first_complete_native_z_row']['tail_radius_upper']:.16g}
main steps          = {candidate['first_complete_native_z_row']['main_accepted_steps']} accepted / {candidate['first_complete_native_z_row']['main_rejected_steps']} rejected
main radius         = {candidate['first_complete_native_z_row']['main_radius_upper']:.16g}
full radius         = {candidate['first_complete_native_z_row']['full_radius_upper']:.16g}
floating difference = {candidate['first_complete_native_z_row']['independent_floating_center_difference']:.16g}
```

The independent A131 floating center is contained, and the A134 fallback is
met.  A151 therefore retires the generic z-chart infrastructure blocker.  It
does not certify the remaining z rows, the 71-thimble weighted sum, or the
fixed-carrier exact branch.

## Provenance guard

Earlier y packets retain historical engine hash
`{historical_engine_hash}`.  The current chart-parametric source has hash
`{current_engine_hash}` and still defaults to `y`.  This is stronger than a
bare source supersession: a machine audit reverses only the explicit chart
parameterization and strict chart-consistency guards and reconstructs the
recorded historical hashes exactly:

```text
transport = {compatibility['reconstructed_historical_y_hashes']['transport_engine']}
main      = {compatibility['reconstructed_historical_y_hashes']['augmented_main_engine']}
full      = {compatibility['reconstructed_historical_y_hashes']['full_splice_builder']}
```

Thus the new source is a byte-certified conservative extension on its `y`
specialization.  This remains not a claim that old packets were rerun.  No
observed Standard Model value enters the construction.
"""
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {relative(CANDIDATE)}")
    print(f"wrote {relative(CERTIFICATE)}")
    print(f"wrote {relative(NOTE)}")
    print("q79 projective chart-covariant E32 adapter: CLOSED at A151")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
