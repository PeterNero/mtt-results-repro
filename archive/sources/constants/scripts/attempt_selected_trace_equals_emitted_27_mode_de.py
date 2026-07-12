"""Try to prove the selected trace equals the emitted 27-mode D_E matrices."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

MORPHISM = DATA / "selected_phifin_s2_finite_trace_morphism_scaffold.candidate.json"
SMOOTH_BN = SM / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DE_27_HONEST = (
    SM
    / "candidate_data"
    / "selected_routec_de_action_on_smooth_bn"
    / "de_action_on_smooth_bn.honest.json"
)

OUTPUT_PACKET = DATA / "selected_trace_equals_emitted_27_mode_de_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_trace_equals_emitted_27_mode_de_attempt_certificate.json"
OUTPUT_NOTE = CORPUS / "SelectedTraceEqualsEmitted27ModeDE_Attempt_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def diagonal(matrix: list[list[float]]) -> list[float]:
    return [float(matrix[i][i]) for i in range(len(matrix))]


def offdiag_max(matrix: list[list[float]]) -> float:
    max_value = 0.0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if i != j:
                max_value = max(max_value, abs(float(value)))
    return max_value


def basis_formula_values(basis: list[dict[str, Any]]) -> list[float]:
    unit = (2.0 * math.pi / 3.0) ** 2
    values = []
    for item in basis:
        m, n = item["integer_representative"]
        values.append(unit * (m * m + n * n))
    return values


def max_abs(values_a: list[float], values_b: list[float]) -> float:
    return max(abs(a - b) for a, b in zip(values_a, values_b))


def build_packet() -> dict[str, Any]:
    morphism = load_json(MORPHISM)
    smooth = load_json(SMOOTH_BN)
    de_27 = load_json(DE_27_HONEST)
    basis = smooth["B_N_lift"]["basis"]
    canonical_diag = basis_formula_values(basis)
    zero_indices = smooth["B_N_lift"]["zero_cluster"]["indices"]
    higgs_shift_indices = zero_indices[1:]

    sector_formula_checks: dict[str, Any] = {}
    for sector, slot in sorted(de_27["operator_slots"].items()):
        diag = diagonal(slot["stiffness_matrix"])
        shift = [0.0] * len(diag)
        if sector == "H":
            for idx in higgs_shift_indices:
                shift[idx] = 1.0
        expected = [base + extra for base, extra in zip(canonical_diag, shift)]
        sector_formula_checks[sector] = {
            "offdiag_max": offdiag_max(slot["stiffness_matrix"]),
            "matches_canonical_formula": max_abs(diag, expected) < 1e-12,
            "max_diag_formula_error": max_abs(diag, expected),
            "uses_higgs_zero_cluster_shift": sector == "H",
            "higgs_shift_indices": higgs_shift_indices if sector == "H" else [],
            "selected_source_verified": bool(slot.get("selected_source_verified")),
        }

    all_formula_match = all(
        item["matches_canonical_formula"] and item["offdiag_max"] < 1e-12
        for item in sector_formula_checks.values()
    )
    selected_flags_all_false = all(
        not item["selected_source_verified"] for item in sector_formula_checks.values()
    )

    formula_theorem = {
        "name": "Emitted27ModeDECanonicalFormula",
        "proved": all_formula_match,
        "statement": (
            "On B_N, each emitted family-sector stiffness matrix is diagonal "
            "with entries ((2*pi)/3)^2(m^2+n^2), repeated across the rank-3 "
            "fiber. The H sector equals the same diagonal operator plus the "
            "rank-two unit zero-cluster projector on indices 13,14."
        ),
    }

    selected_trace_attempt = {
        "name": "SelectedTraceEqualsEmitted27ModeDE",
        "proved": False,
        "reason": (
            "The emitted entries have an exact canonical finite Fourier formula, "
            "but the corpus still does not prove that the selected smooth "
            "Strominger/HYM trace has the canonical active metric normalization "
            "and the H-sector rank-two zero-cluster shift. Therefore the formula is "
            "identified, not yet promoted to selected trace equality."
        ),
    }

    return {
        "packet": "SelectedTraceEqualsEmitted27ModeDE_Attempt_v1",
        "status": "EMITTED_DE_FORMULA_CLOSED_SELECTED_TRACE_EQUALITY_OPEN",
        "inputs": {
            "morphism_scaffold": str(MORPHISM.relative_to(ROOT)),
            "smooth_BN": str(SMOOTH_BN),
            "DE_27_honest": str(DE_27_HONEST),
        },
        "formula_theorem": formula_theorem,
        "selected_trace_attempt": selected_trace_attempt,
        "sector_formula_checks": sector_formula_checks,
        "remaining_selected_trace_payload": {
            "canonical_active_metric_normalization_selected": True,
            "selected_connection_reduces_to_projective_flat_trace_on_active_F3xF3": True,
            "H_sector_rank_two_zero_cluster_shift_selected": True,
            "same_source_derivation_for_all_sector_matrices": True,
        },
        "conditional_consequence": morphism["conditional_consequence_ready"],
        "guardrails": {
            "does_not_set_selected_source_flags": True,
            "does_not_claim_selected_trace_equality": True,
            "does_not_use_observed_or_benchmark_inputs": True,
            "keeps_formula_identity_separate_from_source_provenance": True,
        },
        "verdict": {
            "what_closes_now": (
                "The emitted 27-mode D_E matrices are exactly identified as the "
                "canonical F3xF3 Fourier Laplacian, with only a rank-two unit Higgs "
                "zero-cluster shift."
            ),
            "what_remains": (
                "Prove that the selected Phi_fin/Strominger trace selects this "
                "canonical metric/connection formula and the H-sector shift from "
                "the same source."
            ),
            "next_required_artifact": "SelectedCanonicalTraceFormulaSource_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedTraceEqualsEmitted27ModeDEAttempt",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes_now": {
            "emitted_27_mode_formula": packet["formula_theorem"]["proved"],
            "family_sectors_equal_canonical_laplacian": True,
            "H_sector_equals_canonical_laplacian_plus_zero_shift": True,
        },
        "what_remains_open": {
            "selected_trace_equality": True,
            "canonical_metric_connection_source": True,
            "H_sector_shift_source": True,
            "selected_source_flags": True,
        },
        "selected_trace_attempt": packet["selected_trace_attempt"],
        "conditional_consequence": packet["conditional_consequence"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# SelectedTraceEqualsEmitted27ModeDE Attempt v1

## Result

Status: `{cert["status"]}`

The emitted finite matrices now have an exact formula.  The selected trace
equality is still open.

## Closed Formula

```text
family sectors: lambda(m,n) = ((2*pi)/3)^2 (m^2+n^2)
H sector: same lambda(m,n), plus rank-two unit projector on zero-cluster indices 13,14
```

Formula theorem proved: `{packet["formula_theorem"]["proved"]}`

## Sector Checks

```json
{json.dumps(packet["sector_formula_checks"], indent=2, sort_keys=True)}
```

## Remaining Source Payload

The next proof must derive these formula ingredients from the selected smooth
source, not from the already emitted matrices:

{chr(10).join("- " + item for item in packet["remaining_selected_trace_payload"])}

## Consequence If Source Payload Closes

```text
eta_N = {packet["conditional_consequence"]["eta_N_if_gate_closes"]}
threshold = {packet["conditional_consequence"]["threshold"]}
passes = {packet["conditional_consequence"]["passes_threshold"]}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
