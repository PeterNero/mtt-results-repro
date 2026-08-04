"""Audit the q79 V_alpha source-origin / finite-emission bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "analyze_q79_valpha_source_origin_finite_emission_bridge.py"
CERT = ROOT / "certificates" / "q79_valpha_source_origin_finite_emission_bridge_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_valpha_source_origin_finite_emission_bridge.candidate.json"
CONTRACT = (
    ROOT
    / "candidate_data"
    / "q79_valpha_source_origin_finite_emission_bridge"
    / "selected_payload_contract.json"
)
PAPER = ROOT / "proof_corpus" / "Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1.md"


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
    contract = load(CONTRACT)
    paper = read(PAPER)

    expected_status = (
        "Q79_VALPHA_SOURCE_ORIGIN_FINITE_EMISSION_BRIDGE_CONSTRUCTED_SELECTED_PAYLOAD_OPEN"
    )
    q79 = cert.get("q79_source_side", {})
    finite = cert.get("finite_emission_schema", {})
    shape = finite.get("shape_gates", {})
    flags = finite.get("selected_payload_flags", {})
    alpha = cert.get("alpha1_driver_bridge", {})
    alpha_support = alpha.get("support_gates", {})
    alpha_missing = alpha.get("missing_selected_values", {})
    closed = cert.get("closed_by_this_attempt", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    sm = cert.get("sm_parity_status_evidence_only", {})

    selected_flags_expected_open = (
        flags.get("route_c_residual_selected_source") is False
        and flags.get("rhoE_selected_by_mtt") is False
        and flags.get("rhoE_nonidentity") is False
        and flags.get("de_action_selected_source") is False
        and flags.get("riesz_gap_selected_source") is False
        and flags.get("reduced_green_selected_source") is False
        and flags.get("dotd_selected_source") is False
        and flags.get("dotd_alpha1_driver") is False
    )

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1200]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", CERT),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", CANDIDATE),
        Gate("contract exists", "PASS" if CONTRACT.exists() else "FAIL", CONTRACT),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", PAPER),
        Gate(
            "status expected",
            "PASS" if cert.get("status") == expected_status else "FAIL",
            cert.get("status"),
        ),
        Gate("candidate mirrors cert", "PASS" if candidate == cert else "FAIL", candidate.get("status")),
        Gate(
            "contract mirrors embedded",
            "PASS" if contract == cert.get("selected_payload_contract") else "FAIL",
            contract.get("name"),
        ),
        Gate(
            "q79 source side anchored",
            "PASS"
            if q79.get("central_neutral_obstructed") is True
            and q79.get("ah_yoneda_conditional") is True
            and q79.get("frontier_reduces_to_finite_emission") is True
            and q79.get("frontier_imports_dirty_adjacent_as_provisional_only") is True
            else "FAIL",
            q79,
        ),
        Gate("finite shape gates closed", "PASS" if shape and all(shape.values()) else "FAIL", shape),
        Gate(
            "identity smoke rejected",
            "PASS" if finite.get("identity_rhoE_smoke_rejected") is True else "FAIL",
            finite,
        ),
        Gate(
            "selected payload still open",
            "OPEN" if selected_flags_expected_open else "FAIL",
            flags,
        ),
        Gate(
            "alpha1 support closed",
            "PASS" if alpha_support and all(alpha_support.values()) else "FAIL",
            alpha_support,
        ),
        Gate(
            "alpha1 selected values missing",
            "OPEN" if alpha_missing and all(alpha_missing.values()) else "FAIL",
            alpha_missing,
        ),
        Gate(
            "sm parity evidence only",
            "OPEN"
            if sm.get("present") is True
            and sm.get("imported_as_proof_data") is False
            and sm.get("status_summary", {}).get("dirty") is True
            else "PASS"
            if sm.get("present") is True
            and sm.get("imported_as_proof_data") is False
            and sm.get("status_summary", {}).get("dirty") is False
            else "FAIL",
            sm,
        ),
        Gate(
            "closed reduction flags",
            "PASS"
            if closed.get("q79_source_side_anchored") is True
            and closed.get("finite_emission_codomain_schema_closed") is True
            and closed.get("identity_rhoE_smoke_rejected") is True
            and closed.get("alpha1_support_and_rank_test_closed") is True
            and closed.get("source_origin_and_alpha1_reduced_to_one_payload") is True
            and closed.get("target_fitting_excluded") is True
            else "FAIL",
            closed,
        ),
        Gate(
            "remaining blockers guarded",
            "OPEN"
            if open_items.get("selected_PhiFin_alpha1_payload") is True
            and open_items.get("selected_visible_valpha_source_origin") is True
            and open_items.get("finite_C1_numeric_response_matrices") is True
            and open_items.get("full_SM_closure") is True
            else "FAIL",
            open_items,
        ),
        Gate(
            "guardrails",
            "PASS" if guardrails and all(value is False for value in guardrails.values()) else "FAIL",
            guardrails,
        ),
        Gate(
            "theorem and no closure claim",
            "PASS"
            if cert.get("theorem", {}).get("proved") is True
            and cert.get("closure_claimed") is False
            and cert.get("target_fitting_used") is False
            else "FAIL",
            cert.get("theorem"),
        ),
        Gate(
            "paper records bridge",
            "PASS"
            if contains_all(
                paper,
                [
                    "Q79 VAlpha Source-Origin and Finite-Emission Bridge",
                    "selected Phi_fin alpha1 payload",
                    "shape gates pass",
                    "identity smoke",
                    "Selected Payload Flags",
                    "Alpha1 Driver Bridge",
                    "Q79_Selected_PhiFin_Alpha1_Payload_v1",
                ],
            )
            else "FAIL",
            PAPER,
        ),
    ]

    print("Q79 V_alpha source-origin finite-emission bridge audit")
    print("=====================================================")
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
