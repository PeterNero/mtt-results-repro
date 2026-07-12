"""Audit scalar finite-element deck gluing for the Iwasawa scaffold."""

from __future__ import annotations

import json
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_scalar_fe_gluing_certificate.json"
FILTER = CERT_DIR / "iwasawa_scalar_deck_mode_filter_certificate.json"
DECK = CERT_DIR / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
BASIS = CERT_DIR / "iwasawa_galerkin_basis_skeleton_certificate.json"
PROTOCOL = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
PAPER = ROOT / "Iwasawa_Scalar_Finite_Element_Gluing_Skeleton_v1.md"


Node = tuple[int, int, int, int, int, int]


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left != root_right:
            self.parent[root_right] = root_left


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def boundary_targets(node: Node, n: int) -> list[Node]:
    x1, x2, y1, y2, t1, t2 = node
    targets: list[Node] = []
    if x1 == n:
        targets.append((0, x2, y1, y2, (t1 - y1) % n, (t2 - y2) % n))
    if x2 == n:
        targets.append((x1, 0, y1, y2, (t1 + y2) % n, (t2 - y1) % n))
    if y1 == n:
        targets.append((x1, x2, 0, y2, t1, t2))
    if y2 == n:
        targets.append((x1, x2, y1, 0, t1, t2))
    if t1 == n:
        targets.append((x1, x2, y1, y2, 0, t2))
    if t2 == n:
        targets.append((x1, x2, y1, y2, t1, 0))
    return targets


def quotient_summary(n: int) -> dict[str, Any]:
    nodes = list(product(range(n + 1), repeat=6))
    index = {node: i for i, node in enumerate(nodes)}
    dsu = DisjointSet(len(nodes))
    constraint_count = 0

    for node in nodes:
        for target in boundary_targets(node, n):
            dsu.union(index[node], index[target])
            constraint_count += 1

    classes: dict[int, list[Node]] = {}
    for node in nodes:
        classes.setdefault(dsu.find(index[node]), []).append(node)

    half_open = set(product(range(n), repeat=6))
    half_open_counts = [
        sum(1 for node in members if node in half_open)
        for members in classes.values()
    ]

    return {
        "N": n,
        "closed_node_count": len(nodes),
        "constraint_count": constraint_count,
        "class_count": len(classes),
        "expected_class_count": n**6,
        "half_open_count_min": min(half_open_counts),
        "half_open_count_max": max(half_open_counts),
        "all_classes_have_one_half_open_rep": all(count == 1 for count in half_open_counts),
    }


