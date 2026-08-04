from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
PROBE = PERIOD_DIRECTORY / "covariant_floating_probe"
VALIDATED = PROBE / "validated_transport"
TRANS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
    / "normalized_Deligne_Leray_transgression.packet.json"
)
SAME_CARRIER = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "same_carrier_integral_branch_cutset.theorem.packet.json"
)
PRESENTATION = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_coupled_integral_H2_chain_presentation.packet.json"
)
BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
A231 = VALIDATED / "n3.chain.frontier.json"
A376 = VALIDATED / "n3.rank3.anchored_beta.interval.json"
A373 = VALIDATED / "n3.certified76.recomposition.json"
OUTPUT = VALIDATED / "n3.relative_chain_identity.a400.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourSelectedRelativeChainIdentity_A400_v1.md"
ARTIFACT = "A400"


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


def matrix_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    if not matrix or any(len(row) != len(vector) for row in matrix):
        raise ValueError("integer matrix-vector dimensions changed")
    return [sum(int(value) * int(vector[index]) for index, value in enumerate(row)) for row in matrix]


def manifest(vector: list[int]) -> list[dict[str, int]]:
    return [
        {"distinguished_index": index + 1, "coefficient": int(value)}
        for index, value in enumerate(vector)
        if int(value) != 0
    ]


