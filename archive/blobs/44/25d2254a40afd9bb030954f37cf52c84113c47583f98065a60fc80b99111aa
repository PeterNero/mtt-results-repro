#!/usr/bin/env python3
"""Render the exact complete nonzero-u2 CRT-gluing theorem."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_U1_002_Partial_CRT_Gluing_v1.json"
DEFAULT_OUTPUT = ROOT / "proof_corpus" / "Q79_Ronly_U1_002_Partial_CRT_Gluing_v1.md"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    require(
        certificate.get("status") == "EXACT_FULL_NONZERO_U2_CRT_GLUE_CERTIFIED",
        "certificate",
    )
    by_space = {entry["space_index"]: entry for entry in certificate["spaces"]}
    space5 = by_space[5]
    space6 = by_space[6]
    n5 = len(space5["closed_u2_values"])
    n6 = len(space6["closed_u2_values"])
    total = n5 + n6
    fibers = certificate["accounting"]["canonical_fixed_F101_fibers_represented"]
    p5 = space5["projector_polynomial"]["coefficients_ascending_mod_101"]
    p6 = space6["projector_polynomial"]["coefficients_ascending_mod_101"]
    require(n5 == 100 and n6 == 100, "complete nonzero-u2 components")
    require(p5 == [100, *([0] * 99), 1] and p6 == p5, "u2^100-1")
    text = f"""# q79 R-only `u1=2` Complete Nonzero-`u2` CRT Gluing Theorem

## Status

`EXACT_FULL_NONZERO_U2_CRT_GLUE_CERTIFIED`

Coverage: `COMPLETE_F101_NONZERO_U2_TORUS_IN_BOTH_SPACES`

## Theorem

For space 5 let

```text
P_5(u2) = product_(a=1)^{n5} (u2-a) in F_101[u2],
```

and for space 6 let

```text
P_6(u2) = product_(a=1)^{n6} (u2-a) in F_101[u2].
```

The certificate emits every Lagrange projector

```text
e_a = (P_s/(u2-a)) * ((P_s/(u2-a))(a))^(-1) mod P_s.
```

Their evaluation matrices are the identity, each `e_a` is idempotent modulo
`P_s`, and they sum to one. Hence

```text
F_101[u2]/(P_5) ~= product_(a=1)^{n5} F_101,
F_101[u2]/(P_6) ~= product_(a=1)^{n6} F_101.
```

Every factor is an already-certified complete R-only or full R/`y`/D unit
component. Therefore the full selected ideal quotient is the zero ring over
the complete nonzero `F_101` `u2` torus in each space. This glues `{total}` line
certificates, representing `{fibers}` canonical fixed `F_101` fibers, into
two exact finite-algebra statements.

Writing `A_s` for the selected ambient algebra and `J_s` for its full
R/`y`/D ideal, the exact conclusion is

```text
A_s/(J_s + (P_s))
    ~= product_(a=1)^n_s A_s/(J_s + (u2-a))
     = product_(a=1)^n_s 0
     = 0.
```

## Projector Polynomials

Coefficients are ascending and reduced modulo `101`.

```text
P_5: {p5}
P_6: {p6}
```

## What This Adds

The linewise computation is connected by an explicit algebraic decomposition,
not only by counting. All 100 nonzero `u2` components are certified in both
spaces, and both projector polynomials are exactly `u2^100-1`. The theorem
therefore closes each entire selected nonzero finite `u2` torus without a
monolithic Groebner run.

## Boundary

No new line is classified here. The theorem does not provide expanded global
Nullstellensatz coefficients and does not address the other 98 nonzero `u1`
values, mirror zero-zero charts, characteristic zero, or physical HYM/QG
promotion. The global symbolic chart count remains `138/140`. New continuous
fit parameters: `0`.

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_partial_CRT_gluing_audit.py
```
"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print("Q79_U1_002_FULL_NONZERO_CRT_GLUE_THEOREM_RENDERED")
    print(f"space5={n5}; space6={n6}; total={total}")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
