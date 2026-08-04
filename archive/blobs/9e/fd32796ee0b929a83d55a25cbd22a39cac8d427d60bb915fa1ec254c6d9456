"""Audit the U1/Y Route-C U10/Ubar5 polarization or overlap-normalization gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_selected_u10ubar5_polarization_or_overlap_normalization.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_selected_u10ubar5_polarization_or_overlap_normalization.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_selected_u10ubar5_polarization_or_overlap_normalization_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SelectedU10Ubar5Polarization_or_OverlapNormalization_v1.md"

STATUS = "U1Y_ROUTEC_U10UBAR5_POLARIZATION_OVERLAP_GATE_BUILT_SOURCE_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1"


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
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    route_a = data["route_A_SU5_E6_polarization"]
    route_b = data["route_B_HYM_projector_zero_mode"]
    overlap = data["overlap_normalization"]
    decision = data["decision"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("route A support exact", route_a["support_closed"] is True and route_a["selected_closed"] is False and route_a["finite_packet"]["U_10"] == "I_3" and route_a["finite_packet"]["U_bar5"] == "F", route_a),
        check("route B support not selected", route_b["support_closed"] is True and route_b["selected_closed"] is False and route_b["functional_projector_payload_present"] is True, route_b),
        check("conditional normalization fixed", overlap["conditional_gram_theorem_proved"] is True and overlap["gram_conditionally_forced_after_rho_s"] is True and overlap["selected_transfer_normalization"] is False, overlap),
        check("raw norm and unit transfer recorded", abs(overlap["raw_T3_frobenius_norm_per_matter_sector"] - 2 ** 0.5) < 1e-12 and "sqrt(2)" in overlap["unit_trace_transfer"], overlap),
        check("no selected closure", decision["selected_U10_Ubar5_polarization_emitted"] is False and decision["selected_overlap_normalization_emitted"] is False and decision["alpha1_driver_verified"] is False, decision),
        check("contract includes source and normalization", data["same_branch_emission_contract"]["must_emit"]["selected_overlap_transfer_normalization"] is True and data["same_branch_emission_contract"]["must_emit"]["selected_rho_s_and_zero_mode_bases"] is True, data["same_branch_emission_contract"]),
        check("guardrails hold", guardrails["claims_selected_U10_Ubar5"] is False and guardrails["claims_lambda12"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records support vs selected", "route_A_support_closed = true" in note and "route_A_selected_closed = false" in note and "Do not treat `U_10=I_3`" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C U10/Ubar5 polarization or overlap-normalization audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
