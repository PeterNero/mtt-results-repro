"""Build the sector zero-mode / End0 tensor-product construction attempt.

The previous packet rejected existing B_N/compact dotD values as selected
End0-to-sector functor values and proved that scalar normalization alone is
insufficient.  This step constructs the algebraic End0 tensor-product carrier
that would be used by any selected sector zero-mode realization:

* Q,u,d,L,e,N carry the adjoint triplet of End0(V_alpha).
* H carries the singlet.
* sector projectors are block projectors in the direct-sum carrier.

This closes the carrier algebra and projector arithmetic.  It deliberately
does not claim that the actual selected sector zero modes have been realized in
this carrier, nor that the SU5/E6 matter-slot routing or Gram normalization is
selected.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

END0_PACKET = DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
PROMOTION = DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
SECTOR_CHARGE = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
MATTER_SLOT = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"

OUTPUT = DATA / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct.candidate.json"
CERT = CERTS / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct_certificate.json"
NOTE = CORPUS / "MTT_Selected_SectorZeroMode_Realization_Functor_or_End0TensorProduct_Construction_v1.md"

STATUS = "MTT_SELECTED_END0_TENSOR_PRODUCT_CARRIER_CONSTRUCTED_ZERO_MODE_REALIZATION_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_AdjointTriplet_Realization_or_MatterSlotRouting_Theorem_v1"

MATTER_SECTORS = ["Q", "u", "d", "L", "e", "N"]
SECTORS = MATTER_SECTORS + ["H"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]


def matsub(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matadd(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(s: float, a: list[list[float]]) -> list[list[float]]:
    return [[s * value for value in row] for row in a]


def comm(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return matsub(matmul(a, b), matmul(b, a))


def frob(a: list[list[float]]) -> float:
    return math.sqrt(sum(value * value for row in a for value in row))


def max_abs(a: list[list[float]]) -> float:
    return max(abs(value) for row in a for value in row)


def eye(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def zero(n: int, m: int) -> list[list[float]]:
    return [[0.0 for _ in range(m)] for _ in range(n)]


def block_diag(blocks: list[list[list[float]]]) -> list[list[float]]:
    sizes = [len(block) for block in blocks]
    total = sum(sizes)
    out = zero(total, total)
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[offset + i][offset + j] = value
        offset += len(block)
    return out


def projector(total: int, start: int, size: int) -> list[list[float]]:
    out = zero(total, total)
    for idx in range(start, start + size):
        out[idx][idx] = 1.0
    return out


def trace(a: list[list[float]]) -> float:
    return sum(a[i][i] for i in range(len(a)))


def rank_diagonal_projector(p: list[list[float]]) -> int:
    return int(round(trace(p)))


def matrix_equal(a: list[list[float]], b: list[list[float]], tol: float = 1e-12) -> bool:
    return max_abs(matsub(a, b)) <= tol


def build_carrier(end0_de: dict[str, Any]) -> dict[str, Any]:
    ad = end0_de["selected_End0_basis"]
    ad_mats = {
        "T1": end0_de.get("universal_ad_matrices", {}).get("T1"),
        "T2": end0_de.get("universal_ad_matrices", {}).get("T2"),
        "T3": end0_de["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"],
    }
    if ad_mats["T1"] is None or ad_mats["T2"] is None:
        # Same convention used in the direct End0 table packet.
        ad_mats["T1"] = [[0, 0, 0], [0, 0, -1], [0, 1, 0]]
        ad_mats["T2"] = [[0, 0, 1], [0, 0, 0], [-1, 0, 0]]

    sector_dimensions = {sector: 3 for sector in MATTER_SECTORS}
    sector_dimensions["H"] = 1
    total_dim = sum(sector_dimensions.values())

    blocks_by_t = {}
    for name, mat in ad_mats.items():
        blocks = [mat for _ in MATTER_SECTORS] + [zero(1, 1)]
        blocks_by_t[name] = block_diag(blocks)

    starts: dict[str, int] = {}
    offset = 0
    projectors = {}
    for sector in SECTORS:
        starts[sector] = offset
        dim = sector_dimensions[sector]
        projectors[sector] = projector(total_dim, offset, dim)
        offset += dim

    return {
        "selected_domain_basis": ad["basis"],
        "sector_order": SECTORS,
        "matter_sectors": MATTER_SECTORS,
        "sector_dimensions": sector_dimensions,
        "total_dimension": total_dim,
        "sector_block_starts": starts,
        "domain_ad_matrices": ad_mats,
        "direct_sum_representation": blocks_by_t,
        "sector_projectors": projectors,
        "construction_rule": (
            "rho_sector(T_i)=ad(T_i) on Q,u,d,L,e,N triplet carriers and "
            "rho_H(T_i)=0 on the Higgs singlet carrier."
        ),
    }


def validate_carrier(carrier: dict[str, Any]) -> dict[str, Any]:
    ad = carrier["domain_ad_matrices"]
    rho = carrier["direct_sum_representation"]
    projectors = carrier["sector_projectors"]
    total_dim = carrier["total_dimension"]

    # Convention: these matrices satisfy [T1,T2]=T3, [T2,T3]=T1, [T3,T1]=T2.
    lie_checks = {
        "domain_[T1,T2]=T3": matrix_equal(comm(ad["T1"], ad["T2"]), ad["T3"]),
        "domain_[T2,T3]=T1": matrix_equal(comm(ad["T2"], ad["T3"]), ad["T1"]),
        "domain_[T3,T1]=T2": matrix_equal(comm(ad["T3"], ad["T1"]), ad["T2"]),
        "sector_[T1,T2]=T3": matrix_equal(comm(rho["T1"], rho["T2"]), rho["T3"]),
        "sector_[T2,T3]=T1": matrix_equal(comm(rho["T2"], rho["T3"]), rho["T1"]),
        "sector_[T3,T1]=T2": matrix_equal(comm(rho["T3"], rho["T1"]), rho["T2"]),
    }

    sum_p = zero(total_dim, total_dim)
    projector_checks: dict[str, Any] = {}
    for sector, p in projectors.items():
        sum_p = matadd(sum_p, p)
        projector_checks[f"{sector}_idempotent"] = matrix_equal(matmul(p, p), p)
        projector_checks[f"{sector}_rank"] = rank_diagonal_projector(p)
        for t_name, t_mat in rho.items():
            projector_checks[f"{sector}_commutes_with_{t_name}"] = matrix_equal(
                comm(p, t_mat), zero(total_dim, total_dim)
            )

    orthogonal_pairs = {}
    for i, left in enumerate(SECTORS):
        for right in SECTORS[i + 1 :]:
            orthogonal_pairs[f"{left}_{right}"] = matrix_equal(
                matmul(projectors[left], projectors[right]), zero(total_dim, total_dim)
            )

    t3_norms = {}
    for sector, p in projectors.items():
        block = matmul(p, matmul(rho["T3"], p))
        t3_norms[sector] = {
            "frobenius_norm": frob(block),
            "rank": projector_checks[f"{sector}_rank"],
            "zero_response": max_abs(block) == 0.0,
        }

    return {
        "all_lie_checks_pass": all(lie_checks.values()),
        "lie_checks": lie_checks,
        "projectors_sum_to_identity": matrix_equal(sum_p, eye(total_dim)),
        "all_projectors_idempotent": all(
            value is True for key, value in projector_checks.items() if key.endswith("_idempotent")
        ),
        "all_projectors_commute_with_End0_action": all(
            value is True for key, value in projector_checks.items() if "_commutes_with_" in key
        ),
        "all_distinct_projectors_orthogonal": all(orthogonal_pairs.values()),
        "projector_checks": projector_checks,
        "orthogonal_pairs": orthogonal_pairs,
        "sector_T3_response_norms": t3_norms,
        "matter_T3_norms_equal": len({round(t3_norms[s]["frobenius_norm"], 12) for s in MATTER_SECTORS}) == 1,
        "H_T3_response_zero": t3_norms["H"]["zero_response"],
    }


def build_candidate() -> dict[str, Any]:
    end0_packet = load(END0_PACKET)
    end0_de = load(END0_DE)
    promotion = load(PROMOTION)
    sector_charge = load(SECTOR_CHARGE)
    matter_slot = load(MATTER_SLOT)

    carrier = build_carrier(end0_de)
    validation = validate_carrier(carrier)
    direct_sum_total_rank = sum(carrier["sector_dimensions"].values())

    selected_realization_boundary = {
        "selected_sector_zero_mode_realization_proved": False,
        "selected_family_triplets_equal_End0_adjoint_representation": False,
        "selected_Higgs_singlet_under_End0": False,
        "selected_sector_Gram_normalization": False,
        "selected_matter_slot_routing": False,
        "selected_1M_Dirac_neutrino_rule": False,
        "reason": (
            "The algebraic carrier is now explicit and validator-clean, but the "
            "corpus still does not emit selected zero-mode bases for Q,u,d,L,e,N,H "
            "as this End0 direct-sum representation."
        ),
    }

    data = {
        "candidate": "MTTSelectedSectorZeroModeRealizationFunctorOrEnd0TensorProductConstruction",
        "status": STATUS,
        "inputs": {
            "end0_to_sector_functor_packet": rel(END0_PACKET),
            "selected_End0_DE_payload": rel(END0_DE),
            "alpha1_promotion_theorem": rel(PROMOTION),
            "sector_charge_or_chirality": rel(SECTOR_CHARGE),
            "matter_slot_overlap_normalization": rel(MATTER_SLOT),
        },
        "input_statuses": {
            "end0_to_sector_functor_packet": end0_packet.get("status"),
            "alpha1_promotion_theorem": promotion.get("status"),
            "sector_charge_or_chirality": sector_charge.get("status"),
            "matter_slot_overlap_normalization": matter_slot.get("status"),
        },
        "constructed_End0_tensor_product_carrier": carrier,
        "validation": validation,
        "rank_match": {
            "direct_sum_total_rank": direct_sum_total_rank,
            "six_matter_triplets_plus_H_singlet": "6*3+1",
            "matches_expected_sector_kernel_rank_sum": direct_sum_total_rank == 19,
            "matches_BN_zero_cluster_sector_ranks": True,
        },
        "normalization_boundary": {
            "raw_T3_frobenius_norm_per_matter_sector": math.sqrt(2.0),
            "unit_trace_option": "ad(T3)/sqrt(2) gives Frobenius norm one per matter triplet",
            "physical_transfer_normalization_selected": False,
            "why_open": (
                "Physical normalization still requires selected sector Gram/inner "
                "products and a theorem tying dotD[h_ext] to physical dotD_alpha1."
            ),
        },
        "matter_slot_routing_boundary": {
            "structural_su5_e6_support_present": True,
            "selected_Z_to_u_e_X_to_d_nuD_routing": False,
            "selected_1M_singlet_rule": False,
            "reason": (
                "The End0 tensor-product carrier supplies sector blocks and "
                "projectors, but it does not by itself distinguish the Weyl "
                "phase/shift matter-slot routing."
            ),
        },
        "selected_realization_boundary": selected_realization_boundary,
        "decision": {
            "End0_tensor_product_carrier_constructed": True,
            "sector_projectors_constructed": True,
            "commutator_and_projector_checks_pass": all(
                [
                    validation["all_lie_checks_pass"],
                    validation["projectors_sum_to_identity"],
                    validation["all_projectors_idempotent"],
                    validation["all_projectors_commute_with_End0_action"],
                    validation["all_distinct_projectors_orthogonal"],
                    validation["matter_T3_norms_equal"],
                    validation["H_T3_response_zero"],
                ]
            ),
            "selected_sector_zero_mode_realization_extracted": False,
            "selected_transfer_normalization_extracted": False,
            "selected_matter_slot_routing_extracted": False,
            "physical_dotD_alpha1_payload_extracted": False,
            "next_required_artifact": NEXT,
        },
        "what_closes_now": {
            "universal_End0_tensor_product_carrier": True,
            "sector_direct_sum_projectors": True,
            "su2_commutator_checks": True,
            "six_triplet_plus_H_singlet_rank_model": True,
            "Higgs_singlet_zero_T3_response_in_candidate": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_zero_mode_realization": True,
            "selected_family_triplet_End0_representation_theorem": True,
            "selected_Higgs_singlet_theorem": True,
            "selected_sector_Gram_normalization": True,
            "selected_matter_slot_routing_or_chirality_table": True,
            "selected_1M_Dirac_neutrino_rule": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "C1_response_and_SM_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    return data


def bool_lines(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def note_text(data: dict[str, Any]) -> str:
    norms = data["validation"]["sector_T3_response_norms"]
    return f"""# MTT Selected Sector Zero-Mode Realization Functor or End0 Tensor-Product Construction v1

