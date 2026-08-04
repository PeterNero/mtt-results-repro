"""Build selected T_scheme/lambda_H source-row closure attempt packet.

This artifact works immediately after the charged retarded-overlap
spectral-pairing lemma.  It tests the clean neutral lane

    T_scheme_i = 1

against the already emitted strict charged L_rowlocal rows.  The trial is
useful because it shows that nine charged K_threshold rows would follow
mechanically from the combined product grammar if a selected neutral
T_scheme theorem existed.  The trial is not promoted as selected source data:
no same-branch source currently emits the neutral scheme rows, and the H-sector
lambda_H payload is still absent.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
READINESS = PACKET_DIR / "post_charged_lrowlocal_threshold_readiness_recheck.packet.json"
IDENTITY_TRIAL = PACKET_DIR / "identity_tscheme_neutral_trial.packet.json"
LAMBDA_GATE = PACKET_DIR / "lambda_h_payload_gate_after_charged_lrows.packet.json"
K_GATE = PACKET_DIR / "kthreshold_gate_after_tscheme_lambdah_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_tscheme_lambdah_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TSchemeLambdaHSourceRows_or_KThresholdRowClosure_v1.md"

PREVIOUS = DATA / "selected_retardedoverlapspectralpairinglemma_or_independentquadraturevalues.candidate.json"
CHARGED_ROWS = (
    DATA
    / "selected_retardedoverlapspectralpairinglemma_or_independentquadraturevalues"
    / "charged_strict_lrowlocal_rows_after_pairing_lemma.packet.json"
)
PREVIOUS_K_GATE = (
    DATA
    / "selected_retardedoverlapspectralpairinglemma_or_independentquadraturevalues"
    / "kthreshold_gate_after_charged_lrowlocal_closure.packet.json"
)
THRESHOLD_SOURCE_GATE = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "threshold_scheme_source_gate.packet.json"
)
COMBINED_K_CONTRACT = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "combined_threshold_kernel_k_row_contract.packet.json"
)
STEP55 = DATA / "selected_step55_thresholdmass_admittedrow_import_or_profile_noknob_frontier.candidate.json"
STEP56 = DATA / "selected_step56_diagonalprofile_import_or_noknob_frontier.candidate.json"
SAMEBRANCH = DATA / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction.candidate.json"
STEP69 = DATA / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution.candidate.json"
STEP70 = DATA / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier.candidate.json"

STATUS = (
    "MTT_SELECTED_TSCHEMELAMBDAH_SOURCEROWS_OR_KTHRESHOLDROWCLOSURE_"
    "BUILT_IDENTITY_TRIAL_NEEDS_SOURCE_THEOREM_LAMBDAH_OPEN"
)
NEXT = "MTT_Selected_NeutralTSchemeSourcePrinciple_or_LambdaHSectorPayload_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing T_scheme/lambda_H source-row inputs: " + ", ".join(missing))


def charged_identity_rows(charged_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in charged_rows:
        omega_id = f"Omega_{row['sector']}.gen{row['generation']}"
        l_value = float(row["selected_strict_L_rowlocal_value"])
        rows.append(
            {
                "omega_id": omega_id,
                "sector": row["sector"],
                "generation": row["generation"],
                "strict_L_rowlocal_row_id": row["row_id"],
                "selected_strict_L_rowlocal_value": l_value,
                "identity_T_scheme_candidate_value": 1.0,
                "conditional_K_threshold_value_if_identity_selected": l_value,
                "formula_if_selected": "K_threshold_i = L_rowlocal_i * 1",
                "accepted_as_selected_T_scheme_source_row": False,
                "accepted_as_selected_K_threshold_row": False,
                "identity_T_scheme_selected": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return rows


def contract_row_by_omega(contract_rows: list[dict[str, Any]], omega_id: str) -> dict[str, Any] | None:
    for row in contract_rows:
        if row["omega_id"] == omega_id:
            return row
    return None


def k_attempt_rows(
    previous_gate_rows: list[dict[str, Any]],
    identity_rows: list[dict[str, Any]],
    contract_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_omega = {row["omega_id"]: row for row in identity_rows}
    rows: list[dict[str, Any]] = []
    for row in previous_gate_rows:
        omega_id = row["omega_id"]
        identity_row = by_omega.get(omega_id)
        contract = contract_row_by_omega(contract_rows, omega_id) or {}
        charged = identity_row is not None
        rows.append(
            {
                "omega_id": omega_id,
                "combined_kernel_row_id": row["combined_kernel_row_id"],
                "sector": row["sector"],
                "generation_or_lambda": row["generation_or_lambda"],
                "combined_kernel_definition": contract.get(
                    "definition", "K_threshold_i = L_rowlocal_i * T_scheme_i"
                ),
                "strict_L_rowlocal_available": bool(row["selected_strict_L_rowlocal_available"]),
                "selected_strict_L_rowlocal_value": row["selected_strict_L_rowlocal_value"],
                "identity_T_scheme_candidate_available": charged,
                "identity_T_scheme_candidate_value": 1.0 if charged else None,
                "identity_T_scheme_selected": False,
                "conditional_K_threshold_value_if_identity_selected": (
                    identity_row["conditional_K_threshold_value_if_identity_selected"] if charged else None
                ),
                "selected_T_scheme_source_row_emitted": False,
                "selected_lambda_H_payload_emitted": False if row["sector"] == "H" else None,
                "selected_K_threshold_row_emitted": False,
                "accepted_as_no_knob_source_row": False,
                "product_sufficient_for_scalar_execution_if_selected": bool(
                    contract.get("product_sufficient_for_scalar_execution", True)
                ),
                "split_L_T_required_before_scalar_execution": bool(
                    contract.get("split_L_T_required_before_scalar_execution", False)
                ),
                "blocking_reasons": (
                    [
                        "strict charged L_rowlocal row is available",
                        "neutral identity T_scheme is only a trial, not a selected source theorem",
                        "therefore the conditional K value is not an accepted source row",
                    ]
                    if charged
                    else [
                        "no charged L_rowlocal row applies to H/lambda",
                        "selected lambda_H H-sector payload is not emitted",
                        "neutral identity T_scheme is not selected for the H slot",
                    ]
                ),
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        CHARGED_ROWS,
        PREVIOUS_K_GATE,
        THRESHOLD_SOURCE_GATE,
        COMBINED_K_CONTRACT,
        STEP55,
        STEP56,
        SAMEBRANCH,
        STEP69,
        STEP70,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    charged = load(CHARGED_ROWS)
    previous_k_gate = load(PREVIOUS_K_GATE)
    threshold_source_gate = load(THRESHOLD_SOURCE_GATE)
    combined_contract = load(COMBINED_K_CONTRACT)
    step55 = load(STEP55)
    step56 = load(STEP56)
    samebranch = load(SAMEBRANCH)
    step69 = load(STEP69)
    step70 = load(STEP70)

    identity_rows = charged_identity_rows(charged["rows"])
    contract_rows = combined_contract["combined_kernel_rows"]
    k_rows = k_attempt_rows(previous_k_gate["rows"], identity_rows, contract_rows)
    h_contract = contract_row_by_omega(contract_rows, "Omega_H.lambda") or {}

    readiness = {
        "schema": "MTTPostChargedLRowlocalThresholdReadinessRecheck.v1",
        "status": "CHARGED_LROWS_CLOSED_EXTERNAL_THRESHOLD_SUPPORT_CLASSIFIED_INTERNAL_TSCHEME_OPEN",
        "closure_claimed": True,
        "closed_support": {
            "retarded_overlap_spectral_pairing_lemma_proved": previous["closure_decision"][
                "retarded_overlap_spectral_pairing_lemma_proved"
            ],
            "strict_charged_Lrowlocal_rows_closed": charged["strict_Lrowlocal_row_count_after"] == 9,
            "same_branch_scale_scheme_loop_convention_closed": step55["closure_decision"][
                "same_branch_scale_scheme_loop_convention_closed"
            ],
            "admitted_external_threshold_matching_rows_closed": step55["closure_decision"][
                "threshold_matching_source_rows_closed_at_admitted_external_tier"
            ],
            "admitted_external_mass_scheme_rows_closed": step55["closure_decision"][
                "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"
            ],
            "accepted_diagonal_profile_theorem_closed": step56["closure_decision"][
                "accepted_diagonal_profile_theorem_closed"
            ],
            "combined_K_threshold_product_grammar_closed": combined_contract["closure_claimed"],
            "finite_heat_torsion_prefactor_subsource_closed": step70["closure_decision"][
                "finite_heat_torsion_prefactor_subsource_closed"
            ],
        },
        "support_classification": {
            "external_threshold_mass_profile_rows_are_admitted_replay_not_internal_selectors": True,
            "samebranch_readiness_8_of_9_retained": samebranch["closure_decision"]["Rtheta_readiness_8_of_9"],
            "only_remaining_readiness_blocker_from_step56": step56["closure_decision"][
                "only_remaining_readiness_blocker"
            ],
            "current_threshold_source_gate_status": threshold_source_gate["status"],
        },
        "still_open": {
            "selected_internal_threshold_response_functional_instantiated": False,
            "selected_T_scheme_source_row_count": 0,
            "selected_lambda_H_payload_emitted": False,
            "accepted_selected_K_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    identity_trial = {
        "schema": "MTTIdentityTSchemeNeutralTrial.v1",
        "status": "IDENTITY_TSCHEME_TRIAL_BUILDS_NINE_CONDITIONAL_CHARGED_K_ROWS_BUT_IS_NOT_SELECTED",
        "closure_claimed": True,
        "trial_statement": (
            "If a same-branch neutral threshold-scheme theorem selected T_scheme_i=1 for the charged "
            "u,d,e rows, then the combined product grammar K_threshold_i=L_rowlocal_i*T_scheme_i "
            "would immediately emit nine charged conditional K rows equal to the strict L_rowlocal rows."
        ),
        "trial_formula": "T_scheme_i = 1",
        "preconditions": {
            "strict_charged_Lrowlocal_rows_closed": True,
            "combined_K_threshold_product_grammar_closed": True,
            "observed_values_used": False,
            "target_scoring_used": False,
        },
        "row_count": len(identity_rows),
        "conditional_charged_K_row_count_if_selected": len(identity_rows),
        "selected_T_scheme_source_row_count": 0,
        "identity_T_scheme_selected": False,
        "why_not_selected": [
            "no same-branch source theorem currently emits neutral T_scheme_i=1",
            "Step55 threshold/mass rows are admitted-external replay support, not internal no-knob selectors",
            "Step56 diagonal profile closes a comparison/profile gate, not a threshold-scheme source rule",
            "promoting identity by default would insert an unselected convention as a hidden knob",
        ],
        "rows": identity_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    lambda_gate = {
        "schema": "MTTLambdaHPayloadGateAfterChargedLRows.v1",
        "status": "H_SECTOR_LAMBDAH_PAYLOAD_STILL_OPEN_AFTER_CHARGED_LROWS",
        "closure_claimed": True,
        "omega_id": "Omega_H.lambda",
        "combined_kernel_row_id": h_contract.get("combined_kernel_row_id", "K_threshold.Omega_H.lambda"),
        "known_formula_support": {
            "omega_formula": h_contract.get(
                "omega_formula", "Omega_H.lambda.value = C_HYMthr.H.lambda * epsilon_Theta^(1/3)"
            ),
            "finite_heat_torsion_subfactor_id": h_contract.get("finite_heat_torsion_subfactor_id", "D_fin.H"),
            "prefactor_formula_contract_closed": step69["closure_decision"]["prefactor_formula_contract_closed"],
            "finite_heat_torsion_prefactor_subsource_closed": step70["closure_decision"][
                "finite_heat_torsion_prefactor_subsource_closed"
            ],
        },
        "H_sector_Lrowlocal_available": False,
        "selected_lambda_H_payload_emitted": False,
        "lambda_H_value_row_emitted": False,
        "T_scheme_Omega_H_lambda_source_row_emitted": False,
        "combined_K_threshold_H_lambda_emitted": False,
        "accepted_as_no_knob_source_row": False,
        "blocking_reasons": [
            "charged spectral-pairing lemma covers u,d,e only",
            "no H-sector row-local overlap/quartic payload is emitted",
            "lambda_H remains a threshold/quartic value payload, not a charged L_rowlocal row",
            "external Higgs replay values remain postchecks and cannot select lambda_H",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    k_gate = {
        "schema": "MTTKThresholdGateAfterTSchemeLambdaHAttempt.v1",
        "status": "CONDITIONAL_CHARGED_K_ROWS_BUILT_IDENTITY_TSCHEME_AND_LAMBDAH_NOT_SELECTED",
        "closure_claimed": True,
        "row_count": len(k_rows),
        "strict_charged_Lrowlocal_row_count": charged["strict_Lrowlocal_row_count_after"],
        "identity_T_scheme_trial_row_count": len(identity_rows),
        "conditional_identity_charged_K_rows_if_selected": len(identity_rows),
        "selected_T_scheme_source_row_count": 0,
        "selected_lambda_H_payload_emitted": False,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "rows": k_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterTSchemeLambdaHAttempt.v1",
        "status": "NEXT_FRONTIER_NEUTRAL_TSCHEME_SOURCE_PRINCIPLE_OR_LAMBDAH_PAYLOAD",
        "closure_claimed": True,
        "closed_here": [
            "charged strict L_rowlocal rows imported as closed source rows",
            "admitted external threshold/mass/profile rows reclassified as support, not no-knob selectors",
            "neutral identity T_scheme trial executed without observed data",
            "nine conditional charged K_threshold values built if identity T_scheme is later selected",
            "H/lambda_H obstruction isolated from the charged L_rowlocal closure",
        ],
        "still_open": [
            "selected neutral/identity T_scheme source theorem or nontrivial internal T_scheme rows",
            "selected lambda_H H-sector quartic/threshold payload",
            "ten selected K_threshold rows",
            "strict Omega/lambda_H scalar execution",
            "matrix-level mixing extension and true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTSchemeLambdaHSourceRowsOrKThresholdRowClosure",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "PostChargedLRowlocalTSchemeLambdaHReductionTheorem",
            "proved": True,
            "statement": (
                "After the charged retarded-overlap spectral-pairing lemma, the nine charged "
                "strict L_rowlocal rows are source rows. A neutral identity T_scheme trial shows "
                "that those nine rows would become charged K_threshold rows if T_scheme_i=1 were "
                "selected by a same-branch source theorem. Existing threshold/mass/profile rows "
                "remain admitted replay support rather than internal selectors, and the H-sector "
                "lambda_H payload is still absent. Therefore this packet closes the identity trial "
                "and narrows the remaining source obligations to a selected T_scheme principle or "
                "internal T rows, the lambda_H payload, and then the ten K_threshold rows."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "charged_strict_Lrowlocal_row_count": charged["strict_Lrowlocal_row_count_after"],
            "identity_T_scheme_trial_row_count": len(identity_rows),
            "identity_T_scheme_selected": False,
            "selected_T_scheme_source_row_count": 0,
            "conditional_charged_K_row_count_if_identity_T_scheme_selected": len(identity_rows),
            "selected_lambda_H_payload_emitted": False,
            "accepted_selected_K_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "external_threshold_mass_profile_rows_are_support_not_selectors": True,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "post_charged_lrowlocal_threshold_readiness_recheck": rel(READINESS),
            "identity_tscheme_neutral_trial": rel(IDENTITY_TRIAL),
            "lambda_h_payload_gate_after_charged_lrows": rel(LAMBDA_GATE),
            "kthreshold_gate_after_tscheme_lambdah_attempt": rel(K_GATE),
            "next_cutset_after_tscheme_lambdah_attempt": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedTSchemeLambdaHSourceRowsOrKThresholdRowClosureCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "identity_T_scheme_selected": False,
        "conditional_charged_K_row_count_if_identity_T_scheme_selected": len(identity_rows),
        "selected_T_scheme_source_row_count": 0,
        "selected_lambda_H_payload_emitted": False,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }

    note = f"""# MTT Selected TScheme LambdaH Source Rows or KThreshold Row Closure v1

