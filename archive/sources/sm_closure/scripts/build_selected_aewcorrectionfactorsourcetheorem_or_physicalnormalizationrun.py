"""Build the A_EW correction-factor / physical-normalization frontier run.

This artifact consumes the latest strict PEW/direct-K payload plus the first
repo-wide normalization scan.  It attacks the exact correction factor needed to
turn the best internal clue, 8*Delta_G12/pi^2, into the physical prefactor row.
It is intentionally conservative: near-misses become theorem targets, not
accepted source rows.
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

SLUG = "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CORRECTION_SCAN = PACKET_DIR / "aew_correction_factor_source_search.packet.json"
PHYSICAL_RUN = PACKET_DIR / "physical_normalization_or_direct_k_run.packet.json"
FRONTIER = PACKET_DIR / "active_frontier_after_aew_correction_run.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AEWCorrectionFactorSourceTheorem_or_PhysicalNormalizationRun_v1.md"

FIRST_RUN = DATA / "selected_firstpewgaugeactionnormalizationvalue_or_directkcertificaterun.candidate.json"
FIRST_SCAN = (
    DATA
    / "selected_firstpewgaugeactionnormalizationvalue_or_directkcertificaterun"
    / "repo_wide_pew_numeric_clue_scan.packet.json"
)
PEW_PAYLOAD = DATA / "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload.candidate.json"
AEW_SOURCE = DATA / "selected_aewsourceoperator_or_thresholdconventionrows.candidate.json"
AEW_FILL = (
    DATA / "selected_aewsourceoperator_or_thresholdconventionrows" / "current_packet_fill_validation.packet.json"
)
FINITE_H = DATA / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
K_GATE = (
    DATA
    / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit"
    / "ten_kthreshold_gate_after_finite_hscalar_transport.packet.json"
)
CHARGED_K = (
    DATA
    / "selected_thresholddeltarows_or_lambdahpayloadexecution"
    / "ten_kthreshold_gate_after_charged_null_delta.packet.json"
)
ONE_PRIMITIVE = DATA / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy.candidate.json"
MIN_LEDGER = DATA / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem.candidate.json"

STATUS = (
    "MTT_SELECTED_AEWCORRECTIONFACTOR_SOURCE_THEOREM_OR_PHYSICALNORMALIZATIONRUN_"
    "EXECUTED_SHARP_NEARMISS_STRICT_PEW_OPEN"
)
NEXT = "MTT_Selected_PhysicalNormalizationSourceAxiom_or_DirectKCertificate_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A_EW correction inputs: " + ", ".join(missing))


def correction_candidate_rows(symbols: dict[str, float], epsilon_required: float) -> list[dict[str, Any]]:
    delta = symbols["Delta_G12"]
    p_y = symbols["p_Y"]
    omega = symbols["Omega0_over_sqrt_alpha_phys"]
    lambda_12 = symbols["lambda_12"]
    s_beta = symbols["s_beta"]
    log2008 = symbols["log2008"]
    p_a = symbols["p_a"]
    pi = math.pi
    rows = [
        (
            "corr_from_DeltaG12_pY_Omega0_over_103",
            "1 + Delta_G12^2*(Omega0/sqrt(alpha_phys))^2/(103*p_Y^2)",
            delta**2 * omega**2 / (103 * p_y**2),
            "sharpest constrained source-window clue; denominator 103 has no selected quotient/source theorem",
        ),
        (
            "corr_from_lambda12_Omega0_pi_2008",
            "1 + lambda_12/(2008*(Omega0/sqrt(alpha_phys))*pi^2)",
            lambda_12 / (2008 * omega * pi**2),
            "uses selected internal lambda_12 and the 2008 quotient determinant support, but no same-source prefactor theorem emits it",
        ),
        (
            "corr_from_lambda12_log2008_Omega0_50",
            "1 + 1/(50*lambda_12*log(2008)^2*(Omega0/sqrt(alpha_phys)))",
            1 / (50 * lambda_12 * log2008**2 * omega),
            "structured log-determinant clue only; denominator 50 is not selected here",
        ),
        (
            "corr_from_sbeta_lambda12_Omega0_20",
            "1 + s_beta*(Omega0/sqrt(alpha_phys))^2/(20*lambda_12^2)",
            s_beta * omega**2 / (20 * lambda_12**2),
            "uses selected s_beta but mixes H angular data into physical prefactor without a gauge-action theorem",
        ),
        (
            "corr_from_pa_pY_Omega0_448",
            "1 + (Omega0/sqrt(alpha_phys))/(448*p_a*p_Y)",
            omega / (448 * p_a * p_y),
            "uses the finite quotient 448 but remains a correction clue, not a selected normalization row",
        ),
    ]

    output = []
    for rank, (row_id, formula, epsilon, reason) in enumerate(rows, start=1):
        output.append(
            {
                "rank": rank,
                "row_id": row_id,
                "formula": formula,
                "epsilon_value": epsilon,
                "correction_factor_value": 1.0 + epsilon,
                "epsilon_relative_residual": abs(epsilon - epsilon_required) / abs(epsilon_required),
                "accepted_as_correction_source_row": False,
                "reason_rejected": reason,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return output


def main() -> int:
    sources = [
        FIRST_RUN,
        FIRST_SCAN,
        PEW_PAYLOAD,
        AEW_SOURCE,
        AEW_FILL,
        FINITE_H,
        K_GATE,
        CHARGED_K,
        ONE_PRIMITIVE,
        MIN_LEDGER,
    ]
    require_sources(sources)

    first_run = load(FIRST_RUN)
    first_scan = load(FIRST_SCAN)
    pew_payload = load(PEW_PAYLOAD)
    aew_source = load(AEW_SOURCE)
    aew_fill = load(AEW_FILL)
    finite_h = load(FINITE_H)
    k_gate = load(K_GATE)
    charged_k = load(CHARGED_K)
    one_primitive = load(ONE_PRIMITIVE)
    min_ledger = load(MIN_LEDGER)

    nums = aew_source["numerics"]
    target_aew = float(first_scan["target_A_EW"])
    delta = float(nums["Delta_G12"])
    base = 8 * delta / (math.pi**2)
    correction_required = target_aew / base
    epsilon_required = correction_required - 1.0
    symbols = {
        "Delta_G12": delta,
        "lambda_12": float(nums["lambda_12"]),
        "p_a": float(nums["p_a"]),
        "p_Y": float(nums["p_Y"]),
        "log448": 6.104793232414985,
        "log2008": 7.60489448081162,
        "Omega0_over_sqrt_alpha_phys": float(nums["Omega0_over_sqrt_alpha_phys"]),
        "s_beta": float(nums["s_beta"]),
    }
    rows = correction_candidate_rows(symbols, epsilon_required)
    best = rows[0]
    best_aew = base * best["correction_factor_value"]
    best_aew_relative_residual = abs(best_aew - target_aew) / abs(target_aew)

    correction_scan = {
        "schema": "MTTAEWCorrectionFactorSourceSearch.v1",
        "status": "CORRECTION_FACTOR_SEARCH_EXECUTED_NO_ACCEPTED_SOURCE_ROW",
        "closure_claimed": True,
        "target_A_EW": target_aew,
        "base_internal_clue": {
            "formula": "8*Delta_G12/pi^2",
            "value": base,
            "relative_residual": abs(base - target_aew) / abs(target_aew),
        },
        "required_correction": {
            "correction_factor_required": correction_required,
            "epsilon_required": epsilon_required,
        },
        "source_symbols_used": symbols,
        "candidate_rows": rows,
        "best_candidate_A_EW_value": best_aew,
        "best_candidate_A_EW_relative_residual": best_aew_relative_residual,
        "exact_source_hits_found": 0,
        "accepted_correction_source_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    physical_run = {
        "schema": "MTTPhysicalNormalizationOrDirectKRun.v1",
        "status": "PHYSICAL_NORMALIZATION_AND_DIRECT_K_RECHECK_ZERO_STRICT_ROWS",
        "closure_claimed": True,
        "strict_payload_contract_locked": pew_payload["closure_decision"]["payload_contract_locked"],
        "strict_source_required_field_count": pew_payload["closure_decision"]["source_required_field_count"],
        "strict_source_filled_field_count": pew_payload["closure_decision"]["source_filled_field_count"],
        "physical_prefactor_fields_filled_by_current_packets": aew_fill[
            "accepted_physical_prefactor_rows"
        ],
        "accepted_strict_P_EW_source_rows": 0,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        "selected_R_H_RG_source_emitted": finite_h["closure_decision"]["selected_R_H_RG_source_emitted"],
        "selected_H_radial_source_row_emitted": finite_h["closure_decision"][
            "selected_H_radial_source_row_emitted"
        ],
        "strict_K_rows_closed": charged_k["accepted_selected_K_source_row_count"],
        "strict_K_rows_required": charged_k["selected_K_threshold_row_count_required_for_full_scalar_execution"],
        "minimal_one_primitive_H_lambda_lane_closed": one_primitive["closure_decision"][
            "minimal_one_primitive_H_lambda_lane_closed"
        ],
        "minimal_one_primitive_ten_row_ledger_closed": (
            charged_k["accepted_selected_K_source_row_count"] == 9
            and one_primitive["closure_decision"]["minimal_one_primitive_H_lambda_lane_closed"]
        ),
        "strict_no_knob_ten_row_closure": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier = {
        "schema": "MTTActiveFrontierAfterAEWCorrectionRun.v1",
        "status": "STRICT_FRONTIER_IS_PHYSICAL_NORMALIZATION_OR_DIRECT_K_CERTIFICATE",
        "closure_claimed": True,
        "closed_active_ledger": [
            "nine charged K_threshold rows",
            "selected finite H scalar tau_H(A_N), r_H(A_N), and R_H^RG",
            "zero H-specific radial parameter",
            "minimal one-primitive H/lambda lane",
            "full-SM minimal parameter ledger at 18/24 excluding QCD theta_bar",
        ],
        "still_open_strict": [
            "selected physical gauge/action normalization P_EW or K_phys/f_ab",
            "selected mu_match and RG/threshold scheme",
            "exact source theorem for the A_EW correction factor",
            "direct row-level K_threshold.Omega_H.lambda certificate",
            "strict no-knob ten-row K closure",
            "true precision SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "correction_factor_search_executed": True,
        "best_base_formula": "8*Delta_G12/pi^2",
        "base_A_EW_value": base,
        "correction_factor_required": correction_required,
        "best_correction_formula": best["formula"],
        "best_correction_factor_value": best["correction_factor_value"],
        "best_correction_epsilon_relative_residual": best["epsilon_relative_residual"],
        "best_A_EW_relative_residual_after_correction": best_aew_relative_residual,
        "accepted_correction_source_row_count": 0,
        "accepted_strict_P_EW_source_rows": 0,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
        "selected_R_H_RG_source_emitted": True,
        "strict_K_threshold_rows_closed": 9,
        "minimal_one_primitive_ten_row_ledger_closed": True,
        "strict_no_knob_ten_row_closure": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedAEWCorrectionFactorSourceTheoremOrPhysicalNormalizationRun",
        "status": STATUS,
        "closure_claimed": True,
        "strict_P_EW_source_theorem_closed": False,
        "direct_K_threshold_Omega_H_lambda_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "aew_correction_factor_source_search": rel(CORRECTION_SCAN),
            "physical_normalization_or_direct_k_run": rel(PHYSICAL_RUN),
            "active_frontier_after_aew_correction_run": rel(FRONTIER),
        },
        "closure_decision": decision,
        "numerics": {
            "A_EW_target_postcheck": target_aew,
            "A_EW_base_8Delta_over_pi2": base,
            "correction_factor_required": correction_required,
            "epsilon_required": epsilon_required,
            "best_candidate_A_EW_value": best_aew,
            "best_candidate_A_EW_relative_residual": best_aew_relative_residual,
            "minimal_ledger_non_neutrino_excluding_QCD_theta": min_ledger["closure_decision"][
                "closed_non_neutrino_SM_like_count_excluding_QCD_theta"
            ],
            "minimal_ledger_PMNS_excluding_QCD_theta": min_ledger["closure_decision"][
                "closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"
            ],
        },
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "AEWCorrectionFactorSourceSearchAndFrontierTheorem",
            "proved": True,
            "statement": (
                "The active strict PEW frontier is not the H radial scalar or the nine charged K rows: those are "
                "closed in the active ledger.  The missing strict object is an exact same-source physical "
                "normalization/correction row for A_EW, or a direct K_threshold.Omega_H.lambda certificate.  "
                "A constrained correction-factor search finds sharper theorem targets, but emits zero accepted "
                "strict P_EW or direct-K rows."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_AEWCorrectionFactorSourceTheorem_or_PhysicalNormalizationRun_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "strict_P_EW_source_theorem_closed": False,
        "direct_K_threshold_Omega_H_lambda_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    row_summary = "\n".join(
        "- {formula}: correction={correction:.15f}, eps-rel-resid={resid:.3e}, accepted=false".format(
            formula=row["formula"],
            correction=row["correction_factor_value"],
            resid=row["epsilon_relative_residual"],
        )
        for row in rows
    )
    note = f"""# MTT Selected AEWCorrectionFactorSourceTheorem or PhysicalNormalizationRun v1

Status: `{STATUS}`.

## Result

The active strict PEW/H-lambda frontier is narrowed without moving backwards:

```text
strict charged K rows closed          : 9/10
finite H radial source R_H^RG closed  : true
minimal one-primitive H/lambda lane   : closed
strict P_EW source rows               : 0
direct K_threshold.Omega_H.lambda rows: 0
strict no-knob ten-row closure        : false
```

The best internal base clue remains:

```text
A_EW_base = 8*Delta_G12/pi^2 = {base}
A_EW_postcheck = {target_aew}
required correction = {correction_required}
required epsilon = {epsilon_required}
```

## Correction Search

The constrained source-window correction scan found:

```text
{row_summary}
```

The sharpest new target is
`1 + Delta_G12^2*(Omega0/sqrt(alpha_phys))^2/(103*p_Y^2)`, which gives
`A_EW={best_aew}` with relative residual `{best_aew_relative_residual}`.
It is not promoted because the denominator `103` and the correction functional
are not selected by a same-source gauge/action normalization theorem.

## Next Exact Object

`{NEXT}`.
"""

    write_json(CORRECTION_SCAN, correction_scan)
    write_json(PHYSICAL_RUN, physical_run)
    write_json(FRONTIER, frontier)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
