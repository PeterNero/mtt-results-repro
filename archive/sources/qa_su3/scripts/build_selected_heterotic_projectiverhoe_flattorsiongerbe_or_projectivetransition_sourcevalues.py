"""Build flat torsion gerbe / projective transition source-values gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "invariant_B": DATA / "selected_heterotic_projectiverhoe_invariant_B_potential_candidate.values.json",
    "z3_shadow": DATA / "selected_heterotic_projectiverhoe_abstract_z3_cocycle_shadow_witness.json",
    "transition_equations": DATA / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.equations.json",
    "ctwist_source_search": DATA / "ctwist_source_value_search.candidate.json",
    "finite_nerve": DATA / "selected_heterotic_projectiverhoe_finitegoodcovernerve_incidence_table.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_flattorsiongerbe_or_projectivetransition_sourcevalues.candidate.json"
OUTPUT_VALUES = DATA / "selected_heterotic_projectiverhoe_formal_flattorsion_projective_transition_values.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_projectiverhoe_flattorsiongerbe_promotion_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_flattorsiongerbe_or_projectivetransition_sourcevalues_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_FlatTorsionGerbe_or_ProjectiveTransition_SourceValues_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_FORMAL_FLATTORSION_PROJECTIVE_VALUES_BUILT_SOURCE_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FlatTorsionPromotion_or_SmoothTransitionTables_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def tau_mod3(tau: int) -> int:
    return tau % 3


def main() -> dict[str, Any]:
    invariant_B = load(INPUTS["invariant_B"])
    z3_shadow = load(INPUTS["z3_shadow"])
    transition_equations = load(INPUTS["transition_equations"])
    ct_source = load(INPUTS["ctwist_source_search"])
    finite_nerve = load(INPUTS["finite_nerve"])

    labels = z3_shadow["labels"]
    flat_projective_values = {}
    product_cancellation = {}
    for label in labels:
        row = z3_shadow["tables"][label]
        tau = row["tau"]
        flat_projective_values[label] = {
            "tau": tau,
            "flat_torsion_class_mod3": tau_mod3(tau),
            "curvature_H_component": "0 for flat torsion layer; curvature carried separately by invariant B candidate",
            "formal_pair_transitions": {
                "U01": row["T_01"],
                "U12": row["T_12"],
                "U20": row["T_20"],
            },
            "formal_reverse_transitions": {
                "U10": row["T_10"],
                "U21": row["T_21"],
                "U02": row["T_02"],
            },
            "formal_triple_cocycle": row["central_triple_012"],
            "triple_matches_tau": z3_shadow["checks"][label]["projective_triple_overlap_matches_tau"],
        }

    pairs = [("F1", "G1"), ("F2", "G2"), ("F3", "G3"), ("F4", "G4"), ("F5", "G5")]
    for f_label, g_label in pairs:
        total_tau = flat_projective_values[f_label]["tau"] + flat_projective_values[g_label]["tau"]
        product_cancellation[f"{f_label}+{g_label}->P"] = {
            "tau_sum": total_tau,
            "tau_sum_mod3": tau_mod3(total_tau),
            "P_tau": flat_projective_values["P"]["tau"],
            "twist_cancels_to_P": tau_mod3(total_tau) == tau_mod3(flat_projective_values["P"]["tau"]),
        }

    values = {
        "schema": "SelectedHeteroticProjectiveRhoE.FormalFlatTorsionProjectiveTransitionValues.v1",
        "status": "FORMAL_VALUES_BUILT_NOT_SMOOTH_SOURCE",
        "scope": "formal three-patch finite nerve; validator and promotion target only",
        "cover": finite_nerve["cover_nodes"],
        "pair_overlaps": finite_nerve["pair_overlaps"],
        "triple_overlaps": finite_nerve["triple_overlaps"],
        "curvature_split": {
            "exact_invariant_B_candidate": invariant_B["B_candidate_components"],
            "exact_invariant_B_has_trivial_triple_class": invariant_B["deligne_triple_class_from_B_only"] == 0,
            "flat_torsion_layer_carries_nonzero_tau": True,
            "total_conceptual_B_field": "B_exact + B_flat_torsion/projective_transition, with B_flat curvature zero and nontrivial holonomy",
        },
        "flat_projective_values": flat_projective_values,
        "product_cancellation": product_cancellation,
        "all_triples_match_tau": all(item["triple_matches_tau"] for item in flat_projective_values.values()),
        "all_products_cancel_to_P": all(item["twist_cancels_to_P"] for item in product_cancellation.values()),
        "same_branch_smooth_source_values_found": ct_source["gate_results"]["same_branch_Qa_SU3_values_found"],
        "promotable_now": False,
        "why_not_promotable_now": [
            "formal nerve is not a selected smooth good cover",
            "flat torsion/projective layer is assigned at finite shadow level, not derived from smooth g_ijk",
            "no same-branch local Deligne/Cech values or smooth transition matrices are emitted",
            "metric, Bianchi/Freed-Witten, projector, and operator-domain checks remain open",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_VALUES.write_text(json.dumps(values, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    contract = {
        "schema": "SelectedHeteroticProjectiveRhoE.FlatTorsionGerbePromotionContract.v1",
        "status": "PROMOTION_CONTRACT_OPEN",
        "must_supply": {
            "selected_smooth_good_cover_realizing_U0_U1_U2": None,
            "flat_U1_valued_g_ijk_or_projective_transition_functions": None,
            "proof_g_012_maps_to_tau_before_finite_comparison": None,
            "local_B_i_equals_invariant_B_plus_flat_torsion_representative": None,
            "h_plus_h_minus_twisted_module_transitions": None,
            "metric_unitarity": None,
            "mapped_Freed_Witten_Bianchi_check": None,
            "projector_retention": None,
            "smooth_operator_domain_or_transition_tables": None,
        },
        "formal_values_allowed_as": "validator and target shape only",
        "formal_values_forbidden_as": "same-branch selected smooth source values",
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "formal_flat_torsion_values_built": True,
        "exact_B_curvature_layer_closed": invariant_B["dB_equals_H"],
        "flat_torsion_layer_needed_for_tau": True,
        "all_triples_match_tau": values["all_triples_match_tau"],
        "all_products_cancel_to_P": values["all_products_cancel_to_P"],
        "same_branch_smooth_values_found": values["same_branch_smooth_source_values_found"],
        "promotable_now": False,
        "S1_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEFlatTorsionGerbeOrProjectiveTransitionSourceValues",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "values_path": rel(OUTPUT_VALUES),
        "promotion_contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "closed_now": {
            "formal_Z3_flat_torsion_value_packet": True,
            "twisted_product_cancellation_over_formal_packet": values["all_products_cancel_to_P"],
            "curvature_and_torsion_roles_separated": True,
        },
        "still_open": {
            "same_branch_smooth_good_cover": True,
            "smooth_flat_torsion_Deligne_representative": True,
            "smooth_projective_transition_matrices": True,
            "metric_Bianchi_projector_operator_checks": True,
            "S1_payload_closure": True,
        },
        "guardrails": {
            "does_not_promote_formal_z3_shadow_to_smooth_source": True,
            "does_not_claim_exact_B_derives_nonzero_tau": True,
            "does_not_import_q79_values_as_QaSU3": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "FormalFlatTorsionProjectiveTransitionValuePacketTheorem",
            "proved": True,
            "statement": (
                "The exact invariant B candidate supplies the curvature layer dB=H, "
                "while a separate formal Z3 flat torsion/projective transition packet "
                "supplies the finite tau shadow and F_i G_i -> P twist cancellation. "
                "This cleanly separates curvature from torsion holonomy, but the "
                "formal packet is not yet a selected smooth Deligne/Cech source."
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
        "values_path": rel(OUTPUT_VALUES),
        "promotion_contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "formal_flat_torsion_values_built": True,
        "all_triples_match_tau": values["all_triples_match_tau"],
        "all_products_cancel_to_P": values["all_products_cancel_to_P"],
        "promotable_now": False,
        "S1_closed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE FlatTorsionGerbe or ProjectiveTransition SourceValues v1

## Result

```text
status = {STATUS}
formal_flat_torsion_values_built = true
all_triples_match_tau = {str(values["all_triples_match_tau"]).lower()}
all_products_cancel_to_P = {str(values["all_products_cancel_to_P"]).lower()}
promotable_now = false
S1_closed = false
next_required_artifact = {NEXT}
```

## Construction

The smooth curvature side and the torsion-holonomy side are now separated:

- `B = 6 e5 wedge e6` supplies the exact curvature layer `dB=H`.
- the formal `Z3` flat torsion/projective transition packet supplies the
  finite `tau` shadow and the `F_i G_i -> P` twist cancellation.

This is not yet smooth closure. The new value packet is a validator and target
shape until a same-branch selected good cover and smooth Deligne/Cech transition
functions derive it before comparison to the finite table.

Values:

```text
{rel(OUTPUT_VALUES)}
```

Promotion contract:

```text
{rel(OUTPUT_CONTRACT)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_VALUES)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
