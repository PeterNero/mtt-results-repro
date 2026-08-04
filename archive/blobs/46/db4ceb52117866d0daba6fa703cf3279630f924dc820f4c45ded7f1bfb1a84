# Selected Normalization Minimization Functional v1

## Purpose

This gate builds the strongest current no-knob route toward an absolute
normalization:

```text
selected heterotic topology and flux integers
-> MTT/Strominger selection functional Xi
-> central-circle exact branch
-> candidate normalization output.
```

The target is to decide whether this route already selects an absolute physical
scale or whether it still leaves a scale modulus.

## Source Data

The MTT/Strominger corpus supplies a genuine selection functional:

```text
Xi[g,Phi,B;A,omega^+;Hhat,K,Lambda]
```

with Green-Schwarz/Bianchi constraints, gauge-invariant `Hhat`, and an OU
variance term. Its critical points are exactly Hull-Strominger solutions, and
under SA.F1--SA.F4 the Hessian is positive in fixed gauges, giving a unique
local minimizer in a fixed topological sector.

The explicit heterotic flux corpus supplies integer flux data and componentwise
Bianchi equations:

```text
dH = alpha'/4 (Tr_grav R_+^2 - Tr F^2),
```

with examples:

```text
Iwasawa:  r3^2 = 8(2pi)^2 / (16/alpha' + 8/R^4),
LensNil:  anomaly equations fix R1/R for fixed integers (f,h).
```

The same corpus states the important obstruction:

```text
Iwasawa leaves an overall volume/shape modulus at first order in alpha',
LensNil fixes the ratio R1/R while leaving at most an overall scale modulus,
higher alpha' corrections require parametric control.
```

The exact central-circle branch supplies

```text
alpha_int = 1,
lambda_* = 15,
R1(N) = sqrt(log N / 15)
```

in canonical internal action units.

## Candidate Functional

For fixed selected topological data `T`, flux integers `m`, and central-circle
branch `N`, define the normalization search functional

```text
F_norm(s; T,m,N)
  = Xi_reduced(s; T,m)
  + B_Bianchi(s; T,m)
  + B_quant(s; T,m)
  + B_circle(s; N)
  + B_control(s; T,m),
```

where:

```text
s              = remaining positive dilation / string-unit scale,
Xi_reduced     = MTT/Strominger selection potential restricted to the selected sector,
B_Bianchi      = squared residual of the componentwise Green-Schwarz Bianchi equations,
B_quant        = infinite barrier outside integral flux and gerbe periods,
B_circle       = penalty enforcing the exact central-circle R1(N) branch,
B_control      = barrier enforcing large-volume / small-flux / bounded-geometry control.
```

A genuine no-knob absolute normalization requires:

```text
argmin_{s>0} F_norm(s; T,m,N) = {s_*}
```

with `s_*` finite, positive, unique, and selected before any target
dimensionful observable is evaluated.

## Executable Reduction

The current corpus supports the following executable reduced checks.

### Iwasawa

In internal alpha-prime units, write `alpha'=1`. Then the source equation gives

```text
r3^2(R) = 8(2pi)^2 / (16 + 8/R^4).
```

This is a one-parameter family in `R`. It is a strong Bianchi constraint, not a
unique absolute scale.

### LensNil

For fixed flux integers `(f,h)`, the anomaly equations fix

```text
R1/R,
```

and therefore isolate the invariant shape. The source still says there remains
at most an overall scale modulus at this order. Again this is not yet a unique
absolute scale.

### Central Circle

The exact central-circle branch selects an internal value

```text
R1(N) = sqrt(log N / 15).
```

This can convert a ratio into an internal value if the LensNil `R1/R` ratio is
source-certified. It still does not supply an SI scale unless alpha-prime,
string length, or another dimensional anchor is independently selected.

## Gate Theorem

The selected flux/topology minimization route is now well-posed but not
physically closed.

What is closed:

```text
1. The admissible functional form is source-supported.
2. The no-target-constant rules are explicit.
3. Current flux equations are executable constraints.
4. The current corpus selects shapes, ratios, and internal branch units.
```

What is not closed:

```text
1. A source-certified scale-lifting term depending nontrivially on the remaining dilation s.
2. A proof that F_norm(s) is proper/coercive in s.
3. A proof that the minimizer in s is unique.
4. A physical dimensional anchor converting internal units to SI units.
```

## Correct Next Lemma

The next missing object is not another candidate list. It is:

```text
Scale-Lifting Lemma for the Selected Flux/Strominger Functional
```

stating that the selected `Xi` plus higher-alpha-prime/OU/central-circle
correction produces a coercive one-variable reduced functional

```text
F_scale(s) -> +infinity as s -> 0 or s -> infinity,
F_scale has exactly one critical point,
F_scale''(s_*) > 0.
```

Only then can the program output a no-knob absolute normalization.

## Verdict

The minimization route is now formulated as an executable gate. It does not yet
close physical absolute constants. It reduces the open problem to one precise
lemma:

```text
derive the scale-lifting term and prove unique positive minimization.
```

This is the correct next research target.
