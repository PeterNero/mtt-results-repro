"""Build CONST-EW-02 B5 A0-or-ratio kernel import.

B4 proved that internal difference data does not determine a weak-angle ratio.
This B5 step searches sibling repos and imports the strongest available
alternative: a Theta overlap ratio r_12.  A selected ratio can determine a
high-scale tree weak angle without a common A0 anchor, while the physical
low-scale/effective angle still requires RG and threshold data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
SMPARITY = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b5_a0_or_ratio_kernel_import"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SEARCH = BASE / "cross_repo_source_search.packet.json"
RATIO = BASE / "theta_ratio_high_scale_packet.packet.json"
REPLAY = BASE / "sm_parity_replay_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B5_A0_or_RatioKernelImport_v1.md"

STATUS = "MTT_CONST_EW_02_B5_RATIO_EDGE_IMPORTED_HIGH_SCALE_TREE_VALUE_LOW_SCALE_OPEN"


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


def high_scale_sin2_from_r12(r12: float) -> float:
    return (3.0 * r12) / (3.0 * r12 + 5.0)


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b4_path = DATA / "const_ew_02_weak_mixing_common_anchor_obstruction.candidate.json"
    threshold_reduction_path = NONSM / "certificates" / "selected_electroweak_threshold_kernel_reduction_certificate.json"
    threshold_note_path = NONSM / "proof_corpus" / "Selected_Electroweak_Threshold_Kernel_Reduction_v1.md"
    candidate_computation_path = NONSM / "certificates" / "selected_electroweak_kernel_candidate_computation_certificate.json"
    sm_replay_path = SMPARITY / "candidate_data" / "sm_equivalence_mixing_and_gauge_replay.candidate.json"

    b4 = load(b4_path)
    threshold = load(threshold_reduction_path)
    candidate_computation = load(candidate_computation_path)
    sm_replay = load(sm_replay_path) if sm_replay_path.exists() else {}

    r12 = threshold["theta_ratio"]["source_value"]
    tree_sin2 = high_scale_sin2_from_r12(r12)
    recorded_tree_sin2 = threshold["numeric_diagnostic"]["high_scale_tree_sin2_from_r12"]
    diagnostic = candidate_computation["computed"]["sin2_diagnostic"]

    search_checks = {
        "b4_common_anchor_obstruction_proved": b4["theorem"]["proved"] is True,
        "nonsm_threshold_reduction_present": threshold["status"] == "ELECTROWEAK_KERNEL_REDUCED_TO_NORMALIZATION_AND_THRESHOLD_VECTOR",
        "theta_ratio_present": threshold["theta_ratio"]["definition"] == "g1(mu_Theta)^2/g2(mu_Theta)^2 = I2(Theta)/I1(Theta)",
        "high_scale_tree_formula_matches": abs(tree_sin2 - recorded_tree_sin2) < 1e-15,
        "low_energy_closure_denied": threshold["verdict"]["low_energy_weak_angle_closed"] is False,
        "kernel_candidate_direct_import_rejected": candidate_computation["classification"]["direct_import_as_electroweak_prediction"] is False,
        "sm_parity_replay_available": bool(sm_replay),
    }
    search_ok = all(search_checks.values())

    search = {
        "schema": "MTTConstEW02B5CrossRepoSourceSearch.v1",
        "status": "RATIO_EDGE_FOUND_A0_STILL_OPEN" if search_ok else "B5_IMPORT_INCOMPLETE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B5-A0-SOURCE-SEARCH",
        "inputs": {
            "B4_common_anchor_obstruction": rel(b4_path),
            "nonsm_threshold_reduction_certificate": rel(threshold_reduction_path),
            "nonsm_threshold_reduction_note": rel(threshold_note_path),
            "nonsm_kernel_candidate_computation_certificate": rel(candidate_computation_path),
            "sm_parity_replay_candidate": rel(sm_replay_path),
        },
        "search_checks": search_checks,
        "classification": {
            "A0_path": "still open in strict no-knob lane",
            "Theta_ratio_path": "live high-scale ratio edge; bypasses A0 only for tree-level high-scale ratio",
            "physical_MZ_or_effective_path": "still open; requires K_EW -> (mu_Theta, x, T1, T2, scheme) or equivalent",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    ratio = {
        "schema": "MTTConstEW02ThetaRatioHighScalePacket.v1",
        "status": "HIGH_SCALE_TREE_RATIO_EVALUATED_LOW_SCALE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B5-THETA-RATIO-EDGE",
        "ratio_source": {
            "symbol": "r_12",
            "value": r12,
            "definition": threshold["theta_ratio"]["definition"],
            "source_status": threshold["status"],
            "imported_as": "cross-repo selected-ratio candidate; not yet local no-knob physical closure",
        },
        "formula": {
            "high_scale_tree": "sin^2(theta_W)(mu_Theta) = (3*r_12)/(3*r_12+5)",
            "computed_value": tree_sin2,
            "recorded_source_value": recorded_tree_sin2,
        },
        "why_this_bypasses_B4": [
            "B4 blocks ratio extraction from difference data alone.",
            "A directly selected coupling ratio r_12 is stronger than difference data.",
            "The ratio edge determines only the high-scale tree identity, not the low-scale/effective observable.",
        ],
        "why_this_is_not_final_physical_closure": [
            "x=g2(mu_Theta)^2 is not selected.",
            "mu_Theta is not selected.",
            "T1 and T2 are not selected.",
            "RG/matching scheme is not selected.",
            "candidate threshold direct import is rejected by the sibling repo.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    replay = {
        "schema": "MTTConstEW02SMParityReplayBoundary.v1",
        "status": "PARITY_REPLAY_AVAILABLE_NOT_SOURCE_SELECTOR",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B5-PARITY-REPLAY",
        "external_guardrail_sources": [
            "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf",
            "https://pdglive.lbl.gov/DataBlock.action?node=S044SEF",
        ],
        "sm_parity_import": rel(sm_replay_path),
        "available_replay_values": {
            "sm_parity_replay_present": bool(sm_replay),
            "gauge_triplet_present": "gauge_triplet" in sm_replay or "filled_outputs" in sm_replay,
            "nonsm_diagnostic_values": diagnostic,
        },
        "allowed_use": [
            "compare a future selected prediction to declared schemes/scales",
            "check formula conventions and uncertainty propagation",
            "construct SM-parity replay tables",
        ],
        "forbidden_use": [
            "choose r_12 from observed sin^2(theta_W)",
            "choose x, mu_Theta, T1, or T2 from observed sin^2(theta_W)",
            "promote diagnostic no-threshold value as no-knob closure",
            "promote rejected threshold direct import as prediction",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02NextWorkAfterB5RatioImport.v1",
        "status": "NEXT_WORKORDER_K_EW_THRESHOLD_KERNEL",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL",
            "task": "Derive or import a selected electroweak threshold kernel K_EW -> (mu_Theta, x, T1, T2, scheme) from topology, flux, curvature, torsion, or determinant data.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B6-A0-ANCHOR-CROSSCHECK",
            "task": "Continue searching for same-branch A0/SU2 physical anchor; if found, reconcile it with the Theta ratio edge.",
        },
        "most_promising_clue": "The sibling diagnostic says the 1-2 electroweak split must come from exceptional/local/representation-sensitive data, not the symmetric bulk threshold alone.",
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB5A0OrRatioKernelImport",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B5-A0-OR-RATIO-KERNEL-IMPORT",
        "output_packets": {
            "cross_repo_source_search": rel(SEARCH),
            "theta_ratio_high_scale_packet": rel(RATIO),
            "sm_parity_replay_boundary": rel(REPLAY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "B4_difference_obstruction_preserved": True,
            "Theta_ratio_edge_imported": search_ok,
            "high_scale_tree_sin2_evaluated": search_ok,
            "SM_parity_replay_boundary_built": search_ok,
            "direct_threshold_import_rejected": True,
        },
        "what_remains_open": {
            "strict_no_knob_low_scale_sin2thetaW": True,
            "K_EW_threshold_kernel": True,
            "x_g2_muTheta_squared": True,
            "mu_Theta": True,
            "T1_T2_thresholds": True,
            "RG_matching_scheme": True,
            "effective_kappa_profile": True,
        },
        "theorem": {
            "name": "CONSTEW02B5A0OrRatioKernelImportTheorem",
            "proved": search_ok,
            "statement": (
                "The B4 common-anchor obstruction remains valid for weak-split difference data, but the sibling Theta program supplies "
                "a stronger ratio edge r_12.  If accepted as selected source data, r_12 evaluates the high-scale tree weak-angle identity "
                "sin^2(theta_W)(mu_Theta)=(3 r_12)/(3 r_12+5)=0.2515877565744274 without using the observed weak angle.  "
                "The physical low-scale/effective angle remains open because K_EW must still select x, mu_Theta, thresholds, and scheme."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B5_A0_or_RatioKernelImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "r_12": r12,
        "high_scale_tree_sin2": tree_sin2,
        "physical_sin2thetaW_value_claimed": False,
        "low_scale_electroweak_closure": False,
        "next_primary": "CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B5 A0 or Ratio Kernel Import v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B5-A0-OR-RATIO-KERNEL-IMPORT`

## Result

B4 proved that internal difference data cannot determine the weak-angle ratio.
That theorem still stands.

The wider corpus supplies a different edge: the Theta overlap ratio

`r_12 = g1(mu_Theta)^2/g2(mu_Theta)^2 = {r12}`.

This is stronger than difference data.  It gives the high-scale tree identity

`sin^2(theta_W)(mu_Theta) = (3 r_12)/(3 r_12 + 5)`

and evaluates to

`{tree_sin2}`.

## Boundary

This is not a physical low-scale or effective weak-angle prediction.  It still
needs

- `x = g2(mu_Theta)^2`,
- `mu_Theta`,
- `T1`,
- `T2`,
- RG/matching scheme,
- effective-angle profile `kappa_l` if comparing to `sin^2(theta_eff^l)`.

The sibling threshold candidate direct import is explicitly rejected as an
electroweak prediction.  Its useful clue is that the 1-2 split must come from
exceptional/local/representation-sensitive data, not from the symmetric bulk
threshold alone.

## Superset Strategy

We now carry two lanes:

- `A0` lane: find a common inverse-coupling anchor.
- `Theta ratio` lane: use selected ratio data to bypass `A0` at high-scale tree
  level, then derive the physical threshold/RG kernel.

Both lanes forbid measured `sin^2(theta_W)` as a selector.

## Next

Next label: `CONST-EW-02 / WEAK-MIXING / B6-K_EW-KERNEL`.
"""

    for path, payload in [
        (SEARCH, search),
        (RATIO, ratio),
        (REPLAY, replay),
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
