"""Audit the U1/Y local determinant from 27-mode D_E gap-layer gate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.py"
DATA = REPO / "candidate_data" / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.candidate.json"
CERT = REPO / "certificates" / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer_certificate.json"
SPECTRUM = REPO / "candidate_data" / "selected_electroweak_u1y_localdeterminant_from_27mode_de_gaplayer.spectrum_attempt.json"
NOTE = REPO / "proof_corpus" / "Selected_Electroweak_U1Y_LocalDeterminant_From_27Mode_DE_GapLayer_v1.md"

STATUS = "ELECTROWEAK_U1Y_LOCALDETERMINANT_FROM_27MODE_DE_GAPLAYER_ATTEMPTED_FUNCTIONAL_MAP_OPEN"
NEXT = "Selected_Electroweak_U1Y_DeterminantFunctional_Weighting_or_NoGo_v1"


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
    spectrum = json.loads(SPECTRUM.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    tests = data["determinant_map_tests"]
    guardrails = data["guardrails"]
    expected_gamma = 4.0 * math.pi**2 / 9.0
    expected_logdet = 12.0 * math.log(expected_gamma) + 12.0 * math.log(2.0 * expected_gamma)

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 4, proc.stdout),
        check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("gamma computed", abs(spectrum["base_laplacian_unit_numeric"] - expected_gamma) < 1e-12, spectrum["base_laplacian_unit_numeric"]),
        check("conditional spectrum multiplicities", spectrum["rank3_model_kernel_multiplicity"] == 3 and sum(row["multiplicity"] for row in spectrum["rank3_model_positive_complement"]) == 24, spectrum),
        check("conditional logdet", abs(cert["conditional_logdet_positive_complement"] - expected_logdet) < 1e-12, cert["conditional_logdet_positive_complement"]),
        check("gap bound rejected", tests["use_27mode_gap_bound_as_logdet"]["status"] == "REJECTED_BOUND_NOT_SPECTRUM", tests["use_27mode_gap_bound_as_logdet"]),
        check("model spectrum not promoted", tests["use_rank3_model_complement_spectrum_as_U1Y"]["status"] == "CONDITIONAL_SUPPORT_NOT_SELECTED_U1Y_FUNCTIONAL", tests["use_rank3_model_complement_spectrum_as_U1Y"]),
        check("H zero policy open", tests["include_H_zero_cluster_shift"]["status"] == "POLICY_OPEN", tests["include_H_zero_cluster_shift"]),
        check("Pperp rejected as spectrum", tests["use_Pperp_trace_index_as_weighted_spectrum"]["status"] == "REJECTED_PROJECTOR_NOT_SPECTRUM", tests["use_Pperp_trace_index_as_weighted_spectrum"]),
        check("required functional isolated", "sector restriction from the 27-mode B_N/End0 packet to U1/Y on V/<s>" in data["required_functional"]["must_select"], data["required_functional"]),
        check("no closure", cert["closure_claimed"] is False and decision["lambda_12_closed"] is False and decision["selected_U1Y_determinant_functional_closed"] is False, decision),
        check("guardrails forbid shortcuts", all(value is False for value in guardrails.values()), guardrails),
        check("note says tried before", "What We Tried Before" in note and "did not select the determinant functional" in note, NOTE),
    ]
    print("\nSelected electroweak U1/Y local determinant from 27-mode D_E gap-layer audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