def main() -> None:
    cert = load_json(CERT)
    filt = load_json(FILTER)
    deck = load_json(DECK)
    basis = load_json(BASIS)
    protocol = load_json(PROTOCOL)
    paper = read(PAPER)

    grid = cert.get("grid_model", {})
    boundary = cert.get("boundary_identifications", {})
    constraints = cert.get("constraint_rule", {})
    samples = cert.get("sample_audit_targets", {})
    implication = cert.get("finite_basis_implication", {})
    closes = cert.get("what_this_closes", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    sample_ns = samples.get("N_values", [])
    summaries = [quotient_summary(int(n)) for n in sample_ns]
    expected_nodes = samples.get("expected_closed_node_counts", {})
    expected_dofs = samples.get("expected_quotient_dof_counts", {})

    boundary_text = " ".join(boundary.values())
    constraint_text = " ".join(constraints.values())
    implication_text = " ".join(implication.values())
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status")
            == "IWASAWA_SCALAR_FE_GLUING_SKELETON_FORMULATED_BUNDLE_DE_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if filt.get("status")
            == "IWASAWA_SCALAR_DECK_MODE_FILTER_FORMULATED_SELECTED_MODES_OPEN"
            and deck.get("status")
            == "STANDARD_IWASAWA_DECK_SCAFFOLD_FORMULATED_SELECTION_OPEN"
            and basis.get("status")
            == "GALERKIN_BASIS_SKELETON_FORMULATED_SCALAR_DECK_DATA_OPEN"
            and protocol.get("status")
            == "NONINVARIANT_GALERKIN_EXECUTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            else "FAIL",
            "scalar filter, deck, basis skeleton, and Galerkin protocol imported",
        ),
        Gate(
            "grid model",
            "PASS"
            if grid.get("subdivision_parameter") == "N >= 1"
            and "{0,...,N}^6" in grid.get("closed_cell_nodes", "")
            and "{0,...,N-1}^6" in grid.get("half_open_representatives", "")
            and grid.get("closed_node_count") == "(N+1)^6"
            and grid.get("scalar_quotient_dof_count") == "N^6 after deck boundary gluing"
            else "FAIL",
            str(grid),
        ),
        Gate(
            "boundary maps",
            "PASS"
            if set(boundary)
            == {"x1_face", "x2_face", "y1_face", "y2_face", "t1_face", "t2_face"}
            and contains_all(
                boundary_text,
                [
                    "(t1-y1) mod N",
                    "(t2-y2) mod N",
                    "(t1+y2) mod N",
                    "(t2-y1) mod N",
                    "(x1,x2,0,y2,t1,t2)",
                    "(x1,x2,y1,0,t1,t2)",
                    "(x1,x2,y1,y2,0,t2)",
                    "(x1,x2,y1,y2,t1,0)",
                ],
            )
            else "FAIL",
            boundary_text,
        ),
        Gate(
            "constraint rule",
            "PASS"
            if contains_all(
                constraint_text,
                [
                    "u[source_node]-u[target_node]=0",
                    "one scalar nodal degree of freedom",
                    "quotient class representative",
                ],
            )
            else "FAIL",
            constraint_text,
        ),
        Gate(
            "sample quotient counts",
            "PASS"
            if all(
                summary["closed_node_count"] == int(expected_nodes[str(summary["N"])])
                and summary["class_count"] == int(expected_dofs[str(summary["N"])])
                and summary["class_count"] == summary["expected_class_count"]
                for summary in summaries
            )
            else "FAIL",
            str(summaries),
        ),
        Gate(
            "half-open representatives",
            "PASS"
            if all(summary["all_classes_have_one_half_open_rep"] for summary in summaries)
            and samples.get("expected_half_open_representative_count_per_class") == 1
            else "FAIL",
            str(summaries),
        ),
        Gate(
            "finite basis implication",
            "PASS"
            if contains_all(
                implication_text,
                [
                    "continuous or spectral-element functions",
                    "increase N",
                    "s_N*3*binomial(3,p)",
                    "rho_E",
                    "Gram and stiffness",
                ],
            )
            else "FAIL",
            implication_text,
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("finite_element_boundary_maps") is True
            and closes.get("scalar_nodal_constraint_rule") is True
            and closes.get("sample_quotient_dof_counts") is True
            and closes.get("half_open_representative_check") is True
            and closes.get("finite_element_route_made_executable_at_scalar_level") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if all(open_items.values())
            and contains_all(
                open_text,
                [
                    "MTT_selection_or_source_confirmation_of_Gamma0",
                    "selected_mesh_subdivision_sequence",
                    "finite_element_shape_functions_and_polynomial_order",
                    "bundle_transition_matrices_rho_E",
                    "selected_D_E_action_on_FE_basis",
                    "Riesz_projector_gap_error_certificate",
                ],
            )
            else "FAIL",
            str(open_items),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_Gamma0_is_MTT_selected") is False
            and guardrails.get("claims_selected_scalar_FE_space_constructed") is False
            and guardrails.get("uses_naive_periodic_torus_gluing") is False
            and guardrails.get("claims_bundle_transitions_constructed") is False
            and guardrails.get("claims_selected_D_E_constructed") is False
            and guardrails.get("claims_Galerkin_matrices_constructed") is False
            and guardrails.get("claims_kernel_dimension_three_now") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("closes_scalar_FE_gluing_skeleton") is True
            and verdict.get("closes_bundle_FE_gluing") is False
            and verdict.get("closes_selected_Galerkin_space") is False
            and "rho_E" in verdict.get("next_step", "")
            and "selected D_E" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records FE gluing",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa Scalar Finite-Element Gluing Skeleton",
                    "(N,x2,y1,y2,t1,t2)",
                    "(t1-y1) mod N",
                    "(t1+y2) mod N",
                    "u[source_node] - u[target_node] = 0",
                    "N=4: closed nodes 15625, quotient dofs 4096",
                    "naive six-torus periodic mesh is not valid",
                    "rho_E",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa scalar finite-element gluing audit")
    print("=========================================")
    print()
    for summary in summaries:
        print(
            "N={N}: closed_nodes={closed_node_count}, constraints={constraint_count}, "
            "classes={class_count}, half_open_rep_range={half_open_count_min}..{half_open_count_max}".format(
                **summary
            )
        )
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
