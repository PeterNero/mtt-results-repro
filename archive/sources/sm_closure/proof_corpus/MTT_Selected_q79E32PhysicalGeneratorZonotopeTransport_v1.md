# MTT Selected q79 E32 Physical-Generator Zonotope Transport v1

> **A151 supersession note.** This artifact's y-chart zonotope results remain
> unchanged. The later
> `MTT_Selected_q79ProjectiveChartCovariantE32IntervalAdapter_v1` closes the
> generic z-chart infrastructure and certifies `d048` end to end. The current
> ledger is 16/71 support and 36/123 in L1; 55 supports remain.

## Scope

This note closes a numerical wrapping defect in the rigorous E32 main-segment
transport. It does not change the selected q79 carrier, the Gauss-Manin system,
the distinguished thimble, or the A134 fallback. It replaces only the internal
representation of already-certified transport error.

The first accepted use is `d057 / selected_008` at cutoff
`epsilon = 2e-5`. Observed Standard Model values are not inputs.

## Local Error Recurrence

Let the physical error before one validated step be contained in the zonotope

```text
E_n subset Z(G_n) = {G_n xi : |xi_j| <= 1}.
```

The existing Taylor-residual lemma supplies an interval endpoint fundamental
matrix `P_n`, a pre-propagation correction radius `c_n`, and a direct endpoint
rounding radius `r_n`. Its original coordinate pullback is

```text
F_(n+1)^(-1) P_n,   where F_(n+1) = P_n F_n.
```

Therefore the same lemma is equivalently the physical-space inclusion

```text
E_(n+1) subset P_n E_n + P_n[-c_n,c_n]^6 + [-r_n,r_n]^6.
```

Define the next generator matrix without intermediate reboxing by

```text
G_(n+1) = [ P_n G_n | c_n P_n | r_n I_6 ].
```

Every matrix and radius in this recurrence is an Arb/ACB interval object. By
induction, `Z(G_n)` contains the physical transport error after every accepted
step. The E32 endpoint radius is bounded directly by the absolute row sum

```text
R_E32 = sum_j |(G_N)_(E32,j)|.
```

This is a strict enclosure. The generator blocks are not compressed, fitted,
or projected back to six rotated coordinate radii.

## d057 Certificate

The deep-seed node certificate selects cutoff roots `(3,4)` with node-affinity
margin greater than `1.83`. The endpoint tail uses 384 regular cells and has
radius `1.716579923538575e-6`.

The zonotope main transport uses 120-digit arithmetic, order 64, maximum step
`0.005`, and the certified radial relative homotopy. It accepts 252 steps,
rejects 21 noncontractive or over-budget proposals, and ends with 505 generator
blocks (3030 columns). Its E32 radius is
`1.038675053577015e-5`.

The oriented full splice has radius `1.640566262040011e-5`, lies below the A134
fallback `2.3086601928801926e-5` by `6.68093930840182e-6`, and contains the
independent floating center. The floating value is diagnostic only.

## Independent d037 Reuse

The same frozen zonotope builder is independently consumed by
`d037 / selected_002` at cutoff `1e-5`. Its 384-cell tail radius is
`6.588022287701279e-7`. The main transport accepts 235 steps, rejects 55 local
proposals, ends with 471 generator blocks (2826 columns), and has radius
`8.253525766885164e-8`. The full splice radius is
`7.755247146690182e-7`; it meets the same A134 fallback and contains the
independent floating center.

## Certified Cutoff-Period Reuse

The tail packet already contains a rigorous five-component cutoff-period
enclosure: five serialized centers and one common component-radius upper
bound. For each real coordinate with serialized binary64 center `m`, reconstruct
the Arb ball with radius

```text
r_reconstructed = r_tail + 2 ulp(m).
```

The two-ulp term encloses the Arb-to-binary64 conversion and decimal round
trip. Hence each reconstructed ball contains the corresponding tail-certified
cutoff-period ball. The main transport checks that its certified nodal pair is
the same pair named by the tail packet and consumes these reconstructed balls
directly. This removes an otherwise unnecessary independent recomputation at
the main/tail handoff. The floating period remains diagnostic only.

## Route-Scanned d060 Reuse

