"""Recompute A01 repair candidates against the full invariant MC equations."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUT_A01 = DATA / "printed_a01_integrability_or_closure.candidate.json"
OUTPUT_DATA = DATA / "a01_repair_guardrail_local_recompute.candidate.json"
OUTPUT_CERT = CERTS / "a01_repair_guardrail_local_recompute_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_A01_Repair_Guardrail_Local_Recompute_v1.md"


Matrix = list[list[int]]


def zero() -> Matrix:
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def e(i: int, j: int) -> Matrix:
    out = zero()
    out[i - 1][j - 1] = 1
    return out


def diag(values: list[int]) -> Matrix:
    out = zero()
    for idx, value in enumerate(values):
        out[idx][idx] = value
    return out


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]


def neg(a: Matrix) -> Matrix:
    return [[-a[i][j] for j in range(3)] for i in range(3)]


def mul(a: Matrix, b: Matrix) -> Matrix:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def comm(a: Matrix, b: Matrix) -> Matrix:
    return add(mul(a, b), neg(mul(b, a)))


def is_zero(a: Matrix) -> bool:
    return all(a[i][j] == 0 for i in range(3) for j in range(3))


def sparse(a: Matrix) -> list[dict[str, int]]:
    return [
        {"entry": f"E{i + 1}{j + 1}", "coefficient": a[i][j]}
        for i in range(3)
        for j in range(3)
        if a[i][j] != 0
    ]


def matrix_id(a: Matrix) -> str:
    pieces: list[str] = []
    for i in range(3):
        for j in range(3):
            value = a[i][j]
            if value == 0:
                continue
            basis = f"E{i + 1}{j + 1}"
            if value == 1:
                pieces.append(f"+{basis}")
            elif value == -1:
                pieces.append(f"-{basis}")
            elif value > 0:
                pieces.append(f"+{value}{basis}")
            else:
                pieces.append(f"{value}{basis}")
    return "0" if not pieces else " ".join(pieces).lstrip("+")


def residuals(b1: Matrix, b2: Matrix, b3: Matrix) -> dict[str, Matrix]:
    return {
        "F12_B3_plus_comm_B1_B2": add(b3, comm(b1, b2)),
        "F13_comm_B1_B3": comm(b1, b3),
        "F23_comm_B2_B3": comm(b2, b3),
    }


def evaluate(label: str, source_status: str, b1: Matrix, b2: Matrix, b3: Matrix) -> dict[str, object]:
    res = residuals(b1, b2, b3)
    return {
        "label": label,
        "source_status": source_status,
        "matrices": {
            "B1_e1": matrix_id(b1),
            "B2_e2": matrix_id(b2),
            "B3_e3": matrix_id(b3),
        },
        "residuals": {key: sparse(value) for key, value in res.items()},
        "reduced_F12_passes": is_zero(res["F12_B3_plus_comm_B1_B2"]),
        "full_maurer_cartan_passes": all(is_zero(value) for value in res.values()),
    }


def build() -> tuple[dict[str, object], dict[str, object], str]:
    printed = json.loads(INPUT_A01.read_text(encoding="utf-8"))
    candidates = [
        evaluate(
            "printed_A01",
            "source-printed but rejected by direct curvature audit",
            e(1, 3),
            neg(e(3, 1)),
            e(1, 2),
        ),
        evaluate(
            "repair_A_diagonal_B3",
            "not source-certified; older reduced-equation diagnostic",
            e(1, 3),
            neg(e(3, 1)),
            diag([1, 0, -1]),
        ),
        evaluate(
            "repair_B_move_B2_to_minus_E32",
            "algebraically full-MC integrable, but not source-certified by corpus",
            e(1, 3),
            neg(e(3, 2)),
            e(1, 2),
        ),
    ]
    by_label = {item["label"]: item for item in candidates}
    candidate = {
        "candidate": "SelectedQaSU3A01RepairGuardrailLocalRecompute",
        "status": "A01_REPAIR_GUARDRAIL_LOCAL_RECOMPUTED_REPAIR_B_FULL_MC_PASSES_NOT_SOURCE_CERTIFIED",
        "input_status": printed["status"],
        "normal_form": {
            "A": "sqrt(mu) B1 e1 + sqrt(mu) B2 e2 + mu B3 e3",
            "dbar_e3": "e1^e2",
            "full_MC_equations": [
                "B3 + [B1,B2] = 0",
                "[B1,B3] = 0",
                "[B2,B3] = 0",
            ],
        },
        "local_recompute": candidates,
        "decisions": {
            "printed_A01_rejected": by_label["printed_A01"]["full_maurer_cartan_passes"] is False,
            "repair_A_rejected_in_this_full_MC_convention": by_label["repair_A_diagonal_B3"]["full_maurer_cartan_passes"] is False,
            "repair_B_full_MC_integrable": by_label["repair_B_move_B2_to_minus_E32"]["full_maurer_cartan_passes"] is True,
            "repair_B_source_certified": False,
            "repair_B_accepted_as_operator_exit": False,
            "closure_claimed": False,
        },
        "why_not_closed": [
            "The only tested sparse repair passing the full MC equations changes the printed B2 entry from -E31 to -E32.",
            "No current source artifact selects that correction, supplies its stability/HYM/Bianchi data, or gives its finite D_E/rho_E response.",
            "Therefore the algebraic repair is a useful erratum candidate, not a proof source.",
        ],
        "target_fitting_used": False,
        "next_required_artifact": "Selected_Qa_SU3_Endomorphism_or_Local_System_Torsion_Decision_v1",
    }
    certificate = {
        "certificate": "SelectedQaSU3A01RepairGuardrailLocalRecompute",
        "status": "QA_SU3_A01_REPAIR_GUARDRAIL_LOCAL_RECOMPUTED_REPAIR_B_FULL_MC_PASSES_NOT_SOURCE_CERTIFIED",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "printed_A01_failure_confirmed": True,
            "repair_A_full_MC_failure_confirmed": True,
            "repair_B_full_MC_integrable_candidate_found": True,
            "repair_B_source_certified": False,
        },
        "what_remains_open": {
            "source_selection_of_repair_B_or_other_A01": True,
            "stability_HYM_Bianchi_packet": True,
            "finite_DE_rhoE_or_torsion_response": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 A01 Repair Guardrail Local Recompute v1

We recompute the sparse A01 repair options in the scale-free normal form

```text
A = sqrt(mu) B1 e1 + sqrt(mu) B2 e2 + mu B3 e3,
dbar e3 = e1 wedge e2.
```

The full invariant Maurer-Cartan equations are

```text
B3 + [B1,B2] = 0,
[B1,B3] = 0,
[B2,B3] = 0.
```

## Local Results

| candidate | B1 | B2 | B3 | reduced F12 | full MC |
|---|---|---|---|---|---|
| printed A01 | E13 | -E31 | E12 | fail | fail |
| repair A | E13 | -E31 | E11-E33 | pass | fail |
| repair B | E13 | -E32 | E12 | pass | pass |

The important result is narrow: moving the printed `B2=-E31` entry to
`B2=-E32` gives a sparse full-Maurer-Cartan integrable candidate.

## Guardrail

This does not close Qa/SU3. Repair B is not source-certified by the current
corpus. It is an erratum candidate unless a same-branch source selects it and
also supplies stability/HYM/Bianchi data plus the finite `D_E`, `rho_E`, or
torsion response.

Next required artifact:

```text
{candidate["next_required_artifact"]}
```

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, note


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
