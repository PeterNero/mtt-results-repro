"""Build CONST-EW-02 B9 weak-mixing profile reduction and primitive gate.

B8 closed the flat FP policy for the internal SU2 weak-split lane.  B9 reduces
the remaining physical weak-angle problem to source-selected profile
combinations.  It also records the honest role of a possible single universal
parameter: useful if independently selected, forbidden if chosen from the weak
angle or electroweak targets.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b9_profile_reduction_and_universal_parameter_gate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROFILE = BASE / "one_loop_profile_reduction.packet.json"
IMPORTS = BASE / "superset_imports_critical.packet.json"
PRIMITIVE = BASE / "one_universal_parameter_gate.packet.json"
BOUNDARY = BASE / "weak_mixing_b9_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B9_ProfileReductionAndUniversalParameterGate_v1.md"

STATUS = "MTT_CONST_EW_02_B9_PROFILE_REDUCED_UNIVERSAL_PARAMETER_GATE_READY_VALUES_OPEN"

B1 = 41.0 / 10.0
B2 = -19.0 / 6.0


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


def sin2_from_composites(r12: float, u1: float, u2: float) -> float:
    a1x = 1.0 / r12 + u1
    a2x = 1.0 + u2
    return (3.0 * a2x) / (3.0 * a2x + 5.0 * a1x)


def sin2_from_y_no_threshold(r12: float, y: float) -> float:
    return sin2_from_composites(r12, B1 * y, B2 * y)


def derivative_at_zero(r12: float) -> float:
    h = 1e-7
    return (sin2_from_y_no_threshold(r12, h) - sin2_from_y_no_threshold(r12, -h)) / (2.0 * h)


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b8_path = DATA / "const_ew_02_weak_mixing_b8_flat_fp_policy_import.candidate.json"
    b8_boundary_path = DATA / "const_ew_02_weak_mixing_b8_flat_fp_policy_import" / "weak_mixing_boundary_after_fp.packet.json"
    b5_ratio_path = DATA / "const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import" / "theta_ratio_high_scale_packet.packet.json"
    b6_contract_path = DATA / "const_ew_02_weak_mixing_b6_kew_kernel_gate" / "kew_kernel_contract.packet.json"
    b6_projection_path = DATA / "const_ew_02_weak_mixing_b6_kew_kernel_gate" / "exceptional_projection_gate.packet.json"
    one_primitive_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"
    one_anchor_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "one_anchor_metrology.packet.json"
    t1t2_path = SM_PARITY / "candidate_data" / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
    t1t2_cert_path = SM_PARITY / "certificates" / "selected_t1t2_covariant_green_and_transfer_probe_certificate.json"
    theta_v_path = Q79 / "proof_corpus" / "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle.md"

    b8 = load(b8_path)
    b8_boundary = load(b8_boundary_path)
    ratio = load(b5_ratio_path)
    contract = load(b6_contract_path)
    projection = load(b6_projection_path)
    primitive_src = load(one_primitive_path)
    one_anchor = load(one_anchor_path)
    t1t2 = load(t1t2_path)
    t1t2_cert = load(t1t2_cert_path)

    r12 = float(ratio["ratio_source"]["value"])
    high_scale_sin2 = float(ratio["formula"]["computed_value"])
    high_scale_replayed = sin2_from_y_no_threshold(r12, 0.0)
    y_max_positive_a2 = -1.0 / B2
    sample_y = [0.0, 0.0025, 0.005, 0.01, 0.02]
    profile_samples = {f"y={y:g}": sin2_from_y_no_threshold(r12, y) for y in sample_y}

    profile = {
        "schema": "MTTConstEW02B9OneLoopProfileReduction.v1",
        "status": "ONE_LOOP_PROFILE_REDUCTION_CLOSED_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B9-PROFILE-REDUCTION",
        "inputs": {
            "B5_theta_ratio": rel(b5_ratio_path),
            "B6_K_EW_contract": rel(b6_contract_path),
            "B8_flat_FP_boundary": rel(b8_boundary_path),
        },
        "starting_formula": contract["low_scale_formula"],
        "reduction": {
            "definitions": {
                "r12": "g1(mu_Theta)^2/g2(mu_Theta)^2",
                "x": "g2(mu_Theta)^2 or equivalent selected normalization",
                "L": "log(mu_Theta/MZ)",
                "u1": "x*(b1*L/(8*pi^2) + T1)",
                "u2": "x*(b2*L/(8*pi^2) + T2)",
            },
            "reduced_formula": "sin2 = 3*(1+u2)/(3*(1+u2)+5*(1/r12+u1))",
            "high_scale_check": {
                "u1": 0.0,
                "u2": 0.0,
                "computed": high_scale_replayed,
                "matches_B5_value": abs(high_scale_replayed - high_scale_sin2) < 1e-15,
            },
            "no_threshold_one_profile_lane": {
                "definition": "y=x*L/(8*pi^2), T1=T2=0",
                "formula": "sin2(y)=3*(1+b2*y)/(3*(1+b2*y)+5*(1/r12+b1*y))",
                "b1": B1,
                "b2": B2,
                "valid_positive_A2_interval": f"0 <= y < {-1.0 / B2}",
                "derivative_at_y0": derivative_at_zero(r12),
                "interpretation": (
                    "At one-loop with no selected threshold vector, the physical "
                    "profile collapses to one dimensionless composite y.  This "
                    "does not select y; it reduces what a source theorem must emit."
                ),
                "samples_not_targets": profile_samples,
            },
            "general_threshold_lane": {
                "required_source_output": "source-selected pair (u1,u2), or a rule tying them to one selected primitive",
                "why_difference_only_is_not_enough": (
                    "The weak angle depends on A1*x and A2*x separately.  A "
                    "Delta_G12 or lambda_12 difference cannot determine the ratio "
                    "unless a source theorem supplies the common/profile part."
                ),
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    imports = {
        "schema": "MTTConstEW02B9SupersetImportsCritical.v1",
        "status": "SUPERSET_IMPORTS_USEFUL_BUT_NOT_NUMERIC_CLOSURE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B9-SUPERSET-IMPORTS",
        "imports": {
            "sm_parity_t1t2_covariant_green": {
                "path": rel(t1t2_path),
                "certificate": rel(t1t2_cert_path),
                "usable_now": t1t2["operator_payload_boundary"]["T1_T2_coupled_covariant_Riesz_Green_extracted"] is True,
                "what_it_gives": [
                    "full diagonal End0/T1/T2 Riesz-Green operator support",
                    "pure-gauge periodic equivalence theorem for the T1/T2 block",
                ],
                "what_it_does_not_give": [
                    "sector routing values into electroweak T1/T2 amplitudes",
                    "physical dotD_alpha1 payload",
                    "off-diagonal Ext/HYM control",
                    "numeric weak-angle profile",
                ],
                "critical_verdict": "import as operator support only, not as c1/c2 numeric closure",
            },
            "theta_v_redundancy_paper": {
                "path": rel(theta_v_path),
                "usable_now": True,
                "what_it_gives": [
                    "one-loop RG architecture",
                    "explicit warning that round-trip weak angle agreement is not independent prediction",
                    "support for one unavoidable normalization as a parity-style extension",
                ],
                "critical_verdict": (
                    "use for architecture and guardrails; do not import measured "
                    "g2, mW, GF, or sin2 values as no-knob selectors"
                ),
            },
        },
        "superset_strategy": {
            "straight_path": "Reduce the weak-angle formula using the selected ratio r12 and the B6 one-loop K_EW contract.",
            "support_path": "Import T1/T2 covariant Green support from SM-parity End0/HYM without promoting sector amplitudes.",
            "locked_target": "source-selected profile objects (u1,u2) or y; not measured sin2(theta_W)",
            "one_universal_parameter_lane": "allow a single upstream primitive only if it is selected before electroweak comparison and shared across sectors",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    primitive = {
        "schema": "MTTConstEW02B9OneUniversalParameterGate.v1",
        "status": "ONE_UNIVERSAL_PARAMETER_GATE_READY_NOT_SELECTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B9-ONE-UNIVERSAL-PARAMETER-GATE",
        "policy_import": {
            "source": rel(one_primitive_path),
            "status_relative_to_no_knob": primitive_src["status_relative_to_no_knob"],
            "acceptance_policy": primitive_src["acceptance_policy"],
        },
        "anchor_import": {
            "source": rel(one_anchor_path),
            "minimal_extension": one_anchor["minimal_extension"],
            "guardrail": one_anchor["guardrail"],
        },
        "weak_mixing_role": {
            "strict_no_knob": {
                "allowed": True,
                "requires": "source theorem emits u1,u2 or y with no upstream free primitive",
                "closed_now": False,
            },
            "one_universal_parameter_extension": {
                "allowed": True,
                "requires": [
                    "primitive selected once upstream",
                    "primitive shared across alpha1/weak/cosmology or other constants",
                    "weak angle not used to choose it",
                    "predictions state dependence on the primitive until it is independently measured or derived",
                ],
                "candidate_effective_symbols": [
                    "P_univ",
                    "E0 or L0 from the metrology packet",
                    "y_univ = x(P_univ)*log(mu_Theta(P_univ)/MZ)/(8*pi^2)",
                ],
                "closed_now": False,
            },
        },
        "forbidden": [
            "choose y from observed sin2thetaW",
            "choose x from alpha_EM while claiming no-knob weak-angle prediction",
            "choose mu_Theta from the weak-angle target",
            "retune the primitive per constant",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B9Boundary.v1",
        "status": "PROFILE_REDUCTION_CLOSED_C1C2_AND_PRIMITIVE_SELECTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B9-BOUNDARY",
        "closed_now": {
            "one_loop_formula_reduced_to_u1_u2": True,
            "no_threshold_lane_reduced_to_single_y": True,
            "T1T2_covariant_Green_operator_support_imported": True,
            "one_universal_parameter_gate_formalized": True,
        },
        "still_open": {
            "source_selected_u1_u2_or_y": True,
            "sector_transfer_from_End0_Green_to_EW_T1_T2": True,
            "offdiagonal_Ext_HYM_control": True,
            "physical_profile_or_matching_scheme": True,
            "strict_no_knob_low_scale_weak_angle": True,
            "one_universal_parameter_selection": True,
        },
        "rank_reduction": {
            "before_B9": "raw objects x, mu_Theta, T1, T2, RG/matching scheme, effective kappa profile",
            "after_B9_general_one_loop": "source-selected pair (u1,u2) plus declared scheme",
            "after_B9_no_threshold_one_loop": "single source-selected profile y plus declared no-threshold/scheme policy",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B9NextWork.v1",
        "status": "NEXT_WORKORDER_SOURCE_PROFILE_OR_PRIMITIVE_SELECTION",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B10-SOURCE-PROFILE-SELECTION",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B10-SOURCE-y-OR-u1u2",
            "task": "Derive source-selected y in the no-threshold lane, or source-selected (u1,u2) in the general threshold lane, from End0/HYM/T1T2 sector transfer, flux torsion, or selected K_EW profile data.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B10-UNIVERSAL-PRIMITIVE-SELECTION",
            "task": "If strict no-knob source selection fails, test whether an independently selected single primitive P_univ can emit y_univ and simultaneously serve alpha1 or other constants without retuning.",
        },
        "forbidden_shortcuts": primitive["forbidden"],
    }

    theorem_proved = all(
        [
            b8["theorem"]["proved"] is True,
            b8_boundary["closed_now"]["flat_FP_quotient_policy_for_weaksplit"] is True,
            projection["promotion_tests"]["trace_free_exceptional_plane_closed"] is True,
            contract["status"] == "K_EW_CONTRACT_BUILT_VALUES_OPEN",
            abs(high_scale_replayed - high_scale_sin2) < 1e-15,
            t1t2_cert["path_A_T1T2_covariant_Green_closed"] is True,
        ]
    )

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB9ProfileReductionAndUniversalParameterGate",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B9-PROFILE-REDUCTION-AND-PRIMITIVE-GATE",
        "output_packets": {
            "one_loop_profile_reduction": rel(PROFILE),
            "superset_imports_critical": rel(IMPORTS),
            "one_universal_parameter_gate": rel(PRIMITIVE),
            "weak_mixing_b9_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B9ProfileReductionTheorem",
            "proved": theorem_proved,
            "statement": (
                "Given the selected ratio r12 and the B6 one-loop K_EW contract, "
                "the low-scale weak-angle problem reduces to source-selected "
                "profile combinations u1=x*(b1*L/(8*pi^2)+T1) and "
                "u2=x*(b2*L/(8*pi^2)+T2).  In the no-threshold lane it reduces "
                "further to a single dimensionless profile y=x*L/(8*pi^2).  "
                "The T1/T2 covariant Green import supplies operator support but "
                "not sector amplitudes.  A one-universal-parameter extension is "
                "admissible only if the primitive is selected upstream and not "
                "from the weak-angle target."
            ),
        },
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B9_ProfileReductionAndUniversalParameterGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "r12": r12,
        "high_scale_tree_sin2": high_scale_sin2,
        "one_loop_profile_reduction_closed": True,
        "no_threshold_single_y_lane_closed": True,
        "T1T2_operator_support_imported": True,
        "one_universal_parameter_gate_ready": True,
        "strict_no_knob_physical_weak_angle_closed": False,
        "one_universal_parameter_selected": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B9 Profile Reduction and Universal Parameter Gate v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B9-PROFILE-REDUCTION-AND-PRIMITIVE-GATE`

## Result

B9 does not close the physical weak mixing angle.  It does something narrower
and useful: it reduces the remaining one-loop problem to source-selected
profile combinations.

General one-loop lane:

```text
u1 = x*(b1*L/(8*pi^2) + T1)
u2 = x*(b2*L/(8*pi^2) + T2)
sin2 = 3*(1+u2)/(3*(1+u2)+5*(1/r12+u1))
```

No-threshold lane:

```text
y = x*L/(8*pi^2)
sin2(y)=3*(1+b2*y)/(3*(1+b2*y)+5*(1/r12+b1*y))
```

with:

- `r12 = {r12}`,
- `b1 = {B1}`,
- `b2 = {B2}`,
- `sin2(0) = {high_scale_replayed}`.

The high-scale value exactly replays B5.  The low-scale/effective value still
requires a source-selected `y` or source-selected `(u1,u2)`.

## Superset Import

The SM-parity T1/T2 covariant Green result is imported as operator support:
the coupled diagonal End0 `T1/T2` Green is closed, but sector routing,
off-diagonal Ext/HYM control, and physical amplitudes are not.

## Universal Parameter Policy

A one-universal-parameter extension is admissible as a labeled non-no-knob lane
if the primitive is selected once upstream and shared across sectors.  It is
forbidden to choose that primitive from the weak angle, alpha_EM, or any target
constant while claiming no-knob closure.

## Next

`CONST-EW-02 / WEAK-MIXING / B10-SOURCE-y-OR-u1u2`
"""

    for path, payload in [
        (PROFILE, profile),
        (IMPORTS, imports),
        (PRIMITIVE, primitive),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