def main() -> int:
    trans = load(TRANS)
    same_carrier = load(SAME_CARRIER)
    presentation = load(PRESENTATION)
    basis = load(BASIS)
    a208 = load(A208)
    a231 = load(A231)
    beta = load(A376)
    chain_interval = load(A373)

    if not trans["theorem"]["proved"]:
        raise AssertionError("A121 Deligne transgression theorem is not closed")
    if not same_carrier["theorem"]["proved"]:
        raise AssertionError("same-carrier period theorem is not closed")
    if not presentation["theorem"]["proved"]:
        raise AssertionError("A130 integral H2 presentation theorem is not closed")
    if not basis["exact_checks"]["complete_integral_endpoint_basis"]:
        raise AssertionError("A130 exact endpoint basis is not complete")

    candidates = [
        row
        for row in a208["height_four_candidates"]
        if int(row["A132_objective_rank"]) == 3
    ]
    if len(candidates) != 1:
        raise AssertionError("rank-3 branch is no longer unique in A208")
    candidate = candidates[0]
    ell = [int(value) for value in candidate["effective_coordinates_Z90"]]
    basis_columns = [
        [int(value) for value in row]
        for row in basis["primary_basis"]["basis_columns"]
    ]
    if len(basis_columns) != 98 or len(ell) != 90:
        raise AssertionError("A130/A208 branch dimensions changed")
    primitive = matrix_vector(basis_columns, ell)
    boundary = [
        [int(value) for value in row]
        for row in presentation["chain_complex"]["boundary_matrix_rows"]
    ]
    boundary_image = matrix_vector(boundary, primitive)
    if boundary_image != [0, 0, 0, 0]:
        raise AssertionError("rank-3 primitive branch is not a closed A130 cycle")

    thimbles = primitive[:90]
    handles = primitive[90:]
    selected_manifest = manifest(thimbles)
    if selected_manifest != candidate["primitive_thimble_chain"]:
        raise AssertionError("rank-3 primitive thimble manifest changed")
    if handles != [int(value) for value in candidate["primitive_handle_coordinates"]]:
        raise AssertionError("rank-3 primitive handle coordinates changed")
    if a231["selected_candidate"]["candidate_id"] != candidate["candidate_id"]:
        raise AssertionError("A231 replays a different branch")
    if [int(value) for value in a231["selected_candidate"]["primitive_handle_coordinates"]] != handles:
        raise AssertionError("A231 handle decomposition changed")
    replay_manifest = [
        {
            "distinguished_index": int(row["distinguished_index"]),
            "coefficient": int(row["chain_coefficient"]),
        }
        for row in a231["exact_floating_decomposition"]["thimble_rows"]
    ]
    if replay_manifest != selected_manifest:
        raise AssertionError("A231 numerical chain differs from the exact A130 branch")
    if int(chain_interval["certified_A219_priority_prefix_length"]) != 76:
        raise AssertionError("A373 no longer encloses the complete selected chain")
    if not beta["strict_scope"]["rank3_anchored_beta_interval_closed"]:
        raise AssertionError("A376 rank-3 beta endpoint interval is open")

    wall = a231["exact_floating_decomposition"]
    payload = {
        "schema": "MTTQ79HeightFourSelectedRelativeChainIdentity.v1",
        "status": "RANK3_EXACT_RELATIVE_CHAIN_IDENTITY_CLOSED_CORRELATED_PATH_EXECUTION_OPEN",
        "artifact": ARTIFACT,
        "selected_branch": {
            "candidate_id": candidate["candidate_id"],
            "A132_objective_rank": 3,
            "effective_integral_coordinates_Z90": ell,
            "effective_height": max(abs(value) for value in ell),
            "effective_l1_norm": sum(abs(value) for value in ell),
            "primitive_chain_coordinates_Z98": primitive,
            "primitive_thimble_support": len(selected_manifest),
            "primitive_thimble_l1_norm": sum(abs(value) for value in thimbles),
            "primitive_handle_coordinates": handles,
            "A130_boundary_image_Z4": boundary_image,
            "closed_integral_cycle": True,
        },
        "picard_lefschetz_transport": {
            "wall_source_distinguished_index": int(
                wall["PL_wall_source_distinguished_index"]
            ),
            "crossing_period_distinguished_index": int(
                wall["PL_crossing_period_distinguished_index"]
            ),
            "integral_wall_weight": int(wall["PL_wall_weight"]),
            "A231_corrected_replay_maximum_error": float(
                wall["stored_corrected_replay_maximum_error"]
            ),
            "interpretation": (
                "The displayed numerical representative is transported across the "
                "preselected Picard-Lefschetz wall; this changes the marked integral "
                "representative, not closedness of the transported cycle."
            ),
        },
        "theorem": {
            "name": "Q79SelectedRank3RelativeChainIdentityTheorem",
            "proved": True,
            "statement": (
                "Let ell be the A208 rank-3 integral branch and C_ell the A130 "
                "integral H2 cycle obtained from it. Then partial C_ell=0 exactly. "
                "On the selected same-carrier chamber, the covariant residual is "
                "F_r(A,ell)=integral_(Delta_A-C_ell,A) omega_r(A)=beta_r(A)-"
                "sum_I Pi_rI(A) ell_I, with the preselected Picard-Lefschetz "
                "transport applied to the marked representative."
            ),
            "proof_dependencies": [
                "A121 normalized Deligne/Leray transgression modulo the integral period image",
                "same-carrier period equation and endpoint basis invariance theorem",
                "A130 exact coupled integral H2 presentation",
                "exact A130-basis multiplication by the A208 rank-3 integer vector",
                "A231 marked Picard-Lefschetz-corrected numerical replay",
            ],
        },
        "correlation_contract": {
            "mathematically_available": (
                "The relative chain Delta_A-C_ell may be evaluated as one signed "
                "chain network, and repeated directed path segments may be cancelled "
                "exactly before interval quadrature."
            ),
            "not_present_in_current_endpoint_packets": (
                "A376 beta and A373 thimble periods are separately enclosed endpoint "
                "balls with no shared affine noise symbols or common edge ledger."
            ),
            "forbidden_inference": (
                "Cancellation in floating centers does not permit subtraction of "
                "independent interval radii or promotion of A386 to a zero theorem."
            ),
            "required_computation": (
                "Emit a common oriented edge/path ledger for the Abel-Jacobi B sweep, "
                "76 thimbles, eight handle cylinders and the PL wall update; combine "
                "integer coefficients before validated transport."
            ),
        },
        "authority": {
            "A121_transgression": authority(TRANS),
            "same_carrier_theorem": authority(SAME_CARRIER),
            "A130_chain_presentation": authority(PRESENTATION),
            "A130_exact_H2_basis": authority(BASIS),
            "A208_rank3_branch": authority(A208),
            "A231_chain_replay": authority(A231),
            "A376_beta_interval": authority(A376),
            "A373_chain_interval": authority(A373),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "rank3_integral_branch_coordinates_fixed": True,
            "rank3_primitive_cycle_closed_exactly": True,
            "same_carrier_relative_period_identity_closed": True,
            "A231_marked_PL_replay_consumed": True,
            "correlation_preserving_path_execution_closed": False,
            "existing_independent_endpoint_boxes_may_be_correlated_retroactively": False,
            "integral_branch_selected_by_a_zero_theorem": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "complete the ranked far-cut chain tightening; in parallel emit the "
            "common oriented edge ledger required for a joint relative-chain transport"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Selected Relative-Chain Identity (A400) v1\n\n"
        "A400 multiplies the A208 rank-3 integer vector through the exact A130 "
        "`98 x 90` primary basis and verifies that its four boundary coordinates "
        "vanish identically. The resulting cycle has 76 nonzero thimble "
        f"coefficients, primitive thimble L1 norm `{sum(abs(value) for value in thimbles)}`, "
        f"and handle coordinates `{handles}`.\n\n"
        "Together with A121 and the same-carrier theorem, this proves that the "
        "selected residual is one relative-period integral `beta-Pi*ell`. It does "
        "not retroactively correlate the separately computed A376 and A373 balls. "
        "A common signed path ledger and joint validated transport are still needed "
        "to realize that cancellation numerically.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(
        json.dumps(
            {
                "boundary_image": boundary_image,
                "thimble_support": len(selected_manifest),
                "thimble_l1": sum(abs(value) for value in thimbles),
                "handle_coordinates": handles,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
