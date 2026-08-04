"""Audit the exact q79 space-6, u1=1 D-augmented finite cover."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFIER = ROOT / "scripts" / "certify_q79_Ronly_fixed_u1_space6_D_cover.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_FixedU1_Space6_D_Augmented_Cover_v1.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_FixedU1_Space6_D_Augmented_Cover_v1.md")
DATA = ROOT / "candidate_data" / "q79_Ronly_fixed_u1_space6_D_cover"
EXPECTED_FALLBACKS = {
    (1, 47, 81),
    (2, 32, 86),
    (2, 46, 61),
    (2, 47, 43),
}


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def main() -> None:
    line_packets = sorted((DATA / "line_packets").glob("*.packet.json"))
    full_packets = sorted((DATA / "full_RD_packets").glob("*.full_RD.packet.json"))
    required = [CERTIFIER, CERTIFICATE, THEOREM, *line_packets, *full_packets]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="q79-space6-u1-D-cover-") as directory:
        output = Path(directory) / "certificate.json"
        completed = subprocess.run(
            [sys.executable, str(CERTIFIER), "--output", str(output)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        regenerated = (
            json.loads(output.read_text(encoding="utf-8"))
            if completed.returncode == 0 and output.is_file()
            else {}
        )

    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    cover = regenerated.get("canonical_cover", {})
    signed = regenerated.get("signed_closure", {})
    boundary = regenerated.get("claim_boundary", {})
    fallbacks = {
        (int(row["scalar_class"]), int(row["a"]), int(row["v"]))
        for row in regenerated.get("fallback_witnesses", [])
    }
    checks = regenerated.get("checks", {})
    gates = [
        Gate("all frozen artifacts present", "PASS", f"files={len(required)}"),
        Gate("100 canonical line packets", "PASS" if len(line_packets) == 100 else "FAIL", str(len(line_packets))),
        Gate("four full-parent packets", "PASS" if len(full_packets) == 4 else "FAIL", str(len(full_packets))),
        Gate(
            "certifier reruns",
            "PASS" if completed.returncode == 0 else "FAIL",
            completed.stdout[-180:].strip(),
        ),
        Gate(
            "certificate reproduces",
            "PASS" if regenerated == committed else "FAIL",
            "committed == regenerated",
        ),
        Gate(
            "exact status",
            "PASS"
            if regenerated.get("status") == "EXACT_F101_SPACE6_U1_1_FULL_RD_SLICE_CLOSED"
            else "FAIL",
            "space6/u1=1 finite grid",
        ),
        Gate(
            "canonical accounting",
            "PASS"
            if cover.get("canonical_line_count") == 100
            and cover.get("canonical_endpoint_fiber_count") == 10_000
            and cover.get("literal_R_unit_fibers") == 9_996
            and cover.get("full_parent_fallback_fibers") == 4
            else "FAIL",
            "10000 = 9996 + 4",
        ),
        Gate(
            "exact fallback set",
            "PASS" if fallbacks == EXPECTED_FALLBACKS else "FAIL",
            str(sorted(fallbacks)),
        ),
        Gate(
            "signed exhaustion",
            "PASS" if signed.get("excluded_endpoint_fibers") == 20_000 else "FAIL",
            "20000 fibers",
        ),
        Gate(
            "all deterministic checks",
            "PASS" if len(checks) == 13 and all(checks.values()) else "FAIL",
            f"{sum(bool(value) for value in checks.values())}/13",
        ),
        Gate(
            "zero fit parameters",
            "PASS" if regenerated.get("new_continuous_fit_parameters") == 0 else "FAIL",
            "zero",
        ),
        Gate(
            "global boundary retained",
            "PASS" if boundary.get("global_chart_accounting") == "remains 138/140" else "FAIL",
            str(boundary.get("not_closed", "")),
        ),
        Gate(
            "theorem distinguishes rational grid",
            "PASS"
            if "not a symbolic proof for" in theorem
            and "global chart accounting\ntherefore remains `138/140`" in theorem
            and "No continuous fit parameter" in theorem
            else "FAIL",
            str(THEOREM),
        ),
    ]

    print("q79 space-6 fixed-u1 D-augmented finite-cover audit")
    print("======================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
