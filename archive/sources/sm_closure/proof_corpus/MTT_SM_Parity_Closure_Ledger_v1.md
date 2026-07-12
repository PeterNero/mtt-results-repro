# MTT SM-Parity Closure Ledger v1

## Purpose

This repo separates two standards:

```text
SM-parity:
  MTT may admit measured constants as typed sector data,
  just as the Standard Model admits measured couplings, masses, and mixings.

No-knob:
  MTT must derive those values from selected internal data.
```

The no-knob program remains the goal.  SM-parity is the runway: it asks whether
MTT can be at least as complete as the SM as a physics framework before all
constants are derived.

## What Is Needed

SM-parity closure needs:

```text
core MTT axioms,
typed measured-parameter interface,
QM recovery interface,
QFT/local-field recovery interface,
SM gauge/representation sector interface,
GR recovery interface,
empirical equivalence ledger,
no-knob upgrade ledger for every measured input.
```

The first artifact should be:

```text
MTT_Core_Axioms_and_Measured_Parameter_Interface_v1
```

because without a typed measured-input policy, SM-parity can collapse into vague
knobs.  The rule should be:

```text
measured values may enter only as declared sector data,
with a recorded future no-knob replacement target.
```

## Initial Ledger

High-priority SM-parity sectors:

```text
QM measurement and records,
QFT/local field sector,
SM gauge group and representations,
fermion generations,
GR recovery and Bianchi/stress-energy consistency,
dimensionful constant interface.
```

Next-priority sectors:

```text
gauge couplings,
Yukawa matrices and masses,
CP phases,
Higgs sector,
cosmological parameters.
```

## Starting Point

Start with the interface theorem, not with another constant:

```text
MTT_Core_Axioms_and_Measured_Parameter_Interface_v1
```

Then build:

```text
MTT_SM_Sector_Embedding_Interface_v1
MTT_QM_QFT_GR_Recovery_Interface_v1
MTT_Empirical_Equivalence_Ledger_v1
MTT_No_Knob_Upgrade_Backlog_v1
```

## Guardrails

SM-parity does not mean unconstrained fitting.  A measured value is allowed only
when it is:

```text
typed,
localized to a sector,
declared before downstream calculation,
not reused as proof of source selection,
paired with a no-knob upgrade target.
```

## Verdict

The repo is initialized.  SM-parity is not closed yet.  The first closure target
is a rigorous measured-parameter interface that lets MTT stand on the same
standard as the SM while preserving the stronger no-knob program.
