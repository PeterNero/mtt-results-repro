"""Audit the V_alpha repo-update source frontier ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "analyze_valpha_repo_update_source_frontier.py"
CERT = ROOT / "certificates" / "valpha_repo_update_source_frontier_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "valpha_repo_update_source_frontier.candidate.json"
TABLE = ROOT / "candidate_data" / "valpha_repo_update_source_frontier" / "repo_update_frontier_table.json"
PAPER = ROOT / "proof_corpus" / "VAlpha_Repo_Update_Source_Frontier_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: object


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run_script() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run_script()
    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = read(PAPER)

    frontier = cert.get("repo_update_source_frontier", {})
    repos = frontier.get("repo_table", {})
    reduction = frontier.get("frontier_reduction", {})
    imported = frontier.get("imported_certificate_statuses", {})
    not_imported = frontier.get("not_imported_as_proof_data", {})
    closed = cert.get("closed_by_this_attempt", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    constants_dirty = repos.get("constants", {}).get("status_summary", {}).get("dirty")
    constants_checked = (
        reduction.get("constants_repo_head_checked") is True
        and reduction.get("constants_repo_dirty_provisional_only") == constants_dirty
    )
    gr_dirty = repos.get("gr", {}).get("status_summary", {}).get("dirty")
    gr_checked = (
        reduction.get("gr_repo_head_checked") is True
        and reduction.get("gr_repo_dirty_provisional_only") == gr_dirty
    )
    qa_dirty = repos.get("qa_su3_packet", {}).get("status_summary", {}).get("dirty")
    qa_checked = (
        reduction.get("qa_su3_packet_head_checked") is True
        and reduction.get("qa_su3_internal_logdet_bridge_status_found") is True
        and reduction.get("qa_su3_packet_dirty_provisional_only") == qa_dirty
    )
    sm_dirty = repos.get("sm_parity", {}).get("status_summary", {}).get("dirty")
    sm_checked = (
        repos.get("sm_parity", {}).get("present") is True
        and reduction.get("sm_parity_repo_dirty_provisional_only") == sm_dirty
    )

    expected_status = (
        "VALPHA_REPO_UPDATE_SOURCE_FRONTIER_REDUCED_TO_SOURCE_ORIGIN_FINITE_EMISSION_BRIDGE"
    )

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("table exists", "PASS" if TABLE.exists() else "FAIL", TABLE),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status expected",
            "PASS" if cert.get("status") == expected_status else "FAIL",
            cert.get("status"),
        ),
        Gate("candidate mirrors cert", "PASS" if candidate == cert else "FAIL", candidate.get("status")),
        Gate("table mirrors embedded", "PASS" if table == frontier else "FAIL", table.get("schema")),
        Gate(
            "all repos present",
            "PASS" if set(repos) == {"q79", "constants", "gr", "qa_su3_packet", "sm_parity"}
            and all(row.get("present") is True for row in repos.values())
            else "FAIL",
            repos,
        ),
        Gate(
            "constants checked provisional if dirty",
            "OPEN" if constants_checked and constants_dirty else "PASS" if constants_checked else "FAIL",
            repos.get("constants", {}),
        ),
        Gate(
            "gr checked provisional if dirty",
            "OPEN" if gr_checked and gr_dirty else "PASS" if gr_checked else "FAIL",
            repos.get("gr", {}),
        ),
        Gate(
            "qa packet checked provisional if dirty",
            "OPEN" if qa_checked and qa_dirty else "PASS" if qa_checked else "FAIL",
            repos.get("qa_su3_packet", {}),
        ),
        Gate(
            "sm parity boundary",
            "OPEN" if sm_checked and sm_dirty else "PASS" if sm_checked else "FAIL",
            repos.get("sm_parity", {}),
        ),
        Gate(
            "q79 closed layers imported",
            "PASS"
            if reduction.get("q79_central_neutral_lane_obstructed_reduced_model") is True
            and reduction.get("q79_yoneda_promoted_to_AH_conditional") is True
            else "FAIL",
            reduction,
        ),
        Gate(
            "sm parity statuses used as frontier",
            "PASS"
            if imported.get("sm_nonsplit_or_routec", {}).get("status")
            == "MTT_SELECTED_NONSPLIT_RANK2_OR_ROUTEC_SAME_SOURCE_PACKET_REDUCED_TO_SYMMETRY_BREAKING_SOURCE"
            and imported.get("sm_symmetry_breaker", {}).get("status")
            == "MTT_SAME_SOURCE_SYMMETRY_BREAKING_SOURCE_REDUCED_TO_ORIENTATION_CARRYING_DE_DOTD_PACKET"
            and imported.get("sm_routec_origin", {}).get("status")
            == "MTT_ROUTEC_SELECTED_SOURCE_ORIGIN_LEMMA_REDUCED_TO_FINITE_EMISSION_MORPHISM"
            else "FAIL",
            imported,
        ),
        Gate(
            "proof-data import guard",
            "PASS"
            if not_imported.get("sm_parity_uncommitted_packets")
            == reduction.get("sm_parity_repo_dirty_provisional_only")
            and not_imported.get("sm_parity_frontier_status_not_imported_as_proof") is True
            and not_imported.get("constants_uncommitted_packets")
            == reduction.get("constants_repo_dirty_provisional_only")
            and not_imported.get("gr_uncommitted_packets")
            == reduction.get("gr_repo_dirty_provisional_only")
            and not_imported.get("qa_su3_packet_uncommitted_packets")
            == reduction.get("qa_su3_packet_dirty_provisional_only")
            and all(
                not_imported.get(key) is True
                for key in [
                    "selected_visible_valpha_source",
                    "selected_Pic0_rule",
                    "selected_D_E_dotD_Riesz_Green",
                    "selected_HYM_or_RouteC_values",
                    "primitive_C1_contractions",
                    "full_SM_closure",
                ]
            )
            else "FAIL",
            not_imported,
        ),
        Gate(
            "closed attempt flags",
            "PASS"
            if closed.get("all_local_repos_checked") is True
            and closed.get("constants_update_boundary_recorded") is True
            and closed.get("safe_sm_parity_import_boundary_recorded") is True
            and closed.get("next_frontier_reduced_to_source_origin_finite_emission_bridge") is True
            else "FAIL",
            closed,
        ),
        Gate(
            "still open guarded",
            "OPEN"
            if still_open.get("selected_visible_valpha_source") is True
            and still_open.get("selected_Pic0_rule") is True
            and still_open.get("finite_emission_morphism_Phi_fin") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            still_open,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "paper records frontier and caveats",
            "PASS"
            if contains_all(
                paper,
                [
                    "VAlpha Repo-Update Source Frontier",
                    "sm_parity",
                    "provisional",
                    "orientation-carrying D_E/dotD",
                    "finite emission morphism Phi_fin",
                    "not imported as proof data",
                    "Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("V_alpha repo-update source frontier audit")
    print("=========================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:<{width}}  {gate.status:<{status_width}}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        print("\nFailures")
        print("--------")
        for failure in failures:
            print(f"- {failure.label}: {failure.detail}")
        return 1

    print("\nResult: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
