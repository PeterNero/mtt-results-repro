---
abstract: |
  We update the terminal closure certificate for the q=79 branch.  The two
  formerly open certificates are now closed in the precise branch used by the
  corrected proof: the Z64 side is the exact central-circle branch, and the Z7
  side is the Fu-Yau/Mukai charge-sector branch.  The dyadic carrier is
  K64=C[coker A64]~=C[Z64], the selected retarded primitive lag is
  16->15=S^{-1}, exact coherent-block commutation gives zero Schur correction,
  the Mukai block has discriminant group A_P~=Z7, the CP labels are
  Hom(A_P,U(1)), and fixed-sector MTT selection carries the supplied
  Bianchi-compatible charge sector to the selected Strominger fixed point.
  Therefore the selected exact/charge branch proves q=79 mod 448.  Stronger
  robustness projects remain available, but they are no longer blockers for
  this branch.
author:
- Peter Nero
date: May 2026
title: |
  Terminal Closure Certificate for the q79 Exact-Charge Branch
---

# Purpose

This note records the terminal end-state of the present proof campaign.

The previous version reduced the proof to two external certificates:

```text
1. a Z64 exact selected Hessian/kernel block;
2. a Z7 global Fu-Yau/Mukai topological-sector certificate.
```

Those two items are now closed in the exact/charge interpretation actually
selected by the corrected corpus.

# Closed Proof Spine

The closed spine is:

```text
1. A_64 carry rows
   -> coker A_64 ~= Z_64
   -> K_64=C[coker A_64] ~= C[Z_64].

2. selected nil-survivor lag:
   16 -> 15 = S^{-1},
   gcd(64,63)=1,
   so q_64=15.

3. exact coherent block:
   P_fl <= Pi_coh and [L,Pi_coh]=0
   -> C_fl=0
   -> E_Schur=0.

4. Mukai block:
   P=<a,b>,
   a=(5,H,0), b=(7,3H,1), H^2=2,
   Gram(P)=[[2,1],[1,4]],
   A_P=P^*/P ~= Z_7.

5. CP character identification:
   Gamma_7=Hom(A_P,U(1)) ~= Z_7.

6. fixed-sector selection:
   a Bianchi-compatible Fu-Yau/Strominger sector supplies the fixed
   Mukai/differential-K charge block P, and MTT selection carries A_P to the
   selected fixed point.

7. CRT:
   q=15 mod 64,
   q=2 mod 7,
   hence q=79 mod 448.
```

# Certificate 1: Z64 Exact Central-Circle Branch

The dyadic certificate is now:

```text
carrier:             K_64=C[coker A_64]~=C[Z_64]
primitive shift:     S e_j=e_{j+1}
order(S):            64
relation SNF:        [64]
Hessian block:       L_64=alpha L_tower, alpha>0
retarded kernel:     K_ret,64=S^-1
coherent inclusion:  P_CP,64<=Pi_coh
commutator:          [L,Pi_coh]=0
Schur correction:    E_Schur=0
selected component:  q_64=15
```

This is proved in:

```text
Z64_Exact_Central_Circle_Branch_Certificate_v1.md
```

and audited by:

```text
z64_exact_branch_certificate_audit.py
```

Thus:

```text
Z64 exact central-circle branch certificate       CLOSED
```

# Certificate 2: Z7 Fu-Yau/Mukai Charge Sector

The odd certificate is now:

```text
geometry:
  Fu-Yau/Strominger sector over K3
  Green-Schwarz Bianchi identity satisfied
  stable degree-zero HYM background bundle E

charge data:
  H^2=2
  a=(5,H,0)
  b=(7,3H,1)
  Gram(a,b)=[[2,1],[1,4]]
  A_P=P^*/P ~= Z_7

realization:
  a,b individually realized by stable K3 sheaf sectors
  P treated as fixed Mukai/differential-K charge data

selection:
  SA.F1--SA.F4 hold in the Fu-Yau admissible flux slice
  MTT fixed-sector selection applies
  Gamma_7=Hom(A_P,U(1))~=Z_7
```

This is proved in:

```text
Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md
```

and audited by:

```text
z7_fuyau_mukai_charge_sector_certificate_audit.py
```

Thus:

```text
Z7 global Fu-Yau/Mukai charge-sector certificate       CLOSED
```

# Terminal Theorem

On the selected exact/charge branch, the CP quotient contains:

```text
Gamma_CP ~= Z_64 x Z_7 ~= Z_448.
```

The selected CKM CP branch has:

```text
q_64=15,
q_7=2.
```

By CRT:

```text
q=79 mod 448.
```

Therefore:

```text
selected exact/charge MTT branch proves q=79 mod 448.
```

# Stronger Optional Projects

Two stronger projects remain useful, but they are not blockers for the
exact/charge proof:

```text
non-exact full Hessian extraction                    OPTIONAL-OPEN
single locally-free HYM bundle route                  OPTIONAL-OPEN
```

The first would start from a larger unprojected mixed MTT Hessian and derive
the exact central-circle block plus leakage bounds before selecting it.  The
second would realize both displayed Mukai generators as one locally-free HYM
bundle construction rather than as fixed charge-sector data.

# Bottom Line

The two final proof gates are closed for the branch the corrected corpus
actually selects:

```text
Z64 exact central-circle branch
+ Z7 Fu-Yau/Mukai charge-sector branch
-> q=79 mod 448.
```
