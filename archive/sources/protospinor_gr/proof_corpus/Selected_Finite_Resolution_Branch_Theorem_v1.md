# Selected Finite Resolution Branch Theorem v1

## Result

The finite-resolution branch is no longer symmetric among `N=64`, `N=79`, and
`N=448` once the q79 exact-charge proof is imported.

The selected finite CP quotient is:

```text
Gamma_CP ~= Z64 x Z7 ~= Z448
q64 = 15
q7 = 2
q = 79 mod 448
```

Therefore the finite quotient branch selected by the existing MTT/q79 corpus is:

```text
N = |Gamma_CP| = 448
```

## Why the other candidates no longer serve as the selected branch

```text
N=64   closed dyadic carrier, but it omits the selected Z7 charge factor
N=79   selected CP label q mod 448, not a quotient size
N=448  selected CP quotient Z64 x Z7 ~= Z448
```

## Guardrail

This does not say that the full topology is exactly `Z448`. The q79 corpus
already separates the ambient family carrier from the selected observable
quotient:

```text
pi: Z1344 -> Z448
ker(pi) = Z3-family
```

So the rigorous statement is:

```text
MTT selects a family-trivial CP character factoring through Z448.
```

## Consequence for Omega0

If the one-cell quotient tolerance rule is accepted,

```text
epsilon_adm = 1/|Gamma_CP|,
```

then the selected tolerance is:

```text
epsilon_adm = 1/448 = 0.00223214285714286.
```

The remaining formula becomes:

```text
Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448*C_Q)).
```

If the later sharp-semigroup theorem proves `C_Q=1`, this specializes to:

```text
Omega0 = chi_omega * sqrt(alpha_phys) * sqrt(15/log(448))
sqrt(15/log(448)) = 1.56750938592616
R1(sigma=1) = 0.637954712729934
```

## Still Open

This theorem closes the source-certified finite branch, not the whole physical
normalization. Remaining gates:

```text
derive the quotient-cell admissibility rule from the selected functional
prove whether C_Q=1 is the sharp physical semigroup bound
select alpha_phys or an equivalent action/unit anchor
select chi_omega
```
