"""Audit the Iwasawa block-factorized twisted packet candidate."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT = REPO / "certificates" / "iwasawa_block_factorized_twisted_packet_candidate_certificate.json"
PACKET = REPO / "candidate_data" / "iwasawa_block_factorized_twisted_packet.candidate.json"
PAPER = ROOT / "Iwasawa_Block_Factorized_Twisted_Packet_Candidate_v1.md"
VALIDATOR = REPO / "scripts" / "validate_iwasawa_block_factorized_twisted_packet.py"
ANALYZER = REPO / "scripts" / "analyze_iwasawa_block_factorized_twisted_packet.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def parse_block_report(output: str) -> dict[str, Any]:
    match = re.search(r"block_factorized_report=(\{.*\})", output)
    if not match:
        return {}
    return json.loads(match.group(1))


def analyzer_report() -> dict[str, Any]:
    code, output = run([sys.executable, str(ANALYZER)])
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def validator_report() -> tuple[int, dict[str, Any], str]:
    code, output = run([sys.executable, str(VALIDATOR), str(PACKET)])
    return code, parse_block_report(output), output


def main() -> None:
    cert = load_json(CERT)
    packet = load_json(PACKET)
    paper = read(PAPER)
    validator_code, validator, validator_output = validator_report()
    analysis = analyzer_report()
    calc = cert.get("calculation_results", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})
    family = validator.get("family_twist_block", {})
    projective = family.get("projective_report", {})
    higgs = validator.get("higgs_line_block", {})
    sector = validator.get("sector_partition", {})
    coupling = validator.get("coupling_rule", {})

    gates = [
        Gate(
            "certificate status",
            "PASS"
            if cert.get("status")
            == "IWASAWA_BLOCK_FACTORIZED_TWISTED_PACKET_CANDIDATE_VALIDATED_SELECTION_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate packet status",
            "PASS"
            if packet.get("status") == "CANDIDATE_BLOCK_FACTORIZED_VALIDATED_SELECTION_OPEN"
            else "FAIL",
            str(PACKET),
        ),
        Gate(
            "validator passes",
            "PASS"
            if validator_code == 0
            and validator.get("block_factorized_candidate_valid") is True
            else "FAIL",
            validator_output.splitlines()[-1] if validator_output.splitlines() else "",
        ),
        Gate(
            "family projective block",
            "PASS"
            if family.get("projective_validator_exit") == 0
            and projective.get("projective_gerbe_gluing_passes") is True
            and projective.get("central_twist_is_nontrivial") is True
            and projective.get("strict_vector_bundle_gluing_passes") is False
            else "FAIL",
            str(projective),
        ),
        Gate(
            "Higgs line block",
            "PASS"
            if higgs.get("rank_one_projector") is True
            and higgs.get("ordinary_line_strict_gluing_passes") is True
            else "FAIL",
            str(higgs),
        ),
        Gate(
            "sector partition",
            "PASS"
            if sector.get("covers_all_sm_slots") is True and sector.get("overlap") == []
            else "FAIL",
            str(sector),
        ),
        Gate(
            "rank-four shortcut rejected",
            "PASS"
            if coupling.get("single_rank4_scalar_projective_carrier_allowed") is False
            and coupling.get("same_twist_all_family_allowed_for_trivial_Higgs") is False
            and coupling.get("conjugate_orientation_pairing_required") is True
            and coupling.get("selected_sector_orientation_assignment_supplied") is False
            and analysis.get("naive_rank4_direct_sum_rejected") is True
            else "FAIL",
            str(coupling),
        ),
        Gate(
            "selected data remain open",
            "PASS"
            if analysis.get("selected_source_promotion_ready") is False
            and analysis.get("full_sm_data_ready") is False
            and coupling.get("selected_D_E_supplied") is False
            and coupling.get("primitive_C1_contractions_supplied") is False
            else "FAIL",
            str(analysis.get("remaining_selected_inputs")),
        ),
        Gate(
            "certificate calculation results",
            "PASS"
            if calc.get("block_factorized_candidate_valid") is True
            and calc.get("family_projective_gerbe_gluing_passes") is True
            and calc.get("family_strict_vector_bundle_gluing_passes") is False
            and calc.get("higgs_line_rank_one_projector") is True
            and calc.get("same_twist_all_family_allowed_for_trivial_Higgs") is False
            and calc.get("conjugate_orientation_pairing_required") is True
            and calc.get("selected_sector_orientation_assignment_supplied") is False
            and calc.get("single_rank4_scalar_projective_carrier_allowed") is False
            and calc.get("selected_source_promotion_ready") is False
            else "FAIL",
            str(calc),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("finite_block_architecture_closed") is True
            and verdict.get("selected_mtt_promotion_closed") is False
            and verdict.get("full_sm_closure_closed") is False
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "block-factorized packet schema",
                    "central_phase_histogram",
                    "selected Deligne/Cech gerbe",
                    "primitive C1 contractions",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa block-factorized twisted packet candidate audit")
    print("=======================================================")
    print()
    print(f"packet_validator_exit={analysis.get('packet_validator_exit')}")
    print(
        "family_nontrivial_corner_count="
        f"{analysis.get('family_nontrivial_corner_count')}"
    )
    print(f"finite_block_architecture_closed={verdict.get('finite_block_architecture_closed')}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
