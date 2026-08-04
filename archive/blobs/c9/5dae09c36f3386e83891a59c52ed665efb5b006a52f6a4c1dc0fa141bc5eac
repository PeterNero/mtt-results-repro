"""Build the selected End0-to-sector functor source/value packet attempt.

This is the next gate after the alpha1 value-fill attempt.  It tests whether
the existing End0 response can already be routed into sector dotD values, and
records the minimal selected functor that would be required.
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

VALUE_FILL = DATA / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
END0_BASIS = DATA / "selected_end0_basis_differential_table_or_bn_identification.candidate.json"
TANGENT_THEOREM = DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
BN_DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn.candidate.json"
BN_HONEST = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn" / "sector_projectors_dotd_on_smooth_bn.honest.json"
COMPACT_DOTD = DATA / "selected_routec_strominger_galerkin_solve" / "dotd_response.candidate.json"
OPERATOR_PACKET = DATA / "selected_routec_selected_operator_source_and_overlap_tensor_packet.candidate.json"
SECTOR_ROUTING = DATA / "selected_routec_weylpair_sector_routing_source_lemma.candidate.json"
SOURCE_TO_C1 = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"

OUTPUT = DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"
CERT = CERTS / "selected_end0_to_sector_functor_source_and_value_packet_certificate.json"
NOTE = CORPUS / "MTT_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1.md"

STATUS = "MTT_SELECTED_END0_TO_SECTOR_FUNCTOR_PACKET_ATTEMPTED_EXISTING_VALUES_REJECTED_FUNCTOR_OBJECT_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_Realization_Functor_or_End0TensorProduct_Construction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def flatten_numbers(obj: Any) -> list[float]:
    out: list[float] = []
    if isinstance(obj, (int, float)):
        out.append(float(obj))
    elif isinstance(obj, list):
        for item in obj:
            out.extend(flatten_numbers(item))
    return out


def summarize_dotd_slots(packet: dict[str, Any]) -> dict[str, dict[str, Any]]:
    slots = packet["dotd_response_slots"]
    summary: dict[str, dict[str, Any]] = {}
    for sector, slot in slots.items():
        vals = flatten_numbers(slot["dotD_alpha1_matrix"])
        nonzero = [v for v in vals if abs(v) > 1e-15]
        summary[sector] = {
            "dimension": slot.get("dimension"),
            "expected_kernel_dimension": slot.get("expected_kernel_dimension"),
            "selected_dotD_source_verified": slot.get("selected_dotD_source_verified"),
            "alpha1_driver_verified": slot.get("alpha1_driver_verified"),
            "nonzero_entries": len(nonzero),
            "frobenius_norm": math.sqrt(sum(v * v for v in vals)),
            "min": min(vals) if vals else None,
            "max": max(vals) if vals else None,
        }
    return summary


def note_text(candidate: dict[str, Any]) -> str:
    return f"""# MTT Selected End0 to SectorFunctor Source and Value Packet v1

Status: `{STATUS}`

## Question

Can the selected row-model End0 response

```text
dotD_a[h_ext] = (partial_a h_ext) ad(T3)
```

already be routed into physical sector `dotD_alpha1` matrices?

## Result

Not yet.  The existing packets do not supply a selected functor

```text
R_sector : End0(V_alpha) -> sector zero-mode response packets.
```

The obstruction is not a missing scalar.  A scalar normalization cannot turn
the three-dimensional real adjoint lane `span(T1,T2,T3)` into the sector
zero-mode packets `Q,u,d,L,e,N,H`; it also cannot supply the sector projectors,
family multiplicity, Higgs rank-one carrier, or the `Z/X` matter-slot routing.

## Existing Values Rejected

- The 27-mode `B_N` packet is still rejected as selected `End0(V_alpha)` data:
  it is a gerbe-twisted projective/qutrit execution scaffold, not an ordinary
  adjoint table.
- The compact sector `dotD` matrices are shape-compatible diagnostics, but
  `selected_dotD_source_verified=false` and `alpha1_driver_verified=false` in
  every sector.
