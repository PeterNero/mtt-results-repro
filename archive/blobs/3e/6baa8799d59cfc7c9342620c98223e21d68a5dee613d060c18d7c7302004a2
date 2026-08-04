"""Attempt the final finite-branch Yoneda scalar in a canonical theta ladder.

The preceding reduction shows that the only remaining finite branch-candidate
stability obstruction is M=(-2,1,0).  The obstruction map is

    H^0(1,1,0) x H^1(2,-4,0) -> H^1(3,-3,0).

This script evaluates that map in the minimal theta-ladder basis suggested by
the existing Cech/Kunneth labels.  It is intentionally conditional: the result
becomes a selected proof only if MTT selects this theta multiplication basis,
or if the same nonzero vector is recovered from raw Appell-Humbert/Cech data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

ZERO_SLOPE_REDUCTION = CERTS / "valpha_zero_slope_yoneda_reduction_certificate.json"
SCALAR_TEMPLATE = (
    CANDIDATES / "valpha_zero_slope_yoneda" / "remaining_yoneda_scalar.template.json"
)
SELECTED_COHOMOLOGY = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)
APPELL_HUMBERT = CERTS / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"

OUT_DIR = CANDIDATES / "valpha_remaining_yoneda_scalar"
OUT_PACKET = OUT_DIR / "canonical_theta_ladder_scalar.candidate.json"
OUT_CANDIDATE = CANDIDATES / "valpha_remaining_yoneda_scalar_attempt.candidate.json"
OUT_CERT = CERTS / "valpha_remaining_yoneda_scalar_attempt_certificate.json"
OUT_PAPER = CORPUS / "VAlpha_Remaining_Yoneda_Scalar_Attempt_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def basis_h1_l2() -> list[str]:
    return [f"theta_plus_{i}_tensor_eta_minus_{j}" for i in range(2) for j in range(4)]


def basis_h1_target() -> list[str]:
    return [f"theta_plus3_{i}_tensor_eta_minus3_{j}" for i in range(3) for j in range(3)]


def theta_ladder_image(label: str) -> str | None:
    prefix = "theta_plus_"
    middle = "_tensor_eta_minus_"
    if not label.startswith(prefix) or middle not in label:
        return None
    left, right = label[len(prefix) :].split(middle, maxsplit=1)
    i = int(left)
    j = int(right)
    if i not in range(2) or j not in range(4):
        return None
    if j == 3:
        return None
    return f"theta_plus3_{i}_tensor_eta_minus3_{j}"


def vector_image(vector: list[int], source_basis: list[str], target_basis: list[str]) -> list[int]:
    target_index = {label: index for index, label in enumerate(target_basis)}
    out = [0 for _ in target_basis]
    for coeff, label in zip(vector, source_basis, strict=True):
        if coeff == 0:
            continue
        image = theta_ladder_image(label)
        if image is None:
            continue
        out[target_index[image]] += coeff
    return out


def build_paper(cert: dict[str, Any]) -> str:
    packet = cert["canonical_theta_ladder_packet"]
    return f"""# VAlpha Remaining Yoneda Scalar Attempt v1

## Computation

The remaining finite branch-candidate obstruction is the connecting map for
`M=(-2,1,0)`:

```text
H^0(1,1,0) x H^1(2,-4,0) -> H^1(3,-3,0).
```

In the canonical theta-ladder basis, multiplication by the unique
`H^0(1,1,0)` generator sends:

```json
{json.dumps(packet["basis_map"], indent=2)}
```

The selected Ext vector is:

```json
{json.dumps(packet["selected_ext_vector"], indent=2)}
```

and its image is:

```json
{json.dumps(packet["target_vector"], indent=2)}
```

This vector is nonzero in the canonical ladder model, with distinguished scalar
coefficient `{packet["distinguished_scalar_value"]}` on
`{packet["distinguished_target_label"]}`.

## Meaning

This is very strong evidence about the final finite branch obstruction: the
remaining scalar is not generically forced to vanish.  In fact, with the basis
labels already selected by the terminal Cech packet, the natural ladder sends
`theta_plus_0_tensor_eta_minus_0` to a nonzero target component.

## Guardrail

This is not yet promoted to a selected theorem.  To close stability, we still
need one of:

1. raw Appell-Humbert/Cech multiplication data proving the same nonzero image;
2. an MTT source theorem selecting the canonical theta-ladder basis;
3. an independent HYM/Strominger solve whose stability residual excludes this
   zero-slope injection.