For `d060 / selected_089`, the geometry-only scanner tests 1122 polygonal
routes and certifies 324 in the original relative homotopy class. The selected
route `(0.45,-0.01,0.86)` has critical clearance `0.015569783888339555` and
uses no period or observed-value objective. This improved conditioning permits
order 48. The main transport consumes the tail-certified cutoff periods; their
source radius is `4.21998174059676e-44`, and serialization-safe reconstruction
has radius `2.77555757707253e-17`. It accepts 126 steps, rejects 19 proposals,
ends with 253 blocks (1518 columns), and has radius
`8.26708945089474e-8`. The 384-cell tail radius is
`5.516838641028699e-6`, and the full splice radius is
`5.63375292017554e-6`.

## Route-Scanned d087 Reuse

For `d087 / selected_085`, the geometry-only scanner tests 1122 routes and
certifies 534 in the selected relative homotopy class. The route
`(0.25,0,0.74)` has critical clearance `0.009203753605703522` and chart-zero
clearance `0.10943884469271638`. The independently certified node/Hensel packet
selects roots `(3,4)` with node Jacobian lower bound `85709.19021329148`.

The tail-certified cutoff-period source radius is
`7.82807914281157e-42`; serialization-safe reconstruction has radius
`3.55271369203539e-15`. The order-48 zonotope transport accepts 139 steps,
rejects 50 proposals, ends with 279 blocks (1674 columns), and has main radius
`4.921072286600216e-8`. The 384-cell tail radius is
`4.295933031528421e-6`. Their oriented full splice has radius
`4.365527402683257e-6`, meets the A134 fallback by
`1.87210745261187e-5`, and contains the independent floating center.

## d011 and d086 Continuation

The same tail-reuse zonotope source closes two further `y`-chart queue heads.
For `d011/selected_014`, 145 accepted and 56 rejected proposals give main
radius `2.1153876733524222e-7`; its tail and full radii are respectively
`2.3480975066547676e-6` and `2.647258515509066e-6`. For
`d086/selected_084`, 126 accepted and 37 rejected proposals give main radius
`1.7865286913408602e-7`; its tail and full radii are
`2.270697873285599e-6` and `2.523348872074394e-6`.

## Covariant z-Chart Execution

A123 supplies the exact `y/z` projective overlap law. The interval engine now
uses the selected line chart explicitly, and the independently isolated
`L2=0` wall controls the native `z` domain. The first complete native `z` row,
`d048/selected_046`, uses 68 accepted and 18 rejected zonotope proposals. Its
main, tail, and full radii are `7.936130431453395e-8`,
`4.079888063675264e-10`, and `1.1264182253611922e-7`. A151 therefore retires
the generic `z`-adapter blocker, without declaring the remaining `z` rows
closed.

The chart generalization does not silently replace historical `y` authority.
A byte-level audit specializes the current source back to `y` by reversing
only the explicit chart parameter and strict chart guards. It reconstructs
the recorded transport, augmented-main, and full-splice source hashes exactly.
The old interval packets remain historical executions rather than being
relabelled as new runs.

## A152 d088 Execution

For `d088/selected_064`, the deep-seed interval Newton certificate selects
roots `(0,1)` with node Jacobian lower bound `1267.0119644766608`. The default
48-cell tail partition was correctly rejected because one regular cell still
contained the nodal discriminant. Refining to the established 384-cell policy
closes the tail with radius `1.33992724832277e-8`.

A geometry-only scan tests 1122 routes and accepts 527 in the required
relative homotopy class. The top route `(0.35,0.01,0.82)` has other-critical
clearance `0.013946383993983567`. The rigorous transport accepts 128 steps,
rejects 23 trial steps, ends with 257 blocks (1542 columns), and has main
radius `4.0606162630066217e-7`. Its full splice radius is
`5.876571353979899e-7`; it contains the independent floating center and meets
the A134 fallback.

## A153 d033 Execution

For `d033/selected_010`, interval Newton selects roots `(3,4)` with node
Jacobian lower bound `2056471.1705916817`. The 384-cell endpoint tail has
radius `4.038975447429039e-6`. A geometry-only scan tests 1122 routes and
accepts 441; the selected radial-class route `(0.20,0,0.65)` has
other-critical clearance `0.006147025025469005` and chart-zero clearance
`0.06381917008974228`.

