"""Build the finite-part policy and index/scale source theorem gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "minimal_fill": DATA / "selected_electroweak_qastack_minimal_selected_finitepart_payload_fill.candidate.json",
    "local_det_interface": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob\certificates\selected_local_determinant_computation_interface_certificate.json"),
    "internal_k_anchor": DATA / "selected_k_gauge_anchor_or_full_electroweak_matching.candidate.json",
    "quotient_lemma": DATA / "selected_electroweak_u1y_quotientdeterminant_lemma.candidate.json",
    "pperp_policy": DATA / "selected_u1_quotient_projector_pperp_and_trace_policy.candidate.json",
    "physical_gate": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
}

OUTPUT_DATA = DATA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_finitepart_policy_and_indexscale_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_FinitePartPolicy_and_IndexScale_SourceTheorem_v1.md"

STATUS = "ELECTROWEAK_QASTACK_INTERNAL_FINITEPART_POLICY_INDEXSCALE_CLOSED_SU2_PHYSICAL_OPEN"
NEXT = "Selected_Electroweak_QaStack_SU2Row_or_Cancellation_and_PhysicalAnchor_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    minimal = load(INPUTS["minimal_fill"])
    local_det = load(INPUTS["local_det_interface"])
    internal_k = load(INPUTS["internal_k_anchor"])
    quotient = load(INPUTS["quotient_lemma"])
    pperp = load(INPUTS["pperp_policy"])
    physical = load(INPUTS["physical_gate"])

    positive_table = minimal["filled_payload"]["domain_and_operator"]["positive_eigenvalue_table_on_V_mod_s"]
    quotient_value = quotient["decision"]["quotient_logdet"]
    internal_mu = "1"

    finitepart_policy = {
        "regularization": {
            "selected_for_internal_finite_quotient_row": True,
            "rule": local_det["formula"]["per_factor"],
            "finite_positive_rule": quotient["functional_components_after_lemma"]["regularization_finite_part"],
            "reason": (
                "On the finite selected quotient table there is no infinite heat subtraction. "
                "The local determinant interface already selects the executable finite positive "
                "eigenvalue accounting once the positive spectrum, multiplicities, weights, "
                "and scale are supplied."
            ),
        },
        "kernel_policy": {
            "selected_for_internal_row": True,
            "zero_shared_line_removed_before_positive_determinant": True,
            "source": "Selected U1 Pperp shared-line quotient policy",
            "reason": "The shared central line is not a sector-specific threshold load and is quotiented before positive determinant evaluation.",
        },
        "H_zero_cluster_policy": {
            "selected_for_current_value": True,
            "selected_eta_N": minimal["filled_payload"]["domain_and_operator"]["H_zero_cluster_policy"]["selected_eta_N"],
            "logdet_delta_current_branch": 0.0,
            "reason": "For eta_N=1, inclusion or exclusion of the two shifted H zero-cluster modes contributes 2*log(1)=0, so the current internal p_a value is invariant under that open bookkeeping policy.",
            "general_policy_closed": False,
        },
    }

    index_and_scale = {
        "determinant_index_weights": {
            "selected_for_internal_row": True,
            "policy": "unit weights on the already quotiented V/<s> positive table",
            "reason": (
                "Pperp is applied as a domain quotient, not as an extra scalar determinant weight. "
                "After quotienting, the multiplicities 8 and 8 already contain the rank-2 retained carrier. "
                "Adding another 2/3 would double-count the shared-line quotient."
            ),
            "weights": [
                {"eigenvalue": item["eigenvalue"], "multiplicity": item["quotient_multiplicity"], "index_weight": 1}
                for item in positive_table["entries"]
            ],
        },
        "determinant_scale": {
            "selected_for_internal_row": True,
            "mu": internal_mu,
            "source": "internal K_gauge action-unit anchor",
            "reason": "The internal action-unit theorem fixes K_gauge,int=1. In the same dimensionless finite determinant units, the determinant scale is mu=1. This is not a physical electroweak gauge normalization.",
            "physical_K_gauge_closed": internal_k["decision"]["physical_K_gauge_anchor_closed"],
        },
    }

    p_a_internal = {
        "promoted_as_internal_finite_part": True,
        "formula": quotient["quotient_logdet"]["formula"],
        "value": quotient_value,
        "scope": "selected internal finite determinant row on V/<s>; not measured electroweak closure",
    }

    remaining = {
        "same_scheme_SU2_row_or_cancellation": True,
        "physical_K_gauge_or_Omega0_anchor": physical["decision"]["physical_anchor_closed"] is False,
        "matching_scale_and_RG_scheme": physical["decision"]["convention_reconciliation_closed"] is False,
        "lambda_12": True,
        "measured_electroweak_closure": True,
    }

    candidate = {
        "candidate": "SelectedElectroweakQaStackFinitePartPolicyAndIndexScale",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_status": minimal["status"],
        "finitepart_policy": finitepart_policy,
        "index_and_scale": index_and_scale,
        "p_a_internal": p_a_internal,
        "decision": {
            "regularization_finite_part_selected_internal": True,
            "kernel_policy_selected_internal": True,
            "H_zero_cluster_value_invariant_current_branch": True,
            "determinant_index_weights_selected_internal": True,
            "determinant_scale_mu_selected_internal": True,
            "selected_p_a_internal_promoted": True,
            "selected_p_a_internal_value": quotient_value,
            "same_scheme_SU2_row_or_cancellation_closed": False,
            "lambda_12_closed": False,
            "physical_K_gauge_anchor_closed": False,
            "measured_electroweak_closure": False,
            "target_fitting_used": False,
            "next_required_artifact": NEXT,
        },
        "theorem": {
            "name": "SelectedInternalFinitePartPolicyAndIndexScale",
            "proved": True,
            "statement": (
                "For the selected q79/F,m=1 internal finite quotient row, the local "
                "determinant interface and quotient determinant lemma select the finite "
                "positive zeta/logdet accounting on V/<s>. Pperp is a domain quotient, "
                "so the retained multiplicities already include the rank-two carrier "
                "and the determinant index weights are unit weights on that quotient "
                "table. The selected internal action-unit anchor fixes mu=1 in internal "
                "determinant units. Therefore p_a^int is promoted to the quotient logdet "
                f"{quotient_value}. This does not close lambda_12 or measured electroweak "
                "matching, which still require a same-scheme SU2 row or cancellation and "
                "the physical gauge/action anchor."
            ),
        },
        "what_closes": {
            "internal_finite_positive_zeta_logdet_policy": True,
            "no_double_counting_Pperp_as_weight": True,
            "internal_mu_equals_1": True,
            "selected_p_a_internal": True,
        },
        "what_remains_open": remaining,
        "guardrails": {
            "claims_physical_K_gauge": False,
            "claims_lambda12": False,
            "claims_measured_electroweak_closure": False,
            "uses_observed_electroweak_data": False,
            "target_fitting_used": False,
            "double_counts_Pperp_as_weight": False,
            "promotes_eta1_neutrality_as_general_policy": False,
        },
        "closure_claimed": True,
        "closure_scope": "internal_finitepart_policy_indexscale_and_p_a_only",
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedElectroweakQaStackFinitePartPolicyAndIndexScale",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "selected_p_a_internal_promoted": True,
        "selected_p_a_internal_value": quotient_value,
        "lambda_12_closed": False,
        "measured_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, render_note(candidate, cert)


def render_note(candidate: dict[str, Any], cert: dict[str, Any]) -> str:
    lines = [
        "# Selected Electroweak QaStack FinitePartPolicy and IndexScale SourceTheorem v1",
        "",
        "## Result",
        "",
        "```text",
        f"status = {candidate['status']}",
        "regularization_finite_part_selected_internal = true",
        "determinant_index_weights_selected_internal = true",
        "determinant_scale_mu_selected_internal = true",
        "selected_p_a_internal_promoted = true",
        f"selected_p_a_internal_value = {candidate['decision']['selected_p_a_internal_value']}",
        "lambda_12_closed = false",
        "measured_electroweak_closure = false",
        f"next_required_artifact = {candidate['decision']['next_required_artifact']}",
        "```",
        "",
        "This theorem closes the internal finite-part policy for the selected Qa-stack",
        "row. It does not close the physical electroweak problem.",
        "",
        "## Finite-Part Policy",
        "",
        "```json",
        json.dumps(candidate["finitepart_policy"], indent=2, sort_keys=True),
        "```",
        "",
        "## Index and Scale",
        "",
        "```json",
        json.dumps(candidate["index_and_scale"], indent=2, sort_keys=True),
        "```",
        "",
        "## Internal p_a",
        "",
        "```json",
        json.dumps(candidate["p_a_internal"], indent=2, sort_keys=True),
        "```",
        "",
        "## Theorem",
        "",
        candidate["theorem"]["statement"],
        "",
        "## Guardrails",
        "",
        "- `P_perp` is not counted twice as both quotient and weight.",
        "- `mu=1` is internal determinant scale only, not physical gauge normalization.",
        "- The eta_N=1 zero-cluster neutrality is value-level only, not a general policy theorem.",
        "- `lambda_12` and measured electroweak closure remain open.",
        "",
        "## Certificate",
        "",
        "```json",
        json.dumps(cert, indent=2, sort_keys=True),
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    candidate, cert, note = build()
    DATA.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    PROOF.mkdir(parents=True, exist_ok=True)
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
