from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_rank2_to_rank3_sector_transfer_or_physical_dotd_alpha1_certificate.json"
STATUS = "ABSTRACT_RANK2_TO_RANK3_ADJOINT_TRANSFER_CLOSED_SECTOR_ALPHA1_VALUES_OPEN"
NEXT = "MTT_Selected_SectorFunctor_or_PhysicalAlpha1_SourceValues_From_Selected_HYM_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    abstract = packet["closed_abstract_transfer"]
    require(abstract["closed"] is True, "abstract transfer should close")
    require(abstract["carrier_rank"] == 3, "wrong carrier rank")
    require(abstract["continuous_parameters_added"] == 0, "transfer must add no knob")
    require(abstract["curvature_rule"] == "F_ad(A)=ad(F_A)", "wrong curvature rule")
    require("not finite sector values" in abstract["meaning"], "finite-value boundary missing")

    green = packet["closed_End0_green_payload_available_for_transfer"]
    require(green["closed"] is True, "End0 Green payload should be available")
    require(green["T3_green_closed"] is True, "T3 Green missing")
    require(green["T1T2_green_closed"] is True, "T1/T2 Green missing")
    require(green["T1T2_green_residual_l2"] < 1.0e-12, "T1/T2 residual too large")
    require(green["basis"] == ["T1", "T2", "T3"], "wrong End0 basis")

    sector = packet["finite_sector_transfer_status"]
    require(sector["closed"] is False, "finite sector transfer must remain open")
    require(sector["values_emitted"] is False, "finite sector values must not be emitted")
    require(sector["BN_rejected_as_selected_End0_table"] is True, "BN rejection missing")
    require("projective" in sector["blocking_reason"], "sector blocker should mention projective scaffold")

    alpha1 = packet["physical_dotD_alpha1_status"]
    require(alpha1["closed"] is False, "physical alpha1 must remain open")
    require(alpha1["values_emitted"] is False, "alpha1 values must not be emitted")
    require(alpha1["scaffold_shape_available"] is True, "diagnostic alpha1 scaffold should be detected")
    require(alpha1["alpha1_driver_verified"] is False, "alpha1 driver must not be verified")
    require(alpha1["selected_source_verified"] is False, "selected source must not be verified")

    matter = packet["matter_interface_impact"]
    require(matter["selected_DE_Riesz_Green_dotD_shape_now_available_on_End0"] is True, "End0 shape impact missing")
    require(matter["selected_DE_Riesz_Green_dotD_filled_in_matter_template"] is False, "matter template must not be filled")
    require(matter["selected_sector_projectors_and_zero_modes_filled"] is False, "sector slots must not be filled")

    require(packet["guardrails"]["does_not_promote_abstract_transfer_as_finite_values"], "abstract transfer guardrail missing")
    require(packet["guardrails"]["does_not_promote_diagnostic_dotD_alpha1_shapes"], "alpha1 diagnostic guardrail missing")
    require(packet["guardrails"]["does_not_fill_matter_template_without_sector_values"], "matter template guardrail missing")
    require(STATUS in note and NEXT in note and "continuous parameters added = 0" in note, "note missing essentials")

    print("AUDIT_PASS: abstract rank2-to-rank3 adjoint transfer closed; sector and alpha1 values remain open")


if __name__ == "__main__":
    main()
