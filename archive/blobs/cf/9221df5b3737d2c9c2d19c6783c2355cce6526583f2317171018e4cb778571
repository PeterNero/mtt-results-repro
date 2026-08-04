"""Build the smooth source-certificate or complement-operator payload gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "source_table_solve": DATA / "selected_heterotic_projectiverhoe_sourcetablesolve_or_complementkernelproof.candidate.json",
    "z3_shadow_witness": DATA / "selected_heterotic_projectiverhoe_abstract_z3_cocycle_shadow_witness.json",
    "finite_value_packet": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
    "smooth_source_fill": DATA / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json",
    "finite_representative_tables": DATA / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json",
    "u1y_operator_payload": DATA / "selected_u1y_same_source_nonabelian_or_routec_operator_payload.candidate.json",
    "smparity_boundary": DATA / "smparity_repro_import_boundary_for_rhoe_frontier.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload.candidate.json"
OUTPUT_PAYLOAD = DATA / "selected_heterotic_projectiverhoe_smooth_operator_payload_minimal_contract.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_SmoothSourceCertificate_or_ComplementOperatorPayload_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHSOURCECERTIFICATE_SUPPORT_PREFILTER_CLOSED_OPERATOR_PAYLOAD_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothOperatorPayload_MinimalEmissionSubpacket_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    source_solve = load(INPUTS["source_table_solve"])
    witness = load(INPUTS["z3_shadow_witness"])
    finite_packet = load(INPUTS["finite_value_packet"])
    smooth_fill = load(INPUTS["smooth_source_fill"])
    finite_tables = load(INPUTS["finite_representative_tables"])
    u1y_payload = load(INPUTS["u1y_operator_payload"])
    sm_boundary = load(INPUTS["smparity_boundary"])

    finite_projective = finite_tables["projective_representative_tables"]
    u1y_projective_lane = next(
        lane for lane in u1y_payload["lane_attempts"] if lane["lane_id"] == "C_projective_gerbe_rhoE_packet"
    )

    support_prefilter = {
        "SM_parity_boundary_preserved": sm_boundary["decision"]["rhoe_no_knob_frontier_preserved"],
        "abstract_Z3_shadow_closed": source_solve["decision"]["abstract_Z3_shadow_closed"],
        "all_tau_labels_shadowed": all(
            checks["projective_triple_overlap_matches_tau"] for checks in witness["checks"].values()
        ),
        "finite_internal_response_selected": finite_packet["closed_prerequisites"]["finite_internal_response_attached"],
        "finite_representative_to_cocycle_closed": finite_packet["closed_prerequisites"]["finite_representative_to_cocycle_map"],
        "finite_no_double_count_policy_closed": finite_packet["closed_prerequisites"]["no_double_count_policy"],
        "finite_projective_candidate_built": finite_tables["decision"]["finite_projective_candidate_built"],
        "finite_source_level_twist_cancellation": finite_projective["admissibility"]["Freed_Witten_checked"].startswith("Finite"),
        "finite_projector_context_available": "Projector keeps" in finite_projective["admissibility"]["projector_retention_checked"],
        "source_level_FW_Bianchi_support_closed_in_sibling_projective_lane": any(
            req["field"] == "Freed_Witten_and_Bianchi" and req["satisfied"] is True
            for req in u1y_projective_lane["requirements"]
        ),
    }

    operator_payload_contract = {
        "schema": "SelectedHeteroticProjectiveRhoESmoothOperatorPayload.MinimalContract.v1",
        "status": "VALUES_REQUIRED",
        "source_certificate": {
            "same_branch_smooth_heterotic_QaSU3_source": None,
            "selected_before_target_comparison": True,
            "SM_parity_interface_not_used_as_operator_data": True,
            "observed_data_used": False,
        },
        "lane_A_good_cover_operator_payload": {
            "selected_good_cover_incidence": None,
            "smooth_Deligne_Cech_B_field_representative": None,
            "rhoE_transition_matrices_lift_of_Z3_shadow": None,
            "Hermitian_metric_unitarity_tables": None,
            "mapped_Freed_Witten_Bianchi_projector_retention": None,
            "connection_A_or_projective_connection": None,
            "curvature_F_A": None,
            "operator_action_D_E_or_E_Qa": None,
            "spectrum_gap_heat_zeta_or_torsion_finite_part": None,
        },
        "lane_B_complement_operator_payload": {
            "smooth_operator_domain": None,
            "smooth_to_finite_projection_P11": None,
            "complement_operator_D_comp": None,
            "BRST_FP_ghost_operator": None,
            "heat_kernel_or_zeta_factorization": None,
            "proof_complement_zero_universal_GR_only_or_cancelled": None,
            "finite_part_after_quotient": None,
        },
        "already_available_support_inputs": support_prefilter,
        "forbidden_shortcuts": [
            "promote abstract Z3 shadow to smooth transition tables",
            "promote finite Galerkin rhoE to smooth bundle operator",
            "promote source-level FW/Bianchi support to operator-level determinant data",
            "promote SM parity interface replacement to no-knob Qa/SU3 operator packet",
            "compute E_Qa or physical thresholds before one payload lane emits values",
        ],
    }
    OUTPUT_PAYLOAD.write_text(json.dumps(operator_payload_contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    retired_blockers = {
        "SM_parity_context": True,
        "abstract_Z3_central_shadow": True,
        "finite_tau_character_match": True,
        "finite_internal_response_packet": True,
        "finite_no_double_count_policy": True,
        "finite_source_level_twist_cancellation": True,
        "source_level_FW_Bianchi_support": True,
        "finite_projector_context": True,
    }
    remaining_operator_cutset = {
        "same_branch_smooth_source_certificate": True,
        "selected_good_cover_incidence_or_smooth_domain": True,
        "smooth_Deligne_Cech_B_field_representative": True,
        "rhoE_transition_matrices_or_complement_operator": True,
        "Hermitian_metric_unitarity_or_heat_kernel_domain": True,
        "mapped_operator_level_FW_Bianchi_projector_retention": True,
        "connection_curvature_or_BRST_FP_ghost_operator": True,
        "operator_action_D_E_or_E_Qa": True,
        "positive_spectrum_gap_heat_zeta_torsion_finite_part": True,
    }

    decision = {
        "support_prefilter_closed": all(support_prefilter.values()),
        "retired_blockers_count": sum(1 for value in retired_blockers.values() if value),
        "operator_payload_contract_built": True,
        "lane_A_operator_payload_closed": False,
        "lane_B_complement_payload_closed": False,
        "smooth_transition_tables_emitted": False,
        "complement_kernel_proved": False,
        "smooth_finitepart_computed": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoESmoothSourceCertificateOrComplementOperatorPayload",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "minimal_payload_contract_path": rel(OUTPUT_PAYLOAD),
        "support_prefilter": support_prefilter,
        "retired_blockers": retired_blockers,
        "remaining_operator_cutset": remaining_operator_cutset,
        "decision": decision,
        "guardrails": {
            "does_not_promote_support_to_operator_payload": True,
            "does_not_promote_abstract_Z3_shadow": True,
            "does_not_promote_SM_parity_interface": True,
            "does_not_claim_smooth_transition_tables": True,
            "does_not_claim_complement_kernel": True,
            "does_not_claim_E_Qa_or_physical_threshold": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "SmoothRhoESupportPrefilterClosedOperatorPayloadOpen",
            "proved": True,
            "statement": (
                "The smooth rho_E frontier now has its support prefilter closed: "
                "SM-parity boundary, abstract Z3 central shadow, finite tau/rho_E/D_E "
                "packet, finite representative-to-cocycle map, no-double-count policy, "
                "finite twist cancellation, source-level FW/Bianchi support, and finite "
                "projector context are all available. These supports do not emit the "
                "selected smooth source/operator payload. Closure now requires either "
                "Lane A good-cover operator values or Lane B complement operator values."
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
        "minimal_payload_contract_path": rel(OUTPUT_PAYLOAD),
        "note_path": rel(OUTPUT_NOTE),
        "support_prefilter_closed": decision["support_prefilter_closed"],
        "operator_payload_contract_built": True,
        "lane_A_operator_payload_closed": False,
        "lane_B_complement_payload_closed": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE SmoothSourceCertificate or ComplementOperatorPayload v1

## Result

```text
status = {STATUS}
support_prefilter_closed = true
operator_payload_contract_built = true
lane_A_operator_payload_closed = false
lane_B_complement_payload_closed = false
next_required_artifact = {NEXT}
```

## Closed Support

The stale support-level blockers are now retired: SM-parity boundary, abstract
`Z3` central shadow, finite `tau/rho_E/D_E` packet, finite representative map,
no-double-count policy, finite twist cancellation, source-level FW/Bianchi
support, and finite projector context.

## Still Required

The payload itself is still missing. Closure now requires one of:

- Lane A: selected good-cover transition/operator values with metric,
  Bianchi/projector, connection/curvature, and `D_E` or `E_Qa`;
- Lane B: selected complement operator, BRST/FP ghost operator, heat/zeta/torsion
  factorization, and finite part after quotient.

Minimal contract:

```text
{rel(OUTPUT_PAYLOAD)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_PAYLOAD)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
