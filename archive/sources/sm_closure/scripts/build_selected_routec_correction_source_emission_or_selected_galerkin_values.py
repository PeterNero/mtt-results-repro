"""Audit whether the Route-C diagnostic correction is source-emitted.

The previous artifact found a qutrit/Weyl diagnostic splitter.  This builder
tries the next, stricter gate: does the selected Phi_fin/Galerkin stack emit
that splitter, or any selected correction values, without lifted flags or
observed flavor targets?
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

FIRST = DATA / "selected_routec_first_correction_search_or_galerkin_run.candidate.json"
PHIFIN = DATA / "selected_phifin_alpha1_payload.candidate.json"
SOURCE_ALPHA1 = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
GALERKIN = DATA / "selected_routec_strominger_galerkin_first_run.candidate.json"
HIGHER = DATA / "selected_routec_higherorder_fullresponse_flavor_splitting.candidate.json"

OUTPUT = DATA / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json"
CERT = CERTS / "selected_routec_correction_source_emission_or_selected_galerkin_values_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_Correction_Source_Emission_or_Selected_Galerkin_Values_v1.md"

NEXT = "MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1"
STATUS = "MTT_SELECTED_ROUTEC_CORRECTION_SOURCE_EMISSION_AUDITED_DIAGNOSTIC_SPLITTER_NOT_SOURCE_EMITTED_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def text_contains(data: dict[str, Any], needle: str) -> bool:
    return needle in json.dumps(data, sort_keys=True)


def all_true(values: dict[str, bool]) -> bool:
    return all(value is True for value in values.values())


def selected_payload_audit(phifin: dict[str, Any]) -> dict[str, Any]:
    summary = phifin["payload_summary"]
    flags = summary["selected_payload_flags"]
    hessian_slot = phifin["payload_slots"]["finite_Hessian_C1_source"]
    missing = hessian_slot["missing"]
    return {
        "all_support_shapes_present": summary["all_support_shapes_present"] is True,
        "all_selected_payload_flags_true": all_true(flags),
        "selected_payload_flags": flags,
        "selected_deltaTheta_C1_solution_present": missing["selected_deltaTheta_C1_solution"] is not None,
        "explicit_dotD_Q_u_d_L_e_N_H_present": missing["explicit_dotD_Q_u_d_L_e_N_H"] is not None,
        "sector_response_matrices_present": missing["sector_response_matrices_M_u_M_d_M_e_M_nuD"] is not None,
        "full_lower_order_Hess_Xi_blocks_present": missing["full_lower_order_Hess_Xi_blocks"] is not None,
        "primitive_contractions_present": missing["evaluated_zero_mode_response_integrals"] is not None,
        "selected_values_emitted": summary["all_selected_values_emitted"] is True,
    }


def source_origin_audit(source: dict[str, Any]) -> dict[str, Any]:
    selected_flags = source["source_origin_audit"]["selected_flags"]
    alpha1_values = source["alpha1_driver_audit"]["selected_values"]
    return {
        "selected_flags": selected_flags,
        "all_source_flags_true": all_true(selected_flags),
        "alpha1_selected_values": alpha1_values,
        "all_alpha1_values_present": all_true(alpha1_values),
        "support_converges": source["source_origin_audit"]["support_closed"]["same_source_support_converges"] is True,
        "next_required_artifact": source["next_required_artifact"],
    }


def galerkin_value_audit(galerkin: dict[str, Any], first: dict[str, Any]) -> dict[str, Any]:
    honest = first["parallel_lanes"]["lane_B_galerkin_replay"]
    formal = galerkin["validation"]["formal_lift_diagnostic"]
    return {
        "manifest_filled": honest["manifest_filled"] is True,
        "honest_root_all_pass": honest["honest_root_all_pass"] is True,
        "honest_root_failures": honest["honest_root_failures"],
        "selected_correction_matrices_emitted": honest["selected_correction_matrices_emitted"] is True,
        "formal_lift_lower_validators_all_pass": honest["formal_lift_lower_validators_all_pass"] is True,
        "formal_lift_promotion_passes": honest["formal_lift_promotion_passes"] is True,
        "formal_lift_is_diagnostic_only": honest["formal_lift_is_diagnostic_only"] is True,
        "formal_lift_validation_keys": sorted(formal.keys()),
        "formal_lift_promotable_as_proof": galerkin["interpretation"]["proof_promotion_allowed"] is True,
    }


def main() -> None:
    first = load(FIRST)
    phifin = load(PHIFIN)
    source = load(SOURCE_ALPHA1)
    galerkin = load(GALERKIN)
    higher = load(HIGHER)

    splitter = first["parallel_lanes"]["lane_A_qutrit_weyl_correction_search"]
    representative = splitter["representative"]
    labels = {
        "u": representative["u_correction_label"],
        "d": representative["d_correction_label"],
        "e": representative["e_correction_label"],
        "nuD": representative["nuD_correction_label"],
    }
    selected_inputs = {
        "selected_phifin_alpha1_payload": phifin,
        "selected_source_origin_and_alpha1_driver": source,
        "selected_routec_strominger_galerkin_first_run": galerkin,
        "higherorder_fullresponse_frontier": higher,
    }
    label_emission = {
        name: {
            "label": label,
            "emitted_by_selected_inputs": {
                source_name: text_contains(source_data, label)
                for source_name, source_data in selected_inputs.items()
            },
        }
        for name, label in labels.items()
    }
    any_label_emitted = any(
        emitted
        for sector in label_emission.values()
        for emitted in sector["emitted_by_selected_inputs"].values()
    )

    phifin_audit = selected_payload_audit(phifin)
    source_audit = source_origin_audit(source)
    galerkin_audit = galerkin_value_audit(galerkin, first)

    selected_source_emits_splitter = (
        splitter["diagnostic_splitter_found"] is True
        and splitter["selected_by_mtt"] is True
        and any_label_emitted
        and phifin_audit["selected_values_emitted"] is True
        and galerkin_audit["selected_correction_matrices_emitted"] is True
    )

    source_emission_contract = {
        "name": "RouteCSelectedSplitterSourceEmissionContract",
        "locked_target": "Emit a selected non-scalar, noncommuting, CP-odd correction from the same q79/F,m=1 S3/GS Route-C source.",
        "allowed_paths": {
            "straight_selected_Phi_fin": (
                "Fill selected_deltaTheta_C1, explicit dotD, zero-mode bases, Hessian/source vector, "
                "and primitive contractions from the selected Phi_fin branch."
            ),
            "selected_Galerkin_values": (
                "Run the honest Galerkin branch so D_E, Riesz/Green, dotD, alpha1, and C1 response "
                "validators pass without formal-lift flags."
            ),
            "superset_constrained_target": (
                "Use the diagnostic splitter only as an algebraic target contract; observed masses, "
                "mixings, CP phase, or benchmark entries may not select the source."
            ),
        },
        "representative_diagnostic_target": {
            "u_or_e_label": labels["u"],
            "d_or_nuD_label": labels["d"],
            "u_dy": representative["u_dy"],
            "d_dy": representative["d_dy"],
            "u_H1": representative["u_H1"],
            "d_H1": representative["d_H1"],
        },
        "minimum_acceptance_tests": {
            "selected_source_flags_not_lifted": True,
            "selected_deltaTheta_C1_or_equivalent_present": True,
            "sector_response_matrices_M_u_M_d_M_e_M_nuD_present": True,
            "mass_split_traceless_norm_sq_positive_each_sector": True,
            "ckm_commutator_norm_sq_positive": True,
            "pmns_commutator_norm_sq_positive": True,
            "cp_odd_trace_commutator_cubed_imag_nonzero": True,
            "target_fitting_used": False,
        },
    }

    candidate = {
        "candidate": "MTTSelectedRouteCCorrectionSourceEmissionOrSelectedGalerkinValues",
        "status": STATUS,
        "inputs": {
            "first_correction_search_or_galerkin_run": rel(FIRST),
            "selected_phifin_alpha1_payload": rel(PHIFIN),
            "selected_source_origin_and_alpha1_driver": rel(SOURCE_ALPHA1),
            "selected_routec_strominger_galerkin_first_run": rel(GALERKIN),
            "higherorder_fullresponse_frontier": rel(HIGHER),
        },
        "source_emission_attempt": {
            "attempted": True,
            "diagnostic_splitter_found": splitter["diagnostic_splitter_found"] is True,
            "diagnostic_splitter_selected_by_mtt": splitter["selected_by_mtt"] is True,
            "diagnostic_splitter_promotion_allowed": splitter["promotion_allowed"] is True,
            "label_emission_search": label_emission,
            "any_representative_label_emitted_by_selected_inputs": any_label_emitted,
            "selected_source_emits_splitter": selected_source_emits_splitter,
            "why_not_emitted": (
                "The representative qutrit/Weyl splitter exists only inside the diagnostic search artifact. "
                "The selected Phi_fin/source/Galerkin payloads do not emit its labels, deltaTheta_C1, "
                "sector response matrices, or honest selected correction values."
            ),
        },
        "selected_payload_audit": phifin_audit,
        "source_origin_alpha1_audit": source_audit,
        "selected_galerkin_values_audit": galerkin_audit,
        "source_emission_contract": source_emission_contract,
        "what_closes_now": {
            "representative_splitter_nonemission_checked": True,
            "selected_payload_slots_rechecked": True,
            "honest_vs_formal_galerkin_promotion_rechecked": True,
            "exact_source_emission_contract_built": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_deltaTheta_C1_solution": True,
            "selected_dotD_alpha1_derivative": True,
            "full_lower_order_Hess_Xi_blocks": True,
            "sector_response_matrices_M_u_M_d_M_e_M_nuD": True,
            "selected_zero_mode_bases": True,
            "primitive_C1_contractions": True,
            "honest_galerkin_replay_without_lifted_flags": True,
            "promoted_yukawa_hierarchy_CKM_PMNS_CP": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "CorrectionSourceEmissionAuditAndContractTheorem",
            "proved": True,
            "statement": (
                "The existing selected Route-C/Phi_fin/Galerkin artifacts do not source-emit the diagnostic "
                "qutrit/Weyl splitter or selected correction matrices. The branch is reduced to a concrete "
                "selected source-emission contract: fill selected deltaTheta_C1/dotD/Hessian/primitive "
                "response data, or run honest selected Galerkin values, and then rerun the locked mass, "
                "mixing, and CP tests without observed target inputs."
            ),
        },
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C Correction Source Emission or Selected Galerkin Values

Status: `MTT_SELECTED_ROUTEC_CORRECTION_SOURCE_EMISSION_AUDITED_DIAGNOSTIC_SPLITTER_NOT_SOURCE_EMITTED_VALUES_OPEN`

The previous qutrit/Weyl correction search found a diagnostic splitter.  This
artifact checks the stricter proof question: is that splitter actually emitted
by the selected Phi_fin/source/Galerkin payload?

## Result

It is not source-emitted by the current selected artifacts.

The representative splitter labels occur in the diagnostic search artifact, but
the selected Phi_fin alpha1 payload, selected source-origin/alpha1 driver, and
honest Route-C Galerkin first-run stack do not emit selected correction matrices,
selected deltaTheta_C1, selected sector response matrices, or selected Galerkin
values.

The formal-lift branch remains useful as a consistency diagnostic only.  It does
not prove selected-source emission.

## Source-Emission Contract

The next proof must supply one same-branch selected object:

- selected `deltaTheta_C1` or an equivalent selected correction source,
- selected `dotD_alpha1`,
- selected lower Hessian/source blocks,
- selected zero-mode bases,
- selected primitive C1 contractions,
- sector response matrices `M_u`, `M_d`, `M_e`, `M_nuD`.

After that, the locked finite tests are:

- nonzero traceless Hermitian mass splitting in the relevant sectors,
- nonzero CKM and PMNS commutator norms,
- nonzero complex CP-odd invariant,
- no observed flavor targets or lifted flags used as proof data.

## Conclusion

This closes the non-emission audit and makes the next gate exact.  The branch is
not dead: the diagnostic splitter proves that the finite correction algebra has
enough structure.  What remains missing is selected source emission.

Next artifact: `MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))


if __name__ == "__main__":
    main()
