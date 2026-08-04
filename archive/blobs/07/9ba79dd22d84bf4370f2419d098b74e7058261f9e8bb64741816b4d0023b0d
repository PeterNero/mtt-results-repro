"""Audit the non-invariant Galerkin execution protocol."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
PAPER = ROOT / "Iwasawa_NonInvariant_Galerkin_Execution_Protocol_v1.md"
SPECTRAL_GATE = CERT_DIR / "iwasawa_spectral_operator_gate_certificate.json"
REPAIR_OBSTRUCTION = CERT_DIR / "iwasawa_invariant_a01_repair_obstruction_certificate.json"
SELECTED_DE = CERT_DIR / "iwasawa_selected_de_construction_attempt_certificate.json"
TEMPLATE = CERT_DIR / "iwasawa_spectral_galerkin_data.template.json"
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
    spectral_gate = load_json(SPECTRAL_GATE)
    obstruction = load_json(REPAIR_OBSTRUCTION)
    selected_de = load_json(SELECTED_DE)
    template = load_json(TEMPLATE)
    paper = read(PAPER)
    flux = read(FLUX)

    source_gate = cert.get("operator_source_gate", {})
    hilbert = cert.get("hilbert_space", {})
    basis = cert.get("finite_basis_protocol", {})
    matrix = cert.get("matrix_protocol", {})
    gap = cert.get("gap_error_certificate", {})
    outputs = cert.get("outputs_if_pass", {})
    open_values = cert.get("values_still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    accepted = " ".join(source_gate.get("accepted_sources", []))
    rejected = " ".join(source_gate.get("rejected_sources", []))
    domain_text = " ".join(hilbert.get("domain_requirements", []))
    basis_text = " ".join(
        [
            basis.get("nested_spaces", ""),
            " ".join(basis.get("basis_options", [])),
            " ".join(basis.get("must_include", [])),
            " ".join(basis.get("basis_checks", [])),
        ]
    )
    matrix_text = " ".join(str(value) for value in matrix.values())
    gap_text = " ".join(str(value) for value in gap.values())
    outputs_text = " ".join(str(value) for value in outputs.values())

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status")
            == "NONINVARIANT_GALERKIN_EXECUTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if spectral_gate.get("status")
            == "SPECTRAL_FALLBACK_REDUCED_TO_SELECTED_OPERATOR_AND_BASIS_DATA"
            and obstruction.get("status")
            == "INVARIANT_A01_REPAIR_PATH_RETIRED_TYPED_OR_NONINVARIANT_REQUIRED"
            and selected_de.get("status")
            == "SELECTED_D_E_CONSTRUCTION_BLOCKED_BY_MISSING_CONNECTION_DATA_DIAGNOSTIC_PIPELINE_READY"
            and template.get("mode") == "non_invariant_spectral_galerkin"
            else "FAIL",
            "upstream gates imported",
        ),
        Gate(
            "corpus spectral projection support",
            "PASS"
            if contains_all(
                flux,
                [
                    "compact quotient",
                    "coherent spectral band",
                    "orthogonal projector",
                    "spectral projector",
                    "connection Laplacian",
                ],
            )
            else "FAIL",
            str(FLUX),
        ),
        Gate(
            "source gate accepted routes",
            "PASS"
            if contains_all(
                accepted,
                [
                    "typed monad/Cech",
                    "non-invariant A^(0,1)",
                    "HYM/Strominger",
                ],
            )
            and source_gate.get("selected_D_E_supplied_now") is False
            else "FAIL",
            accepted,
        ),
        Gate(
            "source gate rejected shortcuts",
            "PASS"
            if contains_all(
                rejected,
                [
                    "literal printed invariant A01",
                    "small invariant repair",
                    "unselected sparse h1=3",
                    "rank-one Yukawa seed",
                    "observed flavor data",
                ],
            )
            else "FAIL",
            rejected,
        ),
        Gate(
            "Hilbert/operator domain",
            "PASS"
            if "L2(Omega^{0,*}(X,E))" in hilbert.get("space", "")
            and "D_E^* D_E" in hilbert.get("operator", "")
            and contains_all(
                domain_text,
                [
                    "compact Iwasawa lattice",
                    "bundle transition",
                    "Hermitian metric",
                    "gauge fixing",
                ],
            )
            else "FAIL",
            str(hilbert),
        ),
        Gate(
            "finite basis protocol",
            "PASS"
            if contains_all(
                basis_text,
                [
                    "P_N -> I strongly",
                    "deck-equivariant",
                    "finite-element",
                    "left-invariant seed sector",
                    "non-invariant modes",
                    "bundle fiber basis",
                    "Gram matrix G_N is positive definite",
                    "not just the invariant subspace",
                ],
            )
            else "FAIL",
            basis_text,
        ),
        Gate(
            "matrix formulas",
            "PASS"
            if contains_all(
                matrix_text,
                [
                    "G_N[i,j] = <b_i,b_j>",
                    "K_N[i,j] = <D_E b_i, D_E b_j>",
                    "K_N v = lambda G_N v",
                    "P_fam,N",
                    "G_red,N",
                ],
            )
            else "FAIL",
            matrix_text,
        ),
        Gate(
            "gap/error pass rule",
            "PASS"
            if contains_all(
                gap_text,
                [
                    "lambda_1 <= lambda_2 <= lambda_3",
                    "lambda_4 >= gamma_gap",
                    "eta_total",
                    "epsilon_low + eta_total < tau < gamma_gap - eta_total",
                    "rank three",
                ],
            )
            else "FAIL",
            gap_text,
        ),
        Gate(
            "outputs feed downstream",
            "PASS"
            if outputs.get("kernel_dimension") == 3
            and contains_all(
                outputs_text,
                [
                    "Psi",
                    "anti-family",
                    "Q,u,d,L,e,N,H",
                    "dotD_alpha1",
                    "E6 cubic",
                    "selected_c1_primitive_contractions",
                ],
            )
            else "FAIL",
            outputs_text,
        ),
        Gate(
            "values still open",
            "OPEN"
            if all(open_values.values())
            and set(open_values)
            == {
                "selected_D_E",
                "basis_B_N",
                "G_N",
                "K_N",
                "eigenpairs",
                "eta_total",
                "Psi_i",
                "sector_maps",
                "dotD_alpha1",
            }
            else "FAIL",
            str(open_values),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_kernel_dimension_three_now") is False
            and guardrails.get("uses_observed_masses_or_mixings") is False
            and guardrails.get("uses_invariant_A01_repair") is False
            and guardrails.get("uses_diagnostic_candidate_as_selected") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("closes_execution_protocol") is True
            and verdict.get("closes_numerical_or_symbolic_values") is False
            and "selected D_E" in verdict.get("next_step", "")
            and "V_N" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records protocol",
            "PASS"
            if contains_all(
                paper,
                [
                    "Operator Source Gate",
                    "Finite Basis",
                    "K_N v = lambda G_N v",
                    "epsilon_low + eta_total < tau < gamma_gap - eta_total",
                    "certified errors",
                    "fill this protocol with one selected D_E source",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa non-invariant Galerkin execution protocol audit")
    print("======================================================")
    print()
    print(f"accepted_sources={len(source_gate.get('accepted_sources', []))}")
    print(f"rejected_sources={len(source_gate.get('rejected_sources', []))}")
    print(f"open_value_count={len(open_values)}")
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
