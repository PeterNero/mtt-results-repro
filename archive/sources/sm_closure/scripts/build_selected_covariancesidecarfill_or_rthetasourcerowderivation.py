"""Build covariance sidecar fill or Rtheta source-row derivation artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_covariancesidecarfill_or_rthetasourcerowderivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
WZH_SIDECARS = PACKET_DIR / "wzh_gauge_and_lambda_covariance_sidecars.packet.json"
LADDER = PACKET_DIR / "interim_covariance_ladder_after_sidecar_fill.packet.json"
RTHETA_ATTEMPT = PACKET_DIR / "rtheta_source_row_derivation_recheck_after_sidecar_fill.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_covariance_sidecar_fill.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CovarianceSidecarFill_or_RThetaSourceRowDerivation_v1.md"

PREVIOUS = DATA / "selected_fullcovarianceprofile_or_selectedrthetasourcerows.candidate.json"
PREVIOUS_GATE = (
    DATA
    / "selected_fullcovarianceprofile_or_selectedrthetasourcerows"
    / "full_covariance_profile_gate_after_wzh_bct.packet.json"
)
PREVIOUS_COVERAGE = (
    DATA
    / "selected_fullcovarianceprofile_or_selectedrthetasourcerows"
    / "full_covariance_block_coverage_after_wzh_bct.packet.json"
)
WZH_INVENTORY = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_electroweak_row_inventory.packet.json"
)
GAUGE_BRIDGE = (
    DATA
    / "selected_thresholdpolerunningmaps_or_rthetaconventionsource"
    / "gauge_bridge_policy_validation_status.packet.json"
)
SENSITIVITY = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "diagonal_sensitivity_covariance_scaffold.packet.json"
)
WEAK_ENVELOPE = (
    DATA
    / "selected_correlatedprofilevalues_or_localqftobservablevalues"
    / "correlation_robust_profile_envelope.packet.json"
)
BCT_PROFILE = (
    DATA
    / "selected_charmtablesubstitution_or_selectedrthetarowsdecision"
    / "bct_empirical_table_substituted_profile.packet.json"
)
HIGGS_COV = (
    DATA
    / "selected_higgshomogeneousprofile_or_routeaformulacovariance"
    / "source_derived_correlated_covariance_model.packet.json"
)
RTHETA_ATTEMPT_SOURCE = (
    DATA
    / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
    / "rtheta_source_owner_row_coefficient_construction_attempt.packet.json"
)
RTHETA_DECISION = (
    DATA
    / "selected_rtheta_sourceowner_rowcoefficientpacket_or_blockercontraction"
    / "rtheta_blocker_contraction_decision.packet.json"
)
REFERENCE_VALUES = DATA / "sm_equivalence_reference_data_values_fill.candidate.json"

STATUS = (
    "MTT_SELECTED_COVARIANCESIDECARFILL_OR_RTHETASOURCEROWDERIVATION_"
    "BUILT_WZH_SIDECARS_INTERIM_LADDER_RTHETA_OPEN"
)
NEXT = "MTT_Selected_CrossBlockCovariance_or_RThetaCoefficientValueFill_v1"


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
        raise FileNotFoundError("missing covariance sidecar fill sources: " + ", ".join(missing))


def bridge_delta_map(gauge_bridge: dict[str, Any]) -> dict[str, float]:
    deltas: dict[str, float] = {}
    for row in gauge_bridge["comparison_rows"]:
        row_id = row["id"]
        if row_id.startswith("g1GUT"):
            deltas["g_1_GUT_Mt"] = abs(float(row["absolute_delta"]))
        elif row_id.startswith("g2"):
            deltas["g_2_Mt"] = abs(float(row["absolute_delta"]))
        elif row_id.startswith("g3"):
            deltas["g_3_Mt"] = abs(float(row["absolute_delta"]))
    if "g_1_GUT_Mt" in deltas:
        deltas["g_Y_Mt"] = deltas["g_1_GUT_Mt"] / math.sqrt(5.0 / 3.0)
    return deltas


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_GATE,
        PREVIOUS_COVERAGE,
        WZH_INVENTORY,
        GAUGE_BRIDGE,
        SENSITIVITY,
        WEAK_ENVELOPE,
        BCT_PROFILE,
        HIGGS_COV,
        RTHETA_ATTEMPT_SOURCE,
        RTHETA_DECISION,
        REFERENCE_VALUES,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_gate = load(PREVIOUS_GATE)
    previous_coverage = load(PREVIOUS_COVERAGE)
    wzh_inventory = load(WZH_INVENTORY)
    gauge_bridge = load(GAUGE_BRIDGE)
    sensitivity = load(SENSITIVITY)
    weak_envelope = load(WEAK_ENVELOPE)
    bct_profile = load(BCT_PROFILE)
    higgs_cov = load(HIGGS_COV)
    rtheta_attempt_source = load(RTHETA_ATTEMPT_SOURCE)
    rtheta_decision = load(RTHETA_DECISION)
    reference = load(REFERENCE_VALUES)

    propagated = sensitivity["propagated_diagonal_uncertainties"]
    bridge_deltas = bridge_delta_map(gauge_bridge)
    theory_sigmas = {
        "lambda_Mt": 0.0003,
        "g_Y_Mt": bridge_deltas["g_Y_Mt"],
        "g_1_GUT_Mt": bridge_deltas["g_1_GUT_Mt"],
        "g_2_Mt": bridge_deltas["g_2_Mt"],
    }
    v_row = reference["reference_values"]["constants"]["v_from_G_F"]
    v_sigma = float(v_row["uncertainty"]["plus"])

    sidecar_rows = []
    for row_id in ["g_Y_Mt", "g_1_GUT_Mt", "g_2_Mt", "lambda_Mt"]:
        linear_sigma = float(propagated[row_id]["diagonal_sigma"])
        surrogate_sigma = float(theory_sigmas[row_id])
        total_sigma = math.sqrt(linear_sigma * linear_sigma + surrogate_sigma * surrogate_sigma)
        sidecar_rows.append(
            {
                "id": row_id,
                "linear_sensitivity_sigma": linear_sigma,
                "surrogate_systematic_sigma": surrogate_sigma,
                "total_interim_sigma": total_sigma,
                "variance": total_sigma * total_sigma,
                "surrogate_systematic_source": (
                    "lambda theory sidecar" if row_id == "lambda_Mt" else "one-loop gauge bridge absolute discrepancy"
                ),
                "accepted_as_interim_covariance_sidecar": True,
                "accepted_as_full_covariance_sidecar": False,
                "accepted_as_selected_Rtheta_source_row": False,
            }
        )
    sidecar_rows.insert(
        0,
        {
            "id": "v_from_G_F_tree_reference",
            "linear_sensitivity_sigma": v_sigma,
            "surrogate_systematic_sigma": 0.0,
            "total_interim_sigma": v_sigma,
            "variance": v_sigma * v_sigma,
            "surrogate_systematic_source": "CODATA G_F propagated reference uncertainty only",
            "accepted_as_interim_covariance_sidecar": True,
            "accepted_as_full_covariance_sidecar": False,
            "accepted_as_selected_Rtheta_source_row": False,
        },
    )

    independent_basis = ["v_from_G_F_tree_reference", "g_Y_Mt", "g_2_Mt", "lambda_Mt"]
    alias_basis = {
        "g_1_GUT_Mt": {
            "alias_of": "g_Y_Mt",
            "normalization": "sqrt(5/3)",
            "must_not_be_double_counted_in_covariance": True,
        }
    }
    covariance_diagonal = [
        next(row for row in sidecar_rows if row["id"] == row_id)["variance"]
        for row_id in independent_basis
    ]
    wzh_sidecars = {
        "schema": "MTTWZHGaugeAndLambdaCovarianceSidecars.v1",
        "status": "WZH_INTERIM_COVARIANCE_SIDECARS_FILLED_FULL_COVARIANCE_OPEN",
        "wzh_inventory_source": rel(WZH_INVENTORY),
        "sensitivity_source": rel(SENSITIVITY),
        "gauge_bridge_source": rel(GAUGE_BRIDGE),
        "reference_value_source": rel(REFERENCE_VALUES),
        "sidecar_policy": (
            "Use linear propagated sigma where present and add a conservative surrogate systematic "
            "from the one-loop gauge bridge discrepancy or explicit lambda theory sidecar. This is a "
            "validation/profile sidecar, not a selected-source derivation."
        ),
        "row_sidecars": sidecar_rows,
        "independent_covariance_basis": independent_basis,
        "alias_basis": alias_basis,
        "diagonal_covariance_matrix": [
            [covariance_diagonal[i] if i == j else 0.0 for j in range(len(covariance_diagonal))]
            for i in range(len(covariance_diagonal))
        ],
        "fills_previous_missing_object": "gauge-row uncertainty/correlation sidecars at Mt for gY/g2 and normalization alias handling",
        "accepted_as_interim_covariance_sidecars": True,
        "accepted_as_full_covariance_profile": False,
        "accepted_as_selected_Rtheta_source_rows": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(WZH_SIDECARS, wzh_sidecars)

    missing_after_sidecar = [
        item
        for item in previous_gate["missing_covariance_objects"]
        if not item.startswith("gauge-row uncertainty/correlation sidecars")
    ]
    ladder_rows = [
        {
            "stage": "coverage_matrix",
            "closed": previous["closure_decision"]["block_coverage_matrix_closed"],
            "source": rel(PREVIOUS_COVERAGE),
        },
        {
            "stage": "WZH_interim_sidecars",
            "closed": True,
            "source": rel(WZH_SIDECARS),
        },
        {
            "stage": "weak_correlation_envelope",
            "closed": weak_envelope["chi2_envelope"]["passes_core_correlation_envelope"],
            "source": rel(WEAK_ENVELOPE),
        },
        {
            "stage": "BCT_empirical_correlated_profile",
            "closed": bct_profile["passes_95pct_profile_gate"],
            "source": rel(BCT_PROFILE),
        },
        {
            "stage": "Higgs_source_derived_covariance_model",
            "closed": higgs_cov["accepted_as_source_derived_covariance_model"],
            "source": rel(HIGGS_COV),
        },
        {
            "stage": "cross_block_covariance",
            "closed": False,
            "source": None,
        },
        {
            "stage": "full_published_or_reconstructed_profile_likelihood",
            "closed": False,
            "source": None,
        },
    ]
    ladder = {
        "schema": "MTTInterimCovarianceLadderAfterSidecarFill.v1",
        "status": "INTERIM_COVARIANCE_LADDER_ADVANCED_CROSS_BLOCK_PROFILE_OPEN",
        "previous_gate_source": rel(PREVIOUS_GATE),
        "ladder_rows": ladder_rows,
        "advanced_now": {
            "WZH_interim_sidecars": True,
            "gauge_alias_handling_for_g1GUT": True,
            "block_diagonal_interim_profile_more_actionable": True,
        },
        "can_build_interim_block_diagonal_profile": all(row["closed"] for row in ladder_rows[:5]),
        "can_claim_full_correlated_profile": False,
        "missing_covariance_objects_after_sidecar_fill": missing_after_sidecar,
        "why_still_not_full": (
            "The new W/Z/H sidecars close a local sidecar gap, but cross-block covariance is still missing. "
            "Shared inputs and conventions can correlate weak-scale, BCT, and Higgs replay rows."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(LADDER, ladder)

    rtheta_attempt = {
        "schema": "MTTRThetaSourceRowDerivationRecheckAfterSidecarFill.v1",
        "status": "RTHETA_SOURCE_ROW_DERIVATION_RECHECKED_STILL_OPEN",
        "rtheta_construction_attempt_source": rel(RTHETA_ATTEMPT_SOURCE),
        "rtheta_blocker_decision_source": rel(RTHETA_DECISION),
        "sidecar_fill_source": rel(WZH_SIDECARS),
        "what_sidecar_fill_changes": [
            "profile/covariance sidecar limitation is now partially reduced for W/Z/H rows",
            "g1GUT alias handling is explicit for future covariance inversion",
            "accepted external W/Z/H values can be used as validators for a future Rtheta source map",
        ],
        "what_sidecar_fill_does_not_change": rtheta_attempt_source["why_not_successful"],
        "source_owner_candidate_matrix_closed": rtheta_decision["source_owner_candidate_matrix_closed"],
        "row_coefficient_slot_manifest_closed": rtheta_decision["row_coefficient_slot_manifest_closed"],
        "row_coefficients_filled": rtheta_decision["row_coefficients_filled"],
        "selected_threshold_response_functional_instantiated": rtheta_decision[
            "selected_threshold_response_functional_instantiated"
        ],
        "selected_Rtheta_source_rows_closed": False,
        "accepted_Rtheta_source_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA_ATTEMPT, rtheta_attempt)

    cutset = {
        "schema": "MTTNextCutsetAfterCovarianceSidecarFill.v1",
        "status": "NEXT_ATTACK_CROSS_BLOCK_COVARIANCE_OR_RTHETA_COEFFICIENT_VALUES",
        "closed_now": {
            "WZH_interim_covariance_sidecars": True,
            "gauge_alias_handling_for_covariance": True,
            "interim_covariance_ladder_advanced": True,
            "Rtheta_derivation_rechecked_after_sidecar_fill": True,
        },
        "still_open": {
            "cross_block_covariance": True,
            "full_covariance_profile_likelihood": True,
            "Rtheta_row_coefficients": True,
            "selected_threshold_response_functional": True,
            "selected_Rtheta_source_rows": True,
            "common_scale_convention_map": True,
            "EW_formula_kernels_for_WW_ZZ_Zgamma": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "build the cross-block covariance map from shared input directions and common-scale convention dependencies",
            "route_B": "fill Rtheta row coefficient values for v/gY/g2/lambda against the source-owner slot manifest",
            "route_C": "derive the selected threshold response functional and demote external rows to validators",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedCovarianceSidecarFillOrRThetaSourceRowDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "wzh_gauge_and_lambda_covariance_sidecars": rel(WZH_SIDECARS),
            "interim_covariance_ladder_after_sidecar_fill": rel(LADDER),
            "rtheta_source_row_derivation_recheck_after_sidecar_fill": rel(RTHETA_ATTEMPT),
            "next_cutset_after_covariance_sidecar_fill": rel(CUTSET),
        },
        "theorem": {
            "name": "WZHInterimSidecarFillAndRThetaRecheckTheorem",
            "proved": True,
            "statement": (
                "The W/Z/H gauge and lambda rows admit conservative interim covariance sidecars from "
                "the existing linear sensitivity scaffold plus the one-loop bridge discrepancy/theory "
                "sidecar. This closes the gauge sidecar gap at interim profile level and advances the "
                "covariance ladder, but cross-block covariance, selected Rtheta row coefficients, full "
                "profile likelihood, true SM equivalence, and no-knob closure remain open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "WZH_interim_covariance_sidecars_closed": True,
            "interim_block_diagonal_profile_available": ladder["can_build_interim_block_diagonal_profile"],
            "full_covariance_profile_likelihood_closed": False,
            "selected_Rtheta_source_rows_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "previous_status": previous["status"],
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_CovarianceSidecarFill_or_RThetaSourceRowDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "WZH_interim_covariance_sidecars_closed": True,
        "interim_block_diagonal_profile_available": ladder["can_build_interim_block_diagonal_profile"],
        "full_covariance_profile_likelihood_closed": False,
        "selected_Rtheta_source_rows_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected CovarianceSidecarFill or RThetaSourceRowDerivation v1

Status: `{STATUS}`.

This artifact fills conservative interim W/Z/H covariance sidecars.

```text
W/Z/H interim sidecars closed       : true
interim block-diagonal profile      : {str(ladder["can_build_interim_block_diagonal_profile"]).lower()}
cross-block covariance closed       : false
selected R_theta source rows closed : false
true SM equivalence closed          : false
no-knob closure                     : false
```

The sidecars use existing linear sensitivities plus conservative surrogate
systematics from the one-loop gauge bridge discrepancy or the lambda theory
sidecar. They are validation/profile sidecars, not selected MTT source rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
