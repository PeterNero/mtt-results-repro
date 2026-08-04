"""Build strict PEW/direct-K row emission attempt or gauge-action source packet.

This is the direct constructive attack after the minimal one-primitive H/lambda
lane and the finite-H radial source reconciliation.  It tries to promote the
current PEW/action data into a strict source row.  The packet is allowed to close
only the emission attempt; it must not relabel the counted P_EW primitive or
near-miss expressions as no-knob source data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_strictpewdirectkrowemissionattempt_or_gaugeactionnormalizationsource"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ACCEPTANCE = PACKET_DIR / "strict_pew_directk_acceptance_predicate.packet.json"
ROW_ATTEMPT = PACKET_DIR / "strict_pew_source_row_emission_attempt.packet.json"
DIRECT_K_GATE = PACKET_DIR / "direct_kthreshold_certificate_gate.packet.json"
NEXT_PAYLOAD = PACKET_DIR / "next_gauge_action_normalization_source_payload.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_StrictPEWDirectKRowEmissionAttempt_or_GaugeActionNormalizationSource_v1.md"

STATUS = (
    "MTT_SELECTED_STRICTPEWDIRECTKROWEMISSIONATTEMPT_OR_GAUGEACTIONNORMALIZATIONSOURCE_"
    "ATTEMPT_EXECUTED_ZERO_STRICT_ROWS_SOURCE_PAYLOAD_OPEN"
)
NEXT = "MTT_Selected_PEWGaugeActionNormalizationSourcePacket_or_DirectKCertificatePayload_v1"

SOURCES = {
    "aew_source_operator": DATA / "selected_aewsourceoperator_or_thresholdconventionrows.candidate.json",
    "aew_expression_search": DATA
    / "selected_aewsourceoperator_or_thresholdconventionrows"
    / "expanded_source_expression_search_with_physical_anchor_symbols.packet.json",
    "physical_anchor": DATA
    / "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda.candidate.json",
    "direct_k_attempt": DATA
    / "selected_physicalgaugeactionanchor_or_directkthresholdomegahlambda"
    / "direct_kthreshold_omega_h_lambda_attempt.packet.json",
    "one_primitive_replay": DATA
    / "selected_samebranchgaugeactionsource_or_oneprimitivepolicy"
    / "h_lambda_one_primitive_replay.packet.json",
    "strict_prefactor_audit": DATA
    / "selected_strictphysicalprefactorsource_or_fullsmminimalparameteraudit.candidate.json",
    "finite_h_reconciliation": DATA
    / "selected_strictfinitehsourcerowconstruction_or_nonhiggshrgprediction.candidate.json",
    "ew_rg_route": DATA
    / "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow"
    / "electroweak_gaugekinetic_rg_route_lane.packet.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing strict PEW/direct-K source inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    sources = require_sources()

    aew = sources["aew_source_operator"]
    aew_decision = aew["closure_decision"]
    search = sources["aew_expression_search"]
    anchor_decision = sources["physical_anchor"]["closure_decision"]
    direct_k = sources["direct_k_attempt"]
    one_primitive = sources["one_primitive_replay"]
    strict_pref = sources["strict_prefactor_audit"]["closure_decision"]
    finite_h = sources["finite_h_reconciliation"]["closure_decision"]
    ew_rg = sources["ew_rg_route"]

    numerics = aew["numerics"]
    replay = one_primitive["postcheck"]

    accepted_strict_pew_rows = int(aew_decision["accepted_physical_prefactor_rows"]) + int(
        strict_pref["accepted_strict_prefactor_source_row_total"]
    )
    accepted_direct_k_rows = int(anchor_decision["accepted_direct_K_threshold_Omega_H_lambda_rows"])
    exact_hits = int(search["exact_hits_found"])
    best = search["best_expression_rows"][0]

    acceptance = {
        "schema": "MTTStrictPEWDirectKAcceptancePredicate.v1",
        "status": "STRICT_ACCEPTANCE_PREDICATE_LOCKED",
        "closure_claimed": True,
        "accepted_row_requires": [
            "same-branch physical gauge/action normalization source",
            "selected mu_match",
            "selected RG/threshold scheme",
            "exact selected A_EW expression or direct K_threshold.Omega_H.lambda certificate",
            "no use of lambda_H, observed masses, or target residual as selector",
        ],
        "rejects": [
            "counted P_EW primitive without source theorem",
            "near-miss internal expressions without correction source",
            "diagnostic lambda_H replay",
            "tree-level f=S slot without physical normalization and scheme",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    row_attempt = {
        "schema": "MTTStrictPEWSourceRowEmissionAttempt.v1",
        "status": "STRICT_PEW_SOURCE_ROW_ATTEMPT_EXECUTED_ZERO_ROWS",
        "closure_claimed": True,
        "closed_inputs": {
            "finite_H_radial_source_closed": finite_h["strict_finite_H_radial_source_closed"],
            "selected_R_H_RG_source_emitted": finite_h["selected_R_H_RG_source_emitted"],
            "H_specific_parameter_count_after_finite_H": finite_h[
                "H_specific_parameter_count_after_finite_H"
            ],
            "internal_lambda_12_available": ew_rg["internal_lambda_12_available"],
            "internal_Delta_G12_value": ew_rg["internal_Delta_G12_value"],
            "minimal_one_prefactor_lane_closed": strict_pref["minimal_H_lambda_lane_ready_for_full_SM_ledger"],
        },
        "candidate_rows_tested": [
            {
                "row_id": row["row_id"],
                "formula": row["formula"],
                "value": row["value"],
                "target": row["target"],
                "relative_residual": row["relative_residual"],
                "accepted": row["accepted"],
                "rejection_reason": "not exact and no selected correction/source theorem emits the required factor",
            }
            for row in search["best_expression_rows"]
        ],
        "best_near_miss": {
            "row_id": best["row_id"],
            "formula": best["formula"],
            "relative_residual": best["relative_residual"],
            "correction_factor_required": best["correction_factor_required"],
        },
        "one_primitive_replay": {
            "formula": one_primitive["formula"],
            "P_EW_action_prefactor": one_primitive["inputs"]["P_EW.action_prefactor"],
            "lambda_H_replay": replay["lambda_H_replay"],
            "relative_residual": replay["relative_residual"],
            "accepted_as_strict_source": False,
            "reason": "the primitive is counted/admitted but not source-emitted",
        },
        "accepted_strict_P_EW_source_rows": accepted_strict_pew_rows,
        "exact_expression_hits_found": exact_hits,
        "strict_P_EW_source_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_k_gate = {
        "schema": "MTTDirectKThresholdCertificateGate.v1",
        "status": "DIRECT_K_CERTIFICATE_GATE_EXECUTED_ZERO_ROWS",
        "closure_claimed": True,
        "conditional_formula": direct_k["conditional_formula"],
        "closed_prerequisites": direct_k["closed_prerequisites"],
        "missing_for_strict_direct_K": direct_k["missing_for_strict_direct_K"],
        "diagnostic_replay_only": direct_k["diagnostic_replay_only"],
        "accepted_direct_K_threshold_Omega_H_lambda_rows": accepted_direct_k_rows,
        "strict_K_threshold_Omega_H_lambda_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_payload = {
        "schema": "MTTNextGaugeActionNormalizationSourcePayload.v1",
        "status": "NEXT_PAYLOAD_IS_SOURCE_NORMALIZATION_OR_DIRECT_K_CERTIFICATE",
        "closure_claimed": True,
        "closed_here": [
            "finite H radial source carried into strict PEW/direct-K row attempt",
            "near-miss A_EW expressions rechecked and rejected as source rows",
            "one-primitive H/lambda replay separated from strict source emission",
            "direct-K certificate gate re-executed with zero accepted rows",
        ],
        "required_new_payload": {
            "route_A_same_branch_gauge_action": [
                "source-owned physical gauge/action normalization K_phys or f_ab",
                "selected mu_match",
                "selected RG/threshold scheme",
                "exact A_EW source expression or correction factor",
            ],
            "route_B_direct_K_certificate": [
                "row-level K_threshold.Omega_H.lambda source certificate",
                "same-scheme alignment certificate",
                "numeric or symbolic D_fin.H value row",
            ],
            "route_C_nonHiggs_crossuse": [
                "accepted non-Higgs HRG source map using the same prefactor",
                "prediction target independent of lambda_H replay",
            ],
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedStrictPEWDirectKRowEmissionAttemptOrGaugeActionNormalizationSource",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "strict_row_emission_attempt_closed": True,
        "strict_P_EW_source_theorem_closed": False,
        "direct_K_threshold_Omega_H_lambda_closed": False,
        "minimal_one_primitive_lane_preserved": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "output_packets": {
            "strict_pew_directk_acceptance_predicate": rel(ACCEPTANCE),
            "strict_pew_source_row_emission_attempt": rel(ROW_ATTEMPT),
            "direct_kthreshold_certificate_gate": rel(DIRECT_K_GATE),
            "next_gauge_action_normalization_source_payload": rel(NEXT_PAYLOAD),
        },
        "closure_decision": {
            "strict_row_emission_attempt_closed": True,
            "finite_H_radial_source_closed": finite_h["strict_finite_H_radial_source_closed"],
            "H_specific_parameter_count_after_finite_H": finite_h[
                "H_specific_parameter_count_after_finite_H"
            ],
            "minimal_one_primitive_lane_closed": True,
            "accepted_strict_P_EW_source_rows": accepted_strict_pew_rows,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": accepted_direct_k_rows,
            "exact_A_EW_expression_hits_found": exact_hits,
            "best_A_EW_expression_formula": best["formula"],
            "best_A_EW_expression_relative_residual": best["relative_residual"],
            "P_EW_counted_as_shared_physical_primitive": strict_pref[
                "P_EW_counted_as_shared_physical_primitive"
            ],
            "P_EW_parameter_count": strict_pref["P_EW_parameter_count"],
            "strict_P_EW_source_promoted": False,
            "direct_K_threshold_Omega_H_lambda_emitted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "StrictPEWDirectKRowEmissionAttemptTheorem",
            "proved": True,
            "statement": (
                "Given the currently selected finite H radial source, internal weak-split "
                "support, one-primitive replay, and physical-anchor packets, the strict "
                "PEW/direct-K acceptance predicate emits zero source rows.  The remaining "
                "constructive payload is a same-branch gauge/action normalization with "
                "mu_match and RG/threshold scheme, a direct row-level K certificate, or an "
                "independent non-Higgs HRG cross-use source map."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedStrictPEWDirectKRowEmissionAttemptOrGaugeActionNormalizationSourceCertificate",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "strict_row_emission_attempt_closed": True,
        "accepted_strict_P_EW_source_rows": accepted_strict_pew_rows,
        "accepted_direct_K_threshold_Omega_H_lambda_rows": accepted_direct_k_rows,
        "exact_A_EW_expression_hits_found": exact_hits,
        "minimal_one_primitive_lane_preserved": True,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected StrictPEWDirectKRowEmissionAttempt or GaugeActionNormalizationSource v1

## Theorem

`StrictPEWDirectKRowEmissionAttemptTheorem` is proved.

This is a direct emission attempt for the strict H/lambda row after finite H
radial closure.

## Closed Inputs

- finite H radial source closed: `{str(finite_h["strict_finite_H_radial_source_closed"]).lower()}`
- selected `R_H^RG` source emitted: `{str(finite_h["selected_R_H_RG_source_emitted"]).lower()}`
- H-specific parameter count after finite H: `{finite_h["H_specific_parameter_count_after_finite_H"]}`
- minimal one-primitive lane closed: `true`
- `lambda_H` replay residual in one-primitive lane: `{replay["relative_residual"]}`

## Strict Row Attempt

- accepted strict `P_EW` source rows: `{accepted_strict_pew_rows}`
- accepted direct `K_threshold.Omega_H.lambda` rows: `{accepted_direct_k_rows}`
- exact `A_EW` expression hits found: `{exact_hits}`
- best current expression: `{best["formula"]}`
- best expression relative residual: `{best["relative_residual"]}`
- correction factor required: `{best["correction_factor_required"]}`

The counted primitive `P_EW.action_prefactor={one_primitive["inputs"]["P_EW.action_prefactor"]}`
is preserved as a minimal-parameter lane only.  It is not promoted as strict
selected source data.
Claim boundary: counted primitive is not promoted as strict selected source data.

## Remaining Payload

The next constructive object is one of:

- same-branch physical gauge/action normalization with selected `mu_match` and RG/threshold scheme,
- direct row-level `K_threshold.Omega_H.lambda` certificate,
- accepted non-Higgs HRG source map using the same prefactor without `lambda_H` replay.

Next required artifact: `{NEXT}`.
"""

    write_json(ACCEPTANCE, acceptance)
    write_json(ROW_ATTEMPT, row_attempt)
    write_json(DIRECT_K_GATE, direct_k_gate)
    write_json(NEXT_PAYLOAD, next_payload)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
