from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_q79effectiveintegralbranchquotientandheightfourseed.candidate.json"
CERTIFICATE = ROOT / "certificates" / "selected_q79effectiveintegralbranchquotientandheightfourseed.certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    packet = load(packet_path)
    if candidate["artifact"] != "A132":
        raise AssertionError("A132 artifact label changed")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A132 packet hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("A132 proof-note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A132 candidate hash mismatch")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A132 overclaims exact branch closure")

    authority = packet["authority"]
    for path_key, hash_key in (
        ("period_table", "period_table_sha256"),
        ("period_convergence", "period_convergence_sha256"),
        ("beta_packet", "beta_packet_sha256"),
        ("integral_basis", "integral_basis_sha256"),
        ("builder_source", "builder_source_sha256"),
    ):
        path = ROOT / authority[path_key]
        if sha256(path) != authority[hash_key]:
            raise AssertionError(f"A132 authority hash mismatch: {path_key}")

    periods = load(ROOT / authority["period_table"])
    matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in periods["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    if matrix.shape != (8, 92) or np.any(matrix[:, 90:] != 0.0):
        raise AssertionError("A132 exact Leray-null factorization failed")
    quotient = packet["exact_effective_branch_quotient"]
    if quotient["null_period_entries"] != 16:
        raise AssertionError("A132 null-period count changed")
    if quotient["additional_exact_kernel_excluded"]:
        raise AssertionError("A132 invents exact-kernel completeness")

    beta_packet = load(ROOT / authority["beta_packet"])
    beta = np.asarray(
        [
            complex_value(value)
            for value in beta_packet["tight_endpoint"]["beta_center"]
        ],
        dtype=np.complex128,
    )
    beta_radius = float(
        beta_packet["tight_endpoint"]["uniform_component_radius_upper"]
    )
    seed = packet["height_four_continuation_seed"]
    ell = np.asarray(seed["ell_Z92"], dtype=np.int64)
    if ell.shape != (92,) or np.any(ell[90:] != 0):
        raise AssertionError("A132 canonical quotient representative failed")
    residual = beta - matrix @ ell
    residual_maximum = float(np.max(np.abs(residual)))
    if abs(residual_maximum - seed["residual_maximum_absolute_value"]) > 1.0e-12:
        raise AssertionError("A132 residual replay mismatch")
    if seed["coefficient_height"] != 4:
        raise AssertionError("A132 seed height changed")
    if residual_maximum >= beta_radius:
        raise AssertionError("A132 seed left beta-center enclosure")
    search = packet["fixed_height_search"]
    if search["minimum_center_nonseparated_height_in_fixed_search"] != 4:
        raise AssertionError("A132 fixed-search height frontier changed")
    height_three = search["best_candidate_by_maximum_height"]["3"]
    if height_three is None or height_three["residual_maximum_absolute_value"] <= beta_radius:
        raise AssertionError("A132 fixed-search height-three guard failed")
    if packet["strict_scope"]["exact_Z90_membership_proved"]:
        raise AssertionError("A132 promotes center overlap to exact membership")
    if not packet["strict_scope"]["period_two_run_envelopes_are_not_interval_bounds"]:
        raise AssertionError("A132 period-error guard missing")

    print("q79 A132 effective branch quotient and height-four seed audit: PASS")
    print("closed: exact primitive Leray-null quotient Z92 -> effective Z90")
    print(
        "computed: fixed-search height-4 continuation seed, "
        f"residual {residual_maximum:.6e} < beta radius {beta_radius:.6e}"
    )
    print("open: interval periods, exact membership, covariant PGL3 zero")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
