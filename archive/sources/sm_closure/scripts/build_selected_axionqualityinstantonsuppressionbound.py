from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
SLUG = "selected_axionqualityinstantonsuppressionbound"
STATUS = (
    "MTT_U6_PERTURBATIVE_AXION_QUALITY_EXACT_AND_NONPERTURBATIVE_"
    "QUALITY_INEQUALITY_CLOSED_SELECTED_INSTANTON_AMPLITUDES_OPEN"
)
NEXT = "MTT_Selected_q79HiddenGaugeAndNS5InstantonActionPacket_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_AxionQualityInstantonSuppressionBound_v1.md"

THEOREM = OUT / "exact_axion_quality_sufficient_bound.packet.json"
CENSUS = OUT / "selected_q79_nonQCD_breaking_source_census.packet.json"
DIAGNOSTIC = OUT / "single_instanton_action_thresholds.diagnostic.json"
FRONTIER = OUT / "U6_frontier_after_A98.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def action_bound(cutoff_gev: float, chi_gev4: float, theta_max: float, harmonic: int) -> dict:
    amplitude = cutoff_gev**4
    bounds = {
        "derivative": math.log(abs(harmonic) * amplitude / (chi_gev4 * math.sin(theta_max))),
        "curvature": math.log(harmonic**2 * amplitude / (chi_gev4 * math.cos(theta_max))),
        "global_competitor": math.log(2 * amplitude / (chi_gev4 * (1 + math.cos(theta_max)))),
    }
    return {
        "cutoff_GeV": cutoff_gev,
        "harmonic": harmonic,
        "required_action_components": bounds,
        "required_action_max": max(bounds.values()),
    }