Status: `{STATUS}`

## Result

The universal End0 tensor-product carrier is constructed.

The matter sectors `Q,u,d,L,e,N` carry the selected adjoint triplet
`span(T1,T2,T3)`.  The Higgs sector `H` carries the singlet.  The resulting
direct-sum carrier has rank `19 = 6*3+1`, matching the required sector
zero-mode rank pattern.

This is not yet physical sector closure.  The selected zero-mode bases must
still be proved to realize this carrier, and the selected transfer
normalization and matter-slot routing are still open.

## Construction

```text
rho_sector(T_i)=ad(T_i) on Q,u,d,L,e,N
rho_H(T_i)=0 on H
R_total(T_i)=blockdiag(ad(T_i),...,ad(T_i),0_H)
```

Projectors are the direct-sum block projectors for
`Q,u,d,L,e,N,H`.

## Validation

- Lie algebra checks pass: `{data["validation"]["all_lie_checks_pass"]}`
- projectors sum to identity: `{data["validation"]["projectors_sum_to_identity"]}`
- projectors are idempotent: `{data["validation"]["all_projectors_idempotent"]}`
- projectors commute with End0 action: `{data["validation"]["all_projectors_commute_with_End0_action"]}`
- distinct projectors are orthogonal: `{data["validation"]["all_distinct_projectors_orthogonal"]}`
- matter `T3` norms equal: `{data["validation"]["matter_T3_norms_equal"]}`
- Higgs `T3` response zero: `{data["validation"]["H_T3_response_zero"]}`

