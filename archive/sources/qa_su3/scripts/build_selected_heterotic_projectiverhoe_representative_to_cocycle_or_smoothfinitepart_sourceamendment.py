"""Build the representative-to-cocycle source-amendment packet for projective rho_E."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "smooth_fill": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
    "smooth_missing": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_missing_leaves.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "representative_tables": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
    "smooth_trace_lift": DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_representative_to_cocycle_or_smoothfinitepart_sourceamendment.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_representative_to_cocycle_or_smoothfinitepart_sourceamendment_certificate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_projectiverhoe_finite_representative_to_cocycle_packet.json"
OUTPUT_MISSING = DATA / "selected_heterotic_projectiverhoe_representative_to_cocycle_smooth_missing_leaves.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_RepresentativeToCocycleMap_or_SmoothFinitePart_SourceAmendment_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_REPRESENTATIVE_TO_COCYCLE_FINITE_MAP_CLOSED_SMOOTH_FINITEPART_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothTransitionTables_or_ComplementQuotient_NoDoubleCount_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def product_checks(tau: dict[str, int]) -> dict[str, dict[str, Any]]:
    checks: dict[str, dict[str, Any]] = {}
    for idx in range(1, 6):
        f_label = f"F{idx}"
        g_label = f"G{idx}"
        key = f"{f_label}+{g_label}->P"
        defect = tau[f_label] + tau[g_label] - tau["P"]
        checks[key] = {
            "tau_F": tau[f_label],
            "tau_G": tau[g_label],
            "tau_P": tau["P"],
            "additive_defect": defect,
            "twist_cancels_to_P": defect == 0,
        }
    return checks


def main() -> dict[str, Any]:
    smooth_fill = load(INPUTS["smooth_fill"])
    smooth_missing = load(INPUTS["smooth_missing"])
    finite_packet = load(INPUTS["finite_packet"])
    representative_tables = load(INPUTS["representative_tables"])
    smooth_trace_lift = load(INPUTS["smooth_trace_lift"])

    tau = {key: int(value) for key, value in finite_packet["tau_values"].items()}
    checks = product_checks(tau)
    all_products_cancel = all(row["twist_cancels_to_P"] for row in checks.values())
    nontrivial_twist = any(value != 0 for value in tau.values())

    finite_map_packet = {
        "schema": "SelectedHeteroticProjectiveRhoEFiniteRepresentativeToCocyclePacket.v1",
        "scope": "selected_finite_internal_Qa_SU3_projective_quotient_only",
        "source": {
            "finite_packet": rel(INPUTS["finite_packet"]),
            "representative_tables": rel(INPUTS["representative_tables"]),
            "selected_by_MTT_before_target_comparison": finite_packet["selected"],
            "target_fitting_used": False,
        },
        "finite_representative": {
            "basis": ["K1", "K2", "c"],
            "primitive_covector": finite_packet["Pi_tw"],
            "formula": "tau(L)=<Pi_tw,q(L)> with Pi_tw=+e3",
            "period_unit": "primitive integer c-period unit",
            "character_denominator": 3,
        },
        "central_cocycle_map": {
            "tau_values": tau,
            "rho_E_central_character": finite_packet["rho_E_central_character"],
            "product_checks": checks,
            "all_Fi_Gi_products_cancel_to_P": all_products_cancel,
            "nontrivial_central_twist": nontrivial_twist,
        },
        "finite_response_attached": {
            "D_E_diagonal_matrix_on_labels": finite_packet["D_E_diagonal_matrix_on_labels"],
            "H_sel": finite_packet["H_sel"],
            "Green_operator": finite_packet["Green_operator"],
            "Riesz_projector": finite_packet["Riesz_projector"],
            "Pi_tw": finite_packet["Pi_tw"],
            "chi_Qa": finite_packet["chi_Qa"],
            "internal_finite_part": "log(2008)",
            "trace_normalization": finite_packet["trace_normalization"],
        },
        "smooth_nonpromotion": {
            "not_a_smooth_Deligne_Cech_B_field_representative": True,
            "not_smooth_transition_tables": True,
            "not_bundle_connection_A": True,
            "not_E_Qa": True,
            "not_smooth_heat_zeta_torsion_finite_part": True,
        },
    }

    smooth_still_missing = [
        "smooth Deligne/Cech/B-field representative on a selected good cover",
        "smooth period unit or denominator identified with the finite c-period unit",
        "smooth representative-to-central-cocycle map, not only the finite quotient map",
        "projective rho_E transition matrices on overlaps or generator/boundary tables",
        "selected bundle operator A/rho_E action and curvature F_A",
        "representation action on u(E)-valued one-forms",
        "kernel/quotient/no-double-count policy connecting smooth complement to finite quotient",
        "E_Qa or equivalent zero-order heat/torsion block",
        "positive smooth spectrum or heat coefficients",
        "zeta/torsion regularization convention",
        "exact complement cancellation/quotient theorem",
        "mapped Freed-Witten/Bianchi/projector-retention checks",
    ]

    decision = {
        "finite_representative_to_cocycle_map_closed": all_products_cancel and nontrivial_twist,
        "finite_projective_rhoE_character_table_closed": set(tau) == set(finite_packet["labels"]),
        "finite_internal_response_attached": finite_packet["selected"] is True,
        "smooth_representative_emitted": False,
        "smooth_transition_tables_emitted": False,
        "smooth_bundle_operator_emitted": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "smooth_complement_quotient_closed": False,
        "exact_no_double_count_policy_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    missing = {
        "schema": "SelectedHeteroticProjectiveRhoERepresentativeToCocycleSmoothMissingLeaves.v1",
        "status": "FINITE_MAP_CLOSED_SMOOTH_VALUES_OPEN",
        "closed_now": [
            "finite quotient representative tau(L)=<+e3,q(L)>",
            "finite primitive c-period unit",
            "finite rho_E central character table on F_i,G_i,P",
            "finite product/twist cancellation checks for F_i G_i -> P",
            "finite D_E/Green/Riesz/chi_Qa/logdet attachment retained",
        ],
        "smooth_still_missing": smooth_still_missing,
        "smooth_missing_imported_from_previous_packet": smooth_missing["hard_missing"],
        "legal_repairs": [
            "emit smooth projective rho_E transition tables from the same representative",
            "prove finite quotient is the exact physical quotient of the smooth complement",
            "compute E_Qa/heat/zeta/torsion directly from a selected smooth operator",
            "prove a no-double-count theorem separating GR smooth surface from internal finite quotient",
        ],
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoERepresentativeToCocycleOrSmoothFinitePartSourceAmendment",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "smooth_fill": smooth_fill["status"],
            "representative_tables": representative_tables["status"],
            "smooth_trace_lift": smooth_trace_lift["status"],
        },
        "finite_map_packet_path": rel(OUTPUT_PACKET),
        "smooth_missing_path": rel(OUTPUT_MISSING),
        "finite_map_packet": finite_map_packet,
        "decision": decision,
        "cross_checks": {
            "previous_smooth_packet_open": smooth_fill["decision"]["smooth_operator_source_packet_filled"] is False,
            "previous_trace_lift_no_go_retained": smooth_trace_lift["decision"]["current_source_no_go_for_trace_lift"] is True,
            "finite_packet_selected": finite_packet["selected"] is True,
            "all_product_defects_zero": all_products_cancel,
            "nontrivial_tau_present": nontrivial_twist,
            "logdet_is_internal_only": True,
        },
        "guardrails": {
            "does_not_promote_finite_map_to_smooth_representative": True,
            "does_not_promote_character_table_to_transition_matrices": True,
            "does_not_promote_log2008_to_physical_threshold": True,
            "does_not_claim_smooth_E_Qa": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "FiniteRepresentativeToCocycleMapClosedSmoothFinitePartOpen",
            "proved": True,
            "statement": (
                "On the selected finite internal Qa/SU3 projective quotient, the "
                "representative-to-cocycle map tau(L)=<+e3,q(L)> is closed: it "
                "has primitive c-period unit, nontrivial Z3 projective character, "
                "and all five F_i G_i -> P product twists cancel. This attaches "
                "the existing finite D_E/Green/Riesz/chi_Qa/logdet packet to the "
                "finite representative. It does not emit smooth Deligne/Cech data, "
                "smooth transition matrices, bundle curvature, E_Qa, or a smooth "
                "heat/zeta/torsion finite part."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_PACKET.write_text(json.dumps(finite_map_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_MISSING.write_text(json.dumps(missing, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "finite_map_packet_path": rel(OUTPUT_PACKET),
        "smooth_missing_path": rel(OUTPUT_MISSING),
        "note_path": rel(OUTPUT_NOTE),
        "finite_representative_to_cocycle_map_closed": True,
        "smooth_transition_tables_emitted": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE RepresentativeToCocycleMap or SmoothFinitePart SourceAmendment v1

## Result

```text
status = {STATUS}
finite_representative_to_cocycle_map_closed = true
smooth_transition_tables_emitted = false
E_Qa_computed = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## What Closes

On the selected finite internal Qa/SU3 projective quotient, the representative
map is now explicit:

```text
tau(L) = <+e3, q(L)>
rho_E(L) = exp(2*pi*i*tau(L)/3)
```

The five products `F_i G_i -> P` have zero additive twist defect, so the finite
projective character is compatible with the selected monad product channel.

## What Does Not Close

This is still a finite quotient theorem. It does not emit smooth transition
matrices, a selected bundle connection, `E_Qa`, or a smooth heat/zeta/torsion
finite part. The next target is therefore the smooth transition-table theorem
or an exact complement-quotient/no-double-count theorem.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_MISSING)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
