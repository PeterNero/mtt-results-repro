"""Audit C3 Lens-Nil as a source for rank-one lift weights."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "c3_lens_nil_weight_source_audit_certificate.json"
CHANNEL_CERT = ROOT.parent / "certificates" / "finite_channel_sets_certificate.json"
Q79_CERT = ROOT.parent / "certificates" / "q79_channel_restriction_certificate.json"
WEIGHT_PROTOCOL_CERT = ROOT.parent / "certificates" / "selected_channel_weight_extraction_protocol_certificate.json"
FORCED_BLOCK_CERT = ROOT.parent / "certificates" / "forced_channel_weight_blocks_certificate.json"
STATUS_PAPER = ROOT / "Status_Evaluation_MTT_SM_Closure_vs_QM_QFT_String_v1.md"
STRINGS_LEDGER = ROOT / "Strings_Flux_MTheory_Corpus_Clue_Ledger_for_Z7_CP_v1.md"
FLUX_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)
SELECTION_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
)


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


def restriction_labels(q79_cert: dict, channel_ids: set[str]) -> dict[str, list[int]]:
    flat = {}
    for restrictions in q79_cert.get("channel_restrictions", {}).values():
        flat.update(restrictions)
    return {
        channel_id: flat.get(channel_id, {}).get("allowed_labels", [])
        for channel_id in sorted(channel_ids)
    }


def main() -> None:
    cert = load_json(CERT)
    channel_cert = load_json(CHANNEL_CERT)
    q79_cert = load_json(Q79_CERT)
    protocol_cert = load_json(WEIGHT_PROTOCOL_CERT)
    forced_cert = load_json(FORCED_BLOCK_CERT)
    status_paper = read(STATUS_PAPER)
    strings_ledger = read(STRINGS_LEDGER)
    flux_source = read(FLUX_SOURCE)
    selection_source = read(SELECTION_SOURCE)
    paper = read(ROOT / "C3_Lens_Nil_Weight_Source_Audit_for_Rank_One_Lift_v1.md")

    c3_ids = source_ids(channel_cert, "C3_flux_quantized_lens_nil")
    c3_labels = restriction_labels(q79_cert, c3_ids)
    all_c3_trivial = all(labels == [0] for labels in c3_labels.values())
    blocking = cert.get("blocking_findings", {})

    gates = [
        Gate(
            "certificate status",
            "RETIRED-BLOCKED"
            if cert.get("status") == "C3_LENS_NIL_WEIGHT_SOURCE_RETIRED_UNTIL_REPAIRED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "finite C3 support",
            "PASS" if c3_ids == {"u:C3", "d:C3", "e:C3", "nuD:C3"} else "FAIL",
            ", ".join(sorted(c3_ids)),
        ),
        Gate(
            "q79 character trivial",
            "PASS" if all_c3_trivial else "FAIL",
            str(c3_labels),
        ),
        Gate(
            "weight protocol input",
            "PASS" if protocol_cert.get("status") == "WEIGHT_EXTRACTION_PROTOCOL_FORMULATED_VALUES_OPEN" else "FAIL",
            str(protocol_cert.get("status")),
        ),
        Gate(
            "forced blocks input",
            "PASS" if forced_cert.get("status") == "FORCED_C0_C6_WEIGHT_BLOCKS_PARTIALLY_CLOSED" else "FAIL",
            str(forced_cert.get("status")),
        ),
        Gate(
            "integer flux clue",
            "FORMULATED"
            if "(f,h)" in flux_source and "f,h\\in\\mathbb{Z}" in flux_source
            or "(f,h)" in selection_source and "Z}^2" in selection_source
            else "FAIL",
            "Lens-Nil source contains integer flux labels",
        ),
        Gate(
            "ratio-fixing clue",
            "FORMULATED"
            if "fix the *ratio* $R_1/R$" in flux_source or "fix the ratio $R_1/R$" in selection_source
            else "FAIL",
            "componentwise equations were intended to fix R1/R",
        ),
        Gate(
            "nonclosed beta defect",
            "RETIRED"
            if "d beta_1 != 0" in status_paper
            and "d beta_3 != 0" in status_paper
            and "non-closed component forms" in strings_ledger
            else "FAIL",
            ", ".join(blocking.get("nonclosed_component_forms", [])),
        ),
        Gate(
            "flux-square defect",
            "RETIRED"
            if "F=f eta12+h sigma45 gives F^2=2fh beta_2" in status_paper
            else "FAIL",
            str(blocking.get("abelian_flux_square_mismatch")),
        ),
        Gate(
            "old Lens-Nil coefficient source",
            "RETIRED"
            if "Retire the old Lens-Nil coefficient block" in strings_ledger
            and "retired as a proof source in its old form" in status_paper
            else "FAIL",
            "old coefficient block cannot be reused as a proof source",
        ),
        Gate(
            "C3 A/S remain open",
            "OPEN"
            if cert.get("open", {}).get("C3_A_gamma") is True
            and cert.get("open", {}).get("C3_S_gamma") is True
            else "FAIL",
            "no numerical C3 weights claimed",
        ),
        Gate(
            "repair obligations",
            "PASS" if len(cert.get("required_repair_before_use", [])) >= 5 else "FAIL",
            f"{len(cert.get('required_repair_before_use', []))} obligations",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "C3 Retirement Theorem" in paper else "FAIL",
            "C3 retirement theorem is written",
        ),
    ]

    print("C3 Lens-Nil weight-source audit")
    print("===============================")
    print()
    print(f"C3_channel_count={len(c3_ids)}")
    print(f"C3_labels={c3_labels}")
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
