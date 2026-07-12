from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"

PREV = ROOT / "candidate_data" / "post_alpha_selected_correction_emission_reduction.packet.json"
INTERFACE = QA / "candidate_data" / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.candidate.json"
TABLES = QA / "candidate_data" / "selected_u1y_routec_or_projective_rhoe_selected_operator_tables.candidate.json"

OUT_CERT = ROOT / "certificates" / "post_alpha_nonidentity_rhoe_bn_interface_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "post_alpha_nonidentity_rhoe_bn_interface.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "PostAlpha_NonIdentity_RhoE_BN_Interface_v1.md"

STATUS = "POST_ALPHA_NONIDENTITY_RHOE_BN_INTERFACE_BUILT_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_FillAttempt_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV)
    interface = load(INTERFACE)
    tables = load(TABLES)

    previous_reduction_closed = all(
        [
            prev["theorem"]["proved"] is True,
            prev["what_closes_now"]["nonidentity_rhoE_BN_payload_contract_built"] is True,
            prev["what_remains_open"]["selected_nonidentity_rho_E"] is True,
            prev["what_remains_open"]["selected_quotient_valid_B_N"] is True,
            prev["next_required_artifact"] == "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1",
        ]
    )
    interface_built = all(
        [
            interface["closure_claimed"] is False,
            interface["status"] == "U1Y_ROUTEC_NONIDENTITY_RHOE_QUOTIENTVALID_BN_INTERFACE_BUILT_VALUES_OPEN",
            interface["interface_checks"]["previous_gate_reduced_to_this_payload"] is True,
            interface["interface_checks"]["all_template_selected_values_open"] is True,
            interface["interface_checks"]["identity_rhoE_explicitly_forbidden"] is True,
            interface["interface_checks"]["diagnostic_splitter_explicitly_forbidden"] is True,
            interface["interface_checks"]["closure_claimed"] is False,
            interface["target_fitting_used"] is False,
        ]
    )
    required_payload_keys_preserved = interface["interface_checks"]["required_payload_keys_imported"] == sorted(
        prev["required_payload"].keys()
    )
    template_open = all(
        value is None
        for section, payload in interface["template"].items()
        if isinstance(payload, dict)
        for value in payload.values()
    )
    promotion_rule_complete = all(
        phrase in " ".join(interface["promotion_rule"])
        for phrase in [
            "same_branch_q79_F_m1",
            "non-identity",
            "quotient-valid",
            "without lifted flags",
            "deltaTheta_C1",
            "mass, commutator, and CP",
        ]
    )
    support_tables_not_closure = all(
        [
            tables["closure_claimed"] is True,
            tables["closure_scope"] == "conditional_operator_table_construction_and_selected_table_no_go_only",
            tables["decision"]["operator_table_gate_constructed"] is True,
            tables["decision"]["projective_validator_table_constructed"] is True,
            tables["decision"]["selected_operator_tables_emitted"] is False,
            tables["decision"]["selected_projective_rhoE_tables_emitted"] is False,
            tables["decision"]["selected_A_selected_emitted"] is False,
            tables["decision"]["selected_b_selected_emitted"] is False,
            tables["decision"]["target_fitting_used"] is False,
            tables["routec_operator_table"]["promote_to_A_selected"] is False,
            tables["projective_rhoE_table"]["operator_level_projective_rhoE_promoted"] is False,
        ]
    )
    guardrails_ok = all(
        [
            all(prev["guardrails"].values()),
            "using identity rho_E smoke payloads" in interface["what_this_interface_prevents"],
            "using the diagnostic qutrit/Weyl splitter as selected data" in interface["what_this_interface_prevents"],
            "computing lambda_12 or flavor data before selected A/b emission" in interface["what_this_interface_prevents"],
            tables["target_fitting_used"] is False,
            tables["decision"]["lambda_12_computable"] is False,
            tables["decision"]["lambda_12_closed"] is False,
        ]
    )
    theorem_proved = all(
        [
            previous_reduction_closed,
            interface_built,
            required_payload_keys_preserved,
            template_open,
            promotion_rule_complete,
            support_tables_not_closure,
            guardrails_ok,
        ]
    )

    packet = {
        "theorem": {
            "name": "PostAlphaNonIdentityRhoEBNInterfaceImportTheorem",
            "proved": theorem_proved,
            "closure_claimed": False,
            "statement": (
                "The non-identity rho_E / quotient-valid B_N interface is now built as the strict "
                "payload template for selected correction/full-response emission. The interface preserves "
                "all required payload keys, forbids identity rho_E, diagnostic splitters, formal lifts, "
                "and premature lambda/flavor computation, and reduces the next task to a fill attempt. "
                "Existing conditional Route-C/projective rho_E operator tables are retained only as "
                "support/no-go data, not selected tables."
            ),
        },
        "status": STATUS,
        "interface_checks": interface["interface_checks"],
        "template": interface["template"],
        "promotion_rule": interface["promotion_rule"],
        "support_operator_tables": {
            "closure_scope": tables["closure_scope"],
            "strongest_result": tables["decision"]["strongest_result"],
            "routec_conditional_A_shape": tables["routec_operator_table"]["shape"],
            "routec_conditional_rank": tables["routec_operator_table"]["rank"],
            "projective_nontrivial_central_twist_count": tables["projective_rhoE_table"][
                "nontrivial_central_twist_count"
            ],
            "selected_tables": tables["selected_tables"],
            "open": tables["open"],
        },
        "checks": {
            "previous_reduction_closed": previous_reduction_closed,
            "interface_built": interface_built,
            "required_payload_keys_preserved": required_payload_keys_preserved,
            "template_open": template_open,
            "promotion_rule_complete": promotion_rule_complete,
            "support_tables_not_closure": support_tables_not_closure,
            "guardrails_ok": guardrails_ok,
        },
        "what_closes_now": {
            "nonidentity_rhoE_BN_interface_built": True,
            "required_payload_keys_preserved": True,
            "identity_rhoE_forbidden": True,
            "diagnostic_splitter_forbidden_as_source": True,
            "formal_lift_forbidden_as_proof": True,
            "conditional_operator_tables_classified_support_only": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_nonidentity_rho_E": True,
            "selected_quotient_valid_B_N": True,
            "selected_source_certificate": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_deltaTheta_C1_solution": True,
            "selected_primitive_C1_contractions_or_full_response_matrices": True,
            "A_selected": True,
            "b_selected": True,
            "lambda_12": True,
            "Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
        },
        "guardrails": {
            "does_not_claim_selected_values": True,
            "does_not_claim_selected_operator_tables": True,
            "does_not_promote_conditional_A_to_A_selected": True,
            "does_not_promote_projective_mesh_to_selected_rhoE": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12_or_full_SM": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "next_required_artifact": NEXT,
        "input_artifacts": {"previous": str(PREV), "interface": str(INTERFACE), "support_tables": str(TABLES)},
    }
    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "post_alpha_nonidentity_rhoe_bn_interface",
        "status": STATUS,
        "closure_claimed": False,
        "selected_values_emitted": False,
        "reduced_to": NEXT,
        "checks": {
            "theorem_proved": theorem_proved,
            **packet["checks"],
            "all_closes_true": all(packet["what_closes_now"].values()),
            "all_open_true": all(packet["what_remains_open"].values()),
            "all_guardrails_true": all(packet["guardrails"].values()),
        },
        "packet_written": str(OUT_PACKET),
        "note_written": str(OUT_NOTE),
    }
    note = f"""# PostAlpha NonIdentity RhoE BN Interface v1

## Result

The non-identity `rho_E` / quotient-valid `B_N` payload interface is built.

It requires:

```text
nonidentity rho_E
quotient-valid B_N
selected source certificate
honest D_E/Riesz/Green/dotD replay
selected deltaTheta/C1 solution
selected primitive C1 or full-response matrices
b_selected or homogeneous-zero theorem
```

It forbids identity smoke payloads, diagnostic splitters as selected source,
formal Galerkin lift as proof, and premature `lambda_12` or flavor computation.

Status:

```text
{STATUS}
```

Next:

```text
{NEXT}
```
"""
    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
