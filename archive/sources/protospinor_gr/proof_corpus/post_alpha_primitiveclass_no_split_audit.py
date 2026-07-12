from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_primitiveclass_no_split_certificate.json"
STATUS = "POST_ALPHA_PRIMITIVECLASS_NO_FLAVOR_SPLIT_HIGHERORDER_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["primitive_class_flavor_split_possible"] is False, "primitive class should not split flavor")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    tests = packet["primitive_layer_tests"]
    require(tests["all_fixed_candidates_rank3_each_sector"] is True, "fixed candidates should be rank 3")
    require(tests["all_yy_star_scalar_identity"] is True, "YYstar should be scalar identity")
    require(tests["max_traceless_norm_sq"] == 0.0, "traceless norm should vanish")
    require(tests["max_commutator_norm_sq"] == 0.0, "commutator norm should vanish")
    require(tests["mass_splitting_test_passes"] is False, "mass splitting should fail")
    require(tests["mixing_commutator_test_passes"] is False, "mixing should fail")
    require(tests["cp_odd_test_passes"] is False, "CP test should fail")
    require(all(sector["scalar_identity"] is True for sector in tests["yy_star_scalar_tests"].values()), "each sector should be scalar identity")
    require(all(sector["traceless_norm_sq"] == 0.0 for sector in tests["yy_star_scalar_tests"].values()), "each sector traceless norm should vanish")

    contract = packet["higher_order_contract"]
    require(contract["criterion_imported"] is True, "higher-order criterion missing")
    require(contract["full_response_acceptance_tests_locked"] is True, "acceptance tests not locked")
    require(contract["diagnostic_splitter_exists_without_observed_targets"] is True, "diagnostic splitter fact missing")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "Y_s Y_s* = c I" in note, "note missing essentials")

    print("AUDIT_PASS: primitive quotient has no flavor split; higher-order source emission remains open")


if __name__ == "__main__":
    main()
