# MTT Selected Same-Source Alpha1 Normalization Pin-Down Kernel v1

Status: `MTT_SELECTED_SAMESOURCE_ALPHA1_NORMALIZATION_PINDOWN_KERNEL_BUILT_PACKET_VALUES_OPEN`.

## Pin-Down Kernel

The current local algebra gives one candidate:

```text
lambda_alpha1 = 1
du/dalpha1 = h_ext
||h_ext||_L2 = 0.03961411527057935
residual_L2 = 6.751979459438445e-13
```

This artifact defines when that candidate is selected:

```text
selected source identity
+ selected alpha1 source-strength coordinate
+ selected normalization functional N_alpha1 with N_alpha1(h_ext)=1
+ residual(h_selected_alpha1 - h_ext) <= 1e-12
+ sector dotD equality
+ honest dotD validator replay
```

Only then may the repo set:

```text
selected_value_emitted = true
alpha1_driver_verified = true
```

## Why This Pins It Down

The ambiguity is now reduced to a finite packet fill, not a conceptual gap.
Either the same-source packet emits the normalization functional, or a typed
`B_N` retarded-overlap kernel emits the same derivative.  The template
`candidate_data/selected_samesource_alpha1_normalization_packet.template.json` is the fill target.

No observed constants, benchmark matrices, target fits, or lifted flags are
admissible.

Next artifact: `MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1`.
