"""Audit q79 AH-source or Route-C residual synthesis packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_q79_selected_ah_source_or_routec_residual_synthesis.py"
PACKET = ROOT / "candidate_data" / "q79_selected_ah_source_or_routec_residual_synthesis.candidate.json"
CERT = ROOT / "certificates" / "q79_selected_ah_source_or_routec_residual_synthesis_certificate.json"
NOTE = ROOT / "proof_corpus" / "Q79_Selected_AH_Source_or_RouteC_Residual_Synthesis_v1.md"

STATUS = "Q79_SELECTED_AH_SOURCE_OR_ROUTEC_RESIDUAL_SYNTHESIS_BUILT_FINITE_EMISSION_PRIMARY_VALUES_OPEN"
NEXT = "Q79_Selected_RouteC_FiniteEmissionMorphism_PhiFin_SourceIdentity_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}: {label} -- {detail}")
    if not condition:
        raise SystemExit(1)


def main() -> int:
    packet = load(PACKET)
    cert = load(CERT)
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("script runs", proc.returncode == 0, proc.stdout)
    script_packet = json.loads(proc.stdout)

    check("packet and certificate match", packet == cert, {"packet": PACKET, "cert": CERT})
    check("script agrees", script_packet["status"] == packet["status"], script_packet["status"])
    check("status", packet["status"] == STATUS, packet["status"])
    check("synthesis checks pass", all(packet["synthesis_checks"].values()), packet["synthesis_checks"])
    check("theorem proved without closure", packet["theorem"]["proved"] is True, packet["theorem"])
    check("next artifact", packet["best_next_artifact"] == NEXT, packet["best_next_artifact"])

    ranking = packet["route_ranking"]
    check(
        "finite emission primary",
        ranking[0]["route"] == "selected_finite_emission_Phi_fin_source_identity"
        and ranking[0]["current_status"] == "primary_next_executable",
        ranking[0],
    )
    check(
        "AH/HYM kept conditional",
        ranking[1]["route"] == "selected_AH_goodcover_plus_Gauduchon_chamber"
        and ranking[1]["current_status"] == "parallel_theorem_workstream",
        ranking[1],
    )
    check(
        "formal lift diagnostic only",
        ranking[2]["route"] == "formal_lift_of_RouteC_smoke_flags"
        and ranking[2]["current_status"] == "diagnostic_only",
        ranking[2],
    )
    check(
        "external sources inspiration only",
        all(item["proof_import"] is False for item in packet["external_inspiration"])
        and packet["external_guardrail"]["external_sources_used_as_proof_data"] is False,
        packet["external_inspiration"],
    )
    check(
        "contract requires same-source operator objects",
        "same-source finite D_E action" in packet["best_next_contract"]["must_emit"]
        and "same-source Riesz projector and reduced Green operator"
        in packet["best_next_contract"]["must_emit"]
        and "same-branch dotD/alpha1 derivative" in packet["best_next_contract"]["must_emit"],
        packet["best_next_contract"],
    )
    check(
        "contract rejects diagnostic promotion",
        "lifted selected flags" in packet["best_next_contract"]["must_reject"]
        and "observed CKM/mass/Yukawa inputs" in packet["best_next_contract"]["must_reject"],
        packet["best_next_contract"]["must_reject"],
    )
    check("guardrails all negative", all(v is False for v in packet["guardrails"].values()), packet["guardrails"])
    check(
        "remaining selected values open",
        packet["what_remains_open"]["selected_rho_E_source_identity"] is True
        and packet["what_remains_open"]["same_source_D_E_Riesz_Green_dotD"] is True
        and packet["what_remains_open"]["selected_RouteC_residual_values"] is True,
        packet["what_remains_open"],
    )

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "The AH/HYM branch remains mathematically useful but conditional",
        "The Route-C branch is the better next executable path",
        "method-shape inspiration only",
        NEXT,
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nQ79 AH-source or Route-C residual synthesis audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
