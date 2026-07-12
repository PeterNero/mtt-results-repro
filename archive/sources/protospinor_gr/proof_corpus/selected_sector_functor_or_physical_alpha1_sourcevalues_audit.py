from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_sector_functor_or_physical_alpha1_sourcevalues_certificate.json"
STATUS = "ORDINARY_END0_TO_PROJECTIVE_BN_SECTOR_FUNCTOR_NO_GO_GERBE_LIFT_OR_ALPHA1_SOURCE_REQUIRED"
NEXT = "MTT_Selected_GerbeTwisted_End0_SectorFunctor_or_PhysicalAlpha1_SourceTheorem_v1"


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

    source = packet["ordinary_End0_source"]
    require(source["available"] is True, "ordinary End0 source should be available")
    require(source["basis"] == ["T1", "T2", "T3"], "wrong End0 basis")
    require(source["continuous_parameters_added_by_adjoint_transfer"] == 0, "transfer added a knob")

    target = packet["projective_BN_target"]
    require(target["cocycle_nontrivial"] is True, "projective cocycle should be nontrivial")
    require(target["bundle_equivariance"]["ordinary_bundle_equivariance"] is False, "BN must not be ordinary")
    require(target["bundle_equivariance"]["projective_equivariance_up_to_central_phase"] is True, "BN projective flag missing")
    require(target["projective_phase_distance_from_ordinary_one"] > 1.0, "projective phase too close to 1")
    require(target["projective_commutator_residual"] < 1.0e-12, "projective residual too large")

    obstruction = packet["obstruction"]
    require(obstruction["closed"] is True, "obstruction should close")
    require(obstruction["ordinary_functor_requires_commutator_phase"] == [1.0, 0.0], "ordinary phase wrong")
    require("2-cocycle" in obstruction["formal_reason"], "cocycle reason missing")

    attempt = packet["attempted_positive_functor"]
    require(attempt["ordinary_End0_to_current_BN_sector_functor_proved"] is False, "positive ordinary functor must not be claimed")
    require(attempt["BN_rejected_as_selected_End0_table"] is True, "BN rejection missing")
    require(attempt["diagnostic_sector_projectors_exist"] is True, "diagnostic projectors should exist")
    require(attempt["selected_dotD_source_promotes"] is False, "selected dotD source must not promote")
    require(attempt["alpha1_driver_promotes"] is False, "alpha1 must not promote")

    repair = packet["repair_paths"]
    require(repair["path_A_gerbe_twisted_sector_functor"]["required"] is True, "gerbe repair missing")
    require(repair["path_B_physical_alpha1_source_values"]["required"] is True, "alpha1 repair missing")

    require(packet["guardrails"]["does_not_identify_projective_BN_with_ordinary_End0"], "BN guardrail missing")
    require(packet["guardrails"]["does_not_promote_diagnostic_sector_projectors"], "diagnostic projector guardrail missing")
    require(STATUS in note and NEXT in note and "cocycle" in note and "mismatch" in note, "note missing essentials")

    print("AUDIT_PASS: ordinary End0-to-current-BN sector functor no-go proved; gerbe lift or alpha1 source required")


if __name__ == "__main__":
    main()
