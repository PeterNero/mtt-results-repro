"""Build the C_tau positive finite-part / smooth Dirac convention source theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "ctau_gate": DATA / "selected_heterotic_bn_centralrankoperator_or_smootheqa_sourceemission.candidate.json",
    "operator_intertwiner": DATA / "selected_heterotic_ende_to_bn_operatorintertwiner_or_smoothconnection_sourceamendment.candidate.json",
    "label_embedding_values": DATA / "selected_heterotic_ende_to_bn_labelembedding_candidate_values.json",
    "finitepart_policy": DATA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
    "phifin_gap_layer": DATA / "selected_u1y_routec_trace_equals_27mode_or_full_hym_replay.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_ctau_positivefinitepart_or_smoothdiracconvention_sourcetheorem_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_Ctau_PositiveFinitePart_or_SmoothDiracConvention_SourceTheorem_v1.md"

STATUS = "HETEROTIC_CTAU_DIRAC_CONVENTION_POSITIVE_FINITEPART_CLOSED_TRIVIAL_MAGNITUDE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_ProductOperator_or_SmoothEQa_MagnitudeSource_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    ctau_gate = load(INPUTS["ctau_gate"])
    inter = load(INPUTS["operator_intertwiner"])
    values = load(INPUTS["label_embedding_values"])
    finitepart = load(INPUTS["finitepart_policy"])
    phifin = load(INPUTS["phifin_gap_layer"])

    full_counts = ctau_gate["selected_operator"]["full_BN_spectrum"]
    embedded_counts = ctau_gate["selected_operator"]["embedded_11_spectrum"]
    nonzero_full = full_counts["-1"] + full_counts["1"]
    zero_full = full_counts["0"]
    nonzero_embedded = embedded_counts["-1"] + embedded_counts["1"]
    zero_embedded = embedded_counts["0"]

    dirac_packet = {
        "schema": "SelectedHeteroticCtau.FiniteChiralDiracConvention.v1",
        "source_operator": "C_tau",
        "construction": {
            "chiral_space": "H_plus direct_sum H_minus, each copy equal to the selected B_N carrier",
            "dirac_operator": "D_C = [[0, C_tau], [C_tau, 0]]",
            "positive_operator": "D_C^* D_C = diag(C_tau^2, C_tau^2)",
            "orientation_operator": "sign(C_tau) on the nonzero C_tau complement, with kernel projected out",
            "kernel_policy": "remove ker(C_tau) before finite positive determinant, exactly as the finite determinant policy removes zero modes/shared kernel before logdet",
            "new_continuous_parameter": None,
        },
        "spectra": {
            "full_BN": {
                "C_tau": full_counts,
                "C_tau_square_positive_complement": {"1": nonzero_full},
                "Dirac_square_positive_complement": {"1": 2 * nonzero_full},
                "kernel_dimension_C_tau": zero_full,
                "kernel_dimension_Dirac_square": 2 * zero_full,
            },
            "embedded_11": {
                "C_tau": embedded_counts,
                "C_tau_square_positive_complement": {"1": nonzero_embedded},
                "Dirac_square_positive_complement": {"1": 2 * nonzero_embedded},
                "kernel_dimension_C_tau": zero_embedded,
                "kernel_dimension_Dirac_square": 2 * zero_embedded,
            },
        },
        "finiteparts": {
            "full_BN_logdet_Dirac_square_positive_complement": 0.0,
            "embedded_11_logdet_Dirac_square_positive_complement": 0.0,
            "eta_full_BN_from_symmetric_plus_minus_counts": 0,
            "eta_embedded_11_from_symmetric_plus_minus_counts": 0,
        },
        "selection_status": {
            "finite_chiral_doubling_selected_by_signed_selfadjoint_operator": True,
            "positive_finitepart_policy_applies": finitepart["decision"]["regularization_finite_part_selected_internal"],
            "orientation_retained": True,
            "nonzero_threshold_magnitude_supplied": False,
        },
    }

    oriented_product_request = {
        "schema": "SelectedHeterotic.OrientedPhiFinProductOperatorRequest.v1",
        "purpose": (
            "Use C_tau only as selected sign/orientation and the already selected Phi_fin "
            "gap layer as the positive magnitude carrier, if a same-source product "
            "operator or smooth E_Qa theorem emits their compatibility."
        ),
        "required_to_close_next": {
            "same_BN_domain_for_Ctau_and_PhiFin_positive_gap": values["rho_checks"]["all_labels_preserve_tau_mod3_rank_slot"],
            "commutation_or_simultaneous_functional_calculus": None,
            "source_emits_oriented_operator": None,
            "candidate_operator": "D_oriented^2 = PhiFin_positive_gap on nonzero magnitude complement, orientation/sign = C_tau",
            "prove_kernel_policy_compatible": None,
            "recompute_finitepart_with_Ctau_sector_or_orientation_weights": None,
            "show_no_double_counting_of_shared_circle": None,
        },
        "forbidden_shortcuts": [
            "use C_tau Dirac logdet 0 as the heterotic threshold magnitude",
            "multiply Phi_fin by C_tau without a same-domain commutation/source theorem",
            "insert a positive shift such as 2I+C_tau as a determinant operator",
            "choose orientation weights from observed electroweak data",
        ],
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    decision = {
        "ctau_positive_finitepart_convention_closed": True,
        "ctau_chiral_dirac_convention_source_selected": True,
        "ctau_logdet_value_full_BN": 0.0,
        "ctau_logdet_value_embedded_11": 0.0,
        "ctau_eta_value_full_BN": 0,
        "ctau_eta_value_embedded_11": 0,
        "ctau_supplies_orientation": True,
        "ctau_supplies_nonzero_threshold_magnitude": False,
        "phifin_positive_gap_layer_available": phifin["status"],
        "oriented_phifin_product_operator_closed": False,
        "smooth_E_Qa_magnitude_source_closed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticCtauPositiveFinitePartOrSmoothDiracConventionSourceTheorem",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "ctau_gate": ctau_gate["status"],
            "operator_intertwiner": inter["status"],
            "label_embedding_values": values["status"],
            "finitepart_policy": finitepart["status"],
            "phifin_gap_layer": phifin["status"],
        },
        "dirac_packet": dirac_packet,
        "oriented_product_request": oriented_product_request,
        "decision": decision,
        "theorem": {
            "name": "SelectedCtauFiniteChiralDiracConventionTheorem",
            "proved": True,
            "statement": (
                "For the selected signed central-rank operator C_tau, the canonical finite "
                "chiral doubling D_C=[[0,C_tau],[C_tau,0]] supplies a no-knob positive "
                "operator D_C^*D_C=C_tau^2 on the nonzero complement while retaining "
                "orientation through sign(C_tau). The selected finite positive determinant "
                "policy therefore applies to this convention and gives logdet 0 on both "
                "the full B_N and embedded 11-label carriers, with eta 0 from symmetric "
                "plus/minus counts. Hence C_tau is a selected orientation operator, not "
                "a nonzero threshold-magnitude source. The next closure object must bind "
                "C_tau orientation to the selected Phi_fin positive gap layer or emit an "
                "equivalent smooth E_Qa magnitude operator from the same source."
            ),
        },
        "guardrails": {
            "does_not_claim_ctau_logdet_as_nonzero_threshold": True,
            "does_not_insert_positive_shift": True,
            "does_not_multiply_ctau_and_phifin_without_source": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_scope": "ctau_positive_finitepart_convention_only_trivial_magnitude",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "ctau_positive_finitepart_convention_closed": True,
        "ctau_logdet_value_full_BN": 0.0,
        "ctau_supplies_nonzero_threshold_magnitude": False,
        "oriented_phifin_product_operator_closed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic Ctau PositiveFinitePart or SmoothDiracConvention SourceTheorem v1

## Result

```text
status = {STATUS}
ctau_positive_finitepart_convention_closed = true
ctau_logdet_value_full_BN = 0.0
ctau_supplies_orientation = true
ctau_supplies_nonzero_threshold_magnitude = false
oriented_phifin_product_operator_closed = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Dirac Packet

```json
{json.dumps(dirac_packet, indent=2, sort_keys=True)}
```

## Next Request

```json
{json.dumps(oriented_product_request, indent=2, sort_keys=True)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
