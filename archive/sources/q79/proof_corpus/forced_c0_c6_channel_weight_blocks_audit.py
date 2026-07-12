"""Audit forced C0 and C6 channel-weight blocks."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "forced_channel_weight_blocks_certificate.json"
SEED_CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
CHANNEL_CERT = ROOT.parent / "certificates" / "finite_channel_sets_certificate.json"
Q79_CERT = ROOT.parent / "certificates" / "q79_channel_restriction_certificate.json"
WEIGHT_PROTOCOL_CERT = ROOT.parent / "certificates" / "selected_channel_weight_extraction_protocol_certificate.json"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def source_ids(channel_cert: dict, source_class: str) -> set[str]:
    ids: set[str] = set()
    for channels in channel_cert.get("finite_channel_sets", {}).values():
        for channel in channels:
            if channel.get("source_class") == source_class:
                ids.add(channel.get("id", ""))
    return ids


def matrix_rank_by_nonzero_rows(matrix: list[list[int]]) -> int:
    return sum(1 for row in matrix if any(value != 0 for value in row))


def approx_complex(label: int, modulus: int) -> tuple[float, float]:
    angle = 2.0 * math.pi * label / modulus
    return math.cos(angle), math.sin(angle)


def close_enough(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    cert = load_json(CERT)
    seed_cert = load_json(SEED_CERT)
    channel_cert = load_json(CHANNEL_CERT)
    q79_cert = load_json(Q79_CERT)
    protocol_cert = load_json(WEIGHT_PROTOCOL_CERT)
    paper = read(ROOT / "Forced_C0_C6_Channel_Weight_Blocks_for_Rank_One_Lift_v1.md")

    c0 = cert.get("C0_tree_seed_block", {})
    c6 = cert.get("C6_pure_holonomy_block", {})
    c0_ids = source_ids(channel_cert, "C0_tree_rank_one_seed")
    c6_ids = source_ids(channel_cert, "C6_q79_holonomy_insertion")
    matrix = c0.get("matrix_representative", [])
    rank = matrix_rank_by_nonzero_rows(matrix)

    q79_values = c6.get("character_values", {}).get("79", {})
    q369_values = c6.get("character_values", {}).get("369", {})
    re79, im79 = approx_complex(79, 448)
    re369, im369 = approx_complex(369, 448)
    unit79 = close_enough(re79 * re79 + im79 * im79, 1.0)
    unit369 = close_enough(re369 * re369 + im369 * im369, 1.0)

    gates = [
        Gate(
            "certificate status",
            "PARTIAL-CLOSED" if cert.get("status") == "FORCED_C0_C6_WEIGHT_BLOCKS_PARTIALLY_CLOSED" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "Iwasawa seed input",
            "PASS" if seed_cert.get("tree_level_seed", {}).get("lambda_123_after_rephasing") == 1 else "FAIL",
            "lambda_123=1",
        ),
        Gate(
            "finite channel input",
            "PASS" if c0_ids == set(c0.get("channel_ids", [])) and c6_ids == set(c6.get("channel_ids", [])) else "FAIL",
            f"C0={sorted(c0_ids)}, C6={sorted(c6_ids)}",
        ),
        Gate(
            "q79 restriction input",
            "PASS" if q79_cert.get("restriction_rule", {}).get("C6_q79_holonomy_insertion") == [79, 369] else "FAIL",
            str(q79_cert.get("restriction_rule", {}).get("C6_q79_holonomy_insertion")),
        ),
        Gate(
            "weight protocol input",
            "PASS" if protocol_cert.get("status") == "WEIGHT_EXTRACTION_PROTOCOL_FORMULATED_VALUES_OPEN" else "FAIL",
            str(protocol_cert.get("status")),
        ),
        Gate(
            "C0 forced weight",
            "PASS"
            if c0.get("A_tree_seed") == 1
            and c0.get("S_tree_seed") == 0
            and c0.get("exp_minus_S") == 1
            and c0.get("character_label") == 0
            else "FAIL",
            "A=1, S=0, chi=1",
        ),
        Gate(
            "C0 rank-one representative",
            "PASS" if rank == 1 and c0.get("rank") == 1 else "FAIL",
            f"rank={rank}",
        ),
        Gate(
            "C6 flat action",
            "PASS" if c6.get("S_pure_flat_holonomy") == 0 and c6.get("exp_minus_S") == 1 else "FAIL",
            "S=0 for pure flat holonomy",
        ),
        Gate(
            "C6 character labels",
            "PASS" if c6.get("allowed_character_labels") == [79, 369] else "FAIL",
            str(c6.get("allowed_character_labels")),
        ),
        Gate(
            "C6 character values",
            "PASS"
            if close_enough(q79_values.get("real_approx", 0.0), re79)
            and close_enough(q79_values.get("imag_approx", 0.0), im79)
            and close_enough(q369_values.get("real_approx", 0.0), re369)
            and close_enough(q369_values.get("imag_approx", 0.0), im369)
            else "FAIL",
            "computed exp(2*pi*i*k/448)",
        ),
        Gate(
            "unit modulus",
            "PASS" if c6.get("unit_modulus") is True and unit79 and unit369 else "FAIL",
            "|chi_79|=|chi_369|=1",
        ),
        Gate(
            "full weights remain open",
            "OPEN"
            if cert.get("open", {}).get("C1_C2_C3_C4_C7_A_gamma") is True
            and cert.get("open", {}).get("C6_A_gamma") is True
            else "FAIL",
            "partial forced-value closure only",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "Forced C0/C6 Weight-Block Theorem" in paper else "FAIL",
            "forced block theorem is written",
        ),
    ]

    print("Forced C0/C6 channel-weight blocks audit")
    print("========================================")
    print()
    print(f"C0_channel_count={len(c0_ids)}")
    print(f"C6_channel_count={len(c6_ids)}")
    print(f"chi_79=({re79:.16f},{im79:.16f})")
    print(f"chi_369=({re369:.16f},{im369:.16f})")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
