"""Audit the U1/Y Route-C End0-to-sector source/value packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.candidate.json"
VALUES = REPO / "candidate_data" / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet.values.json"
CERT = REPO / "certificates" / "selected_u1y_routec_end0_to_sector_functor_source_and_value_packet_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_End0_to_SectorFunctor_Source_and_Value_Packet_v1.md"

STATUS = "U1Y_ROUTEC_END0_TO_SECTOR_VALUE_PACKET_CONSTRUCTED_MODEL_VALUES_ZERO_MODE_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_ZeroModeBasis_From_HYM_Projector_Source_Theorem_v1"


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
    values = json.loads(VALUES.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    guardrails = data["guardrails"]
    validation = values["sector_carrier_model"]["validation"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("domain filled", decision["End0_domain_values_filled"] is True and values["domain"]["ad_T3_matrix"] == [[0, -1, 0], [1, 0, 0], [0, 0, 0]], values["domain"]),
        check("carrier built", decision["End0_tensor_product_carrier_constructed"] is True and values["sector_carrier_model"]["total_dimension"] == 19, values["sector_carrier_model"]["rank_match"]),
        check("projectors and brackets", validation["all_lie_checks_pass"] is True and validation["projectors_sum_to_identity"] is True and validation["all_projectors_idempotent"] is True, validation),
        check("conditional theorems imported", decision["conditional_adjoint_triplet_theorem_proved"] is True and decision["conditional_gram_normalization_theorem_proved"] is True, decision),
        check("not promoted", decision["selected_zero_mode_bases_emitted"] is False and decision["selected_source_map_emitted"] is False and decision["physical_dotD_alpha1_payload_extracted"] is False, decision),
        check("routing still open", decision["selected_matter_slot_routing_extracted"] is False and decision["selected_1M_Dirac_neutrino_rule"] is False, decision),
        check("no downstream closure", data["closure_claimed"] is False and guardrails["claims_lambda12"] is False and guardrails["claims_full_sm_closure"] is False, guardrails),
        check("guardrails", guardrails["promotes_model_carrier_as_selected_zero_modes"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents blocker", "not promoted to the selected physical dotD payload" in note and "selected zero-mode bases" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C End0-to-sector value packet audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