The central path contains a narrow conditioning pocket. The interval engine
accepts 171 steps and rejects 84 noncontractive or over-budget proposals,
without changing the accepted enclosure. The final main radius is
`6.326398650143199e-7`. The full splice radius is
`4.933663213080309e-6`; it contains the independent floating center and meets
the A134 fallback.

## A154 d035 Append Frontier

The generic augmented-frame engine closes `d035/selected_004`, coefficient
`+1`, on the certified `(0.20,0,0.74)` radial-class route. Its 384-cell tail
has radius `1.8892766888711778e-6`. The main transport accepts 191 steps,
rejects 97 trial steps, and closes with radius `1.4173551537312103e-6`.
The full splice radius is `3.893695826207023e-6`; it contains the independent
floating center and meets the A134 fallback. This row advances the append
ledger without changing the nine-row zonotope recurrence count.

## A155 d063 Append Frontier

The generic augmented-frame engine closes `d063/selected_063`, coefficient
`+2`, on the scanner-selected `(0.20,0.02,0.78)` route. The route has
other-critical clearance `0.01653227432999781`. Its 384-cell tail has radius
`1.917458927191973e-7`; 100 accepted main steps and 17 rejected trial steps
close the main radius at `3.4309395125334205e-6`. The full splice radius is
`5.04381816313071e-6`, contains the independent floating center, and meets the
A134 fallback.

## A156 d026 Append Frontier

The same generic augmented-frame engine closes `d026/selected_015`, coefficient
`-1`, on the scanner-selected `(0.20,0,0.74)` route. The route is in the radial
relative-homotopy class, has zero certified winding, and retains other-critical
clearance `0.005153608796651186`. Its 384-cell tail has radius
`1.1451826514852216e-8`; 148 accepted main steps and 46 rejected trial steps
close the main radius at `1.330671149301234e-6`. The full splice radius is
`1.8933050220937277e-6`, contains the independent floating center, and meets the
A134 fallback with margin `2.11932969067082e-5`.

## A157 d032 Pair-Selected Append Frontier

The default near-node point seed is not authoritative for `d032/selected_035`:
its apparent weak Jacobian comes from selecting the wrong local pair. The
established deeper radial selector uniquely identifies pair `[4,5]` and
interval-certifies the actual node with Jacobian lower bound
`56299.22284545123`. The pair-aware engine then closes coefficient `+1` on the
scanner-selected `(0.45,-0.02,0.86)` route, whose other-critical clearance is
`0.015083264764071557`. Its 384-cell tail radius is
`2.0679009899993166e-6`; 100 accepted main steps and 33 rejected trial steps
close the main radius at `2.0334266570578483e-7`. The full splice radius is
`2.3554023620420143e-6`, contains the independent floating center, and meets the
A134 fallback with margin `2.0731199566759912e-5`.

## A158 d030 Compact-H1 Orientation Frontier

`d030/selected_034`, coefficient `+1`, exposes and closes a previously hidden
typing error in the polygonal orientation gate. The selected floating source
and interval engine use homologous local vanishing arcs, but a polygonal
transport can change the three meromorphic puncture-lift coordinates while
leaving the compact cycle unchanged. The existing 90-thimble synchronization
theorem states that exactly the first two holomorphic periods descend to
compact `H1`; the other three rows retain puncture-at-infinity lift dependence
and are not orientation data. A158 therefore consumes that theorem directly,
selects the sign from the two compact rows, and records the five-row mismatch
only as a diagnostic.

On the scanner-selected `(0.25,0.02,0.86)` route, compact-H1 orientation is
separated with selected residual `1.922947248965649e-10` versus opposite-sign
residual `0.25870010053171594`. The higher meromorphic lift difference is
`11.520484471488459` and is explicitly excluded from sign selection. The route
has other-critical clearance `0.013924490788332338`; 91 accepted main steps and
24 rejected trial steps give main radius `6.576746775026099e-8`. Its 384-cell
tail radius is `1.3701298353652194e-6`, and the full splice radius is
`1.4630221993883199e-6`. The full interval contains the independent floating
center and meets the A134 fallback with margin `2.1623579729413607e-5`.

