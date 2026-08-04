"""Audit the selected channel-weight extraction protocol."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "selected_channel_weight_extraction_protocol_certificate.json"
THETA_CERT = ROOT.parent / "certificates" / "theta_flavor_kernel_skeleton_certificate.json"
SEED_CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
LEDGER_CERT = ROOT.parent / "certificates" / "rank_one_lift_correction_channel_ledger_certificate.json"
CHANNEL_CERT = ROOT.parent / "certificates" / "finite_channel_sets_certificate.json"
Q79_CERT = ROOT.parent / "certificates" / "q79_channel_restriction_certificate.json"


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


def channel_ids(channel_cert: dict) -> set[str]:
    ids: set[str] = set()
    for channels in channel_cert.get("finite_channel_sets", {}).values():
        ids.update(channel.get("id", "") for channel in channels)
    return ids


def restriction_ids(q79_cert: dict) -> set[str]:
    ids: set[str] = set()
    for restrictions in q79_cert.get("channel_restrictions", {}).values():
        ids.update(restrictions.keys())
    return ids


def main() -> None:
    cert = load_json(CERT)
    theta_cert = load_json(THETA_CERT)
    seed_cert = load_json(SEED_CERT)
    ledger_cert = load_json(LEDGER_CERT)
    channel_cert = load_json(CHANNEL_CERT)
    q79_cert = load_json(Q79_CERT)
    paper = read(ROOT / "Selected_Channel_Weight_Extraction_Protocol_for_Rank_One_Lift_v1.md")

    formula_text = " ".join(cert.get("weight_formula", {}).values())
    forbidden = set(cert.get("forbidden_inputs", []))
    ids = channel_ids(channel_cert)
    q79_ids = restriction_ids(q79_cert)
    c6_labels = cert.get("q79_character_rule", {}).get("C6_q79_holonomy_insertion")
    non_c6_labels = cert.get("q79_character_rule", {}).get("all_other_source_classes")

    gates = [
        Gate(
            "certificate status",
            "FORMULATED" if cert.get("status") == "WEIGHT_EXTRACTION_PROTOCOL_FORMULATED_VALUES_OPEN" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "Theta scaffold input",
            "PASS" if theta_cert.get("status") == "SCAFFOLD_CLOSED_KERNEL_DATA_OPEN" else "FAIL",
            str(theta_cert.get("status")),
        ),
        Gate(
            "Iwasawa seed input",
            "PASS" if seed_cert.get("tree_level_seed", {}).get("lambda_123_after_rephasing") == 1 else "FAIL",
            "lambda_123=1",
        ),
        Gate(
            "correction ledger input",
            "PASS" if ledger_cert.get("status") == "CHANNEL_LEDGER_FORMULATED_COEFFICIENTS_OPEN" else "FAIL",
            str(ledger_cert.get("status")),
        ),
        Gate(
            "finite channel input",
            "PASS" if channel_cert.get("status") == "FINITE_CHANNEL_SETS_FORMULATED_WEIGHTS_OPEN" else "FAIL",
            f"channels={len(ids)}",
        ),
        Gate(
            "q79 restriction input",
            "PASS" if q79_cert.get("status") == "Q79_CHANNEL_RESTRICTION_FORMULATED_WEIGHTS_OPEN" else "FAIL",
            str(q79_cert.get("status")),
        ),
        Gate(
            "all channel ids covered",
            "PASS" if ids == q79_ids and len(ids) == cert.get("fixed_support", {}).get("total_channels") else "FAIL",
            f"finite={len(ids)}, restricted={len(q79_ids)}",
        ),
        Gate(
            "weight formula",
            "PASS" if all(token in formula_text for token in ["A_{s,gamma", "exp(-S", "chi_{s,gamma"]) else "FAIL",
            "A_gamma exp(-S_gamma) chi_gamma",
        ),
        Gate(
            "C0 tree seed protocol",
            "PASS"
            if cert.get("c0_tree_seed_normalization", {}).get("lambda_123") == 1
            and cert.get("c0_tree_seed_normalization", {}).get("action_cost") == 0
            else "FAIL",
            "lambda_123=1, S_C0=0",
        ),
        Gate(
            "q79 character rule",
            "PASS" if c6_labels == [79, 369] and non_c6_labels == [0] else "FAIL",
            f"C6={c6_labels}, non-C6={non_c6_labels}",
        ),
        Gate(
            "forbidden proxy inputs",
            "PASS"
            if {
                "Execution II benchmark matrix entries",
                "observed fermion masses",
                "observed CKM angle magnitudes",
                "observed PMNS angle magnitudes",
            }.issubset(forbidden)
            else "FAIL",
            "benchmark and observed flavor data cannot define weights",
        ),
        Gate(
            "values remain open",
            "OPEN"
            if cert.get("open", {}).get("numerical_A_gamma") is True
            and cert.get("open", {}).get("numerical_S_gamma") is True
            else "FAIL",
            "protocol only; no numerical weights claimed",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "No-Proxy Weight Extraction Theorem" in paper else "FAIL",
            "weight extraction theorem is written",
        ),
    ]

    print("Selected channel-weight extraction protocol audit")
    print("================================================")
    print()
    print(f"channel_count={len(ids)}")
    print(f"c6_labels={c6_labels}")
    print(f"non_c6_labels={non_c6_labels}")
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
