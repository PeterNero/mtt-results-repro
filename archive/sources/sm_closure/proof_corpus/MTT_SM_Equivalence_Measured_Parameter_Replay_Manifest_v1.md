# MTT SM-Equivalence Measured Parameter Replay Manifest v1

Status: `MTT_SM_EQUIVALENCE_MEASURED_PARAMETER_REPLAY_MANIFEST_BUILT_VALUES_OPEN`.

## Theorem

`SMEquivalenceMeasuredParameterReplayManifestTheorem` is proved in the local
audit sense: after the selected source/interface boundary is frozen, measured
SM parameters may enter as downstream replay slots.  They cannot select the
source, topology, operator packet, dynamic overlap tensor, or no-knob kernels.

## Superset Use

This is a superset-to-boundary step, followed by a straight replay step.
Topology, terminal-monad, q79/theta, Qa/SU3, HYM, and dynamic-overlap paths are
used only to lock the selected source/operator boundary.  The measured replay
then follows the SM standard.

## Slots

- `gauge.alpha_1_alpha_2_alpha_3`
- `yukawa.Y_u_Y_d_Y_e`
- `mixing.CKM`
- `mixing.PMNS`
- `higgs.v_mh_lambda_or_potential`
- `neutrino.yukawa_or_mass_splittings`

No numeric values are inserted here.  The next artifact, `MTT_SM_Equivalence_Reference_Data_Packet_v1`, must freeze
versioned reference values, conventions, units, scales, uncertainties, and
correlation policy before any numeric replay is allowed.

## Guardrail

A successful replay is evidence for SM-equivalence only.  It is not a no-knob
derivation unless the selected internal dynamic overlap/threshold/source kernels
are emitted separately.
