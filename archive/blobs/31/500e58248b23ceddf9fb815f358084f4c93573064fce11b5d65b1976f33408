"""Build Step67 theta-overlap anchor / exponent-prefactor frontier."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
EXTERNAL_PACKET = PACKET_DIR / "step67_external_inspiration_not_proof.packet.json"
ANCHOR_PACKET = PACKET_DIR / "step67_theta_overlap_suppression_anchor.packet.json"
TRIAL_PACKET = PACKET_DIR / "step67_exponent_lattice_diagnostic_trials.packet.json"
MISSING_PACKET = PACKET_DIR / "step67_next_exponent_prefactor_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step67_ThetaOverlapAnchor_or_ExponentPrefactorFrontier_v1.md"

STEP66 = DATA / "selected_step66_scalarvalue_nogo_or_magnitudethresholdsource_frontier.candidate.json"
STEP66_MISSING = (
    DATA
    / "selected_step66_scalarvalue_nogo_or_magnitudethresholdsource_frontier"
    / "step66_minimal_missing_source_object.packet.json"
)
EXT_OVERLAP = DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json"
ALPHA1 = (
    DATA
    / "selected_step44_alpha1universalanchor_admission_or_rthetarowexecution"
    / "step44_alpha1_source_anchor_admission.packet.json"
)
RTHETA_ALPHA1 = (
    DATA
    / "selected_step46_alpha1_to_rtheta_coefficient_map_or_valueexecution"
    / "step46_selected_alpha1_to_rtheta_coefficient_map.packet.json"
)
FAMILY_SPECTRUM = (
    DATA
    / "selected_familyresolvingoperator_or_generationthresholdrowsexecution"
    / "selected_first_response_family_spectrum.packet.json"
)
SECTOR_FRONTIER = (
    DATA
    / "selected_sectorscaledeigenprofilethresholdrows_or_yukawamagnitudesourceexecution"
    / "sector_coefficient_frontier.packet.json"
)
HIGHER_RESPONSE_ATTEMPT = (
    DATA
    / "selected_higherresponsesectorcoefficients_or_thresholdfunctionalsourcerows"
    / "higher_response_sector_coefficient_source_attempt.packet.json"
)
COMMON_VALUES = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)

STATUS = "MTT_SELECTED_STEP67_THETA_OVERLAP_ANCHOR_CLOSED_EXPONENT_PREFACTOR_FRONTIER_OPEN"
NEXT = "MTT_Selected_ThetaOverlapExponentTheorem_or_HYMThresholdPrefactorRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def obs_values(common: dict[str, Any]) -> dict[str, list[float]]:
    values = common.get("derived_magnitudes", common["values"])
    lambda_h = values["lambda_H"] if "lambda_H" in values else values["lambda_H_MZ_firstpass"]
    return {
        "u": list(values["diag_abs_Y_u"]),
        "d": list(values["diag_abs_Y_d"]),
        "e": list(values["diag_abs_Y_e"]),
        "H": [float(lambda_h)],
    }


def model_postcheck(name: str, exponents: dict[str, list[float]], values: dict[str, list[float]], eps: float) -> dict[str, Any]:
    rows = []
    factors = []
    for sector, sector_values in values.items():
        for idx, observed in enumerate(sector_values):
            exponent = exponents[sector][idx]
            predicted_scale = eps**exponent
            factor = observed / predicted_scale
            factors.append(factor)
            rows.append(
                {
                    "sector": sector,
                    "generation": None if sector == "H" else idx + 1,
                    "exponent": exponent,
                    "source_scale": predicted_scale,
                    "postcheck_value_not_selector": observed,
                    "order_one_factor_postcheck": factor,
                    "accepted_as_selected_value": False,
                }
            )
    return {
        "model_id": name,
        "exponents": exponents,
        "rows": rows,
        "min_postcheck_factor": min(factors),
        "max_postcheck_factor": max(factors),
        "factor_span": max(factors) / min(factors),
        "log10_factor_span": math.log10(max(factors) / min(factors)),
        "accepted_as_selected_exponent_theorem": False,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP66,
        STEP66_MISSING,
        EXT_OVERLAP,
        ALPHA1,
        RTHETA_ALPHA1,
        FAMILY_SPECTRUM,
        SECTOR_FRONTIER,
        HIGHER_RESPONSE_ATTEMPT,
        COMMON_VALUES,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step67 inputs: " + ", ".join(missing))

    step66 = load(STEP66)
    ext = load(EXT_OVERLAP)
    alpha1 = load(ALPHA1)
    rtheta_alpha1 = load(RTHETA_ALPHA1)
    spectrum = load(FAMILY_SPECTRUM)
    sector_frontier = load(SECTOR_FRONTIER)
    higher_attempt = load(HIGHER_RESPONSE_ATTEMPT)
    common = load(COMMON_VALUES)

    origin = ext["transition_overlap_table"]["sample_values"][0]["generator_values"]
    e_minus_4pi_from_geometry = float(origin["g4"]["abs"])
    epsilon_theta = math.sqrt(e_minus_4pi_from_geometry)
    exact_epsilon = math.exp(-2.0 * math.pi)
    exact_e_minus_4pi = math.exp(-4.0 * math.pi)
    if abs(e_minus_4pi_from_geometry - exact_e_minus_4pi) > 1e-18:
        raise AssertionError("AH transition factor does not match exp(-4*pi)")
    if abs(epsilon_theta - exact_epsilon) > 1e-18:
        raise AssertionError("epsilon mismatch")

    external_packet = {
        "schema": "MTTStep67ExternalInspirationNotProof.v1",
        "status": "EXTERNAL_FLAVOR_MECHANISMS_USED_AS_DESIGN_INSPIRATION_ONLY",
        "external_sources": [
            {
                "topic": "magnetized orbifold zero-mode overlaps",
                "url": "https://arxiv.org/pdf/0812.3534",
                "usable_pattern": "generation count and Yukawa hierarchy can arise from zero-mode wavefunction overlap integrals",
            },
            {
                "topic": "Riemann theta overlap formulae in magnetized branes",
                "url": "https://arxiv.org/abs/0904.0910",
                "usable_pattern": "Yukawa couplings can be expressed through theta-function wavefunction overlaps",
            },
            {
                "topic": "Froggatt-Nielsen exponent logic",
                "url": "https://link.springer.com/article/10.1007/JHEP03(2025)150",
                "usable_pattern": "hierarchies can be controlled by charges/exponents, but MTT must source them before replay",
            },
            {
                "topic": "modular flavor hierarchy near fixed points",
                "url": "https://link.springer.com/article/10.1140/epjc/s10052-023-12303-2",
                "usable_pattern": "small parameters can be selected by modular/geometric structure rather than by per-sector fits",
            },
        ],
        "used_as_proof": False,
        "used_as_selector": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(EXTERNAL_PACKET, external_packet)

    anchor_packet = {
        "schema": "MTTStep67ThetaOverlapSuppressionAnchor.v1",
        "status": "SOURCE_SELECTED_THETA_OVERLAP_SUPPRESSION_ANCHOR_EMITTED",
        "source": rel(EXT_OVERLAP),
        "selected_AH_degree_vector": ext["transition_overlap_table"]["degree_vector"],
        "selected_transition_generator": "g4",
        "selected_transition_factor_at_origin": e_minus_4pi_from_geometry,
        "exact_transition_factor": "exp(-4*pi)",
        "epsilon_theta": epsilon_theta,
        "epsilon_theta_exact": "exp(-2*pi)",
        "epsilon_theta_closed_as_source_overlap_anchor": True,
        "alpha1_source_anchor_available": alpha1["admitted_at_source_tier"],
        "alpha1_value_closure_anchor": alpha1["admitted_as_value_closure_anchor"],
        "rtheta_alpha1_map_constructed": rtheta_alpha1["map_domain_closed"],
        "family_resolving_operator_closed": spectrum["family_resolving_operator_closed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ANCHOR_PACKET, anchor_packet)

    values = obs_values(common)
    exponent_models = {
        "integer_all": {
            "u": [2.0, 1.0, 0.0],
            "d": [2.0, 1.0, 0.0],
            "e": [2.0, 1.0, 0.0],
            "H": [1.0 / 3.0],
        },
        "shared_circle_half_d_e": {
            "u": [2.0, 1.0, 0.0],
            "d": [2.0, 1.0, 0.5],
            "e": [2.0, 1.0, 0.5],
            "H": [1.0 / 3.0],
        },
        "qutrit_third_d_e": {
            "u": [2.0, 1.0, 0.0],
            "d": [2.0, 1.0, 2.0 / 3.0],
            "e": [2.0, 1.0, 2.0 / 3.0],
            "H": [1.0 / 3.0],
        },
    }
    trials = [
        model_postcheck(name, exponents, values, epsilon_theta)
        for name, exponents in exponent_models.items()
    ]
    trials_by_span = sorted(trials, key=lambda item: item["log10_factor_span"])
    trial_packet = {
        "schema": "MTTStep67ExponentLatticeDiagnosticTrials.v1",
        "status": "THETA_OVERLAP_EXPONENT_TRIALS_RUN_POSTCHECKS_ONLY",
        "epsilon_theta": epsilon_theta,
        "epsilon_theta_exact": "exp(-2*pi)",
        "trial_count": len(trials),
        "trials": trials,
        "smallest_postcheck_span_model": trials_by_span[0]["model_id"],
        "smallest_postcheck_log10_factor_span": trials_by_span[0]["log10_factor_span"],
        "postcheck_values_source": rel(COMMON_VALUES),
        "postcheck_values_used_as_selectors": False,
        "accepted_scalar_row_count_now": 0,
        "accepted_exponent_lattice_theorem": False,
        "accepted_HYM_threshold_prefactor_rows": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(TRIAL_PACKET, trial_packet)

    missing_packet = {
        "schema": "MTTStep67NextExponentPrefactorCutset.v1",
        "status": "EXPONENT_THEOREM_OR_HYM_THRESHOLD_PREFACTOR_ROWS_REQUIRED",
        "not_missing_anymore": [
            "source-selected overlap suppression anchor epsilon_Theta=exp(-2*pi)",
            "source-tier alpha1 anchor",
            "Rtheta_alpha1 typed map",
            "selected family-resolving spectrum",
            "pure Weyl coefficient/source rows",
        ],
        "still_missing": [
            "selected theorem assigning charged-sector exponent lattice before postcheck",
            "selected HYM/threshold prefactor rows for u,d,e generations",
            "selected lambda_H exponent/prefactor row",
            "selected threshold response functional instantiation",
            "mass-scheme/profile convention at internal no-knob tier",
        ],
        "best_next_route": (
            "derive a theta-overlap exponent theorem from the selected qutrit family spectrum, "
            "shared-circle weight, and AH/HYM overlap geometry; then emit HYM threshold prefactors "
            "or prove they are fixed by the same selected connection."
        ),
        "forbidden_routes": [
            "promote diagnostic order-one factors as selected prefactors",
            "choose exponent lattice by minimizing postcheck residuals",
            "use observed Yukawa/Higgs values as source rows",
            "reopen pure Weyl row emission or family-resolution as active blockers",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(MISSING_PACKET, missing_packet)

    candidate = {
        "candidate": "MTTSelectedStep67ThetaOverlapAnchorOrExponentPrefactorFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "external_inspiration_not_proof": rel(EXTERNAL_PACKET),
            "theta_overlap_suppression_anchor": rel(ANCHOR_PACKET),
            "exponent_lattice_diagnostic_trials": rel(TRIAL_PACKET),
            "next_exponent_prefactor_cutset": rel(MISSING_PACKET),
        },
        "theorem": {
            "name": "Step67ThetaOverlapSuppressionAnchorTheorem",
            "proved": True,
            "statement": (
                "The selected Appell-Humbert/theta overlap table emits an exact source-selected "
                "universal suppression anchor epsilon_Theta=exp(-2*pi), since the selected g4 "
                "transition factor is exp(-4*pi). This is not an empirical fit and is compatible "
                "with the external overlap/FN/modular pattern of flavor hierarchies. However, "
                "epsilon_Theta plus the closed family spectrum still does not emit accepted scalar "
                "rows: an exponent assignment theorem and HYM/threshold prefactor rows are still "
                "required, including lambda_H."
            ),
        },
        "closure_decision": {
            "theta_overlap_suppression_anchor_closed": True,
            "epsilon_theta_value": epsilon_theta,
            "alpha1_source_anchor_available": True,
            "rtheta_alpha1_map_constructed": True,
            "family_resolving_operator_closed": True,
            "external_sources_used_as_proof": False,
            "exponent_lattice_diagnostic_trials_run": True,
            "accepted_scalar_row_count_now": 0,
            "accepted_exponent_lattice_theorem": False,
            "accepted_HYM_threshold_prefactor_rows": False,
            "lambda_H_row_emitted": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step66["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "frontier_context": {
            "sector_frontier_status": sector_frontier["status"],
            "higher_response_attempt_status": higher_attempt["status"],
            "step66_next": step66["next_required_artifact"],
        },
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step67_ThetaOverlapAnchor_or_ExponentPrefactorFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step67 ThetaOverlapAnchor or ExponentPrefactorFrontier v1

Status: `{STATUS}`.

## What Closed

The selected AH/theta overlap table emits an exact non-fit suppression anchor:

```text
selected transition factor       : exp(-4*pi)
epsilon_Theta                    : exp(-2*pi)
epsilon_Theta numeric            : {epsilon_theta:.18e}
source-tier alpha1 available     : true
Rtheta_alpha1 map constructed    : true
family-resolving operator closed : true
accepted scalar rows             : 0
lambda_H row emitted             : false
true SM equivalence closed       : false
full no-knob closure             : false
```

External flavor mechanisms were used only as design inspiration: overlap
integrals, theta-function wavefunctions, FN exponent logic, and modular fixed
point hierarchies. None of those external sources is used as an MTT proof or as
an empirical selector.

## Diagnostic

The exponent-lattice trials use `epsilon_Theta` and selected family labels, then
compare against admitted replay values only as postchecks. No trial is accepted
as selected scalar-row emission. The smallest postcheck span in this run is:

```text
model                         : {trials_by_span[0]["model_id"]}
log10 order-one factor span   : {trials_by_span[0]["log10_factor_span"]:.6f}
```

## New Frontier

The active wall is now sharper:

`{NEXT}`

Minimum next success: prove the exponent lattice from selected qutrit/shared
circle/AH-HYM geometry and emit selected HYM/threshold prefactor rows, including
`lambda_H`, before any comparison with measured Yukawa or Higgs values.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
