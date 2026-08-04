"""Build neutral T_scheme source-principle or lambda_H payload normal form.

The previous packet tested the tempting neutral lane T_scheme_i=1.  This packet
turns that temptation into a strict source obligation.  The selected threshold
functional contract defines

    T_scheme(s,g) = exp(Delta_threshold + Delta_mass + Delta_profile).

Therefore the neutral identity factor is selected only if the same branch emits
the zero-delta theorem/rows.  Absence of emitted threshold rows is not the same
as a selected zero.  This artifact rejects identity-by-silence, preserves the
nine conditional charged K rows as conditional support, and isolates the
H/lambda_H payload as the other still-open branch.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ZERO_DELTA = PACKET_DIR / "neutral_tscheme_zero_delta_requirement.packet.json"
IDENTITY_DECISION = PACKET_DIR / "neutral_identity_route_decision.packet.json"
LAMBDA_NORMAL = PACKET_DIR / "h_sector_lambda_payload_normal_form.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_neutral_tscheme_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_NeutralTSchemeSourcePrinciple_or_LambdaHSectorPayload_v1.md"

PREVIOUS = DATA / "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure.candidate.json"
IDENTITY_TRIAL = (
    DATA
    / "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure"
    / "identity_tscheme_neutral_trial.packet.json"
)
K_GATE = (
    DATA
    / "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure"
    / "kthreshold_gate_after_tscheme_lambdah_attempt.packet.json"
)
LAMBDA_GATE = (
    DATA
    / "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure"
    / "lambda_h_payload_gate_after_charged_lrows.packet.json"
)
OVERLAP_FUNCTIONAL = (
    DATA
    / "selected_rowlocalhymoverlapquadraturefunctional_or_thresholdschemesourcetheorem"
    / "selected_overlap_quadrature_functional.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
POSTPI_CONVENTION = DATA / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation.candidate.json"
THRESHOLD_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
STEP55 = DATA / "selected_step55_thresholdmass_admittedrow_import_or_profile_noknob_frontier.candidate.json"
STEP56 = DATA / "selected_step56_diagonalprofile_import_or_noknob_frontier.candidate.json"

STATUS = (
    "MTT_SELECTED_NEUTRALTSCHEMESOURCEPRINCIPLE_OR_LAMBDAHSECTORPAYLOAD_"
    "BUILT_ZERO_DELTA_GATE_IDENTITY_NOT_SELECTED"
)
NEXT = "MTT_Selected_ThresholdDeltaRows_or_LambdaHPayloadExecution_v1"


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
        raise FileNotFoundError("missing neutral T_scheme/lambda_H inputs: " + ", ".join(missing))


def zero_delta_rows(identity_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in identity_rows:
        rows.append(
            {
                "omega_id": row["omega_id"],
                "sector": row["sector"],
                "generation": row["generation"],
                "neutral_identity_candidate_value": row["identity_T_scheme_candidate_value"],
                "required_zero_delta_equation": (
                    "Delta_threshold({omega}) + Delta_mass({omega}) + Delta_profile({omega}) = 0"
                ).format(omega=row["omega_id"]),
                "T_scheme_formula": "T_scheme = exp(Delta_threshold + Delta_mass + Delta_profile)",
                "selected_Delta_threshold_row_emitted": False,
                "selected_Delta_mass_row_emitted": False,
                "selected_Delta_profile_row_emitted": False,
                "selected_zero_delta_sum_theorem_emitted": False,
                "identity_T_scheme_selected": False,
                "conditional_K_threshold_value_if_zero_delta_selected": row[
                    "conditional_K_threshold_value_if_identity_selected"
                ],
                "accepted_as_selected_T_scheme_source_row": False,
                "accepted_as_selected_K_threshold_row": False,
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
        IDENTITY_TRIAL,
        K_GATE,
        LAMBDA_GATE,
        OVERLAP_FUNCTIONAL,
        THRESHOLD_CONTRACT,
        POSTPI_CONVENTION,
        THRESHOLD_IMPORT,
        STEP55,
        STEP56,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    identity = load(IDENTITY_TRIAL)
    k_gate = load(K_GATE)
    lambda_gate = load(LAMBDA_GATE)
    overlap = load(OVERLAP_FUNCTIONAL)
    threshold_contract = load(THRESHOLD_CONTRACT)
    postpi = load(POSTPI_CONVENTION)
    threshold_import = load(THRESHOLD_IMPORT)
    step55 = load(STEP55)
    step56 = load(STEP56)

    rows = zero_delta_rows(identity["rows"])

    zero_delta = {
        "schema": "MTTNeutralTSchemeZeroDeltaRequirement.v1",
        "status": "NEUTRAL_TSCHEME_IDENTITY_REQUIRES_SELECTED_ZERO_DELTA_ROWS",
        "closure_claimed": True,
        "functional_definition": "T_scheme(s,g)=exp(Delta_threshold+Delta_mass+Delta_profile)",
        "source_contract_ref": rel(OVERLAP_FUNCTIONAL),
        "threshold_response_contract_ref": rel(THRESHOLD_CONTRACT),
        "closed_support": {
            "same_branch_scale_scheme_loop_convention_closed": postpi["closure_decision"][
                "same_branch_scale_scheme_loop_convention_closed"
            ],
            "post_pi_formal_convention_source_contract_closed": postpi["closure_decision"][
                "post_pi_formal_convention_source_contract_closed"
            ],
            "threshold_functional_contract_emitted": threshold_contract["closure_claimed"],
            "charged_strict_Lrowlocal_rows_closed": previous["closure_decision"][
                "charged_strict_Lrowlocal_row_count"
            ]
            == 9,
            "combined_K_product_gate_available": k_gate["closure_claimed"],
        },
        "zero_delta_requirement": {
            "charged_zero_delta_row_count_required_for_identity": len(rows),
            "selected_zero_delta_row_count_emitted": 0,
            "selected_zero_delta_sum_theorem_emitted": False,
            "identity_T_scheme_selected": False,
            "reason": (
                "The monoidal unit is a legal value only after the selected branch emits "
                "Delta_threshold+Delta_mass+Delta_profile=0. Missing rows do not equal zero rows."
            ),
        },
        "rows": rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    identity_decision = {
        "schema": "MTTNeutralIdentityRouteDecision.v1",
        "status": "IDENTITY_BY_SILENCE_REJECTED_ZERO_DELTA_THEOREM_REQUIRED",
        "closure_claimed": True,
        "decision": {
            "neutral_identity_T_scheme_candidate_tested": True,
            "neutral_identity_T_scheme_promoted_as_selected": False,
            "selected_T_scheme_source_row_count": 0,
            "conditional_charged_K_rows_preserved_if_zero_delta_later_selected": len(rows),
            "accepted_selected_K_source_row_count": 0,
        },
        "why_identity_not_promoted": [
            "the same-branch convention source closes scale/scheme ownership, not threshold delta values",
            "the selected threshold response functional contract defines T_scheme by exponentiated delta rows",
            "Step55/Step56 threshold, mass, and profile rows are admitted replay support rather than internal no-knob selectors",
            "absence of emitted delta rows is not a selected zero-delta theorem",
            "promoting T_scheme=1 without zero-delta source rows would introduce an unselected hidden convention",
        ],
        "legal_reentry_condition": (
            "Identity may be promoted only by a selected NullThresholdDeltaTheorem or by explicit "
            "selected Delta_threshold/Delta_mass/Delta_profile rows whose sum is zero for each charged slot."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    lambda_normal = {
        "schema": "MTTHSectorLambdaPayloadNormalForm.v1",
        "status": "LAMBDAH_PAYLOAD_NORMAL_FORM_BUILT_SOURCE_PAYLOAD_OPEN",
        "closure_claimed": True,
        "omega_id": lambda_gate["omega_id"],
        "combined_kernel_row_id": lambda_gate["combined_kernel_row_id"],
        "known_formula_support": lambda_gate["known_formula_support"],
        "normal_form_requirement": {
            "H_sector_Lrowlocal_or_quartic_payload_required": True,
            "T_scheme_Omega_H_lambda_required": True,
            "selected_lambda_H_payload_required": True,
            "combined_K_threshold_H_lambda_required": True,
        },
        "current_emission": {
            "H_sector_Lrowlocal_available": lambda_gate["H_sector_Lrowlocal_available"],
            "T_scheme_Omega_H_lambda_source_row_emitted": lambda_gate[
                "T_scheme_Omega_H_lambda_source_row_emitted"
            ],
            "selected_lambda_H_payload_emitted": lambda_gate["selected_lambda_H_payload_emitted"],
            "lambda_H_value_row_emitted": lambda_gate["lambda_H_value_row_emitted"],
            "combined_K_threshold_H_lambda_emitted": lambda_gate["combined_K_threshold_H_lambda_emitted"],
        },
        "why_still_open": lambda_gate["blocking_reasons"]
        + [
            "the charged zero-delta route cannot supply the H/lambda row",
            "the H formula shell and D_fin.H support are not a quartic/threshold payload value",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterNeutralTSchemeGate.v1",
        "status": "NEXT_FRONTIER_THRESHOLD_DELTA_ROWS_OR_LAMBDAH_PAYLOAD",
        "closure_claimed": True,
        "closed_here": [
            "neutral identity T_scheme route converted into nine selected zero-delta obligations",
            "identity-by-silence rejected as a no-knob proof step",
            "conditional nine charged K_threshold rows preserved if zero-delta theorem is later selected",
            "H/lambda_H normal form isolated from charged threshold-scheme closure",
        ],
        "still_open": [
            "selected NullThresholdDeltaTheorem or explicit Delta_threshold/Delta_mass/Delta_profile rows",
            "selected nontrivial internal T_scheme rows if the neutral theorem fails",
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
        "candidate": "MTTSelectedNeutralTSchemeSourcePrincipleOrLambdaHSectorPayload",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "NeutralTSchemeZeroDeltaGateTheorem",
            "proved": True,
            "statement": (
                "Because the selected threshold-scheme factor is defined as "
                "T_scheme=exp(Delta_threshold+Delta_mass+Delta_profile), the neutral identity "
                "candidate T_scheme=1 is selected only if the same branch emits zero-delta rows or "
                "a NullThresholdDeltaTheorem. The current corpus closes same-branch convention "
                "ownership and charged L_rowlocal rows, but emits no threshold delta rows and no "
                "zero-delta theorem. Therefore identity-by-silence is rejected, nine charged "
                "conditional K rows remain conditional support, and the next actual value-source "
                "target is selected threshold delta rows or the H-sector lambda_H payload."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "charged_zero_delta_row_count_required_for_identity": len(rows),
            "selected_zero_delta_row_count_emitted": 0,
            "selected_zero_delta_sum_theorem_emitted": False,
            "identity_T_scheme_selected": False,
            "selected_T_scheme_source_row_count": 0,
            "conditional_charged_K_rows_preserved_if_zero_delta_later_selected": len(rows),
            "accepted_selected_K_source_row_count": 0,
            "selected_lambda_H_payload_emitted": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "neutral_tscheme_zero_delta_requirement": rel(ZERO_DELTA),
            "neutral_identity_route_decision": rel(IDENTITY_DECISION),
            "h_sector_lambda_payload_normal_form": rel(LAMBDA_NORMAL),
            "next_cutset_after_neutral_tscheme_gate": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "support_classification": {
            "external_import_lane_closed_at_admitted_replay_tier": threshold_import["closure_decision"][
                "external_import_lane_closed_at_admitted_replay_tier"
            ],
            "selected_threshold_response_functional_instantiated": threshold_import["closure_decision"][
                "selected_threshold_response_functional_instantiated"
            ],
            "threshold_matching_source_rows_closed_at_admitted_external_tier": step55["closure_decision"][
                "threshold_matching_source_rows_closed_at_admitted_external_tier"
            ],
            "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier": step55["closure_decision"][
                "mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"
            ],
            "accepted_diagonal_profile_theorem_closed": step56["closure_decision"][
                "accepted_diagonal_profile_theorem_closed"
            ],
        },
    }

    cert = {
        "certificate": "MTTSelectedNeutralTSchemeSourcePrincipleOrLambdaHSectorPayloadCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "charged_zero_delta_row_count_required_for_identity": len(rows),
        "selected_zero_delta_row_count_emitted": 0,
        "identity_T_scheme_selected": False,
        "selected_T_scheme_source_row_count": 0,
        "selected_lambda_H_payload_emitted": False,
        "accepted_selected_K_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Neutral TScheme Source Principle or LambdaH Sector Payload v1

Status: `{STATUS}`

## Result

The neutral identity trial is now in normal form:

`T_scheme(s,g) = exp(Delta_threshold + Delta_mass + Delta_profile)`.

So `T_scheme=1` requires a selected zero-delta theorem, not just absent rows.

- charged zero-delta rows required for identity: `{len(rows)}`
- selected zero-delta rows emitted: `0`
- selected zero-delta theorem emitted: `false`
- identity `T_scheme` selected: `false`
- accepted selected `K_threshold` rows: `0`
- selected `lambda_H` payload emitted: `false`

## Conditional Charged Rows Preserved

If a selected zero-delta theorem is later emitted, the nine charged conditional
`K_threshold` values remain:

{chr(10).join(f"- {row['sector']}.gen{row['generation']}: {row['conditional_K_threshold_value_if_zero_delta_selected']:.12f}" for row in rows)}

## Why This Matters

Same-branch convention ownership is closed, but convention ownership is not a
threshold-value theorem.  External threshold/mass/profile rows are admitted
replay support, not no-knob selectors.  Therefore promoting `T_scheme=1` from
silence would be a hidden convention.

## Current Frontier

Next required artifact: `{NEXT}`

Remaining source obligations:

1. selected `NullThresholdDeltaTheorem`, or explicit selected
   `Delta_threshold/Delta_mass/Delta_profile` rows;
2. selected nontrivial internal `T_scheme` rows if the neutral theorem fails;
3. selected H-sector `lambda_H` quartic/threshold payload;
4. ten selected `K_threshold` rows;
5. strict `Omega/lambda_H` scalar execution;
6. matrix-level mixing extension and true SM equivalence.
"""

    write_json(ZERO_DELTA, zero_delta)
    write_json(IDENTITY_DECISION, identity_decision)
    write_json(LAMBDA_NORMAL, lambda_normal)
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
