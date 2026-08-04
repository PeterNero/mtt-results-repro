# MTT q79 Height-Four Verified Stopping Checkpoint (2026-07-20)

## Exact frontier

- A373 final target inventory: closed (`76/76`).
- A374-A376 rank-3 handle, base-lift, and anchored-beta blocks: closed.
- A377 full residual interval: closed.
- A379 beta Hessian and A383 handle Hessian: closed.
- A380-A382 coefficient-weighted target Hessians: `43/76` full budgets closed.
- Target tails: `76/76` current and within their diagnostic half-budgets.
- A384 same-source residual Jacobian: waiting only for the remaining 33 full target budgets.
- A385S multivariate PGL(3) chart source: closed and audited.
- A385I raw interval local Hessian source: closed and audited.
- A385A centered eight-variable affine local Hessian source: closed and audited.

The intentionally unfinished target indices, in current A373 priority order, are:

`079 027 037 029 081 070 068 064 076 003 046 078 017 012 090 071 023 061 025 049 067 077 088 018 066 084 022 089 024 059 019 014 065`

The queue workers were stopped deliberately after their persisted reanchor/checkpoint
files had been written. No queue worker remains active. The canonical authority is
`hessian/precision.manifest.json`; its stable counts at this checkpoint are:

- full budget: `43`
- current main certificate: `43`
- main diagnostic half-budget: `41`
- current tail certificate: `76`
- tail diagnostic half-budget: `76`

## New result at this checkpoint: A385A

A385A replaces dependency-forgetting raw interval evaluation by the rigorous form

`f(z) = f_0 + sum_s f_s epsilon_s + Delta_f`, with `|epsilon_s| <= 1`,

for all eight complex PGL(3) coordinates. Each requested real-imaginary square is
enclosed by a complex disk of radius `sqrt(2) r`. Matrix-exponential and Frechet
terms use explicit quadratic-tail bounds; each parametric 11 by 11 reduction solve
is closed by a positive weighted Neumann contraction.

Certified output:

- covariant affine forms: `640`
- anchored-beta forcing affine forms: `128`
- maximum covariant centered-disk radius: `0.0001411028347900714`
- maximum beta-forcing centered-disk radius: `0.02195288643088207`
- maximum reduction contraction: `0.043756678341077625 < 1`
- compression relative to A385I raw boxes: `8,709,760.7x` and `29,826,641.8x`

The independent audit passes:

`python proof_corpus/selected_q79heightfourpgl3centeredaffinehessiansource_audit.py`

This is a local source theorem. It does not yet certify moving initial cycles, full
path transport, a wall-free polydisk, a Krawczyk zero, or full Standard Model
closure.

## Ordered continuation

1. Resume the 33 listed target Hessians and bring the strict manifest to `76/76`.
2. Build A384 with `scripts/build_q79_height4_rank3_residual_jacobian_interval.py`
   and run its independent audit.
3. Construct the moving affine H1 initial-cycle source and propagate A385A through
   the same 76 targets, handle, beta, and Picard-Lefschetz path data.
4. Select and certify a wall-free coordinate polydisk.
5. Run interval Newton/Krawczyk for existence and uniqueness of the covariant zero.
6. Run the complete verifier, freeze the final result ledger, commit, and push.

The next proof target is therefore not another point-source or value-row theorem.
It is completion of the 33 target Hessians, immediately followed by A384.
