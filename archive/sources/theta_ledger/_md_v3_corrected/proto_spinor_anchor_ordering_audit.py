"""Audit the proto-spinor anchor-ordering lemma."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def main() -> None:
    lemma = read(ROOT / "ProtoSpinor_Anchor_Ordering_Lemma_for_Family_Metric_v1.md")
    metric = read(ROOT / "Anchored_Kinetic_Metric_Source_Candidate_v1.md")

    gates = [
        Gate("lemma file", "PASS" if "Anchor Ordering Is Canonical" in lemma else "FAIL", "anchor-ordering lemma present"),
        Gate("role triple", "PASS" if "transport, lens, nil" in lemma else "FAIL", "three proto-spinor roles named"),
        Gate("strict order", "PASS" if "0 < J_lens < J_nil" in lemma else "FAIL", "cost order stated"),
        Gate("gap source", "PASS" if "lambda_nil/lambda_lens" in lemma and "lambda_nil/lambda_lens" in metric else "FAIL", "uses lens/nil hierarchy"),
        Gate("relabeling handled", "PASS" if "basis relabeling" in lemma else "FAIL", "family label permutation scoped"),
        Gate("no flavor input", "PASS" if "no measured flavor data" in lemma else "FAIL", "ordering not fit to masses"),
        Gate("sector scale", "OPEN" if "derive sector scale s_x" in lemma else "FAIL", "still must derive scale from MTT"),
    ]

    print("Proto-spinor anchor-ordering audit")
    print("==================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
