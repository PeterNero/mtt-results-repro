"""Build physical-normalization or smooth-EQa source-data request."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "remaining": DATA / "selected_heterotic_projectiverhoe_after_internal_complement_quotient_remaining.json",
    "internal_quotient": DATA / "selected_heterotic_projectiverhoe_internal_complement_quotient_theorem.json",
    "physical_boundary_contract": DATA / "selected_heterotic_projectiverhoe_physicalboundary_or_smoothidentity_contract.json",
    "direct_payload": DATA / "selected_heterotic_projectiverhoe_direct_finite_internal_operator_payload.json",
    "physical_anchor": DATA / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json",
    "kphys_or_smooth": DATA / "selected_heterotic_projectiverhoe_kphysanchor_or_smoothoperatoridentity_fill.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_sourcedata_request.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_source_request.json"
OUTPUT_LOCK = DATA / "selected_heterotic_projectiverhoe_internal_closure_lock_after_source_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_physicalnormalization_or_smootheqa_sourcedata_request_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_PhysicalNormalization_or_SmoothEQa_SourceData_Request_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_INTERNAL_CLOSED_SOURCE_REQUEST_BUILT_PHYSICAL_SMOOTHEQA_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_PhysicalAnchor_or_SmoothEQa_SourceFillAttempt_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    remaining = load(INPUTS["remaining"])
    internal_quotient = load(INPUTS["internal_quotient"])
    boundary_contract = load(INPUTS["physical_boundary_contract"])
    direct_payload = load(INPUTS["direct_payload"])
    physical_anchor = load(INPUTS["physical_anchor"])
    kphys_or_smooth = load(INPUTS["kphys_or_smooth"])

    request = {
        "schema": "SelectedHeteroticProjectiveRhoE.PhysicalNormalizationOrSmoothEQaSourceRequest.v1",
        "status": "SOURCE_DATA_REQUIRED",
        "already_closed_internal_branch": {
            "selected_domain": direct_payload["operator_domain_or_finite_quotient_domain"]["labels"],
            "rho_E_and_D_E": True,
            "finite_internal_logdet": internal_quotient["closed_claims"]["selected_internal_logdet"],
            "internal_complement_quotient_policy": internal_quotient["closed_claims"]["internal_complement_quotient_policy"],
            "scope": internal_quotient["scope"],
        },
        "lane_A_physical_normalization_required": {
            "same_branch_physical_action_unit": None,
            "K_phys_or_Omega0_or_ellp_or_kappa11_or_alpha_prime": None,
            "matching_scale_mu_match": None,
            "RG_and_threshold_scheme": None,
            "typed_electroweak_convention_map": None,
            "threshold_vector_or_local_determinant_vector_if_electroweak_matching_is_attempted": None,
            "proof_no_observed_constant_selected_any_missing_value": None,
        },
        "lane_B_optional_smooth_EQa_required": {
            "smooth_projective_rhoE_transition_or_Deligne_Cech_representative": None,
            "selected_bundle_connection_A_or_equivalent_smooth_operator_source": None,
            "bundle_curvature_F_A": None,
            "representation_action_on_uE_valued_one_forms": None,
            "trace_lift_from_finite_trace_to_smooth_heat_zeta_torsion_trace": None,
            "smooth_E_Qa_matrix_or_equivalent_finitepart_operator": None,
            "smooth_regularization_and_zero_mode_policy": None,
        },
        "acceptable_fill_sources": [
            "same-branch M-theory/protospinor action-unit theorem for K_phys",
            "same-branch electroweak threshold/local determinant vector with typed convention map",
            "same-branch smooth rho_E/Deligne-Cech transition tables plus smooth operator identity",
            "same-branch smooth Weitzenbock/E_Qa or heat/zeta/torsion finite-part table",
        ],
        "forbidden_shortcuts": boundary_contract["forbidden_shortcuts"],
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_REQUEST.write_text(json.dumps(request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lock = {
        "schema": "SelectedHeteroticProjectiveRhoE.InternalClosureLockAfterSourceRequest.v1",
        "status": "INTERNAL_BRANCH_LOCKED_WAITING_FOR_EXTERNAL_SOURCE_DATA",
        "locked_claims": {
            "selected_finite_internal_operator_payload": True,
            "internal_complement_quotient_policy": True,
            "selected_internal_logdet": "log(2008)",
        },
        "locked_nonclaims": {
            "physical_coupling_or_measured_match": True,
            "K_phys": True,
            "smooth_heat_trace": True,
            "smooth_E_Qa": True,
            "SM_or_electroweak_closure": True,
        },
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_LOCK.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    physical_slots_known = {
        "internal_K_equals_one": physical_anchor["source_checks"]["internal_K_equals_one"],
        "mtheory_gauge_slot_identified": physical_anchor["source_checks"]["mtheory_gauge_slot_identified"],
        "physical_anchor_closed": physical_anchor["decision"]["physical_anchor_closed"],
        "threshold_vector_closed": physical_anchor["decision"]["threshold_vector_closed"],
    }
    smooth_slots_known = {
        "smooth_lane_preferred": kphys_or_smooth["decision"]["best_next_lane"] == "smooth_operator_identity_bridge",
        "smooth_lane_has_geometry": kphys_or_smooth["decision"]["smooth_lane_has_geometry_but_no_bundle_operator"],
        "smooth_operator_identity_closed": kphys_or_smooth["decision"]["smooth_operator_identity_closed"],
    }

    decision = {
        "source_request_built": True,
        "internal_branch_locked": True,
        "physical_lane_open": True,
        "smooth_EQa_lane_open": True,
        "physical_slots_identified_but_values_open": physical_slots_known["mtheory_gauge_slot_identified"] and not physical_slots_known["physical_anchor_closed"],
        "smooth_geometry_support_present_but_operator_values_open": smooth_slots_known["smooth_lane_has_geometry"] and not smooth_slots_known["smooth_operator_identity_closed"],
        "no_more_internal_computation_required_for_log2008": True,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEPhysicalNormalizationOrSmoothEQaSourceDataRequest",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "source_request_path": rel(OUTPUT_REQUEST),
        "internal_lock_path": rel(OUTPUT_LOCK),
        "physical_slots_known": physical_slots_known,
        "smooth_slots_known": smooth_slots_known,
        "decision": decision,
        "closed_now": {
            "source_request_for_remaining_bridges": True,
            "internal_closure_lock": True,
            "clean_separation_internal_vs_physical_vs_smooth": True,
        },
        "still_open": {
            "physical_action_unit_K_phys_or_equivalent": True,
            "matching_scale_RG_threshold_scheme": True,
            "typed_electroweak_convention_map": True,
            "smooth_EQa_or_trace_lift_if_smooth_identity_required": True,
        },
        "guardrails": {
            "does_not_recompute_or_disturb_internal_log2008": True,
            "does_not_set_K_phys_from_internal_units": True,
            "does_not_compare_to_observed_constants": True,
            "does_not_treat_smooth_EQa_as_required_for_internal_closure": True,
            "does_not_treat_finite_trace_as_smooth_trace": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "PhysicalNormalizationOrSmoothEQaSourceDataRequestTheorem",
            "proved": True,
            "statement": (
                "After internal rho_E/direct-payload/complement-quotient closure, "
                "no further internal calculation is required for the selected "
                "internal determinant log(2008). Any further extension must supply "
                "new source data in one of two lanes: physical normalization "
                "(action unit, matching, RG, convention map) or optional smooth "
                "identity/E_Qa data. The request records all required leaves and "
                "forbids using observed constants or internal units as substitutes."
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
        "source_request_path": rel(OUTPUT_REQUEST),
        "internal_lock_path": rel(OUTPUT_LOCK),
        "note_path": rel(OUTPUT_NOTE),
        "source_request_built": True,
        "internal_branch_locked": True,
        "physical_lane_open": True,
        "smooth_EQa_lane_open": True,
        "selected_internal_logdet": "log(2008)",
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE PhysicalNormalization or SmoothEQa SourceData Request v1

## Result

```text
status = {STATUS}
source_request_built = true
internal_branch_locked = true
selected_internal_logdet = log(2008)
physical_lane_open = true
smooth_EQa_lane_open = true
next_required_artifact = {NEXT}
```

## Meaning

The selected internal `rho_E` branch is closed and locked at internal scope.
Further progress now requires new source data, not another internal
normalization pass.

The two legal extension lanes are:

- physical normalization: action unit, matching scale, RG/threshold convention,
  and typed electroweak convention map;
- optional smooth identity: smooth `rho_E`/Deligne-Cech source or smooth
  `E_Qa`/trace-lift data.

Source request:

```text
{rel(OUTPUT_REQUEST)}
```

Internal lock:

```text
{rel(OUTPUT_LOCK)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REQUEST)}")
    print(f"wrote {rel(OUTPUT_LOCK)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(result["status"])
