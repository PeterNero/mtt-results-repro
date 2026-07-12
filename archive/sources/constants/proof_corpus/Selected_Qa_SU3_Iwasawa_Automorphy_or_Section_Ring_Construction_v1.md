# Selected Qa/SU3 Iwasawa Automorphy or Section Ring Construction v1

## Purpose

This artifact tries the next construction step after the line-bundle
section-ring interface.  It tests three possible interpretations:

```text
literal scalar constants,
torus-style theta/Appell-Humbert shortcut,
Iwasawa automorphy/section-ring construction.
```

## Route Decision

```text
literal constant route: rejected, because all required section charges are nonzero
torus theta shortcut: rejected until an Iwasawa transfer theorem is supplied
selected source direct route: blocked, because section data are not printed
automorphy route: open, requires factor-of-automorphy cocycle
direct operator exit: open, if Dolbeault/Cech/rho_E packet is supplied
```

The external literature signal supports caution: Iwasawa manifolds are compact
complex homogeneous/non-Kahler quotients, and Picard/line-bundle computations
on compact complex parallelizable quotients are nontrivial.  This is not a
ready permission to import torus theta formulas.

## Symbolic Rank-One Relation

If every required section space is one-dimensional, and if products are
nonzero,

```text
eF_i * eG_i = m_i eP,
```

then the monad condition reduces to:

```text
m1*u1*v1 + m2*u2*v2 + m3*u3*v3 + m4*u4*v4 + m5*u5*v5 = 0
```

All five products land in the expected target charge:

```text
P = K2 - K1 = (-1,1,0)
```

So we now have a symbolic construction pattern.  For example, if `m1,m2` are
nonzero, the pair

```text
u1 = 1, v1 = m2, u2 = 1, v2 = -m1
```

cancels the first two terms.  This is not yet closure, because the section
dimensions, bases, multiplication constants, and local-freeness test are not
known.

## Required Automorphy Packet

The needed object is:

```text
a_q(gamma1 gamma2, z) = a_q(gamma1, gamma2.z) a_q(gamma2, z)
s_q(gamma.z) = a_q(gamma,z) s_q(z)
a_p a_q = a_{p+q}
```

for every required charge `q`, plus section bases and multiplication constants.

## Verdict

```text
all products land in P: yes
symbolic rank-one relation built: yes
literal constant route retired: yes
torus theta shortcut retired until transfer theorem: yes
automorphy schema built: yes
actual automorphy factors found: no
section dimensions found: no
explicit f,g constructed: no
g*f=0 proved: no
Qa/SU3 closed: no
target fitting used: no
```

Next artifact:

```text
Selected_Qa_SU3_Iwasawa_Automorphy_Cocycle_Data_or_NoGo_v1
```