## Interpretation Correction

Intermediate endpoint radii can contract under later transport. They are not a
monotone cumulative cost. Earlier manually aborted d057 probes therefore do not
prove failure and are not used as no-go evidence. The accepted result is based
only on the completed final packet and full-splice certificate.

## A159 d085 Certified-Tail Reuse Frontier

`d085/selected_077`, coefficient `+1`, closes on the standard certified nodal
pair `[1,2]`. Its interval node Jacobian has lower bound
`3277.991084271393`. A scan certifies 522 null-homotopic routes; the frozen
`(0.2,0,0.7)` route has other-critical clearance
`0.0030717440711569206` and selected y-chart-zero clearance
`0.0951671260942113`.

The main computation reuses the cutoff-period balls already certified by the
384-cell tail packet. With Taylor order 20, every local remainder remains
subject to the unchanged `1e-8` lift-correction gate. The transport accepts 148
steps, rejects 53 trial steps, and closes with main radius
`1.1901906201071195e-5`. Orientation is separated by residual
`2.1559395228739639e-10` versus `11.150372981456783` for the opposite sign.
The full splice radius is `1.8597572761791529e-5`, contains the independent
floating center, and meets the A134 fallback with margin
`4.4890291670103975e-6`.

## A160 d010 Anti-Wrapping Frontier

`d010/selected_021`, coefficient `+1`, has the standard certified nodal pair
`[1,2]` with interval Jacobian lower bound `159124.5000257777`. The geometry
scan accepts 135 null-homotopic routes and freezes `(0.2,-0.01,0.65)`, with
other-critical clearance `0.0064859920929681136` and selected y-chart-zero
clearance `0.17001348479496647`.

An order-20 compressed-frame execution completed all 193 steps but was
correctly rejected because its final wrapping radius `2.128e-5` exceeded the
selected `1.9e-5` main cap. The same order, precision, local correction gate,
node, tail, and route then close under the uncompressed physical-generator
zonotope. It accepts 193 steps, rejects 102 trial steps, and yields main radius
`9.198311075311998e-7`. The 384-cell tail has radius
`3.2598659274185597e-6`; the full radius `4.560701455602612e-6` contains the
independent floating center and meets the fallback with margin
`1.8525900473199315e-5`.

## A161 d012 Standard-Pair Frontier

`d012/selected_017`, coefficient `+1`, closes on the certified nodal pair
`[1,3]`, whose interval Jacobian has lower bound `3052969.864483049`. The route
scan accepts 138 of 1122 null-homotopic candidates and freezes
`(0.32,0.01,0.86)`, with other-critical clearance
`0.004179802527816796` and selected y-chart-zero clearance
`0.13160082890764052`.

Taylor order 20 satisfies the unchanged local lift-correction gate. The
uncompressed physical-generator zonotope accepts 190 steps, rejects 100 trial
steps, and closes with main radius `5.743632409585513e-7`. Orientation is
selected with sign `-1` and base residual `6.004788336613063e-10`. The 384-cell
tail radius is `1.49679504168887e-6`; the full splice radius
`2.3084341584933558e-6` contains the independent floating center and meets the
A134 fallback with margin `2.0778167770308571e-5`.

## A162 d017 Stiff-Node Frontier

`d017/selected_022`, coefficient `+2`, closes on the certified nodal pair
`[1,2]`. Its interval node Jacobian has lower bound `41.87819506043567`, so this
row is more weakly conditioned than the immediately preceding rows. The route
scan nevertheless accepts 200 of 1122 null-homotopic candidates and freezes
`(0.45,0.01,0.86)`, with other-critical clearance
`0.010732452056156522` and selected y-chart-zero clearance
`0.07203228358389155`.

The order-20 uncompressed physical-generator zonotope resolves the stiff
near-node region without relaxing the local correction gate. It accepts 182
steps, rejects 95 trial steps, and closes with main radius
`3.831653826366047e-7`. Orientation is selected with sign `-1` and base residual
`2.416265037138939e-11`. The 384-cell tail radius is
`1.3301582466596076e-6`; the full splice radius `1.8720345043021782e-6`
contains the independent floating center and meets the A134 fallback with
margin `2.1214567424499748e-5`.

