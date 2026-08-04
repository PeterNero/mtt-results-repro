"""Audit the first q79 fixed-u1 R-only exception and its exact D closure."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_fixed_u1_exceptional_line"
PARENTS = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
D_SCRIPT = ROOT / "scripts" / "verify_q79_Ronly_symbolic_exception_D_unit.py"
SIGN_SCRIPT = ROOT / "scripts" / "verify_q79_inverse_root_v_sign_involution.py"
D_CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_FixedU1_Exceptional_Line_D_Closure_v1.json"
SIGN_CERTIFICATE = ROOT / "certificates" / "Q79_Inverse_Root_V_Sign_Involution_v1.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_FixedU1_Exceptional_Line_D_Closure_v1.md")
STEM = "space5_class1_u1_001_a_018_symbolic_v"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def run(command: list[str]) -> tuple[subprocess.CompletedProcess[str], dict]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = Path(command[-1])
    packet = (
        json.loads(output.read_text(encoding="utf-8"))
        if completed.returncode == 0 and output.is_file()
        else {}
    )
    return completed, packet


def main() -> None:
    parent_paths = [
        PARENTS / f"space_{space}_h0_g0_class{scalar_class}_inverse_root.msolve.in"
        for space in (5, 6)
        for scalar_class in (1, 2)
    ]
    data_paths = [
        DATA / f"{STEM}.input.packet.json",
        DATA / f"{STEM}.msolve.in",
        DATA / f"{STEM}.msolve.out",
        DATA / f"{STEM}.msolve.log",
    ]
    required = [
        D_SCRIPT,
        SIGN_SCRIPT,
        D_CERTIFICATE,
        SIGN_CERTIFICATE,
        THEOREM,
        *parent_paths,
        *data_paths,
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="q79-exceptional-line-D-") as directory:
        temporary = Path(directory)
        d_output = temporary / "D_certificate.json"
        sign_output = temporary / "sign_certificate.json"
        d_completed, regenerated_d = run(
            [
                sys.executable,
                str(D_SCRIPT),
                "--parent",
                str(parent_paths[0].relative_to(ROOT)),
                "--symbolic-input",
                str(data_paths[1].relative_to(ROOT)),
                "--input-packet",
                str(data_paths[0].relative_to(ROOT)),
                "--basis-output",
                str(data_paths[2].relative_to(ROOT)),
                "--basis-log",
                str(data_paths[3].relative_to(ROOT)),
                "--space",
                "5",
                "--output",
                str(d_output),
            ]
        )
        sign_command = [sys.executable, str(SIGN_SCRIPT)]
        for path in parent_paths:
            sign_command.extend(["--input", str(path.relative_to(ROOT))])
        sign_command.extend(["--output", str(sign_output)])
        sign_completed, regenerated_sign = run(sign_command)

    committed_d = json.loads(D_CERTIFICATE.read_text(encoding="utf-8"))
    committed_sign = json.loads(SIGN_CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    d_checks = regenerated_d.get("checks", {})
    sign_checks = regenerated_sign.get("checks", {})
    quotient = regenerated_d.get("quotient_algebra", {})
    witness = regenerated_d.get("unit_witness", {})
    exhaustion = regenerated_sign.get("finite_exhaustion", {})
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate(
            "D certifier reruns",
            "PASS" if d_completed.returncode == 0 else "FAIL",
            d_completed.stdout[-160:].strip(),
        ),
        Gate(
            "sign certifier reruns",
            "PASS" if sign_completed.returncode == 0 else "FAIL",
            sign_completed.stdout[-160:].strip(),
        ),
        Gate(
            "D certificate reproduces",
            "PASS" if regenerated_d == committed_d else "FAIL",
            "committed == regenerated",
        ),
        Gate(
            "sign certificate reproduces",
            "PASS" if regenerated_sign == committed_sign else "FAIL",
            "committed == regenerated",
        ),
        Gate(
            "D status",
            "PASS"
            if regenerated_d.get("status")
            == "EXACT_R_ONLY_DOUBLE_POINT_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D"
            else "FAIL",
            "scheme-theoretic D closure",
        ),
        Gate(
            "double-point quotient",
            "PASS"
            if quotient.get("q_coefficients") == [5, 90, 1]
            and quotient.get("support_root") == 56
            and quotient.get("length") == 2
            and quotient.get("reduced") is False
            else "FAIL",
            "F101[v]/((v-56)^2)",
        ),
        Gate(
            "all exact D checks",
            "PASS" if len(d_checks) == 11 and all(d_checks.values()) else "FAIL",
            f"{sum(bool(value) for value in d_checks.values())}/11",
        ),
        Gate(
            "D remainder",
            "PASS"
            if witness.get("parent_row") == 18
            and witness.get("D_remainder_coefficients") == [100, 97]
            else "FAIL",
            "D18=100+97v",
        ),
        Gate(
            "Bezout identity",
            "PASS"
            if witness.get("q_multiplier_coefficients") == [68]
            and witness.get("D_multiplier_coefficients") == [36, 17]
            and witness.get("identity_coefficients") == [1]
            else "FAIL",
            "68q+(36+17v)D18=1",
        ),
        Gate(
            "sign status",
            "PASS"
            if regenerated_sign.get("status")
            == "EXACT_FULL_PARENT_SIGN_INVOLUTION_AND_CANONICAL_A_COVER"
            else "FAIL",
            "complete parent involution",
        ),
        Gate(
            "all exact sign checks",
            "PASS" if len(sign_checks) == 9 and all(sign_checks.values()) else "FAIL",
            f"{sum(bool(value) for value in sign_checks.values())}/9",
        ),
        Gate(
            "sign exhaustion",
            "PASS"
            if exhaustion.get("scalar_selection_checks") == 200
            and exhaustion.get("line_point_checks") == 20_000
            and exhaustion.get("canonical_representatives") == list(range(1, 51))
            else "FAIL",
            "200 scalar cases; 20,000 line points",
        ),
        Gate(
            "no fit parameters",
            "PASS"
            if regenerated_d.get("new_continuous_fit_parameters") == 0
            and regenerated_sign.get("new_continuous_fit_parameters") == 0
            else "FAIL",
            "zero",
        ),
        Gate(
            "claim boundary saved",
            "PASS"
            if "does not classify other `a`" in theorem
            and "must finish" in theorem
            and "No continuous fit parameter" in theorem
            else "FAIL",
            str(THEOREM),
        ),
    ]

    print("q79 fixed-u1 exceptional-line D-closure audit")
    print("================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
