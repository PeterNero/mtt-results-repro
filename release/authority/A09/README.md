# MTT SM-Parity Closure Reproduction Capsule

This repo is a clean, minimal reproduction package for the SM-parity closure
result from `mtt-sm-parity-closure`.

It rebuilds the final theorem from frozen input packets:

```text
SM_parity_closed = true
true_SM_equivalence_closed = false
no_knob_closed = false
```

The result is deliberately tiered. It proves SM-parity closure under the
declared parity-interface standard. It does not claim no-knob derivation of the
actual Qa/SU3 operator packet, true precision SM equivalence, or derivation of
measured constants.

## Reproduce

Run:

```powershell
python scripts\verify.py
```

The verifier rebuilds all output packets from `inputs/`, checks the guardrails,
and writes `reports/verification_report.txt`.

## What Is Bundled

- Frozen input packets needed for the final SM-parity closure step.
- A deterministic builder for the Qa/SU3 parity-interface replacement.
- A deterministic verifier for theorem flags, closure flags, and guardrails.
- A proof note generated from the rebuilt result.

## What Is Not Claimed

- No-knob closure.
- Actual selected Qa/SU3 `D_E` or `rho_E` operator data.
- Full threshold/covariance/precision SM equivalence.
- Use of observed SM values as source selectors.
- Target fitting.

## Source Boundary

Measured values remain downstream replay inputs. They do not select the source,
branch, quotient, operator packet, or no-knob proof.