## A163 d051 Narrow-Clearance Frontier

`d051/selected_062`, coefficient `-2`, closes on the certified nodal pair
`[0,1]`, with interval node Jacobian lower bound `525079.1991958322`. The route
scan accepts 154 of 1122 null-homotopic candidates. Its top-ranked family is the
same straight radial homotopy; the frozen representative `(0.2,0,0.74)` has
other-critical clearance `0.0005434606878915084` and selected y-chart-zero
clearance `0.0669270710616152`.

The order-20 uncompressed physical-generator zonotope resolves the narrow
critical-value tube under the unchanged local correction gate. It accepts 259
steps, rejects 153 trial steps, and closes with main radius
`1.1786789306105185e-6`. Orientation is selected with sign `-1` and base
residual `1.9855193718527444e-11`. The 384-cell tail radius is
`3.526161225231306e-7`; the full splice radius `2.019519840246176e-6` contains
the independent floating center and meets the A134 fallback with margin
`2.1067082088555751e-5`.

## A164 d055 Contracting-Radius Frontier

`d055/selected_086`, coefficient `+1`, closes on the certified nodal pair
`[3,4]`, with interval node Jacobian lower bound `694082191.3623276`. The route
scan accepts 188 of 1122 null-homotopic candidates and freezes
`(0.6,0.01,0.65)`, with other-critical clearance `0.005978689209782696` and
selected y-chart-zero clearance `0.07183201724323864`.

The order-20 uncompressed physical-generator zonotope accepts 243 steps and
rejects 145 guarded trials. Its intermediate radius grows above `3.1e-6` and
then contracts under later transport, closing at main radius
`1.3338361979199125e-6`; only this completed endpoint enclosure is charged.
Orientation is selected with sign `-1` and base residual
`7.031356995868635e-10`. The 384-cell tail radius is
`2.761550554453152e-6`; the full splice radius `4.647876217234171e-6` contains
the independent floating center and meets the A134 fallback with margin
`1.8438725711567756e-5`.

## A165 d034 Refined-Tail and Y-Queue Frontier

`d034/selected_007`, coefficient `-3`, closes on the certified nodal pair
`[4,5]`, with interval node Jacobian lower bound `33208421.445407536`. The
standard 384-cell tail is correctly rejected because its orientation intervals
overlap. Halving the radial cells preserves the same sign rule and geometry;
the resulting 768-cell tail certifies radius `5.526991380122582e-6`.

The route scan accepts 441 of 1122 null-homotopic candidates. Its top radial
family has an intrinsic other-critical clearance of only
`0.00014908710399122414`; the frozen representative is `(0.2,0,0.74)`. The
order-20 zonotope resolves the narrow early pocket, accepts 288 steps, rejects
183 guarded trials, and closes with main radius `2.20656062847174e-6`.
Orientation is selected with sign `+1` and base residual
`1.936800243298604e-9`. The full splice radius `8.64753941698382e-6` contains
the independent floating center and meets the A134 fallback with margin
`1.4439062511818106e-5`.

## A166 d059 Native-Z Successor

`d059/selected_042`, coefficient `+3`, is the first append after exhaustion of
the ranked y-chart queue. Its native z-chart node closes on pair `[0,1]` with
interval node Jacobian lower bound `16.12989586070368`, quartic lower bound
`2.676811553144434`, and Hensel Jacobian lower bound `7.16532009104752`. The
standard 384-cell endpoint partition closes directly with tail radius
`3.2196170278442353e-9`.

All 1122 geometry-only routes are certified null-homotopic. The frozen ranked
representative `(0.2,0,0.82)` has other-critical clearance
`0.03020965880170749`, z-chart-zero clearance `0.25629873774204354`, and path
length `0.2625680655537892`. The order-20 uncompressed zonotope accepts 74
steps and rejects 21 guarded proposals, closing at main radius
`8.601425856598232e-8`. The selected orientation sign is `-1`, with base
residual `4.357017498414094e-12` versus opposite-sign residual
`1.6062874932938351`. The full splice radius `1.2486213707418872e-7` contains
the independent floating center and meets the A134 fallback with margin
`2.2961739791727738e-5`.

## A167 d031 Native-Z Successor

