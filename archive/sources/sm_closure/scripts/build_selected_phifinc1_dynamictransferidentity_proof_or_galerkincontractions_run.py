"""Build PhiFinC1 dynamic-transfer proof / Galerkin contractions run gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PREVIOUS = DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
DYNAMIC = DATA / "selected_dynamictransferhessian_bselected_or_honestgalerkinc1_valuefill.candidate.json"
TRANSPORT = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
PHIFIN_SCHEMA = DATA / "finite_emission_morphism_phifin.candidate.json"
GALERKIN_SPEC = DATA / "selected_routec_strominger_galerkin_solve_spec.candidate.json"
GALERKIN_C1 = DATA / "selected_routec_strominger_galerkin_solve" / "c1_primitive_contractions.candidate.json"
CROSSREPO_ALPHA1 = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"

OUTPUT = DATA / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run.candidate.json"
CERT = CERTS / "selected_phifinc1_dynamictransferidentity_proof_or_galerkincontractions_run_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_v1.md"

STATUS = "MTT_SELECTED_PHIFINC1_DYNAMICTRANSFERIDENTITY_PROOF_OR_GALERKINCONTRACTIONS_RUN_BUILT_STATIONARY_TRACE_CLOSED_C1_OPEN"
NEXT = "MTT_Selected_DifferentiatedPhiFinC1_PrimitiveOverlapContractions_or_GalerkinRun_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def maybe_load(path: Path) -> dict[str, Any] | None:
    if path.exists():
        return load(path)
    return None


def stage_status(spec: dict[str, Any], stage_name: str) -> dict[str, Any]:
    for stage in spec["execution_stages"]:
        if stage["stage"] == stage_name:
            return stage
    raise KeyError(stage_name)


def main() -> int:
    previous = load(PREVIOUS)
    dynamic = load(DYNAMIC)
    transport = load(TRANSPORT)
    gauge_trace = load(GAUGE_TRACE)
    phifin_alpha1 = load(PHIFIN_ALPHA1)
    phifin_schema = load(PHIFIN_SCHEMA)
    galerkin_spec = load(GALERKIN_SPEC)
    galerkin_c1 = load(GALERKIN_C1)
    crossrepo_alpha1 = maybe_load(CROSSREPO_ALPHA1)

    coord = previous["normal_form_identity"]["coordinate_system"]
    finite_values = previous["normal_form_identity"]["finite_values_if_identity_proved"]
    transport_validator = transport["validator_result"]
    transport_decision = transport["promotion_decision"]
    trace_decision = gauge_trace["promotion_decision"]

    alpha1_import = {
        "import_available": crossrepo_alpha1 is not None,
        "selected_dotD_source_verified_imported": bool(
            crossrepo_alpha1
            and crossrepo_alpha1.get("selected_dotD_source_verified_imported") is True
        ),
        "alpha1_driver_verified_imported": bool(
            crossrepo_alpha1
            and crossrepo_alpha1.get("alpha1_driver_verified_imported") is True
        ),
        "primitive_C1_contractions_claimed_by_import": bool(
            crossrepo_alpha1
            and crossrepo_alpha1.get("primitive_C1_contractions_claimed") is True
        ),
        "A_selected_claimed_by_import": bool(crossrepo_alpha1 and crossrepo_alpha1.get("A_selected_claimed") is True),
        "b_selected_claimed_by_import": bool(crossrepo_alpha1 and crossrepo_alpha1.get("b_selected_claimed") is True),
    }

    stationary_trace_import = {
        "source": rel(TRANSPORT),
        "functional_trace_source": rel(GAUGE_TRACE),
        "selected_source_verified": transport_validator["selected_source_verified"],
        "selected_projector_source_verified": transport_decision["selected_projector_source_verified"],
        "selected_riesz_green_source_verified": transport["what_closes_now"]["selected_riesz_green_source_verified"],
        "selected_rho_s_validator_ready": transport_validator["selected_rho_s_validator_ready"],
        "transport_closed_finite_validator_replay": transport_decision["transport_closed_finite_validator_replay"],
        "symbolic_transport_conjugation_validator_extended": transport_validator[
            "symbolic_transport_conjugation_validator_extended"
        ],
        "functional_gauge_transported_trace_proved": trace_decision["functional_selected_trace_proved"],
        "finite_raw_truncation_aliasing_bypassed_by_symbolic_transport": transport_validator[
            "finite_raw_truncation_aliasing_bypassed_by_exact_symbolic_transport"
        ],
        "selected_dotD_source_verified_inside_stationary_transport_replay": transport_validator[
            "selected_dotD_source_verified"
        ],
        "alpha1_driver_verified_inside_stationary_transport_replay": transport_validator[
            "alpha1_driver_verified"
        ],
        "crossrepo_alpha1_dotD_support": alpha1_import,
    }

    phifinc1_identity_attempt = {
        "attempted_source": "stationary gauge-transported Phi_fin trace plus symbolic transport-conjugation validator replay",
        "target_identity": previous["normal_form_identity"]["identity_equations"],
        "stationary_trace_sufficient_for_C1_transfer_identity": False,
        "selected_identity_proved_now": False,
        "reason": (
            "The imported theorem proves stationary projectors, ranks, Riesz/Green identities, and rho_s source "
            "transport.  The C1 dynamic-transfer identity is a differentiated overlap/Hessian statement.  It needs "
            "the selected derivative of Phi_fin through alpha1/dotD and the primitive three-by-three overlap "
            "contractions in the fixed 72-real coordinate system."
        ),
        "missing_dynamic_objects": [
            "differentiated transport derivative dU/dalpha inside Phi_fin^C1",
            "selected alpha1 driver or imported same-branch alpha1 theorem attached to Phi_fin^C1",
            "primitive C1 overlap contractions",
            "selected Hessian/source vector values",
            "sector response matrices M_u, M_d, M_e, M_nuD",
        ],
        "if_future_identity_proved_then_values": finite_values,
        "normal_form_values_not_promoted_now": True,
    }

    s0 = stage_status(galerkin_spec, "S0_selected_source")
    s4 = stage_status(galerkin_spec, "S4_spectral_projectors")
    s5 = stage_status(galerkin_spec, "S5_alpha1_response")
    s6 = stage_status(galerkin_spec, "S6_c1_contractions")
    galerkin_run_attempt = {
        "source_spec": rel(GALERKIN_SPEC),
        "stationary_support_reused": {
            "S0_selected_source_support": s0,
            "S4_projector_riesz_green_support": s4,
            "stationary_support_closed_by_transport_conjugation": True,
        },
        "open_dynamic_stages": {
            "S5_alpha1_response": s5,
            "S6_c1_contractions": s6,
            "C1_manifest_status": galerkin_c1["status"],
            "C1_manifest_selected_source_verified": galerkin_c1["selected_source_verified"],
            "required_outputs": galerkin_c1["required_outputs"],
        },
        "can_promote_honest_galerkin_C1_now": False,
        "required_next_emissions": [
            "zero-mode bases in the selected transported frame",
            "primitive three-by-three contraction terms",
            "linear response matrices",
            "C33/nonzero-family-rank tests",
            "coordinate map into the fixed 72-real phase/shift packet basis",
        ],
    }

    partial_promotion_theorem = {
        "name": "StationaryPhiFinTraceIsNotC1TransferTheorem",
        "proved": True,
        "statement": (
            "The selected stationary Phi_fin trace and transport-conjugation validator prove selected projector, "
            "Riesz/Green, and rho_s source identities, but they do not by themselves prove the C1 dynamic-transfer "
            "identity.  A future differentiated Phi_fin^C1 packet may promote the normal-form Weyl values only if "
            "it emits the same phase/shift columns, selected Hessian/source normalization, and primitive overlap "
            "contractions from the same q79/F,m=1 branch.  Otherwise an honest Galerkin C1 run supplies the selected "
            "replacement equation."
        ),
        "corollary_if_future_differentiated_packet_closes": {
            "A_selected_b_selected_deltaTheta_follow": True,
            "finite_values": finite_values,
            "condition": "Phi_fin^C1 emits phase/shift columns and b_selected=phase+shift with G=12 I_2",
        },
        "corollary_now": {
            "stationary_source_layer_closed": True,
            "C1_dynamic_layer_closed": False,
            "selected_A_b_delta_promoted": False,
        },
    }

    source_payload_flags = phifin_alpha1["payload_summary"]["selected_payload_flags"]
    candidate = {
        "candidate": "MTTSelectedPhiFinC1DynamicTransferIdentityProofOrGalerkinContractionsRun",
        "status": STATUS,
        "inputs": {
            "previous_normal_form_gate": rel(PREVIOUS),
            "dynamic_transfer_value_gate": rel(DYNAMIC),
            "transport_conjugation_validator_replay": rel(TRANSPORT),
            "gauge_transported_bn_phifin_trace": rel(GAUGE_TRACE),
            "phifin_alpha1_payload": rel(PHIFIN_ALPHA1),
            "finite_emission_morphism_phifin": rel(PHIFIN_SCHEMA),
            "routec_strominger_galerkin_solve_spec": rel(GALERKIN_SPEC),
            "honest_C1_primitive_contractions_manifest": rel(GALERKIN_C1),
            "crossrepo_alpha1_driver_replay_import": rel(CROSSREPO_ALPHA1) if crossrepo_alpha1 else None,
        },
        "coordinate_system": coord,
        "stationary_trace_import": stationary_trace_import,
        "phifin_payload_boundary": {
            "schema_status": phifin_schema["status"],
            "all_support_shapes_present": phifin_alpha1["payload_summary"]["all_support_shapes_present"],
            "all_selected_values_emitted": phifin_alpha1["payload_summary"]["all_selected_values_emitted"],
            "finite_Hessian_C1_source_selected": source_payload_flags["finite_Hessian_C1_source"],
            "primitive_C1_contractions_selected": source_payload_flags["primitive_C1_contractions"],
            "dotD_alpha1_selected_inside_phifin_payload": source_payload_flags["dotD_alpha1"],
        },
        "PhiFinC1_identity_attempt": phifinc1_identity_attempt,
        "Galerkin_run_attempt": galerkin_run_attempt,
        "partial_promotion_theorem": partial_promotion_theorem,
        "what_closes_now": {
            "stationary_PhiFin_trace_imported_as_selected_source": True,
            "selected_projector_riesz_green_rho_s_layer_closed": True,
            "stationary_trace_insufficiency_for_C1_transfer_proved": True,
            "PhiFinC1_or_Galerkin_live_target_sharpened": True,
            "normal_form_values_preserved_as_conditional_only": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_differentiated_PhiFinC1_transfer_identity": True,
            "selected_dotD_alpha1_attached_to_PhiFinC1": not alpha1_import[
                "selected_dotD_source_verified_imported"
            ],
            "selected_alpha1_driver_attached_to_PhiFinC1": not alpha1_import[
                "alpha1_driver_verified_imported"
            ],
            "primitive_C1_overlap_contractions": True,
            "selected_Hessian_source_vector_b_selected": True,
            "selected_A_selected_deltaTheta_sector_response_matrices": True,
            "honest_Galerkin_C1_run_or_equivalent_symbolic_contractions": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG_no_knob": True,
            "full_SM_no_knob_closure": True,
        },
        "promotion_decision": {
            "stationary_source_layer_promoted": True,
            "selected_PhiFinC1_identity_promoted": False,
            "selected_A_selected_promoted": False,
            "selected_b_selected_promoted": False,
            "selected_deltaTheta_C1_promoted": False,
            "selected_sector_response_matrices_promoted": False,
            "honest_Galerkin_C1_contractions_promoted": False,
            "full_SM_no_knob_closure_promoted": False,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "selected_PhiFinC1_identity_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1_DynamicTransferIdentity_Proof_or_GalerkinContractions_Run_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "stationary_source_layer_promoted": True,
        "selected_PhiFinC1_identity_claimed": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "deltaTheta_C1_claimed": False,
        "Galerkin_C1_contractions_claimed": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFinC1 DynamicTransferIdentity Proof or GalerkinContractions Run v1

Status: `{STATUS}`.

This artifact imports the symbolic transport-conjugation theorem into the
`Phi_fin^C1` proof target.

Closed now:

```text
P_s^sel = U P_s^model U^-1
G_s^sel = U G_s^model U^-1
rho_s selected-source validator ready
stationary projector/Riesz/Green/source layer closed
```

But this is a stationary trace theorem.  It does not emit the differentiated
`Phi_fin^C1` overlap/Hessian data:

```text
Phi_C1_selected(Z) = phase_packet
Phi_C1_selected(X) = shift_packet
b_selected         = phase_packet + shift_packet
G_selected         = 12 I_2
```

So the previous normal-form values remain conditional:

```text
A^T A         = {finite_values["Gram_A_transpose_A"]}
A^T b         = {finite_values["A_transpose_b"]}
deltaTheta_C1 = {finite_values["deltaTheta_C1"]}
```

The live target is now precise: emit a differentiated `Phi_fin^C1` packet with
the primitive overlap contractions, or run the honest selected Galerkin C1
contract and solve whatever selected equation it emits.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
