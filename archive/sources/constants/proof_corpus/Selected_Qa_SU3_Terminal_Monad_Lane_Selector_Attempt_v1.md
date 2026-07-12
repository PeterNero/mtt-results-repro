# Selected Qa/SU3 Terminal Monad Lane Selector Attempt v1

## Result

The terminal monad-difference lane has a closed conditional uniqueness theorem.

From the Iwasawa monad line table, the terminal differences are:

```text
L1-K2=(-2,-1,1)
L2-K2=(-1,0,-1)
L3-K2=(1,-2,0)
L4-K2=(1,-1,-1)
L5-K2=(2,0,1)
```

Inside this lane, the only central-neutral difference whose double is the
visible target is:

```text
L3-K2=(1,-2,0)
2(L3-K2)=(2,-4,0)
```

The printed `g3` type is the dual `K2-L3=(-1,2,0)`, so it identifies the same
line up to duality.

## What Closed

```text
conditional uniqueness inside terminal lane: yes
unique zero-central terminal difference: yes
unique double-target match: yes
proof frontier no longer arithmetic: yes
typed monad recovery attempt closed negative: yes
spectral fallback identified: yes
```

## What Did Not Close

The source-lane selector is still missing:

```text
source lane selector for terminal monad differences: no
typed sections or transition data: no
Pic0 selection or quotient: no
binding to Appell-Humbert/Cech transitions: no
same-source D_E/dotD/Riesz/Green: no
full SM closure: no
```

The typed monad route cannot close from the current corpus because explicit
`f_i,g_i` sections, transition functions, Cech maps, exactness checks, and
selected `H^1(X,E)` representatives were not recovered.

## Next Routes

There are now two honest routes:

```text
1. Prove terminal monad lane selection:
   MTT selects L_i-K2 as the visible ordered L source lane,
   Pic0 is selected or quotiented,
   typed sections or equivalent transition/rho_E data are supplied.

2. Use the non-invariant spectral Galerkin fallback:
   construct selected D_E,
   use a finite basis beyond left-invariant forms,
   compute low spectrum and Riesz projector,
   prove anti-family/gap/error bounds,
   derive dotD_alpha1 and Green data.
```

## Gate Verdict

```text
terminal monad lane selector closed: no
conditional uniqueness closed: yes
remaining gate is lane selector or spectral source: yes
target fitting used: no
```

