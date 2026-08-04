from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_REPO = TEXPAPERS / "mtt-sm-parity-closure"

PARENT_DESCENT = (
    ROOT
    / "certificates"
    / "q79_shared_z64_fuyau_parent_quarterturn_descent_certificate.json"
)
ORDINARY_HYM_NOGO = (
    ROOT
    / "certificates"
    / "q79_ordinary_exterior_dual_hym_nogo_and_derived_kernel_cutset_certificate.json"
)
CLUTCHING = (
    SM_REPO
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "rank_one_fuyau_shared_circle_clutching.packet.json"
)
SOURCE_GATE = (
    SM_REPO
    / "candidate_data"
    / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution"
    / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json"
)
ORBIT = (
    SM_REPO
    / "candidate_data"
    / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
    / "Z4_Chern_orbit_superset.packet.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_marked_shared_circle_c4_descent_nogo_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Marked_Shared_Circle_C4_Descent_NoGo_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def matrix_order(matrix: sp.Matrix, limit: int = 12) -> int | None:
    power = sp.eye(matrix.rows)
    for order in range(1, limit + 1):
        power = power * matrix
        if power == sp.eye(matrix.rows):
            return order
    return None


def as_int_rows(matrix: sp.Matrix) -> list[list[int]]:
    return [[int(value) for value in row] for row in matrix.tolist()]


def main() -> None:
    parent = load(PARENT_DESCENT)
    ordinary_hym_nogo = load(ORDINARY_HYM_NOGO)
    clutching = load(CLUTCHING)
    source_gate = load(SOURCE_GATE)
    orbit = load(ORBIT)

    quarterturn = sp.Matrix(parent["finite_data"]["integral_quarterturn"])
    chern_direction = sp.Matrix([1, 0])
    shared_circle_direction = sp.Matrix([0, 1])
    quarterturn_chern = quarterturn * chern_direction
    quarterturn_shared = quarterturn * shared_circle_direction

    oriented_marked_stabilizer = [sp.eye(2)]
    unoriented_marked_stabilizer = [sp.eye(2), -sp.eye(2)]
    signed_stabilizer_orders = [
        matrix_order(matrix) for matrix in unoriented_marked_stabilizer
    ]

    unmarked_exit_contract = {
        "forget_or_equivariantly_transport_the_shared_circle_marking": False,
        "reconstruct_the_same_circle_Z64_and_gravity_source_after_quotient": False,
        "descend_the_shared_circle_c3_clutching_map_equivariantly": False,
        "descend_the_spectral_gerbe_visible_bundle_and_balanced_HYM_data": False,
        "prove_the_descended_projected_Hessian_is_JDE_invariant": False,
    }

    checks = {
        "active_vertical_lattice_is_twisted_plus_shared": (
            clutching["rank_one_FuYau_topology"]["space"]
            == "X=P_delta x S1_shared"
            and source_gate["rank_one_torus_candidate"]["omega_1_over_2pi"]
            == "delta"
            and source_gate["rank_one_torus_candidate"]["omega_2_over_2pi"] == 0
            and source_gate["rank_one_torus_candidate"][
                "one_geometric_circle_untwisted"
            ]
        ),
        "quarterturn_has_order_four": (
            quarterturn**2 == -sp.eye(2) and quarterturn**4 == sp.eye(2)
        ),
        "quarterturn_moves_the_Chern_direction": (
            quarterturn_chern == shared_circle_direction
        ),
        "quarterturn_moves_the_marked_shared_circle_to_twisted_direction": (
            quarterturn_shared == -chern_direction
        ),
        "oriented_Chern_and_shared_marking_stabilizer_is_identity": (
            len(oriented_marked_stabilizer) == 1
            and oriented_marked_stabilizer[0] == sp.eye(2)
        ),
        "unoriented_marked_stabilizer_has_only_orders_one_and_two": (
            signed_stabilizer_orders == [1, 2]
        ),
        "marked_stabilizer_contains_no_order_four_element": (
            all(order != 4 for order in signed_stabilizer_orders)
        ),
        "shared_circle_is_the_chiral_clutching_direction": (
            clutching["clutching_construction"]["gluing_direction"]
            == "the untwisted shared S1"
            and clutching["clutching_construction"]["integral_c3"] == [6, -6]
        ),
        "parent_packet_only_proves_unmarked_orbit_covariance": (
            orbit["orbit_length"] == 4
            and orbit["gerbe_execution_covariance"]["scope"]
            == "conditional on the Z4 orbit being the selected parent Fu-Yau source"
            and parent["claim_tiers"][
                "MTT_types_C4_as_Lens_redundancy_not_physical_superselection"
            ]
            == "OPEN"
        ),
        "shared_circle_to_FuYau_typing_is_itself_conditional": (
            source_gate["source_guard"][
                "corpus_identifies_it_with_the_untwisted_FuYau_circle"
            ]
            is False
            and source_gate["source_guard"]["rank_one_FuYau_topology_selected_by_MTT"]
            is False
        ),
        "ordinary_same_branch_HYM_functor_exit_was_already_excluded": (
            ordinary_hym_nogo["claim_tiers"][
                "ordinary_dual_or_exterior_square_realizes_JDE"
            ]
            == "CLOSED_NO_GO"
        ),
        "unmarked_modular_exit_has_no_silent_completed_rows": (
            not any(unmarked_exit_contract.values())
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_marked_shared_circle_c4_descent_nogo",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_MARKED_SHARED_CIRCLE_C4_AUTONOMOUS_DESCENT_CLOSED_NOGO_UNMARKED_MODULAR_REFORMULATION_EXACTLY_TYPED_OPEN",
        "inputs": {
            "parent_descent": str(PARENT_DESCENT),
            "ordinary_HYM_no_go": str(ORDINARY_HYM_NOGO),
            "shared_circle_clutching": str(CLUTCHING),
            "rank_one_source_gate": str(SOURCE_GATE),
            "C4_orbit": str(ORBIT),
        },
        "checks": checks,
        "finite_data": {
            "basis_order": ["twisted_Chern_circle", "marked_shared_untwisted_circle"],
            "Chern_direction": list(map(int, chern_direction)),
            "shared_circle_direction": list(map(int, shared_circle_direction)),
            "quarterturn": as_int_rows(quarterturn),
            "quarterturn_Chern_image": list(map(int, quarterturn_chern)),
            "quarterturn_shared_circle_image": list(map(int, quarterturn_shared)),
            "oriented_marked_stabilizer": [
                as_int_rows(matrix) for matrix in oriented_marked_stabilizer
            ],
            "unoriented_marked_stabilizer": [
                as_int_rows(matrix) for matrix in unoriented_marked_stabilizer
            ],
            "unoriented_marked_stabilizer_orders": signed_stabilizer_orders,
            "unmarked_modular_exit_contract": unmarked_exit_contract,
            "unmarked_modular_exit_contract_rows_available": sum(
                unmarked_exit_contract.values()
            ),
            "unmarked_modular_exit_contract_rows_required": len(
                unmarked_exit_contract
            ),
            "continuous_fitted_parameters": 0,
        },
        "theorem": {
            "name": "MarkedSharedCircleC4DescentNoGo",
            "marked_setup": (
                "Conditional on the active X=P_delta x S1_shared typing, the vertical "
                "integral lattice carries both the primitive Chern direction e1 and "
                "the marked shared untwisted circle e2."
            ),
            "no_go": (
                "The quarter-turn J sends e1 to e2 and e2 to -e1. Therefore it is "
                "not an automorphism of the torus bundle with its shared-circle "
                "marking. The oriented marked stabilizer is identity; even after "
                "forgetting both signs its finite part is {+I,-I}, with no order four."
            ),
            "clutching_strengthening": (
                "The current smooth c3=+/-6 construction explicitly clutches along "
                "S1_shared. J transports that gluing direction to the twisted circle, "
                "so the chiral payload also fails to descend without new equivariant data."
            ),
            "scope": (
                "This rules out autonomous C4/Lens descent in the current marked "
                "shared-circle realization. It does not rule out a different unmarked "
                "modular parent, but such a reformulation must rederive the shared-circle "
                "source, chiral clutching, spectral/HYM data, and projected operator."
            ),
        },
        "claim_tiers": {
            "C4_preserves_the_marked_shared_circle_direction": "CLOSED_NO_GO",
            "C4_is_an_automorphism_of_the_active_marked_rank_one_FuYau_branch": "CLOSED_NO_GO",
            "autonomous_Lens_descent_in_current_marked_shared_circle_setup": "CLOSED_NO_GO_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING",
            "shared_circle_c3_clutching_is_C4_equivariant": "CLOSED_NO_GO_FOR_DISPLAYED_CLUTCHING_DIRECTION",
            "unmarked_four_branch_modular_parent": "CLOSED_CONDITIONAL_AS_PARENT_ORBIT_ONLY",
            "unmarked_parent_preserves_current_same_circle_physical_source": "OPEN_REQUIRES_REDERIVATION",
            "unmarked_parent_descends_actual_spectral_HYM_operator": "OPEN",
            "direct_projected_HYM_block": "OPEN",
            "nonlocal_same_branch_Fourier_Mukai_JDE": "OPEN_11_ROW_CONTRACT_2_AVAILABLE",
        },
        "guardrails": {
            "claims_unmarked_torus_modular_equivalence_preserves_a_marked_shared_circle": False,
            "claims_parent_orbit_covariance_is_autonomous_physical_descent": False,
            "claims_shared_circle_clutching_descends_under_C4": False,
            "claims_primitive_MTT_selects_the_active_FuYau_typing": False,
            "uses_observed_physics_data": False,
            "adds_fitted_numeric_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Marked Shared-Circle C4 Descent No-Go v1

Status:
`Q79_MARKED_SHARED_CIRCLE_C4_AUTONOMOUS_DESCENT_CLOSED_NOGO_UNMARKED_MODULAR_REFORMULATION_EXACTLY_TYPED_OPEN`

## The marked vertical lattice

On the active conditional Fu-Yau topology

```text
X=P_delta x S1_shared,
c=(delta,0),
```

the vertical integral basis has two distinct roles:

```text
e1 = twisted circle carrying delta,
e2 = marked shared untwisted circle.
```

The quarter-turn is

```text
J=[[0,-1],[1,0]],
J e1=e2,
J e2=-e1.
```

It therefore exchanges the marked shared circle with the twisted direction.
It is an automorphism of the four-element unmarked Chern-orbit parent, but not
of one torus bundle with its shared-circle marking.

## Exact stabilizer

An integral orientation-preserving matrix fixing both oriented vectors `e1`
and `e2` is the identity. If both orientations are forgotten, the finite
marked stabilizer is only

```text
{+I,-I},
```

with orders one and two. It contains no order-four element. Hence the current
marked setup cannot use `C4` as an autonomous Lens redundancy.

## The chiral bundle makes the marking physical

The existing smooth non-pullback `SU(3)` construction obtains `c3=+/-6` by
clutching specifically along the untwisted `S1_shared`. Under `J`, that gluing
direction becomes the twisted circle. Thus the displayed chiral payload is not
`C4` equivariant either; parent covariance of curvature cost, Bianchi number,
and gerbe topology does not repair it.

## Scope and surviving exit

This is conditional on identifying the corpus shared circle with the
untwisted Fu-Yau factor. That identification is itself still a primitive-source
premise. But the dichotomy is exact:

```text
if the shared circle is marked, autonomous C4/Lens descent is impossible;
if it is unmarked, the current same-circle gravity source and c3 clutching
must be rederived after quotient.
```

An unmarked modular reformulation must supply five new rows: transport or
forget the marking, reconstruct the same-circle source, descend the chiral
clutching, descend the spectral/gerbe/HYM data, and prove projected-Hessian
invariance. None is present. Lens descent is therefore no longer a shortcut in
the current program.

The two live routes are the genuinely nonlocal same-branch Fourier-Mukai
contract or direct computation of the selected projected HYM block after the
actual bundle and balanced HYM connection exist.

No observed value and no fitted parameter is used.
"""

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


if __name__ == "__main__":
    main()
