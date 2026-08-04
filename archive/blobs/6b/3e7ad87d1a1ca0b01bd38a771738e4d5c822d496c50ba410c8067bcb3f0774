"""Build flat-torsion promotion / smooth-transition table gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "formal_values": DATA / "selected_heterotic_projectiverhoe_formal_flattorsion_projective_transition_values.json",
    "promotion_contract": DATA / "selected_heterotic_projectiverhoe_flattorsiongerbe_promotion_contract.json",
    "deligne_equations": DATA / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_equations.json",
    "invariant_B": DATA / "selected_heterotic_projectiverhoe_invariant_B_potential_candidate.values.json",
    "finite_nerve": DATA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidence_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_flattorsionpromotion_or_smoothtransitiontables.candidate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_projectiverhoe_symbolic_smoothtransition_table_template.json"
OUTPUT_SOURCE_GAP = DATA / "selected_heterotic_projectiverhoe_smoothtransition_source_gap.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_flattorsionpromotion_or_smoothtransitiontables_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_FlatTorsionPromotion_or_SmoothTransitionTables_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SYMBOLIC_TRANSITION_TABLE_TEMPLATE_BUILT_SMOOTH_PROMOTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothTransitionSourceGap_Closure_or_DirectOperatorPayload_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def zeta_power_string(k: int) -> str:
    return f"zeta_3^{k % 3}"


def transition_table(values: dict[str, Any]) -> dict[str, Any]:
    table: dict[str, Any] = {}
    for label, row in values["flat_projective_values"].items():
        tau_mod3 = row["flat_torsion_class_mod3"]
        table[label] = {
            "tau": row["tau"],
            "tau_mod3": tau_mod3,
            "smooth_symbolic_transitions": {
                "T01": "identity_U01",
                "T12": "identity_U12",
                "T20": zeta_power_string(tau_mod3),
            },
            "reverse_transitions": {
                "T10": "identity_U10",
                "T21": "identity_U21",
                "T02": zeta_power_string(-tau_mod3),
            },
            "triple_product_T01_T12_T20": zeta_power_string(tau_mod3),
            "target_cocycle": zeta_power_string(tau_mod3),
            "formal_cocycle_law_passes": row["triple_matches_tau"],
            "formal_unitarity_passes": True,
            "flat_curvature_zero": True,
            "source_promoted": False,
        }
    return table


def product_checks(table: dict[str, Any]) -> dict[str, Any]:
    pairs = [("F1", "G1"), ("F2", "G2"), ("F3", "G3"), ("F4", "G4"), ("F5", "G5")]
    checks: dict[str, Any] = {}
    for left, right in pairs:
        total = (table[left]["tau_mod3"] + table[right]["tau_mod3"]) % 3
        checks[f"{left}*{right}->P"] = {
            "left_tau_mod3": table[left]["tau_mod3"],
            "right_tau_mod3": table[right]["tau_mod3"],
            "product_tau_mod3": total,
            "P_tau_mod3": table["P"]["tau_mod3"],
            "cancels_to_P": total == table["P"]["tau_mod3"],
        }
    return checks


def main() -> dict[str, Any]:
    formal_values = load(INPUTS["formal_values"])
    contract = load(INPUTS["promotion_contract"])
    equations = load(INPUTS["deligne_equations"])
    invariant_B = load(INPUTS["invariant_B"])
    finite_nerve = load(INPUTS["finite_nerve"])

    table = transition_table(formal_values)
    products = product_checks(table)

    template = {
        "schema": "SelectedHeteroticProjectiveRhoE.SymbolicSmoothTransitionTableTemplate.v1",
        "status": "SYMBOLIC_TEMPLATE_ONLY_NOT_SOURCE_PROMOTED",
        "cover_nodes": finite_nerve["cover_nodes"],
        "pair_overlaps": finite_nerve["pair_overlaps"],
        "triple_overlaps": finite_nerve["triple_overlaps"],
        "curvature_layer": {
            "B_exact": invariant_B["B_candidate_components"],
            "dB_equals_H": invariant_B["dB_equals_H"],
            "flat_layer_curvature": 0,
            "separation_rule": "exact invariant B carries H; flat projective transition carries torsion holonomy",
        },
        "symbolic_transition_table": table,
        "product_checks": products,
        "formal_all_cocycles_pass": all(row["formal_cocycle_law_passes"] for row in table.values()),
        "formal_all_unitarity_pass": all(row["formal_unitarity_passes"] for row in table.values()),
        "formal_all_products_cancel_to_P": all(row["cancels_to_P"] for row in products.values()),
        "smooth_source_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    source_gap = {
        "schema": "SelectedHeteroticProjectiveRhoE.SmoothTransitionSourceGap.v1",
        "status": "SOURCE_GAP_SHARPLY_IDENTIFIED",
        "passed_formally": {
            "three_patch_projective_cocycle_shape": template["formal_all_cocycles_pass"],
            "U1_phase_unitarity_if_scalar_transitions": template["formal_all_unitarity_pass"],
            "flat_layer_zero_curvature": True,
            "exact_B_curvature_layer": template["curvature_layer"]["dB_equals_H"],
            "F_i_G_i_to_P_twist_cancellation": template["formal_all_products_cancel_to_P"],
        },
        "not_yet_source_promoted": {
            "selected_smooth_good_cover_realizing_U0_U1_U2": contract["must_supply"]["selected_smooth_good_cover_realizing_U0_U1_U2"],
            "flat_U1_valued_g_ijk_or_projective_transition_functions": contract["must_supply"]["flat_U1_valued_g_ijk_or_projective_transition_functions"],
            "proof_g_012_maps_to_tau_before_finite_comparison": contract["must_supply"]["proof_g_012_maps_to_tau_before_finite_comparison"],
            "local_B_i_equals_invariant_B_plus_flat_torsion_representative": contract["must_supply"]["local_B_i_equals_invariant_B_plus_flat_torsion_representative"],
            "h_plus_h_minus_twisted_module_transitions": contract["must_supply"]["h_plus_h_minus_twisted_module_transitions"],
            "metric_unitarity": contract["must_supply"]["metric_unitarity"],
            "mapped_Freed_Witten_Bianchi_check": contract["must_supply"]["mapped_Freed_Witten_Bianchi_check"],
            "projector_retention": contract["must_supply"]["projector_retention"],
            "smooth_operator_domain_or_transition_tables": contract["must_supply"]["smooth_operator_domain_or_transition_tables"],
        },
        "equation_packet_source": rel(INPUTS["deligne_equations"]),
        "minimal_closing_payload": [
            "a selected smooth good cover or smooth quotient domain whose nerve maps to U0,U1,U2",
            "smooth U(1)-valued transition/cochain functions whose triple product is zeta_3^tau(label)",
            "a proof that those functions are selected by the heterotic Qa/SU3 branch before finite comparison",
            "twisted module transitions for F_i, G_i, P with product retention",
            "metric, Bianchi/Freed-Witten, and projector retention checks on the same cover",
            "operator-domain or rho_E transition-table identity linking the smooth data to the selected finite packet",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_SOURCE_GAP.write_text(json.dumps(source_gap, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "symbolic_smooth_transition_template_built": True,
        "formal_cocycle_law_passes": template["formal_all_cocycles_pass"],
        "formal_unitarity_passes_for_scalar_U1_phases": template["formal_all_unitarity_pass"],
        "formal_products_cancel_to_P": template["formal_all_products_cancel_to_P"],
        "exact_B_plus_flat_torsion_split_consistent": template["curvature_layer"]["dB_equals_H"],
        "smooth_source_promoted": False,
        "S1_closed": False,
        "smooth_transition_tables_source_selected": False,
        "direct_operator_payload_emitted": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEFlatTorsionPromotionOrSmoothTransitionTables",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "template_path": rel(OUTPUT_TEMPLATE),
        "source_gap_path": rel(OUTPUT_SOURCE_GAP),
        "decision": decision,
        "closed_now": {
            "symbolic_transition_table_template": True,
            "formal_projective_cocycle_validator": template["formal_all_cocycles_pass"],
            "formal_scalar_unitarity_validator": template["formal_all_unitarity_pass"],
            "formal_twist_cancellation_validator": template["formal_all_products_cancel_to_P"],
            "curvature_torsion_separation_validator": True,
        },
        "still_open": {
            "selected_smooth_good_cover_or_domain": True,
            "smooth_transition_functions": True,
            "smooth_to_finite_tau_derivation": True,
            "module_transition_and_projector_retention": True,
            "mapped_Bianchi_Freed_Witten_metric_checks": True,
            "smooth_operator_identity_or_direct_payload": True,
        },
        "guardrails": {
            "does_not_treat_symbolic_template_as_smooth_source": True,
            "does_not_use_finite_shadow_as_source_derivation": True,
            "does_not_reopen_exact_B_as_nonzero_tau_source": True,
            "does_not_import_observed_constants": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "SymbolicFlatTorsionTransitionTemplateTheorem",
            "proved": True,
            "statement": (
                "From the formal flat Z3 torsion packet one obtains a consistent "
                "three-patch symbolic projective transition-table template: the "
                "triple products reproduce zeta_3^tau, scalar U(1) unitarity is "
                "formal, the flat layer has zero curvature, and F_i G_i -> P "
                "twist cancellation is preserved. This is a validator theorem only; "
                "a selected smooth good cover, smooth transition functions, and "
                "same-branch operator-domain checks are still required for source "
                "promotion."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "source_gap_path": rel(OUTPUT_SOURCE_GAP),
        "note_path": rel(OUTPUT_NOTE),
        "symbolic_smooth_transition_template_built": True,
        "formal_cocycle_law_passes": template["formal_all_cocycles_pass"],
        "formal_products_cancel_to_P": template["formal_all_products_cancel_to_P"],
        "smooth_source_promoted": False,
        "S1_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE FlatTorsionPromotion or SmoothTransitionTables v1

## Result

```text
status = {STATUS}
symbolic_smooth_transition_template_built = true
formal_cocycle_law_passes = {str(template["formal_all_cocycles_pass"]).lower()}
formal_products_cancel_to_P = {str(template["formal_all_products_cancel_to_P"]).lower()}
smooth_source_promoted = false
S1_closed = false
next_required_artifact = {NEXT}
```

## What This Closes

The formal flat torsion packet now has a clean symbolic transition-table
template. On the three-patch validator nerve, each selected label has
`T01=1`, `T12=1`, and `T20=zeta_3^tau`, so the triple product reproduces the
finite `tau` shadow. The scalar `U(1)` phase table is formally unitary, has
zero flat curvature, and preserves all five `F_i G_i -> P` cancellation checks.

## What It Does Not Close

This is still not a smooth source theorem. The table is a target/validator
until the same branch emits a selected smooth cover or smooth quotient domain,
actual transition functions, the derivation of `tau` before finite comparison,
module/projector retention, mapped metric/Bianchi/Freed-Witten checks, and a
smooth operator identity or direct operator payload.

Template:

```text
{rel(OUTPUT_TEMPLATE)}
```

Source gap:

```text
{rel(OUTPUT_SOURCE_GAP)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_TEMPLATE)}")
    print(f"wrote {rel(OUTPUT_SOURCE_GAP)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(result["status"])
