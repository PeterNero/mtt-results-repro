"""Build the maximal current-source fill attempt for smooth rho_E insertion."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "template": DATA / "selected_heterotic_projectiverhoe_newsourceinsertion.template.json",
    "interface": DATA / "selected_heterotic_projectiverhoe_newsourceinsertion_goodcovertables_or_exactfactorization.candidate.json",
    "finite_value_packet": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
    "ordered_ah_goodcover_source": DATA / "selected_u1y_ah_goodcover_source_or_routec_selected_residual.candidate.json",
    "terminal_ah_binding_slotmap": DATA / "selected_u1y_routec_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt_certificate.json"
OUTPUT_MISSING = DATA / "selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt_missing_leaves.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_NewSourceInsertion_FillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_NEWSOURCE_FILLATTEMPT_PARTIAL_SOURCE_LAYER_ONLY_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_GoodCoverTransitionSkeleton_or_ComplementKernel_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def present(value: Any) -> bool:
    return value not in (None, False, [], {})


def main() -> dict[str, Any]:
    template = load(INPUTS["template"])
    interface = load(INPUTS["interface"])
    finite_packet = load(INPUTS["finite_value_packet"])
    ordered_source = load(INPUTS["ordered_ah_goodcover_source"])
    terminal_binding = load(INPUTS["terminal_ah_binding_slotmap"])

    finite_values = finite_packet["finite_internal_values"]
    ah_layer = ordered_source["ah_goodcover_stability_layer"]
    source_layer = ordered_source["source_layer"]
    binding = terminal_binding["baseorder_binding"]

    lane_a_fill = {
        "selected_cover_or_finite_quotient_cover": {
            "filled": True,
            "value": {
                "finite_quotient_cover": finite_values["labels"],
                "ordered_AH_goodcover_source_layer": binding["terminal_source_label"],
                "scope": "finite quotient plus ordered source/stability layer only",
            },
        },
        "Deligne_Cech_or_B_field_representative": {
            "filled": False,
            "reason": "ordered AH/good-cover source layer does not print a selected Deligne/Cech/B-field representative for heterotic projective rho_E",
        },
        "period_unit_map_to_primitive_c": {
            "filled": True,
            "value": "finite Z3 central unit tau in primitive c-period units",
            "scope": "finite internal representative-to-cocycle support only",
        },
        "projective_rhoE_transition_matrices": {
            "filled": False,
            "reason": "finite central characters are available, but the interface forbids using the finite character table as smooth transition matrices",
        },
        "Z3_central_character_matches_tau": {
            "filled": True,
            "value": finite_values["rho_E_central_character"],
        },
        "cocycle_law_checked": {
            "filled": False,
            "reason": "no selected smooth overlap table U_alpha_beta is emitted, so the triple-overlap cocycle law cannot be checked",
        },
        "metric_unitarity_compatibility": {
            "filled": False,
            "reason": "finite unitary characters are support only; no selected smooth Hermitian transition metric is emitted",
        },
        "mapped_Freed_Witten_Bianchi_projector_retention": {
            "filled": False,
            "reason": "current source records compatibility context, not a mapped same-branch heterotic Freed-Witten/Bianchi/projector-retention table",
        },
        "bundle_operator_action_A_F_A_D_E_or_E_Qa": {
            "filled": False,
            "reason": "finite D_E is emitted for the internal quotient, but no smooth bundle connection A, curvature F_A, or E_Qa block is emitted",
        },
    }

    lane_b_fill = {
        "smooth_operator_domain": {
            "filled": False,
            "reason": "current source does not emit the selected smooth operator domain; GR/protospinor routing is a separation theorem, not a domain formula",
        },
        "projection_to_eleven_label_quotient": {
            "filled": True,
            "value": finite_values["labels"],
        },
        "det_heat_zeta_torsion_factorization": {
            "filled": False,
            "reason": "no exact heat/zeta/torsion determinant quotient theorem is emitted for the smooth complement",
        },
        "smooth_complement_cancels_universal_or_GR_only": {
            "filled": False,
            "reason": "GR-only routing is support; exact determinant cancellation or universality is not proved",
        },
        "BRST_FP_gauge_quotient_counted_once": {
            "filled": True,
            "value": finite_packet["lane_B_exact_complement_quotient"]["BRST_FP_gauge_quotient_counted_once"],
        },
        "finite_part_equals_log2008_internal_units": {
            "filled": True,
            "value": finite_values["finite_internal_part"],
            "scope": "selected finite internal quotient units only",
        },
    }

    source_certificate_fill = {
        "same_branch_Qa_SU3_heterotic_projective_source": {
            "filled": False,
            "reason": "U1/Y ordered AH source and terminal binding are compatible support, but not a heterotic Qa/SU3 smooth rho_E source certificate",
        },
        "selected_by_MTT_before_target_comparison": {
            "filled": True,
            "value": ordered_source["source_layer"]["ordered_source_selected_by_mtt_under_principle"],
            "scope": "ordered source/stability layer under explicit terminal admissible-section principle",
        },
        "no_observed_coupling_or_scale_input": {
            "filled": True,
            "value": True,
        },
        "source_path_or_proof_reference": {
            "filled": True,
            "value": [
                rel(INPUTS["ordered_ah_goodcover_source"]),
                rel(INPUTS["terminal_ah_binding_slotmap"]),
                rel(INPUTS["finite_value_packet"]),
            ],
        },
    }

    lane_a_closed = all(item["filled"] is True for item in lane_a_fill.values()) and source_certificate_fill["same_branch_Qa_SU3_heterotic_projective_source"]["filled"] is True
    lane_b_closed = all(item["filled"] is True for item in lane_b_fill.values()) and source_certificate_fill["same_branch_Qa_SU3_heterotic_projective_source"]["filled"] is True

    missing = {
        "source_certificate": {
            key: value for key, value in source_certificate_fill.items() if value["filled"] is False
        },
        "lane_A_good_cover_transition_tables": {
            key: value for key, value in lane_a_fill.items() if value["filled"] is False
        },
        "lane_B_exact_complement_factorization": {
            key: value for key, value in lane_b_fill.items() if value["filled"] is False
        },
    }

    decision = {
        "fill_attempt_executed": True,
        "ordered_AH_goodcover_source_layer_imported": ah_layer["selected_ordered_AH_goodcover_source_for_stability_layer"],
        "terminal_AH_binding_imported": binding["AH_goodcover_binding_selected_at_ordered_source_layer"],
        "finite_internal_packet_imported": finite_packet["closed_prerequisites"]["finite_internal_response_attached"],
        "lane_A_closed": lane_a_closed,
        "lane_B_closed": lane_b_closed,
        "smooth_transition_tables_emitted": False,
        "exact_smooth_complement_quotient_closed": False,
        "smooth_finitepart_computed": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoENewSourceInsertionFillAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "template_status": template["status"],
        "interface_status": interface["status"],
        "source_certificate_fill": source_certificate_fill,
        "lane_A_good_cover_transition_tables_fill": lane_a_fill,
        "lane_B_exact_complement_factorization_fill": lane_b_fill,
        "missing_leaves_path": rel(OUTPUT_MISSING),
        "decision": decision,
        "guardrails": {
            "does_not_use_finite_character_table_as_smooth_transition_matrices": True,
            "does_not_promote_ordered_stability_layer_to_operator_layer": True,
            "does_not_promote_GR_routing_to_exact_determinant_factorization": True,
            "does_not_claim_E_Qa": True,
            "does_not_claim_physical_threshold_normalization": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "MaximalCurrentSourceFillAttemptNoPromotion",
            "proved": True,
            "statement": (
                "From the current repository one may legally fill the finite quotient, "
                "finite Z3/tau character match, ordered source-layer selection, "
                "projection-to-eleven-label quotient, no-double-count policy, and "
                "internal log(2008) finite part. These data do not close either "
                "smooth insertion lane: the selected heterotic same-branch smooth "
                "rho_E source certificate, smooth transition matrices, smooth cocycle "
                "checks, smooth bundle operator action, smooth operator domain, and "
                "exact heat/zeta/torsion complement factorization remain absent."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_MISSING.write_text(json.dumps(missing, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "missing_leaves_path": rel(OUTPUT_MISSING),
        "note_path": rel(OUTPUT_NOTE),
        "fill_attempt_executed": True,
        "lane_A_closed": lane_a_closed,
        "lane_B_closed": lane_b_closed,
        "smooth_transition_tables_emitted": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE NewSourceInsertion FillAttempt v1

## Result

```text
status = {STATUS}
lane_A_closed = false
lane_B_closed = false
smooth_transition_tables_emitted = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## What This Fills

This is the maximal legal fill from the current repository. It imports:

- the ordered AH/good-cover source layer selected under the explicit terminal
  admissible-section principle,
- the terminal AH/base-order binding,
- the selected finite internal `rho_E/D_E/Green/Riesz/chi_Qa/log(2008)` packet.

It fills only finite/source-layer leaves: the eleven-label finite quotient, the
finite `Z3`/`tau` character match, the no-double-count policy, and the internal
finite part `log(2008)`.

## Why It Still Does Not Close

The current source still does not emit a selected heterotic same-branch smooth
`rho_E` source certificate, smooth projective transition matrices, triple-overlap
cocycle checks, smooth Hermitian metric compatibility, smooth bundle operator
action, smooth operator domain, or exact heat/zeta/torsion complement
factorization.

Missing leaves are recorded in:

```text
{rel(OUTPUT_MISSING)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_MISSING)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
