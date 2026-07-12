"""Audit the U1/Y Route-C operator-source identity bridge subpacket."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_operator_source_identity_bridge_subpacket.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_operator_source_identity_bridge_subpacket.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_operator_source_identity_bridge_subpacket_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_OperatorSourceIdentity_Bridge_Subpacket_v1.md"

STATUS = "U1Y_ROUTEC_OPERATOR_SOURCE_IDENTITY_BRIDGE_CURRENT_SOURCE_NOGO"
NEXT = "Selected_U1Y_RouteC_OperatorLayerPic0_or_SelectedResidual_Source_Subpacket_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    reqs = data["bridge_requirements"]
    result = data["source_identity_bridge_result"]
    routes = data["route_evaluation"]

    check("status exact", data["status"] == STATUS and cert["status"] == STATUS, data["status"])
    check(
        "four bridge requirements",
        set(reqs)
        == {
            "selected_operator_source_identity",
            "s3_gs_to_operator_bridge",
            "operator_layer_pic0",
            "selected_residual_or_hym",
        },
        reqs,
    )
    check(
        "support present but nothing selected",
        cert["support_requirements"] == 4
        and cert["selected_requirements"] == 0
        and all(row["support_present"] is True for row in reqs.values())
        and all(row["selected_emitted"] is False for row in reqs.values()),
        cert,
    )
    check(
        "bridge no-go scoped",
        result["bridge_closed"] is False
        and result["current_source_nogo"] is True
        and result["mathematical_impossibility_claimed"] is False
        and cert["mathematical_impossibility_claimed"] is False,
        result,
    )
    check(
        "s3 gs support retained but not promoted",
        routes["s3_gs_convergence_route"]["closed_support"]["selected_s3_source_closed"] is True
        and routes["s3_gs_convergence_route"]["closed_support"]["visible_green_schwarz_curvature_closed"] is True
        and routes["s3_gs_convergence_route"]["passes_bridge"] is False,
        routes["s3_gs_convergence_route"],
    )
    check(
        "terminal valpha update retained",
        routes["terminal_valpha_route"]["retired"]["selected_valpha_attempt_no_longer_blocks_on_ordered_source_validator"] is True
        and routes["terminal_valpha_route"]["open_item_count"] >= 20
        and routes["terminal_valpha_route"]["passes_bridge"] is False,
        routes["terminal_valpha_route"],
    )
    check(
        "hard cut set includes pic0 residual and DE",
        cert["hard_cut_set_count"] == 5
        and any("Pic0" in item for item in data["hard_cut_set"])
        and any("residual" in item for item in data["hard_cut_set"])
        and any("D_E" in item for item in data["hard_cut_set"]),
        data["hard_cut_set"],
    )
    check(
        "next artifact exact",
        data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT,
        cert,
    )
    check(
        "guardrails hold",
        data["guardrails"]["claims_lambda12"] is False
        and data["guardrails"]["promotes_support_as_selected"] is False
        and data["guardrails"]["uses_observed_data"] is False
        and cert["lambda_12_closed"] is False
        and cert["target_fitting_used"] is False,
        data["guardrails"],
    )
    check(
        "note records current-source no-go",
        "current_source_nogo = true" in note
        and "support convergence" in note
        and NEXT in note,
        NOTE,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
