"""Audit the visible V_alpha Chern/Bianchi source-packet candidate ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "build_visible_valpha_chern_bianchi_source_packet_candidates.py"
CANDIDATE = REPO / "candidate_data" / "visible_valpha_chern_bianchi_source_packet_candidates.candidate.json"
CERT = REPO / "certificates" / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json"
PAPER = ROOT / "Visible_VAlpha_Chern_Bianchi_Source_Packet_Candidates_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def candidate_by_id(candidates: list[dict[str, Any]], candidate_id: str) -> dict[str, Any]:
    for candidate in candidates:
        if candidate.get("id") == candidate_id:
            return candidate
    return {}


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)

    prerequisites = cert.get("prerequisite_gates", {})
    interface = cert.get("source_packet_interface", {})
    candidates = cert.get("candidate_ranking", [])
    rank2 = candidate_by_id(candidates, "rank2_non_split_extension_preferred_L_1_-2_0")
    abelian = candidate_by_id(candidates, "abelian_two_line_flux_row")
    route_c = candidate_by_id(candidates, "direct_route_c_finite_hym_strominger_solve")
    twisted = candidate_by_id(candidates, "twisted_s3_or_gerbe_source_transfer")
    best = cert.get("best_current_route", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    visible_fields = interface.get("visible_required_fields", [])

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status candidate ledger",
            "PASS"
            if cert.get("status")
            == "VISIBLE_VALPHA_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_SOURCE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("calculation_results") == cert.get("calculation_results")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "input gates present",
            "PASS"
            if all(prerequisites.values())
            and prerequisites.get("rank2_extension_route") is True
            and prerequisites.get("l2_h1_gate") is True
            and prerequisites.get("integral_alpha1_row") is True
            and prerequisites.get("terminal_g3_dual_extension_sign") is True
            else "FAIL",
            str(prerequisites),
        ),
        Gate(
            "interface has hard source fields",
            "PASS"
            if interface.get("schema") == "VisibleVAlphaSourcePacket.v1"
            and contains_all(
                "\n".join(visible_fields),
                [
                    "finite_Cech_or_Dolbeault_cochain_packet",
                    "nonzero_closed_nonexact_Ext_vector",
                    "HYM_or_Strominger_or_Route_C_residual_certificate",
                    "same_source_D_E_operator_block",
                    "same_source_dotD_alpha1_response",
                    "Riesz_projector_and_reduced_Green_packet",
                ],
            )
            else "FAIL",
            str(interface),
        ),
        Gate(
            "rank2 primary branch",
            "PASS"
            if rank2.get("live_role") == "primary_next_branch"
            and rank2.get("topological_target", {}).get("l_vector_abc") == [1, -2, 0]
            and rank2.get("topological_target", {}).get("c2_V_alpha") == [4, 0, 0]
            and rank2.get("already_audited_support", {}).get(
                "terminal_g3_dual_sign_and_order_closed"
            )
            is True
            and rank2.get("promotion_status") == "OPEN"
            else "FAIL",
            str(rank2),
        ),
        Gate(
            "rank2 missing source fields marked open",
            "OPEN"
            if rank2.get("source_packet_fields", {})
            .get("line_bundle_cochain_packet", {})
            .get("status")
            == "OPEN"
            and rank2.get("source_packet_fields", {})
            .get("nonzero_ext_class", {})
            .get("status")
            == "OPEN"
            and rank2.get("source_packet_fields", {})
            .get("same_source_operator_data", {})
            .get("status")
            == "OPEN"
            else "FAIL",
            str(rank2.get("source_packet_fields", {})),
        ),
        Gate(
            "abelian row demoted",
            "PASS"
            if abelian.get("promotion_status") == "REJECTED_AS_FINAL_SOURCE"
            and abelian.get("topological_target", {}).get("standard_chern_character_row")
            == [4, 0, 0]
            and abelian.get("live_role") == "Chern_Bianchi_support_template_only"
            else "FAIL",
            str(abelian),
        ),
        Gate(
            "fallbacks retained",
            "OPEN"
            if route_c.get("promotion_status") == "OPEN"
            and twisted.get("promotion_status") == "OPEN"
            and route_c.get("live_role") == "parallel_fallback_branch"
            and twisted.get("live_role") == "conditional_support_branch"
            else "FAIL",
            str({"route_c": route_c, "twisted": twisted}),
        ),
        Gate(
            "best route executable target",
            "PASS"
            if best.get("candidate_id") == "rank2_non_split_extension_preferred_L_1_-2_0"
            and best.get("next_validator") == "scripts/validate_visible_rank2_l2_cohomology.py"
            and len(best.get("closed_before_next_step", [])) == 3
            else "FAIL",
            str(best),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("candidate_count") == 4
            and calc.get("primary_candidate_is_rank2_non_split_extension") is True
            and calc.get("terminal_g3_sign_order_closed_before_source_selection") is True
            and calc.get("selected_visible_valpha_source_constructed") is False
            and calc.get("actual_H1_X_L_squared_computed") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closes hierarchy only",
            "PASS"
            if closes.get("visible_valpha_candidate_hierarchy") is True
            and closes.get("exact_source_packet_fields_for_promotion") is True
            and closes.get("direct_abelian_shortcut_demoted_to_support_template") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("compute_actual_h1_for_L_squared") is True
            and still_open.get("prove_non_split_extension_stability") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records ledger",
            "PASS"
            if contains_all(
                paper,
                [
                    "rank-two non-split extension",
                    "terminal `g3` sign/order ambiguity is now closed",
                    "abelian row is support, not the source",
                    "VisibleVAlphaSourcePacket.v1",
                    "H^1(X,L^2)",
                    "same-source D_E/dotD/Riesz/Green",
                    "full SM closure",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible V_alpha Chern/Bianchi source-packet candidate audit")
    print("===========================================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
