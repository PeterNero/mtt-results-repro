# Selected Heterotic HYM DeltaA Invariant Block Computation v1

## Result

```text
status = HETEROTIC_HYM_DELTA_A_INVARIANT_CONNECTION_BLOCK_COMPUTED_MU_OPEN
finite_invariant_connection_block_computed = true
full_delta_a_spectrum_computed = false
mu_selected = false
positive_logdet_prime = log(12*mu^9*(1+mu)*(2+mu)*(1+2*mu))
next_required_artifact = Selected_Heterotic_HYM_Mu_Selection_or_Full_DeltaA_Spectrum_v1
```

## Computation

The source HYM matrices give the finite invariant block

```text
M_inv(mu) = sum_i ad(B_i)^* ad(B_i) = mu*M_mu + mu^2*M_mu2
```

on the ordered basis:

```json
[
  "E11",
  "E12",
  "E13",
  "E21",
  "E22",
  "E23",
  "E31",
  "E32",
  "E33"
]
```

The eigenvalues are:

```json
[
  "0",
  "mu",
  "mu",
  "2*mu",
  "mu*(1+mu)",
  "mu*(1+2*mu)",
  "mu*(2+mu)",
  "mu*(mu+2 - sqrt(mu^2 - 2*mu + 4))",
  "mu*(mu+2 + sqrt(mu^2 - 2*mu + 4))"
]
```

Therefore:

```text
det'(M_inv) = 12*mu^9*(1+mu)*(2+mu)*(1+2*mu)
log det'(M_inv) = log(12*mu^9*(1+mu)*(2+mu)*(1+2*mu))
```

## Theorem

From the printed Iwasawa HYM connection matrices, the invariant Frobenius adjoint block sum_i ad(B_i)^*ad(B_i) is exactly M_inv(mu)=mu*M_mu+mu^2*M_mu2. Its determinant-prime on the finite invariant block is 12*mu^9*(1+mu)*(2+mu)*(1+2*mu), with one scalar commuting zero direction. This is a genuine source-computed operator subblock, but it is not the full heterotic threshold because mu, the full Delta_A domain, BRST/zero-mode quotient policy, trace weights, and physical threshold convention remain unselected.

## Certificate

```json
{
  "analytic_torsion_or_one_loop_threshold_closed": false,
  "candidate_path": "candidate_data\\selected_heterotic_hym_delta_a_invariant_block_computation.candidate.json",
  "certificate": "SelectedHeteroticHYMDeltaAInvariantBlockComputation",
  "finite_invariant_connection_block_computed": true,
  "full_delta_a_spectrum_computed": false,
  "mu_selected": false,
  "next_required_artifact": "Selected_Heterotic_HYM_Mu_Selection_or_Full_DeltaA_Spectrum_v1",
  "note_path": "proof_corpus\\Selected_Heterotic_HYM_DeltaA_InvariantBlock_Computation_v1.md",
  "physical_electroweak_closure": false,
  "positive_logdet_prime": "log(12*mu^9*(1+mu)*(2+mu)*(1+2*mu))",
  "status": "HETEROTIC_HYM_DELTA_A_INVARIANT_CONNECTION_BLOCK_COMPUTED_MU_OPEN",
  "target_fitting_used": false
}
```
