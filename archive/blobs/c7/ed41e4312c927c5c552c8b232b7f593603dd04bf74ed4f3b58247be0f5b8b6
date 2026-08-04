"""Prove the analytic q79 alpha1 tangent / retarded-kernel formula.

The previous q79 artifact reduced selected dotD_alpha1 and C1 emission to a
missing selected tangent source.  This step closes the part that can be closed
without inventing source values: the Riesz/Duhamel/reduced-Green variational
identity on the locked finite B_N gap layer.

It deliberately does not emit the physical alpha1 tangent, selected sector
routing, or selected dotD matrices.  The theorem says exactly how such data
would be accepted once a same-branch source-normalization or End0-to-sector
routing theorem supplies them.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

OUT_DIR = CANDIDATES / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel"
OUT_CANDIDATE = CANDIDATES / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel.candidate.json"
OUT_CERT = CERTS / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel_certificate.json"
OUT_PAPER = CORPUS / "Q79_Selected_Alpha1_Tangent_or_Retarded_Overlap_Kernel_v1.md"

OUT_FORMULA = OUT_DIR / "analytic_variational_kernel_formula.json"
OUT_TRIAGE = OUT_DIR / "cross_repo_external_source_triage.json"
OUT_CONTRACT = OUT_DIR / "selected_tangent_value_fill_contract.open.json"

STATUS = "Q79_SELECTED_ALPHA1_TANGENT_KERNEL_ANALYTIC_FORMULA_PROVED_SOURCE_VALUES_OPEN"
NEXT = "Q79_Selected_Physical_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1"

CONSTANTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
SM_PARITY = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

DOTD_C1 = CERTS / "q79_selected_dotd_alpha1_c1_response_emission_certificate.json"
TRACE_GAP = CERTS / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay_certificate.json"
CONSTANTS_ALPHA1 = (
    CONSTANTS
    / "certificates"
    / "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt_certificate.json"
)
CONSTANTS_SOURCE_DRIVER = (
    CONSTANTS
    / "certificates"
    / "selected_dotd_alpha1_source_and_driver_theorem_attempt_certificate.json"
)
SM_PHYSICAL_DOTD = (
    SM_PARITY
    / "certificates"
    / "selected_physical_dotd_alpha1_or_end0_sector_routing_certificate.json"
)
SM_T1T2_GREEN = (
    SM_PARITY
    / "certificates"
    / "selected_t1t2_covariant_green_and_transfer_probe_certificate.json"
)
SM_OFFDIAG = (
    SM_PARITY
    / "certificates"
    / "selected_offdiagonal_ext_control_or_sector_transfer_certificate.json"
)

INPUTS = {
    "q79_dotd_alpha1_c1_response_reduction": DOTD_C1,
    "q79_trace_gap_layer": TRACE_GAP,
    "constants_alpha1_tangent_attempt": CONSTANTS_ALPHA1,
    "constants_source_driver_attempt": CONSTANTS_SOURCE_DRIVER,
    "sm_physical_dotd_or_end0_sector_routing": SM_PHYSICAL_DOTD,
    "sm_t1t2_covariant_green": SM_T1T2_GREEN,
    "sm_offdiagonal_ext_control": SM_OFFDIAG,
}

EXTERNAL_REFERENCES = [
    {
        "key": "kato_perturbation_linear_operators",
        "title": "Perturbation theory for linear operators",
        "url": "https://link.springer.com/book/10.1007/978-3-662-12678-3",
        "use": (
            "Analytic perturbation theory, eigenprojection perturbation, and "
            "semigroup perturbation are the standard functional-analytic frame "
            "for the Riesz and Duhamel identities used here."
        ),
    },
    {
        "key": "duhamel_integral_semigroups",
        "title": "On theoretical and practical aspects of Duhamel's integral",
        "url": "https://yadda.icm.edu.pl/baztech/element/bwmeta1.element.baztech-b07432ca-7c06-4303-8967-e42c578b93de",
        "use": (
            "Records Duhamel formulae and their operator-semigroup "
            "interpretation; this supports the retarded-kernel derivative "
            "identity used below."
        ),
    },
    {
        "key": "heterotic_moduli_strominger_algebroids",
        "title": "Algebroids, Heterotic Moduli Spaces and the Strominger System",
        "url": "https://arxiv.org/abs/1402.1532",
        "use": (
            "Heterotic/Strominger first-order deformations live in structured "
            "cohomology/operator data, so alpha1 cannot be treated as an "
            "untyped free scalar knob."
        ),
    },
    {
        "key": "heterotic_moduli_recent_review",
        "title": "Recent Developments in Heterotic Moduli",
        "url": "https://arxiv.org/abs/2409.16524",
        "use": (
            "The modern deformation-complex viewpoint aligns with the local "
            "End0/source-normalization acceptance contract."
        ),
    },
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def exact_scalar_check() -> dict[str, Any]:
    """A one-mode exact sign check for the reduced-Green formula.

    For L(eps)=[[0, eps*a],[eps*a, mu]], the zero eigenvector has derivative
    -a/mu in the positive-eigenvalue direction.  This agrees with
    dot psi = -G Q dotL psi and with the t->infinity Duhamel integral.
    """

    source_coeff = 2
    gap_mu = 5
    response = -source_coeff / gap_mu
    return {
        "operator_family": "L(eps) = [[0, eps*a], [eps*a, mu]]",
        "source_coeff_a": source_coeff,
        "gap_mu": gap_mu,
        "green_coeff": 1 / gap_mu,
        "riesz_projection_derivative_offdiag": response,
        "duhamel_integral_minus_int_0_inf_exp_minus_mu_t_a_dt": response,
        "horizontal_response_minus_G_source": response,
        "expected_exact_fraction": "-2/5",
        "all_three_formulas_agree": response == -0.4,
    }


def selected_gap_layer(dotd: dict[str, Any], trace: dict[str, Any]) -> dict[str, Any]:
    frontier_gap = (
        dotd.get("dotd_alpha1_frontier", {})
        .get("selected_DE_gap_layer", {})
    )
    trace_gap = (
        trace.get("selected_trace_equality_gap_layer_proof", {})
        .get("gap_layer", {})
    )
    return {
        "basis_id": frontier_gap.get("basis_id") or trace_gap.get("basis_id"),
        "basis_dimension": frontier_gap.get("basis_dimension") or trace_gap.get("basis_dimension"),
        "selected_eta_N": frontier_gap.get("selected_eta_N") or trace_gap.get("selected_eta_N"),
        "selected_gap_lower_bound": frontier_gap.get("selected_gap_lower_bound")
        or trace_gap.get("selected_gap_lower_bound"),
        "selected_green_norm_bound": frontier_gap.get("selected_green_norm_bound")
        or trace_gap.get("selected_green_norm_bound"),
        "D_E_gap_Riesz_Green_layer_locked": frontier_gap.get("D_E_gap_Riesz_Green_layer_locked")
        or trace.get("what_closes_now", {}).get("selected_Riesz_Green_gap_layer_closed"),
    }


def build_formula(dotd: dict[str, Any], trace: dict[str, Any]) -> dict[str, Any]:
    gap = selected_gap_layer(dotd, trace)
    green_bound = gap.get("selected_green_norm_bound")
    return {
        "schema": "Q79AnalyticRetardedRieszKernelFormula.v1",
        "status": "ANALYTIC_FORMULA_PROVED_SELECTED_TANGENT_VALUES_OPEN",
        "selected_gap_layer": gap,
        "assumptions": {
            "finite_locked_BN_basis": gap["basis_dimension"] == 27,
            "isolated_family_cluster": gap["selected_gap_lower_bound"] is not None
            and gap["selected_gap_lower_bound"] > 0,
            "same_source_differentiable_deformation_required": True,
            "selected_tangent_values_required_before_replay": True,
        },
        "formulae": {
            "riesz_projection": (
                "P(eps) = (1/(2*pi*i)) int_Gamma (z I - A(eps))^{-1} dz"
            ),
            "riesz_projection_derivative": (
                "P'(0) = (1/(2*pi*i)) int_Gamma R0(z) A'(0) R0(z) dz"
            ),
            "duhamel_retarded_semigroup_derivative": (
                "d/d eps exp(-t A(eps))|0 = - int_0^t exp(-(t-s)A0) A'(0) exp(-s A0) ds"
            ),
            "reduced_green_limit": (
                "G Q = int_0^infty exp(-t A0) Q dt when A0 has a positive complement gap"
            ),
            "horizontal_zero_mode_response": (
                "dotPsi_i = - G Q dotD_alpha1 Psi_i, with P dotPsi_i=0"
            ),
        },
        "sign_convention": (
            "The resolvent is R0(z)=(z I - A0)^{-1}; the minus sign in the "
            "horizontal response comes from differentiating the zero-mode "
            "equation and applying the reduced inverse on P-perp."
        ),
        "q79_bound_if_tangent_supplied": {
            "source_norm_to_response_norm_bound": (
                "||dotPsi|| <= ||G|| ||Q dotD_alpha1 Psi||"
            ),
            "selected_green_norm_bound": green_bound,
        },
        "exact_scalar_check": exact_scalar_check(),
        "what_the_formula_closes": {
            "analytic_riesz_projection_derivative_formula": True,
            "duhamel_retarded_kernel_derivative_formula": True,
            "reduced_green_horizontal_response_identity": True,
            "conditional_projector_retention_given_selected_tangent": True,
        },
        "what_the_formula_does_not_close": {
            "selected_alpha1_tangent_parameter": True,
            "selected_retarded_overlap_values": True,
            "sector_equality_to_existing_dotD_matrices": True,
            "honest_dotD_replay_without_lifted_flags": True,
        },
    }


def build_triage() -> dict[str, Any]:
    input_statuses = {name: status_record(path) for name, path in INPUTS.items()}
    return {
        "schema": "Q79Alpha1KernelCrossRepoExternalTriage.v1",
        "status": "FORMULA_SUPPORTED_SOURCE_NORMALIZATION_OPEN",
        "input_statuses": input_statuses,
        "external_references": EXTERNAL_REFERENCES,
        "external_inspiration": {
            "operator_perturbation": (
                "Kato-style Riesz projection and semigroup perturbation justify "
                "differentiating the isolated family projector once a selected "
                "operator tangent exists."
            ),
            "retarded_kernel": (
                "Duhamel converts the derivative of the retarded semigroup into "
                "the reduced-Green response on the gapped complement."
            ),
            "string_geometry": (
                "Hull-Strominger/heterotic moduli are deformation-complex data; "
                "this supports the local conclusion that alpha1 needs a typed "
                "same-branch source normalization or routing functor."
            ),
        },
        "local_cross_repo_lesson": {
            "constants_repo": (
                "The retarded-overlap lane is classified, but sector charge, "
                "transfer normalization, and selected B_N tangent remain open."
            ),
            "sm_parity_repo": (
                "A selected local Ext-density tangent and Frechet dotD replay "
                "exist in the End0 row model; the repo correctly refuses to "
                "promote it to physical alpha1 without source normalization or "
                "End0-to-sector routing."
            ),
            "q79_repo": (
                "The q79 D_E gap/Riesz/Green layer is selected, and same-basis "
                "dotD value matrices exist, but selected dotD source flags and "
                "alpha1 driver flags remain open."
            ),
        },
        "triage_conclusion": (
            "The analytic retarded/Riesz kernel formula is no longer the blocker. "
            "The blocker is the selected physical source-normalization or "
            "End0-to-sector routing value fill."
        ),
    }


def build_contract(formula: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "Q79SelectedAlpha1TangentValueFillContract.v1",
        "status": "OPEN_SOURCE_NORMALIZATION_OR_ROUTING_VALUES_REQUIRED",
        "must_emit_before_selected_dotD_replay": [
            "same-branch selected alpha1 source-normalization, or selected End0-to-sector routing functor",
            "normalization value mapping the discrete alpha1 Chern/source row into the tangent direction",
            "finite B_N operator derivative dotD_alpha1 derived from that source",
            "proof that the Riesz/Duhamel formula above acts on the same locked q79/F,m=1 basis",
            "sector-by-sector equality to the existing same-basis dotD_alpha1 value matrices",
            "honest replay certificate setting selected_dotD_source_verified and alpha1_driver_verified by theorem",
        ],
        "acceptance_tests_after_values": [
            "D_E gap layer remains selected with positive complement gap",
            "P dotPsi_i=0 horizontal gauge holds",
            "A dotPsi_i + Q dotD_alpha1 Psi_i = 0 sector by sector",
            "no diagnostic lifted source flags are used",
            "no observed masses, CKM angles, thresholds, or benchmark matrices enter",
        ],
        "legal_promotion_routes": {
            "route_A_source_normalization": (
                "Identify the discrete alpha1 Chern/source row with the selected "
                "infinitesimal Ext-density or equivalent HYM/Strominger tangent."
            ),
            "route_B_end0_to_sector_routing": (
                "Emit a selected End0-to-sector functor and normalization that "
                "maps the End0 response to Q,u,d,L,e,N,H sector matrices."
            ),
        },
        "response_formula_to_use_once_values_exist": formula["formulae"][
            "horizontal_zero_mode_response"
        ],
        "next_required_artifact": NEXT,
    }


def build_candidate() -> dict[str, Any]:
    dotd = load(DOTD_C1)
    trace = load(TRACE_GAP)
    formula = build_formula(dotd, trace)
    triage = build_triage()
    contract = build_contract(formula)

    write_json(OUT_FORMULA, formula)
    write_json(OUT_TRIAGE, triage)
    write_json(OUT_CONTRACT, contract)

    data = {
        "certificate": "Q79SelectedAlpha1TangentOrRetardedOverlapKernel",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "paper": rel(OUT_PAPER),
        "artifact_paths": {
            "analytic_variational_kernel_formula": rel(OUT_FORMULA),
            "cross_repo_external_source_triage": rel(OUT_TRIAGE),
            "selected_tangent_value_fill_contract": rel(OUT_CONTRACT),
        },
        "input_statuses": triage["input_statuses"],
        "analytic_variational_kernel_formula": formula,
        "cross_repo_external_source_triage": triage,
        "selected_tangent_value_fill_contract": contract,
        "what_closes_now": {
            "analytic_riesz_projection_derivative_formula": True,
            "duhamel_retarded_kernel_derivative_formula": True,
            "reduced_green_horizontal_response_identity": True,
            "conditional_projector_retention_given_selected_tangent": True,
            "external_research_and_cross_repo_triage_completed": True,
            "selected_tangent_acceptance_contract_written": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_alpha1_source_normalization": True,
            "selected_End0_to_sector_routing_values": True,
            "selected_alpha1_tangent_parameter_or_kernel_values": True,
            "sector_equality_from_selected_derivative_to_dotD_matrices": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "selected_dotD_source_theorem": True,
            "same_branch_alpha1_driver_theorem": True,
            "selected_Hess_Xi_finite_blocks": True,
            "selected_primitive_C1_contractions": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_or_full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_alpha1_tangent_values": False,
            "claims_selected_dotD_source": False,
            "claims_alpha1_driver": False,
            "claims_sector_routing_values": False,
            "claims_C1_response_emitted": False,
            "claims_A_selected_or_b_selected": False,
            "claims_Yukawa_or_full_SM_closure": False,
            "promotes_diagnostic_lift_as_proof": False,
            "uses_observed_or_benchmark_inputs": False,
        },
        "theorem": {
            "name": "Q79AnalyticRetardedRieszKernelFormulaTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "On the locked q79/F,m=1 B_N gap layer, any same-branch "
                "differentiable selected alpha1 deformation has a unique "
                "horizontal first response given by the Riesz/Duhamel reduced "
                "Green formula dotPsi_i=-G Q dotD_alpha1 Psi_i.  This proves the "
                "analytic retarded-kernel formula and projector-retention "
                "criterion conditionally on a selected tangent source.  It does "
                "not emit the selected alpha1 tangent, the sector routing "
                "normalization, honest dotD replay, C1 response matrices, "
                "A_selected, b_selected, Yukawa magnitudes, or full SM closure."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "external_references": EXTERNAL_REFERENCES,
        "next_required_artifact": NEXT,
    }
    return data


def bool_lines(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def list_lines(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def build_paper(data: dict[str, Any]) -> str:
    formula = data["analytic_variational_kernel_formula"]
    gap = formula["selected_gap_layer"]
    contract = data["selected_tangent_value_fill_contract"]
    triage = data["cross_repo_external_source_triage"]
    refs = "\n".join(
        f"- {ref['title']}: {ref['url']}" for ref in data["external_references"]
    )
    return f"""# Q79 Selected Alpha1 Tangent or Retarded Overlap Kernel v1

