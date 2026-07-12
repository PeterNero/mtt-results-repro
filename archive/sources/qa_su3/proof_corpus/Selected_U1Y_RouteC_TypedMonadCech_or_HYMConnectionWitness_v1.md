# Selected U1Y Route-C TypedMonadCech or HYMConnectionWitness v1

## Result

```text
status = U1Y_ROUTEC_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_CONTRACT_BUILT_VALUES_OPEN
contract_built = true
accepts_three_equivalent_witness_routes = true
payload_missing_leaf_count = 29
selected_connection_witness_constructed = false
primitive_C1_values_computed = false
next_required_artifact = Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1
```

This creates the local witness contract. It does not fill the witness.
Any one of the three payload families below is enough, provided the data
come from the selected branch and replay without lifted flags.

## Accepted Witness Routes

### typed_monad_cech
- typed f_i section representatives for all nonzero maps
- typed g_i section representatives for all nonzero maps
- Cech cover, line-bundle transitions, and cocycle checks
- g o f = 0 certificate
- exactness/local-freeness or controlled torsion-free sheaf substitute
- selected Hermitian metric/gauge and finite D_E action on B_N
- H1(E) basis, anti-family check, sector projections, Riesz/Green/dotD

### direct_hym
- selected holomorphic bundle or sheaf model
- selected Gauduchon/balanced metric
- HYM connection coefficients A or equivalent rho_E
- residual bounds for F^(0,2), HYM primitive part, Bianchi/Strominger row
- finite Galerkin basis, D_E action, Riesz gap, Green, dotD alpha1

### finite_routec_solve
- non-identity selected rho_E boundary matrices
- local A^(0,1) or discrete connection variables
- zero/controlled residual solve for cocycle, metric, integrability, HYM, Bianchi
- positive selected Hessian or selection functional gap
- same-source export into D_E/Riesz/Green/dotD validators

## Finite Prefix Support

- `basis_id`: `F3xF3_gerbe_twisted_fourier_N1_rank3`
- `dimension`: `27`
- `DE_emitted`: `True`
- `dotD_alpha1_emitted`: `True`
- `primitive_C1_engine_built`: `True`
- `selected_by_mtt`: `False`

## Guardrails

- Finite prefix values are support, not selected provenance.
- One complete witness route is enough; mixing partial routes is not.
- The replay must be honest: no lifted selected-source flags.

## Certificate

```json
{
  "accepts_three_equivalent_witness_routes": true,
  "candidate_path": "candidate_data\\selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.candidate.json",
  "certificate": "SelectedU1YRouteCTypedMonadCechOrHYMConnectionWitness",
  "closure_claimed": false,
  "contract_built": true,
  "next_required_artifact": "Selected_U1Y_RouteC_FiniteHYMConnectionSolve_or_TypedCechPayload_v1",
  "note_path": "proof_corpus\\Selected_U1Y_RouteC_TypedMonadCech_or_HYMConnectionWitness_v1.md",
  "payload_missing_leaf_count": 29,
  "payload_path": "candidate_data\\selected_u1y_routec_typed_monad_cech_or_hym_connection_witness.open.json",
  "primitive_C1_values_computed": false,
  "selected_connection_witness_constructed": false,
  "status": "U1Y_ROUTEC_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_CONTRACT_BUILT_VALUES_OPEN",
  "target_fitting_used": false
}
```
