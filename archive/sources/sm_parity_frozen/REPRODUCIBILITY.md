# Reproducibility Protocol

This capsule has one purpose: rebuild the final SM-parity closure decision from
frozen machine-readable inputs.

## Command

```powershell
python scripts\verify.py
```

## Expected Result

The command must end with:

```text
Verification result: PASS
SM-parity closure: TRUE
true SM equivalence: FALSE
no-knob closure: FALSE
```

## Interpretation

The proof is an SM-style parity result. It says that, once measured parameters
are admitted only downstream in the same role they play in the Standard Model,
the MTT typed interface has enough audited structure to close the SM-parity
packet.

The proof does not say that MTT has derived the Standard Model constants or the
actual Qa/SU3 operator packet without knobs.

## Guardrails Checked

- `observed_data_used_as_selector = false`
- `target_fitting_used = false`
- `actual_selected_operator_packet_claimed = false`
- `true_SM_equivalence_closed = false`
- `no_knob_closed = false`

## Frozen Inputs

The input packets in `inputs/` are intentionally small. They freeze the state
immediately before the final closure move:

- one-gate SM-parity matrix
- Qa/SU3 integration status
- actual selected SM-packet/anomaly audit
- prior final-packet certificate
- prior one-gate candidate

This makes the reproduction auditable without requiring the full exploratory
workspace.
