"""Audit the attempted fill of IwasawaTwistedSourcePromotionPacket.v1."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_twisted_source_packet_fill_attempt_certificate.json"
PACKET = CERT_DIR / "iwasawa_twisted_source_promotion_packet.attempt.json"
CARRIER = REPO / "candidate_data" / "iwasawa_projective_magnetic_carrier.meshN1.json"
PAPER = ROOT / "Iwasawa_Twisted_Source_Promotion_Packet_Fill_Attempt_v1.md"
SCRIPT = REPO / "scripts" / "attempt_fill_iwasawa_twisted_source_packet.py"
CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_projective_magnetic_carrier.py"


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


def fresh_projective_candidate() -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as temp_dir:
        path = Path(temp_dir) / "fresh_projective.json"
        code, output = run(
            [
                sys.executable,
                str(CONSTRUCTOR),
                "--mesh-N",
                "1",
                "--emit-candidate",
                str(path),
            ]
        )
        if code != 0:
            raise RuntimeError(output)
        return load_json(path)


def attempt_report() -> dict[str, Any]:
    code, output = run(
        [
            sys.executable,
            str(SCRIPT),
            "--packet",
            str(PACKET),
            "--carrier",
            str(CARRIER),
        ]
    )
    if code != 0:
        raise RuntimeError(output)
    return json.loads(output)


def main() -> None:
    cert = load_json(CERT)
    packet = load_json(PACKET)
    carrier = load_json(CARRIER)
    fresh_carrier = fresh_projective_candidate()
    report = attempt_report()
    paper = read(PAPER)
    script_text = read(SCRIPT)

    filled = cert.get("filled_fields", {})
    unfilled = cert.get("unfilled_fields", {})
    obstruction = cert.get("single_carrier_obstruction", {})
    block_resolution = cert.get("block_factorized_resolution", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "BLOCKED"
            if cert.get("status")
            in {
                "IWASAWA_TWISTED_SOURCE_PACKET_PARTIAL_FILL_BLOCKED",
                "IWASAWA_TWISTED_SOURCE_PACKET_PARTIAL_FILL_BLOCKED_SELECTED_SOURCE",
            }
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "attempt packet exists",
            "PASS"
            if packet.get("status")
            in {
                "CANDIDATE_BLOCKED_SELECTED_GERBE_MAP_AND_PROJECTORS_MISSING",
                "CANDIDATE_BLOCKED_SELECTED_GERBE_MAP_MISSING_BLOCK_SECTOR_MAPS_VALIDATED",
                "CANDIDATE_BLOCKED_SELECTED_CYCLES_GS_PROJECTORS_OPEN",
                "CANDIDATE_BLOCKED_VISIBLE_OPERATOR_SOURCE_SPECTRAL_PROJECTORS_OPEN",
            }
            else "FAIL",
            str(PACKET),
        ),
        Gate(
            "candidate carrier reproducible",
            "PASS"
            if carrier.get("prototype") == fresh_carrier.get("prototype")
            and carrier.get("generator_data") == fresh_carrier.get("generator_data")
            and carrier.get("metric_data") == fresh_carrier.get("metric_data")
            else "FAIL",
            str(CARRIER),
        ),
        Gate(
            "script records obstruction",
            "PASS"
            if contains_all(
                script_text,
                [
                    "Comm(X,Z)=C*I_3",
                    "rank_one_invariant_projector_possible",
                    "block_factorized_sector_maps",
                    "partial_selected_source_progress",
                    "single_carrier_rank_one_H_test",
                    "visible_twisted_s3_source_packet_gate_created",
                    "visible_twisted_s3_finite_cp_cancellation_closed",
                    "visible_twisted_s3_smooth_source_lift_gate_created",
                    "iwasawa_deligne_cover_gauge_reduction_closed",
                    "visible_twisted_s3_class_restriction_packet_gate_created",
                    "visible_twisted_s3_class_restriction_closed",
                ],
            )
            else "FAIL",
            str(SCRIPT),
        ),
        Gate(
            "fillable fields",
            "PASS" if all(filled.values()) else "FAIL",
            str(filled),
        ),
        Gate(
            "unfilled fields",
            "OPEN" if all(unfilled.values()) else "FAIL",
            str(unfilled),
        ),
        Gate(
            "promotion validator refuses packet",
            "PASS"
            if report.get("validator_results", {})
            .get("twisted_source_promotion_packet", {})
            .get("exit")
            == 1
            and report.get("verdict", {}).get("packet_passes_promotion_validator") is False
            else "FAIL",
            str(report.get("validator_results", {}).get("twisted_source_promotion_packet", {})),
        ),
        Gate(
            "projective mesh passes",
            "PASS"
            if report.get("validator_results", {}).get("projective_rhoE_mesh", {}).get("exit")
            == 0
            else "FAIL",
            str(report.get("validator_results", {}).get("projective_rhoE_mesh", {})),
        ),
        Gate(
            "metric passes",
            "PASS"
            if report.get("validator_results", {}).get("rhoE_metric", {}).get("exit") == 0
            else "FAIL",
            str(report.get("validator_results", {}).get("rhoE_metric", {})),
        ),
        Gate(
            "block sector maps pass",
            "PASS"
            if report.get("validator_results", {})
            .get("block_factorized_sector_maps", {})
            .get("exit")
            == 0
            and report.get("block_factorized_resolution", {}).get(
                "finite_sector_projectors_filled"
            )
            is True
            else "FAIL",
            str(report.get("block_factorized_resolution", {})),
        ),
        Gate(
            "single-carrier H sector fails",
            "PASS"
            if report.get("validator_results", {})
            .get("single_carrier_rank_one_H_test", {})
            .get("exit")
            == 1
            and report.get("commutant_obstruction", {}).get(
                "rank_one_invariant_projector_possible"
            )
            is False
            else "FAIL",
            str(report.get("commutant_obstruction", {})),
        ),
        Gate(
            "single-carrier obstruction recorded",
            "PASS"
            if obstruction.get("current_carrier_can_host_rank_one_H_projector") is False
            and "Comm(X,Z)=C*I_3" in obstruction.get("statement", "")
            else "FAIL",
            str(obstruction),
        ),
        Gate(
            "block resolution recorded",
            "PASS"
            if block_resolution.get("finite_sector_projectors_filled") is True
            and block_resolution.get("separate_higgs_line_validated") is True
            and block_resolution.get(
                "block_sector_projector_retention_for_selected_s3_source_closed"
            )
            is True
            and block_resolution.get(
                "coherent_spectral_projector_retention_still_requires_operator_source"
            )
            is True
            else "FAIL",
            str(block_resolution),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("packet_filled_as_far_as_current_evidence_allows") is True
            and verdict.get("promotion_packet_passes") is False
            and verdict.get("finite_block_factorized_sector_maps_validated") is True
            and verdict.get("current_projective_carrier_remains_unpromoted") is True
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records attempt",
            "PASS"
            if contains_all(
                paper,
                [
                    "Filled Fields",
                    "Unfilled Selected Source Fields",
                    "Comm(X,Z) = C*I_3",
                    "Block-Factorized Sector Maps",
                    "selected S3 class/restriction closure",
                    "complete selected visible cycle/worldvolume packet",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa twisted-source packet fill-attempt audit")
    print("================================================")
    print()
    print(f"attempt_status={report.get('status')}")
    print(
        "promotion_exit="
        f"{report.get('validator_results', {}).get('twisted_source_promotion_packet', {}).get('exit')}"
    )
    print(
        "rank_one_projector_possible="
        f"{report.get('commutant_obstruction', {}).get('rank_one_invariant_projector_possible')}"
    )
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
