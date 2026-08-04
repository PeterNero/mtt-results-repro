"""Build CONST-EW-02 B8 flat FP quotient policy import.

The sibling no-knob repo already proves the narrow flat Faddeev-Popov quotient
normalization policy for weak-split gauge-kinetic accounting.  This local B8
artifact imports that theorem into the individual-constants weak-mixing branch.
It promotes the SU2 flat FP policy only in that narrow scope and keeps the
physical low-scale/effective weak angle open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b8_flat_fp_policy_import"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORTS = BASE / "flat_fp_imports.packet.json"
POLICY = BASE / "flat_fp_policy_promotion.packet.json"
BOUNDARY = BASE / "weak_mixing_boundary_after_fp.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B8_FlatFPPolicyImport_v1.md"

STATUS = "MTT_CONST_EW_02_B8_FLAT_FP_POLICY_IMPORTED_SU2_WEAKSPLIT_CLOSED_VALUES_OPEN"


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

    b7_path = DATA / "const_ew_02_weak_mixing_b7_local_coefficient_source_gate.candidate.json"
    b7_su2_path = DATA / "const_ew_02_weak_mixing_b7_local_coefficient_source_gate" / "su2_quotient_policy_gate.packet.json"
    flat_fp_path = NONSM / "certificates" / "selected_flat_fp_quotient_normalization_policy_certificate.json"
    flat_fp_note_path = NONSM / "proof_corpus" / "Selected_Flat_FP_Quotient_Normalization_Policy_v1.md"
    qc_path = NONSM / "certificates" / "selected_qc_circle_gauge_block_equivalence_certificate.json"
    internal_weaksplit_path = DATA / "const_em_01_alpha1_internal_weaksplit_import" / "internal_threshold_promotion.packet.json"

    b7 = load(b7_path)
    b7_su2 = load(b7_su2_path)
    flat_fp = load(flat_fp_path)
    qc = load(qc_path)
    internal = load(internal_weaksplit_path)

    values = internal["promoted_internal_values"]
    p_y = values["p_Y_internal"]
    p_su2_internal = values["p_SU2_weaksplit"]
    lambda_12_internal = values["lambda_12_internal"]
    delta_g12_internal = values["Delta_G12_internal"]

    selected_su2 = flat_fp["selected_flat_su2_data"]["selected_p_SU2_for_weak_split"]
    selected_qc = flat_fp["selected_flat_su2_data"]["selected_p_Qc_for_weak_split"]
    extra_fp = flat_fp["selected_flat_su2_data"]["extra_fp_threshold_term"]

    import_checks = {
        "B7_gate_proved": b7["theorem"]["proved"] is True,
        "B7_flat_policy_was_open": b7_su2["decision"]["flat_FP_quotient_policy_promoted"] is False,
        "sibling_flat_fp_policy_closed": flat_fp["status"] == "FLAT_FP_QUOTIENT_NORMALIZATION_POLICY_CLOSED_FOR_WEAK_SPLIT",
        "sibling_su2_selected_for_lambda12": flat_fp["verdict"]["su2_selected_for_lambda_12_accounting"] is True,
        "flat_fp_extra_term_zero": extra_fp == 0.0,
        "flat_adjoint_not_kept_as_threshold": flat_fp["verdict"]["flat_adjoint_fp_kept_as_threshold"] is False,
        "qc_precedent_closed": qc["verdict"]["qc_selected_for_lambda_12_accounting"] is True,
        "local_internal_su2_matches_import": abs(selected_su2 - p_su2_internal) < 1e-12,
    }
    imports_ok = all(import_checks.values())

    imports = {
        "schema": "MTTConstEW02B8FlatFPImports.v1",
        "status": "FLAT_FP_IMPORTS_ACCEPTED" if imports_ok else "FLAT_FP_IMPORTS_INCOMPLETE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-QUOTIENT-POLICY",
        "inputs": {
            "B7_local_coefficient_source_gate": rel(b7_path),
            "B7_su2_policy_gate": rel(b7_su2_path),
            "sibling_flat_fp_policy_certificate": rel(flat_fp_path),
            "sibling_flat_fp_policy_note": rel(flat_fp_note_path),
            "sibling_qc_circle_precedent": rel(qc_path),
            "local_internal_weaksplit": rel(internal_weaksplit_path),
        },
        "import_checks": import_checks,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    policy = {
        "schema": "MTTConstEW02B8FlatFPPolicyPromotion.v1",
        "status": "SU2_FLAT_FP_POLICY_PROMOTED_FOR_WEAKSPLIT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-QUOTIENT-POLICY",
        "promoted_policy": {
            "scope": flat_fp["scope"],
            "source_policy": flat_fp["source_policy"],
            "functional_test": flat_fp["functional_test"],
            "policy_action": flat_fp["selected_flat_su2_data"]["policy_action"],
            "extra_fp_threshold_term": extra_fp,
        },
        "selected_values_for_weaksplit_accounting": {
            "selected_p_Qc_for_weak_split": selected_qc,
            "selected_p_SU2_for_weak_split": selected_su2,
            "local_p_Y_internal": p_y,
            "local_lambda_12_internal": lambda_12_internal,
            "local_Delta_G12_internal": delta_g12_internal,
        },
        "what_this_changes": [
            "The SU2 flat FP ambiguity is no longer an open local blocker for weak-split accounting.",
            "The field-independent flat adjoint FP determinant is discarded or absorbed as quotient normalization in this scope.",
            "The local branch keeps its existing internal p_Y/lambda_12 values; this step does not change them.",
        ],
        "what_this_does_not_change": [
            "It does not derive x=g2(mu_Theta)^2.",
            "It does not derive mu_Theta.",
            "It does not derive low-scale T1/T2 or the full K_EW threshold/RG profile.",
            "It does not derive sin^2(theta_W)(M_Z) or sin^2(theta_eff^l).",
            "It does not fix absolute partition-function normalization or vacuum energy.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B8WeakMixingBoundaryAfterFP.v1",
        "status": "SU2_WEAKSPLIT_POLICY_CLOSED_PHYSICAL_WEAK_ANGLE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B8-BOUNDARY",
        "closed_now": {
            "flat_FP_quotient_policy_for_weaksplit": True,
            "SU2_selected_for_lambda12_accounting": True,
            "Qc_abelian_precedent_imported": True,
            "near_hit_and_target_fitting_still_forbidden": True,
        },
        "still_open": {
            "source_selected_c1_c2_or_T1_T2": True,
            "x_g2_muTheta_squared": True,
            "mu_Theta": True,
            "RG_matching_scheme": True,
            "effective_kappa_l_profile": True,
            "low_scale_or_effective_sin2thetaW_prediction": True,
        },
        "theorem_boundary": (
            "B8 closes a quotient-policy ambiguity inside the internal weak-split accounting lane. "
            "It is not a physical electroweak closure theorem."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B8NextWork.v1",
        "status": "NEXT_WORKORDER_LOCAL_C1C2_OR_KEW_COMPLETION",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B9-LOCAL-C1C2-OR-KEW-COMPLETION",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B9-LOCAL-C1C2-SOURCE",
            "task": "Derive c1,c2, or equivalent T1/T2, from selected exceptional/local curvature, torsion, determinant, flux, or divisor data now that SU2 flat FP policy is closed.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B9-KEW-PHYSICAL-PROFILE",
            "task": "Search for source-selected x, mu_Theta, RG/matching scheme, and effective kappa profile to turn the high-scale ratio into a low-scale/effective weak-angle calculation.",
        },
        "forbidden_shortcuts": [
            "promote B8 as physical sin2thetaW closure",
            "use measured weak angle to choose c1,c2, x, mu_Theta, or thresholds",
            "reuse discarded flat FP determinant as an adjustable threshold term",
            "claim absolute partition-function normalization from weak-split quotient policy",
        ],
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB8FlatFPPolicyImport",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-QUOTIENT-POLICY",
        "output_packets": {
            "flat_fp_imports": rel(IMPORTS),
            "flat_fp_policy_promotion": rel(POLICY),
            "weak_mixing_boundary_after_fp": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "theorem": {
            "name": "CONSTEW02B8FlatFPPolicyImportTheorem",
            "proved": imports_ok,
            "statement": (
                "The selected flat SU2 Faddeev-Popov determinant is field-independent along the selected weak-split "
                "gauge-kinetic background insertion.  By the sibling flat-FP policy theorem and Qc abelian precedent, "
                "it is discarded or absorbed as representative-measure normalization rather than kept as an interacting "
                "threshold term.  Thus SU2 is selected for internal lambda_12 accounting with no extra flat FP term, "
                "while physical low-scale/effective weak-angle closure remains open."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B8_FlatFPPolicyImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_p_SU2_for_weak_split": selected_su2,
        "extra_flat_fp_threshold_term": extra_fp,
        "flat_FP_policy_closed_for_weaksplit": True,
        "low_scale_electroweak_closure": False,
        "physical_sin2thetaW_value_claimed": False,
        "next_primary": "CONST-EW-02 / WEAK-MIXING / B9-LOCAL-C1C2-SOURCE",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B8 Flat FP Policy Import v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B8-FLAT-FP-QUOTIENT-POLICY`

## Result

B8 imports the sibling theorem `Selected_Flat_FP_Quotient_Normalization_Policy_v1`.

Closed now:

- flat FP quotient policy for weak-split gauge-kinetic accounting,
- SU2 selected for `lambda_12` accounting,
- extra flat FP threshold term is `0`.

Selected SU2 value:

`p_SU2 = {selected_su2}`.

Local branch values remain:

- `p_Y_internal = {p_y}`,
- `lambda_12_internal = {lambda_12_internal}`,
- `Delta_G12_internal = {delta_g12_internal}`.

## Boundary

This is not a physical weak-angle closure.  It does not derive `x`,
`mu_Theta`, low-scale thresholds, RG scheme, effective `kappa_l`, or
`sin^2(theta_W)(M_Z)`.

It also does not fix absolute partition-function normalization or vacuum
energy.

## Next

Next primary label:

`CONST-EW-02 / WEAK-MIXING / B9-LOCAL-C1C2-SOURCE`.
"""

    for path, payload in [
        (IMPORTS, imports),
        (POLICY, policy),
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
