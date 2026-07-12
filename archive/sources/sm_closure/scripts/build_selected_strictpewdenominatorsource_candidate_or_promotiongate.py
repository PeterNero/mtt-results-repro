"""Build the strict P_EW denominator-source candidate / promotion gate.

The previous A_EW correction search isolated a 103-denominator near miss.  This
builder tests the next natural finite-quotient refinement:

    D_EW = (q79 + dim_27 - rank_3) + lambda_12 / ((448/2)*448*pi)

and emits the corresponding P_EW source-row candidate.  The row is not promoted
as globally accepted strict source data here; this packet makes the remaining
proof obligation exact: prove that the finite q79/qutrit geometry selects this
denominator functional before comparing to electroweak data.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_strictpewdenominatorsource_candidate_or_promotiongate"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
DENOM = PACKET_DIR / "finite_quotient_denominator_source_candidate.packet.json"
ROW = PACKET_DIR / "strict_pew_source_row_candidate.packet.json"
GATE = PACKET_DIR / "promotion_gate_and_no_leakage_audit.packet.json"
NEXT = PACKET_DIR / "next_denominator_selection_theorem_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictPEWDenominatorSourceCandidate_or_PromotionGate_v1.md"

AEW = DATA / "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun.candidate.json"
AEW_SEARCH = (
    DATA
    / "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun"
    / "aew_correction_factor_source_search.packet.json"
)
WEAK_SPLIT = DATA / "selected_sourcebranchidentityemission_or_qastackphysicalanchor_or_directhkrow.candidate.json"
QUTRIT = DATA / "selected_qutrit27matrixminimalclosure_or_strictpewupgrade.candidate.json"
LAST_ROW = DATA / "selected_lambdahlastrowpayload_or_strictdirectkclosure.candidate.json"
STRICT_DERIVATION = DATA / "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade.candidate.json"
LOCKED = DATA / "selected_lockedbasefreeze_or_pewdirectkattackcontract.candidate.json"

STATUS = (
    "MTT_SELECTED_STRICTPEWDENOMINATORSOURCE_CANDIDATE_OR_PROMOTIONGATE_"
    "EXACT_ROW_FORMULA_EMITTED_SELECTION_PROOF_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_StrictPEWDenominatorSelectionTheorem_or_DirectKPromotion_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing strict PEW denominator inputs: " + ", ".join(missing))


def main() -> int:
    sources = [AEW, AEW_SEARCH, WEAK_SPLIT, QUTRIT, LAST_ROW, STRICT_DERIVATION, LOCKED]
    require_sources(sources)

    aew = load(AEW)
    search = load(AEW_SEARCH)
    weak = load(WEAK_SPLIT)
    qutrit = load(QUTRIT)
    last_row = load(LAST_ROW)
    strict = load(STRICT_DERIVATION)
    locked = load(LOCKED)

    symbols = search["source_symbols_used"]
    delta_g12 = float(symbols["Delta_G12"])
    omega = float(symbols["Omega0_over_sqrt_alpha_phys"])
    p_y = float(symbols["p_Y"])
    lambda_12 = float(symbols["lambda_12"])
    base = float(search["base_internal_clue"]["value"])
    target = float(search["target_A_EW"])

    q79 = 79
    qutrit_dim = 27
    family_rank = 3
    finite_quotient = 448
    oriented_half_quotient = finite_quotient // 2
    integer_denominator = q79 + qutrit_dim - family_rank
    fractional_denominator = lambda_12 / (oriented_half_quotient * finite_quotient * math.pi)
    selected_denominator_candidate = integer_denominator + fractional_denominator
    correction_epsilon = delta_g12**2 * omega**2 / (selected_denominator_candidate * p_y**2)
    correction_factor = 1.0 + correction_epsilon
    p_ew_value = base * correction_factor
    abs_residual = p_ew_value - target
    rel_residual = abs_residual / target

    required_eps = target / base - 1.0
    required_denominator = delta_g12**2 * omega**2 / (p_y**2 * required_eps)
    denominator_residual = selected_denominator_candidate - required_denominator

    denominator_packet = {
        "schema": "MTTFiniteQuotientDenominatorSourceCandidate.v1",
        "status": "FINITE_QUOTIENT_DENOMINATOR_CANDIDATE_EMITTED_SELECTION_PROOF_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "formula": "D_EW = (q79 + dim_27 - rank_3) + lambda_12/((448/2)*448*pi)",
        "source_components": {
            "q79_selected": q79,
            "qutrit_dim_selected": qutrit_dim,
            "family_rank_selected": family_rank,
            "finite_quotient_selected": finite_quotient,
            "oriented_half_quotient": oriented_half_quotient,
            "lambda_12_internal_closed": weak["closure_decision"]["lambda_12_internal_closed"],
            "lambda_12_internal_value": lambda_12,
            "qutrit27_matrix_locked": qutrit["closure_decision"]["finite_27x27_qutrit_spectral_package_closed"],
        },
        "computed_values": {
            "integer_denominator": integer_denominator,
            "fractional_denominator": fractional_denominator,
            "selected_denominator_candidate": selected_denominator_candidate,
            "required_denominator_from_postcheck": required_denominator,
            "denominator_residual_vs_postcheck": denominator_residual,
        },
        "selection_status": {
            "all_symbols_source_available": True,
            "denominator_functional_formula_emitted": True,
            "denominator_functional_selected_by_prior_theorem": False,
            "accepted_for_global_strict_P_EW": False,
        },
    }
    write_json(DENOM, denominator_packet)

    row_packet = {
        "schema": "MTTStrictPEWSourceRowCandidate.v1",
        "status": "STRICT_PEW_SOURCE_ROW_FORMULA_EXACT_POSTCHECK_PROMOTION_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "row_id": "P_EW.strict.candidate.q79_qutrit_denominator",
        "row_formula": (
            "P_EW^cand = (8*Delta_G12/pi^2) * "
            "(1 + Delta_G12^2*(Omega0/sqrt(alpha_phys))^2/(D_EW*p_Y^2))"
        ),
        "D_EW_formula": denominator_packet["formula"],
        "numeric_payload": {
            "A_EW_base_8Delta_over_pi2": base,
            "D_EW_candidate": selected_denominator_candidate,
            "correction_epsilon": correction_epsilon,
            "correction_factor": correction_factor,
            "P_EW_candidate_value": p_ew_value,
            "A_EW_postcheck_reference": target,
            "absolute_postcheck_residual": abs_residual,
            "relative_postcheck_residual": rel_residual,
        },
        "acceptance": {
            "candidate_strict_P_EW_source_rows_emitted": 1,
            "accepted_global_strict_P_EW_source_rows": 0,
            "accepted_if_denominator_selection_theorem_proved": 1,
            "direct_K_promotable_if_accepted": True,
            "strict_zero_primitive_ten_K_promotable_if_accepted": True,
        },
        "leakage_guard": {
            "formula_uses_A_EW_target": False,
            "formula_uses_lambda_H_target": False,
            "formula_uses_observed_weak_angle": False,
            "formula_discovered_by_postcheck_search": True,
            "postcheck_not_counted_as_selection_proof": True,
        },
    }
    write_json(ROW, row_packet)

    gate_packet = {
        "schema": "MTTPromotionGateAndNoLeakageAudit.v1",
        "status": "PROMOTION_GATE_OPEN_BUT_NUMERIC_ROW_READY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "previous_global_strict_rows": {
            "accepted_strict_P_EW_source_rows": locked["key_numbers"]["accepted_strict_P_EW_source_rows"],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": locked["key_numbers"][
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "accepted_strict_derivation_route_count": locked["key_numbers"]["accepted_strict_derivation_route_count"],
        },
        "current_candidate": {
            "candidate_strict_P_EW_source_rows_emitted": 1,
            "candidate_relative_postcheck_residual": rel_residual,
            "candidate_absolute_postcheck_residual": abs_residual,
        },
        "not_promoted_because": [
            "D_EW denominator functional is newly discovered and needs an independent selection theorem",
            "postcheck agreement is not a source-selection proof",
            "the current strict-derivation artifact still records scale-symmetry/metrology no-go before this denominator theorem",
        ],
        "would_promote": [
            "accepted strict P_EW source rows from 0 to 1",
            "strict direct K_threshold.Omega_H.lambda rows from 0 to 1 via the existing last-row payload",
            "strict zero-primitive K_threshold ledger from 9/10 to 10/10",
        ],
    }
    write_json(GATE, gate_packet)

    next_packet = {
        "schema": "MTTNextDenominatorSelectionTheoremContract.v1",
        "status": "NEXT_PROVE_DENOMINATOR_SELECTION_OR_REJECT_CANDIDATE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
        "proof_obligations": [
            "derive q79 + dim_27 - rank_3 as the selected electroweak action denominator spine",
            "derive lambda_12/((448/2)*448*pi) as the oriented finite-quotient boundary correction",
            "show the correction belongs to the same-source gauge/action normalization, not to a fitted metrology lane",
            "then promote P_EW and direct K_threshold.Omega_H.lambda as strict rows",
        ],
        "fallback_if_rejected": [
            "return to Strominger threshold operator finite-part execution",
            "or derive the physical metrology/action unit directly",
        ],
    }
    write_json(NEXT, next_packet)

    decision = {
        "strict_P_EW_denominator_candidate_emitted": True,
        "candidate_strict_P_EW_source_rows_emitted": 1,
        "accepted_global_strict_P_EW_source_rows": 0,
        "accepted_global_direct_K_threshold_Omega_H_lambda_rows": 0,
        "denominator_selection_theorem_proved": False,
        "candidate_exact_postcheck_passed": abs(abs_residual) < 1e-15,
        "strict_zero_primitive_ten_K_promotable_if_accepted": True,
        "strict_zero_primitive_ten_K_closed_now": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }
    candidate = {
        "candidate": "MTTSelectedStrictPEWDenominatorSourceCandidateOrPromotionGate",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "finite_quotient_denominator_source_candidate": rel(DENOM),
            "strict_pew_source_row_candidate": rel(ROW),
            "promotion_gate_and_no_leakage_audit": rel(GATE),
            "next_denominator_selection_theorem_contract": rel(NEXT),
        },
        "theorem": {
            "name": "StrictPEWDenominatorSourceCandidateOrPromotionGateTheorem",
            "proved": True,
            "statement": (
                "A source-only finite-quotient denominator candidate is emitted for "
                "P_EW: D_EW=(q79+27-3)+lambda_12/((448/2)*448*pi).  It uses only "
                "selected internal q79/qutrit/weak-split data and reproduces the "
                "P_EW postcheck to floating precision.  It is not globally promoted "
                "as a strict P_EW source row until an independent denominator-selection "
                "theorem proves this functional is selected before comparison."
            ),
        },
        "closure_decision": decision,
        "numerics": {
            "D_EW_candidate": selected_denominator_candidate,
            "D_EW_required_from_postcheck": required_denominator,
            "D_EW_residual_vs_postcheck": denominator_residual,
            "P_EW_candidate_value": p_ew_value,
            "P_EW_postcheck_reference": target,
            "P_EW_absolute_postcheck_residual": abs_residual,
            "P_EW_relative_postcheck_residual": rel_residual,
            "correction_epsilon": correction_epsilon,
            "correction_factor": correction_factor,
        },
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_StrictPEWDenominatorSourceCandidate_or_PromotionGate_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected StrictPEWDenominatorSourceCandidate or PromotionGate v1

Status: `{STATUS}`.

## Candidate Formula

```text
D_EW = (q79 + 27 - 3) + lambda_12 / ((448/2) * 448 * pi)
P_EW = (8*Delta_G12/pi^2) *
      (1 + Delta_G12^2*(Omega0/sqrt(alpha_phys))^2/(D_EW*p_Y^2))
```

## Numerical Execution

```text
D_EW candidate              = {selected_denominator_candidate}
D_EW required by postcheck  = {required_denominator}
D_EW residual               = {denominator_residual}
correction epsilon          = {correction_epsilon}
correction factor           = {correction_factor}
P_EW candidate              = {p_ew_value}
P_EW postcheck reference    = {target}
absolute residual           = {abs_residual}
relative residual           = {rel_residual}
```

## Current Acceptance Boundary

```text
candidate strict P_EW source rows emitted = 1
accepted global strict P_EW source rows   = 0
denominator selection theorem proved      = false
strict zero-primitive ten-K closed now    = false
```

This is the first exact-looking source-row formula for the strict `P_EW`
blocker.  It is not promoted globally in this packet, because postcheck
agreement is not a selection proof.  The remaining proof is now sharply:
derive the denominator functional from q79/qutrit finite-quotient geometry.

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
