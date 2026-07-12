# Selected Qa/SU3 Monad Map Construction or Source Augmentation v1

## Result

The printed Iwasawa SU3 monad topology is charge-compatible with typed maps, but it does not yet construct the maps.
For each summand, the required map entries are sections of `L_i tensor K1^{-1}` and `K2 tensor L_i^{-1}`.
Every product `g_i f_i` lands in the same charge `K2-K1 = (-1, 1, 0)`, so the obstruction is not a charge mismatch.

## Charge Table

| i | ell_i | f_i charge | g_i charge | g_i f_i charge | compatible |
|---|---|---|---|---|---|
| 1 | (-2, 0, 1) | (-3, 0, 1) | (2, 1, -1) | (-1, 1, 0) | yes |
| 2 | (-1, 1, -1) | (-2, 1, -1) | (1, 0, 1) | (-1, 1, 0) | yes |
| 3 | (1, -1, 0) | (0, -1, 0) | (-1, 2, 0) | (-1, 1, 0) | yes |
| 4 | (1, 0, -1) | (0, 0, -1) | (-1, 1, 1) | (-1, 1, 0) | yes |
| 5 | (2, 1, 1) | (1, 1, 1) | (-2, 0, -1) | (-1, 1, 0) | yes |

## Gate Verdict

- charge table computed: yes
- charge-level compatibility passed: yes
- section data found: no
- explicit f,g constructed: no
- g*f=0 checked: no
- monad route retired: no
- source augmentation required: yes
- Qa/SU3 closed: no
- target fitting used: no

## Minimal Data Needed

A closure source must provide one of these:

- five typed `f_i` entries, five typed `g_i` entries, and the relation `sum_i g_i f_i = 0`;
- an Iwasawa line-bundle section ring: bases for all required `H0` spaces and the multiplication table into `H0(K2 tensor K1^{-1})`;
- a direct same-monad Dolbeault/Cech/`rho_E` operator exit.

## Next Artifact

Selected_Qa_SU3_Iwasawa_Line_Bundle_Section_Ring_Interface_v1
