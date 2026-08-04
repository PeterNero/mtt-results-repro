from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79heightfoure32handleintervalandthimblecutset"
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

    if candidate["artifact"] != "A134":
        raise AssertionError("A134 artifact label changed")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A134 overclaims branch closure")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A134 packet hash mismatch")
    if sha256(frontier_path) != candidate["frontier_sha256"]:
        raise AssertionError("A134 frontier hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("A134 theorem-note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A134 candidate hash mismatch")

    authority = {row["path"]: row["sha256"] for row in packet["authority"]}
    for relative, expected in authority.items():
        if sha256(ROOT / relative) != expected:
            raise AssertionError(f"A134 authority hash mismatch: {relative}")
    a133_path = next(
        ROOT / path for path in authority if path.endswith("interval_cutset.packet.json")
    )
    handle_path = next(
        ROOT / path
        for path in authority
        if path.endswith("E32_handle_combination.interval.packet.json")
    )
    periods_path = next(
        ROOT / path
        for path in authority
        if path.endswith("full_integral_basis_period_table.packet.json")
    )
    handles_path = next(
        ROOT / path
        for path in authority
        if path.endswith("primitive_handle_periods.packet.json")
    )
    a133 = load(a133_path)
    handle = load(handle_path)
    periods = load(periods_path)
    handles = load(handles_path)

    matrix = np.asarray(
        [[complex_value(value) for value in row] for row in periods["period_matrix_rows"]],
        dtype=np.complex128,
    )
    ell = np.asarray(
        a133["height_four_seed"]["effective_coordinates_Z90"] + [0, 0],
        dtype=np.int64,
    )
    handle_coordinates = np.asarray(
        a133["height_four_seed"]["primitive_handle_coordinates"],
        dtype=np.int64,
    )
    handle_matrix = np.asarray(
        [
            [complex_value(value) for value in row]
            for row in handles["primitive_handle_period_matrix"]
        ],
        dtype=np.complex128,
    )
    decomposition = packet["selected_E32_decomposition"]
    full_center = complex(matrix[5] @ ell)
    floating_handle = complex(handle_matrix[5] @ handle_coordinates)
    floating_thimble = full_center - floating_handle
    if abs(full_center - complex_value(decomposition["A131_full_combination_center"])) > 1e-14:
        raise AssertionError("A134 full center replay changed")
    if abs(floating_handle - complex_value(decomposition["A131_floating_handle_combination_center"])) > 1e-14:
        raise AssertionError("A134 handle center replay changed")
    if abs(floating_thimble - complex_value(decomposition["A131_floating_thimble_combination_center"])) > 1e-14:
        raise AssertionError("A134 thimble center replay changed")

    interval = handle["E32_handle_combination"]["interval"]
    interval_center = complex_value(interval["center"])
    interval_radius = float(interval["uniform_radius_upper"])
    center_shift = abs(interval_center - floating_handle)
    ledger = packet["strict_budget_ledger"]
    total_budget = float(
        a133["minimal_strict_interval_target"][
            "strict_required_period_combination_radius_upper"
        ]
    )
    remaining = total_budget - interval_radius - center_shift
    if abs(remaining - ledger["remaining_weighted_thimble_combination_radius_budget"]) > 1e-14:
        raise AssertionError("A134 remaining budget mismatch")
    if remaining <= 2.8e-3:
        raise AssertionError("A134 weighted thimble budget collapsed")
    if int(decomposition["primitive_thimble_support"]) != 71:
        raise AssertionError("A134 thimble support changed")
    if int(decomposition["primitive_thimble_l1_norm"]) != 123:
        raise AssertionError("A134 thimble L1 norm changed")

    scope = packet["scope"]
    if not scope["selected_handle_combination_interval_closed"]:
        raise AssertionError("A134 handle interval not marked closed")
    if scope["selected_thimble_combination_interval_closed"]:
        raise AssertionError("A134 invents a weighted thimble interval")
    if scope["fixed_carrier_exact_separation_proved"]:
        raise AssertionError("A134 invents fixed-carrier separation")
    if scope["covariant_alignment_zero_solved"]:
        raise AssertionError("A134 invents a covariant alignment zero")

    print("q79 A134 E32 handle interval and thimble cutset audit: PASS")
    print(f"closed: selected E32 handle interval radius {interval_radius:.6e}")
    print(f"agreement: A131 handle center difference {center_shift:.6e}")
    print(f"open cutset: one weighted 71-thimble interval radius < {remaining:.6e}")
    print("then: frozen-carrier decision and covariant F/J continuation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
