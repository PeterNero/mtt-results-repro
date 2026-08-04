# Canonical q79 Damping-to-Pointer Isometry Theorem

## Statement

Let `H` be the selected finite q79 carrier, let `P=P_Haar` be its normalized
Reynolds projector, and let `Q=I-P`. For `0 <= a <= 1`, define

```text
S_a = P + a Q,
C_a = sqrt(1-a^2) Q,
V_a z = S_a z tensor |0> + C_a z tensor |1>.
```

Then `V_a:H -> H tensor C^2` is an isometry. Its two pointer effects are

```text
E_0 = P + a^2 Q,
E_1 = (1-a^2) Q,
E_0 + E_1 = I.
```

After the pointer is traced out, the reduced channel is

```text
Phi_a(rho) = S_a rho S_a^* + C_a rho C_a^*.
```

It leaves the diagonal `P/Q` blocks fixed and multiplies each cross block by
`a`. At `a=0`,

```text
Phi_0(rho) = P rho P + Q rho Q,
```

so the asymptotic damping limit is exactly the nonselective measurement channel
for the selected binary `P/Q` context.

Moreover, the isometry has the explicit unitary completion on
`H tensor C^2 = H direct-sum H`

```text
      [ P+aQ              -sqrt(1-a^2)Q ]
U_a = [                                     ].
      [ sqrt(1-a^2)Q       P+aQ            ]
```

For `0<a<1`, its two Kraus operators are linearly independent, so the channel
has Kraus rank two and a two-dimensional pointer is minimal.

## Proof

Because `P` and `Q` are complementary orthogonal projectors,
`P^2=P`, `Q^2=Q`, and `PQ=QP=0`. Therefore

```text
V_a^* V_a
 = S_a^* S_a + C_a^* C_a
 = P + a^2 Q + (1-a^2)Q
 = I.
```

The effect formulas follow from the same calculation. Expanding `Phi_a` into
the four `P/Q` matrix blocks proves that its diagonal blocks are fixed and its
cross blocks acquire exactly one factor of `a`. Setting `a=0` proves the final
formula. Since the two unitary blocks commute and their squared norms sum to
the identity, direct block multiplication gives `U_a^*U_a=I`. The first Kraus
operator has a nonzero `P` component whereas the second has none, proving
linear independence whenever the loss amplitude is nonzero. The repository
certificate checks every identity over the rationals at the exact witness
`a=3/5`, `sqrt(1-a^2)=4/5`.

## Scope

This theorem closes a canonical trace-preserving dilation and branch-recording
map for the already selected q79 binary response. It does not establish that
one pointer value is objectively realized, derive the physical attenuation
law or clock scale, or select general system-apparatus couplings. Any unitary
extension away from the image of `V_a` is nonunique and is not treated as new
physical source data. The displayed real-positive completion fixes a canonical
representative after the two pointer labels and their orientation are chosen;
it does not claim that those labels constitute an objective outcome mechanism.
