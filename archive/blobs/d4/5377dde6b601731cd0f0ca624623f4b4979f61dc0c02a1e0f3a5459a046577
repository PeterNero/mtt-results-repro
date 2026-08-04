"""Build accepted common-scale Yukawa/Higgs values or profile-likelihood execution gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALUES = PACKET_DIR / "versioned_common_scale_yukawa_higgs_values.packet.json"
PROFILE = PACKET_DIR / "profile_likelihood_execution_summary.packet.json"
PROMOTION = PACKET_DIR / "precision_promotion_gate.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_value_profile_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AcceptedCommonScaleYukawaHiggsValues_or_ProfileLikelihoodExecution_v1.md"

PREVIOUS = DATA / "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_yukawamagnitudergclosure_or_finaltruesmequivalenceaudit"
    / "next_cutset_after_final_value_audit.packet.json"
)
FIRSTPASS = (
    DATA
    / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket"
    / "accepted_firstpass_common_scale_yukawa_higgs_values.packet.json"
)
THRESHOLD_POLICY = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
)
DIAGONAL_PROFILE = (
    DATA
    / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
    / "diagonal_profile_likelihood_execution.packet.json"
)
DIAGONAL_GATE = (
    DATA
    / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
    / "updated_true_equivalence_gate_after_diagonal_profile.packet.json"
)
FORMULA = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "buttazzo_boundary_formula_replay.packet.json"
)
LITERATURE = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "external_literature_rg_benchmark_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_ACCEPTEDCOMMONSCALEYUKAWAHIGGSVALUES_OR_PROFILELIKELIHOODEXECUTION_"
    "BUILT_VERSIONED_VALUES_AND_DIAGONAL_PROFILE_TRUE_EQUIVALENCE_OPEN"
)
NEXT = "MTT_Selected_CorrelatedThresholdProfileMatrix_or_YukawaHiggsPrecisionPromotion_v1"


Matrix = list[list[list[float]]]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing value/profile execution sources: " + ", ".join(missing))


def cabs(pair: list[float]) -> float:
    return math.hypot(float(pair[0]), float(pair[1]))


def diag_abs(matrix: Matrix) -> list[float]:
    return [cabs(matrix[i][i]) for i in range(len(matrix))]


def frob(matrix: Matrix) -> float:
    return math.sqrt(sum(cabs(item) ** 2 for row in matrix for item in row))


def offdiag_frob(matrix: Matrix) -> float:
    return math.sqrt(
        sum(cabs(matrix[i][j]) ** 2 for i in range(len(matrix)) for j in range(len(matrix[i])) if i != j)
    )


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CUTSET,
        FIRSTPASS,
        THRESHOLD_POLICY,
        DIAGONAL_PROFILE,
        DIAGONAL_GATE,
        FORMULA,
        LITERATURE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    firstpass = load(FIRSTPASS)
    threshold = load(THRESHOLD_POLICY)
    diagonal = load(DIAGONAL_PROFILE)
    diagonal_gate = load(DIAGONAL_GATE)
    formula = load(FORMULA)
    literature = load(LITERATURE)

    accepted = firstpass["accepted_values"]
    yu = accepted["Y_u_MZ_firstpass"]
    yd = accepted["Y_d_MZ_firstpass"]
    ye = accepted["Y_e_MZ_firstpass"]
    lam = float(accepted["lambda_H_MZ_firstpass"])

    value_packet = {
        "schema": "MTTVersionedCommonScaleYukawaHiggsValues.v1",
        "status": "VERSIONED_FIRSTPASS_COMMON_SCALE_VALUES_EMITTED_PROFILE_INPUT_ONLY",
        "source_packet": rel(FIRSTPASS),
        "reference_scale": firstpass["acceptance_convention"]["target_scale"],
        "reference_scheme": firstpass["acceptance_convention"]["target_scheme"],
        "transport_convention": firstpass["acceptance_convention"],
        "values": {
            "Y_u_MZ_firstpass": yu,
            "Y_d_MZ_firstpass": yd,
            "Y_e_MZ_firstpass": ye,
            "lambda_H_MZ_firstpass": lam,
        },
        "derived_magnitudes": {
            "diag_abs_Y_u": diag_abs(yu),
            "diag_abs_Y_d": diag_abs(yd),
            "diag_abs_Y_e": diag_abs(ye),
            "frob_Y_u": frob(yu),
            "frob_Y_d": frob(yd),
            "frob_Y_e": frob(ye),
            "offdiag_frob_Y_u": offdiag_frob(yu),
            "offdiag_frob_Y_d": offdiag_frob(yd),
            "offdiag_frob_Y_e": offdiag_frob(ye),
            "lambda_H": lam,
        },
        "acceptance_evidence": firstpass["acceptance_evidence"],
        "accepted_as_versioned_common_scale_candidate_values": True,
        "accepted_for_SM_parity": firstpass["accepted_for_SM_parity"],
        "accepted_for_profile_execution_input": True,
        "accepted_for_true_precision_equivalence": False,
        "accepted_as_no_knob_MTT_prediction": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(VALUES, value_packet)

    profile_packet = {
        "schema": "MTTProfileLikelihoodExecutionSummary.v1",
        "status": "DIAGONAL_PROFILE_EXECUTED_COARSE_PASS_FULL_CORRELATED_PROFILE_OPEN",
        "diagonal_profile_source": rel(DIAGONAL_PROFILE),
        "literature_reference": literature["source"],
        "comparison_target": diagonal["comparison_target"],
        "boundary_formula_source": rel(FORMULA),
        "current_repo_input_variant": formula["current_repo_input_variant"],
        "profile_summary": {
            "chi2_diagonal": diagonal["chi2_diagonal"],
            "degrees_of_freedom": diagonal["degrees_of_freedom"],
            "reduced_chi2_diagonal": diagonal["reduced_chi2_diagonal"],
            "max_abs_pull": diagonal["max_abs_pull"],
            "passes_coarse_diagonal_profile": diagonal["passes_coarse_diagonal_profile"],
            "accepted_as_full_covariance_profile": diagonal["accepted_as_full_covariance_profile"],
        },
        "profile_rows": diagonal["profile_rows"],
        "what_this_closes": {
            "versioned_value_packet_available_for_profile_execution": True,
            "diagonal_profile_likelihood_executed": True,
            "coarse_profile_pass_recorded": diagonal["passes_coarse_diagonal_profile"],
        },
        "what_this_does_not_close": {
            "published_or_reconstructed_full_correlated_profile": True,
            "non_gaussian_profile_likelihood": True,
            "multi_loop_threshold_convention_values": True,
            "precision_threshold_and_mass_scheme_values": True,
            "true_SM_equivalence": True,
        },
        "accepted_for_true_precision_equivalence": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(PROFILE, profile_packet)

    promotion_tests = {
        "finite_firstpass_values_emitted": firstpass["acceptance_evidence"]["finite_values_emitted"],
        "internal_RK_convergence_closed": firstpass["acceptance_evidence"]["internal_RK_convergence_closed"],
        "versioned_common_scale_candidate_values_emitted": True,
        "coarse_diagonal_profile_passes": diagonal["passes_coarse_diagonal_profile"],
        "external_literature_benchmark_present": literature["accepted_as_external_literature_benchmark_reference"],
        "threshold_matching_values_emitted": threshold["values_promotable_now"],
        "mass_scheme_conversion_values_emitted": threshold["values_promotable_now"],
        "full_correlated_covariance_profile_emitted": diagonal["accepted_as_full_covariance_profile"],
        "multi_loop_threshold_convention_values_emitted": False,
        "no_knob_MTT_source_derivation_of_values": False,
    }
    hard_failures = [
        key
        for key, value in promotion_tests.items()
        if key
        in {
            "threshold_matching_values_emitted",
            "mass_scheme_conversion_values_emitted",
            "full_correlated_covariance_profile_emitted",
            "multi_loop_threshold_convention_values_emitted",
            "no_knob_MTT_source_derivation_of_values",
        }
        and value is False
    ]
    can_promote_true_precision = not hard_failures
    promotion_packet = {
        "schema": "MTTPrecisionPromotionGate.v1",
        "status": "PROMOTION_TEST_EXECUTED_TRUE_PRECISION_PROMOTION_REJECTED",
        "previous_required_artifact": previous_cutset["recommended_next"]["artifact"],
        "promotion_tests": promotion_tests,
        "hard_failures": hard_failures,
        "promotion_decision": {
            "accepted_as_versioned_common_scale_candidate_values": True,
            "accepted_for_SM_parity": firstpass["accepted_for_SM_parity"],
            "accepted_for_diagonal_profile_execution": True,
            "accepted_for_true_precision_equivalence": can_promote_true_precision,
            "accepted_as_full_SM_no_knob_closure": False,
        },
        "reason": (
            "The executable value/profile layer now exists and passes the coarse diagonal profile sanity check. "
            "It cannot be promoted to true precision SM equivalence because threshold matching, mass-scheme "
            "conversion, full correlated profile likelihood, multi-loop convention values, and no-knob value "
            "source derivation are still absent."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION, promotion_packet)

    next_cutset = {
        "schema": "MTTNextCutsetAfterValueProfileExecution.v1",
        "status": "VALUE_PROFILE_LAYER_EXECUTED_CORRELATED_THRESHOLD_PROMOTION_OPEN",
        "closed_now": [
            "versioned common-scale first-pass Yukawa/Higgs matrix packet emitted",
            "derived Yukawa/Higgs magnitudes emitted for audit and profile use",
            "diagonal profile likelihood execution attached to the same value packet",
            "precision promotion test executed without target fitting",
        ],
        "still_open": [
            "threshold matching values",
            "mass-scheme conversion values",
            "full correlated covariance/profile likelihood",
            "multi-loop threshold convention table",
            "no-knob MTT source derivation of Yukawa/Higgs magnitudes",
            "true SM equivalence and full no-knob closure",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The value/profile layer is now executable. The next real promotion requires a correlated "
                "threshold/profile matrix or an accepted precision-promotion theorem that supplies the missing "
                "threshold, mass-scheme, covariance, and multi-loop convention rows."
            ),
        },
        "guardrails_inherited": diagonal_gate["guardrails"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedAcceptedCommonScaleYukawaHiggsValuesOrProfileLikelihoodExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "versioned_common_scale_yukawa_higgs_values": rel(VALUES),
            "profile_likelihood_execution_summary": rel(PROFILE),
            "precision_promotion_gate": rel(PROMOTION),
            "next_cutset_after_value_profile_execution": rel(NEXT_CUTSET),
        },
        "theorem": {
            "name": "VersionedValueProfileExecutionAndPromotionGateTheorem",
            "proved": True,
            "statement": (
                "The selected first-pass common-scale Yukawa/Higgs matrices can be promoted to a versioned "
                "candidate value packet and used in a diagonal profile execution. This closes the existence "
                "of an executable value/profile layer. It does not close true precision SM equivalence, because "
                "the same audit rejects promotion without threshold matching, mass-scheme conversion, full "
                "correlated likelihood, multi-loop convention values, and no-knob value-source derivation."
            ),
        },
        "what_closes_now": {
            "versioned_common_scale_Yu_Yd_Ye_lambdaH_packet_emitted": True,
            "derived_yukawa_higgs_magnitudes_emitted": True,
            "diagonal_profile_execution_attached": True,
            "coarse_diagonal_profile_passes": diagonal["passes_coarse_diagonal_profile"],
            "precision_promotion_gate_executed": True,
        },
        "what_remains_open": {
            "threshold_matching_values": True,
            "mass_scheme_conversion_values": True,
            "full_correlated_covariance_profile": True,
            "multi_loop_threshold_convention_values": True,
            "no_knob_Yukawa_Higgs_value_source_derivation": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "value_profile_execution_layer_closed": True,
            "accepted_common_scale_values_for_SM_parity": firstpass["accepted_for_SM_parity"],
            "accepted_common_scale_values_for_true_precision": False,
            "full_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_AcceptedCommonScaleYukawaHiggsValues_or_ProfileLikelihoodExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected AcceptedCommonScaleYukawaHiggsValues or ProfileLikelihoodExecution v1

Status: `{STATUS}`.

This artifact emits a versioned first-pass common-scale value packet:

```text
diag |Y_u(M_Z)| = {value_packet["derived_magnitudes"]["diag_abs_Y_u"]}
diag |Y_d(M_Z)| = {value_packet["derived_magnitudes"]["diag_abs_Y_d"]}
diag |Y_e(M_Z)| = {value_packet["derived_magnitudes"]["diag_abs_Y_e"]}
lambda_H(M_Z)  = {lam}
```

It also attaches the diagonal profile execution:

```text
reduced chi2 = {diagonal["reduced_chi2_diagonal"]}
max pull     = {diagonal["max_abs_pull"]}
coarse pass  = {diagonal["passes_coarse_diagonal_profile"]}
```

Promotion decision:

```text
accepted as versioned value/profile packet: true
accepted for SM-parity replay: {firstpass["accepted_for_SM_parity"]}
accepted for true precision equivalence: false
true SM equivalence: open
```

This does not promote first-pass values to true precision equivalence. The missing
rows are threshold matching, mass-scheme conversion, full correlated profile
likelihood, multi-loop convention values, and no-knob value-source derivation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
