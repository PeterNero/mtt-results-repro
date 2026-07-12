# Selected Qa/SU3 Visible Rank2 VAlpha Source Attempt v1

## Result

The q79 visible source route has been sharpened to the rank-two non-split
extension

```text
0 -> L -> V_alpha -> L^{-1} -> 0
```

with

```text
L=(1,-2,0),  L^2=(2,-4,0),
c1(V_alpha)=0,  c2(V_alpha)=4 alpha_1,  ch2(V_alpha)=-4 alpha_1.
```

This closes the conditional Ext mathematics, but not the selected source
theorem.

## What Closed

The q79 certificates now provide:

```text
topological rank-two target: closed
explicit Appell-Humbert automorphy for L^2: closed
conditional finite H^1 packet: h1=8
closed non-exact Ext vector: yes
validator exit: 0
observed masses/mixings used: no
benchmark flavor entries used: no
```

The validated cochain packet is algebraically good:

```text
candidate role: UNSELECTED_FIXTURE
d1 d0 = 0: yes
dim ker d1: 8
rank d0: 0
h1: 8
extension class closed: yes
extension class exact: no
nonzero Ext class: yes
```

So the old blocker "maybe H^1(X,L^2) is zero or undefined" is gone for the
base-pullback model.  The remaining blocker is source selection.

## What Did Not Close

The packet still does not promote to selected MTT data:

```text
selected source promotes: no
promotes to non-split V_alpha input: no
selected L^2 packet: no
unique L branch selected: no
neutral Pic0 character selected: no
non-split stability proved: no
HYM or Route-C residual proved: no
same-source D_E/dotD/Riesz/Green: no
full SM closure: no
```

The q79 selector obstruction proves that the current closed invariants cannot
uniquely select `L=(1,-2,0)`.  The target and swapped branch are degenerate
under base swap, and flat Pic0 twists are invisible to the current curvature
and topology data.

## Correct Next Gate

The next object is therefore:

```text
Selected_Pullback_L2_Branch_Orientation_Source.v1
```

It must break both:

```text
base-swap degeneracy between target and swapped branch
flat Pic0 character degeneracy
```

Allowed ways to close it are:

```text
selected target Gauduchon wall r1:r2=sqrt(2):1
selected ordered integral Cech/automorphy/D_E source
same-source D_E/dotD/Hessian term ordering the base factors
holonomy-sensitive term selecting or quotienting Pic0 characters
```

After that source certificate exists, the same H1=8 matrices can be rerun as
`SELECTED_DATA`; then the proof must still establish non-split stability,
HYM/Strominger or Route-C residual closure, and the same-source
`D_E/dotD/Riesz/Green` packet.

## Gate Verdict

```text
visible rank-two V_alpha source closed: no
conditional Ext math closed: yes
remaining gate is selector, not Ext existence: yes
target fitting used: no
```