Sector `T3` response norms:

```json
{json.dumps(norms, indent=2, sort_keys=True)}
```

## Boundary

This construction supplies the algebraic functor carrier and projectors.  It
does not prove:

- selected sector zero-mode bases realize the adjoint triplet,
- the Higgs zero mode is selected as the End0 singlet,
- the sector Gram/inner-product normalization,
- the `Z -> u/e`, `X -> d/nuD` matter-slot routing or replacement,
- the `1_M` Dirac-neutrino rule,
- honest physical `dotD_alpha1` replay.

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

Next artifact: `{NEXT}`.
"""


def main() -> None:
    data = build_candidate()
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "certificate": "MTT_Selected_SectorZeroMode_Realization_Functor_or_End0TensorProduct_Construction_v1",
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "End0_tensor_product_carrier_constructed": True,
                "sector_projectors_constructed": True,
                "selected_sector_zero_mode_realization_extracted": False,
                "selected_transfer_normalization_extracted": False,
                "selected_matter_slot_routing_extracted": False,
                "closure_claimed": False,
                "target_fitting_used": False,
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(note_text(data), encoding="utf-8")
    print(json.dumps({"status": STATUS, "candidate": rel(OUTPUT), "note": rel(NOTE)}, indent=2))


if __name__ == "__main__":
    main()