- The conditional Weyl transfer is exact only after assuming sector routing and
  normalization; those are precisely the missing selected values.

## Minimal Functor Object

The next object must emit:

1. a selected domain basis map from `T1,T2,T3` into sector response carriers,
2. selected sector zero-mode carriers/projectors for `Q,u,d,L,e,N,H`,
3. a normalization mapping `dotD[h_ext]` to sector `dotD_alpha1`,
4. a selected matter-slot/routing rule, especially `Z -> u/e` and
   `X -> d/nuD` or a replacement rule,
5. an honest validator replay where selected source flags are theorem-derived.

## What Closes Here

The existing values are rejected as physical sector values, and the exact
missing functor/value packet is specified.  This avoids turning a useful
diagnostic scaffold into a proof by naming.

Next artifact: `{NEXT}`.
"""


def main() -> None:
    value_fill = load(VALUE_FILL)
    end0_de = load(END0_DE)
    end0_basis = load(END0_BASIS)
    tangent = load(TANGENT_THEOREM)
    bn_dotd = load(BN_DOTD)
    bn_honest = load(BN_HONEST)
    compact = load(COMPACT_DOTD)
    operator_packet = load(OPERATOR_PACKET)
    sector_routing = load(SECTOR_ROUTING)
    source_to_c1 = load(SOURCE_TO_C1)

    end0_basis_selected = end0_basis["path_A_identify_existing_BN"]["closed"] is True
    bn_rejected_as_end0 = end0_basis["path_A_identify_existing_BN"]["result"] == "REJECTED_AS_SELECTED_END0_TABLE"
    compact_summary = summarize_dotd_slots(compact)
    bn_summary = summarize_dotd_slots(bn_honest)

    family_frobs = {
        k: v["frobenius_norm"]
        for k, v in compact_summary.items()
        if k in {"Q", "u", "d", "L", "e", "N"}
    }
    family_norms_identical = len({round(v, 12) for v in family_frobs.values()}) == 1

    existing_values_test = {
        "candidate": "ExistingBNDotDOrCompactSectorMatricesAsSelectedFunctorValues",
        "passes": False,
        "bn_rejected_as_selected_End0_basis": bn_rejected_as_end0,
        "honest_bn_validator_fails_only_by_source_flags": bn_dotd["validation"]["honest_validator_fails_only_by_source_driver_flags"] is True,
        "all_compact_sector_flags_false": all(
            v["selected_dotD_source_verified"] is False and v["alpha1_driver_verified"] is False
            for v in compact_summary.values()
        ),
        "compact_family_sector_norms_identical": family_norms_identical,
        "conditional_weyl_transfer_exact_but_unselected": source_to_c1["conditional_transfer_map"]["conditional_exact"] is True
        and source_to_c1["selected_status"]["selected_sector_routing_emitted"] is False,
        "reason": (
            "Existing sector matrices are diagnostic/conditional carriers. They lack theorem-derived source flags, "
            "and the B_N execution scaffold is explicitly not the selected End0 basis."
        ),
    }

    scalar_normalization_no_go = {
        "closed": True,
        "statement": (
            "No scalar normalization of the selected T3-row response can by itself define R_sector, because "
            "the codomain requires sector carriers, zero-mode projectors, family/Higgs multiplicities, and matter-slot routing."
        ),
        "domain_basis": end0_de["selected_End0_basis"]["basis"],
        "domain_adT3_matrix": end0_de["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"],
        "codomain_sectors": ["Q", "u", "d", "L", "e", "N", "H"],
        "requires_tensor_product_or_realization_functor": True,
    }

    minimal_functor_contract = {
        "name": "SelectedEnd0ToSectorFunctorContract",
        "status": "OPEN",
        "must_emit": [
            "selected domain basis map End0(V_alpha)[T1,T2,T3] -> sector carrier algebra",
            "selected sector zero-mode realization for Q,u,d,L,e,N,H",
            "sector projectors in the image of the selected End0 realization",
            "normalization of dotD[h_ext] relative to sector inner products/Gram matrices",
            "matter-slot routing or chirality table independent of locked target columns",
            "honest dotD validator packet with selected_dotD_source_verified=true and alpha1_driver_verified=true by theorem",
        ],
        "allowed_superset_paths": [
            "straight End0 tensor product with selected zero-mode representation",
            "Route-C/Strominger Galerkin realization if it emits ordinary End0 basis data",
            "typed monad/Cech matter-slot functor if it emits sector zero-mode bases",
            "SU5/E6 route only after selected matter-slot source and singlet-neutrino rule are proved",
        ],
        "forbidden_shortcuts": [
            "identify B_N with End0 after it was rejected as projective/qutrit scaffold",
            "set selected flags from diagnostic lifted packet",
            "choose Z/X routing because it solves locked target columns",
            "use observed masses, mixings, CP phases, or benchmark matrices",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedEnd0ToSectorFunctorSourceAndValuePacket",
        "status": STATUS,
        "inputs": {
            "alpha1_value_fill": rel(VALUE_FILL),
            "selected_End0_DE_payload": rel(END0_DE),
            "End0_BN_identification": rel(END0_BASIS),
            "alpha1_promotion_theorem": rel(TANGENT_THEOREM),
            "sector_projectors_dotd": rel(BN_DOTD),
            "BN_honest_dotd_payload": rel(BN_HONEST),
            "compact_dotd_response": rel(COMPACT_DOTD),
            "selected_operator_overlap_packet": rel(OPERATOR_PACKET),
            "sector_routing_source_lemma": rel(SECTOR_ROUTING),
            "source_to_C1_transfer_map": rel(SOURCE_TO_C1),
        },
        "selected_End0_domain": {
            "basis": end0_de["selected_End0_basis"]["basis"],
            "basis_selected": True,
            "adT3_matrix": end0_de["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"],
            "dotD_formula": tangent["theorem_slot"]["formal_statement"],
        },
        "existing_value_tests": existing_values_test,
        "scalar_normalization_no_go": scalar_normalization_no_go,
        "sector_value_summaries": {
            "compact_dotd_response": compact_summary,
            "BN_27mode_honest": bn_summary,
        },
        "minimal_functor_contract": minimal_functor_contract,
        "decision": {
            "selected_End0_to_sector_functor_values_extracted": False,
            "existing_BN_or_compact_values_promoted": False,
            "scalar_normalization_sufficient": False,
            "functor_contract_specified": True,
            "next_required_artifact": NEXT,
        },
        "superset_strategy": {
            "mode": "DUAL_REJECTION_PLUS_CONTRACT",
            "straight_path": "selected End0 row response in T1,T2,T3 is retained as domain data",
            "support_path": "B_N, compact Route-C dotD, Weyl transfer, and SU5/E6 clues are retained as shape support",
            "locked_target": "no measured constants and no lifted flags",
            "result": "existing values rejected; functor/zero-mode realization is the missing mathematical object",
        },
        "what_closes_now": {
            "existing_BN_values_rejected_as_selected_End0_sector_functor": True,
            "scalar_normalization_no_go_recorded": True,
            "selected_End0_domain_basis_retained": True,
            "minimal_functor_contract_emitted": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_sector_zero_mode_realization": True,
            "selected_End0_to_sector_functor_values": True,
            "selected_transfer_normalization": True,
            "selected_sector_charge_or_chirality_table": True,
            "physical_dotD_alpha1_same_branch_driver": True,
            "sector_dotD_alpha1_matrices": True,
            "C1_response_and_SM_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "certificate": "MTT_Selected_End0_to_SectorFunctor_Source_and_Value_Packet_v1",
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "existing_BN_or_compact_values_promoted": False,
                "scalar_normalization_sufficient": False,
                "functor_contract_specified": True,
                "selected_End0_to_sector_functor_values_extracted": False,
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
    NOTE.write_text(note_text(candidate), encoding="utf-8")

    print(json.dumps({"status": STATUS, "candidate": rel(OUTPUT), "note": rel(NOTE)}, indent=2))


if __name__ == "__main__":
    main()
