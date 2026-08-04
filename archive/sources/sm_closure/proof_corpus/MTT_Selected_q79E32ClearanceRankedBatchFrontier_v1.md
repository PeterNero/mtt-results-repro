# MTT Selected q79 E32 Clearance-Ranked Batch Frontier v1

## A138 result

The reusable weighted batch ledger now accepts three complete interval
thimbles: `d004` with coefficient `+2`, `d061` with coefficient `-3`, and
`d019` with coefficient `+3`. The new d019 execution has

```text
tail radius = 9.588625796141949e-09
main radius = 1.949802843119291e-07
full radius = 2.853320921758496e-07
fallback    = 2.308660192880193e-05
```

The d019 tail required 1,536 local intervals because its widest initial
factor enclosure was not discriminant-separated at lower subdivisions. That
refinement produced a very tight full ball. All three independent A131 centers
are contained but are not used as bounds.

The exact ledger is now 3/71 support and L1 weight
8/123. The remaining weighted budget is
`0.002772700723429714`. The d047 coefficient-four row remains partial with
node/Hensel and tail closed but no accepted main interval.

## Non-looping execution policy

The builder emits the remaining y and z queues directly from the selected A134
integer chain and the certified A127 radial clearances. Fresh rows are ordered
by coefficient L1 times available clearance. Accepted full packets are found
and charged automatically, so later runs do not reconstruct the ledger by
hand.

## Open

- 68 complete thimble intervals, L1 weight 115;
- the covariant z-chart interval adapter;
- the weighted sum and exact frozen-carrier decision.
