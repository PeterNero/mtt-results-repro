"""Audit alpha1 tangent-kernel cross-repo refinement."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import_alpha1_tangent_kernel_crossrepo_refinement.py"
PACKET = ROOT / "candidate_data" / "alpha1_tangent_kernel_crossrepo_refinement.candidate.json"
CERT = ROOT / "certificates" / "alpha1_tangent_kernel_crossrepo_refinement_certificate.json"
NOTE = ROOT / "proof_corpus" / "Alpha1_TangentKernel_CrossRepo_Refinement_v1.md"
STATUS = "ALPHA1_TANGENT_KERNEL_IMPORTED_ACCEPTANCE_REFINED_SELECTION_NORMALIZATION_OPEN"


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

    kernel = packet["imported_tangent_kernel"]
    tangent = kernel["tangent"]
    normalization = kernel["normalization_functional"]
    check(
        "finite tangent kernel imported but not selected",
        kernel["kernel_name"] == "K_alpha1_tangent"
        and tangent["symbol"] == "h_ext"
        and tangent["zero_mean"] is True
        and tangent["selected_now"] is False
        and tangent["h_ext_l2"] > 0
        and tangent["h_ext_residual_l2"] < 1e-12,
        tangent,
    )
    check(
        "canonical dual pins unit candidate only",
        normalization["N_alpha1_h_ext"] == 1.0
        and normalization["lambda_alpha1_candidate"] == 1.0
        and normalization["selected_now"] is False
        and "not a selected MTT normalization" in normalization["why_not_selected"],
        normalization,
    )

    refinement = packet["acceptance_refinement"]
    remaining = refinement["still_required_now"]
    check(
        "acceptance theorem keeps true blockers open",
        refinement["current_repo_improvement"][
            "stationary_source_projector_riesz_green_replay_closed"
        ]
        is True
        and all(remaining.values()),
        refinement,
    )

    retarded = packet["retarded_alternative"]
    check(
        "retarded pattern is classified but not proof source",
        retarded["classified"]
        and retarded["kernel_pattern_available"]
        and retarded["typed_sm_dotD_kernel_emitted"] is False
        and not any(retarded["open_transfer_checks"].values()),
        retarded,
    )

    update = packet["frontier_update"]
    check(
        "frontier narrows to same-source normalization packet",
        update["old_next"]
        == "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1"
        and update["current_next"]
        == "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1",
        update,
    )
    check("guardrails retained", all(value is True for value in cert["guardrails"].values()), cert["guardrails"])

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "canonical L2 dual",
        "not a selected MTT normalization functional",
        "Acceptance Refinement",
        "Retarded Alternative Boundary",
    ):
        check(f"note records {phrase}", phrase in note, NOTE)

    print("\nAlpha1 tangent-kernel cross-repo refinement audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
