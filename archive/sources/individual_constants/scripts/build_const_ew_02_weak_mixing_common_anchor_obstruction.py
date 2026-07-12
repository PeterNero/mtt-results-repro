"""Build CONST-EW-02 common-anchor obstruction theorem.

The weak mixing angle is a ratio.  The imported internal weak split supplies
same-scheme difference data, but difference data alone cannot determine the
ratio unless the common inverse-coupling anchor is also selected.  This script
formalizes that gate and prepares the next search object.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_common_anchor_obstruction"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DERIVATION = BASE / "ratio_from_difference_derivation.packet.json"
ANCHOR_TEST = BASE / "common_anchor_selection_test.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_CommonAnchorObstruction_v1.md"

STATUS = "MTT_CONST_EW_02_COMMON_ANCHOR_OBSTRUCTION_PROVED_VALUE_OPEN"


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


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    frontier_path = DATA / "const_ew_02_weak_mixing_angle_source_frontier.candidate.json"
    formulae_path = DATA / "const_ew_02_weak_mixing_angle_source_frontier" / "weak_angle_formulae.packet.json"
    weaksplit_path = DATA / "const_em_01_alpha1_internal_weaksplit_import" / "internal_threshold_promotion.packet.json"
    alpha1_primitive_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"

    frontier = load(frontier_path)
    formulae = load(formulae_path)
    weaksplit = load(weaksplit_path)
    alpha1_primitive = load(alpha1_primitive_path)
    values = weaksplit["promoted_internal_values"]

    lambda_12 = values["lambda_12_internal"]
    delta_g12 = values["Delta_G12_internal"]
    p_y = values["p_Y_internal"]
    p_su2 = values["p_SU2_weaksplit"]

    # If inverse couplings are AY=A0+dY and A2=A0+d2, only D=dY-d2 is known.
    # The angle as a function of A0 and D, after choosing centered offsets
    # dY=+D/2 and d2=-D/2, is s2=(A0-D/2)/(2*A0).  This is a one-parameter
    # family, so the split cannot select a unique angle.
    sample_family = []
    for a0 in [10.0, 25.0, 50.0, 100.0]:
        sample_family.append(
            {
                "A0": a0,
                "s2_from_centered_internal_lambda12": (a0 - lambda_12 / 2.0) / (2.0 * a0),
                "s2_from_centered_Delta_G12": (a0 - delta_g12 / 2.0) / (2.0 * a0),
            }
        )

    derivation = {
        "schema": "MTTConstEW02RatioFromDifferenceDerivation.v1",
        "status": "DIFFERENCE_DATA_DOES_NOT_SELECT_RATIO",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B4-COMMON-ANCHOR-OBSTRUCTION",
        "imported_values": {
            "p_Y_internal": p_y,
            "p_SU2_weaksplit": p_su2,
            "lambda_12_internal": lambda_12,
            "Delta_G12_internal": delta_g12,
        },
        "algebra": {
            "inverse_couplings": "AY=A0+dY, A2=A0+d2",
            "known_split": "D=dY-d2",
            "tree_angle": "s2W=A2/(AY+A2)",
            "centered_offsets": "dY=D/2, d2=-D/2",
            "one_parameter_family": "s2W(A0,D)=(A0-D/2)/(2*A0)",
            "consequence": "For fixed nonzero D, changing A0 changes s2W while preserving the same split D.",
        },
        "sample_nonuniqueness_witness": sample_family,
        "proof_result": "The weak-split packet fixes a difference class, not the absolute common inverse-coupling anchor; therefore it cannot by itself select a unique physical weak mixing angle.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    primitive_ready = alpha1_primitive["status"] == "ONE_UNIVERSAL_PRIMITIVE_EXTENSION_READY"
    anchor_test = {
        "schema": "MTTConstEW02CommonAnchorSelectionTest.v1",
        "status": "COMMON_ANCHOR_NOT_SELECTED_BY_CURRENT_SOURCE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B4-COMMON-ANCHOR-OBSTRUCTION",
        "strict_no_knob_tests": {
            "same_branch_A0_packet_exists": False,
            "A0_selected_without_measured_weak_angle": False,
            "A0_selected_without_measured_alpha": False,
            "SU2_physical_anchor_selected": False,
            "RG_scale_profile_selected": False,
        },
        "one_primitive_lane": {
            "alpha1_one_primitive_ready": primitive_ready,
            "can_share_primitive_conditionally": primitive_ready,
            "still_needs_SU2_and_RG_map": True,
            "not_no_knob_closure": True,
        },
        "accepted_closure_level": "obstruction theorem plus next search target",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02NextWorkAfterCommonAnchorObstruction.v1",
        "status": "NEXT_WORKORDER_FIND_A0_OR_REPLAY_LANE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B5-A0-SOURCE-SEARCH",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B5-A0-SOURCE-SEARCH",
            "task": "Search corpus/repos for a same-branch common inverse-coupling anchor A0 for U1/Y and SU2, independent of measured alpha or weak-angle values.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B5-PARITY-REPLAY",
            "task": "Build a downstream SM-parity replay lane using declared external weak-angle schemes, explicitly forbidden from source selection.",
        },
        "source_terms_to_search": [
            "common inverse coupling anchor",
            "A0",
            "SU2 row",
            "weak split",
            "Weinberg angle",
            "electroweak mixing",
            "theta closure",
            "rod clock action unit",
            "shared circle",
        ],
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingCommonAnchorObstruction",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B4-COMMON-ANCHOR-OBSTRUCTION",
        "imports": {
            "source_frontier": rel(frontier_path),
            "weak_angle_formulae": rel(formulae_path),
            "internal_weaksplit_values": rel(weaksplit_path),
            "alpha1_one_primitive_lane": rel(alpha1_primitive_path),
        },
        "output_packets": {
            "ratio_from_difference_derivation": rel(DERIVATION),
            "common_anchor_selection_test": rel(ANCHOR_TEST),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "difference_data_insufficient_for_ratio_theorem": True,
            "common_anchor_A0_identified_as_required_object": True,
            "one_primitive_lane_preserved_but_guardrailed": True,
            "observed_value_backsolve_forbidden": True,
        },
        "what_remains_open": {
            "same_branch_A0_source": True,
            "SU2_physical_anchor": True,
            "RG_scale_profile": True,
            "numerical_sin2thetaW_prediction": True,
        },
        "theorem": {
            "name": "CONSTEW02CommonAnchorObstructionTheorem",
            "proved": True,
            "statement": (
                "The imported U1/Y-SU2 weak split fixes only difference data.  Because "
                "sin^2(theta_W)=A2/(AY+A2) depends on the common inverse-coupling anchor A0 as well as the split, "
                "there is a one-parameter family of weak angles preserving the same split.  Therefore the next required "
                "source object is a target-independent same-branch A0/SU2 physical packet or a labeled parity replay lane."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_CommonAnchorObstruction_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "next_primary": "CONST-EW-02 / WEAK-MIXING / B5-A0-SOURCE-SEARCH",
        "lambda_12_internal": lambda_12,
        "Delta_G12_internal": delta_g12,
        "A0_source_closed": False,
        "physical_sin2thetaW_value_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EW 02 Weak Mixing Common Anchor Obstruction v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B4-COMMON-ANCHOR-OBSTRUCTION`

## Theorem

The imported internal weak split is real progress, but it is difference data.
The physical weak angle is a ratio.

Write inverse couplings as

`AY = A0 + dY`, `A2 = A0 + d2`,

with known split

`D = dY - d2`.

Then

`sin^2(theta_W) = A2 / (AY + A2)`.

Using centered offsets `dY=D/2`, `d2=-D/2` gives

`sin^2(theta_W)(A0,D) = (A0 - D/2)/(2 A0)`.

So the same internal split allows a one-parameter family of weak angles unless
the common inverse-coupling anchor `A0` is selected independently.

## Imported Split

- `lambda_12_internal = {lambda_12}`,
- `Delta_G12_internal = {delta_g12}`.

Neither is the physical weak angle.

## Result

Closed now:

- weak-split insufficiency theorem,
- `A0` identified as the missing source object,
- one-primitive lane preserved but labeled as non-no-knob,
- measured-value backsolve forbidden.

Open:

- same-branch `A0` source,
- SU2 physical/source anchor,
- RG/scale/profile transport,
- numerical `sin^2(theta_W)` prediction.

## Next

Next label: `CONST-EW-02 / WEAK-MIXING / B5-A0-SOURCE-SEARCH`.
"""

    for path, payload in [
        (DERIVATION, derivation),
        (ANCHOR_TEST, anchor_test),
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
