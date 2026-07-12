from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    candidate = load_json("candidate_data/selected_internalrtheta_vsd01_backimport_or_valuesourcefrontier.candidate.json")
    cert = load_json("certificates/selected_internalrtheta_vsd01_backimport_or_valuesourcefrontier_certificate.json")
    direct_rtheta = load_json("certificates/selected_internalrthetascalarrowemission_or_universalanchorselection_certificate.json")
    phifin_sector = load_json("certificates/selected_phifinminimizertracesectorpayload_or_internalscalarrows_certificate.json")
    static_matter = load_json("certificates/selected_u10ubar5_1m_sourcepromotion_samebranch_emission_certificate.json")
    dynamic_cutset = load_json("certificates/selected_dynamic_overlapkernel_or_c1primitive_source_emission_certificate.json")
    first_row = load_json("certificates/selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource_certificate.json")
    all_rows = load_json("certificates/selected_firstrowprovenancepromotion_or_allrowsweylexecution_certificate.json")
    vsd01 = load_json("certificates/selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource_certificate.json")
    post_source = load_json("certificates/selected_postsourcevaluepromotionrows_or_trueprecisionexit_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["closure_claimed"] is False, "must not claim no-knob closure")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed data used as selector")

    require(direct_rtheta["direct_emission_attempt_executed"] is True, "direct Rtheta attempt not executed")
    require(direct_rtheta["accepted_internal_scalar_row_count"] == 0, "direct Rtheta unexpectedly accepted rows")
    require(direct_rtheta["fullS2_payload_ready"] is False, "old fullS2 blocker unexpectedly ready")
    require(phifin_sector["transported_sector_payload_imported"] is True, "transported PhiFin sector payload not imported")
    require(phifin_sector["accepted_internal_scalar_row_count"] == 0, "PhiFin sector unexpectedly accepted scalar rows")
    require(static_matter["static_U10_Ubar5_1M_source_closed"] is True, "static U10/Ubar5/1M source not closed")
    require(static_matter["static_matter_slot_readout_closed"] is True, "static matter-slot readout not closed")
    require(static_matter["dynamic_overlap_kernel_closed"] is False, "static matter packet unexpectedly closes dynamic kernel")
    require(dynamic_cutset["what_closes"]["dynamic_frontier_reduced_after_static_sector_closure"] is True, "dynamic cutset not reduced")
    require(dynamic_cutset["dynamic_kernel_emitted"] is False, "dynamic cutset unexpectedly emits kernel")

    require(first_row["first_row_exactness_certificate_emitted"] is True, "first row exactness not emitted")
    require(first_row["first_row_value_exact"] == "4/3", "first row exact value changed")
    require(all_rows["all_72_row_values_exact"] is True, "all 72 row values not exact")
    require(all_rows["all_72_exactness_certificates"] is True, "all 72 exactness certs missing")
    require(all_rows["formal_110_row_replay_closed"] if "formal_110_row_replay_closed" in all_rows else True, "unused")

    vsd_closes = vsd01["what_closes"]
    require(vsd_closes["A_selected_promoted"] is True, "VSD01 did not promote A_selected")
    require(vsd_closes["b_selected_promoted"] is True, "VSD01 did not promote b_selected")
    require(vsd_closes["deltaTheta_C1_promoted"] is True, "VSD01 did not promote deltaTheta_C1")
    require(vsd_closes["all_72_primitive_rows_exact"] is True, "VSD01 lost 72 rows")
    require(vsd_closes["formal_110_row_assembly"] is True, "VSD01 lost formal 110 assembly")
    require(vsd_closes["physical_PhiFinC1_action_source"] is True, "VSD01 lost physical PhiFinC1 action source")
    require(vsd_closes["primitive_C1_contractions_first_response_layer"] is True, "VSD01 lost primitive C1 first response")
    require(vsd_closes["same_source_dynamic_matter_overlap_operator_packet"] is True, "VSD01 lost dynamic overlap packet")
    require(vsd_closes["selected_dynamic_overlap_tensor_T_selected"] is True, "VSD01 lost selected dynamic overlap tensor")
    require(vsd_closes["source_owner_verified"] is True, "VSD01 lost source owner")

    consumed = candidate["older_blockers_consumed"]
    require(consumed["all_72_row_values_exact"] is True, "candidate did not import 72 exact rows")
    require(consumed["formal_110_row_replay_closed"] is True, "candidate did not import formal 110 replay")
    require(consumed["physical_PhiFinC1_action_source_closed_at_VSD01_source_assembly_scope"] is True, "candidate did not import VSD01 action source")
    require(consumed["A_selected_promoted"] is True, "candidate did not import A")
    require(consumed["b_selected_promoted"] is True, "candidate did not import b")
    require(consumed["deltaTheta_C1_promoted"] is True, "candidate did not import deltaTheta")

    frontier = candidate["current_value_frontier_after_backimport"]
    require(post_source["closed_value_obligation_rows_at_admitted_external_tier"] == 4, "post-source external count changed")
    require(post_source["closed_value_obligation_rows_at_internal_no_knob_tier"] == 0, "post-source internal count changed")
    require(post_source["readiness_fraction"] == "8/9", "post-source readiness changed")
    require(frontier["internal_Rtheta_scalar_rows_accepted"] == 0, "candidate overclaims internal Rtheta rows")
    require(frontier["lambda_H_row_emitted"] is False, "candidate overclaims lambda_H row")
    require(frontier["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision")
    require(frontier["post_source_external_value_lane"] == "4/5 admitted replay", "candidate external lane mismatch")
    require(frontier["post_source_internal_no_knob_value_lane"] == "0/5 internal no-knob", "candidate internal lane mismatch")
    require(frontier["post_source_value_readiness"] == "8/9", "candidate readiness mismatch")

    require(cert["all_72_row_values_exact"] is True, "certificate lost 72 exact rows")
    require(cert["physical_PhiFinC1_action_source_closed_at_VSD01_source_assembly_scope"] is True, "certificate lost VSD01 action source")
    require(cert["internal_Rtheta_scalar_rows_accepted"] == 0, "certificate overclaims internal scalar rows")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")
    require(cert["next_required_artifact"] == candidate["next_attack"]["artifact"], "next artifact mismatch")

    print(
        json.dumps(
            {
                "candidate": "candidate_data/selected_internalrtheta_vsd01_backimport_or_valuesourcefrontier.candidate.json",
                "status": candidate["status"],
                "dynamic_source_blocker": "consumed at VSD01 source-assembly scope",
                "all_72_rows_exact": True,
                "formal_110_assembly": True,
                "A_b_deltaTheta": "promoted",
                "internal_Rtheta_scalar_rows": 0,
                "post_source_value_lane": "4/5 admitted external, 0/5 internal, readiness 8/9",
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected internal Rtheta VSD01 backimport audit passed")


if __name__ == "__main__":
    main()
