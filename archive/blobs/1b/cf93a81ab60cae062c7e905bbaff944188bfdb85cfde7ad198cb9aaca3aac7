from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from flint import acb, arb, ctx

import certify_q79_height4_target_full_residue_interval as target_transport
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
PERIODS = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
VALIDATED = PERIODS / "covariant_floating_probe" / "validated_transport"
A400 = VALIDATED / "n3.relative_chain_identity.a400.json"
A401 = VALIDATED / "n3.lower_b_contour_homotopy.a401.json"
A402S = VALIDATED / "n3.beta_minus_B.source.a402s.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
OUTPUT = VALIDATED / "n3.common_junction_edge_ledger.a403.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourCommonJunctionEdgeLedger_A403_v1.md"
ARTIFACT = "A403"
RADIUS = 0.2
HUB = 0.2 + 0.0j


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def midpoint(value: acb) -> complex:
    return complex(float(value.real.mid()), float(value.imag.mid()))


def main() -> int:
    ctx.dps = 100
    identity = load(A400)
    roots = load(A401)
    correlated_source = load(A402S)
    handle_execution = load(A383)
    if not identity["theorem"]["proved"]:
        raise AssertionError("A400 relative-chain identity is not closed")
    if not roots["strict_scope"]["all_90_simple_n3_critical_values_interval_certified"]:
        raise AssertionError("A401 complete critical-value inventory is unavailable")
    if not correlated_source["strict_scope"]["beta_minus_B_initial_source_interval_closed"]:
        raise AssertionError("A402S correlated source is unavailable")
    if not handle_execution["strict_scope"]["rank3_handle_Hessian_interval_closed"]:
        raise AssertionError("A383 handle execution is unavailable")

    node_rows = roots["critical_value_certificate"]["nodes"]
    if len(node_rows) != 90:
        raise AssertionError("A401 no longer contains all 90 nodes")
    root_clearances = []
    nodes_by_index = {}
    for row in node_rows:
        index = int(row["distinguished_index"])
        if index in nodes_by_index:
            raise AssertionError("A401 distinguished indices are not unique")
        value = validated.decoded_acb(row["normalized_parameter_ball"])
        distance_lower = validated.lower(abs(value))
        root_clearances.append(distance_lower)
        nodes_by_index[index] = (row, value)
    minimum_root_distance = min(root_clearances)
    clearance = math.nextafter(minimum_root_distance - RADIUS, -math.inf)
    if clearance <= 0.0 or RADIUS >= 0.5:
        raise AssertionError("the proposed common-junction disk is not certified")

    chain = [int(value) for value in identity["selected_branch"]["primitive_chain_coordinates_Z98"]]
    if len(chain) != 98 or chain[90:] != [1, 1, 1, -1, 1, 0, 0, 1]:
        raise AssertionError("A400 primitive chain changed")
    if identity["selected_branch"]["A130_boundary_image_Z4"] != [0, 0, 0, 0]:
        raise AssertionError("A400 boundary closure changed")

    target_rows = []
    target_authority = {}
    for index, coefficient in enumerate(chain[:90], start=1):
        if coefficient == 0:
            continue
        node_path = VALIDATED / f"d{index:03d}.n3.node.refined.json"
        node = load(node_path)
        parameter = validated.decoded_acb(node["certified_node"]["parameter_ball"])
        raw_distance_lower = validated.lower(abs(parameter))
        if raw_distance_lower <= RADIUS:
            raise AssertionError(f"d{index:03d} node enters the junction disk")
        a401_row, normalized = nodes_by_index[index]
        lattice_shift = a401_row["normalizing_lattice_shift"]
        translated = parameter + acb(
            int(lattice_shift[0]), int(lattice_shift[1])
        )
        if not translated.overlaps(normalized):
            raise AssertionError(f"d{index:03d} node does not match A401 modulo the lattice")
        center = midpoint(parameter)
        entry = RADIUS * center / abs(center)
        target_rows.append(
            {
                "distinguished_index": index,
                "root_id": a401_row["root_id"],
                "signed_chain_coefficient": coefficient,
                "canonical_inner_segment": {
                    "symbolic_start": f"e_{index}=R*s_{index}/|s_{index}|",
                    "midpoint_diagnostic_only": pair(entry),
                    "end": pair(0 + 0j),
                },
                "junction_replacement": {
                    "arc": f"e_{index} to h inside |t|<=R",
                    "shared_trunk": "h to 0",
                    "homotopic_relative_endpoints_in_puncture_free_disk": True,
                },
                "canonical_node_distance_from_base_lower": raw_distance_lower,
                "A401_normalized_node_distance_from_base_lower": validated.lower(
                    abs(normalized)
                ),
            }
        )
        target_authority[f"d{index:03d}_certified_node"] = authority(node_path)
    if len(target_rows) != 76:
        raise AssertionError("the selected thimble support is no longer 76")

    handles = []
    labels = ["a1", "b1", "a2", "b2", "a1", "b1", "a2", "b2"]
    branches = ["A", "A", "A", "A", "B", "B", "B", "B"]
    for offset, coefficient in enumerate(chain[90:]):
        handles.append(
            {
                "primitive_handle_index_zero_based": offset,
                "basis_label": labels[offset],
                "branch": branches[offset],
                "signed_coefficient": coefficient,
                "junction_disk_route": (
                    "0 to h then an interior arc to the A-axis exit"
                    if branches[offset] == "A"
                    else "0 to h, already a prefix of the A401 lower B contour"
                ),
            }
        )

    payload = {
        "schema": "MTTQ79HeightFourCommonJunctionEdgeLedger.v1",
        "status": "ROOT_FREE_COMMON_JUNCTION_LEDGER_AND_ZERO_TRUNK_PROVED",
        "artifact": ARTIFACT,
        "root_free_junction_disk": {
            "base": pair(0 + 0j),
            "exact_radius": "1/5",
            "radius_binary64": RADIUS,
            "hub": pair(HUB),
            "torus_injectivity_radius_lower": 0.5,
            "certified_critical_value_count": len(node_rows),
            "minimum_critical_value_torus_distance_lower": minimum_root_distance,
            "critical_value_clearance_from_closed_disk_lower": clearance,
            "closed_disk_contains_no_critical_value": True,
            "smooth_Gauss_Manin_local_system_on_disk": True,
            "disk_simply_connected": True,
        },
        "oriented_edge_ledger": {
            "selected_thimble_rows": target_rows,
            "selected_handle_rows": handles,
            "beta_minus_B_route": {
                "source": "A402S",
                "first_edge": "0 to h to 0.65 on the positive real axis",
                "B_handle_already_promoted_into_correlated_source": True,
                "affine_beta_source_is_not_cancelled_as_a_homogeneous_cycle": True,
            },
            "Picard_Lefschetz_wall": identity["picard_lefschetz_transport"],
            "shared_trunk": {
                "edge": "h to 0",
                "aggregate_boundary_coordinates_Z4": [0, 0, 0, 0],
                "zero_by_A130_integral_boundary_map": True,
                "homogeneous_period_integral_cancels_before_interval_quadrature": True,
            },
        },
        "theorem": {
            "name": "Selected common-junction zero-trunk theorem",
            "proved": True,
            "statement": (
                "Inside the A401-certified root-free disk |t|<=1/5, each "
                "selected thimble tail and handle start may be homotoped to the "
                "hub h=1/5. Parallel transport preserves the exact A130 boundary "
                "relation, so the aggregate homogeneous cycle on the common "
                "h-to-0 trunk is zero and its period/residue contribution is "
                "removed exactly before interval quadrature."
            ),
        },
        "summary": {
            "selected_thimble_count": len(target_rows),
            "primitive_handle_count": len(handles),
            "common_trunk_boundary_rank": 0,
            "minimum_junction_disk_clearance_lower": clearance,
        },
        "authority": {
            "A400_relative_chain_identity": authority(A400),
            "A401_complete_critical_value_inventory": authority(A401),
            "A402S_correlated_beta_minus_B_source": authority(A402S),
            "A383_selected_handle_execution": authority(A383),
            "straight_thimble_transport_engine": authority(
                Path(target_transport.__file__).resolve()
            ),
            "builder_source": authority(Path(__file__).resolve()),
            **target_authority,
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "all_90_critical_values_consumed": True,
            "all_76_selected_thimble_inner_edges_led": True,
            "all_eight_handle_inner_edges_led": True,
            "Picard_Lefschetz_wall_ledgered": True,
            "common_root_free_junction_disk_closed": True,
            "aggregate_common_trunk_cancellation_proved": True,
            "outer_thimble_and_arc_transports_executed": False,
            "full_correlation_preserving_path_execution_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "execute the 76 outer legs and junction arcs, combine their integer "
            "cycles at h, omit the A403 zero trunk, and splice to A402"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Common Junction Edge Ledger (A403) v1\n\n"
        "A403 consumes A401's complete 90-node inventory and proves that the "
        "closed disk `|t|<=1/5` is root-free. Its minimum certified clearance is "
        f"`{clearance:.12g}`. All 76 selected thimble tails and all eight handle "
        "starts are ledgered through the common hub `h=1/5`.\n\n"
        "The A400/A130 boundary image is exactly zero, so the aggregate "
        "homogeneous cycle on the shared `h->0` trunk vanishes before interval "
        "quadrature. The outer legs and junction arcs still require validated "
        "execution; A403 does not prove the covariant zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