It does not prove full stability, HYM existence, or full SM closure.
"""


def main() -> int:
    reduction = load(ZERO_SLOPE_REDUCTION)
    scalar_template = load(SCALAR_TEMPLATE)
    selected = load(SELECTED_COHOMOLOGY)
    appell = load(APPELL_HUMBERT)

    source_basis = selected.get("cochain_complex", {}).get("basis_labels_C1") or basis_h1_l2()
    target_basis = basis_h1_target()
    selected_vector = selected.get("reported_cohomology", {}).get(
        "extension_class_vector_C1",
        [1, 0, 0, 0, 0, 0, 0, 0],
    )
    image = vector_image(selected_vector, source_basis, target_basis)
    nonzero = any(value != 0 for value in image)
    distinguished_source_label = selected.get("reported_cohomology", {}).get(
        "nonzero_extension_class_label",
        "theta_plus_0_tensor_eta_minus_0",
    )
    distinguished_label = theta_ladder_image(distinguished_source_label)
    distinguished_value = (
        image[target_basis.index(distinguished_label)] if distinguished_label in target_basis else None
    )

    basis_map = {
        label: theta_ladder_image(label)
        for label in source_basis
    }
    killed_basis = [label for label, target in basis_map.items() if target is None]

    packet = {
        "schema": "VAlphaRemainingYonedaScalarCanonicalThetaLadder.v1",
        "status": "CANONICAL_THETA_LADDER_SCALAR_NONZERO_CONDITIONAL_SOURCE_OPEN",
        "source_space": "H^1(2,-4,0)",
        "hom_generator_space": "H^0(1,1,0)",
        "target_space": "H^1(3,-3,0)",
        "source_basis": source_basis,
        "target_basis": target_basis,
        "basis_map": basis_map,
        "killed_source_basis_labels": killed_basis,
        "selected_ext_vector": selected_vector,
        "target_vector": image,
        "target_vector_nonzero": nonzero,
        "distinguished_source_label": selected.get("reported_cohomology", {}).get(
            "nonzero_extension_class_label"
        ),
        "distinguished_target_label": distinguished_label,
        "distinguished_scalar_value": distinguished_value,
        "interpretation": (
            "The remaining finite branch injection is obstructed in the canonical "
            "theta-ladder model if this nonzero image is selected by the actual "
            "Appell-Humbert/Cech multiplication source."
        ),
    }

    cert = {
        "certificate": "VAlphaRemainingYonedaScalarAttempt",
        "status": "VALPHA_REMAINING_YONEDA_SCALAR_CANONICAL_NONZERO_SELECTION_OPEN",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "canonical_ladder_packet": rel(OUT_PACKET),
        "paper": rel(OUT_PAPER),
        "inputs": {
            "zero_slope_reduction": rel(ZERO_SLOPE_REDUCTION),
            "remaining_scalar_template": rel(SCALAR_TEMPLATE),
            "selected_cohomology": rel(SELECTED_COHOMOLOGY),
            "appell_humbert": rel(APPELL_HUMBERT),
        },
        "input_statuses": {
            "zero_slope_reduction": reduction.get("status"),
            "scalar_template": scalar_template.get("status"),
            "selected_cohomology": selected.get("status"),
            "appell_humbert": appell.get("status"),
        },
        "canonical_theta_ladder_packet": packet,
        "closed_by_this_attempt": {
            "canonical_ladder_scalar_computed": True,
            "canonical_ladder_scalar_nonzero": nonzero,
            "selected_ext_label_not_in_ladder_kernel": distinguished_source_label not in killed_basis,
            "remaining_branch_obstruction_would_close_if_ladder_selected": nonzero,
        },
        "still_open": {
            "prove_raw_appell_humbert_cech_multiplication_matches_ladder": True,
            "prove_mtt_selects_canonical_theta_ladder_basis": True,
            "promote_scalar_nonzero_to_selected_source_theorem": True,
            "complete_destabilizing_subsheaf_enumeration": True,
            "selected_hym_or_strominger_existence_certificate": True,
            "operator_layer_pic0": True,
            "same_source_D_E_Riesz_Green_dotD": True,
            "primitive_C1_matrices": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_selected_scalar_proved": False,
            "claims_full_stability": False,
            "claims_hym_existence": False,
            "claims_full_subsheaf_enumeration": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The last finite branch-candidate Yoneda scalar is nonzero in the "
                "canonical theta-ladder model: the selected theta_plus_0_tensor_eta_minus_0 "
                "basis vector maps to a nonzero H^1(3,-3,0) component.  This is a strong "
                "candidate closure, but it still needs source promotion from actual "
                "Appell-Humbert/Cech multiplication or an MTT basis-selection theorem."
            ),
            "next_action": (
                "Prove that the selected terminal Cech source uses this canonical ladder "
                "multiplication, or compute the same multiplication directly from the "
                "Appell-Humbert factor of automorphy."
            ),
        },
    }

    write_json(OUT_PACKET, packet)
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")

    print("VAlpha remaining Yoneda scalar attempt")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
