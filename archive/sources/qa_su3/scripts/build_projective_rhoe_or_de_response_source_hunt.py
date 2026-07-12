"""Hunt for a selected Qa/SU3 projective rho_E or D_E response source."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

FILL_ATTEMPT = DATA / "gerbe_twisted_local_system_response_fill_attempt.candidate.json"
OUTPUT_DATA = DATA / "projective_rhoe_or_de_response_source_hunt.candidate.json"
OUTPUT_CERT = CERTS / "projective_rhoe_or_de_response_source_hunt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Projective_RhoE_or_DE_Response_Source_Hunt_v1.md"

Q79_CERTS = {
    "projective_rhoe_mesh_validator": Q79 / "certificates" / "iwasawa_projective_rhoe_mesh_validator_certificate.json",
    "projective_twist_source_hunt": Q79 / "certificates" / "iwasawa_projective_twist_source_hunt_certificate.json",
    "twisted_source_promotion_gate": Q79 / "certificates" / "iwasawa_twisted_source_promotion_gate_certificate.json",
    "visible_rhoe_source_ansatz": Q79 / "certificates" / "visible_rhoE_source_ansatz_search_certificate.json",
    "visible_twisted_s3_closure": Q79 / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json",
}


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def maybe_load(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"present": False, "path": str(path)}
    data = load(path)
    data["present"] = True
    data["path"] = str(path)
    return data


def build() -> tuple[dict[str, object], dict[str, object], str]:
    fill = load(FILL_ATTEMPT)
    q79 = {name: maybe_load(path) for name, path in Q79_CERTS.items()}
    route_tests = [
        {
            "route_id": "q79_projective_rhoe_mesh_validator_transfer",
            "verdict": "VALIDATOR_READY_GUARDRAIL_ONLY",
            "promotes_qa_su3_source": False,
            "evidence": {
                "present": q79["projective_rhoe_mesh_validator"].get("present", False),
                "projective_validator_ready": q79["projective_rhoe_mesh_validator"].get("verdict", {}).get("projective_validator_ready"),
                "claims_selected_rho_E_constructed": q79["projective_rhoe_mesh_validator"].get("guardrails", {}).get("claims_selected_rho_E_constructed"),
                "claims_selected_D_E_constructed": q79["projective_rhoe_mesh_validator"].get("guardrails", {}).get("claims_selected_D_E_constructed"),
            },
            "reason": "It supplies the right projective rho_E mesh validator, but explicitly does not select a Qa/SU3 rho_E or D_E source.",
        },
        {
            "route_id": "q79_projective_twist_source_hunt_transfer",
            "verdict": "ALIGNED_BUT_SOURCE_MAP_OPEN",
            "promotes_qa_su3_source": False,
            "evidence": {
                "present": q79["projective_twist_source_hunt"].get("present", False),
                "projective_route_corpus_aligned": q79["projective_twist_source_hunt"].get("verdict", {}).get("projective_route_corpus_aligned"),
                "selected_projective_twist_source_found": q79["projective_twist_source_hunt"].get("verdict", {}).get("selected_projective_twist_source_found"),
                "selected_twisted_D_E_missing": q79["projective_twist_source_hunt"].get("missing_for_projective_carrier_selection", {}).get("selected_twisted_D_E_and_dotD_action"),
            },
            "reason": "It finds alignment with heterotic gerbe/B-field/Bianchi data, but the selected map to the central cocycle and D_E/dotD response remain open.",
        },
        {
            "route_id": "q79_twisted_source_promotion_gate_transfer",
            "verdict": "PROMOTION_CONTRACT_REUSABLE_VALUES_OPEN",
            "promotes_qa_su3_source": False,
            "evidence": {
                "present": q79["twisted_source_promotion_gate"].get("present", False),
                "twisted_promotion_gate_ready": q79["twisted_source_promotion_gate"].get("verdict", {}).get("twisted_promotion_gate_ready"),
                "current_projective_carrier_remains_unpromoted": q79["twisted_source_promotion_gate"].get("verdict", {}).get("current_projective_carrier_remains_unpromoted"),
                "selected_twisted_D_E_open": q79["twisted_source_promotion_gate"].get("still_open", {}).get("selected_twisted_D_E_and_dotD_response"),
            },
            "reason": "It gives an excellent promotion contract for Qa/SU3 to imitate, but no selected Qa/SU3 promotion packet is filled.",
        },
        {
            "route_id": "visible_rhoe_source_ansatz_transfer",
            "verdict": "NARROWS_ROUTE_NOT_SOURCE",
            "promotes_qa_su3_source": False,
            "evidence": {
                "present": q79["visible_rhoe_source_ansatz"].get("present", False),
                "next_object": q79["visible_rhoe_source_ansatz"].get("calculation_results", {}).get("next_object_identified"),
                "claims_selected_D_E_constructed": q79["visible_rhoe_source_ansatz"].get("guardrails", {}).get("claims_selected_D_E_constructed"),
                "promotes_projective_fixture_as_selected": q79["visible_rhoe_source_ansatz"].get("guardrails", {}).get("promotes_projective_fixture_as_selected"),
            },
            "reason": "It rules out several ordinary rho_E shortcuts and points to selected response/twist data, exactly matching the Qa/SU3 blocker.",
        },
    ]
    hunt_result = {
        "validator_patterns_found": all(test["evidence"]["present"] for test in route_tests),
        "projective_rhoe_validator_available": route_tests[0]["evidence"]["projective_validator_ready"] is True,
        "twisted_promotion_contract_available": route_tests[2]["evidence"]["twisted_promotion_gate_ready"] is True,
        "selected_qa_su3_projective_rhoE_found": False,
        "selected_qa_su3_D_E_or_dotD_found": False,
        "selected_qa_su3_finite_response_found": False,
        "qa_su3_packet_closed": False,
        "target_fitting_used": False,
    }
    candidate = {
        "candidate": "SelectedQaSU3ProjectiveRhoEOrDEResponseSourceHunt",
        "status": "QA_SU3_PROJECTIVE_RHOE_OR_DE_RESPONSE_SOURCE_HUNT_DONE_VALIDATORS_FOUND_SOURCE_OPEN",
        "input_status": fill["status"],
        "q79_certificate_statuses": {name: data.get("status", "MISSING") for name, data in q79.items()},
        "route_tests": route_tests,
        "hunt_result": hunt_result,
        "accepted_reuse": [
            "projective rho_E mesh validator schema",
            "twisted-source promotion contract",
            "guardrail that ordinary rho_E shortcuts do not select the source",
            "requirement for selected gerbe/B-field map to central cocycle before D_E/dotD promotion",
        ],
        "rejected_reuse": [
            "direct q79/S3 finite table as Qa/SU3 representative",
            "projective magnetic carrier as selected physical rho_E",
            "validator pass as source selection",
            "D_E/dotD source flags from q79 as Qa/SU3 operator data",
        ],
        "decision": {
            "result": "Reusable projective rho_E/D_E validators found; selected Qa/SU3 response source not found.",
            "why": "Every strong candidate is either off-branch q79 machinery or a promotion contract whose source fields remain open.",
            "next_move": "Instantiate a Qa/SU3 twisted-source promotion packet with selected gerbe/B-field representative, central cocycle map, Bianchi/Freed-Witten/projector flags, and projective rho_E/D_E response data.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Twisted_Source_Promotion_Packet_Interface_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "projective_rhoE_validator_pattern_found": hunt_result["projective_rhoe_validator_available"],
            "twisted_promotion_contract_found": hunt_result["twisted_promotion_contract_available"],
            "ordinary_rhoE_shortcuts_rejected_by_guardrail": True,
        },
        "what_remains_open": {
            "selected_qa_su3_projective_rhoE": True,
            "selected_qa_su3_D_E_or_dotD": True,
            "selected_gerbe_to_central_cocycle_map": True,
            "finite_response": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Projective RhoE or DE Response Source Hunt v1

## Result

The hunt found reusable machinery, but not the selected Qa/SU3 response source.

```text
projective rho_E mesh validator: found
twisted-source promotion contract: found
ordinary rho_E shortcut guardrails: found
selected Qa/SU3 projective rho_E: not found
selected Qa/SU3 D_E/dotD: not found
finite response: not found
target fitting used: no
```

## Interpretation

The q79 projective machinery is extremely useful as a validator pattern. It
separates strict ordinary gluing from genuine projective/gerbe gluing and gives
a promotion contract requiring selected gerbe/B-field source data, central
cocycle map, Bianchi, Freed-Witten, projector, metric, sector, and response
validators.

But it does not select the Qa/SU3 packet. It is off-branch and its own
certificates mark selected `D_E`/`dotD` and source promotion as open.

## Next Artifact

```text
{candidate["next_required_artifact"]}
```

That artifact should instantiate the promotion schema for Qa/SU3 directly,
instead of importing q79 values.

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, note


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
