"""Build CONST-EW-02 weak mixing angle source frontier.

This starts the second individual-constant branch after alpha1.  It imports
the closed internal weak-split data from CONST-EM-01 and turns it into a
strictly guarded weak-angle frontier: the internal split is usable, but a
physical sin^2(theta_W) value still requires a same-branch SU2 normalization,
scale, and RG/threshold profile.
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

SLUG = "const_ew_02_weak_mixing_angle_source_frontier"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORTS = BASE / "alpha1_imports.packet.json"
FORMULAE = BASE / "weak_angle_formulae.packet.json"
FRONTIER = BASE / "source_frontier.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixingAngle_SourceFrontier_v1.md"

STATUS = "MTT_CONST_EW_02_WEAK_MIXING_SOURCE_FRONTIER_BUILT_VALUE_OPEN"


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

    template_path = DATA / "const_em_01_alpha1_frontier_closure_ledger" / "next_constant_template.packet.json"
    handoff_path = DATA / "const_em_01_alpha1_frontier_closure_ledger" / "main_repo_handoff.packet.json"
    formula_map_path = DATA / "const_em_01_alpha1_convention_map" / "electroweak_formula_map.packet.json"
    comparison_path = DATA / "const_em_01_alpha1_convention_map" / "comparison_protocol.packet.json"
    weaksplit_path = DATA / "const_em_01_alpha1_internal_weaksplit_import" / "internal_threshold_promotion.packet.json"

    template = load(template_path)
    handoff = load(handoff_path)
    formula_map = load(formula_map_path)
    comparison = load(comparison_path)
    weaksplit = load(weaksplit_path)
    values = weaksplit["promoted_internal_values"]

    p_y = values["p_Y_internal"]
    p_su2 = values["p_SU2_weaksplit"]
    lambda_12 = values["lambda_12_internal"]
    delta_g12 = values["Delta_G12_internal"]

    import_checks = {
        "template_recommends_weak_mixing": any(
            target["target"] == "weak mixing angle / sin^2 theta_W"
            for target in template["candidate_next_targets"]
        ),
        "alpha1_handoff_ready": handoff["status"] == "HANDOFF_READY",
        "weak_mixing_formula_present": "weak_mixing" in formula_map["convention_equations"],
        "comparison_protocol_forbids_source_selectors": comparison["allowed_modes"]["no_knob_derivation"]["source_selector_allowed"] is False,
        "internal_weaksplit_closed": weaksplit["internal_closure_claimed"] is True,
        "physical_alpha_not_claimed": weaksplit["closure_claimed"] is False,
        "observed_data_not_used": (
            template["observed_data_used_as_selector"] is False
            and handoff["observed_data_used_as_selector"] is False
            and formula_map["observed_data_used_as_selector"] is False
            and comparison["observed_data_used_as_selector"] is False
            and weaksplit["observed_data_used_as_selector"] is False
        ),
        "target_fitting_not_used": (
            template["target_fitting_used"] is False
            and handoff["target_fitting_used"] is False
            and formula_map["target_fitting_used"] is False
            and comparison["target_fitting_used"] is False
            and weaksplit["target_fitting_used"] is False
        ),
    }
    import_ok = all(import_checks.values())

    imports = {
        "schema": "MTTConstEW02WeakMixingAlpha1Imports.v1",
        "status": "ALPHA1_IMPORTS_ACCEPTED_FOR_WEAK_ANGLE" if import_ok else "ALPHA1_IMPORTS_REJECTED_FOR_WEAK_ANGLE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B1-IMPORT-ALPHA1-WEAKSPLIT",
        "inputs": {
            "next_constant_template": rel(template_path),
            "alpha1_main_repo_handoff": rel(handoff_path),
            "electroweak_formula_map": rel(formula_map_path),
            "comparison_protocol": rel(comparison_path),
            "internal_weaksplit_values": rel(weaksplit_path),
        },
        "import_checks": import_checks,
        "imported_internal_values": {
            "p_Y_internal": p_y,
            "p_SU2_weaksplit": p_su2,
            "lambda_12_internal": lambda_12,
            "Delta_G12_internal": delta_g12,
        },
        "scope": "internal weak-split and electroweak convention support only",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    formulae = {
        "schema": "MTTConstEW02WeakAngleFormulae.v1",
        "status": "WEAK_ANGLE_FORMULAE_BUILT_CONDITIONAL_VALUE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B2-FORMULAE",
        "standard_formulae": {
            "hypercharge_convention": "alpha_1^GUT = (5/3) alpha_Y",
            "tree_angle": "s2W(mu) = alpha_Y(mu)/(alpha_Y(mu)+alpha_2(mu))",
            "inverse_coupling_ratio": "s2W(mu) = A2(mu)/(AY(mu)+A2(mu)), where AY=1/alpha_Y and A2=1/alpha_2",
            "on_shell_replay": "s2W_on_shell = 1 - M_W^2/M_Z^2",
            "effective_angle": "sin^2(theta_eff^l) = kappa_l(mu) s2W(mu)",
        },
        "selected_internal_split": {
            "p_Y_internal": p_y,
            "p_SU2_weaksplit": p_su2,
            "lambda_12_internal": lambda_12,
            "Delta_G12_internal": delta_g12,
            "exp_minus_lambda12": math.exp(-lambda_12),
            "logistic_of_lambda12": 1.0 / (1.0 + math.exp(lambda_12)),
        },
        "why_internal_split_is_not_the_angle": [
            "lambda_12 is a same-scheme internal weak-split row, not a physical coupling ratio.",
            "s2W requires the absolute inverse-coupling pair AY(mu), A2(mu), not only their internal difference.",
            "physical comparison requires scale, scheme, and threshold/profile declarations.",
            "the observed value cannot be used to choose the missing offset or profile.",
        ],
        "conditional_source_form": {
            "unknown_common_inverse_anchor": "A0(mu)",
            "AY_mu": "A0(mu) + delta_Y(mu)",
            "A2_mu": "A0(mu) + delta_2(mu)",
            "internal_constraint": "delta_Y(mu) - delta_2(mu) is constrained by the imported weak-split packet after declaring the map from p rows to inverse couplings",
            "s2W_mu": "(A0(mu)+delta_2(mu))/(2*A0(mu)+delta_Y(mu)+delta_2(mu))",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    frontier = {
        "schema": "MTTConstEW02WeakMixingSourceFrontier.v1",
        "status": "SOURCE_FRONTIER_BUILT_PHYSICAL_VALUE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B3-SOURCE-FRONTIER",
        "what_is_closed": {
            "weak_angle_selected_as_next_target": import_ok,
            "standard_formula_map_imported": import_ok,
            "internal_pY_pSU2_lambda12_imported": import_ok,
            "no_observed_angle_selector": True,
            "no_target_fit": True,
        },
        "what_remains_open": {
            "same_branch_SU2_physical_normalization": True,
            "common_inverse_coupling_anchor_A0": True,
            "map_from_internal_p_rows_to_physical_inverse_couplings": True,
            "matching_scale_and_scheme": True,
            "RG_threshold_profile": True,
            "effective_angle_kappa_factor": True,
            "numerical_sin2thetaW_prediction": True,
        },
        "superset_strategy": {
            "straight_path": "Use selected electroweak formulae and the imported alpha1 weak-split packet to define the physical target.",
            "superset_paths": [
                "Gauge-row path: promote SU2 and U1 rows into a same-scheme inverse-coupling packet.",
                "Mass-shell path: use W/Z/Higgs electroweak replay only as downstream parity data, never as selector.",
                "RG path: transport the selected source packet to a declared comparison scale.",
                "One-universal-primitive path: if strict no-knob fails, reuse the alpha1 rod/clock/action primitive only if selected target-independently.",
            ],
            "locked_target": "sin^2(theta_W)(mu) or sin^2(theta_eff^l) must be declared with scheme and scale before any numerical comparison.",
        },
        "theorem": {
            "name": "CONSTEW02WeakMixingSourceFrontierTheorem",
            "proved": import_ok,
            "statement": (
                "Given the alpha1 frontier handoff, electroweak convention map, and closed internal weak-split packet, "
                "the weak mixing angle branch is reduced to a precise source-promotion problem: construct same-branch "
                "physical alpha_Y and alpha_2 inverse-coupling data plus scale/profile transport.  No numerical weak "
                "angle is derived at this stage, and observed weak-angle values are forbidden as selectors."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02NextLabeledWorkorder.v1",
        "status": "NEXT_WORKORDER_SAME_BRANCH_SU2_PACKET",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B4-SU2-PHYSICAL-PACKET",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B4-SU2-PHYSICAL-PACKET",
            "task": "Construct a same-branch SU2 physical/source normalization packet and decide whether alpha_2 shares the alpha1 rod/clock/action anchor or requires an independent source row.",
        },
        "secondary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B5-RG-PROFILE",
            "task": "Declare scale/scheme and RG/threshold transport for comparing s2W(M_Z), low-energy running, or sin^2(theta_eff^l).",
        },
        "forbidden_shortcuts": [
            "backsolve A0 from measured sin^2(theta_W)",
            "identify lambda_12_internal directly with the physical angle",
            "use W/Z masses as source selectors",
            "claim sin^2(theta_eff^l) without kappa/profile data",
        ],
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingAngleSourceFrontier",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B1-B3-SOURCE-FRONTIER",
        "output_packets": {
            "alpha1_imports": rel(IMPORTS),
            "weak_angle_formulae": rel(FORMULAE),
            "source_frontier": rel(FRONTIER),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": frontier["what_is_closed"],
        "what_remains_open": frontier["what_remains_open"],
        "theorem": frontier["theorem"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixingAngle_SourceFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "next_primary": "CONST-EW-02 / WEAK-MIXING / B4-SU2-PHYSICAL-PACKET",
        "imported_lambda_12_internal": lambda_12,
        "physical_sin2thetaW_value_claimed": False,
        "same_branch_SU2_physical_packet_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EW 02 Weak Mixing Angle Source Frontier v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B1-B3-SOURCE-FRONTIER`

## Result

The weak mixing angle is now opened as the second individual-constant branch.
The alpha1 handoff, electroweak formula map, and internal weak-split packet are
accepted as source support.

Imported internal values:

- `p_Y_internal = {p_y}`,
- `p_SU2_weaksplit = {p_su2}`,
- `lambda_12_internal = {lambda_12}`,
- `Delta_G12_internal = {delta_g12}`.

This closes the target setup and internal split import.  It does not derive a
physical weak mixing angle.

## Formula Boundary

The target formula is

`sin^2(theta_W)(mu) = alpha_Y(mu)/(alpha_Y(mu)+alpha_2(mu))`.

Equivalently, with inverse couplings `AY=1/alpha_Y` and `A2=1/alpha_2`,

`sin^2(theta_W)(mu) = A2(mu)/(AY(mu)+A2(mu))`.

Therefore an internal weak split is not enough.  We still need the same-branch
physical `AY(mu)` and `A2(mu)` packet, including common anchor, scale, scheme,
and thresholds.

## Superset Use

We combine several encodings under a locked target:

- gauge-row path: U1/Y and SU2 source rows,
- mass-shell path: W/Z replay only as downstream parity check,
- RG path: scale/profile transport,
- one-universal-primitive path: only if the alpha1 primitive is selected
  target-independently and shared across sectors.

Forbidden shortcuts:

- backsolve from measured `sin^2(theta_W)`,
- identify `lambda_12_internal` directly with the physical angle,
- use W/Z masses as source selectors,
- claim `sin^2(theta_eff^l)` without the effective-profile `kappa` factor.

## Next

Next label: `CONST-EW-02 / WEAK-MIXING / B4-SU2-PHYSICAL-PACKET`.
"""

    for path, payload in [
        (IMPORTS, imports),
        (FORMULAE, formulae),
        (FRONTIER, frontier),
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
