from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_selected_q79_height4_survivor_queue_and_E32_priority as builder
from explore_q79_a126_integral_period_branch_lll import kannan_candidates, realification


CANDIDATE = ROOT / "candidate_data" / "selected_q79heightfoursurvivorqueueande32priority.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79heightfoursurvivorqueueande32priority.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recompute-grid",
        action="store_true",
        help="rerun all 355 A132 Kannan embeddings and prove finite-grid completeness",
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    packet = load(packet_path)
    if candidate["artifact"] != "A208" or packet["artifact"] != "A208":
        raise AssertionError("A208 artifact label changed")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A208 packet hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("A208 proof-note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A208 candidate hash mismatch")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A208 overclaims carrier closure")

    for path_key, hash_key in (
        ("A132_packet", "A132_packet_sha256"),
        ("A134_support_packet", "A134_support_packet_sha256"),
        ("A207_decision_packet", "A207_decision_packet_sha256"),
        ("period_table", "period_table_sha256"),
        ("period_convergence", "period_convergence_sha256"),
        ("A132_beta_packet", "A132_beta_packet_sha256"),
        ("refined_beta_packet", "refined_beta_packet_sha256"),
        ("integral_basis", "integral_basis_sha256"),
        ("builder_source", "builder_source_sha256"),
    ):
        path = ROOT / packet["authority"][path_key]
        if sha256(path) != packet["authority"][hash_key]:
            raise AssertionError(f"A208 authority hash mismatch: {path_key}")

    inputs = builder.search_inputs()
    period_matrix = inputs["period_matrix"]
    primary_basis = inputs["primary_basis"]
    original_beta = inputs["beta"]
    real_matrix = np.vstack(
        [period_matrix[:, :90].real, period_matrix[:, :90].imag]
    )
    real_beta = realification(original_beta)
    refined_beta_packet = load(builder.REFINED_BETA)
    refined_beta = np.asarray(
        [
            complex(float(value["real"]), float(value["imaginary"]))
            for value in refined_beta_packet["endpoint"]["beta_center"]
        ],
        dtype=np.complex128,
    )
    a134 = load(builder.A134)
    old_support = {
        int(row["distinguished_index"])
        for row in a134["selected_E32_decomposition"]["primitive_thimble_chain"]
    }

    rows = packet["height_four_candidates"]
    if len(rows) != 5:
        raise AssertionError("A208 height-four candidate count changed")
    if [row["A132_objective_rank"] for row in rows] != [1, 2, 3, 4, 5]:
        raise AssertionError("A208 objective order changed")
    objective_values = []
    for row in rows:
        ell90 = [int(value) for value in row["effective_coordinates_Z90"]]
        if len(ell90) != 90 or max(abs(value) for value in ell90) != 4:
            raise AssertionError("A208 effective height-four vector changed")
        ell = np.asarray(ell90 + [0, 0], dtype=np.float64)
        primitive = np.asarray(
            primary_basis @ np.asarray(ell90, dtype=object), dtype=object
        )
        thimble = [int(value) for value in primitive[:90]]
        handles = [int(value) for value in primitive[90:]]
        sparse = [
            {"distinguished_index": index + 1, "coefficient": value}
            for index, value in enumerate(thimble)
            if value
        ]
        if sparse != row["primitive_thimble_chain"]:
            raise AssertionError("A208 primitive thimble replay mismatch")
        if handles != row["primitive_handle_coordinates"]:
            raise AssertionError("A208 primitive handle replay mismatch")
        missing = sorted(
            {item["distinguished_index"] for item in sparse} - old_support
        )
        if missing != row["new_E32_interval_indices_relative_to_A207"]:
            raise AssertionError("A208 incremental interval support mismatch")

        refined_residual = refined_beta - period_matrix @ ell
        e32_absolute = float(abs(refined_residual[builder.E32_INDEX]))
        if abs(e32_absolute - row["refined_floating_E32_residual_absolute_value"]) > 1.0e-12:
            raise AssertionError("A208 refined E32 residual replay mismatch")
        original_residual = original_beta - period_matrix @ ell
        original_maximum = float(np.max(np.abs(original_residual)))
        if abs(original_maximum - row["A132_center_residual_maximum"]) > 1.0e-12:
            raise AssertionError("A208 A132 residual replay mismatch")
        if original_maximum >= float(inputs["beta_radius"]):
            raise AssertionError("A208 row left the A132 beta component balls")

        witness = row["Kannan_witness"]
        emitted = kannan_candidates(
            real_matrix,
            real_beta,
            scale=int(witness["embedding_scale"]),
            coefficient_weight=int(witness["coefficient_weight"]),
            marker_weight=int(witness["marker_weight"]),
        )
        if tuple(ell90) not in {
            tuple(int(value) for value in emitted_ell)
            for _method, emitted_ell in emitted
        }:
            raise AssertionError("A208 Kannan witness does not emit recorded vector")
        objective_values.append(
            (
                row["A132_center_residual_maximum"],
                row["A132_center_residual_l2"],
                row["effective_l1_norm"],
            )
        )

    if objective_values != sorted(objective_values):
        raise AssertionError("A208 A132 objective ranking changed")
    e32_priority = min(
        rows,
        key=lambda row: (
            row["refined_floating_E32_residual_absolute_value"],
            row["A132_objective_rank"],
        ),
    )
    if e32_priority["A132_objective_rank"] != 3:
        raise AssertionError("A208 E32-priority survivor changed")
    if rows[0]["A207_decision"] != "REJECTED_BY_CERTIFIED_E32_ZERO_EXCLUSION":
        raise AssertionError("A208 lost the A207 rejection")
    if any(row["A207_decision"] != "UNTESTED" for row in rows[1:]):
        raise AssertionError("A208 invents a survivor decision")

    union = sorted(
        {
            index
            for row in rows[1:]
            for index in row["new_E32_interval_indices_relative_to_A207"]
        }
    )
    ledger = packet["A207_survivor_ledger"]
    if union != ledger["additional_interval_union"] or len(union) != 15:
        raise AssertionError("A208 15-row interval union changed")
    if packet["strict_scope"]["global_height_four_completeness_over_Z90_proved"]:
        raise AssertionError("A208 promotes fixed-grid enumeration to Z90 completeness")
    if packet["symmetry_policy"]["quotient_applied"]:
        raise AssertionError("A208 silently quotients an unproved symmetry")

    if arguments.recompute_grid:
        records = builder.collect_records(inputs)
        center_nonseparated = [
            record
            for record in records
            if record["residual_maximum_absolute_value"] < float(inputs["beta_radius"])
        ]
        height_four = sorted(
            [
                record
                for record in center_nonseparated
                if record["coefficient_height"] == 4
            ],
            key=builder.objective,
        )
        if (len(records), len(center_nonseparated), len(height_four)) != (575, 85, 5):
            raise AssertionError("A208 exhaustive fixed-grid replay changed")
        if [record["ell_Z92"][:90] for record in height_four] != [
            row["effective_coordinates_Z90"] for row in rows
        ]:
            raise AssertionError("A208 exhaustive fixed-grid candidate set changed")

    print("q79 A208 height-four survivor queue and E32 priority audit: PASS")
    print("closed: complete enumeration of the finite A132 grid's five height-four rows")
    print("closed: unique A132 objective winner; A207 rejects exactly that one row")
    print(
        "computed: A132-rank-3 survivor has the smallest floating E32 residual, "
        f"{e32_priority['refined_floating_E32_residual_absolute_value']:.6e}"
    )
    print("next: certify the 15-row incremental E32 union and survivor handle combinations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
