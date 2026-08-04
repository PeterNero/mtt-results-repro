"""Audit Route-C Galerkin execution cutset and primitive search import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_routec_galerkin_execution_cutset_and_primitive_search.py"
PACKET = ROOT / "candidate_data" / "routec_galerkin_execution_cutset_and_primitive_search.candidate.json"
CERT = ROOT / "certificates" / "routec_galerkin_execution_cutset_and_primitive_search_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_Galerkin_Execution_Cutset_and_Primitive_Search_v1.md"
STATUS = "ROUTEC_GALERKIN_EXECUTION_REDUCED_TO_PRIMITIVE_EMISSION_AND_SOURCE_PROMOTION_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(label: str, condition: bool, detail: object) -> None:
    print(f"{'PASS' if condition else 'FAIL'}: {label} -- {detail}")
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
    script_cert = json.loads(proc.stdout)

    check("status", cert["status"] == STATUS, cert["status"])
    check("script agrees", script_cert["status"] == cert["status"], script_cert["status"])
    check("theorem proved", packet["theorem"]["proved"] is True, packet["theorem"])
    check("all checks pass", all(packet["checks"].values()), packet["checks"])

    chain = packet["execution_chain"]
    check(
        "chain reaches primitive search",
        chain["solve_spec_next"] == "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1"
        and chain["first_run_next"] == "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1"
        and chain["r1_r4_next"] == "MTT_Selected_RouteC_Selected_Primitive_Emission_Search_v1"
        and chain["primitive_search_status"]
        == "MTT_SELECTED_ROUTEC_PRIMITIVE_EMISSION_SEARCH_EXECUTED_NO_LEGAL_EMISSION_FOUND",
        chain,
    )

    cutset = packet["cutset"]
    check(
        "cutset is selected PhiFin plus quotient-valid BN",
        cutset["provenance_minimal_missing_primitive"] == "Phi_fin_selected_payload"
        and cutset["basis_minimal_missing_primitive"]
        == "quotient_valid_B_N_basis_certificate"
        and all(value is False for value in cutset["R1_to_R6_closure_vector"].values()),
        cutset,
    )

    ladder = packet["constructive_numeric_ladder"]
    check(
        "numeric ladder built but source promotion open",
        ladder["nonidentity_rhoE_packet_built"]
        and ladder["smooth_BN_basis_scaffold_built"]
        and ladder["DE_matrix_on_27_mode_BN_built"]
        and ladder["dotD_alpha1_matrix_same_basis_built"]
        and ladder["C1_engine_built_zero_canonical_response"]
        and all(value is True for value in ladder["still_open"].values()),
        ladder,
    )

    update = packet["frontier_update"]
    check(
        "frontier moved to primitive source promotion or BN basis emission",
        update["old_next"] == "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1"
        and update["current_next"]
        == "MTT_Selected_RouteC_Primitive_SourcePromotion_or_BNBasis_Emission_v1",
        update,
    )
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "primitive emission/source promotion",
        "Constructive Numeric Ladder",
        "quotient-valid selected `B_N` basis",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nRoute-C Galerkin execution cutset and primitive search audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
