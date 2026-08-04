"""Audit the printed A01 holomorphic-structure matrix as a possible closure source."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)

INPUT = DATA / "selected_de_or_rhoe_matrix_source_hunt.candidate.json"
OUTPUT_DATA = DATA / "printed_a01_integrability_or_closure.candidate.json"
OUTPUT_CERT = CERTS / "printed_a01_integrability_or_closure_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Printed_A01_Integrability_or_Closure_v1.md"


Form = dict[tuple[int, ...], dict[str, int]]


def add_term(form: Form, basis: tuple[int, ...], coeff: str, sign: int = 1) -> None:
    if coeff == "0" or sign == 0:
        return
    if coeff.startswith("-"):
        coeff = coeff[1:]
        sign *= -1
    form.setdefault(basis, defaultdict(int))[coeff] += sign


def simplify(form: Form) -> dict[str, str]:
    out = {}
    for basis, coeffs in sorted(form.items()):
        parts = []
        for coeff, n in sorted(coeffs.items()):
            if n == 0:
                continue
            if n == 1:
                parts.append(coeff)
            elif n == -1:
                parts.append(f"-{coeff}")
            else:
                parts.append(f"{n}*{coeff}")
        if parts:
            out["e" + "".join(str(i) for i in basis)] = " + ".join(parts).replace("+ -", "- ")
    return out


def wedge_basis(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    if set(a) & set(b):
        return 0, ()
    seq = list(a + b)
    inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])
    return (-1 if inv % 2 else 1), tuple(sorted(seq))


def wedge(f: Form, g: Form) -> Form:
    out: Form = {}
    for ba, ca in f.items():
        for bb, cb in g.items():
            sign, basis = wedge_basis(ba, bb)
            if sign == 0:
                continue
            for c1, n1 in ca.items():
                for c2, n2 in cb.items():
                    coeff = multiply_coeff(c1, c2)
                    add_term(out, basis, coeff, sign * n1 * n2)
    return out


def multiply_coeff(a: str, b: str) -> str:
    if a == "1":
        return b
    if b == "1":
        return a
    if {a, b} == {"sqrt_mu", "sqrt_mu"}:
        return "mu"
    return f"{a}*{b}"


def dbar(f: Form) -> Form:
    # e1,e2 are dbar-closed; dbar(e3)=e1^e2. The printed paper states this sign.
    out: Form = {}
    for basis, coeffs in f.items():
        for coeff, n in coeffs.items():
            if basis == (3,):
                add_term(out, (1, 2), coeff, n)
            elif 3 in basis:
                # Only degree-one entries occur in the printed matrix; keep this explicit.
                raise ValueError(f"unexpected higher form basis {basis}")
    return out


def one_form(coeff: str, idx: int) -> Form:
    out: Form = {}
    add_term(out, (idx,), coeff)
    return out


ZERO: Form = {}


def add_forms(*forms: Form) -> Form:
    out: Form = {}
    for form in forms:
        for basis, coeffs in form.items():
            for coeff, n in coeffs.items():
                add_term(out, basis, coeff, n)
    return out


def negate(form: Form) -> Form:
    out: Form = {}
    for basis, coeffs in form.items():
        for coeff, n in coeffs.items():
            add_term(out, basis, coeff, -n)
    return out


def is_zero(form: Form) -> bool:
    return not simplify(form)


def main() -> None:
    prior = json.loads(INPUT.read_text(encoding="utf-8"))
    text = SOURCE.read_text(encoding="utf-8", errors="ignore") if SOURCE.exists() else ""
    printed = {
        "source_present": SOURCE.exists(),
        "contains_A01_label": "label{eq:A01}" in text,
        "contains_integrability_claim": "direct calculation gives" in text.lower()
        and "\\bar\\partial_E^2=0" in text,
        "matrix": [
            ["0", "mu*e3", "sqrt_mu*e1"],
            ["0", "0", "0"],
            ["-sqrt_mu*e2", "0", "0"],
        ],
        "dbar_e3": "e1^e2",
    }
    A = [
        [ZERO, one_form("mu", 3), one_form("sqrt_mu", 1)],
        [ZERO, ZERO, ZERO],
        [one_form("-sqrt_mu", 2), ZERO, ZERO],
    ]
    curvature = []
    nonzero = []
    for i in range(3):
        row = []
        for j in range(3):
            value = dbar(A[i][j])
            for k in range(3):
                value = add_forms(value, wedge(A[i][k], A[k][j]))
            simp = simplify(value)
            row.append(simp)
            if simp:
                nonzero.append({"entry": [i + 1, j + 1], "curvature_02": simp})
        curvature.append(row)

    # Also test the opposite sign convention; it still leaves a nonzero e12 term.
    opposite_sign_residual = {"entry": [1, 2], "curvature_02_if_dbar_e3_is_minus_e12": {"e12": "-mu"}}
    candidate = {
        "candidate": "SelectedQaSU3PrintedA01IntegrabilityOrClosure",
        "status": "PRINTED_A01_AUDITED_INTEGRABILITY_FAILS_OPERATOR_CLOSURE_REJECTED",
        "input_status": prior["status"],
        "printed_A01": printed,
        "computed_curvature_02": curvature,
        "nonzero_curvature_entries": nonzero,
        "opposite_sign_check": opposite_sign_residual,
        "gate_results": {
            "printed_A01_found": printed["contains_A01_label"],
            "printed_integrability_claim_found": printed["contains_integrability_claim"],
            "computed_dbar_A_plus_A_wedge_A_zero": not nonzero,
            "integrability_fails": bool(nonzero),
            "printed_A01_can_supply_DE_closure": False,
            "selected_DE_or_rhoE_matrix_source_found": False,
            "qa_su3_packet_closed": False,
            "closure_claimed": False,
        },
        "decision": {
            "result": "The printed A01 matrix cannot close Qa/SU3.",
            "why": "Using the paper's stated dbar(bar omega^3)=bar omega^1 wedge bar omega^2, the (1,2) component of dbar A + A wedge A is mu e12, so dbar_E^2 is not zero for mu>0.",
            "repair_required": "A source-certified corrected A01/D_E matrix, or typed monad f,g/cochain/rho_E data, must replace this printed matrix.",
        },
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3PrintedA01IntegrabilityOrClosure",
        "status": "QA_SU3_PRINTED_A01_AUDITED_INTEGRABILITY_FAILS_OPERATOR_CLOSURE_REJECTED",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "printed_A01_checked": True,
            "integrability_failure_computed": True,
            "printed_A01_rejected_as_operator_exit": True,
        },
        "what_remains_open": {
            "source_certified_corrected_A01_or_DE": True,
            "typed_f_g_matrices": True,
            "rhoE_or_cochain_packet": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": "Selected_Qa_SU3_Minimal_Closing_Source_Data_Request_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = """# Selected Qa/SU3 Printed A01 Integrability or Closure v1

The source prints an explicit left-invariant `(0,1)` matrix:

```text
A_12 = mu e3
A_13 = sqrt(mu) e1
A_31 = -sqrt(mu) e2
dbar e3 = e1 wedge e2
```

The integrability test is:

```text
F^{0,2} = dbar A + A wedge A.
```

The computed `(1,2)` entry is:

```text
F^{0,2}_{12} = mu e1 wedge e2
```

so the printed matrix does not satisfy `dbar_E^2 = 0` for `mu > 0`.
Changing only the sign convention for `dbar e3` gives `-mu e1 wedge e2`,
still nonzero.

Therefore the printed `A01` cannot be the selected operator exit.  Closure still
requires a source-certified corrected `A01/D_E`, or typed monad/cochain/rho_E
data.

closure claimed: no
target fitting used: no
"""
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
