"""Audit the exact q79 all-space, u1=1 D-augmented finite cover."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFIER = ROOT / "scripts" / "certify_q79_Ronly_fixed_u1_all_spaces_D_cover.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_FixedU1_AllSpaces_D_Augmented_Cover_v1.json"
THEOREM = Path(__file__).with_name(
    "Q79_Ronly_FixedU1_AllSpaces_D_Augmented_Cover_v1.md"
)
SPACE_AUDITS = [
    Path(__file__).with_name("q79_Ronly_fixed_u1_space5_D_augmented_cover_audit.py"),
    Path(__file__).with_name("q79_Ronly_fixed_u1_space6_D_augmented_cover_audit.py"),
]


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def main() -> None:
    required = [CERTIFIER, CERTIFICATE, THEOREM, *SPACE_AUDITS]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    audit_results = []
    for audit in SPACE_AUDITS:
        completed = subprocess.run(
            [sys.executable, str(audit)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        audit_results.append((audit, completed))

    with tempfile.TemporaryDirectory(prefix="q79-all-spaces-u1-D-cover-") as directory:
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
    canonical = regenerated.get("canonical_union", {})
    signed = regenerated.get("signed_union", {})
    boundary = regenerated.get("claim_boundary", {})
    checks = regenerated.get("checks", {})
    theorem = THEOREM.read_text(encoding="utf-8")
    gates = [
        Gate("all union artifacts present", "PASS", f"files={len(required)}"),
        Gate(
            "both component audits pass",
            "PASS" if all(row.returncode == 0 for _, row in audit_results) else "FAIL",
            ", ".join(f"{path.name}:{row.returncode}" for path, row in audit_results),
        ),
        Gate(
            "union certifier reruns",
            "PASS" if completed.returncode == 0 else "FAIL",
            completed.stdout[-180:].strip(),
        ),
        Gate(
            "certificate reproduces",
            "PASS" if regenerated == committed else "FAIL",
            "committed == regenerated",
        ),
        Gate(
            "exact union status",
            "PASS"
            if regenerated.get("status")
            == "EXACT_F101_ALL_INVERSE_ROOT_U1_1_FULL_RD_SLICE_CLOSED"
            else "FAIL",
            "all four inverse-root u1=1 slices",
        ),
        Gate(
            "canonical accounting",
            "PASS"
            if canonical.get("canonical_endpoint_fibers") == 20_000
            and canonical.get("literal_R_unit_fibers") == 19_989
            and canonical.get("literal_full_R_y_D_unit_fibers") == 11
            else "FAIL",
            "20000 = 19989 + 11",
        ),
        Gate(
            "signed exhaustion",
            "PASS" if signed.get("excluded_endpoint_fibers") == 40_000 else "FAIL",
            "40000 fibers",
        ),
        Gate(
            "finite-slice accounting",
            "PASS"
            if signed.get("closed_space_class_u1_slices") == 4
            and signed.get("finite_strategy_space_class_u1_slices") == 400
            and boundary.get("finite_slice_accounting") == "4/400"
            else "FAIL",
            "4/400",
        ),
        Gate(
            "all deterministic checks",
            "PASS" if len(checks) == 10 and all(checks.values()) else "FAIL",
            f"{sum(bool(value) for value in checks.values())}/10",
        ),
        Gate(
            "global boundary retained",
            "PASS" if boundary.get("global_chart_accounting") == "remains 138/140" else "FAIL",
            str(boundary.get("not_closed", "")),
        ),
        Gate(
            "zero fit parameters",
            "PASS" if regenerated.get("new_continuous_fit_parameters") == 0 else "FAIL",
            "zero",
        ),
        Gate(
            "theorem states exact tier",
            "PASS"
            if "four of the 400 finite" in theorem
            and "global chart accounting therefore remains `138/140`" in theorem
            and "No continuous fit parameter" in theorem
            else "FAIL",
            str(THEOREM),
        ),
    ]

    print("q79 all-space fixed-u1 D-augmented finite-cover audit")
    print("========================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
