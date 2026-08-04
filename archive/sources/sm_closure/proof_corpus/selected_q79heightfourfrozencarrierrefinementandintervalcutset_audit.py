from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79heightfourfrozencarrierrefinementandintervalcutset"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"


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
    frontier_path = ROOT / candidate["frontier"]

    if candidate["artifact"] != "A133":
        raise AssertionError("A133 artifact label changed")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A133 overclaims exact branch closure")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A133 packet hash mismatch")
    if sha256(frontier_path) != candidate["frontier_sha256"]:
        raise AssertionError("A133 frontier hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("A133 theorem-note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A133 candidate hash mismatch")

    authority = {row["path"]: row["sha256"] for row in packet["authority"]}
    for relative, expected in authority.items():
        if sha256(ROOT / relative) != expected:
            raise AssertionError(f"A133 authority hash mismatch: {relative}")

    period_path = next(
        ROOT / path
        for path in authority
        if path.endswith("selected_alignment_full_integral_basis_period_table.packet.json")
    )
    convergence_path = next(
        ROOT / path
        for path in authority
        if path.endswith("selected_alignment_full_integral_basis_convergence.packet.json")
    )
    a132_path = next(
        ROOT / path
        for path in authority
        if path.endswith("selected_alignment_effective_branch_quotient_and_height4_seed.packet.json")
    )
    beta_path = next(
        ROOT / path
        for path in authority
        if path.endswith("order40_step003.interval.packet.json")
    )
    basis_path = next(
        ROOT / path
        for path in authority
        if path.endswith("selected_alignment_exact_integral_H2_basis.packet.json")
    )

    periods = load(period_path)
    convergence = load(convergence_path)
    a132 = load(a132_path)
    beta_packet = load(beta_path)
    basis = load(basis_path)
    matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in periods["period_matrix_rows"]
        ],
        dtype=np.complex128,
    )
    ell = np.asarray(
        a132["height_four_continuation_seed"]["ell_Z92"], dtype=np.int64
    )
    beta = np.asarray(
        [complex_value(value) for value in beta_packet["endpoint"]["beta_center"]],
        dtype=np.complex128,
    )
    beta_radius = float(beta_packet["endpoint"]["uniform_component_radius_upper"])
    residual = beta - matrix @ ell
    entrywise = np.asarray(
        convergence["primary_entrywise_absolute_difference_envelope_rows"],
        dtype=np.float64,
    )
    period_proxy = entrywise @ np.abs(ell[:90]).astype(np.float64)
    conditional_lower = np.maximum(0.0, np.abs(residual) - beta_radius - period_proxy)
    index = int(np.argmax(conditional_lower))
    target = packet["minimal_strict_interval_target"]
    if periods["form_names"][index] != "E32" or target["form"] != "E32":
        raise AssertionError("A133 separating row changed")
    if index != int(target["row_index"]):
        raise AssertionError("A133 separating row index mismatch")
    budget = float(abs(residual[index]) - beta_radius)
    if abs(budget - target["strict_required_period_combination_radius_upper"]) > 1.0e-14:
        raise AssertionError("A133 strict period-radius budget mismatch")
    if conditional_lower[index] <= 3.0e-3:
        raise AssertionError("A133 proxy separation margin collapsed")
    if period_proxy[index] >= budget / 1.0e4:
        raise AssertionError("A133 proxy is not comfortably inside the strict budget")

    primary_basis = np.asarray(
        basis["primary_basis"]["basis_columns"], dtype=object
    )
    primitive = primary_basis @ np.asarray(ell[:90], dtype=object)
    primitive = np.asarray([int(value) for value in primitive], dtype=np.int64)
    manifest = packet["height_four_seed"]["primitive_thimble_chain"]
    replay = np.zeros(90, dtype=np.int64)
    for row in manifest:
        replay[int(row["distinguished_index"]) - 1] = int(row["coefficient"])
    if not np.array_equal(replay, primitive[:90]):
        raise AssertionError("A133 primitive thimble manifest mismatch")
    if packet["height_four_seed"]["primitive_handle_coordinates"] != primitive[90:].tolist():
        raise AssertionError("A133 primitive handle manifest mismatch")
    if len(manifest) != 71:
        raise AssertionError("A133 primitive support changed")

    scope = packet["scope"]
    if not scope["beta_interval_refinement_closed"]:
        raise AssertionError("A133 beta refinement is not closed")
    if scope["A131_two_run_proxy_is_an_interval_certificate"]:
        raise AssertionError("A133 promotes a convergence proxy to interval proof")
    if scope["fixed_carrier_exact_separation_proved"]:
        raise AssertionError("A133 invents fixed-carrier exact separation")
    if scope["covariant_alignment_zero_solved"]:
        raise AssertionError("A133 invents a covariant alignment zero")

    print("q79 A133 height-four frozen-carrier refinement audit: PASS")
    print(
        "closed: rigorous beta radius "
        f"{packet['refined_beta']['new_uniform_component_radius']:.6e}"
    )
    print(
        "cutset: one E32 combined-period interval with radius below "
        f"{budget:.6e}"
    )
    print(
        "diagnostic: A131 proxy gives conditional separation lower "
        f"{conditional_lower[index]:.6e}, but is not interval proof"
    )
    print("open: combined-period interval and covariant F/J continuation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
