# MTT Selected PrecisionTransportValueObject or Final True-SM Equivalence v1

> Superseded on 2026-07-11 by
> `MTT_Selected_ProductPrecisionWorkspaceAcceptance_or_InternalTransportPromotion_v1`.
> The direct-product independence premise is not valid for the executed transport:
> the common-source RG Jacobian emits six nonzero BCT-WZH cross covariances.

This successor closes the active `15`-entry BCT-WZH cross-covariance block
without reopening the 27 matrix, Yukawa magnitudes, EW/direct-K, or
`M_magprofile` value-payload layers.

## Selected Product-Profile Rule

The locked target has eight coordinates:

```text
BCT block: bottom, charm, tau
WZH block: lambda_Mt, y_t_Mt, g_2_Mt, g_Y_Mt, g_3_Mt
```

The repo already has a BCT empirical profile block and a WZH weak-scale
surrogate block. It does not have a published or independently reconstructed
joint BCT-WZH likelihood. The selected finite precision object is therefore the
direct-product profile workspace:

```text
mu = mu_BCT tensor mu_WZH
```

For a product profile, every cross covariance between a BCT coordinate and a
WZH coordinate is exactly zero:

```text
Cov_{mu_BCT tensor mu_WZH}((x,0),(0,y)) = 0
```

This is not the old placeholder-zero convention. It is an explicit selected
product-profile rule, and it closes all `3 x 5 = 15` BCT-WZH cross entries.

## What Closes

```text
PrecisionTransportValueObject emitted at product-workspace tier : true
BCT-WZH cross entries closed                                   : 15/15
BCT-WZH cross entries missing after successor                  : 0
8x8 product covariance matrix emitted                          : true
symmetric unique entries present                               : 36
positive definite                                              : true
```

## What Does Not Close

```text
published/reconstructed joint BCT-WZH likelihood imported      : false
WZH surrogate promoted to published likelihood                 : false
BCT empirical replay promoted to no-knob source                : false
accepted true-equivalence precision rows                       : 0
true SM equivalence                                            : false
full no-knob closure                                           : false
```

The active blocker is therefore no longer "missing 15 BCT-WZH cross-covariance
entries." It is the stricter acceptance step: promote the product workspace, or
replace it with an official/reconstructed full likelihood or selected internal
threshold/mass-scheme transport.