`d031/selected_048`, coefficient `-2`, closes next on native z-chart pair
`[4,5]`. The interval node Jacobian lower bound is `670.6966041106965`, the
quartic lower bound is `5.478527882165851`, and the Hensel Jacobian lower bound
is `30.014267755668655`. The standard 384-cell endpoint partition closes with
tail radius `1.0621430429624825e-8`.

All 1122 geometry-only routes again certify as null-homotopic. The frozen
representative `(0.2,0,0.65)` has other-critical clearance
`0.029595753830404022`, z-chart-zero clearance `0.25629873774204354`, and path
length `0.26714760965399653`. Its order-20 uncompressed zonotope accepts 132
steps and rejects 67 guarded proposals, closing with main radius
`1.816473192839754e-7`. The selected main-transport orientation is `-1`, with
base residual `2.859456150288752e-10` versus opposite-sign residual
`3.9105276796542054`. The full splice radius `2.675095345239243e-7` contains
the independent floating center and meets the A134 fallback with margin
`2.2819092394278002e-5`.

## A168 d039 Native-Z Successor

`d039/selected_037`, coefficient `-2`, closes next on native z-chart pair
`[1,2]`. The interval node Jacobian lower bound is `6.913856800884213`, the
quartic lower bound is `0.6723711048609368`, and the Hensel Jacobian lower
bound is `0.4520829026519169`. The coarse 48-segment endpoint partition is
correctly rejected at the nodal discriminant; its same-geometry 96-segment
refinement closes with tail radius `1.4066956168790059e-6`.

The geometry-only scan certifies 815 of 1122 routes as null-homotopic. The
frozen winner `(0.45,-0.01,0.86)` has other-critical clearance
`0.03370999370021831`, z-chart-zero clearance `0.25629873774204354`, and path
length `0.4800881923495244`. Its order-20 uncompressed zonotope accepts 103
steps and rejects 32 guarded proposals, closing with main radius
`1.0881261871947691e-7`. The selected main-transport orientation is `+1`, with
base residual `2.4939871080217148e-11` versus opposite-sign residual
`3.0640251347741305`. The full splice radius `1.5605798893147951e-6` contains
the independent floating center and meets the A134 fallback with margin
`2.1526022039487131e-5`.

## A169 d014 Native-Z Successor

`d014/selected_059`, coefficient `-1`, closes next on native z-chart pair
`[3,4]`. The interval node Jacobian lower bound is `139.58607960351011`, the
quartic lower bound is `8.32322355714877`, and the Hensel Jacobian lower bound
is `69.27605038227624`. The 384-segment endpoint partition is correctly
rejected at the nodal discriminant; its same-geometry 768-segment refinement
closes with tail radius `1.1550937359383619e-8`.

All 1122 geometry-only routes certify as null-homotopic. The frozen
representative `(0.2,0,0.65)` has other-critical clearance
`0.04818849350988268`, z-chart-zero clearance `0.25629873774204354`, and path
length `0.27480650421584873`. Its order-20 uncompressed zonotope accepts 75
steps and rejects 23 guarded proposals, closing with main radius
`1.2239440876842448e-7`. The selected main-transport orientation is `+1`, with
base residual `5.276917183896251e-12` versus opposite-sign residual
`0.9757357784224523`. The full splice radius `1.8464276241303426e-7` contains
the independent floating center and meets the A134 fallback with margin
`2.2901959166388892e-5`.

## A170 d075 Native-Z Successor

`d075/selected_067`, coefficient `-2`, closes next on native z-chart pair
`[3,4]`. The interval node Jacobian lower bound is `1297686.090009849`, the
quartic lower bound is `17.895519759930497`, and the Hensel Jacobian lower
bound is `320.249627478063`. The standard 384-segment endpoint partition
closes with tail radius `5.82789970593467e-6`.

The geometry-only scan certifies 606 of 1122 routes as null-homotopic. The
frozen winner `(0.2,0,0.65)` has other-critical clearance
`0.021040347992309895`, z-chart-zero clearance `0.23559468062379893`, and path
length `0.7056833213801024`. Its order-20 uncompressed zonotope accepts 149
steps and rejects 55 guarded proposals, closing with main radius
`2.127205331505899e-7`. The selected main-transport orientation is `+1`, with
base residual `1.8232437827963128e-10` versus opposite-sign residual
`1.9220381139388214`. The full splice radius `6.12873136418557e-6` contains the
independent floating center and meets the A134 fallback with margin
`1.6957870564616357e-5`.