Status: `{STATUS}`

## What this closes

- strict charged `L_rowlocal` rows imported: `{charged["strict_Lrowlocal_row_count_after"]}`
- neutral identity `T_scheme_i=1` trial rows built: `{len(identity_rows)}`
- conditional charged `K_threshold` rows if identity is later selected: `{len(identity_rows)}`
- admitted external threshold/mass/profile rows classified as support, not source selectors: `true`

## What this does not close

- selected `T_scheme.*` source rows emitted: `false`
- selected `lambda_H` payload emitted: `false`
- accepted selected `K_threshold` rows: `0`
- accepted internal scalar value rows: `0`
- true SM/no-knob equivalence: `false`

## Identity trial result

The trial formula is `T_scheme_i = 1`.  With the charged product grammar
`K_threshold_i = L_rowlocal_i * T_scheme_i`, it would make the following
conditional charged `K_threshold` values:

{chr(10).join(f"- {row['sector']}.gen{row['generation']}: {row['conditional_K_threshold_value_if_identity_selected']:.12f}" for row in identity_rows)}

These are not accepted rows.  The identity scheme still needs a selected
same-branch source theorem, because otherwise `T_scheme=1` would be an
unselected convention hidden inside the proof.

## Current frontier

Next required artifact: `{NEXT}`

Remaining source obligations:

1. selected neutral/identity `T_scheme` theorem or nontrivial internal
   `T_scheme` rows;
2. selected H-sector `lambda_H` quartic/threshold payload;
3. ten selected `K_threshold` rows;
4. strict `Omega/lambda_H` scalar execution;
5. matrix-level mixing extension and true SM equivalence.
"""

    write_json(READINESS, readiness)
    write_json(IDENTITY_TRIAL, identity_trial)
    write_json(LAMBDA_GATE, lambda_gate)
    write_json(K_GATE, k_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
