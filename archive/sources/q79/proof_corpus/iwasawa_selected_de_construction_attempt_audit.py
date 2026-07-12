"""Audit the attempt to construct the selected Iwasawa operator D_E."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_selected_de_construction_attempt_certificate.json"
PAPER = ROOT / "Iwasawa_Selected_DE_Construction_Attempt_v1.md"
SPECTRAL = CERT_DIR / "iwasawa_spectral_operator_gate_certificate.json"
RECOVERY = CERT_DIR / "iwasawa_typed_monad_section_recovery_certificate.json"
DOLBEAULT = CERT_DIR / "iwasawa_dolbeault_complex_extraction_certificate.json"
SCAN = CERT_DIR / "corrected_a01_candidate_scan_certificate.json"
DIAGNOSTIC = CERT_DIR / "iwasawa_diagnostic_h1_three_spectral_pipeline_certificate.json"
FLUX = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    spectral = load_json(SPECTRAL)
    recovery = load_json(RECOVERY)
    dolbeault = load_json(DOLBEAULT)
    scan = load_json(SCAN)
    diagnostic = load_json(DIAGNOSTIC)
    paper = read(PAPER)
    flux = read(FLUX)

    routes = cert.get("route_evaluation", {})
    abstract = cert.get("abstract_operator_package", {})
    progress = cert.get("diagnostic_progress", {})
    minimal = cert.get("minimal_new_data_to_close", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    r1 = routes.get("R1_corrected_non_invariant_Dolbeault_operator", {})
    r2 = routes.get("R2_typed_monad_sections", {})
    r3 = routes.get("R3_direct_selected_HYM_solve", {})
    missing = " ".join(abstract.get("missing_for_computation", []))
    one_of = " ".join(minimal.get("one_of", []))

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status")
            == "SELECTED_D_E_CONSTRUCTION_BLOCKED_BY_MISSING_CONNECTION_DATA_DIAGNOSTIC_PIPELINE_READY"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "spectral fallback active",
            "PASS"
            if spectral.get("closed_decisions", {}).get("fallback_is_now_active") is True
            and spectral.get("currently_missing", {}).get("selected_operator_D_E") is True
            else "FAIL",
            str(spectral.get("currently_missing", {})),
        ),
        Gate(
            "R1 blocked by A01 status",
            "PASS"
            if r1.get("status") == "BLOCKED"
            and dolbeault.get("literal_integrability_result", {}).get("integrable") is False
            and scan.get("guardrails", {}).get("claims_example_candidate_is_selected") is False
            else "FAIL",
            str(r1),
        ),
        Gate(
            "R2 blocked by typed sections",
            "PASS"
            if r2.get("status") == "BLOCKED"
            and recovery.get("route_decision", {}).get("typed_monad_cech_can_close_now") is False
            else "FAIL",
            str(r2),
        ),
        Gate(
            "R3 abstract only",
            "PASS"
            if r3.get("status") == "ABSTRACT_EXISTENCE_ONLY"
            and "Hermitian--Yang--Mills" in flux
            and "Li--Yau" in flux
            else "FAIL",
            str(r3),
        ),
        Gate(
            "formal operator recorded",
            "PASS"
            if abstract.get("formal_symbol") == "D_E = barpartial_{A_HYM} + barpartial_{A_HYM}^*"
            and abstract.get("mathematically_admissible_if_selected_HYM_connection_supplied") is True
            and abstract.get("computable_from_current_corpus") is False
            else "FAIL",
            str(abstract),
        ),
        Gate(
            "missing computation data",
            "PASS"
            if contains_all(
                missing,
                [
                    "connection coefficients",
                    "Hermitian metric",
                    "gauge fixing",
                    "basis action",
                    "residual and gap",
                ],
            )
            else "FAIL",
            missing,
        ),
        Gate(
            "diagnostic pipeline imported",
            "PASS"
            if progress.get("unselected_h1_three_pipeline_executed") is True
            and diagnostic.get("what_this_achieves", {}).get(
                "proves_pipeline_can_extract_three_modes_when_valid_D_is_given"
            )
            is True
            and progress.get("extracted_representatives") == diagnostic.get(
                "computed_hodge_pipeline", {}
            ).get("representatives")
            else "FAIL",
            str(progress),
        ),
        Gate(
            "minimal new data",
            "PASS"
            if contains_all(
                one_of,
                [
                    "non-invariant",
                    "typed monad sections",
                    "direct HYM",
                ],
            )
            and "operator matrix L_N" in " ".join(minimal.get("then_compute", []))
            else "FAIL",
            str(minimal),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("promotes_abstract_Li_Yau_existence_to_matrix") is False
            and guardrails.get("uses_diagnostic_candidate_as_selected") is False
            and guardrails.get("claims_selected_H1_E_values") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("selected_D_E_constructed") is False
            and verdict.get("diagnostic_pipeline_ready") is True
            and "selected connection/operator source" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records attempt",
            "PASS"
            if contains_all(
                paper,
                [
                    "Route R1",
                    "Route R2",
                    "Route R3",
                    "abstract existence only",
                    "diagnostic Hodge pipeline works",
                    "selected `D_E` is not yet constructed",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa selected D_E construction attempt audit")
    print("==============================================")
    print()
    print(f"R1={r1.get('status')}")
    print(f"R2={r2.get('status')}")
    print(f"R3={r3.get('status')}")
    print(f"diagnostic_reps={progress.get('extracted_representatives')}")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