## A171 d018 Native-Z Successor

`d018/selected_054`, coefficient `-2`, closes next on native z-chart pair
`[4,5]`. The interval node Jacobian lower bound is `471609.6633877652`, the
quartic lower bound is `27.009752062579917`, and the Hensel Jacobian lower
bound is `729.5267064820401`. The standard 384-segment endpoint partition
closes with tail radius `1.2428286488841425e-6`.

The geometry-only scan certifies 1119 of 1122 routes as null-homotopic. The
frozen winner `(0.45,-0.01,0.86)` has other-critical clearance
`0.02032832356063741`, z-chart-zero clearance `0.25629873774204354`, and path
length `0.3200380974389225`. Its order-20 uncompressed zonotope accepts 111
steps and rejects 55 guarded proposals, closing with main radius
`1.1239108844990107e-7`. The selected main-transport orientation is `-1`, with
base residual `7.877677759638932e-11` versus opposite-sign residual
`4.280590888033315`. The full splice radius `1.4017736589266863e-6` contains
the independent floating center and meets the A134 fallback with margin
`2.168482826987524e-5`.

## A172 d001 Native-Z Successor

`d001/selected_033`, coefficient `+1`, closes next on native z-chart pair
`[0,1]`. The interval node Jacobian lower bound is `3472.4749372847405`, the
quartic lower bound is `49.70732540723015`, and the Hensel Jacobian lower bound
is `2470.8181991402685`. The standard 384-segment endpoint partition closes
with tail radius `5.4652383241204927e-7`.

The geometry-only scan certifies 902 of 1122 routes as null-homotopic. The
frozen winner `(0.55,0.03,0.86)` has other-critical clearance
`0.060544030484850735`, z-chart-zero clearance `0.16146486010299235`, infinity
clearance `0.3284480736549116`, and path length `0.547227549315182`. Its
order-20 uncompressed zonotope accepts 117 steps and rejects 36 guarded
proposals, closing with main radius `4.5844626040661814e-6`. The selected
main-transport orientation is `-1`, with base residual `8.040205297707689e-11`
versus opposite-sign residual `4.280590888175318`. The full splice radius
`7.0299094261372383e-6` contains the independent floating center and meets the
A134 fallback with margin `1.6056692502664689e-5`.

## A173 d046 Native-Z Successor

`d046/selected_045`, coefficient `+3`, closes next on native z-chart pair
`[1,2]`. The interval node Jacobian lower bound is `4.984926703297502`, the
quartic lower bound is `2.970580168206725`, and the Hensel Jacobian lower bound
is `8.824346535743095`. The standard 384-segment endpoint partition is too
coarse to separate the nodal discriminant; the same-contour 768-segment
refinement closes with tail radius `1.0406598907053424e-6`.

The geometry-only scan certifies 495 of 1122 routes as null-homotopic. The
frozen winner `(0.45,0.02,0.70)` has other-critical clearance
`0.029599762022191837`, z-chart-zero clearance `0.0872283695522862`, infinity
clearance `0.34557369853455555`, and path length `0.7168410769128437`. Its
order-20 uncompressed zonotope accepts 164 steps and rejects 66 guarded
proposals, closing with main radius `6.883023908842079e-7`. The selected
main-transport orientation is `+1`, with base residual `5.29614314520417e-11`
versus opposite-sign residual `1.6062874932609106`. The full splice radius
`2.0140664531709267e-6` contains the independent floating center and meets the
A134 fallback with margin `2.1072535475630998e-5`.

## A174 d089 Native-Z Successor

`d089/selected_032`, coefficient `-1`, closes next on native z-chart pair
`[1,2]`. The interval node Jacobian lower bound is `82.94027767247935`, the
quartic lower bound is `3.5514768611306176`, and the Hensel Jacobian lower
bound is `12.612987895146185`. The standard 384-segment endpoint partition
closes with tail radius `2.1323743014389777e-9`.

