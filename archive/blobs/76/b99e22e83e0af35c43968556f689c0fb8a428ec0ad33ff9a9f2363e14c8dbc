# Selected Heterotic BN CentralRankOperator or SmoothEQa SourceEmission v1

## Result

```text
status = HETEROTIC_BN_CENTRALRANKOPERATOR_SOURCEEMISSION_SIGNED_INTERTWINER_CLOSED_POSITIVE_FINITEPART_OPEN
C_tau_signed_intertwiner_closed = true
positive_finitepart_for_C_tau_closed = false
operator_identity_closed_for_signed_layer = true
operator_identity_closed_for_positive_finitepart_layer = false
next_required_artifact = Selected_Heterotic_Ctau_PositiveFinitePart_or_SmoothDiracConvention_SourceTheorem_v1
```

## Theorem

The phase-preserving End(E)->B_N embedding source-selects the diagonal central-rank operator C_tau on B_N. Its compression P^T C_tau P is exactly the internal signed tau/D_E operator, so the signed operator-identity layer is closed. This does not close the positive finite-part layer: C_tau is signed and has zero modes, C_tau^2 loses the tau orientation, and positive shifts are unselected. The live no-knob route is a source-selected chiral Dirac/eta or smooth E_Qa convention that keeps sign data while feeding a positive operator to the already selected finite determinant policy.

## Regularization Fork

```json
{
  "C_tau_signed": {
    "eigenvalues_embedded_11": {
      "-1": 4,
      "0": 3,
      "1": 4
    },
    "eigenvalues_full_BN": {
      "-1": 9,
      "0": 9,
      "1": 9
    },
    "finite_positive_logdet_available": false,
    "has_zero_modes": true,
    "intertwines_internal_tau": true,
    "operator": "C_tau",
    "positive_definite": false,
    "reason": "It is the exact signed orientation operator, but heat/zeta positive determinant policy cannot consume negative and zero eigenvalues directly.",
    "source_status": "candidate_from_embedding"
  },
  "C_tau_square_or_absolute": {
    "embedded_positive_complement_eigenvalues": {
      "1": 8
    },
    "finite_positive_logdet": {
      "embedded_positive_complement": 0.0,
      "full_positive_complement": 0.0
    },
    "intertwines_internal_tau": false,
    "loses_orientation_sign": true,
    "operator": "C_tau^2 or |C_tau|",
    "positive_complement_eigenvalues": {
      "1": 18
    },
    "positive_semidefinite": true,
    "reason": "Squaring supplies a legal positive complement but collapses +tau and -tau and gives only logdet 0 on the unit spectrum."
  },
  "I_plus_C_tau": {
    "has_zero_modes": true,
    "intertwines_internal_tau": false,
    "operator": "I + C_tau",
    "positive_definite": false,
    "reason": "The shift is natural-looking but still has a zero sector and is not selected by the source packet.",
    "requires_zero_mode_policy": true,
    "spectrum": {
      "0": 9,
      "1": 9,
      "2": 9
    }
  },
  "chiral_Dirac_pair": {
    "eta_invariant_from_current_symmetric_counts": {
      "embedded_11": 0,
      "full_BN": 0
    },
    "operator": "D_chiral with sign(C_tau), determinant from D_chiral^* D_chiral and phase/eta from sign",
    "orientation_possible": true,
    "positive_finitepart_possible": true,
    "reason": "This is the best live route: separate positive determinant from signed orientation, but it needs a source theorem selecting the chiral/eta convention.",
    "source_selected_Dirac_convention": false
  },
  "two_I_plus_C_tau": {
    "finite_positive_logdet": "9*log(1)+9*log(2)+9*log(3)",
    "intertwines_internal_tau": false,
    "operator": "2I + C_tau",
    "positive_definite": true,
    "reason": "It is positive, but the additive shift is an unselected knob unless a smooth E_Qa/Dirac convention emits it.",
    "source_selected_shift": false,
    "spectrum": {
      "1": 9,
      "2": 9,
      "3": 9
    }
  }
}
```

## Meaning

This is real progress: the signed `End(E)->B_N` operator identity is now
explicit, source-tied to the existing embedding, and audited. The remaining
blocker is narrower than before. We no longer need to search for an arbitrary
operator bridge; we need the source-selected rule that turns this signed
central-rank operator into a positive finite determinant computation without
forgetting its sign/orientation data.
