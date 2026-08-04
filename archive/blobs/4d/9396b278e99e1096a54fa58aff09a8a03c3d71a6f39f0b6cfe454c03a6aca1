"""Audit the same-source monad/GS/operator fusion gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "same_source_monad_gs_operator_fusion_gate_certificate.json"
CANDIDATE = REPO / "candidate_data" / "same_source_monad_gs_operator_fusion_gate.candidate.json"
TEMPLATE = REPO / "certificates" / "same_source_monad_gs_operator_fusion.template.json"
NOTE = REPO / "proof_corpus" / "Same_Source_Monad_GS_Operator_Fusion_Gate_v1.md"
SCRIPT = REPO / "scripts" / "build_same_source_monad_gs_operator_fusion_gate.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    computed = run_script()
    note = NOTE.read_text(encoding="utf-8")

    closed = cert["closed_constituents"]
    current = cert["current_fusion_attempt"]
    implication = cert["proof_implication"]
    no_patchwork = cert["why_current_patchwork_is_not_a_proof"]
    guardrails = cert["guardrails"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "SAME_SOURCE_MONAD_GS_OPERATOR_FUSION_GATE_FORMULATED_SOURCE_OPEN",
            cert["status"],
        ),
        check(
            "script agrees with saved candidate",
            computed["closed_constituents"] == candidate["closed_constituents"]
            and computed["current_fusion_attempt"] == candidate["current_fusion_attempt"]
            and computed["minimal_next_packet"] == candidate["minimal_next_packet"],
            computed["status"],
        ),
        check(
            "template is open fusion packet",
            template["schema"] == "SameSourceMonadGSOperatorFusionPacket.v1"
            and template["status"] == "OPEN_SAME_SOURCE_MONAD_GS_OPERATOR_FUSION_REQUIRED"
            and "source_identity" in template
            and "operator_response" in template,
            template,
        ),
        check(
            "separate constituents recognized as closed",
            closed["monad_conditional_uniqueness_closed"] is True
            and closed["monad_sufficiency_after_selection_closed"] is True
            and closed["time_oriented_m1_gerbe_representative_closed"] is True
            and closed["visible_green_schwarz_curvature_row_closed"] is True
            and closed["route_c_finite_pipeline_conditionally_passes"] is True
            and closed["selected_source_promotion_gate_ready"] is True,
            closed,
        ),
        check(
            "unconditional selector remains open",
            closed["unconditional_monad_selector_still_open"] is True
            and cert["current_fusion_closes_selected_monad_source"] is False,
            {
                "closed": closed["unconditional_monad_selector_still_open"],
                "fusion_closes": cert["current_fusion_closes_selected_monad_source"],
            },
        ),
        check(
            "current same-source fields fail honestly",
            current == {
                "pic0_resolved_or_quotiented": False,
                "projector_retention_verified": False,
                "promotion_attempt_passes": False,
                "same_source_operator_source_verified": False,
                "selected_dotD_constructed": False,
                "selected_ordered_source_verified": False,
                "visible_green_schwarz_source_verified": False,
            },
            current,
        ),
        check(
            "patchwork shortcut blocked",
            no_patchwork["separate_constituents_do_not_define_same_source"] is True
            and no_patchwork["route_c_smoke_uses_lifted_flags_only"] is True
            and no_patchwork["green_schwarz_closure_is_curvature_level_only"] is True
            and no_patchwork["pic0_remains_invisible_to_closed_topology_cohomology_curvature"]
            is True,
            no_patchwork,
        ),
        check(
            "proof implication names selector closure",
            "Selected_Monad_Difference_L2_Source.v1" in implication["statement"]
            and any("Pic0" in line for line in implication["why"])
            and any("conditional uniqueness" in line for line in implication["then_existing_theorems_apply"]),
            implication,
        ),
        check(
            "no overclaim",
            guardrails["claims_unconditional_monad_selector_proved"] is False
            and guardrails["claims_selected_visible_operator_source"] is False
            and guardrails["claims_selected_D_E_dotD"] is False
            and guardrails["claims_pic0_resolved"] is False
            and guardrails["uses_lifted_flags_as_proof"] is False
            and guardrails["claims_full_SM_closure"] is False,
            guardrails,
        ),
        check(
            "note records same-source requirement",
            "SameSourceMonadGSOperatorFusionPacket.v1" in note
            and "Not by patchwork" in note
            and "single-source packet" in note,
            NOTE,
        ),
    ]

    print("\nSame-source monad/GS/operator fusion gate audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
