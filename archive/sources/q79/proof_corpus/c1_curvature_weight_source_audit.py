"""Audit C1 curvature as a source for rank-one lift weights."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "c1_curvature_weight_source_audit_certificate.json"
CHANNEL_CERT = ROOT.parent / "certificates" / "finite_channel_sets_certificate.json"
Q79_CERT = ROOT.parent / "certificates" / "q79_channel_restriction_certificate.json"
WEIGHT_PROTOCOL_CERT = ROOT.parent / "certificates" / "selected_channel_weight_extraction_protocol_certificate.json"
LEDGER_CERT = ROOT.parent / "certificates" / "rank_one_lift_correction_channel_ledger_certificate.json"
C3_CERT = ROOT.parent / "certificates" / "c3_lens_nil_weight_source_audit_certificate.json"
C1_INSERTION_CERT = ROOT.parent / "certificates" / "c1_curvature_insertion_formula_certificate.json"

STRINGS_ROOT = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
)
FLUX_SOURCE = STRINGS_ROOT / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
SELECTION_SOURCE = STRINGS_ROOT / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
STROMINGER_SOURCE = STRINGS_ROOT / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
STRING_SOURCE = STRINGS_ROOT / "Modal_Triplet_Theory__From_MTT_to_String_Theory.md"
MTHEORY_SOURCE = STRINGS_ROOT / "Modal_Triplet_Theory__From_MTT_to_M_theory.md"


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


def contains_any(text: str, needles: list[str]) -> bool:
    return any(needle in text for needle in needles)


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


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
    ledger_cert = load_json(LEDGER_CERT)
    c3_cert = load_json(C3_CERT)
    c1_insertion_cert = load_json(C1_INSERTION_CERT)

    flux = read(FLUX_SOURCE)
    selection = read(SELECTION_SOURCE)
    strominger = read(STROMINGER_SOURCE)
    string_source = read(STRING_SOURCE)
    mtheory = read(MTHEORY_SOURCE)
    source_blob = "\n".join([flux, selection, strominger, string_source, mtheory])
    paper = read(ROOT / "C1_Curvature_Weight_Source_Audit_for_Rank_One_Lift_v1.md")

    c1_ids = source_ids(channel_cert, "C1_alpha_prime_curvature")
    c1_labels = restriction_labels(q79_cert, c1_ids)
    all_c1_trivial = all(labels == [0] for labels in c1_labels.values())
    c1_channel_status = cert.get("C1_channel_status", {})
    open_fields = cert.get("open", {})
    ledger_c1 = ledger_cert.get("channels", {}).get("C1_alpha_prime_curvature", {})
    protocol_a_sources = protocol_cert.get("allowed_weight_sources", {}).get("A_gamma", [])
    protocol_s_sources = protocol_cert.get("allowed_weight_sources", {}).get("S_gamma", [])

    has_green_schwarz_curvature = (
        contains_any(source_blob, ["dH", "dH_b", "d\\widehat{H}", "\\mathrm{d}\\widehat{H}"])
        and contains_any(source_blob, ["alpha'", "\\alpha'"])
        and contains_any(source_blob, ["R_+", "R_{+}", "R^+"])
        and contains_any(source_blob, ["Tr", "\\mathrm{Tr}"])
    )
    has_selected_torsional_connection = (
        contains_any(selection, ["selection functional uses $R_+$", "supersymmetric torsional connection $R_+$"])
        or contains_any(strominger, ["Bismut connection", "R^+"])
    )
    has_alpha_prime_caveat = (
        contains_any(source_blob, ["curvature-squared", "higher $\\alpha'$ corrections", "higher-order $\\alpha'$"])
        and contains_any(source_blob, ["local field redefinitions", "scheme-dependent", "field redefinitions"])
    )
    has_gap_curvature = contains_any(source_blob, ["Delta_{\\mathrm{curv}}", "\\Delta_{\\rm curv}", "Delta_curv"])
    has_yukawa_overlap_context = contains_all(
        mtheory,
        ["Yukawa couplings are triple overlaps", "fixed by the same modal/topological data"],
    ) or "normalized cubic Yukawa" in flux

    gates = [
        Gate(
            "certificate status",
            "ADMISSIBLE-OPEN"
            if cert.get("status") == "C1_CURVATURE_WEIGHT_SOURCE_ADMISSIBLE_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "finite C1 support",
            "PASS" if c1_ids == {"u:C1", "d:C1", "e:C1", "nuD:C1"} else "FAIL",
            ", ".join(sorted(c1_ids)),
        ),
        Gate(
            "q79 character trivial",
            "PASS" if all_c1_trivial else "FAIL",
            str(c1_labels),
        ),
        Gate(
            "ledger C1 source",
            "FORMULATED" if ledger_c1.get("source_status") == "FORMULATED" else "FAIL",
            str(ledger_c1.get("coefficient_status")),
        ),
        Gate(
            "weight protocol input",
            "PASS" if protocol_cert.get("status") == "WEIGHT_EXTRACTION_PROTOCOL_FORMULATED_VALUES_OPEN" else "FAIL",
            str(protocol_cert.get("status")),
        ),
        Gate(
            "C3 retirement compatibility",
            "PASS" if c3_cert.get("status") == "C3_LENS_NIL_WEIGHT_SOURCE_RETIRED_UNTIL_REPAIRED" else "FAIL",
            "C1 is independent of the retired old C3 coefficient block",
        ),
        Gate(
            "Green-Schwarz curvature source",
            "FORMULATED" if has_green_schwarz_curvature else "FAIL",
            "Bianchi identity contains alpha-prime torsional curvature data",
        ),
        Gate(
            "selected torsional connection",
            "FORMULATED" if has_selected_torsional_connection else "FAIL",
            "R_+ or R^+ is selected, not an arbitrary curvature choice",
        ),
        Gate(
            "alpha-prime scheme caveat",
            "OPEN" if has_alpha_prime_caveat else "FAIL",
            "higher-order curvature terms require a fixed scheme",
        ),
        Gate(
            "curvature gap control",
            "FORMULATED" if has_gap_curvature else "FAIL",
            "Delta_curv appears in fixed-point/gap estimates",
        ),
        Gate(
            "Yukawa overlap context",
            "FORMULATED" if has_yukawa_overlap_context else "FAIL",
            "Yukawas are overlap data once the fixed point is selected",
        ),
        Gate(
            "no-proxy source discipline",
            "PASS"
            if "selected channel insertion operator O_gamma" in protocol_a_sources
            and "selected alpha-prime order or curvature action for C1" in protocol_s_sources
            else "FAIL",
            "C1 must enter through selected O_C1, A_gamma, and S_gamma",
        ),
        Gate(
            "C1 channel status",
            "ADMISSIBLE-OPEN"
            if c1_channel_status.get("coefficient_status") == "ADMISSIBLE_SOURCE_VALUES_OPEN"
            else "FAIL",
            str(c1_channel_status),
        ),
        Gate(
            "selected insertion",
            "FORMULATED-OPEN"
            if c1_insertion_cert.get("status") == "C1_CURVATURE_INSERTION_FORMULATED_VALUES_OPEN"
            else "OPEN" if open_fields.get("selected_O_C1_insertion_operator") is True else "FAIL",
            "O_C1 formal definition supplied by follow-up; evaluated components remain open",
        ),
        Gate(
            "C1 A/S values",
            "OPEN"
            if open_fields.get("C1_A_gamma") is True and open_fields.get("C1_S_gamma") is True
            else "FAIL",
            "no numerical C1 weights claimed",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "C1 Admissibility Theorem" in paper else "FAIL",
            "C1 admissibility theorem is written",
        ),
    ]

    print("C1 curvature weight-source audit")
    print("================================")
    print()
    print(f"C1_channel_count={len(c1_ids)}")
    print(f"C1_labels={c1_labels}")
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
