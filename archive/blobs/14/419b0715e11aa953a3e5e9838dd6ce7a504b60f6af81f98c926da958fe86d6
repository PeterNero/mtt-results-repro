"""Build CONST-EW-02 B11 loop-volume bridge proof attempt.

B11 attacks the requested bridge

    x*log(mu_Theta/MZ) = sqrt(15/log(448)).

The current source record supports the right-hand side, but still lacks a
source theorem for x, mu_Theta, or their product.  This builder therefore
proves the conditional bridge and records a rigorous current-source
underdetermination obstruction for strict no-knob promotion.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b11_loop_volume_bridge_proof_attempt"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PROOF_ATTEMPT = BASE / "selected_loop_volume_bridge_proof_attempt.packet.json"
UNDERDET = BASE / "current_source_underdetermination.packet.json"
CONDITIONAL = BASE / "conditional_one_primitive_bridge.packet.json"
BOUNDARY = BASE / "weak_mixing_b11_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B11_LoopVolumeBridgeProofAttempt_v1.md"

STATUS = "MTT_CONST_EW_02_B11_CONDITIONAL_BRIDGE_PROVED_STRICT_SOURCE_OBSTRUCTION"

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

    b10_path = DATA / "const_ew_02_weak_mixing_b10_loop_volume_profile_candidate.candidate.json"
    b10_bridge_path = DATA / "const_ew_02_weak_mixing_b10_loop_volume_profile_candidate" / "loop_volume_bridge_requirement.packet.json"
    b10_candidates_path = DATA / "const_ew_02_weak_mixing_b10_loop_volume_profile_candidate" / "source_y_candidates.packet.json"
    b9_profile_path = DATA / "const_ew_02_weak_mixing_b9_profile_reduction_and_universal_parameter_gate" / "one_loop_profile_reduction.packet.json"
    execution_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "execution_formulae.packet.json"
    primitive_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"
    nonsm_exhaustion_path = NONSM / "proof_corpus" / "Electroweak_No_Knob_Closure_Source_Exhaustion_Theorem_v1.md"
    qa_rg_path = QA_SU3 / "candidate_data" / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json"
    qa_norm_path = QA_SU3 / "candidate_data" / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json"

    b10 = load(b10_path)
    b10_bridge = load(b10_bridge_path)
    b10_candidates = load(b10_candidates_path)
    b9_profile = load(b9_profile_path)
    execution = load(execution_path)
    primitive = load(primitive_path)
    qa_rg = load(qa_rg_path)
    qa_norm = load(qa_norm_path)

    r12 = float(b9_profile["reduction"]["high_scale_check"]["computed"])
    # The B9 profile packet stores high-scale sin2 in the high-scale check, not r12.
    # Recover r12 from sin2 = 3r/(3r+5).
    r_ratio = (5.0 * r12) / (3.0 * (1.0 - r12))
    inv_sqrt_tau = float(execution["dimensionless_internal_values"]["inv_sqrt_tau_int"])
    y_loop = inv_sqrt_tau / (8.0 * math.pi * math.pi)
    sin2_if_bridge = sin2_from_y(r_ratio, y_loop)
    sample_L = math.log(5000.0 / 91.1876)
    x_if_5tev_scaffold = inv_sqrt_tau / sample_L
    g2_if_5tev_scaffold = math.sqrt(x_if_5tev_scaffold)

    proof_attempt = {
        "schema": "MTTConstEW02B11SelectedLoopVolumeBridgeProofAttempt.v1",
        "status": "STRICT_BRIDGE_NOT_PROVED_CONDITIONAL_FORM_PROVED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B11-LOOP-VOLUME-BRIDGE-PROOF-ATTEMPT",
        "inputs": {
            "B10_candidate": rel(b10_path),
            "B10_bridge_requirement": rel(b10_bridge_path),
            "B10_source_y_candidates": rel(b10_candidates_path),
            "B9_profile_reduction": rel(b9_profile_path),
            "alpha1_execution_formulae": rel(execution_path),
            "one_universal_primitive_policy": rel(primitive_path),
            "nonsm_source_exhaustion": rel(nonsm_exhaustion_path),
            "qa_su3_physicalanchor_rg": rel(qa_rg_path),
            "qa_su3_gaugekinetic_rg_scheme": rel(qa_norm_path),
        },
        "right_hand_side_source": {
            "emitted": True,
            "value": inv_sqrt_tau,
            "expression": "sqrt(15/log(448))",
            "source": rel(execution_path),
        },
        "left_hand_side_source": {
            "x_g2_muTheta_squared_selected": False,
            "L_log_muTheta_over_MZ_selected": False,
            "product_xL_selected": False,
            "corpus_status": "OPEN",
        },
        "conditional_algebra": {
            "if_xL_equals_inv_sqrt_tau": {
                "y": y_loop,
                "sin2_no_threshold_one_loop": sin2_if_bridge,
                "proved_by_substitution_into_B9": True,
            },
            "if_use_old_5TeV_scaffold_as_diagnostic_only": {
                "L_5TeV_over_MZ": sample_L,
                "x_required": x_if_5tev_scaffold,
                "g2_required": g2_if_5tev_scaffold,
                "classification": "DIAGNOSTIC_NOT_SELECTION",
            },
        },
        "strict_no_knob_verdict": {
            "bridge_proved": False,
            "reason": (
                "The current source packets emit the right-hand metrology invariant "
                "but do not emit x, mu_Theta, L, or the product xL as selected "
                "electroweak K_EW data."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    underdet = {
        "schema": "MTTConstEW02B11CurrentSourceUnderdetermination.v1",
        "status": "CURRENT_SOURCE_UNDERDETERMINATION_PROVED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B11-UNDERDETERMINATION",
        "lemma": {
            "name": "xLProductIndependenceUnlessK_EWEmitsProduct",
            "proved": True,
            "statement": (
                "Given only a selected value C=sqrt(15/log(448)) and the B9 "
                "formula, the equation x*L=C is not forced unless a source theorem "
                "selects x, L, or their product. For any positive x there is an "
                "L=C/x; for any positive L there is an x=C/L. Thus the bridge is "
                "a codimension-one source constraint, not a consequence of the "
                "currently emitted packets."
            ),
        },
        "compatibility_family": {
            "for_any_x_positive": "mu_Theta = MZ*exp(C/x)",
            "for_any_L_positive": "x = C/L",
            "consequence": "infinitely many positive pairs satisfy the bridge; infinitely many positive pairs do not",
        },
        "cross_repo_consistency": {
            "nonsm_exhaustion_theorem_blocks_full_no_knob_EW": True,
            "qa_su3_frontier_keeps_matching_scale_open": qa_rg["still_open"]["matching_scale_mu_match"] is True,
            "qa_su3_frontier_keeps_physical_gauge_action_anchor_open": qa_rg["still_open"]["physical_gauge_action_anchor"] is True,
            "qa_su3_route_selects_heterotic_threshold_kernel_values_open": qa_norm["decision"]["gaugekinetic_normalization_closed"] is False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    conditional = {
        "schema": "MTTConstEW02B11ConditionalOnePrimitiveBridge.v1",
        "status": "CONDITIONAL_ONE_PRIMITIVE_BRIDGE_CLOSED_NOT_SELECTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B11-CONDITIONAL-ONE-PRIMITIVE-BRIDGE",
        "primitive_policy": primitive["acceptance_policy"],
        "conditional_theorem": {
            "name": "OnePrimitiveEWProfileBridgeTheorem",
            "proved": True,
            "statement": (
                "If a single upstream universal primitive P_univ selects the "
                "dimensionless electroweak loop profile product xL and emits "
                "xL=sqrt(15/log(448)), then B9 and B10 yield a conditional "
                "no-threshold one-loop weak-angle value without using the weak "
                "angle as selector."
            ),
            "value_if_condition_met": {
                "xL": inv_sqrt_tau,
                "y": y_loop,
                "sin2_no_threshold_one_loop": sin2_if_bridge,
            },
        },
        "not_no_knob": True,
        "primitive_selected_now": False,
        "why_not_selected_now": "No current packet emits P_univ -> xL as a selected theorem-derived value.",
        "allowed_future_use": [
            "Declare P_univ once upstream.",
            "Show it emits xL before electroweak comparison.",
            "Reuse it across alpha1/GR/cosmology or other constants with predictive surplus.",
            "Report dependence on P_univ until independently measured or derived.",
        ],
        "forbidden_future_use": [
            "Choose P_univ from the weak angle.",
            "Choose P_univ from alpha_EM and then call weak mixing no-knob.",
            "Retune P_univ per constant.",
            "Promote diagnostic 5 TeV scaffold as selected scale.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B11Boundary.v1",
        "status": "STRICT_BRIDGE_OPEN_CONDITIONAL_BRIDGE_CLOSED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B11-BOUNDARY",
        "closed_now": {
            "right_hand_metrology_invariant_sourced": True,
            "conditional_one_primitive_bridge_theorem": True,
            "current_source_underdetermination_obstruction": True,
            "diagnostic_5TeV_required_x_computed": True,
        },
        "still_open": {
            "strict_SelectedEWLoopVolumeProfileBridge": True,
            "source_emitted_xL_product": True,
            "source_selected_x": True,
            "source_selected_muTheta_or_L": True,
            "heterotic_or_rhoUV_K_EW_kernel": True,
            "threshold_precision_lane": True,
        },
        "next_live_object": "Selected_EW_ProfileProduct_SourceTheorem_or_HeteroticThresholdKernel_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B11NextWork.v1",
        "status": "NEXT_WORKORDER_SOURCE_EMIT_PROFILE_PRODUCT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B12-SOURCE-EMIT-xL-OR-KEW",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B12-PROFILE-PRODUCT-SOURCE",
            "task": "Search for or construct a same-branch theorem emitting xL=sqrt(15/log(448)) directly from K_EW, rho_UV response, heterotic/Strominger threshold data, or a selected universal primitive.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B12-HETEROTIC-THRESHOLD-KERNEL",
            "task": "Use the QA/SU3 and no-knob route discriminator to attempt the selected heterotic/Strominger electroweak threshold kernel that emits gauge normalization, mu_match, and scheme.",
        },
        "forbidden_shortcuts": conditional["forbidden_future_use"],
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB11LoopVolumeBridgeProofAttempt",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B11-LOOP-VOLUME-BRIDGE-PROOF-ATTEMPT",
        "output_packets": {
            "selected_loop_volume_bridge_proof_attempt": rel(PROOF_ATTEMPT),
            "current_source_underdetermination": rel(UNDERDET),
            "conditional_one_primitive_bridge": rel(CONDITIONAL),
            "weak_mixing_b11_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B11LoopVolumeBridgeAttemptTheorem",
            "proved": True,
            "statement": (
                "The current corpus proves the conditional bridge but not the "
                "strict source bridge.  The RHS sqrt(15/log(448)) is selected in "
                "the metrology/alpha1 packet, and substitution into B9 proves the "
                "conditional y value.  However, current source packets do not emit "
                "x, L, or xL.  Therefore strict no-knob promotion is blocked by "
                "underdetermination until K_EW, heterotic/Strominger thresholds, "
                "rho_UV response, or a declared universal primitive emits xL."
            ),
        },
        "strict_bridge_proved": False,
        "conditional_bridge_proved": True,
        "sin2_if_condition_met": sin2_if_bridge,
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B11_LoopVolumeBridgeProofAttempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_bridge_proved": False,
        "conditional_bridge_proved": True,
        "current_source_underdetermination_proved": True,
        "xL_rhs": inv_sqrt_tau,
        "y_if_condition_met": y_loop,
        "sin2_if_condition_met": sin2_if_bridge,
        "x_required_if_5TeV_scaffold_used": x_if_5tev_scaffold,
        "g2_required_if_5TeV_scaffold_used": g2_if_5tev_scaffold,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B11 Loop Volume Bridge Proof Attempt v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B11-LOOP-VOLUME-BRIDGE-PROOF-ATTEMPT`

## What Was Proved

The conditional bridge is now theorem-level:

```text
if x*log(mu_Theta/MZ) = sqrt(15/log(448)),
then y = sqrt(15/log(448))/(8*pi^2)
```

and B9 gives:

```text
y = {y_loop}
sin2_no_threshold_one_loop = {sin2_if_bridge}
```

No weak-angle observation is used as a selector.

## What Was Not Proved

The strict bridge:

```text
x*log(mu_Theta/MZ) = sqrt(15/log(448))
```

is not yet proved from the current corpus.  The right-hand side is sourced, but
the current packets do not source `x`, `L`, or their product.

This is a rigorous current-source obstruction, not merely a missing numerical
calculation.  For any positive `x`, one may choose `L=C/x`; for any positive
`L`, one may choose `x=C/L`.  Therefore a source theorem must emit the product.

## Diagnostic Only

Using the old `5 TeV` scaffold gives:

```text
L = {sample_L}
x_required = {x_if_5tev_scaffold}
g2_required = {g2_if_5tev_scaffold}
```

This is not a selection theorem.

## Next

`CONST-EW-02 / WEAK-MIXING / B12-SOURCE-EMIT-xL-OR-KEW`
"""

    for path, payload in [
        (PROOF_ATTEMPT, proof_attempt),
        (UNDERDET, underdet),
        (CONDITIONAL, conditional),
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
