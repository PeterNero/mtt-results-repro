"""Build CONST-EW-02 B13 dual-route xL emission attempt.

B13 tries the two strict routes selected by B12:

1. heterotic/Strominger scale-threshold emission;
2. Phi_EW(rho_UV, branch data) response emission.

The current sources sharpen the calculation but still do not emit xL.  This
builder preserves the useful numeric candidates as diagnostics and names the
exact next bridge: a selected horizontal scale law plus electroweak projection
to the profile product.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b13_dual_route_xl_emission_attempt"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
HET = BASE / "heterotic_strominger_scale_route.packet.json"
RHO = BASE / "rho_uv_phi_ew_route.packet.json"
SYNTHESIS = BASE / "dual_route_synthesis.packet.json"
BOUNDARY = BASE / "weak_mixing_b13_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B13_DualRouteXLEmissionAttempt_v1.md"

STATUS = "MTT_CONST_EW_02_B13_DUAL_ROUTE_ATTEMPT_XL_NOT_EMITTED_NEXT_BRIDGE_SHARP"


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

    b12_path = DATA / "const_ew_02_weak_mixing_b12_profile_product_source_contract.candidate.json"
    b12_routes_path = DATA / "const_ew_02_weak_mixing_b12_profile_product_source_contract" / "profile_product_route_matrix.packet.json"
    b12_support_path = DATA / "const_ew_02_weak_mixing_b12_profile_product_source_contract" / "internal_x_equals_one_support_lane.packet.json"
    scale_extraction_path = NONSM / "proof_corpus" / "Selected_Scale_Coefficient_Extraction_for_Flux_Strominger_Branch_v1.md"
    bianchi_path = NONSM / "proof_corpus" / "Bianchi_Constrained_Scale_Lifting_Check_for_Iwasawa_Rho_UV_v1.md"
    rho_attempt_path = NONSM / "proof_corpus" / "Selected_Rho_UV_Response_Ratio_Computation_Attempt_v1.md"
    qa_source_search_path = NONSM / "proof_corpus" / "Selected_Qa_SU3_Strominger_HYM_Source_Packet_Search_v1.md"

    b12 = load(b12_path)
    b12_routes = load(b12_routes_path)
    b12_support = load(b12_support_path)

    c = float(b12_routes["target_product"]["required_value"])
    exp_c = math.exp(c)
    # Values imported from the Bianchi-constrained scale-lifting note.  We keep
    # them here as diagnostics because the note itself does not emit JSON.
    scale_candidates = [
        {
            "name": "H1_extra_horizontal_residual_scaling",
            "R": 2.982841305980989,
            "rho_UV": 3.929428772053664,
            "s_star": 2.485498155594327,
            "r3": 4.428918195741528,
            "source_status": "candidate functional, not selected",
        },
        {
            "name": "H2_rho_UV_includes_full_UV_scale_response",
            "R": 4.44052820580178,
            "rho_UV": 0.16453039057735,
            "s_star": 1.464646764366198,
            "r3": 4.44002897918297,
            "source_status": "candidate functional, not selected",
        },
        {
            "name": "FP_fixed_point_consistency",
            "R": 2.7576341244749276,
            "rho_UV": 7.329403266619077,
            "source_status": "compatibility equation, not selected minimizer",
        },
    ]
    for row in scale_candidates:
        row["L_if_mu_over_ref_equals_R"] = math.log(row["R"])
        row["x_required_to_hit_C_with_L_logR"] = c / row["L_if_mu_over_ref_equals_R"]
        row["relative_R_vs_expC"] = (row["R"] - exp_c) / exp_c
        row["emits_xL"] = False

    h2 = next(row for row in scale_candidates if row["name"].startswith("H2"))

    heterotic = {
        "schema": "MTTConstEW02B13HeteroticStromingerScaleRoute.v1",
        "status": "SCALE_ROUTE_REFINED_XL_NOT_EMITTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B13-HETEROTIC-STROMINGER-xL",
        "inputs": {
            "B12_route_matrix": rel(b12_routes_path),
            "scale_coefficient_extraction": rel(scale_extraction_path),
            "bianchi_constrained_scale_lifting": rel(bianchi_path),
            "qa_su3_strominger_source_search": rel(qa_source_search_path),
        },
        "closed_scale_formulae": {
            "scale_functional_shape": "F_scale(s)=A*s^(-4)+B*s^2",
            "coefficient_structure": "A=C_UV^2, B=delta/(30*kappa), s_*=(60*kappa*C_UV^2/delta)^(1/6)",
            "exponent_p": 4,
        },
        "diagnostic_scale_laws": scale_candidates,
        "best_support_candidate": {
            "name": h2["name"],
            "reason": "H2 is the branch whose rho_UV value matches the closed selected rho_UV scale reported elsewhere; it still is not a selected electroweak projection.",
            "R": h2["R"],
            "L_logR": h2["L_if_mu_over_ref_equals_R"],
            "x_required_to_hit_C": h2["x_required_to_hit_C_with_L_logR"],
        },
        "why_xL_not_emitted": [
            "The scale-law H1/H2/FP choice is not selected by source theorem.",
            "Even a selected scale R would still require an electroweak projection identifying L=log(mu_match/MZ) or a reference-scale ratio.",
            "The QA/SU3 source search states the same-branch Strominger/HYM threshold source packet and determinant finite part remain absent.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rho_route = {
        "schema": "MTTConstEW02B13RhoUVPhiEWRoute.v1",
        "status": "RHOUV_RESPONSE_ROUTE_REFINED_PHI_EW_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B13-RHOUV-PHI-EW",
        "inputs": {
            "rho_UV_response_ratio_attempt": rel(rho_attempt_path),
            "B12_route_matrix": rel(b12_routes_path),
        },
        "closed_formula": {
            "rho_UV_R": "G_11 * [64(2*pi)^2/(16*R^4+8)]^2 / ||D_raw||^2",
            "source_certified_piece": "UV row U_raw=(v1_tilde,0,0) and v1_tilde(R)=64(2*pi)^2/(16*R^4+8)",
        },
        "missing_for_phi_ew": [
            "selected response-row inner product G_11",
            "selected finite-memory disturbance covariance ||D_raw||^2",
            "fluctuation-dissipation/retarded-kernel theorem tying these to the electroweak profile product",
            "projection map Phi_EW(rho_UV, branch data)->xL",
        ],
        "forbidden_direct_maps": [
            "xL = rho_UV",
            "xL = log(1/rho_UV)",
            "xL = s_star",
            "threshold = rho_UV",
        ],
        "emits_xL": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    synthesis = {
        "schema": "MTTConstEW02B13DualRouteSynthesis.v1",
        "status": "DUAL_ROUTE_EXECUTED_NEXT_BRIDGE_IDENTIFIED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B13-DUAL-ROUTE-SYNTHESIS",
        "target": {
            "xL_required": c,
            "exp_xL_required": exp_c,
            "sin2_if_emitted": b12_routes["target_product"]["sin2_if_emitted"],
        },
        "route_results": {
            "heterotic_strominger": "refined to scale-law plus electroweak-projection bridge; no xL emission",
            "rho_uv_phi_ew": "refined to G_11/D_raw/Phi_EW bridge; no xL emission",
            "internal_x_equals_one_support": "would ask for scale ratio exp(C), but physical reference-scale selection remains open",
        },
        "new_minimal_bridge": {
            "name": "SelectedHorizontalScaleLawAndEWProjectionBridge",
            "statement": (
                "Select the horizontal scale law on the Iwasawa/Strominger branch "
                "and prove an electroweak projection from that selected scale law "
                "to xL=sqrt(15/log(448)), or prove Phi_EW emits the same product "
                "from rho_UV response data."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B13Boundary.v1",
        "status": "XL_EMISSION_STILL_OPEN_BRIDGE_SHARPENED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B13-BOUNDARY",
        "closed_now": {
            "heterotic_scale_formula_imported": True,
            "H1_H2_FP_candidates_classified": True,
            "rhoUV_response_formula_imported": True,
            "Phi_EW_missing_inputs_identified": True,
            "next_bridge_named": True,
        },
        "still_open": {
            "actual_xL_source_emission": True,
            "selected_horizontal_scale_law": True,
            "electroweak_projection_from_scale_law": True,
            "selected_G11_and_Draw_covariance": True,
            "Phi_EW_rhoUV_to_xL": True,
            "same_branch_threshold_determinant": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B13NextWork.v1",
        "status": "NEXT_WORKORDER_SCALELAW_EW_PROJECTION_OR_PHI_EW",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B14-SCALELAW-EW-PROJECTION-OR-PHI-EW",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B14-HORIZONTAL-SCALELAW-EW-PROJECTION",
            "task": "Prove which H1/H2/FP horizontal scale law is selected and whether its scale variable projects to electroweak L=log(mu_match/MZ) or xL.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B14-PHI-EW-COVARIANCE",
            "task": "Attempt to source G_11, ||D_raw||^2, and the retarded/fluctuation-dissipation map needed for Phi_EW(rho_UV)->xL.",
        },
        "forbidden_shortcuts": [
            "choose H1/H2/FP by closeness to required xL",
            "identify R with mu_match/MZ without theorem",
            "set G_11=||D_raw||^2=1 as physical proof without selected covariance theorem",
            "map rho_UV directly to xL by an ad hoc function",
        ],
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB13DualRouteXLEmissionAttempt",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B13-DUAL-ROUTE-xL-EMISSION-ATTEMPT",
        "output_packets": {
            "heterotic_strominger_scale_route": rel(HET),
            "rho_uv_phi_ew_route": rel(RHO),
            "dual_route_synthesis": rel(SYNTHESIS),
            "weak_mixing_b13_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B13DualRouteEmissionAttemptTheorem",
            "proved": True,
            "statement": (
                "Executing the heterotic/Strominger and rho_UV routes with current "
                "sources does not emit xL.  The heterotic route refines to the "
                "H1/H2/FP horizontal-scale-law selection plus electroweak projection "
                "problem.  The rho_UV route refines to selected covariance data and "
                "a Phi_EW response map.  No observed weak-angle or alpha_EM selector "
                "is used."
            ),
        },
        "strict_xL_emitted_now": False,
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B13_DualRouteXLEmissionAttempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_xL_emitted_now": False,
        "heterotic_route_refined": True,
        "rhoUV_route_refined": True,
        "next_bridge": synthesis["new_minimal_bridge"]["name"],
        "required_xL": c,
        "required_scale_ratio_if_x_int_1": exp_c,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B13 Dual Route XL Emission Attempt v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B13-DUAL-ROUTE-xL-EMISSION-ATTEMPT`

## Result

B13 tried both strict routes.

The heterotic/Strominger route imports:

```text
F_scale(s)=A*s^(-4)+B*s^2
A=C_UV^2
B=delta/(30*kappa)
```

and classifies the H1/H2/FP scale-law candidates.  None emits `xL`.

The `rho_UV` route imports:

```text
rho_UV(R)=G_11*[64(2*pi)^2/(16R^4+8)]^2/||D_raw||^2
```

but `G_11`, `D_raw`, and `Phi_EW` are still open.

## Target

```text
xL = {c}
exp(xL) = {exp_c}
```

## Next

`CONST-EW-02 / WEAK-MIXING / B14-SCALELAW-EW-PROJECTION-OR-PHI-EW`
"""

    for path, payload in [
        (HET, heterotic),
        (RHO, rho_route),
        (SYNTHESIS, synthesis),
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
