"""Audit the exact q79 inverse-root rowwise diagonal-symmetry no-go."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
VERIFIER = ROOT / "scripts" / "verify_q79_inverse_root_diagonal_torus_no_go.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Inverse_Root_Diagonal_Symmetry_NoGo_v1.json"
THEOREM = Path(__file__).with_name("Q79_Inverse_Root_Diagonal_Symmetry_NoGo_v1.md")
PARENTS = tuple(
    DATA / f"space_{space}_h0_g0_class{scalar_class}_inverse_root.msolve.in"
    for space in (5, 6)
    for scalar_class in (1, 2)
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def main() -> None:
    required = [VERIFIER, CERTIFICATE, THEOREM, *PARENTS]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="q79-diagonal-nogo-") as directory:
        output = Path(directory) / "certificate.json"
        command = [sys.executable, str(VERIFIER)]
        for parent in PARENTS:
            command.extend(["--input", str(parent.relative_to(ROOT))])
        command.extend(["--output", str(output)])
        run = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        regenerated = (
            json.loads(output.read_text(encoding="utf-8"))
            if run.returncode == 0 and output.is_file()
            else {}
        )

    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    charts = regenerated.get("charts", [])
    exact_kernels = [
        row.get("weight_kernel_mod_100")
        == [[0] * 19, [0] * 18 + [50]]
        for row in charts
    ]
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("verifier reruns", "PASS" if run.returncode == 0 else "FAIL", run.stdout[-180:].strip()),
        Gate("certificate reproduces", "PASS" if regenerated == committed else "FAIL", "committed == regenerated"),
        Gate(
            "exact status",
            "PASS" if regenerated.get("status") == "EXACT_ROWWISE_DIAGONAL_TRANSITIVE_U1_NORMALIZATION_NO_GO" else "FAIL",
            str(regenerated.get("status")),
        ),
        Gate("four parent charts", "PASS" if len(charts) == 4 else "FAIL", str(len(charts))),
        Gate(
            "rank table",
            "PASS" if all((row.get("rank_over_Q"), row.get("rank_mod_2"), row.get("rank_mod_5")) == (19, 18, 19) for row in charts) else "FAIL",
            "19/18/19 in every chart",
        ),
        Gate("complete kernels", "PASS" if all(exact_kernels) else "FAIL", "identity and v weight 50"),
        Gate(
            "u1 fixed",
            "PASS" if all(row.get("u1_exponents_mod_100") == [0] and row.get("maximum_u1_orbit_size") == 1 for row in charts) else "FAIL",
            "orbit size 1",
        ),
        Gate(
            "all checks",
            "PASS" if len(regenerated.get("checks", {})) == 12 and all(regenerated.get("checks", {}).values()) else "FAIL",
            f"{sum(bool(value) for value in regenerated.get('checks', {}).values())}/12",
        ),
        Gate(
            "claim boundary retained",
            "PASS" if "route-elimination theorem" in theorem and "does not close" in theorem and "No continuous fit parameter" in theorem else "FAIL",
            str(THEOREM),
        ),
    ]

    print("q79 inverse-root diagonal-symmetry no-go audit")
    print("================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
