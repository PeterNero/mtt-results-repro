"""Audit source status for selected stack determinant inputs."""

from __future__ import annotations

import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_stack_determinant_source_status_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Stack_Determinant_Source_Status_v1.md"

PROTO = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\10 ProtoSpinor"
    r"\Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3.md"
)
FINITE_ALG = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\10 ProtoSpinor"
    r"\Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md"
)
HET = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def report(name: str, ok: bool, detail: object = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    proto = read(PROTO)
    finite_alg = read(FINITE_ALG)
    het = read(HET)
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "SELECTED_STACK_DETERMINANT_SOURCE_STATUS_CERTIFIED_VALUES_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "ProtoSpinor source has three-stack embedding",
            contains_all(proto, ["U(3)_a", "U(2)_b", "U(1)_c", "Y=\\frac{1}{6}Q_a-\\frac{1}{2}Q_c"]),
            PROTO,
        )
    )
    failures.append(
        not report(
            "finite algebra source fixes quantum numbers not couplings",
            contains_all(
                finite_alg,
                [
                    "A_F=\\mathbb{C}\\oplus\\mathbb{H}\\oplus M_3(\\mathbb{C})",
                    "hypercharge assignments",
                    "It does not compute coupling values",
                ],
            ),
            FINITE_ALG,
        )
    )
    failures.append(
        not report(
            "heterotic source leaves thresholds uncomputed",
            contains_all(
                het,
                [
                    "These two scalar equations fix the ratio $R_1/R$",
                    "f=S",
                    "one-loop thresholds, which we do not attempt to compute here",
                ],
            ),
            HET,
        )
    )
    failures.append(
        not report(
            "certificate separates structure from determinant values",
            cert["verdict"]["hypercharge_structure_source_certified"] is True
            and cert["verdict"]["stack_determinant_values_source_certified"] is False,
            cert["verdict"],
        )
    )
    failures.append(
        not report(
            "note names next determinant artifact",
            "Selected_Qa_Qc_SU2_Stack_Determinants_v1" in note
            and "not source-certified" in note,
            NOTE,
        )
    )
    failures.append(
        not report(
            "numeric closure not claimed",
            cert["verdict"]["numeric_electroweak_closure"] is False,
            cert["verdict"],
        )
    )

    print("\nSelected stack determinant source status audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
