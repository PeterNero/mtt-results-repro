# MTT q79 d027 Disk Cauchy Majorant (A406D) v1

Let the complementary quartic in the local nodal coordinate be

`h(c+z)=a_0+a_1 z+...+a_4 z^4`.

For every `|z| <= rho`, the reverse triangle inequality gives

`|h(c+z)| >= lower(|a_0|) - sum_{k=1}^4 upper(|a_k|) rho^k`.

Thus a positive right-hand side proves that `h` is nonzero on the closed
complex disk. Since the disk is simply connected, the selected square-root
branch and its reciprocal are analytic there. Cauchy's estimate therefore
bounds the even Taylor coefficients by the disk radius `rho`, without replacing
the disk by its larger circumscribed coordinate square.

Writing `delta` for the discriminant of the colliding quadratic factor, the
central-binomial estimate `binom(2n,n) <= 4^n` gives the geometric ratio

`q = upper(|delta|)/(4 rho^2)`.

The value tail and its differentiated tail used by the implementation are the
closed geometric sums for `q < 1`; A406D retains the stronger gate `q < 1/2`.
The derivative majorant is obtained coefficientwise from the differentiated
local quartic on the same disk.

For selected d027 at cutoff `1e-3`, the first certified dyadic disk is
`rho=1/8`. Its numerical lower bound and ratio are emitted in A406F and replayed
by the dedicated audit; they are not assumed in this theorem statement.
