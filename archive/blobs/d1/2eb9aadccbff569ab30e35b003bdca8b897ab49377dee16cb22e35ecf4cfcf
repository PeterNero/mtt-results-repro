"""Build smooth trace-lift or E_Qa finite-part gate for projective rho_E."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "contract": DATA / "selected_heterotic_projectiverhoe_smooth_trace_lift_or_eqa_finitepart_contract.json",
    "trace_policy": DATA / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy.candidate.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "internal_finite_part": DATA / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json",
    "smooth_identifiability": DATA / "smooth_determinant_spectral_table_or_source_operator.candidate.json",
    "complement_gate": DATA / "complement_spectrum_or_smooth_operator_source.candidate.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart_certificate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_projectiverhoe_smooth_operator_source_packet_required.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothTraceLift_or_EQaFinitePartOperator_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTH_TRACE_LIFT_CURRENT_SOURCE_NOGO_EQA_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothOperator_SourcePacket_or_ComplementQuotientTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    contract = load(INPUTS["contract"])
    trace_policy = load(INPUTS["trace_policy"])
    finite_packet = load(INPUTS["finite_packet"])
    finite_part = load(INPUTS["internal_finite_part"])
    smooth_id = load(INPUTS["smooth_identifiability"])
    complement = load(INPUTS["complement_gate"])
    rplus = load(INPUTS["rplus_payload"])

    finite_logdet = finite_part["Delta_selected_internal_exact"]
    finite_logdet_numeric = finite_part["Delta_selected_internal_numeric"]
    lambda_examples = [2, 3, 5]
    nonidentifiability_examples = [
        {
            "smooth_completion": f"H_sel direct_sum [{lam}]",
            "same_selected_finite_packet": True,
            "smooth_logdet": f"log(2008) + log({lam})",
            "smooth_logdet_numeric": finite_logdet_numeric + math.log(lam),
        }
        for lam in lambda_examples
    ]

    trace_lift_lane = {
        "lane_id": "A_trace_lift_theorem",
        "status": "CURRENT_SOURCE_NO_GO",
        "support": {
            "finite_internal_trace_policy_closed": trace_policy["decision"]["finite_internal_trace_and_quotient_policy_closed"],
            "finite_logdet_closed": finite_logdet == "log(2008)",
            "prior_identifiability_no_go_available": smooth_id["smooth_complement_identifiability"]["smooth_determinant_identified"] is False,
            "complement_gate_reduced_determinant_isolated": complement["decision"]["reduced_coherent_sector_determinant"] == "CONDITIONAL_LOG_2008",
        },
        "missing": {
            "projection_family_from_smooth_operator_to_finite_labels": False,
            "heat_trace_convergence_or_exact_compression_theorem": False,
            "complement_cancellation_or_quotient_theorem": False,
            "no_double_count_BRST_or_FP_determinant_policy": False,
            "smooth_trace_equals_finite_eleven_label_trace": False,
        },
        "verdict": (
            "The finite trace is closed internally, but the current source does not "
            "prove it is the smooth heat/zeta/torsion trace."
        ),
    }

    eqa_lane = {
        "lane_id": "B_smooth_EQa_or_finitepart_operator",
        "status": "OPEN_SOURCE_PACKET_REQUIRED",
        "support": {
            "selected_finite_rhoE_packet_emitted": finite_packet["selected"],
            "Bismut_Rplus_geometry_available": rplus["decision"]["R_plus_curvature_filled"],
            "standard_embedding_retired": trace_policy["decision"]["standard_embedding_route_retired_for_current_branch"],
        },
        "missing": {
            "smooth_projective_transition_or_Deligne_Cech_data": False,
            "selected_bundle_connection_A": False,
            "selected_bundle_curvature_F_A": False,
            "representation_action_on_uE_one_forms": False,
            "kernel_and_quotient_policy": False,
            "E_Qa_matrix": False,
            "positive_spectrum_or_heat_zeta_torsion_table": False,
            "finite_part_regularization_scale": False,
        },
        "verdict": (
            "R+ supplies geometry only. E_Qa requires the selected bundle/operator "
            "source packet, not another normalization choice."
        ),
    }

    quotient_lane = {
        "lane_id": "C_complement_quotient_theorem",
        "status": "PARTIAL_NOT_PROMOTED",
        "support": {
            "GR_internal_separation_already_used": True,
            "finite_internal_quotient_policy_closed": trace_policy["closed_subclaims"]["finite_internal_quotient_policy"],
            "conditional_reduced_determinant_value": complement["reduced_determinant_conditional"]["value"],
        },
        "missing": {
            "smooth_complement_outside_QaSU3_threshold_response": False,
            "BRST_or_coherent_sector_exact_cancellation": False,
            "no_double_count_theorem": False,
        },
        "verdict": (
            "This is the shortest proof route if source text selects exact complement "
            "quotient/cancellation; current data still do not."
        ),
    }

    required_packet = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothOperatorSourcePacketRequired.v1",
        "status": "OPEN",
        "next_required_artifact": NEXT,
        "accepted_closing_routes": [
            "exact smooth complement quotient/cancellation theorem",
            "selected smooth projective rho_E transition plus bundle/operator E_Qa packet",
            "source-certified heat/zeta/torsion finite-part table replacing E_Qa",
        ],
        "minimum_smooth_operator_payload": {
            "smooth_projective_rhoE_transition_or_Deligne_Cech_representative": None,
            "selected_bundle_connection_A_or_equivalent_operator_source": None,
            "bundle_curvature_F_A": None,
            "representation_action_on_uE_one_forms": None,
            "kernel_and_quotient_policy": None,
            "E_Qa_matrix_or_equivalent_zero_order_block": None,
            "positive_spectrum_heat_zeta_or_torsion_finite_part": None,
            "trace_lift_or_complement_quotient_proof": None,
        },
        "forbidden_shortcuts": contract["forbidden_shortcuts"],
    }

    decision = {
        "finite_internal_result_preserved": True,
        "smooth_trace_lift_proved": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "current_source_no_go_for_trace_lift": True,
        "smooth_operator_source_packet_required": True,
        "best_next_route": "smooth_operator_source_packet_or_complement_quotient",
        "next_required_artifact": NEXT,
        "required_packet_path": rel(OUTPUT_PACKET),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothTraceLiftOrEQaFinitePartOperator",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "trace_policy": trace_policy["status"],
            "smooth_identifiability": smooth_id["status"],
            "complement_gate": complement["status"],
            "rplus_payload": rplus["status"],
        },
        "finite_internal_result": {
            "value": finite_logdet,
            "numeric": finite_logdet_numeric,
            "scope": finite_part["scope"],
            "preserved": True,
        },
        "smooth_nonidentifiability_witness": {
            "statement": "Appending any positive smooth-complement eigenvalue leaves the selected finite packet unchanged but changes the smooth determinant.",
            "examples": nonidentifiability_examples,
            "conclusion": "finite trace/logdet does not determine smooth heat/zeta/torsion finite part without a trace-lift or complement-quotient theorem",
        },
        "lanes": {
            "trace_lift": trace_lift_lane,
            "smooth_EQa_or_finitepart_operator": eqa_lane,
            "complement_quotient": quotient_lane,
        },
        "decision": decision,
        "guardrails": {
            "does_not_promote_finite_trace_to_smooth_trace": True,
            "does_not_claim_E_Qa": True,
            "does_not_reopen_standard_embedding": True,
            "does_not_use_gap_suppression_as_exact_determinant": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "ProjectiveRhoESmoothTraceLiftCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The selected finite projective rho_E packet fixes the internal quotient "
                "determinant log(2008), but it does not determine the smooth heat/zeta/"
                "torsion finite part. Positive complement modes can be appended without "
                "changing the finite packet while changing the smooth determinant. Hence "
                "closure now requires either an exact complement quotient/cancellation "
                "theorem or a selected smooth operator source packet computing E_Qa or an "
                "equivalent finite part."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT_PACKET.write_text(json.dumps(required_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "required_packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "finite_internal_result_preserved": True,
        "smooth_trace_lift_proved": False,
        "E_Qa_computed": False,
        "smooth_finitepart_computed": False,
        "current_source_no_go_for_trace_lift": True,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothTraceLift or EQaFinitePartOperator v1

## Result

```text
status = {STATUS}
finite_internal_result_preserved = true
smooth_trace_lift_proved = false
E_Qa_computed = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## The Key Point

The selected finite internal result remains exactly:

```text
Delta_selected_internal = log(2008)
```

But this is not automatically the smooth heat/zeta/torsion finite part. A
smooth completion can keep the same finite selected packet and append a positive
complement eigenvalue `Lambda`, changing the smooth determinant to:

```text
logdet_smooth = log(2008) + log(Lambda)
```

Therefore the finite trace cannot be promoted to a smooth trace without a source
theorem.

## What Would Close It

```text
{rel(OUTPUT_PACKET)}
```

The next proof must either source-select exact complement quotient/cancellation,
or emit the smooth projective `rho_E`/bundle/operator packet and compute `E_Qa`
or an equivalent heat/zeta/torsion finite part.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
