"""Audit the explicit minimum-degree-nine q79 R-only fiber theorem."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "q79_Ronly_triple_fiber_min_degree"
SCRIPT = ROOT / "scripts" / "certify_q79_Ronly_explicit_minimum_degree9.py"
REPRODUCER = ROOT / "scripts" / "reproduce_q79_Ronly_explicit_degree9.sh"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_Triple_Fiber_Explicit_Minimum_Degree9_v2.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_Triple_Fiber_Explicit_Minimum_Degree9_v2.md")


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def main() -> None:
    required = [
        SCRIPT,
        REPRODUCER,
        CERTIFICATE,
        THEOREM,
        DATA / "parent_space5_class1_inverse_root.msolve.in",
        DATA / "selected_full14.msolve.in",
        DATA / "explicit_degree9_multipliers.json",
        DATA / "homogeneous_D8_D9.msolve.in",
        DATA / "homogeneous_D8_D9.msolve.out",
        DATA / "explicit_degree9_generation.packet.json",
        DATA / "msolve_f4_tail_dump.patch",
        DATA / "msolve_f4_ancestry_dump.patch",
        DATA / "msolve_f4_provenance_degree.patch",
        DATA / "msolve_f4_operation_dag.patch",
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    with tempfile.TemporaryDirectory(prefix="q79-r-only-degree9-") as directory:
        regenerated_path = Path(directory) / "certificate.json"
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--output", str(regenerated_path)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        regenerated = (
            json.loads(regenerated_path.read_text(encoding="utf-8"))
            if completed.returncode == 0 and regenerated_path.is_file()
            else {}
        )

    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    expected = "EXACT_EXPLICIT_MINIMUM_DEGREE_9_R_ONLY_TRIPLE_FIBER_CERTIFICATE"
    identity = regenerated.get("explicit_identity", {})
    minimum = regenerated.get("minimum_degree_theorem", {})
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("consolidator reruns", "PASS" if completed.returncode == 0 else "FAIL", completed.stdout[-160:]),
        Gate("committed status", "PASS" if committed.get("status") == expected else "FAIL", expected),
        Gate("regenerated status", "PASS" if regenerated.get("status") == expected else "FAIL", expected),
        Gate("packet reproduces exactly", "PASS" if regenerated == committed else "FAIL", "committed == regenerated"),
        Gate("parent specialization", "PASS" if regenerated.get("checks", {}).get("selected_rows_are_exact_parent_specializations") else "FAIL", "19 variables -> 16 selected rows"),
        Gate("explicit identity", "PASS" if identity.get("computed_residual") == "1" else "FAIL", "sum q_i f_i = 1"),
        Gate("multiplier terms", "PASS" if identity.get("total_multiplier_terms") == 175084 else "FAIL", "175084"),
        Gate("minimum degree", "PASS" if minimum.get("minimum_maximum_product_total_degree") == 9 else "FAIL", "NF(t^8)!=0, NF(t^9)=0"),
        Gate("D rows unused", "PASS" if regenerated.get("selected_rows", {}).get("D_terminal_rows_used") == [] else "FAIL", "R-only"),
        Gate("no fit parameters", "PASS" if regenerated.get("new_continuous_fit_parameters") == 0 else "FAIL", "zero"),
        Gate("theorem note saved", "PASS" if "175,084" in theorem and "degree nine is minimal" in theorem else "FAIL", str(THEOREM)),
    ]

    print("q79 R-only explicit minimum-degree-nine audit")
    print("================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
