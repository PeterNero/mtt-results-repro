"""Audit the q79 stability/HYM or Route-C residual source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_samesource_operatorpacket_fill_or_nogo.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_stability_hym_or_routec_residual_source.py"
CERT = ROOT / "certificates" / "q79_stability_hym_or_routec_residual_source_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_stability_hym_or_routec_residual_source.candidate.json"
TABLE = ROOT / "candidate_data" / "q79_stability_hym_or_routec_residual_source" / "central_neutral_destabilizer_summary.json"
PAPER = ROOT / "proof_corpus" / "Q79_Selected_RouteC_Stability_HYM_or_RouteC_Residual_Source_v1.md"

STATUS = "Q79_SELECTED_ROUTEC_STABILITY_ATTEMPT_CENTRAL_NEUTRAL_CLOSED_GLOBAL_ENUMERATION_OPEN"
NEXT = "Q79_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1"
EXPECTED_SM = "MTT_SELECTED_ROUTEC_STABILITY_ATTEMPT_CENTRAL_NEUTRAL_CLOSED_GLOBAL_ENUMERATION_OPEN"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TABLE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table == cert["central_neutral_destabilizer_theorem"], "summary table mismatch", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)
    require(
        cert["sm_input_statuses"]["stability_source_candidate"]["status"] == EXPECTED_SM,
        "SM stability status mismatch",
        failures,
    )

    central = cert["central_neutral_destabilizer_theorem"]
    ah = cert["appell_humbert_promotion"]
    routec = cert["route_c_residual_lane"]
    verdict = cert["q79_proof_verdict"]
    remaining = cert["what_remains_open"]

    require(central["candidate_count"] == 6, "expected six central-neutral candidates", failures)
    require(central["all_candidate_boundaries_injective"] is True, "boundaries not injective", failures)
    require(central["all_candidates_obstructed"] is True, "candidates not obstructed", failures)
    require(central["central_shared_circle_degree_zero"] is True, "shared circle not preserved", failures)
    require(ah["conditional_on_selected_AH_source"] is True, "AH condition missing", failures)
    require(routec["still_open"]["HYM_or_RouteC_selected_values"] is True, "Route-C lane overclosed", failures)
    require(verdict["central_neutral_stability_subtheorem_proved"] is True, "subtheorem not proved", failures)
    require(verdict["full_stability_proved"] is False, "full stability overclaimed", failures)
    require(verdict["hym_existence_proved"] is False, "HYM overclaimed", failures)

    for key in (
        "global_rank_one_torsion_free_subsheaf_enumeration",
        "selected_HYM_or_Strominger_existence_certificate",
        "selected_RouteC_residual_values",
        "same_source_D_E_Riesz_Green_dotD",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"open flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)
    require(cert["theorem"]["proved"] is True, "theorem must be proved", failures)
    require(cert["theorem"]["closure_claimed"] is False, "theorem closure must stay false", failures)

    for phrase in (
        "central-neutral destabilizer subtheorem",
        "does not close full stability/HYM",
        "candidate count",
        "Q79SelectedRouteCStabilityCentralNeutralSubtheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 stability/HYM source audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 stability/HYM source audit PASS")
    print(f"status: {cert['status']}")
    print(f"candidate_count: {central['candidate_count']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