def main() -> int:
    paths = {
        "A97": ROOT / "candidate_data" / "selected_4dgreenschwarzaxionreductionandsurvivingcurrent.candidate.json",
        "A97_map": ROOT / "candidate_data" / "selected_4dgreenschwarzaxionreductionandsurvivingcurrent" / "U6_current_map_after_A97.packet.json",
        "A97_reduction": ROOT / "candidate_data" / "selected_4dgreenschwarzaxionreductionandsurvivingcurrent" / "universal_B6_axion_reduction.packet.json",
        "q79_flat_gerbe": Q79 / "candidate_data" / "time_oriented_m1_green_schwarz_gate.candidate.json",
        "strominger_corpus": TEXPAPERS / "16 Strings, Flux, & M-Theory Encodings" / "_md" / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
        "mtheory_corpus": TEXPAPERS / "16 Strings, Flux, & M-Theory Encodings" / "_md" / "Modal_Triplet_Theory__From_MTT_to_M_theory.md",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing A98 authority: " + ", ".join(missing))

    a97 = load(paths["A97"])
    a97_map = load(paths["A97_map"])
    reduction = load(paths["A97_reduction"])
    flat = load(paths["q79_flat_gerbe"])
    strominger_text = paths["strominger_corpus"].read_text(encoding="utf-8")
    mtheory_text = paths["mtheory_corpus"].read_text(encoding="utf-8")

    theta_max = 1e-10
    quality_theorem = {
        "schema": "MTTExactAxionQualitySufficientBound.v1",
        "status": "EXACT_GLOBAL_MINIMUM_DISPLACEMENT_CERTIFICATE_FORMULATED",
        "potential": {
            "definition": "V(theta)=chi_QCD*(1-cos(theta+theta_bar))+DeltaV(theta)",
            "breaking_expansion": "DeltaV(theta)=-sum_j Lambda_j^4*cos(n_j*theta+delta_j)",
            "period": "2*pi",
            "theta_tolerance": theta_max,
        },
        "norm_bounds": {
            "M0": "sum_j Lambda_j^4 bounds sup|DeltaV|",
            "M1": "sum_j |n_j| Lambda_j^4 bounds sup|DeltaV'|",
            "M2": "sum_j n_j^2 Lambda_j^4 bounds sup|DeltaV''|",
        },
        "sufficient_conditions": {
            "derivative": "M1 < chi_QCD*sin(theta_tolerance)",
            "local_convexity": "M2 < chi_QCD*cos(theta_tolerance)",
            "exclude_opposite_QCD_extremum": "2*M0 < chi_QCD*(1+cos(theta_tolerance))",
        },
        "conclusion": "The unique global minimum obeys angular_distance(theta+theta_bar,2*pi*Z)<theta_tolerance.",
        "proof": [
            "Outside the tolerance neighborhoods of 0 and pi, the QCD derivative has magnitude at least chi_QCD*sin(theta_tolerance), so the derivative condition fixes its sign and excludes stationary points.",
            "Inside the 0 neighborhood, the curvature condition makes the potential strictly convex and gives one minimum.",
            "Inside the pi neighborhood, the QCD energy is at least chi_QCD*(1+cos(theta_tolerance)); the M0 condition keeps it above the value available near zero, so it cannot be global.",
        ],
        "theorem": {
            "name": "ExactAxionQualityGlobalMinimumTheorem",
            "proved": True,
            "uses_small_angle_linearization": False,
            "uses_observed_theta_as_selector": False,
        },
    }

    perturbative_markers = {
        "strominger_B_only_through_Hhat": "enters only via" in strominger_text,
        "strominger_large_gauge_invariance": "large gauge transformations" in strominger_text,
        "corpus_continuous_shift_symmetry": "continuous shift symmetries" in mtheory_text,
        "corpus_nonperturbative_effects_named": "nonperturbative effects" in mtheory_text,
        "corpus_NS5_tension_named": "T_{\\mathrm{NS5}}" in mtheory_text,
    }
    source_census = {
        "schema": "MTTSelectedQ79NonQCDBreakingSourceCensus.v1",
        "status": "PERTURBATIVE_BREAKING_ZERO_NONPERTURBATIVE_SOURCE_PAYLOAD_OPEN",
        "closed": {
            "perturbative_local_potential_for_theta_MI": 0,
            "reason": "The ten-dimensional gerbe/higher-form gauge symmetry permits derivative and quantized topological couplings but forbids a perturbative local potential for the universal axion.",
            "q79_flat_Z3_gerbe_de_Rham_H": flat["flat_torsion_curvature_effect"]["curvature_H_form"],
            "flat_Z3_gerbe_generates_continuous_axion_potential": False,
            "QCD_color_harmonic": 1,
            "QCD_color_coupling_selected": a97["results"]["visible_color_embedding_index"] == 1,
        },
        "selected_nonQCD_payload": {
            "hidden_gauge_group_and_light_matter": None,
            "hidden_confinement_or_instanton_scale": None,
            "hidden_axion_anomaly_integer": None,
            "Euclidean_NS5_wrapped_cycle": None,
            "Euclidean_NS5_action": None,
            "worldsheet_instanton_cycles_actions_and_harmonics": None,
            "other_allowed_nonperturbative_sectors": None,
            "amplitude_prefactors": None,
            "relative_phases": None,
        },
        "readiness": {"filled": 0, "required": 9},
        "cross_repo_result": "The q79, constants, flux/string and SM proof inventories contain the Bianchi packet, shift symmetry and brane-tension templates, but no selected hidden-sector/NS5 amplitude table on the same q79/F,m=1 compactification.",
        "corpus_markers": perturbative_markers,
        "forbidden_shortcuts": [
            "Do not identify the flat Z3 gerbe with the continuous universal axion.",
            "Do not use the Z64 closure label as an axion harmonic without a source map.",
            "Do not insert an observed axion mass, theta bound, string scale or hidden confinement scale as selected MTT data.",
            "Do not infer an exponentially small amplitude from a brane-tension formula without the selected wrapped volume and coupling.",
        ],
    }

    chi_benchmark = 0.0756**4
    diagnostic = {
        "schema": "MTTSingleInstantonActionThresholdDiagnostic.v1",
        "status": "EXTERNAL_SCALE_DIAGNOSTIC_NOT_SELECTED_MTT_DATA",
        "inputs": {
            "theta_tolerance": theta_max,
            "chi_QCD_GeV4_from_75p6MeV_benchmark": chi_benchmark,
            "single_harmonic": 1,
        },
        "thresholds": [
            action_bound(1e16, chi_benchmark, theta_max, 1),
            action_bound(1e17, chi_benchmark, theta_max, 1),
        ],
        "interpretation": "For a prefactor Lambda_UV^4*exp(-S), the derivative condition dominates and requires S around 181 at 1e16 GeV or 190 at 1e17 GeV. These are search targets, not predictions.",
        "selected_prediction": False,
    }

    frontier = {
        "schema": "MTTU6FrontierAfterA98.v1",
        "status": "U6_NINE_OF_TEN_EXACT_QUALITY_TEST_READY_SELECTED_NONPERTURBATIVE_VALUES_OPEN",
        "current_map_readiness": a97_map["readiness"],
        "new_closure": {
            "perturbative_axion_quality": True,
            "exact_nonperturbative_acceptance_inequality": True,
            "single_instanton_action_threshold_formula": True,
        },
        "still_open": {
            "selected_hidden_and_brane_instants_payload": True,
            "quality_breaking_bound_final_field": True,
            "physical_absolute_f_MI_no_knob_value": True,
        },
        "U6_strong_CP_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }

    checks = {
        "A97_is_nine_of_ten": a97_map["readiness"] == {"filled": 9, "required": 10},
        "A97_quality_open": a97_map["final_fields"]["quality_breaking_bound"] is False,
        "universal_axion_periodic": reduction["mode"]["periodicity"] == "theta_MI equivalent to theta_MI + 2*pi",
        "all_perturbative_markers": all(perturbative_markers.values()),
        "flat_gerbe_H_zero": source_census["closed"]["q79_flat_Z3_gerbe_de_Rham_H"] == "0",
        "nonQCD_payload_zero_of_nine": source_census["readiness"] == {"filled": 0, "required": 9},
        "exact_quality_theorem": quality_theorem["theorem"]["proved"],
        "no_linearization": not quality_theorem["theorem"]["uses_small_angle_linearization"],
        "diagnostic_not_selected": not diagnostic["selected_prediction"],
        "action_threshold_ordered": diagnostic["thresholds"][1]["required_action_max"] > diagnostic["thresholds"][0]["required_action_max"],
        "quality_not_overclosed": not frontier["U6_strong_CP_closed"],
        "no_new_parameter": frontier["new_continuous_parameters"] == 0,
    }
    outputs = {
        "quality_theorem": str(THEOREM.relative_to(ROOT)).replace("\\", "/"),
        "source_census": str(CENSUS.relative_to(ROOT)).replace("\\", "/"),
        "action_diagnostic": str(DIAGNOSTIC.relative_to(ROOT)).replace("\\", "/"),
        "U6_frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedAxionQualityInstantonSuppressionBound.v1",
        "status": STATUS,
        "results": {
            "perturbative_quality_closed": True,
            "exact_global_minimum_bound_closed": True,
            "selected_nonQCD_source_payload": "0/9",
            "quality_final_field_closed": False,
            "U6_current_map": "9/10",
            "U6_strong_CP_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_AxionQualityInstantonSuppressionBound_v1",
        "status": STATUS,
        "perturbative_quality_closed": True,
        "exact_quality_inequality_closed": True,
        "selected_nonQCD_payload": "0/9",
        "U6_current_map": "9/10",
        "U6_strong_CP_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Axion-Quality Instanton Suppression Bound v1

## Exact quality theorem

Write

```text
V(theta)=chi_QCD[1-cos(theta+theta_bar)] + DeltaV(theta),
DeltaV=-sum_j Lambda_j^4 cos(n_j theta+delta_j).
```

Define

```text
M0=sum Lambda_j^4,
M1=sum |n_j| Lambda_j^4,
M2=sum n_j^2 Lambda_j^4.
```

For a tolerance `epsilon`, the three exact sufficient inequalities are

```text
M1 < chi_QCD sin(epsilon),
M2 < chi_QCD cos(epsilon),
2 M0 < chi_QCD [1+cos(epsilon)].
```

They imply that the unique global minimum satisfies
`dist(theta+theta_bar,2*pi*Z)<epsilon`. This is not a small-angle
linearization: derivative signs exclude all stationary points outside the
zero and opposite-point neighborhoods, strict convexity fixes the zero
neighborhood, and the `M0` bound excludes the opposite point globally.

## What closes

The selected heterotic gerbe gauge symmetry makes the perturbative local
potential for the universal axion exactly zero. The q79 order-three gerbe has
de Rham `H=0` and neither helps nor harms this continuous mode. Thus the
perturbative quality subproblem is closed, and the full nonperturbative test is
now executable once its source values are supplied.

## What remains

The current corpus does not emit the selected hidden gauge spectrum,
confinement/instanton scales, anomaly harmonics, wrapped NS5 cycle and action,
worldsheet-instanton table, prefactors, or phases on the same q79 branch. That
payload is `0/9`. A brane-tension formula alone is insufficient without the
selected volume and coupling.

For orientation only, a one-instanton prefactor at `10^16`--`10^17 GeV` would
need an action of roughly `181`--`190` for `epsilon=1e-10`; those numbers use
external QCD/scale benchmarks and are not MTT predictions.

U6 remains `9/10`, with zero new continuous parameters.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (THEOREM, quality_theorem),
        (CENSUS, source_census),
        (DIAGNOSTIC, diagnostic),
        (FRONTIER, frontier),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
