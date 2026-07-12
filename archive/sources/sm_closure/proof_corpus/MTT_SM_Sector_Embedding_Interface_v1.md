# MTT SM Sector Embedding Interface v1

## Purpose

This artifact defines the SM sector boundary for SM-parity closure.  It says
what must be selected as source structure before any measured SM numerical
values are allowed to enter.

It does not prove the actual selected representation packet, anomaly
calculation, local-QFT functor, or no-knob constants.  It closes the interface
that prevents measured couplings, masses, and phases from selecting the sector
they are later used to compare.

## Selected SM Packet

- `sector_name`: SM
- `gauge_carrier`: SU3 x SU2 x U1 or a selected MTT packet mapped to that gauge carrier.
- `representation_packet`: Typed fermion and Higgs representation content, including conjugates and chirality convention.
- `family_index`: A declared three-family index or selected internal replacement.
- `operator_packet`: Covariant derivative, kinetic operators, Higgs/Yukawa operator slots, gauge curvature, and anomaly operators.
- `anomaly_conditions`: Gauge, mixed, and gravitational anomaly cancellation checks.
- `locality_limit`: The rule or functor by which the modal packet presents local QFT observables.
- `renormalization_interface`: Scale, scheme, running-parameter slots, and matching conventions.
- `measured_slot_boundary`: The exact point after which measured couplings, Yukawas, phases, and Higgs parameters may enter.

## Embedding Rules

- The SM sector packet must be selected before measured SM numerical values are admitted.
- Gauge group and representation content are selected source data, not measured parity inputs.
- Family count is selected source data for SM-parity; measured masses cannot establish it.
- Gauge couplings, Yukawa matrices, CP phases, Higgs potential parameters, and RG thresholds are downstream measured slots unless a no-knob source is supplied.
- The selected packet must declare anomaly and consistency checks before empirical comparison.
- The embedding must expose local QFT observables through an explicit observable map Obs_SM.
- Every measured SM slot must inherit the slot schema from the measured-parameter interface.

## Required Components

- `gauge_group`: SELECTED_SOURCE_DATA_REQUIRED. Must be declared as the SM gauge carrier before measured couplings enter. No-knob target: derive SU3 x SU2 x U1 from selected modal/topological/operator packet.
- `fermion_representations`: SELECTED_SOURCE_DATA_REQUIRED. Must list chiral representation content and conjugation conventions. No-knob target: derive representation packet and anomaly cancellation from selected topology/monad/section data.
- `three_generations`: SELECTED_SOURCE_DATA_REQUIRED. May be asserted as SM-parity source structure, but not inferred from masses. No-knob target: derive family index from selected internal packet.
- `higgs_carrier`: SELECTED_SOURCE_DATA_REQUIRED. Must define Higgs representation and electroweak breaking interface. No-knob target: derive Higgs projector/carrier from selected MTT source.
- `gauge_couplings`: MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION. Measured running parameters with scheme and scale. No-knob target: derive threshold kernels and absolute normalization from selected operator data.
- `yukawa_matrices`: MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION. Measured complex matrices with basis, phase, scale, and uncertainty. No-knob target: derive from selected overlap/operator kernels.
- `cp_phases`: MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION. Measured phase data only after representation and mixing conventions are declared. No-knob target: derive finite character-to-physical phase map from selected source.
- `higgs_parameters`: MEASURED_PARITY_INPUT_ALLOWED_AFTER_PACKET_SELECTION. Measured vev, mass, quartic, and potential terms with RG convention. No-knob target: derive Higgs potential and thresholds from selected source.

## Forbidden Imports

- using measured masses to choose the family index
- using gauge coupling values to choose SU3 x SU2 x U1
- using CKM or PMNS targets to choose the representation packet
- using q79 numeric success as a direct proof of Qa/SU3 color embedding
- using anomaly cancellation as a generic existence claim without listing the actual representation packet
- treating benchmark matrices as selected Yukawa or CP source matrices

## Acceptance Tests

- SM packet fields are all declared.
- Gauge group, representations, family count, and Higgs carrier are classified as selected source data.
- Couplings, Yukawas, CP phases, and Higgs numerical parameters are downstream measured parity inputs.
- Measured values are barred from source selection.
- Anomaly checks and local-QFT observable map are required before empirical equivalence.
- Full SM-parity closure is not claimed by this interface alone.

## Interface Theorem

An MTT sector can be used as an SM-parity sector only after it declares a
selected SM packet containing gauge carrier, representation packet, family
index, Higgs carrier, operator packet, anomaly requirements, locality limit,
renormalization interface, and measured-slot boundary.

Measured values may then enter only downstream as typed parity slots inherited
from the measured-parameter interface.  They may not select the SM packet.

## What This Closes

- selected_sm_packet_schema
- source_vs_measured_sm_boundary
- downstream_sm_parameter_slot_policy
- forbidden_sm_imports
- sm_embedding_acceptance_tests

## What Remains Open

- actual_selected_representation_packet
- anomaly_calculation_certificate
- local_QFT_observable_functor
- QM_QFT_GR_recovery_theorem
- empirical_equivalence_ledger
- no_knob_constants

## Next Artifact

```text
MTT_QM_QFT_GR_Recovery_Interface_v1
```
