# Selected U1/SU2 Threshold Index Source Selector or Operator Spectrum v1

## Result

This artifact adds the source theorem for the motivated `2/3` U1 threshold
index.  It does not yet promote `2/3` to selected electroweak closure.

Derived source index:

```text
U1 = 2/3
SU2 = 1/1
```

## Source Theorem

```text
SharedCentralCircleQuotientSelectsTwoThirdsU1ThresholdWeight
```

Statement:

```text
For a selected U1 threshold carrier with three isotropic modal directions, if exactly one direction is the shared central-circle universal mode and the physical quotient removes that universal mode before determinant evaluation, then the normalized U1 threshold index is (3-1)/3=2/3.
```

Proof:

- Model the raw U1 threshold carrier as a 3-dimensional isotropic trace space V.
- Let s be the selected shared central-circle universal direction.
- The physical quotient for weak-split thresholds uses P_perp = I - |s><s|/<s,s>.
- The normalized trace weight is Tr(P_perp)/Tr(I_V).
- Since rank(P_perp)=2 and dim(V)=3, the weight is 2/3.
- This quotient is source-based only if s is selected before electroweak comparison and the selected U1 operator uses this quotient trace.

## Corpus Support

- `central_circle_neutrality`: CENTRAL_CIRCLE_NEUTRAL_TERMINAL_LANE_FILTER_PROVED_SELECTOR_OPEN
- `hypercharge_structure`: SELECTED_HYPERCHARGE_NORMALIZED_THRESHOLD_INTERFACE_BUILT_VALUES_OPEN
- `stack_determinants`: SELECTED_STACK_DETERMINANT_SOURCE_STATUS_CERTIFIED_VALUES_OPEN
- `su2_quotient`: SU2_NONABELIAN_GHOST_QUOTIENT_REDUCED_NOT_CLOSED

## Promotion Hypotheses

- `H1_three_direction_u1_threshold_carrier`: OPEN - selected U1 threshold carrier is a 3-direction isotropic modal trace space
  Reason: current sources describe circle/lens/nil and hypercharge structure but do not emit the selected U1 threshold trace carrier
- `H2_exactly_one_shared_central_universal_mode`: PARTIAL_SUPPORT - one and only one U1 threshold direction is the shared central-circle universal mode
  Reason: central-circle neutrality is source-supported, but not yet tied to the U1 threshold operator domain
- `H3_physical_quotient_removes_shared_mode`: OPEN - the weak-split determinant quotient removes the universal shared mode before finite determinant evaluation
  Reason: the current physical quotient/projector schema is built, but the selected U1 kernel/projector is not supplied
- `H4_SU2_unit_index_or_selected_spectrum`: OPEN - SU2 threshold weight is selected as 1 in this index comparison, or the selected SU2 spectrum replaces the index model
  Reason: SU2 flat/universal FP branch is identified but not selected; non-flat branch still requires spectrum
- `H5_no_target_selection`: CLOSED_FOR_THIS_THEOREM - the quotient and index are selected without using lambda_12 or measured electroweak data
  Reason: the theorem derives 2/3 from rank quotient only and does not use the diagnostic target

## Decision

```text
source_theorem_built = true
derived_U1_weight = 2/3
uses_electroweak_target = false
promoted_to_selected_threshold_index = false
I_1_I_2_payloads_filled = false
measured_electroweak_closure = false
```

## Documentation Contract For Later

When a later artifact claims that `2/3` is selected by shared-circle or
complex-nesting structure, it must cite this theorem and fill:

- `H1_three_direction_u1_threshold_carrier`
- `H2_exactly_one_shared_central_universal_mode`
- `H3_physical_quotient_removes_shared_mode`
- `H4_SU2_unit_index_or_selected_spectrum`

## Guardrails

- This theorem is not an electroweak fit and does not use lambda_12 as input.
- Do not promote 2/3 until the selected U1 threshold carrier/projector is supplied.
- Do not assume SU2 weight 1 if the selected SU2 operator spectrum or FP quotient changes it.
- Target-near rational hits remain rejected unless a separate source theorem selects them.

## Next Required Object

```text
Selected_U1_Threshold_Carrier_Projector_or_SU2_Operator_Spectrum_v1
```
