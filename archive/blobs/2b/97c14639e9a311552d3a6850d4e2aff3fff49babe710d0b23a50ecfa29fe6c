"""Build the smooth-transition/complement-quotient/no-double-count gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "rep_to_cocycle": DATA / "selected_heterotic_projectiverhoe_representative_to_cocycle_or_smoothfinitepart_sourceamendment.candidate.json",
    "smooth_missing": DATA / "selected_heterotic_projectiverhoe_representative_to_cocycle_smooth_missing_leaves.json",
    "gr_internal_separation": DATA / "gr_surface_internal_quantum_separation_theorem.candidate.json",
    "smooth_trace_lift": DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json",
    "smooth_source_fill": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothtransitiontables_or_complementquotient_nodoublecount.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothtransitiontables_or_complementquotient_nodoublecount_certificate.json"
OUTPUT_CONTRACT = DATA / "selected_heterotic_projectiverhoe_exact_complement_or_smooth_transition_value_contract.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothTransitionTables_or_ComplementQuotient_NoDoubleCount_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_NODOUBLECOUNT_POLICY_CLOSED_SMOOTHTABLES_COMPLEMENTQUOTIENT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_ExactComplementQuotient_or_SmoothRhoETransitionTables_ValuePacket_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    rep_to_cocycle = load(INPUTS["rep_to_cocycle"])
    smooth_missing = load(INPUTS["smooth_missing"])
    gr_sep = load(INPUTS["gr_internal_separation"])
    trace_lift = load(INPUTS["smooth_trace_lift"])
    source_fill = load(INPUTS["smooth_source_fill"])

    no_double_count_policy = {
        "closed": True,
        "source": rel(INPUTS["gr_internal_separation"]),
        "rule": (
            "Count the selected finite internal Qa/SU3 projective determinant once; "
            "route real smooth elastic GR/protospinor surface modes to the GR sector; "
            "do not append an independent smooth Qa/SU3 complement determinant unless "
            "a selected smooth operator packet or exact quotient/cancellation theorem is emitted."
        ),
        "finite_internal_value_retained": "log(2008)",
        "smooth_GR_surface_not_counted_as_QaSU3_internal_threshold": True,
        "shared_circle_role": "coherence/phase carrier, not a second smooth determinant domain",
    }

    contract = {
        "schema": "SelectedHeteroticProjectiveRhoEExactComplementOrSmoothTransitionValueContract.v1",
        "status": "VALUE_PACKET_REQUIRED",
        "closed_prerequisites": {
            "finite_representative_to_cocycle_map": rep_to_cocycle["decision"]["finite_representative_to_cocycle_map_closed"],
            "finite_projective_rhoE_character_table": rep_to_cocycle["decision"]["finite_projective_rhoE_character_table_closed"],
            "finite_internal_response_attached": rep_to_cocycle["decision"]["finite_internal_response_attached"],
            "no_double_count_policy": True,
        },
        "lane_A_smooth_transition_tables_required": [
            "selected good cover or finite quotient cover for the smooth heterotic source",
            "Deligne/Cech/B-field representative on that cover",
            "period unit map identifying the smooth class with the finite primitive c unit",
            "overlap transition matrices or generator/boundary projective rho_E tables",
            "cocycle law with central character exp(2*pi*i*tau/3)",
            "metric/unitarity compatibility",
            "mapped Freed-Witten and Bianchi checks",
            "projector retention from smooth module to F_i,G_i,P quotient",
            "bundle/operator action producing A/F_A or equivalent D_E",
        ],
        "lane_B_exact_complement_quotient_required": [
            "projection family from smooth operator domain to the eleven-label finite quotient",
            "proof that the orthogonal smooth complement contributes universally, cancels, or belongs only to GR/protospinor response",
            "heat/zeta/torsion determinant factorization theorem",
            "BRST/FP/gauge quotient determinant counted exactly once",
            "finite part equals log(2008) in internal units after quotient, without adding an arbitrary complement eigenvalue",
        ],
        "forbidden_shortcuts": [
            "use the finite character table as smooth transition matrices",
            "append or delete complement eigenvalues by convention",
            "reuse GR smooth response as a Qa/SU3 internal threshold",
            "set E_Qa=0 without a selected operator theorem",
            "compare to observed couplings or scales",
        ],
    }

    decision = {
        "no_double_count_policy_closed": True,
        "GR_surface_routing_closed": gr_sep["decision"]["GR_smooth_surface_response"] == "ROUTED_TO_GR_PROTOSPINOR_SECTOR",
        "finite_internal_quotient_retained": rep_to_cocycle["decision"]["finite_representative_to_cocycle_map_closed"],
        "smooth_transition_tables_emitted": False,
        "smooth_Deligne_representative_emitted": False,
        "exact_complement_quotient_closed": False,
        "smooth_bundle_operator_emitted": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "full_physical_threshold_claimed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothTransitionTablesOrComplementQuotientNoDoubleCount",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "rep_to_cocycle": rep_to_cocycle["status"],
            "gr_internal_separation": gr_sep["status"],
            "smooth_trace_lift": trace_lift["status"],
            "smooth_source_fill": source_fill["status"],
        },
        "no_double_count_policy": no_double_count_policy,
        "contract_path": rel(OUTPUT_CONTRACT),
        "decision": decision,
        "remaining_smooth_missing": smooth_missing["smooth_still_missing"],
        "cross_checks": {
            "rep_to_cocycle_finite_map_closed": rep_to_cocycle["decision"]["finite_representative_to_cocycle_map_closed"],
            "trace_lift_no_go_retained": trace_lift["decision"]["current_source_no_go_for_trace_lift"],
            "source_fill_smooth_values_absent": source_fill["decision"]["smooth_operator_source_packet_filled"] is False,
            "GR_no_double_count_guardrail_present": "this does not double-count local FP/BRST or gauge quotient determinants" in gr_sep["guardrails"],
            "smooth_nonidentifiability_examples_retained": len(trace_lift["smooth_nonidentifiability_witness"]["examples"]) == 3,
        },
        "guardrails": {
            "does_not_promote_no_double_count_to_exact_complement_quotient": True,
            "does_not_promote_finite_character_to_smooth_transition_tables": True,
            "does_not_claim_E_Qa": True,
            "does_not_claim_smooth_finitepart": True,
            "does_not_claim_physical_coupling_match": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "NoDoubleCountPolicyClosedExactComplementOrSmoothTablesOpen",
            "proved": True,
            "statement": (
                "Given the accepted GR-surface/internal-quantum separation and the "
                "finite representative-to-cocycle theorem, the no-double-count policy "
                "is closed: the finite internal Qa/SU3 determinant is counted once, "
                "and smooth GR/protospinor modes are not added as a second Qa/SU3 "
                "threshold complement. This does not by itself prove exact complement "
                "quotient/cancellation or emit smooth projective rho_E transition "
                "tables, so the next value packet must close one of those two lanes."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "contract_path": rel(OUTPUT_CONTRACT),
        "note_path": rel(OUTPUT_NOTE),
        "no_double_count_policy_closed": True,
        "smooth_transition_tables_emitted": False,
        "exact_complement_quotient_closed": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothTransitionTables or ComplementQuotient NoDoubleCount v1

## Result

```text
status = {STATUS}
no_double_count_policy_closed = true
smooth_transition_tables_emitted = false
exact_complement_quotient_closed = false
E_Qa_computed = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## Closed Subclause

The no-double-count policy is now theorem-derived from the GR-surface/internal
quantum separation: the selected finite internal Qa/SU3 determinant is counted
once, while real smooth elastic GR/protospinor modes are routed to the GR
sector and are not appended as an independent Qa/SU3 threshold determinant.

## Still Open

This does not emit smooth `rho_E` transition tables and does not prove exact
smooth complement quotient/cancellation. The next value packet must provide
one of those two objects.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_CONTRACT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
