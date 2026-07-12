# MTT Verifier Freeze 2026 06 06 Status v1

Frozen verifier: `scripts/verify_full_frozen_2026_06_06.py`

The frozen verifier preserves the full historical audit chain that was active
after commit `473704e Close PSM local source promotion gate`.  It is the
reproducibility archive for the long proof spine: SM-parity, true-equivalence
frontier artifacts, Route-C/HYM imports, terminal/SM-slot functor work,
dynamic-C1 source gates, and the latest PSM-C1-02 bridge/source-promotion
artifacts.

Current status at freeze:

- SM-parity replay is no longer the active blocker under the declared standard.
- Post-SM-parity work is active.
- `PSM-C1-02 / SOURCE-IDENTITY / VPB-1-LOCAL` is closed under the explicit
  local `SelectedWeylVariationActionPrinciple`.
- `PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED` remains open.
- The no-knob/dynamic-C1 closure still requires deriving the local principle
  from selected physical action data or independently executing the same finite
  row-source packet.
- Measured constants remain downstream parity inputs or benchmarks; they are
  not source selectors.

Why freeze:

The full verifier is valuable as a reproducibility archive, but it takes roughly
two minutes on the current machine and reruns many historical audits whose
outputs are no longer changing during frontier work.  The active `verify.py`
should therefore become a fast frontier verifier.  The frozen verifier remains
available for periodic full-chain audits before major claims, releases, or paper
integration.

Recommended usage:

- Fast daily/frontier check: `python scripts/verify.py`
- Full historical replay: `python scripts/verify_full_frozen_2026_06_06.py`
