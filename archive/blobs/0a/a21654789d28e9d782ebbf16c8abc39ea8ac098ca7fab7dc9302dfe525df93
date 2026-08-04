"""Import Route-C I10 payload contract / quadrature values gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_phifinc1_binding_reduction_import_certificate.json"
UPSTREAM_SLUG = "selected_minimizertracec1payloadtheorem_or_quadraturetablevalues"
UPSTREAM_PACKET = SM / "candidate_data" / f"{UPSTREAM_SLUG}.candidate.json"
UPSTREAM_CERT = SM / "certificates" / f"{UPSTREAM_SLUG}_certificate.json"
UPSTREAM_NOTE = SM / "proof_corpus" / "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1.md"
UPSTREAM_DIR = SM / "candidate_data" / UPSTREAM_SLUG
PAYLOAD = UPSTREAM_DIR / "i10_minimizer_trace_c1_payload_contract.packet.json"
QUADRATURE = UPSTREAM_DIR / "quadrature_values_staging_tables.packet.json"
MANIFEST = UPSTREAM_DIR / "closure_acceptance_manifest.packet.json"

OUTPUT_PACKET = DATA / "routec_i10_payload_contract_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_i10_payload_contract_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_I10PayloadContract_Import_v1.md"

STATUS = "ROUTEC_I10_PAYLOAD_CONTRACT_IMPORTED_VALUES_OPEN"
PREVIOUS_STATUS = "ROUTEC_PHIFINC1_BINDING_REDUCTION_IMPORTED_I10_OR_QUADRATURE_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_MINIMIZERTRACE_C1_PAYLOAD_OR_QUADRATURE_VALUES_CONTRACT_BUILT_OPEN"
NEXT = "MTT_Selected_I10_PayloadCertificate_or_IndependentQuadratureValuesFill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    cert = load(UPSTREAM_CERT)
    payload = load(PAYLOAD)
    quadrature = load(QUADRATURE)
    manifest = load(MANIFEST)
    note = UPSTREAM_NOTE.read_text(encoding="utf-8")
    replay = upstream["replay_if_route_A_or_B_accepted"]
    required = payload["payload_certificate_required"]

    payload_checks = {
        key: spec["required"] is True
        and len(spec["must_emit"]) == 4
        and len(spec["forbidden"]) == 2
        for key, spec in required.items()
    }

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1",
        "F1_upstream_contract_proved_open": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["unpatched_theorem_closure_claimed"] is False
        and upstream["observed_data_used"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": cert["status"] == UPSTREAM_STATUS
        and cert["theorem_proved"] is True
        and cert["closure_claimed"] is False
        and cert["next_required_artifact"] == NEXT,
        "F3_i10_payload_contract_fixed": payload["status"] == "PAYLOAD_CERTIFICATE_CONTRACT_BUILT_VALUES_OPEN"
        and payload["theorem_slot"] == "I10_phifinc1_minimizes_c1_defect_functional"
        and all(payload_checks.values())
        and payload["promotion_rule"]["current_all_payload_certificates_verified"] is False
        and payload["promotion_rule"]["if_all_payload_certificates_verified"]["SM_parity_dynamic_packet_closes"] is True,
        "F4_quadrature_tables_staged_empty": quadrature["status"] == "TABLES_STAGED_VALUES_EMPTY"
        and quadrature["values_filled_now"] is False
        and quadrature["expected_minimum_counts"]["zero_mode_basis_rows"] == 8
        and quadrature["expected_minimum_counts"]["primitive_contraction_rows"] == 18
        and quadrature["expected_minimum_counts"]["hessian_source_rows"] == 2
        and quadrature["expected_minimum_counts"]["sector_matrix_rows"] == 18
        and all(rows == [] for rows in quadrature["tables"].values())
        and quadrature["would_close_if_filled"]["honest_independent_Galerkin_C1_closes"] is True,
        "F5_acceptance_manifest_open": manifest["status"] == "DUAL_ROUTE_ACCEPTANCE_MANIFEST_BUILT_OPEN"
        and manifest["route_A_i10_payload_certificate"]["accepted_now"] is False
        and manifest["route_B_independent_quadrature_values"]["accepted_now"] is False
        and manifest["closure_claimed_now"] is False
        and manifest["replay_target_if_accepted"] == replay
        and "deltaTheta_solve_matches_replay" in manifest["route_B_independent_quadrature_values"]["required_checks"],
        "F6_remaining_gates_preserved": all(upstream["what_remains_open"][key] is True for key in [
            "selected_minimizer_trace_payload_verified",
            "selected_c1_response_payload_verified",
            "defect_functional_minimizer_payload_verified",
            "independent_quadrature_values_filled",
            "unpatched_SM_parity_dynamic_packet_closure",
            "true_SM_equivalence_closure",
        ])
        and all(upstream["promotion_decision"][key] is False for key in [
            "route_A_i10_payload_certificate_accepted",
            "route_B_independent_quadrature_values_accepted",
            "I10_proved",
            "unpatched_SM_parity_dynamic_packet_closed",
            "true_SM_equivalence_closed",
        ]),
        "F7_note_route_summary_present": "Route A" in note and "Route B" in note,
    }

    summary = {
        "route_A_i10_payload_contract_built": True,
        "route_A_accepted_now": False,
        "route_B_quadrature_tables_staged": True,
        "route_B_values_filled_now": False,
        "closure_claimed_now": False,
        "expected_minimum_counts": quadrature["expected_minimum_counts"],
        "A_transpose_A": replay["A_transpose_A"],
        "A_transpose_b": replay["A_transpose_b"],
        "deltaTheta_C1": replay["deltaTheta_C1"],
    }

    return {
        "packet": "RouteC_I10PayloadContract_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
            "upstream_payload_contract": str(PAYLOAD),
            "upstream_quadrature_tables": str(QUADRATURE),
            "upstream_acceptance_manifest": str(MANIFEST),
        },
        "theorem": {
            "name": "RouteCI10PayloadContractImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The remaining unpatched closure routes are now machine-checkable: "
                "Route A requires three I10 payload certificates, while Route B "
                "requires independent quadrature/Hessian table values and acceptance checks."
            ),
        },
        "checks": checks,
        "i10_payload_contract_summary": summary,
        "upstream_candidate": upstream,
        "upstream_packets": {
            "i10_minimizer_trace_c1_payload_contract": payload,
            "quadrature_values_staging_tables": quadrature,
            "closure_acceptance_manifest": manifest,
        },
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_route_A_accepted": False,
            "claims_route_B_accepted": False,
            "claims_I10_proved": False,
            "claims_unpatched_A_selected": False,
            "claims_unpatched_b_selected": False,
            "claims_unpatched_deltaTheta_C1": False,
            "claims_unpatched_SM_dynamic_closure": False,
            "claims_true_SM_equivalence": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCI10PayloadContractImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "i10_payload_contract_summary": packet["i10_payload_contract_summary"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    s = cert["i10_payload_contract_summary"]
    return f"""# RouteC I10 Payload Contract Import v1

Status: `{cert["status"]}`.

The unpatched closure conditions are now machine-checkable.

```text
Route A I10 payload contract built = {s["route_A_i10_payload_contract_built"]}
Route A accepted now = {s["route_A_accepted_now"]}
Route B quadrature tables staged = {s["route_B_quadrature_tables_staged"]}
Route B values filled now = {s["route_B_values_filled_now"]}
closure claimed now = {s["closure_claimed_now"]}
```

Expected minimum independent-table counts:

```text
{s["expected_minimum_counts"]}
```

Replay if either route is accepted:

```text
A^T A = {s["A_transpose_A"]}
A^T b = {s["A_transpose_b"]}
deltaTheta_C1 = {s["deltaTheta_C1"]}
```

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
