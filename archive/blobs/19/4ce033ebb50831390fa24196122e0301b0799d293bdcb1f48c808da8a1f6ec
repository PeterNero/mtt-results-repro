from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79signedsheetspinliftreduction"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"


@dataclass(frozen=True)
class Qsqrt2:
    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __add__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational + other.rational, self.radical + other.radical)

    def __sub__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(self.rational - other.rational, self.radical - other.radical)

    def __neg__(self) -> Qsqrt2:
        return Qsqrt2(-self.rational, -self.radical)

    def __mul__(self, other: Qsqrt2) -> Qsqrt2:
        return Qsqrt2(
            self.rational * other.rational + 2 * self.radical * other.radical,
            self.rational * other.radical + self.radical * other.rational,
        )


Quaternion = tuple[Qsqrt2, Qsqrt2, Qsqrt2, Qsqrt2]
ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))
MINUS_ONE = Qsqrt2(Fraction(-1))
ROOT_HALF = Qsqrt2(Fraction(0), Fraction(1, 2))
Q_ONE: Quaternion = (ONE, ZERO, ZERO, ZERO)
Q_MINUS_ONE: Quaternion = (MINUS_ONE, ZERO, ZERO, ZERO)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def q_neg(value: Quaternion) -> Quaternion:
    return tuple(-entry for entry in value)  # type: ignore[return-value]


def q_mul(left: Quaternion, right: Quaternion) -> Quaternion:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


def q_pow(value: Quaternion, exponent: int) -> Quaternion:
    output = Q_ONE
    for _ in range(exponent):
        output = q_mul(output, value)
    return output


def generated_group(generators: list[Quaternion]) -> set[Quaternion]:
    group = {Q_ONE}
    frontier = [Q_ONE]
    expanded = generators + [q_neg(generator) for generator in generators]
    while frontier:
        current = frontier.pop()
        for generator in expanded:
            candidate = q_mul(current, generator)
            if candidate not in group:
                group.add(candidate)
                frontier.append(candidate)
    return group


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    packet = load(packet_path)

    if candidate["artifact"] != "FoundationalBridge-FB2":
        raise AssertionError("FB2 artifact label changed")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("FB2 overclaims global Spin closure")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("FB2 packet hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("FB2 note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("FB2 candidate hash mismatch")
    for authority in packet["authority"]:
        if sha256(ROOT / authority["path"]) != authority["sha256"]:
            raise AssertionError(f"FB2 authority mismatch: {authority['path']}")

    if packet["q79_sheet_monodromy_theorem"]["monodromy_group"] != "S3":
        raise AssertionError("q79 sheet monodromy group changed")
    if not packet["q79_sheet_monodromy_theorem"]["proved"]:
        raise AssertionError("q79 S3 theorem not marked proved")

    q1: Quaternion = (ZERO, ROOT_HALF, -ROOT_HALF, ZERO)
    q2: Quaternion = (ZERO, ZERO, ROOT_HALF, -ROOT_HALF)
    if q_pow(q1, 2) != Q_MINUS_ONE or q_pow(q2, 2) != Q_MINUS_ONE:
        raise AssertionError("binary transposition squares changed")
    if q_mul(q_mul(q1, q2), q1) != q_mul(q_mul(q2, q1), q2):
        raise AssertionError("binary braid relation failed")
    if q_pow(q_mul(q1, q2), 3) != Q_MINUS_ONE:
        raise AssertionError("binary Coxeter central sign changed")
    group = generated_group([q1, q2])
    if len(group) != 12 or Q_MINUS_ONE not in group:
        raise AssertionError("binary preimage is not Dic_3 of order 12")

    theorem = packet["binary_spin_theorem"]
    if theorem["extension_splits"]:
        raise AssertionError("non-split binary extension was silently split")
    if not theorem["local_braid_lift_exists"]:
        raise AssertionError("local braid lift was lost")
    contract = packet["global_spin_contract"]
    if contract["global_Spin_lift_closed"] or contract["closed_count"] != 0:
        raise AssertionError("global q79 Spin relation data was invented")
    if packet["worldinworld_Q_source_status"]["selected_Q_or_closure_Hessian_emitted"]:
        raise AssertionError("FB2 invented the world-in-world Q source")

    print("q79 signed-sheet Spin-lift reduction audit: PASS")
    print("closed: connected degree-three cover plus ordinary tangency gives S3 monodromy")
    print("closed: exact local braid lift generates non-split Dic_3 of order 12")
    print("open: global relator signs, w2, branch extension, and selected Q/Hessian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
