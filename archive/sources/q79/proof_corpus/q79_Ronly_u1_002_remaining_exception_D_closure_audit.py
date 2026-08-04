"""Replay-audit the six final q79 u1=2 finite-quotient D-unit certificates."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = (
    ROOT
    / "scripts"
    / "verify_q79_Ronly_symbolic_finite_groebner_exception_D_unit.py"
)
DATA = ROOT / "candidate_data" / "q79_Ronly_u1_002_symbolic_exception_D_closure"
THEOREM = Path(__file__).with_name(
    "Q79_Ronly_U1_002_Remaining_Exception_D_Closure_v1.md"
)
STATUS = (
    "EXACT_R_ONLY_FINITE_GROEBNER_LINE_REJECTED_SCHEME_THEORETICALLY_BY_D"
)


@dataclass(frozen=True)
class Spec:
    space: int
    u2: int
    scalar_class: int
    a: int
    dimension: int
    determinant: int

    @property
    def certificate_name(self) -> str:
        return (
            f"space{self.space}_class{self.scalar_class}_u1_002_"
            f"a_{self.a:03d}_symbolic_t_finite_groebner.D_unit.certificate.json"
        )


@dataclass(frozen=True)
class Gate:
    label: str
    passed: bool
    detail: str


SPECS = (
    Spec(5, 31, 1, 47, 10, 36),
    Spec(6, 53, 2, 18, 10, 1),
    Spec(6, 59, 2, 23, 20, 1),
    Spec(5, 73, 2, 6, 10, 95),
    Spec(5, 75, 2, 43, 20, 1),
    Spec(6, 91, 2, 11, 3, 38),
)


def artifact_matches(entry: dict[str, object]) -> bool:
    path = ROOT / str(entry.get("path", ""))
    return bool(
        path.is_file()
        and path.stat().st_size == entry.get("bytes")
        and hashlib.sha256(path.read_bytes()).hexdigest() == entry.get("sha256")
    )


def replay(spec: Spec, output: Path) -> subprocess.CompletedProcess[str]:
    family = (
        ROOT
        / "candidate_data"
        / f"q79_Ronly_u1_002_space{spec.space}_symbolic_u2_prefix"
    )
    stem = f"space{spec.space}_u1_002_u2_{spec.u2:03d}.msolve"
    parent = (
        ROOT
        / "candidate_data"
        / "q79_Ronly_classfree_representative_lines"
        / f"space_{spec.space}_h0_g0_class{spec.scalar_class}_inverse_root.msolve.in"
    )
    command = [
        sys.executable,
        str(VERIFIER),
        "--parent",
        str(parent),
        "--family-packet",
        str(family / "family.packet.json"),
        "--source-input",
        str(family / "inputs" / f"{stem}.in"),
        "--basis-output",
        str(family / "inputs" / f"{stem}.out"),
        "--basis-log",
        str(family / "inputs" / f"{stem}.log"),
        "--space",
        str(spec.space),
        "--u1",
        "2",
        "--u2",
        str(spec.u2),
        "--scalar-class",
        str(spec.scalar_class),
        "--a",
        str(spec.a),
        "--output",
        str(output),
    ]
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def main() -> None:
    certificate_paths = [DATA / spec.certificate_name for spec in SPECS]
    required = [VERIFIER, THEOREM, *certificate_paths]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    packets = [json.loads(path.read_text(encoding="utf-8")) for path in certificate_paths]
    replay_results: list[subprocess.CompletedProcess[str]] = []
    replay_equal: list[bool] = []
    with tempfile.TemporaryDirectory(prefix="q79-u1-002-final-D-") as directory:
        temporary = Path(directory)
        for index, (spec, path) in enumerate(zip(SPECS, certificate_paths)):
            output = temporary / f"certificate-{index}.json"
            result = replay(spec, output)
            replay_results.append(result)
            replay_equal.append(
                result.returncode == 0
                and output.is_file()
                and output.read_bytes() == path.read_bytes()
            )

    coordinates = [
        (
            packet.get("space_index"),
            packet.get("fixed_coordinates", {}).get("selected_u2"),
            packet.get("scalar_square_class_representative"),
            packet.get("fixed_coordinates", {}).get("a_equals_v_times_u3"),
        )
        for packet in packets
    ]
    expected_coordinates = [
        (spec.space, spec.u2, spec.scalar_class, spec.a) for spec in SPECS
    ]
    witnesses = [
        (
            packet.get("quotient_algebra", {}).get("dimension"),
            packet.get("unit_witness", {}).get("parent_row"),
            packet.get("unit_witness", {}).get("D_multiplication_determinant"),
        )
        for packet in packets
    ]
    expected_witnesses = [
        (spec.dimension, 18, spec.determinant) for spec in SPECS
    ]
    products = [
        packet.get("unit_witness", {}).get("product_coefficients", [])
        for packet in packets
    ]
    theorem = THEOREM.read_text(encoding="utf-8")
    normalized_theorem = " ".join(theorem.split())
    gates = [
        Gate("all artifacts present", not missing, f"files={len(required)}"),
        Gate(
            "certificate statuses",
            all(packet.get("status") == STATUS for packet in packets),
            f"certificates={len(packets)}",
        ),
        Gate(
            "coordinates are exact",
            coordinates == expected_coordinates,
            str(coordinates),
        ),
        Gate(
            "quotient dimensions and D witnesses",
            witnesses == expected_witnesses,
            str(witnesses),
        ),
        Gate(
            "displayed inverses multiply to one",
            all(
                product
                and product[0] == 1
                and all(value == 0 for value in product[1:])
                for product in products
            ),
            "six exact unit products",
        ),
        Gate(
            "all source artifacts hash-bind",
            all(
                packet.get("artifacts")
                and all(artifact_matches(entry) for entry in packet["artifacts"].values())
                for packet in packets
            ),
            "parent/family/input/basis/log/provenance",
        ),
        Gate(
            "all finite-algebra checks pass",
            all(
                packet.get("checks")
                and all(packet["checks"].values())
                and packet["quotient_algebra"]["associativity_basis_triple_checks"]
                == packet["quotient_algebra"]["dimension"] ** 3
                for packet in packets
            ),
            "exact reduction, multiplication, associativity, y lift and D inverse",
        ),
        Gate(
            "independent deterministic replays",
            all(replay_equal),
            f"{sum(replay_equal)}/{len(replay_equal)} byte-identical",
        ),
        Gate(
            "replay processes succeeded",
            all(result.returncode == 0 for result in replay_results),
            "; ".join(result.stdout.splitlines()[-2] for result in replay_results),
        ),
        Gate(
            "theorem records all six rows",
            all(
                f"| {spec.space} | {spec.u2} | {spec.scalar_class} | {spec.a} | "
                f"{spec.dimension} | 18 | {spec.determinant} |"
                in theorem
                for spec in SPECS
            ),
            str(THEOREM),
        ),
        Gate(
            "claim boundary retained",
            "does not establish characteristic-zero closure" in normalized_theorem
            and "does not promote a physical q79, HYM, QFT, SM, or quantum-gravity claim"
            in normalized_theorem,
            "finite F_101 u1=2 lines only",
        ),
        Gate(
            "zero fit parameters",
            all(packet.get("new_continuous_fit_parameters") == 0 for packet in packets),
            "zero",
        ),
    ]
    print("q79 u1=2 final finite-quotient D-closure audit")
    print("=================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(
            f"{gate.label:{width}s}  "
            f"{'PASS' if gate.passed else 'FAIL':4s}  {gate.detail}"
        )
    if any(not gate.passed for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