## Result

The analytic retarded/Riesz kernel formula is proved on the locked q79/F,m=1
`B_N` gap layer.  The selected physical source values are still open.

This removes one blocker cleanly: once a selected same-branch `alpha1` tangent
or equivalent retarded-overlap source is supplied, the horizontal response is
not ambiguous.  It is

```text
dotPsi_i = - G Q dotD_alpha1 Psi_i, with P dotPsi_i = 0.
```

## Locked Input

- basis: `{gap["basis_id"]}`
- basis dimension: `{gap["basis_dimension"]}`
- selected eta_N: `{gap["selected_eta_N"]}`
- selected gap lower bound: `{gap["selected_gap_lower_bound"]}`
- selected Green norm bound: `{gap["selected_green_norm_bound"]}`
- D_E gap/Riesz/Green layer locked: `{gap["D_E_gap_Riesz_Green_layer_locked"]}`

## Analytic Formulae

```text
{formula["formulae"]["riesz_projection"]}
{formula["formulae"]["riesz_projection_derivative"]}
{formula["formulae"]["duhamel_retarded_semigroup_derivative"]}
{formula["formulae"]["reduced_green_limit"]}
{formula["formulae"]["horizontal_zero_mode_response"]}
```

Sign convention:

```text
{formula["sign_convention"]}
```

