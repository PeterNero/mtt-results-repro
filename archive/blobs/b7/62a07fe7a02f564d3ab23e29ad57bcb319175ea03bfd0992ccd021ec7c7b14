from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79e32thimbleregularsingularreduction"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
J = np.asarray(
    [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]],
    dtype=object,
)
I4 = np.eye(4, dtype=object)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_rank_one(matrix: np.ndarray) -> bool:
    if not np.any(matrix != 0):
        return False
    return all(
        matrix[a, c] * matrix[b, d] - matrix[a, d] * matrix[b, c] == 0
        for a in range(4)
        for b in range(a + 1, 4)
        for c in range(4)
        for d in range(c + 1, 4)
    )


def primitive_image_generator(matrix: np.ndarray) -> list[int]:
    for column in range(4):
        values = [int(matrix[row, column]) for row in range(4)]
        if any(values):
            divisor = 0
            for value in values:
                divisor = math.gcd(divisor, abs(value))
            values = [value // divisor for value in values]
            if next(value for value in values if value) < 0:
                values = [-value for value in values]
            return values
    raise AssertionError("missing image generator")


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    packet = load(packet_path)
    frontier_path = ROOT / candidate["frontier"]

    if candidate["artifact"] != "A135":
        raise AssertionError("A135 artifact label changed")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("A135 overclaims weighted closure")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("A135 packet hash mismatch")
    if sha256(frontier_path) != candidate["frontier_sha256"]:
        raise AssertionError("A135 frontier hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("A135 note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("A135 candidate hash mismatch")
    for authority in packet["authority"]:
        if sha256(ROOT / authority["path"]) != authority["sha256"]:
            raise AssertionError(f"A135 authority mismatch: {authority['path']}")

    rows = packet["exact_selected_inventory"]["rows"]
    if len(rows) != 71:
        raise AssertionError("A135 selected support changed")
    if sum(abs(int(row["height_four_chain_coefficient"])) for row in rows) != 123:
        raise AssertionError("A135 selected L1 norm changed")
    for row in rows:
        matrix = np.asarray(row["integral_local_monodromy_T"], dtype=object)
        nilpotent = matrix - I4
        if nilpotent.tolist() != row["integer_logarithm_numerator_N_equals_T_minus_I"]:
            raise AssertionError("A135 stored local logarithm mismatch")
        if not exact_rank_one(nilpotent):
            raise AssertionError("A135 local logarithm rank mismatch")
        if np.any(nilpotent @ nilpotent != 0):
            raise AssertionError("A135 local logarithm nilpotence mismatch")
        if np.any(matrix.T @ J @ matrix != J):
            raise AssertionError("A135 symplectic replay mismatch")
        vector = primitive_image_generator(nilpotent)
        if vector != row["primitive_vanishing_image_generator"]:
            raise AssertionError("A135 primitive image direction mismatch")
        vector_array = np.asarray(vector, dtype=object)
        if np.any(nilpotent @ vector_array != 0):
            raise AssertionError("A135 image is not in kernel")
        if np.any(matrix @ vector_array != vector_array):
            raise AssertionError("A135 vanishing direction is not fixed")

    theorem = packet["local_theorem"]
    if not theorem["proved_for_all_selected_thimbles"]:
        raise AssertionError("A135 theorem not marked proved")
    scope = packet["scope"]
    if not scope["regular_singular_nilpotent_reduction_closed"]:
        raise AssertionError("A135 nilpotent reduction not closed")
    if scope["local_Frobenius_coefficients_numerically_emitted"]:
        raise AssertionError("A135 invents numerical Frobenius coefficients")
    if scope["weighted_71_thimble_interval_closed"]:
        raise AssertionError("A135 invents weighted interval closure")
    if scope["fixed_carrier_exact_separation_proved"]:
        raise AssertionError("A135 invents fixed-carrier separation")

    print("q79 A135 E32 thimble regular-singular reduction audit: PASS")
    print("closed: 71/71 exact local PL logarithms have rank 1 and square zero")
    print("closed: every primitive vanishing image direction lies in ker(N) and is fixed by T")
    print("closed: log-free Frobenius recurrence with (nI-R)^-1=(I+R/n)/n")
    print("open: numerical Frobenius balls, weighted E32 interval, and covariant F/J")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
