"""Build the heterotic HYM erratum/repair comparison gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

INPUTS = {
    "printed_block": DATA / "selected_heterotic_hym_delta_a_invariant_block_computation.candidate.json",
    "connection_erratum": NONSM / "certificates" / "selected_qa_su3_hym_connection_erratum_or_convention_resolution_certificate.json",
    "erratum_guardrail": NONSM / "certificates" / "selected_qa_su3_hym_erratum_guardrail_deep_scan_certificate.json",
    "explicit_route_retirement": NONSM / "certificates" / "selected_qa_su3_explicit_hym_route_retirement_certificate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_hym_erratum_repair_comparison_gate.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_hym_erratum_repair_comparison_gate_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_HYM_Erratum_Repair_Comparison_Gate_v1.md"

STATUS = "HETEROTIC_HYM_ERRATUM_REPAIR_COMPARISON_BUILT_SOURCE_SELECTION_OPEN"
NEXT = "Selected_Heterotic_HYM_RepairedPipeline_A_B_SourceSelection_or_Retirement_v1"

SAMPLES = [0.25, 1.0, 4.0]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def zero() -> list[list[float]]:
    return [[0.0] * 3 for _ in range(3)]


def e(i: int, j: int, scale: float = 1.0) -> list[list[float]]:
    m = zero()
    m[i][j] = scale
    return m


def add(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]


def sub(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(3)] for i in range(3)]


def mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def comm(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return sub(mul(a, b), mul(b, a))


def frob2(a: list[list[float]]) -> float:
    return sum(x * x for row in a for x in row)


def flatten(a: list[list[float]]) -> list[float]:
    return [x for row in a for x in row]


def basis() -> list[list[list[float]]]:
    return [e(i, j) for i in range(3) for j in range(3)]


def connection(variant: str, mu: float) -> list[list[list[float]]]:
    s = math.sqrt(mu)
    b1 = e(0, 2, s)
    if variant == "repair_B_one_entry_B2_move":
        b2 = e(2, 1, -s)
    else:
        b2 = e(2, 0, -s)
    if variant == "repair_A_diagonal_B3":
        b3 = add(e(0, 0, mu), e(2, 2, -mu))
    else:
        b3 = e(0, 1, mu)
    return [b1, b2, b3]


def integrability_residual(variant: str, mu: float) -> list[list[float]]:
    b1, b2, b3 = connection(variant, mu)
    return add(b3, comm(b1, b2))


def gram_matrix(variant: str, mu: float) -> list[list[float]]:
    bs = connection(variant, mu)
    xs = basis()
    mat = [[0.0] * 9 for _ in range(9)]
    for b in bs:
        cols = [flatten(comm(b, x)) for x in xs]
        for i in range(9):
            for j in range(9):
                mat[i][j] += sum(cols[i][k] * cols[j][k] for k in range(9))
    return mat


def jacobi_eigs(a: list[list[float]]) -> list[float]:
    a = [row[:] for row in a]
    n = len(a)
    for _ in range(200):
        p, q, mx = 0, 1, abs(a[0][1])
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > mx:
                    p, q, mx = i, j, abs(a[i][j])
        if mx < 1e-11:
            break
        phi = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
        c, s = math.cos(phi), math.sin(phi)
        for k in range(n):
            apk, aqk = a[p][k], a[q][k]
            a[p][k], a[q][k] = c * apk - s * aqk, s * apk + c * aqk
        for k in range(n):
            akp, akq = a[k][p], a[k][q]
            a[k][p], a[k][q] = c * akp - s * akq, s * akp + c * akq
    return sorted(0.0 if abs(a[i][i]) < 1e-9 else a[i][i] for i in range(n))


def sample_variant(variant: str) -> dict[str, Any]:
    samples = []
    for mu in SAMPLES:
        eigs = jacobi_eigs(gram_matrix(variant, mu))
        pos = [x for x in eigs if x > 1e-8]
        det = math.prod(pos)
        residual = integrability_residual(variant, mu)
        samples.append(
            {
                "mu": mu,
                "integrability_residual_norm_squared": frob2(residual),
                "eigenvalues": eigs,
                "zero_modes": len(eigs) - len(pos),
                "positive_modes": len(pos),
                "det_prime": det,
                "log_det_prime": math.log(det) if det > 0 else None,
                "trace": sum(eigs),
            }
        )
    return {
        "variant": variant,
        "integrable_under_standard_check": all(s["integrability_residual_norm_squared"] < 1e-10 for s in samples),
        "samples": samples,
        "source_certified": False if variant != "printed_as_source" else None,
    }


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    printed_block = load(INPUTS["printed_block"])
    erratum = load(INPUTS["connection_erratum"])
    guardrail = load(INPUTS["erratum_guardrail"])
    retirement = load(INPUTS["explicit_route_retirement"])

    variants = {
        "printed_as_source": sample_variant("printed_as_source"),
        "repair_A_diagonal_B3": sample_variant("repair_A_diagonal_B3"),
        "repair_B_one_entry_B2_move": sample_variant("repair_B_one_entry_B2_move"),
    }
    variants["printed_as_source"]["source_certified"] = False

    decision = {
        "printed_block_demoted_to_diagnostic": True,
        "printed_integrable_under_standard_check": variants["printed_as_source"]["integrable_under_standard_check"],
        "repair_A_integrable": variants["repair_A_diagonal_B3"]["integrable_under_standard_check"],
        "repair_B_integrable": variants["repair_B_one_entry_B2_move"]["integrable_under_standard_check"],
        "repair_A_source_certified": False,
        "repair_B_source_certified": False,
        "any_repair_selected": False,
        "hym_route_retired_as_final_proof_source_until_repair_selection": True,
        "physical_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticHYMErratumRepairComparisonGate",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "printed_block": printed_block["status"],
            "connection_erratum": erratum["status"],
            "erratum_guardrail": guardrail["status"],
            "explicit_route_retirement": retirement["status"],
        },
        "variants": variants,
        "decision": decision,
        "theorem": {
            "name": "HeteroticHYMErratumRepairComparisonGate",
            "proved": True,
            "statement": (
                "The printed Iwasawa HYM connection cannot be used as a final "
                "threshold proof source under the standard integrability check. "
                "Two algebraic repairs are integrable in diagnostics: Repair A "
                "replaces B3 by mu(E11-E33), and Repair B moves B2 from -E31 "
                "to -E32 while keeping B3=E12. Neither repair is source-certified. "
                "Therefore all HYM determinant/Hessian blocks computed from the "
                "printed or repaired matrices remain diagnostic until a source "
                "erratum or independent selection theorem chooses one branch and "
                "verifies the Chern-Weil, HYM, trace, quotient, and threshold data."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "selects_repair_by_near_hit": False,
            "promotes_printed_nonintegrable_matrix": False,
            "promotes_unsourced_repair": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedHeteroticHYMErratumRepairComparisonGate",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "printed_block_demoted_to_diagnostic": True,
        "repair_A_integrable": decision["repair_A_integrable"],
        "repair_B_integrable": decision["repair_B_integrable"],
        "any_repair_selected": False,
        "hym_route_retired_as_final_proof_source_until_repair_selection": True,
        "physical_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    return f"""# Selected Heterotic HYM Erratum Repair Comparison Gate v1

## Result

```text
status = {candidate["status"]}
printed_block_demoted_to_diagnostic = true
repair_A_integrable = {str(candidate["decision"]["repair_A_integrable"]).lower()}
repair_B_integrable = {str(candidate["decision"]["repair_B_integrable"]).lower()}
any_repair_selected = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Comparison

```json
{json.dumps(candidate["variants"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