All 1122 geometry-only routes certify as null-homotopic. The frozen winner
`(0.35,0,0.70)` has other-critical clearance `0.033175593766291145`,
z-chart-zero clearance `0.25629873774204354`, infinity clearance
`0.3535533905922738`, and path length `0.21617181149344228`. Its order-20
uncompressed zonotope accepts 71 steps and rejects 16 guarded proposals,
closing with main radius `2.9346360173223173e-7`. The selected main-transport
orientation is `-1`, with base residual `1.3006831943897518e-12` versus
opposite-sign residual `2.1041919264343365`. The full splice radius
`4.171525822549427e-7` contains the independent floating center and meets the
A134 fallback with margin `2.2669449346546984e-5`.

## A175 d069 Native-Z Successor

`d069/selected_078`, coefficient `-2`, closes next on native z-chart pair
`[3,4]`. The interval node Jacobian lower bound is `859.5126035729988`, the
quartic lower bound is `6.574920546388487`, and the Hensel Jacobian lower bound
is `43.22958019132149`. The standard 384-segment endpoint partition closes
with tail radius `9.208371682944972e-7`.

The geometry-only scan certifies 526 of 1122 routes as null-homotopic. The
frozen winner `(0.35,-0.02,0.70)` has other-critical clearance
`0.03037574507359249`, z-chart-zero clearance `0.25629873774204354`, infinity
clearance `0.3535533905922738`, and path length `0.7859157901244211`. Its
order-20 uncompressed zonotope accepts 138 steps and rejects 37 guarded
proposals, closing with main radius `3.0482279579327836e-7`. The selected
main-transport orientation is `-1`, with base residual `4.906159612591468e-11`
versus opposite-sign residual `0.975735778415619`. The full splice radius
`1.3519217159085886e-6` contains the independent floating center and meets the
A134 fallback with margin `2.1734680212893338e-5`.

## A176 d050 Native-Z Successor

`d050/selected_047`, coefficient `+1`, closes next on native z-chart pair
`[1,2]`. The interval node Jacobian lower bound is `3.2835928474746736`, the
quartic lower bound is `2.5918659000328943`, and the Hensel Jacobian lower
bound is `6.717768843753326`. The standard 384-segment endpoint partition is
too coarse to separate the nodal discriminant; the same-contour 768-segment
refinement closes with tail radius `3.890338897381829e-10`.

The geometry-only scan certifies 992 of 1122 routes as null-homotopic. The
frozen winner `(0.20,-0.01,0.86)` has other-critical clearance
`0.020935564535092217`, z-chart-zero clearance `0.25629873774204354`, infinity
clearance `0.3535533905922738`, and path length `0.39095929300124943`. Its
order-20 uncompressed zonotope accepts 92 steps and rejects 30 guarded
proposals, closing with main radius `1.258544559744545e-7`. The selected
main-transport orientation is `-1`, with base residual `4.1474892260273116e-11`
versus opposite-sign residual `0.9757357784114155`. The full splice radius
`1.78374099046863e-7` contains the independent floating center and meets the
A134 fallback with margin `2.2908227829755063e-5`.

## Boundary

This theorem validates reusable route selection, anti-wrapping transport,
certified main/tail cutoff-period handoff, the compact-H1 orientation gate, and
the native `z`-chart adapter. A177-A205 extend the construction to every one of
the 29 remaining native-z supports. A206 promotes the refined 768-segment
`d047` hard row after proving that its new cutoff payload is contained in the
already-certified main-transport input. The append-only ledger is therefore
exactly 71/71 support and L1 weight 123/123, with no ranked or partial row left.

A207 then applies the frozen A130/A131 canonical signs `sigma_d` to the raw
holomorphic interval packets and directly sums the exact integer chain. The
weighted-thimble radius is `0.0004842494354306837`; its center is only
`2.677700007837837e-06` from the independent A131 center. After adding the
certified handle, the radius-plus-displacement cost is
`0.0011918737811637164`, below the A133 strict budget
`0.003338125011653557`. The final E32 residual has an imaginary interval wholly
below zero and hence absolute-value lower bound
`0.0016980843713102275`. Thus the weighted 71-thimble enclosure and frozen
height-four carrier decision are closed: that carrier is rejected, while the
existence or selection of another covariant carrier remains open.
