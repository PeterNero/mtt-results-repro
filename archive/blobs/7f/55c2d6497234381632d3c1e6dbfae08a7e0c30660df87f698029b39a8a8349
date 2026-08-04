"""Build CONST-EW-02 B10 loop-volume profile candidate.

B9 reduced the no-threshold one-loop weak-angle lane to one dimensionless
profile y=x*log(mu_Theta/MZ)/(8*pi^2).  B10 tests source-side internal
dimensionless invariants as candidates for the numerator x*log(mu_Theta/MZ).
The best candidate found here is inv_sqrt_tau_int=sqrt(15/log(448)), imported
from the alpha1/metrology branch.  This is promising, but not yet a theorem:
the bridge equating x*L to inv_sqrt_tau_int remains open.
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

SLUG = "const_ew_02_weak_mixing_b10_loop_volume_profile_candidate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CANDIDATES = BASE / "source_y_candidates.packet.json"
BRIDGE = BASE / "loop_volume_bridge_requirement.packet.json"
BOUNDARY = BASE / "weak_mixing_b10_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B10_LoopVolumeProfileCandidate_v1.md"

STATUS = "MTT_CONST_EW_02_B10_LOOP_VOLUME_PROFILE_CANDIDATE_FOUND_BRIDGE_OPEN"

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


def sin2_from_y(r12: float, y: float) -> float:
    a1x = 1.0 / r12 + B1 * y
    a2x = 1.0 + B2 * y
    return (3.0 * a2x) / (3.0 * a2x + 5.0 * a1x)


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b9_profile_path = DATA / "const_ew_02_weak_mixing_b9_profile_reduction_and_universal_parameter_gate" / "one_loop_profile_reduction.packet.json"
    b9_candidate_path = DATA / "const_ew_02_weak_mixing_b9_profile_reduction_and_universal_parameter_gate.candidate.json"
    execution_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "execution_formulae.packet.json"
    primitive_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"
    b5_ratio_path = DATA / "const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import" / "theta_ratio_high_scale_packet.packet.json"

    b9_profile = load(b9_profile_path)
    b9_candidate = load(b9_candidate_path)
    execution = load(execution_path)
    primitive = load(primitive_path)
    ratio = load(b5_ratio_path)

    r12 = float(ratio["ratio_source"]["value"])
    internal = execution["dimensionless_internal_values"]
    tau = float(internal["tau_int"])
    sqrt_tau = float(internal["sqrt_tau_int"])
    inv_sqrt_tau = float(internal["inv_sqrt_tau_int"])
    omega_over_sqrt_alpha = float(internal["Omega0_over_sqrt_alpha_phys"])
    gap_over_sqrt_alpha = float(internal["Lambda_gap_phys_over_sqrt_alpha_phys"])
    lambda_internal = float(internal["lambda_internal"])

    raw_candidates = [
        ("tau_int", tau, "dimensionless tau_int=log(448)/15"),
        ("sqrt_tau_int", sqrt_tau, "dimensionless metrology square-root coefficient"),
        ("inv_sqrt_tau_int", inv_sqrt_tau, "dimensionless inverse clock/rod coefficient sqrt(15/log(448))"),
        ("Omega0_over_sqrt_alpha_phys", omega_over_sqrt_alpha, "same numeric source as inv_sqrt_tau_int in the alpha1 anchor packet"),
        ("Lambda_gap_over_sqrt_alpha_phys", gap_over_sqrt_alpha, "dimensionless modal gap coefficient"),
        ("1/lambda_internal", 1.0 / lambda_internal, "inverse internal eigenvalue lambda=15"),
        ("sqrt_tau_int/lambda_internal", sqrt_tau / lambda_internal, "suppressed metrology coefficient"),
    ]
    rows = []
    for name, numerator, source_role in raw_candidates:
        y = numerator / (8.0 * math.pi * math.pi)
        rows.append(
            {
                "name": name,
                "source_role": source_role,
                "profile_numerator_candidate": numerator,
                "y_candidate": y,
                "sin2_no_threshold_one_loop_if_bridge_holds": sin2_from_y(r12, y),
                "promoted": False,
                "classification": "SOURCE_CANDIDATE_BRIDGE_OPEN",
            }
        )

    best = next(row for row in rows if row["name"] == "inv_sqrt_tau_int")
    exact_expression = "sqrt(15/log(448))/(8*pi^2)"

    candidates = {
        "schema": "MTTConstEW02B10SourceYCandidates.v1",
        "status": "SOURCE_Y_CANDIDATES_EMITTED_BRIDGE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B10-SOURCE-y-CANDIDATES",
        "inputs": {
            "B9_profile_reduction": rel(b9_profile_path),
            "alpha1_dimensional_anchor_execution": rel(execution_path),
            "one_universal_primitive_policy": rel(primitive_path),
        },
        "loop_volume_rule_tested": {
            "candidate_rule": "y = C_source/(8*pi^2)",
            "why_allowed_as_test": "8*pi^2 is already the one-loop RG volume in the B6/B9 contract; C_source is imported from source-side alpha1/metrology data, not from weak-angle data.",
            "why_not_promoted": "No theorem currently identifies C_source with x*log(mu_Theta/MZ) or with a selected K_EW profile integral.",
        },
        "candidate_rows": rows,
        "best_structural_candidate": {
            "name": best["name"],
            "exact_y_expression": exact_expression,
            "y_candidate": best["y_candidate"],
            "sin2_if_bridge_holds": best["sin2_no_threshold_one_loop_if_bridge_holds"],
            "selection_reason": (
                "It is the already-selected inverse metrology coefficient and equals "
                "Omega0/sqrt(alpha_phys) in the alpha1 anchor execution packet; "
                "placing it over the universal one-loop volume gives the cleanest "
                "same-branch profile candidate."
            ),
            "promoted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    bridge = {
        "schema": "MTTConstEW02B10LoopVolumeBridgeRequirement.v1",
        "status": "BRIDGE_LEMMA_SHARPLY_IDENTIFIED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B10-LOOP-VOLUME-BRIDGE",
        "required_lemma": {
            "name": "SelectedEWLoopVolumeProfileBridge",
            "statement": (
                "For the selected branch and declared one-loop no-threshold scheme, "
                "x*log(mu_Theta/MZ) = inv_sqrt_tau_int = sqrt(15/log(448)), "
                "or more generally the K_EW profile integral emits the same y."
            ),
            "equivalent_forms": [
                "y = inv_sqrt_tau_int/(8*pi^2)",
                "x*L = inv_sqrt_tau_int",
                "integral_{MZ}^{muTheta} g2(muTheta)^2 dlog(mu)/(8*pi^2) = inv_sqrt_tau_int/(8*pi^2)",
                "K_EW[B]_profile = sqrt(15/log(448))/(8*pi^2)",
            ],
            "what_would_close_if_proved": [
                "source-selected no-threshold one-loop y",
                "conditional weak-angle prediction in the B9 formula",
                "one-universal-profile bridge from alpha1/metrology into weak mixing",
            ],
            "what_it_still_would_not_close": [
                "two-loop/electroweak threshold precision",
                "threshold-lane T1,T2 amplitudes",
                "strict no-knob alpha_phys physical normalization",
            ],
        },
        "superset_strategy": {
            "straight_path": "Prove x*L=inv_sqrt_tau_int directly from the selected K_EW overlap/profile kernel.",
            "support_path": "Use the alpha1 metrology invariant as a universal primitive candidate shared across constants.",
            "locked_target": "source-side loop profile y, not observed weak angle.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B10Boundary.v1",
        "status": "PROMISING_PROFILE_CANDIDATE_FOUND_BUT_NOT_PROMOTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B10-BOUNDARY",
        "closed_now": {
            "source_side_y_candidate_table_built": True,
            "best_loop_volume_candidate_identified": True,
            "bridge_lemma_named": True,
            "one_universal_parameter_role_sharpened": True,
        },
        "still_open": {
            "SelectedEWLoopVolumeProfileBridge": True,
            "source_selected_y_promoted": True,
            "strict_no_knob_low_scale_weak_angle": True,
            "threshold_precision_lane": True,
            "two_loop_or_effective_scheme": True,
        },
        "guardrail": "The near numerical behavior of y=inv_sqrt_tau_int/(8*pi^2) is evidence for a bridge search, not a proof and not a fitted prediction.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B10NextWork.v1",
        "status": "NEXT_WORKORDER_PROVE_LOOP_VOLUME_PROFILE_BRIDGE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B11-SELECTED-LOOP-VOLUME-PROFILE-BRIDGE",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B11-PROVE-xL-EQUALS-inv_sqrt_tau",
            "task": "Prove or refute x*log(mu_Theta/MZ)=sqrt(15/log(448)) from selected K_EW overlap/profile data, without using observed weak-angle values.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B11-THRESHOLD-LANE-CONTROL",
            "task": "If the no-threshold bridge is too strong, derive selected threshold corrections T1,T2 around the same source candidate and quantify their source-side size.",
        },
        "forbidden_shortcuts": [
            "select inv_sqrt_tau because it matches a measured weak angle",
            "declare the bridge proved from numerical closeness",
            "reuse electroweak measurements to choose x or mu_Theta",
        ],
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB10LoopVolumeProfileCandidate",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B10-LOOP-VOLUME-PROFILE-CANDIDATE",
        "output_packets": {
            "source_y_candidates": rel(CANDIDATES),
            "loop_volume_bridge_requirement": rel(BRIDGE),
            "weak_mixing_b10_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B10LoopVolumeProfileCandidateTheorem",
            "proved": b9_candidate["theorem"]["proved"] is True and b9_profile["reduction"]["no_threshold_one_profile_lane"]["definition"] == "y=x*L/(8*pi^2), T1=T2=0",
            "statement": (
                "The selected alpha1/metrology packet emits the dimensionless "
                "source coefficient inv_sqrt_tau_int=sqrt(15/log(448)).  Placing "
                "this coefficient over the universal one-loop volume 8*pi^2 "
                "defines a source-side candidate y_loop for the B9 no-threshold "
                "profile.  This identifies a sharp bridge lemma, but does not "
                "itself promote a physical weak-angle prediction."
            ),
        },
        "best_candidate": candidates["best_structural_candidate"],
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B10_LoopVolumeProfileCandidate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "best_y_candidate": best["y_candidate"],
        "best_y_exact_expression": exact_expression,
        "sin2_if_bridge_holds": best["sin2_no_threshold_one_loop_if_bridge_holds"],
        "bridge_lemma_proved": False,
        "source_selected_y_promoted": False,
        "physical_weak_angle_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B10 Loop Volume Profile Candidate v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B10-LOOP-VOLUME-PROFILE-CANDIDATE`

## Candidate Found

B9 reduced the no-threshold one-loop profile to:

```text
y = x*log(mu_Theta/MZ)/(8*pi^2)
```

The alpha1/metrology branch already emits:

```text
inv_sqrt_tau_int = sqrt(15/log(448)) = {inv_sqrt_tau}
```

The clean source-side candidate is therefore:

```text
y_loop = sqrt(15/log(448))/(8*pi^2) = {best["y_candidate"]}
```

Inserted into the B9 no-threshold one-loop formula, this would give:

```text
sin2_if_bridge_holds = {best["sin2_no_threshold_one_loop_if_bridge_holds"]}
```

This is not promoted as a prediction.  The bridge is still missing.

## Required Bridge

`SelectedEWLoopVolumeProfileBridge`:

```text
x*log(mu_Theta/MZ) = sqrt(15/log(448))
```

or equivalently:

```text
K_EW[B]_profile = sqrt(15/log(448))/(8*pi^2)
```

## Guardrail

The candidate was selected from existing source-side alpha1/metrology data and
the universal one-loop volume.  It was not selected from the observed weak
angle.  Its numerical behavior is a reason to attack the bridge lemma, not a
proof of closure.

## Next

`CONST-EW-02 / WEAK-MIXING / B11-PROVE-xL-EQUALS-inv_sqrt_tau`
"""

    for path, payload in [
        (CANDIDATES, candidates),
        (BRIDGE, bridge),
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
