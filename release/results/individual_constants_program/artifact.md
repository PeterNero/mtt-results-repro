# MTT Individual Constants Source Search

This repo is a focused fork for individual physical constants.

Goal: test whether selected MTT source data can derive individual constants
with zero fitted knobs, or with at most a very small number of universal
source-level parameters selected before empirical comparison.

Seed policy:

- measured values may be used for downstream comparison only;
- measured values may not select source packets, branches, kernels, or
  universal parameters;
- universal parameters are allowed only as source-level, global, typed
  constants, never as per-observable fitted knobs;
- every candidate constant receives an explicit readiness label.

Initial target:

`CONST-EM-01 / ALPHA1-SOURCE-STRENGTH`

This is the closest first attack because the SM-parity repo already contains
alpha1/source-strength, retarded-overlap, and transported dotD scaffolding.
