"""Audit the q79 character restriction on finite rank-one lift channels."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "q79_channel_restriction_certificate.json"
THETA_CERT = ROOT.parent / "certificates" / "theta_flavor_kernel_skeleton_certificate.json"
CHANNEL_CERT = ROOT.parent / "certificates" / "finite_channel_sets_certificate.json"

EXPECTED_SETS = {"Gamma_u", "Gamma_d", "Gamma_e", "Gamma_nuD"}
ALLOWED_LABELS = {0, 79, 369}


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    cert = load_json(CERT)
    theta_cert = load_json(THETA_CERT)
    channel_cert = load_json(CHANNEL_CERT)
    paper = read(ROOT / "Q79_Channel_Restriction_for_Finite_Rank_One_Lift_Channels_v1.md")

    q = theta_cert.get("cp_character", {}).get("q_mod_448")
    modulus = cert.get("selected_character", {}).get("modulus")
    inverse = cert.get("selected_character", {}).get("inverse_label")
    restrictions = cert.get("channel_restrictions", {})

    channel_sets = channel_cert.get("finite_channel_sets", {})
    flat_channels = {
        channel["id"]: channel
        for channels in channel_sets.values()
        for channel in channels
    }
    flat_restrictions = {
        channel_id: restriction
        for restrictions_for_set in restrictions.values()
        for channel_id, restriction in restrictions_for_set.items()
    }

    c6_ids = {channel_id for channel_id, channel in flat_channels.items() if channel.get("source_class") == "C6_q79_holonomy_insertion"}
    non_c6_ids = set(flat_channels) - c6_ids
    c6_ok = all(flat_restrictions.get(channel_id, {}).get("allowed_labels") == [79, 369] for channel_id in c6_ids)
    non_c6_ok = all(flat_restrictions.get(channel_id, {}).get("allowed_labels") == [0] for channel_id in non_c6_ids)
    all_labels = {
        label
        for restriction in flat_restrictions.values()
        for label in restriction.get("allowed_labels", [])
    }

    gates = [
        Gate(
            "Theta q source",
            "CLOSED" if q == 79 else "FAIL",
            f"q={q}",
        ),
        Gate(
            "Finite channel input",
            "FORMULATED" if channel_cert.get("status") == "FINITE_CHANNEL_SETS_FORMULATED_WEIGHTS_OPEN" else "FAIL",
            str(channel_cert.get("status")),
        ),
        Gate(
            "Certificate status",
            "FORMULATED" if cert.get("status") == "Q79_CHANNEL_RESTRICTION_FORMULATED_WEIGHTS_OPEN" else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "Conjugate label",
            "PASS" if modulus == 448 and inverse == 369 and (q + inverse) % modulus == 0 else "FAIL",
            f"q={q}, inverse={inverse}, modulus={modulus}",
        ),
        Gate(
            "Restriction set names",
            "PASS" if set(restrictions) == EXPECTED_SETS else "FAIL",
            ", ".join(sorted(restrictions)),
        ),
        Gate(
            "All channels covered",
            "PASS" if set(flat_restrictions) == set(flat_channels) else "FAIL",
            f"covered={len(flat_restrictions)}, expected={len(flat_channels)}",
        ),
        Gate(
            "C6 q79/conjugate only",
            "PASS" if c6_ok and len(c6_ids) == 4 else "FAIL",
            f"C6 ids={sorted(c6_ids)}",
        ),
        Gate(
            "Non-C6 trivial only",
            "PASS" if non_c6_ok and len(non_c6_ids) == 24 else "FAIL",
            f"non-C6 count={len(non_c6_ids)}",
        ),
        Gate(
            "No other labels",
            "PASS" if all_labels <= ALLOWED_LABELS else "FAIL",
            str(sorted(all_labels)),
        ),
        Gate(
            "Weights remain open",
            "OPEN" if cert.get("open", {}).get("channel_weights") is True else "FAIL",
            "restriction is support-level only",
        ),
        Gate(
            "Paper records theorem",
            "PASS" if "allowed_label" in paper and "{79,369}" in paper and "{0}" in paper else "FAIL",
            "q79 restriction theorem is written",
        ),
    ]

    print("q79 channel restriction audit")
    print("=============================")
    print()
    print(f"q={q}")
    print(f"inverse_label={inverse}")
    print(f"cp_active_channel_count={len(c6_ids)}")
    print(f"trivial_channel_count={len(non_c6_ids)}")
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

