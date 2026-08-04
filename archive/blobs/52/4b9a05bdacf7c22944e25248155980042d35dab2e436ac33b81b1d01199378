from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_alpha1_tangent_or_retarded_overlap_kernel_construct_certificate.json"
STATUS = "SELECTED_ALPHA1_TANGENT_KERNEL_CONSTRUCTED_SELECTION_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(cert["kernel_constructed"] is True, "kernel should be constructed")
    require(cert["alpha1_driver_verified"] is False, "alpha1 driver must remain open")
    require(cert["selected_physical_alpha1_closed"] is False, "physical alpha1 must remain open")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all checks should pass")

    kernel = packet["constructed_tangent_kernel"]
    require(kernel["tangent"]["symbol"] == "h_ext", "wrong tangent")
    require(kernel["tangent"]["zero_mean"] is True, "h_ext should be zero mean")
    require(kernel["tangent"]["h_ext_residual_l2"] < 1.0e-12, "h_ext residual too large")
    require(kernel["tangent"]["selected_now"] is False, "tangent must not be selected yet")
    require(
        kernel["operator_formula"]["identity"] == "D_sel(delta psi)+dotD_h psi_sel=0",
        "wrong transport identity",
    )
    require(kernel["normalization_functional"]["N_alpha1_h_ext"] == 1.0, "normalization not unit")
    require(kernel["normalization_functional"]["lambda_alpha1_candidate"] == 1.0, "lambda not pinned")
    require(kernel["normalization_functional"]["selected_now"] is False, "normalization must remain unselected")

    replay = packet["honest_replay_status"]
    require(replay["full_flag_validation_exit_code"] == 0, "full-flag diagnostic should pass")
    require(replay["source_only_probe_exit_code"] == 1, "source-only probe should fail")
    require(replay["source_only_fails_only_by_alpha1_driver"] is True, "failure should be alpha1 only")
    require(replay["honest_replay_without_lifted_flags_closed"] is False, "honest replay must remain open")

    require(all(packet["what_closes_now"].values()), "closure construct flags should be true")
    require(all(packet["what_remains_open"].values()), "open blockers should remain true")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "N_alpha1(h_ext) = 1" in note, "note missing essentials")

    print("AUDIT_PASS: alpha1 tangent kernel constructed; selected normalization remains open")


if __name__ == "__main__":
    main()
