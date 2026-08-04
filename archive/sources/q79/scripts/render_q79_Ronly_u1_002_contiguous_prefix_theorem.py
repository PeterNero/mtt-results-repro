#!/usr/bin/env python3
"""Render the current q79 u1=2 contiguous-prefix theorem from its certificate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.json"
DEFAULT_OUTPUT = ROOT / "proof_corpus" / "Q79_Ronly_U1_002_Contiguous_CrossSpace_Prefix_v1.md"


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
        certificate.get("status") == "EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED",
        "contiguous-prefix certificate",
    )
    accounting = certificate["accounting"]
    n5 = accounting["space5_contiguous_symbolic_lines_closed"]
    n6 = accounting["space6_contiguous_symbolic_lines_closed"]
    total = accounting["cross_space_symbolic_lines_closed"]
    r_units = accounting["R_only_unit_lines"]
    d_units = accounting["D_augmented_unit_lines"]
    fibers = accounting["canonical_fixed_F101_fibers_closed"]
    remaining = accounting["cross_space_symbolic_lines_remaining_unclassified"]
    stop5 = certificate["first_unproved_line"]["space5"]
    stop6 = certificate["first_unproved_line"]["space6"]
    solver = certificate["solver_provenance"]
    exceptions = [
        row
        for row in certificate["space5_closed_lines"] + certificate["space6_closed_lines"]
        if row["complete_status"] == "EXACT_FULL_R_Y_D_UNIT"
    ]
    exception_rows = "\n".join(
        f"- space {row['space_index']} `u2={row['u2']}`: R-only quotient dimension "
        f"`{row['quotient_dimension']}`, `D{row['D_unit_row']}` determinant "
        f"`{row['D_multiplication_determinant']}`."
        for row in exceptions
    ) or "- None."
    complete_cover = n5 == 100 and n6 == 100 and remaining == 0
    title = (
        "q79 R-only `u1=2` Complete Cross-Space Cover"
        if complete_cover
        else "q79 R-only `u1=2` Contiguous Cross-Space Prefix"
    )
    next_obligations = (
        """space 5: all u2=1,...,100 closed (ALL_100_LINES_CLOSED)
space 6: all u2=1,...,100 closed (ALL_100_LINES_CLOSED)."""
        if complete_cover
        else (
            f"space 5: u2={stop5['next_u2']} ({stop5['reason']})\n"
            f"space 6: u2={stop6['next_u2']} ({stop6['reason']})."
        )
    )
    boundary = (
        """All `200` nonzero-`u2`, `u1=2` cross-space lines are classified.
The theorem does not address the other `98` nonzero `u1` values, either
mirror zero-zero chart, or a characteristic-zero system. It does not promote
the finite-field obstruction to physical HYM or quantum-gravity data. The
global symbolic chart count remains `138/140`."""
        if complete_cover
        else (
            f"This theorem does not classify the other `{remaining}` `u1=2` lines, "
            "the other `98` nonzero `u1` values, either mirror zero-zero chart, or a "
            "characteristic-zero system. It does not promote the finite-field "
            "obstruction to physical HYM or quantum-gravity data. The global "
            "symbolic chart count remains `138/140`."
        )
    )
    text = f"""# {title}

## Status

`EXACT_U1_002_CONTIGUOUS_CROSSSPACE_PREFIX_CLOSED`

Coverage: `{certificate.get('coverage_status', 'CONTIGUOUS_PREFIX_ONLY')}`

## Theorem

At `u1=2`, the complete saturated symbolic-line ideals are unit at the
required R-only or full R/`y`/D tier for

```text
space 5: u2=1,...,{n5}
space 6: u2=1,...,{n6}.
```

Each R-only literal basis `[1]` excludes the entire displayed Laurent line
over `F_101` and every scalar extension. A nonunit R-only basis is counted
only when an exact finite-quotient certificate proves a selected D terminal
is invertible. Thus the theorem closes `{total}/200` symbolic lines and
represents `{fibers}` canonical fixed `F_101` fibers.

## Exact Accounting

```text
space-5 contiguous lines closed:                {n5}/100
space-6 contiguous lines closed:                {n6}/100
cross-space lines closed:                       {total}/200
literal R-only unit lines:                          {r_units}
D-augmented unit lines:                              {d_units}
canonical fixed F_101 fibers represented:         {fibers}
remaining unclassified u1=2 lines:                 {remaining}
new continuous fit parameters:                           0
```

## Finite-Quotient Exceptions

{exception_rows}

No nonunit R-only output is promoted by itself.

## Exact Solver Provenance

```text
engine:       {solver['engine']}
binary bytes: {solver['binary_bytes']}
binary SHA256:{solver['binary_sha256']}
mode:         {solver['mode']}
```

Every counted log is checked for characteristic `101`, one thread, DRL,
reduced-basis output, zero invalid equations, and a completed solver timing.
Literal unit lines additionally require the solver's single-element/no-solution
verdict. Inputs, outputs, logs, and the provenance baseline are hash-bound.

## Next Exact Obligations

```text
{next_obligations}
```

## Boundary

{boundary}

## Reproduce

```text
python proof_corpus/q79_Ronly_u1_002_contiguous_prefix_audit.py
```
"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print("Q79_U1_002_CONTIGUOUS_PREFIX_THEOREM_RENDERED")
    print(f"space5={n5}; space6={n6}; total={total}")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
