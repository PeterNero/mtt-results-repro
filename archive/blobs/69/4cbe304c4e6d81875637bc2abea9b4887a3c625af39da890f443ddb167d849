"""Audit the U1/Y Route-C same-source selected-emission source certificate gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_samesource_selected_emission_source_certificate.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_samesource_selected_emission_source_certificate.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_samesource_selected_emission_source_certificate_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SameSource_SelectedEmission_SourceCertificate_v1.md"

STATUS = "U1Y_ROUTEC_SAMESOURCE_SELECTED_EMISSION_CERTIFICATE_ATTEMPTED_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedU10Ubar5Polarization_or_OverlapNormalization_v1"


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
    fields = data["emission_fields"]
    decision = data["decision"]
    canonical = data["canonical_1M_lemma"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("canonical 1M lemma imported", canonical["one_M_maps_to_Nc"] is True and canonical["matches_required_route"] is True and canonical["proposed_shift_route"] == ["d", "nuD"], canonical),
        check("all support present", cert["support_present"] == 7 and cert["required_fields"] == 7 and all(row["support_present"] is True for row in fields.values()), cert),
        check("nothing selected emitted yet", cert["selected_emitted"] == 0 and cert["same_source"] == 0 and cert["theorem_derived"] == 0, cert),
        check("selected emission remains open", decision["same_source_selected_emission_certificate_closed"] is False and decision["selected_1M_Dirac_source_emitted"] is False, decision),
        check("alpha1 still not promoted", decision["N_alpha1_h_ext_promoted_to_du_dalpha1"] is False and decision["alpha1_driver_verified"] is False, decision),
        check("operator and normalization blockers named", fields["operator_values"]["selected_emitted"] is False and fields["normalization"]["selected_emitted"] is False and "normalization" in fields["normalization"]["blocker"], fields),
        check("acceptance requires true selected fields", data["acceptance"]["validator_flags_required"]["selected_emitted"] is True and data["acceptance"]["passes_now"] is False, data["acceptance"]),
        check("guardrails hold", guardrails["claims_alpha1_driver_verified"] is False and guardrails["claims_lambda12"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records structural support not closure", "support_present = 7 / 7" in note and "selected_emitted = 0 / 7" in note and "Do not treat structural support as selected emission" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C same-source selected-emission source certificate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
