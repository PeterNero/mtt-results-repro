"""Audit alpha1 driver closure and post-alpha gate import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_alpha1_driver_closure_and_postalpha_gate.py"
PACKET = ROOT / "candidate_data" / "alpha1_driver_closure_and_postalpha_gate_import.candidate.json"
CERT = ROOT / "certificates" / "alpha1_driver_closure_and_postalpha_gate_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "Alpha1_Driver_Closure_and_PostAlpha_Gate_Import_v1.md"

STATUS = "ALPHA1_DRIVER_CLOSED_POSTALPHA_PRIMITIVE_C1_LAMBDA12_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1_AtomEmission_or_SelectedLambda12_SpectralTable_v1"


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

    alpha = packet["closed_alpha1_driver"]
    value = alpha["promoted_value"]
    replay = alpha["honest_dotd_replay"]
    check(
        "alpha1 selected value closes",
        value["selected_value_emitted_by_this_theorem"] is True
        and value["N_alpha1_h_ext"] == 1.0
        and value["lambda_alpha1"] == 1.0
        and value["du_dalpha1"] == "h_ext"
        and value["tangent_residual_l2"] == 0.0,
        value,
    )
    check(
        "honest dotD replay closes",
        replay["selected_dotD_source_verified"]
        and replay["alpha1_driver_verified"]
        and replay["honest_dotD_validator_closed"]
        and "not diagnostic flags" in replay["why_not_lifted_flags"].lower(),
        replay,
    )

    post = packet["post_alpha_frontier"]
    primitive = post["primitive_status"]
    lambda12 = post["lambda12_status"]
    check(
        "primitive C1 atoms remain exact open gate",
        primitive["atom_count"] == 24
        and primitive["missing_atom_count"] == 24
        and primitive["all_primitive_atoms_emitted"] is False
        and all(len(row["missing_terms"]) == 6 for row in post["atom_table"].values()),
        primitive,
    )
    check(
        "lambda12 remains separate open gate",
        lambda12["lambda_12_closed"] is False
        and lambda12["lambda_12_computable_from_this_gate"] is False
        and lambda12["electroweak_lane_A_lambda12_closed"] is False,
        lambda12,
    )

    update = packet["frontier_update"]
    check(
        "frontier advances to primitive atoms or lambda12 table",
        update["old_next"] == "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1"
        and update["current_next"] == NEXT,
        update,
    )
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "alpha1_driver_verified = true",
        "honest dotD replay = PASS",
        "not a full SM closure claim",
        "selected primitive C1 atom table",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nAlpha1 driver closure and post-alpha gate import audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
