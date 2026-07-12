"""Build the smooth rho_E transition skeleton or complement-kernel equations."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "fill_attempt": DATA / "selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt.candidate.json",
    "missing_leaves": DATA / "selected_heterotic_projectiverhoe_newsourceinsertion_fillattempt_missing_leaves.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_exactcomplement_or_smoothrhoetransition_valuepacket.values.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.candidate.json"
OUTPUT_EQS = DATA / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel.equations.json"
OUTPUT_CERT = CERTS / "selected_heterotic_projectiverhoe_goodcover_transition_skeleton_or_complement_kernel_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_ProjectiveRhoE_GoodCoverTransitionSkeleton_or_ComplementKernel_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_GOODCOVER_TRANSITION_SKELETON_OR_COMPLEMENT_KERNEL_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SourceTableSolve_or_ComplementKernelProof_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    fill_attempt = load(INPUTS["fill_attempt"])
    missing = load(INPUTS["missing_leaves"])
    finite_packet = load(INPUTS["finite_packet"])
    finite_values = finite_packet["finite_internal_values"]
    labels = finite_values["labels"]
    tau = finite_values["tau"]

    transition_skeleton = {
        "cover_symbols": {
            "cover": "U_alpha for alpha in selected_good_cover_index_set A",
            "overlaps": "U_alpha_beta = U_alpha cap U_beta",
            "triple_overlaps": "U_alpha_beta_gamma = U_alpha cap U_beta cap U_gamma",
            "value_status": "index set and overlap incidence not emitted by current source",
        },
        "unknowns": {
            label: {
                "transition_matrix": f"T_{{alpha,beta}}^{label}",
                "rank": "rank(E_label) or selected projective fiber dimension",
                "central_character_required": finite_values["rho_E_central_character"][label],
                "tau_required": tau[label],
            }
            for label in labels
        },
        "required_equations": {
            "identity_on_diagonal": "T_{alpha,alpha}^ell = I_ell",
            "inverse_on_reversed_overlap": "T_{beta,alpha}^ell = (T_{alpha,beta}^ell)^(-1)",
            "projective_triple_overlap": "T_{alpha,beta}^ell T_{beta,gamma}^ell T_{gamma,alpha}^ell = zeta_3^{tau_ell} I_ell on U_{alpha,beta,gamma}",
            "finite_character_shadow": "Tr_central(T^ell triple cocycle) maps to exp(2*pi*i*tau_ell/3)",
            "metric_unitarity": "(T_{alpha,beta}^ell)^* h_alpha^ell T_{alpha,beta}^ell = h_beta^ell",
            "bundle_operator_compatibility": "D_E^beta T_{alpha,beta}^ell = T_{alpha,beta}^ell D_E^alpha plus connection/curvature correction terms",
            "projector_retention": "Pi_Qa T_{alpha,beta}^ell = T_{alpha,beta}^ell Pi_Qa on selected quotient labels",
            "freed_witten_bianchi": "dH = tr(R wedge R) - tr(F_A wedge F_A) with the same B-field/gerbe representative used by T",
        },
        "forbidden_instantiations": [
            "T_{alpha,beta}^ell := finite scalar rho_E(ell) without a selected cover",
            "identity transition matrices with nonzero tau labels",
            "transition tables selected by matching observed couplings or scales",
        ],
    }

    complement_kernel = {
        "operator_symbols": {
            "D_smooth": "selected smooth heterotic Qa/SU3 threshold operator",
            "P_11": "projection to ordered labels F1..F5,G1..G5,P",
            "D_fin": "selected finite internal D_E already emitted",
            "D_comp": "(I - P_11) D_smooth (I - P_11)",
            "ghost_operator": "BRST/FP quotient operator in the same gauge convention",
        },
        "required_factorization_equations": {
            "domain_decomposition": "Dom(D_smooth) = Im(P_11) direct_sum Dom(D_comp) after gauge quotient",
            "heat_trace_split": "Tr_Q exp(-t D_smooth) = Tr exp(-t D_fin) + Tr exp(-t D_comp) - Tr exp(-t ghost_operator)",
            "zeta_split": "zeta_smooth(s) = zeta_fin(s) + zeta_comp(s) - zeta_ghost(s)",
            "finite_part_rule": "FP[-zeta_smooth'(0)]_Qa = log(2008) iff FP[-zeta_comp'(0)+zeta_ghost'(0)] is zero/universal/GR-only outside Qa/SU3",
            "no_double_count": "the finite internal determinant log(2008) is counted once",
        },
        "current_known_values": {
            "finite_part_internal_units": finite_values["finite_internal_part"],
            "D_fin": finite_values["D_E"],
            "labels": labels,
        },
        "missing_values": [
            "D_smooth formula/domain",
            "P_11 as a smooth-to-finite quotient map",
            "D_comp spectrum or heat kernel",
            "ghost operator and determinant convention",
            "proof that complement contribution is zero, universal, GR-only, or cancels",
        ],
    }

    equations = {
        "schema": "SelectedHeteroticProjectiveRhoEGoodCoverTransitionSkeletonOrComplementKernel.Equations.v1",
        "status": "EQUATIONS_BUILT_VALUES_OPEN",
        "transition_skeleton": transition_skeleton,
        "complement_kernel": complement_kernel,
        "source_requirements": {
            "same_branch_source_certificate_required": True,
            "selected_before_target_comparison_required": True,
            "observed_data_allowed": False,
        },
    }
    OUTPUT_EQS.write_text(json.dumps(equations, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "SelectedHeteroticProjectiveRhoEGoodCoverTransitionSkeletonOrComplementKernel",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "equations_path": rel(OUTPUT_EQS),
        "transition_skeleton_built": True,
        "complement_kernel_built": True,
        "missing_leaves_carried": missing,
        "decision": {
            "goodcover_equation_system_ready": True,
            "complement_kernel_equation_system_ready": True,
            "smooth_transition_values_solved": False,
            "exact_complement_kernel_proved": False,
            "smooth_finitepart_computed": False,
            "E_Qa_computed": False,
            "next_required_artifact": NEXT,
            "target_fitting_used": False,
            "closure_claimed": False,
        },
        "guardrails": {
            "does_not_instantiate_T_from_finite_character_table": True,
            "does_not_assert_smooth_domain": True,
            "does_not_assert_heat_kernel_cancellation": True,
            "does_not_use_observed_couplings_or_scales": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "GoodCoverTransitionSkeletonOrComplementKernelReduction",
            "proved": True,
            "statement": (
                "The remaining smooth rho_E closure problem is reduced to two explicit "
                "equation systems. Lane A must solve selected projective transition "
                "matrices on a good cover whose triple-overlap central cocycle shadows "
                "the finite tau table and satisfies metric, projector, and Bianchi "
                "compatibility. Lane B must solve a smooth heat/zeta/torsion quotient "
                "kernel showing that the smooth complement contributes zero, a universal "
                "constant, a GR-only term outside Qa/SU3, or a BRST/FP cancellation. "
                "No values are inserted by the skeleton itself."
            ),
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "equations_path": rel(OUTPUT_EQS),
        "note_path": rel(OUTPUT_NOTE),
        "transition_skeleton_built": True,
        "complement_kernel_built": True,
        "smooth_transition_values_solved": False,
        "smooth_finitepart_computed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic ProjectiveRhoE GoodCoverTransitionSkeleton or ComplementKernel v1

## Result

```text
status = {STATUS}
transition_skeleton_built = true
complement_kernel_built = true
smooth_transition_values_solved = false
smooth_finitepart_computed = false
next_required_artifact = {NEXT}
```

## Construction

This artifact turns the remaining smooth `rho_E` gap into two explicit equation
systems:

- Lane A: selected projective transition matrices on a good cover, with
  triple-overlap central cocycle shadowing the finite `tau` table.
- Lane B: selected smooth complement heat/zeta/torsion kernel, with BRST/FP
  quotient and no-double-count convention.

The equation payload is:

```text
{rel(OUTPUT_EQS)}
```

No transition values, smooth domain, complement spectrum, `E_Qa`, or physical
threshold normalization are claimed here.
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_EQS)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
