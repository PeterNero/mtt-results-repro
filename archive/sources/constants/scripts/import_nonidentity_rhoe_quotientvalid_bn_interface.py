"""Import the non-identity rho_E / quotient-valid B_N interface."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")

PREVIOUS = CERTS / "selected_correction_fullresponse_frontier_import_certificate.json"
LOCAL_PREFIX = CERTS / "routec_rhoe_bn_operator_prefix_import_certificate.json"
QA_PACKET = QA / "candidate_data" / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface.candidate.json"
QA_CERT = QA / "certificates" / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn_interface_certificate.json"
QA_TEMPLATE = QA / "certificates" / "selected_u1y_routec_nonidentity_rhoe_quotientvalid_bn.template.json"

OUTPUT_PACKET = DATA / "nonidentity_rhoe_quotientvalid_bn_interface_import.candidate.json"
OUTPUT_CERT = CERTS / "nonidentity_rhoe_quotientvalid_bn_interface_import_certificate.json"
OUTPUT_NOTE = CORPUS / "NonIdentity_RhoE_QuotientValid_BN_Interface_Import_v1.md"

STATUS = "NONIDENTITY_RHOE_QUOTIENTVALID_BN_INTERFACE_IMPORTED_FILL_OPEN"
UPSTREAM_STATUS = "U1Y_ROUTEC_NONIDENTITY_RHOE_QUOTIENTVALID_BN_INTERFACE_BUILT_VALUES_OPEN"
OLD_NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_FillAttempt_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    prefix = load(LOCAL_PREFIX)
    upstream = load(QA_PACKET)
    upstream_cert = load(QA_CERT)
    template = load(QA_TEMPLATE)
    prefix_closed = prefix["closed_now"]
    prefix_summary = prefix["finite_prefix_summary"]
    checks = {
        "G0_previous_frontier_matches": previous["frontier_update"]["current_next"] == OLD_NEXT,
        "G1_upstream_interface_status_matches": upstream["status"] == UPSTREAM_STATUS
        and upstream_cert["status"] == UPSTREAM_STATUS,
        "G2_template_values_open": upstream["interface_checks"]["all_template_selected_values_open"] is True
        and template["source_evidence"]["selected_by_mtt"] is None
        and template["rho_E"]["nonidentity"] is None
        and template["B_N"]["quotient_valid"] is None,
        "G3_forbidden_shortcuts_named": upstream["interface_checks"]["identity_rhoE_explicitly_forbidden"] is True
        and upstream["interface_checks"]["diagnostic_splitter_explicitly_forbidden"] is True
        and "using a formal Galerkin lift as proof" in upstream["what_this_interface_prevents"],
        "G4_required_payload_keys_match_frontier": upstream["interface_checks"]["required_payload_keys_imported"]
        == [
            "b_selected_or_homogeneous_zero_theorem",
            "nonidentity_rho_E",
            "primitive_C1_contractions_or_full_response_matrices",
            "quotient_valid_B_N",
            "selected_D_E_Riesz_Green_dotD",
            "selected_deltaTheta_C1_solution",
            "selected_source_certificate",
        ],
        "G5_local_support_scaffold_present": prefix_closed["nonidentity_projective_rhoE_candidate_built"] is True
        and prefix_closed["smooth_BN_27_mode_scaffold_built"] is True
        and prefix_closed["D_E_matrix_on_27_mode_BN_emitted"] is True
        and prefix_closed["sector_projectors_and_dotD_same_basis_emitted"] is True,
        "G6_local_scaffold_not_selected_fill": prefix_summary["rho_E"]["selected_by_mtt"] is False
        and prefix["not_closed"]["R1_selected_source_certificate"] is True
        and prefix["not_closed"]["R2_source_promotion_for_rhoE"] is True
        and prefix["not_closed"]["selected_dotD_source_verified"] is True,
        "G7_canonical_C1_zero_no_closure": prefix_closed["canonical_C1_zero_response_no_go_proved"] is True
        and prefix_summary["C1"]["all_c1_matrices_zero_for_canonical_tensor"] is True
        and prefix["guardrails"]["claims_nonzero_C1_response"] is False,
        "G8_no_downstream_closure": upstream_cert["closure_claimed"] is False
        and upstream_cert["what_remains_open"]["A_selected"] is True
        and upstream_cert["what_remains_open"]["Yukawa_CKM_PMNS_CP_or_full_SM_closure"] is True
        and prefix["guardrails"]["claims_full_SM_closure"] is False,
    }
    return {
        "packet": "NonIdentity_RhoE_QuotientValid_BN_Interface_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_frontier": str(PREVIOUS.relative_to(ROOT)),
            "local_routec_prefix": str(LOCAL_PREFIX.relative_to(ROOT)),
            "qa_interface_packet": str(QA_PACKET),
            "qa_interface_certificate": str(QA_CERT),
            "qa_template": str(QA_TEMPLATE),
        },
        "theorem": {
            "name": "NonIdentityRhoEQuotientValidBNInterfaceImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The non-identity rho_E / quotient-valid B_N construction is now "
                "an executable selected-value interface.  Existing Route-C support "
                "already supplies a non-identity projective rho_E candidate, a 27-mode "
                "smooth B_N scaffold, model D_E/Riesz/Green, same-basis dotD/projectors, "
                "and a C1 contraction engine.  Those are support values only: the "
                "upstream template leaves selected_by_mtt, same_branch_q79_F_m1, "
                "rho_E, quotient-valid B_N, honest replay, deltaTheta/C1, A_selected, "
                "and b_selected open, and the canonical translation-invariant C1 tensor "
                "still gives zero one-response matrices."
            ),
        },
        "checks": checks,
        "upstream_interface": upstream,
        "upstream_certificate": upstream_cert,
        "template": template,
        "local_support_scaffold": {
            "closed_now": prefix_closed,
            "finite_prefix_summary": prefix_summary,
            "not_closed": prefix["not_closed"],
            "next_closing_object": prefix["next_closing_object"],
        },
        "frontier_update": {
            "old_next": OLD_NEXT,
            "current_next": NEXT,
            "why": (
                "The strict interface is now imported.  The next task is to fill it "
                "with theorem-derived selected values, not diagnostic or model-active "
                "scaffold values."
            ),
        },
        "guardrails": {
            "does_not_fill_selected_rho_E": True,
            "does_not_fill_quotient_valid_B_N": True,
            "does_not_promote_local_prefix_scaffold": True,
            "does_not_promote_diagnostic_splitter": True,
            "does_not_promote_identity_rhoE_or_formal_lift": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_claim_Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
        },
        "verdict": {
            "what_closes_now": (
                "The exact fill contract is imported and aligned with the existing "
                "finite Route-C scaffold.  We know which boxes have support values "
                "and which boxes still require selected-source proof."
            ),
            "what_remains": (
                "Fill selected_by_mtt, same_branch_q79_F_m1, nonidentity rho_E, "
                "quotient-valid B_N, honest D_E/Riesz/Green/dotD replay, selected "
                "deltaTheta/C1, and b_selected or a homogeneous-zero theorem."
            ),
            "next_required_artifact": NEXT,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "NonIdentityRhoEQuotientValidBNInterfaceImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "checks": packet["checks"],
        "frontier_update": packet["frontier_update"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    support = packet["local_support_scaffold"]["finite_prefix_summary"]
    return f"""# NonIdentity RhoE QuotientValid BN Interface Import v1

## Result

Status: `{cert["status"]}`

The strict selected-value interface is imported.  Existing Route-C machinery
already provides scaffold values:

```json
{json.dumps(support, indent=2, sort_keys=True)}
```

## Interpretation

The scaffold is valuable but not promoted.  Its `rho_E` candidate is explicitly
not selected by MTT, and the canonical C1 primitive gives zero one-response
matrices.  The next fill attempt must therefore supply theorem-derived selected
source evidence, selected non-identity `rho_E`, quotient-valid `B_N`, honest
operator replay, and selected `deltaTheta/C1` emission.

```json
{json.dumps(packet["frontier_update"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
