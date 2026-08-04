from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "n3.chain.relation_l1.a393.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def fraction(value: dict[str, int]) -> Fraction:
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def main() -> int:
    packet = load(PACKET)
    require(packet["artifact"] == "A393", "A393 artifact changed")
    require(packet["schema"] == "MTTQ79Rank3ChainRelationL1Optimality.v1", "A393 schema changed")
    require(packet["status"] == "PL_CORRECTED_RANK3_CHAIN_L1_MINIMAL_MODULO_SURFACE_RELATIONS_PROVED", "A393 status changed")
    chain = [int(value) for value in packet["PL_corrected_chain_coordinates"]]
    relations = [[int(value) for value in row] for row in packet["surface_relation_matrix_98_by_4"]]
    dual = [fraction(value) for value in packet["dual_witness"]]
    require(len(chain) == len(relations) == len(dual) == 98, "A393 dimension changed")
    require(all(len(row) == 4 for row in relations), "A393 relation matrix changed")
    require(chain[64] == 4, "A393 lost the PL-corrected d065 coefficient")
    require(sum(value != 0 for value in chain[:90]) == 76, "A393 thimble support changed")
    require(sum(abs(value) for value in chain) == 174, "A393 L1 norm changed")
    require(max(abs(value) for value in dual) <= 1, "A393 dual norm exceeds one")
    annihilation = [
        sum((Fraction(relations[row][column]) * dual[row] for row in range(98)), Fraction(0))
        for column in range(4)
    ]
    require(annihilation == [Fraction(0)] * 4, "A393 dual does not annihilate R")
    pairing = sum((dual[index] * chain[index] for index in range(98)), Fraction(0))
    require(pairing == 174, "A393 dual pairing changed")
    replay = packet["exact_replay"]
    require(int(replay["chain_l1_norm"]) == 174, "A393 replay norm changed")
    require(fraction(replay["dual_l_infinity_norm"]) == 1, "A393 replay dual norm changed")
    require([fraction(value) for value in replay["relation_transpose_times_dual"]] == annihilation, "A393 replay annihilation changed")
    require(fraction(replay["dual_pairing_with_chain"]) == pairing, "A393 replay pairing changed")
    require(packet["theorem"]["global_integer_relation_shift_optimality"] is True, "integer theorem lost")
    require(packet["theorem"]["global_real_relation_shift_optimality"] is True, "real theorem lost")
    for label, record in packet["authority"].items():
        path = ROOT / record["path"]
        require(path.exists(), f"A393 authority absent: {label}")
        require(sha256(path) == record["sha256"], f"A393 authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["unweighted_L1_relation_compression_closed_by_optimality"] is True, "A393 no-go lost")
    for key in (
        "observed_SM_values_used",
        "weighted_interval_radius_optimality_proved",
        "minimum_support_L0_optimality_proved",
        "coupled_chain_period_transport_closed",
        "interval_Newton_existence_and_uniqueness_closed",
        "covariant_zero_proved",
        "full_SM_closure_proved",
    ):
        require(scope[key] is False, f"A393 overclaims {key}")
    print("PASS: A393 proves exact global L1 minimality modulo all four surface relations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
