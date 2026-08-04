"""Audit the formal C1 curvature insertion formula."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "c1_curvature_insertion_formula_certificate.json"
C1_SOURCE_CERT = ROOT.parent / "certificates" / "c1_curvature_weight_source_audit_certificate.json"
WEIGHT_PROTOCOL_CERT = ROOT.parent / "certificates" / "selected_channel_weight_extraction_protocol_certificate.json"
SEED_CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
CHANNEL_CERT = ROOT.parent / "certificates" / "finite_channel_sets_certificate.json"
Q79_CERT = ROOT.parent / "certificates" / "q79_channel_restriction_certificate.json"

STRINGS_ROOT = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
)
FLUX_SOURCE = STRINGS_ROOT / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
SELECTION_SOURCE = STRINGS_ROOT / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
STROMINGER_SOURCE = STRINGS_ROOT / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
CY_SOURCE = STRINGS_ROOT / "Modal_Triplet_Theory__From_MTT_to_Calabi__Yau_Compactifications.md"
QFT_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\7 Quantum Field Theory"
    r"\Modal_Triplet_Theory__Quantum_Amplitudes_from_Modal_Geometry_v2.md"
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


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def contains_any(text: str, needles: list[str]) -> bool:
    return any(needle in text for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    c1_source_cert = load_json(C1_SOURCE_CERT)
    protocol_cert = load_json(WEIGHT_PROTOCOL_CERT)
    seed_cert = load_json(SEED_CERT)
    channel_cert = load_json(CHANNEL_CERT)
    q79_cert = load_json(Q79_CERT)

    flux = read(FLUX_SOURCE)
    selection = read(SELECTION_SOURCE)
    strominger = read(STROMINGER_SOURCE)
    cy = read(CY_SOURCE)
    qft = read(QFT_SOURCE)
    paper = read(ROOT / "C1_Curvature_Insertion_Formula_for_Rank_One_Lift_v1.md")

    scheme = cert.get("selected_scheme", {})
    operator = cert.get("linear_response_operator", {})
    separation = cert.get("separation_rule", {})
    closed = cert.get("closed", {})
    open_fields = cert.get("open", {})

    c1_ids = {
        channel.get("id")
        for channels in channel_cert.get("finite_channel_sets", {}).values()
        for channel in channels
        if channel.get("source_class") == "C1_alpha_prime_curvature"
    }
    q79_flat = {}
    for restrictions in q79_cert.get("channel_restrictions", {}).values():
        q79_flat.update(restrictions)
    c1_labels = {channel_id: q79_flat.get(channel_id, {}).get("allowed_labels") for channel_id in sorted(c1_ids)}

    has_rplus_scheme = contains_any(
        "\n".join([flux, selection, strominger]),
        ["R_+", "R^+", "omega^+", "omega_+"],
    ) and contains_any(
        "\n".join([flux, selection, strominger]),
        ["Bismut", "torsional", "torsionful"],
    )
    has_hhat = contains_all(strominger, ["\\widehat{H}", "omega^+", "R^+"])
    has_positive_hessian = contains_all(strominger, ["Positive Hessian", "strictly convex", "bounded projector"])
    has_resolvent_projector = contains_any(
        "\n".join([strominger, cy]),
        ["resolvent", "Riesz", "Green operator"],
    ) and contains_any(
        "\n".join([strominger, cy]),
        ["projector", "P_H", "Pi"],
    )
    has_iwasawa_yukawa = contains_all(flux, ["three orthonormal harmonic representatives", "Yukawa", "rank one"])
    has_cy_overlap = contains_all(cy, ["Yukawa couplings", "harmonic reps"])
    has_qft_normalization = contains_all(qft, ["canonical normalization", "overlap"])

    protocol_a = protocol_cert.get("allowed_weight_sources", {}).get("A_gamma", [])
    protocol_s = protocol_cert.get("allowed_weight_sources", {}).get("S_gamma", [])

    gates = [
        Gate(
            "certificate status",
            "FORMULATED-OPEN"
            if cert.get("status") == "C1_CURVATURE_INSERTION_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "C1 source input",
            "ADMISSIBLE-OPEN"
            if c1_source_cert.get("status") == "C1_CURVATURE_WEIGHT_SOURCE_ADMISSIBLE_VALUES_OPEN"
            else "FAIL",
            str(c1_source_cert.get("status")),
        ),
        Gate(
            "weight protocol input",
            "PASS" if protocol_cert.get("status") == "WEIGHT_EXTRACTION_PROTOCOL_FORMULATED_VALUES_OPEN" else "FAIL",
            str(protocol_cert.get("status")),
        ),
        Gate(
            "rank-one seed input",
            "PASS" if seed_cert.get("tree_level_seed", {}).get("rank") == 1 else "FAIL",
            "Iwasawa tree Yukawa seed available",
        ),
        Gate(
            "finite C1 support",
            "PASS" if c1_ids == {"u:C1", "d:C1", "e:C1", "nuD:C1"} else "FAIL",
            ", ".join(sorted(c1_ids)),
        ),
        Gate(
            "C1 trivial character",
            "PASS" if all(labels == [0] for labels in c1_labels.values()) else "FAIL",
            str(c1_labels),
        ),
        Gate(
            "R_plus scheme source",
            "PASS" if has_rplus_scheme and scheme.get("connection", "").startswith("R_plus") else "FAIL",
            "torsional R_+ connection selected",
        ),
        Gate(
            "Green-Schwarz Hhat",
            "PASS" if has_hhat and "Hhat" in scheme.get("green_schwarz_field", "") else "FAIL",
            "gauge-invariant Hhat source present",
        ),
        Gate(
            "positive Hessian response",
            "FORMULATED" if has_positive_hessian and "Hess_Xi" in operator.get("selected_deformation_equation", "") else "FAIL",
            "linearized deformation is a Hessian-response problem",
        ),
        Gate(
            "projector derivative",
            "FORMULATED" if has_resolvent_projector and "dotP_a" in operator.get("projector_derivative", "") else "FAIL",
            "Riesz/resolvent formula gives zero-mode response",
        ),
        Gate(
            "Yukawa overlap source",
            "PASS" if has_iwasawa_yukawa and has_cy_overlap else "FAIL",
            "tree seed and general overlap formula are present",
        ),
        Gate(
            "protocol O_gamma hook",
            "PASS"
            if "selected channel insertion operator O_gamma" in protocol_a
            and "selected alpha-prime order or curvature action for C1" in protocol_s
            else "FAIL",
            "C1 is tied to selected insertion and curvature action",
        ),
        Gate(
            "kinetic separation",
            "PASS"
            if closed.get("kinetic_separation_rule") is True
            and "C5" in separation.get("kinetic_metric_effect", "")
            and has_qft_normalization
            else "FAIL",
            "pure L2-metric effects stay in C5 canonical normalization",
        ),
        Gate(
            "O_C1 definition",
            "FORMULATED"
            if closed.get("O_C1_formal_definition") is True
            and "O_C1[Y_s]" in operator.get("C1_insertion_definition", "")
            else "FAIL",
            "formal insertion is a first derivative of the raw overlap",
        ),
        Gate(
            "values remain open",
            "OPEN"
            if open_fields.get("explicit_V_C1_functional") is True
            and open_fields.get("C1_A_gamma_values") is True
            and open_fields.get("C1_S_gamma_values") is True
            else "FAIL",
            "no numerical C1 coefficient claimed",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "C1 Linear-Response Insertion Theorem" in paper else "FAIL",
            "linear-response theorem is written",
        ),
    ]

    print("C1 curvature insertion formula audit")
    print("====================================")
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
