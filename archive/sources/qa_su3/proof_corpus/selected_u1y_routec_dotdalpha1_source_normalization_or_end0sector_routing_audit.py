"""Audit the U1/Y Route-C dotD alpha1 source-normalization or End0 routing gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_dotdalpha1_source_normalization_or_end0sector_routing.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_dotdalpha1_source_normalization_or_end0sector_routing.candidate.json"
CONTRACT = REPO / "candidate_data" / "selected_u1y_routec_end0_to_sector_functor_value_packet.open.json"
CERT = REPO / "certificates" / "selected_u1y_routec_dotdalpha1_source_normalization_or_end0sector_routing_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_dotDAlpha1_SourceNormalization_or_End0SectorRouting_v1.md"

STATUS = "U1Y_ROUTEC_DOTD_ALPHA1_SOURCENORM_NOGO_END0SECTOR_FUNCTOR_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_End0_to_SectorFunctor_Source_and_Value_Packet_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    guardrails = data["guardrails"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("source norm rejected", decision["naive_source_normalization_rejected"] is True and cert["naive_source_normalization_rejected"] is True, decision),
        check("End0 route primary", decision["End0_sector_route_primary"] is True and cert["End0_sector_route_primary"] is True, decision),
        check("SM support not closure", decision["selected_Ext_density_scale_tangent_closed_in_SM_support"] is True and decision["physical_dotD_alpha1_payload_extracted"] is False, decision),
        check("contract open", contract["status"] == "OPEN_SELECTED_END0_TO_SECTOR_FUNCTOR_VALUES_REQUIRED" and len(contract["required_fields"]) >= 7, contract),
        check("values absent", decision["selected_End0_to_sector_functor_values_extracted"] is False and decision["selected_transfer_normalization_closed"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and decision["primitive_C1_values_computed"] is False and decision["lambda_12_computable"] is False, decision),
        check("guardrails", guardrails["claims_selected_dotD_source"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents route", "The direct scalar-normalization route is now rejected locally" in note and "End0-to-sector functor" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C dotD alpha1 source-normalization or End0 routing audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
