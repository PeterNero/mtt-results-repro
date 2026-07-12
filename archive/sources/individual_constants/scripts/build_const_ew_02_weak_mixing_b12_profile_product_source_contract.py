"""Build CONST-EW-02 B12 profile-product source contract.

B12 executes the next frontier after the B11 bridge attempt.  It checks the
current source routes for an emitted product xL and constructs the exact payload
contract needed to promote the weak-mixing loop profile.
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

SLUG = "const_ew_02_weak_mixing_b12_profile_product_source_contract"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTES = BASE / "profile_product_route_matrix.packet.json"
CONTRACT = BASE / "source_emission_contract.packet.json"
SUPPORT = BASE / "internal_x_equals_one_support_lane.packet.json"
BOUNDARY = BASE / "weak_mixing_b12_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B12_ProfileProductSourceContract_v1.md"

STATUS = "MTT_CONST_EW_02_B12_PROFILE_PRODUCT_CONTRACT_BUILT_NO_CURRENT_SOURCE_EMISSION"


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

    b11_path = DATA / "const_ew_02_weak_mixing_b11_loop_volume_bridge_proof_attempt.candidate.json"
    b11_boundary_path = DATA / "const_ew_02_weak_mixing_b11_loop_volume_bridge_proof_attempt" / "weak_mixing_b11_boundary.packet.json"
    b11_proof_path = DATA / "const_ew_02_weak_mixing_b11_loop_volume_bridge_proof_attempt" / "selected_loop_volume_bridge_proof_attempt.packet.json"
    b11_cond_path = DATA / "const_ew_02_weak_mixing_b11_loop_volume_bridge_proof_attempt" / "conditional_one_primitive_bridge.packet.json"
    qa_k_path = QA_SU3 / "candidate_data" / "selected_k_gauge_anchor_or_full_electroweak_matching.candidate.json"
    qa_norm_path = QA_SU3 / "candidate_data" / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme.candidate.json"
    ew_interface_path = NONSM / "proof_corpus" / "Selected_Electroweak_Kernel_Interface_Theorem_v1.md"
    norm_min_path = NONSM / "proof_corpus" / "Selected_Normalization_Minimization_Functional_v1.md"

    b11 = load(b11_path)
    b11_boundary = load(b11_boundary_path)
    b11_proof = load(b11_proof_path)
    b11_cond = load(b11_cond_path)
    qa_k = load(qa_k_path)
    qa_norm = load(qa_norm_path)

    c = float(b11_proof["right_hand_side_source"]["value"])
    y = float(b11_cond["conditional_theorem"]["value_if_condition_met"]["y"])
    sin2 = float(b11_cond["conditional_theorem"]["value_if_condition_met"]["sin2_no_threshold_one_loop"])
    l_if_x_int_1 = c
    scale_ratio_if_x_int_1 = math.exp(l_if_x_int_1)

    route_rows = [
        {
            "route": "R1_DIRECT_K_EW_PRODUCT",
            "kind": "strict_no_knob",
            "source_home": "Selected electroweak kernel K_EW",
            "required_emission": "xL := g2(mu_Theta)^2 * log(mu_Theta/MZ)",
            "current_support": "kernel interface built; values open",
            "current_source_emits_xL": False,
            "promotion_status": "OPEN",
        },
        {
            "route": "R2_FACTORIZED_x_AND_L",
            "kind": "strict_no_knob_if_both_factors_sourced",
            "source_home": "physical gauge anchor plus selected matching scale",
            "required_emission": "x and L separately, both before electroweak comparison",
            "current_support": "internal K_gauge,int=1 exists but physical K_gauge and mu_match remain open",
            "current_source_emits_xL": False,
            "promotion_status": "OPEN",
        },
        {
            "route": "R3_HETEROTIC_STROMINGER_THRESHOLD_KERNEL",
            "kind": "best_strict_no_knob_route",
            "source_home": "selected heterotic/Strominger finite threshold determinant or analytic torsion",
            "required_emission": "kappa_EW, Delta^sel, mu_Theta, scheme; product xL derivable from emitted kappa/zeta/mu",
            "current_support": "Strominger functional and selection route exist; scale-lifting and threshold determinant values open",
            "current_source_emits_xL": False,
            "promotion_status": "PRIMARY_OPEN",
        },
        {
            "route": "R4_RHO_UV_RESPONSE_BRIDGE",
            "kind": "strict_no_knob_if_map_proved",
            "source_home": "Phi_EW(rho_UV, branch data)",
            "required_emission": "source-certified map to xL or to (kappa_EW,Delta^sel,mu_Theta)",
            "current_support": "rho_UV closed, direct threshold identification forbidden",
            "current_source_emits_xL": False,
            "promotion_status": "OPEN",
        },
        {
            "route": "R5_ONE_UNIVERSAL_PRIMITIVE",
            "kind": "not_strict_no_knob",
            "source_home": "single declared upstream primitive P_univ",
            "required_emission": "P_univ -> xL=C, shared across constants",
            "current_support": "primitive policy ready; no primitive selected",
            "current_source_emits_xL": False,
            "promotion_status": "CONDITIONAL_OPEN",
        },
    ]

    routes = {
        "schema": "MTTConstEW02B12ProfileProductRouteMatrix.v1",
        "status": "NO_CURRENT_ROUTE_EMITS_PROFILE_PRODUCT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B12-PROFILE-PRODUCT-ROUTES",
        "target_product": {
            "symbol": "xL",
            "required_value": c,
            "required_expression": "sqrt(15/log(448))",
            "y_if_emitted": y,
            "sin2_if_emitted": sin2,
        },
        "routes": route_rows,
        "route_verdict": {
            "strict_no_knob_xL_emitted_now": False,
            "conditional_one_primitive_lane_available": True,
            "best_next_route": "R3_HETEROTIC_STROMINGER_THRESHOLD_KERNEL",
            "secondary_route": "R4_RHO_UV_RESPONSE_BRIDGE",
        },
        "inputs": {
            "B11": rel(b11_path),
            "QA_SU3_K_gauge": rel(qa_k_path),
            "QA_SU3_RG_route": rel(qa_norm_path),
            "nonSM_EW_kernel_interface": rel(ew_interface_path),
            "nonSM_normalization_minimization": rel(norm_min_path),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    contract = {
        "schema": "MTTConstEW02B12SourceEmissionContract.v1",
        "status": "PROFILE_PRODUCT_SOURCE_CONTRACT_BUILT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B12-SOURCE-EMISSION-CONTRACT",
        "minimal_acceptance_contract": {
            "emitted_fields": {
                "source_identity": "selected source packet name and theorem provenance",
                "scheme": "fixed RG/matching/threshold convention",
                "profile_product": "xL = g2(mu_Theta)^2 * log(mu_Theta/MZ)",
                "profile_product_value": c,
                "no_observed_selector_proof": True,
            },
            "either_factorized_or_direct": [
                {
                    "direct": "emit xL directly from K_EW profile integral",
                },
                {
                    "factorized": "emit x and L separately with same-source compatibility proof",
                },
                {
                    "threshold_kernel": "emit kappa_EW,zeta_2,Delta_2,mu_Theta and derive xL",
                },
            ],
            "required_guardrails": [
                "no weak-angle target selector",
                "no alpha_EM backsolve claimed as no-knob",
                "no 5 TeV scaffold promotion",
                "rho_UV may enter only through Phi_EW theorem",
                "one primitive must be declared not strict no-knob unless independently derived",
            ],
        },
        "derived_if_contract_filled": {
            "y": y,
            "sin2_no_threshold_one_loop": sin2,
            "strict_no_knob_possible": "only if source_identity is strict no-knob and no primitive fallback is used",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    support = {
        "schema": "MTTConstEW02B12InternalXEqualsOneSupportLane.v1",
        "status": "INTERNAL_SUPPORT_LANE_BUILT_PHYSICAL_SCALE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B12-INTERNAL-x-ONE-SUPPORT",
        "source": rel(qa_k_path),
        "internal_kernel_support": {
            "K_gauge_int": qa_k["decision"]["internal_K_gauge_value"],
            "SU2_internal_entry": qa_k["decision"]["selected_internal_kernel_vector"]["SU2"],
            "interpretation": "In canonical internal action units, SU2 can be read as x_int=1 support.",
        },
        "if_internal_x_int_equals_1": {
            "required_L_int": l_if_x_int_1,
            "required_scale_ratio": scale_ratio_if_x_int_1,
            "formula": "mu_match/M_ref = exp(sqrt(15/log(448)))",
        },
        "why_not_physical_closure": [
            "K_gauge,int=1 is explicitly internal, not measured physical coupling.",
            "M_ref/MZ identification is not source-selected.",
            "mu_match remains open in the QA/SU3 and no-knob electroweak frontiers.",
        ],
        "promoted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B12Boundary.v1",
        "status": "SOURCE_CONTRACT_CLOSED_XL_EMISSION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B12-BOUNDARY",
        "closed_now": {
            "profile_product_route_matrix": True,
            "minimal_source_emission_contract": True,
            "internal_x_equals_one_support_lane": True,
            "best_strict_route_selected": "R3_HETEROTIC_STROMINGER_THRESHOLD_KERNEL",
            "secondary_route_selected": "R4_RHO_UV_RESPONSE_BRIDGE",
        },
        "still_open": {
            "actual_xL_source_emission": True,
            "heterotic_threshold_determinant_or_torsion_values": True,
            "scale_lifting_lemma_for_flux_strominger_functional": True,
            "Phi_EW_rhoUV_response_map": True,
            "physical_matching_scale": True,
            "physical_gauge_action_anchor": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B12NextWork.v1",
        "status": "NEXT_WORKORDER_HETEROTIC_OR_RHOUV_SOURCE_EMISSION",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B13-HETEROTIC-OR-RHOUV-xL-EMISSION",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B13-HETEROTIC-STROMINGER-xL",
            "task": "Attempt a selected heterotic/Strominger finite threshold or scale-lifting theorem that emits xL or emits (kappa_EW,zeta_2,mu_match) from which xL follows.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B13-RHOUV-PHI-EW",
            "task": "Attempt a source-certified Phi_EW(rho_UV, branch data)->xL response bridge; direct rho_UV threshold reuse remains forbidden.",
        },
        "forbidden_shortcuts": [
            "promote internal K_gauge,int=1 as physical g2 normalization",
            "choose mu_match from the weak angle",
            "choose P_univ from alpha_EM or sin2thetaW while calling the result no-knob",
            "set rho_UV equal to xL or a threshold without a Phi_EW theorem",
        ],
    }

    theorem_proved = all(
        [
            b11["conditional_bridge_proved"] is True,
            b11_boundary["still_open"]["source_emitted_xL_product"] is True,
            qa_k["decision"]["internal_K_gauge_anchor_closed"] is True,
            qa_norm["decision"]["gaugekinetic_normalization_closed"] is False,
        ]
    )

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB12ProfileProductSourceContract",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B12-PROFILE-PRODUCT-SOURCE-CONTRACT",
        "output_packets": {
            "profile_product_route_matrix": rel(ROUTES),
            "source_emission_contract": rel(CONTRACT),
            "internal_x_equals_one_support_lane": rel(SUPPORT),
            "weak_mixing_b12_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B12ProfileProductSourceContractTheorem",
            "proved": theorem_proved,
            "statement": (
                "The current source routes do not emit xL, but the exact contract "
                "for such an emission is now closed.  The best strict route is a "
                "selected heterotic/Strominger threshold or scale-lifting kernel; "
                "the secondary route is a Phi_EW(rho_UV, branch data) response "
                "bridge.  The internal K_gauge,int=1 lane supplies x_int=1 support "
                "only in canonical internal action units and cannot be promoted as "
                "a physical weak-angle closure."
            ),
        },
        "strict_xL_emitted_now": False,
        "contract_ready": True,
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B12_ProfileProductSourceContract_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_xL_emitted_now": False,
        "source_contract_ready": True,
        "best_strict_route": "R3_HETEROTIC_STROMINGER_THRESHOLD_KERNEL",
        "secondary_route": "R4_RHO_UV_RESPONSE_BRIDGE",
        "internal_x_equals_one_support": True,
        "physical_weak_angle_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B12 Profile Product Source Contract v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B12-PROFILE-PRODUCT-SOURCE-CONTRACT`

## Result

B12 does not emit `xL`.  It closes the exact source-emission contract for what
would count as proof:

```text
xL = g2(mu_Theta)^2 * log(mu_Theta/MZ) = sqrt(15/log(448))
```

The best strict route is:

```text
selected heterotic/Strominger threshold or scale-lifting kernel
```

The secondary strict route is:

```text
Phi_EW(rho_UV, branch data) -> xL
```

## Internal Support Lane

The QA/SU3 repo has `K_gauge,int=1` and `SU2=1` in canonical internal action
units.  If read as `x_int=1`, the bridge asks for:

```text
L_int = {l_if_x_int_1}
mu_match/M_ref = {scale_ratio_if_x_int_1}
```

This is useful support, not physical closure.

## Next

`CONST-EW-02 / WEAK-MIXING / B13-HETEROTIC-OR-RHOUV-xL-EMISSION`
"""

    for path, payload in [
        (ROUTES, routes),
        (CONTRACT, contract),
        (SUPPORT, support),
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