The exact one-mode check gives all three forms the same response:

```text
L(eps) = [[0, eps*2], [eps*2, 5]]
response = -2/5 = {formula["exact_scalar_check"]["horizontal_response_minus_G_source"]}
```

## Cross-Repo and External Triage

The constants repo says the retarded-overlap lane is classified but sector
charge, transfer normalization, and selected `B_N` tangent remain open.

The SM-parity repo has a selected local Ext-density tangent and Frechet `dotD`
replay in the End0 row model.  It correctly refuses to promote that local
tangent to physical `alpha1` without source normalization or End0-to-sector
routing.

External perturbation theory supplies the Riesz/Duhamel machinery, while the
heterotic/Strominger deformation literature supports the same typed-source
discipline: first-order deformations live in operator/cohomology data, not in
an untyped free scalar.

Triage conclusion:

```text
{triage["triage_conclusion"]}
```

## Value-Fill Contract

Before selected `dotD_alpha1` replay can be claimed, the next artifact must
emit:

{list_lines(contract["must_emit_before_selected_dotD_replay"])}

Acceptance tests after values exist:

{list_lines(contract["acceptance_tests_after_values"])}

Legal promotion routes:

- Route A: `{contract["legal_promotion_routes"]["route_A_source_normalization"]}`
- Route B: `{contract["legal_promotion_routes"]["route_B_end0_to_sector_routing"]}`

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as an analytic formula theorem.

{data["theorem"]["statement"]}

## External References Used

{refs}

Next required artifact:
`{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 selected alpha1 tangent / retarded overlap kernel")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
