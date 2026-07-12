from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_nonidentity_rhoe_bn_interface_certificate.json"
STATUS = "POST_ALPHA_NONIDENTITY_RHOE_BN_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_FillAttempt_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["selected_values_emitted"] is False, "must not emit selected values")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    checks = packet["interface_checks"]
    require(checks["previous_gate_reduced_to_this_payload"] is True, "previous gate not linked")
    require(checks["all_template_selected_values_open"] is True, "template selected values should be open")
    require(checks["identity_rhoE_explicitly_forbidden"] is True, "identity rhoE must be forbidden")
    require(checks["diagnostic_splitter_explicitly_forbidden"] is True, "diagnostic splitter must be forbidden")

    template = packet["template"]
    require(template["schema"] == "SelectedU1YRouteCNonIdentityRhoEQuotientValidBN.v1", "wrong template schema")
    for section, payload in template.items():
        if isinstance(payload, dict):
            require(all(value is None for value in payload.values()), f"template section {section} should remain open")

    support = packet["support_operator_tables"]
    require(support["closure_scope"] == "conditional_operator_table_construction_and_selected_table_no_go_only", "wrong support-table closure scope")
    require(support["routec_conditional_A_shape"] == [72, 2], "wrong conditional A shape")
    require(support["routec_conditional_rank"] == 2, "wrong conditional A rank")
    require(support["projective_nontrivial_central_twist_count"] == 274, "wrong twist count")
    require(all(value is False for value in support["selected_tables"].values()), "selected support tables should all be false")

    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "nonidentity rho_E" in note, "note missing essentials")

    print("AUDIT_PASS: nonidentity rhoE/quotient-valid BN interface built; selected values remain open")


if __name__ == "__main__":
    main()
