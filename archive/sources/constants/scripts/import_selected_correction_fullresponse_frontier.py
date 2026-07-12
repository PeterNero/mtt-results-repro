"""Import the selected correction/full-response frontier reduction."""

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

PREVIOUS = CERTS / "primitive_c1_fiberclass_higherorder_frontier_import_certificate.json"
QA_PACKET = QA / "candidate_data" / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission.candidate.json"
QA_CERT = QA / "certificates" / "selected_u1y_routec_selectedcorrection_source_or_fullresponse_emission_certificate.json"

OUTPUT_PACKET = DATA / "selected_correction_fullresponse_frontier_import.candidate.json"
OUTPUT_CERT = CERTS / "selected_correction_fullresponse_frontier_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_Correction_FullResponse_Frontier_Import_v1.md"

STATUS = "SELECTED_CORRECTION_FULLRESPONSE_FRONTIER_REDUCED_RHOE_BN_DELTATHETA_OPEN"
UPSTREAM_STATUS = "U1Y_ROUTEC_SELECTED_CORRECTION_EMISSION_REDUCED_NONIDENTITY_RHOE_BN_OPEN"
OLD_NEXT = "Selected_U1Y_RouteC_SelectedCorrectionMatrixSource_or_FullResponseEmission_v1"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(QA_PACKET)
    upstream_cert = load(QA_CERT)
    reduction = upstream["reduction"]
    diag = upstream["diagnostic_representative_support_only"]
    payload = upstream["required_payload"]
    guards = upstream["guardrails"]
    open_items = upstream["what_remains_open"]

    checks = {
        "G0_previous_frontier_matches": previous["frontier_update"]["current_next"] == OLD_NEXT,
        "G1_upstream_status_matches": upstream["status"] == UPSTREAM_STATUS
        and upstream_cert["status"] == UPSTREAM_STATUS,
        "G2_upstream_theorem_proved_reduction_only": upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream_cert["closure_claimed"] is False,
        "G3_diagnostic_splitter_support_only": reduction["diagnostic_splitter_exists"] is True
        and reduction["diagnostic_splitter_not_promoted"] is True
        and upstream_cert["diagnostic_splitter_recorded_support_only"] is True
        and upstream["decision"]["diagnostic_splitter_promoted"] is False,
        "G4_diagnostic_tests_show_no_algebraic_splitter_obstruction": diag["candidate_count"] > 0
        and all(value > 0.0 for value in diag["mass_split_traceless_norm_sq"].values())
        and diag["ckm_commutator_norm_sq"] > 0.0
        and diag["pmns_commutator_norm_sq"] > 0.0
        and diag["cp_odd_trace_commutator_cubed_imag"] != 0.0,
        "G5_primitive_and_formal_routes_rejected": reduction["primitive_only_span_counterexample"] is True
        and reduction["strict_primitive_search_found_no_legal_emission"] is True
        and reduction["formal_lift_rejected_as_proof"] is True,
        "G6_selected_emission_still_open": upstream_cert["selected_correction_matrix_source_closed"] is False
        and upstream_cert["selected_full_response_emission_closed"] is False
        and upstream["decision"]["selected_correction_matrix_source_closed"] is False
        and upstream["decision"]["selected_full_response_emission_closed"] is False,
        "G7_required_payload_contract_complete": set(payload)
        == {
            "selected_source_certificate",
            "nonidentity_rho_E",
            "quotient_valid_B_N",
            "selected_D_E_Riesz_Green_dotD",
            "selected_deltaTheta_C1_solution",
            "primitive_C1_contractions_or_full_response_matrices",
            "b_selected_or_homogeneous_zero_theorem",
        }
        and all(item["required"] is True and item["current_status"] == "open" for item in payload.values()),
        "G8_no_targets_or_downstream_promotions": all(value is False for value in guards.values())
        and upstream["target_fitting_used"] is False
        and open_items["A_selected"] is True
        and open_items["b_selected"] is True
        and open_items["lambda_12"] is True
        and open_items["Yukawa_CKM_PMNS_CP_or_full_SM_closure"] is True,
        "G9_next_artifact_is_rhoe_bn": upstream["next_required_artifact"] == NEXT
        and upstream_cert["next_required_artifact"] == NEXT
        and upstream["decision"]["nonidentity_rhoE_and_BN_required"] is True,
    }

    return {
        "packet": "Selected_Correction_FullResponse_Frontier_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_primitive_frontier": str(PREVIOUS.relative_to(ROOT)),
            "qa_selected_correction_fullresponse_packet": str(QA_PACKET),
            "qa_selected_correction_fullresponse_certificate": str(QA_CERT),
        },
        "theorem": {
            "name": "SelectedCorrectionFullResponseFrontierImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected correction/full-response gate is reduced to a sharper "
                "source-construction problem.  A diagnostic qutrit/Weyl splitter "
                "shows no algebraic obstruction to mass splitting, noncommuting "
                "CKM/PMNS-style sectors, or a CP-odd invariant, and the q79 Weyl-pair "
                "packet supplies exact conditional A-support.  None of that is "
                "selected source emission.  Primitive-only emission, formal Galerkin "
                "lift, and diagnostic splitter promotion are rejected, so the next "
                "non-circular artifact must construct non-identity rho_E and "
                "quotient-valid B_N from the same q79/F,m=1 branch and then solve "
                "selected deltaTheta/C1 honestly."
            ),
        },
        "checks": checks,
        "upstream_certificate": upstream_cert,
        "upstream_packet": upstream,
        "frontier_update": {
            "old_next": OLD_NEXT,
            "current_next": NEXT,
            "why": (
                "The algebraic splitter smoke test passes, but no selected same-source "
                "payload emits correction matrices.  The proof obligation is therefore "
                "moved upstream to selected non-identity rho_E, quotient-valid B_N, and "
                "honest deltaTheta/C1 emission."
            ),
        },
        "required_payload": payload,
        "guardrails": {
            "does_not_claim_selected_correction_matrix_source": True,
            "does_not_claim_selected_full_response_emission": True,
            "does_not_promote_diagnostic_splitter": True,
            "does_not_promote_formal_galerkin_lift": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_lambda12": True,
            "does_not_claim_Yukawa_CKM_PMNS_CP_or_full_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "The correction/full-response gate is no longer vague: it has a "
                "machine-checkable reduction to selected rho_E/B_N construction plus "
                "selected deltaTheta/C1 solve, while diagnostic support remains support only."
            ),
            "what_remains": (
                "Construct the selected non-identity rho_E, quotient-valid B_N, "
                "selected D_E/Riesz/Green/dotD replay, selected deltaTheta/C1 solution, "
                "primitive C1 contractions or full response matrices, and b_selected "
                "or a homogeneous-zero theorem."
            ),
            "next_required_artifact": NEXT,
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "SelectedCorrectionFullResponseFrontierImport",
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
    diag = packet["upstream_packet"]["diagnostic_representative_support_only"]
    return f"""# Selected Correction FullResponse Frontier Import v1

## Result

Status: `{cert["status"]}`

The correction/full-response gate is now reduced, not closed.  The diagnostic
qutrit/Weyl splitter shows that finite mass splitting, sector noncommutation,
and a CP-odd invariant are algebraically reachable without observed targets.
That splitter remains support only.

```json
{json.dumps(diag, indent=2, sort_keys=True)}
```

## Reduction

Primitive-only emission and formal Galerkin lift do not prove selected
correction matrices.  The next construction must emit selected non-identity
`rho_E` and quotient-valid `B_N` from the same q79/F,m=1 branch, then run an
honest selected `deltaTheta/C1` solve.

```json
{json.dumps(packet["frontier_update"], indent=2, sort_keys=True)}
```

## Guardrail

No selected Yukawa hierarchy, CKM/PMNS matrix, CP phase, `A_selected`,
`b_selected`, `lambda_12`, or full SM closure is claimed here.
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
