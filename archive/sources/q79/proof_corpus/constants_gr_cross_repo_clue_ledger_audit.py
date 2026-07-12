"""Audit the constants/GR cross-repo clue ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_constants_gr_cross_repo_clues.py"
CANDIDATE = REPO / "candidate_data" / "constants_gr_cross_repo_clues.candidate.json"
CERT = REPO / "certificates" / "constants_gr_cross_repo_clues_certificate.json"
PAPER = ROOT / "Constants_GR_CrossRepo_Clue_Ledger_v1.md"


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


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)

    statuses = cert.get("imported_statuses", {})
    imports = cert.get("useful_imports_for_q79_sm_closure", {})
    not_imported = cert.get("not_imported_as_proof_data", {})
    calc = cert.get("calculation_results", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status clue ledger",
            "PASS"
            if cert.get("status") == "CONSTANTS_GR_CROSS_REPO_CLUES_FORMULATED_IMPORTS_METHOD_NOT_DATA"
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
            "constants statuses imported",
            "PASS"
            if statuses.get("constants_operator_packet_interface")
            == "QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_INTERFACE_BUILT_VALUES_OPEN"
            and statuses.get("constants_operator_packet_fill_attempt")
            == "QA_SU3_COLOR_BUNDLE_OPERATOR_PACKET_FILL_ATTEMPT_PARTIAL_SOURCE_OPEN"
            else "FAIL",
            str(statuses),
        ),
        Gate(
            "gr statuses imported",
            "PASS"
            if statuses.get("gr_stf_hessian_form")
            == "SELECTED_STF_HESSIAN_FORM_CLOSED_POSITIVE_SCALE_OPEN"
            and statuses.get("gr_stf_scale_to_geff")
            == "STF_HESSIAN_SCALE_TIED_TO_GEFF_ABSOLUTE_NORMALIZATION_OPEN"
            else "FAIL",
            str(statuses),
        ),
        Gate(
            "useful method imports",
            "PASS"
            if imports.get("selected_source_packet_discipline", {}).get("import_as_method")
            is True
            and imports.get("same_branch_source_guardrail", {}).get("import_as_method")
            is True
            and imports.get("constructive_source_candidate_search", {}).get("import_as_method")
            is True
            and imports.get("target_source_separation", {}).get("import_as_method")
            is True
            else "FAIL",
            str(imports),
        ),
        Gate(
            "proof data not imported",
            "PASS"
            if all(not_imported.values())
            and not_imported.get("H1_X_L_squared_value") is True
            and not_imported.get("selected_nonzero_Ext_class") is True
            and not_imported.get("log2008_as_full_threshold_or_SM_closure") is True
            else "FAIL",
            str(not_imported),
        ),
        Gate(
            "calculation scoped",
            "PASS"
            if calc.get("constants_repo_checked") is True
            and calc.get("gr_repo_checked") is True
            and calc.get("qa_su3_packet_repo_checked") is True
            and calc.get("qa_su3_internal_reduced_logdet_status_found") is True
            and calc.get("direct_H1_or_Cech_data_found") is False
            and calc.get("useful_interface_discipline_found") is True
            and calc.get("useful_constructive_source_packet_search_found") is True
            else "FAIL",
            str(calc),
        ),
        Gate(
            "closes cross-repo check",
            "PASS"
            if closes.get("cross_repo_update_check") is True
            and closes.get("safe_import_boundary") is True
            and closes.get("next_visible_valpha_packet_requirements_refined") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("fill_visible_rank2_l2_cohomology_template") is True
            and still_open.get("build_selected_visible_valpha_source_packet") is True
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
            "qa log2008 status scoped",
            "PASS"
            if imports.get("qa_su3_internal_reduced_packet_status", {}).get("value")
            == "log(2008)"
            and imports.get("qa_su3_internal_reduced_packet_status", {}).get("closed_scope")
            == "internal reduced Qa/SU3 determinant only"
            else "FAIL",
            str(imports.get("qa_su3_internal_reduced_packet_status")),
        ),
        Gate(
            "verdict next action",
            "PASS"
            if "Visible_VAlpha_Strominger_HYM_Source_Packet" in verdict.get("next_action", "")
            and "Chern/Bianchi" in verdict.get("next_action", "")
            and "no direct H^1(X,L^2)" in verdict.get("honest_answer", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records boundary",
            "PASS"
            if contains_all(
                paper,
                [
                    "proof discipline",
                    "source certificate",
                    "candidate Chern/Bianchi source packets",
                    "target/source separation",
                    "What We Must Not Import",
                    "H^1(X,L^2) value",
                    "visible `V_alpha` selected-source packet",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Constants/GR cross-repo clue ledger audit")
    print("=========================================")
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
