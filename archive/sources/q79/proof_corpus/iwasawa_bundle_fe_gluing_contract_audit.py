"""Audit the rank-three bundle finite-element gluing contract."""

from __future__ import annotations

import json
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_bundle_fe_gluing_contract_certificate.json"
RHO_TEMPLATE = CERT_DIR / "iwasawa_bundle_rhoE_data.template.json"
SCALAR_FE = CERT_DIR / "iwasawa_scalar_fe_gluing_certificate.json"
SCALAR_FILTER = CERT_DIR / "iwasawa_scalar_deck_mode_filter_certificate.json"
BASIS = CERT_DIR / "iwasawa_galerkin_basis_skeleton_certificate.json"
PROTOCOL = CERT_DIR / "iwasawa_non_invariant_galerkin_protocol_certificate.json"
ZERO_MODE = CERT_DIR / "selected_zero_mode_basis_dotd_interface_certificate.json"
PAPER = ROOT / "Iwasawa_Bundle_Finite_Element_Gluing_Contract_v1.md"


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


def boundary_targets(node: Node, n: int) -> list[tuple[str, Node]]:
    x1, x2, y1, y2, t1, t2 = node
    targets: list[tuple[str, Node]] = []
    if x1 == n:
        targets.append(("g1", (0, x2, y1, y2, (t1 - y1) % n, (t2 - y2) % n)))
    if x2 == n:
        targets.append(("g2", (x1, 0, y1, y2, (t1 + y2) % n, (t2 - y1) % n)))
    if y1 == n:
        targets.append(("g3", (x1, x2, 0, y2, t1, t2)))
    if y2 == n:
        targets.append(("g4", (x1, x2, y1, 0, t1, t2)))
    if t1 == n:
        targets.append(("g5", (x1, x2, y1, y2, 0, t2)))
    if t2 == n:
        targets.append(("g6", (x1, x2, y1, y2, t1, 0)))
    return targets


def scalar_class_count(n: int) -> int:
    nodes = list(product(range(n + 1), repeat=6))
    index = {node: i for i, node in enumerate(nodes)}
    dsu = DisjointSet(len(nodes))
    for node in nodes:
        for _, target in boundary_targets(node, n):
            dsu.union(index[node], index[target])
    return len({dsu.find(i) for i in range(len(nodes))})


def main() -> None:
    cert = load_json(CERT)
    rho_template = load_json(RHO_TEMPLATE)
    scalar_fe = load_json(SCALAR_FE)
    scalar_filter = load_json(SCALAR_FILTER)
    basis = load_json(BASIS)
    protocol = load_json(PROTOCOL)
    zero_mode = load_json(ZERO_MODE)
    paper = read(PAPER)

    convention = cert.get("section_convention", {})
    boundary_rule = cert.get("boundary_constraint_rule", {})
    face_labels = cert.get("generator_face_labels", {})
    required = cert.get("required_rhoE_data", {})
    smoke = cert.get("sample_trivial_rho_check", {})
    closes = cert.get("what_this_closes", {})
    open_items = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    sample_ns = smoke.get("N_values", [])
    bundle_counts = {str(n): convention.get("rank", 0) * scalar_class_count(int(n)) for n in sample_ns}
    expected_counts = smoke.get("expected_bundle_quotient_dof_counts", {})

    convention_text = " ".join(str(value) for value in convention.values())
    boundary_text = " ".join(str(value) for value in boundary_rule.values())
    face_text = " ".join(
        str(value)
        for face in face_labels.values()
        for value in face.values()
    )
    required_text = " ".join(str(value) for value in required.values())
    open_text = " ".join(open_items)

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status")
            == "IWASAWA_BUNDLE_FE_GLUING_CONTRACT_FORMULATED_RHOE_DATA_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "dependencies align",
            "PASS"
            if scalar_fe.get("status")
            == "IWASAWA_SCALAR_FE_GLUING_SKELETON_FORMULATED_BUNDLE_DE_OPEN"
            and scalar_filter.get("status")
            == "IWASAWA_SCALAR_DECK_MODE_FILTER_FORMULATED_SELECTED_MODES_OPEN"
            and basis.get("status")
            == "GALERKIN_BASIS_SKELETON_FORMULATED_SCALAR_DECK_DATA_OPEN"
            and protocol.get("status")
            == "NONINVARIANT_GALERKIN_EXECUTION_PROTOCOL_FORMULATED_VALUES_OPEN"
            and zero_mode.get("status")
            == "SELECTED_ZERO_MODE_DOTD_INTERFACE_FORMULATED_VALUES_OPEN"
            else "FAIL",
            "scalar FE, scalar filter, basis, protocol, and zero-mode interface imported",
        ),
        Gate(
            "section convention",
            "PASS"
            if convention.get("rule") == "s(gamma*z)=rho_E(gamma,z) s(z)"
            and convention.get("rank") == 3
            and "3x3 complex invertible" in convention.get("rho_shape", "")
            and "rho_E(gamma*delta,z)" in convention.get("cocycle", "")
            and "I_3" in convention.get("identity", "")
            and "^-1" in convention.get("inverse", "")
            else "FAIL",
            convention_text,
        ),
        Gate(
            "boundary constraint rule",
            "PASS"
            if contains_all(
                boundary_text,
                [
                    "source_node = gamma * target_node",
                    "u[source_node] - rho_E(gamma,target_node) u[target_node] = 0",
                    "three copies of the scalar FE gluing rule",
                    "ordered products of rho_E matrices",
                ],
            )
            else "FAIL",
            boundary_text,
        ),
        Gate(
            "generator face slots",
            "PASS"
            if set(face_labels)
            == {"x1_face", "x2_face", "y1_face", "y2_face", "t1_face", "t2_face"}
            and contains_all(
                face_text,
                [
                    "g1",
                    "(t1-y1) mod N",
                    "g2",
                    "(t1+y2) mod N",
                    "g3",
                    "g4",
                    "g5",
                    "g6",
                    "rho_E(g1,target)",
                    "rho_E(g6,target)",
                ],
            )
            else "FAIL",
            face_text,
        ),
        Gate(
            "rhoE required data",
            "PASS"
            if contains_all(
                required_text,
                [
                    "rho_E(g_j,z)",
                    "det rho_E",
                    "cocycle",
                    "Hermitian metric",
                    "Q,u,d,L,e,N,H",
                ],
            )
            else "FAIL",
            required_text,
        ),
        Gate(
            "rhoE template open",
            "OPEN"
            if rho_template.get("status") == "OPEN"
            and rho_template.get("rank") == 3
            and set(rho_template.get("generator_data", {}))
            == {"g1", "g2", "g3", "g4", "g5", "g6"}
            and all(value is None for value in rho_template.get("generator_data", {}).values())
            else "FAIL",
            str(rho_template),
        ),
        Gate(
            "trivial schema smoke test",
            "PASS"
            if smoke.get("rho_E(g_j,z)") == "I_3 for all generators and boundary targets"
            and all(bundle_counts[str(n)] == int(expected_counts[str(n)]) for n in sample_ns)
            and smoke.get("meaning") == "identity rho_E is only a schema smoke test, not a selected bundle"
            else "FAIL",
            str(bundle_counts),
        ),
        Gate(
            "what this closes",
            "PASS"
            if closes.get("bundle_boundary_constraint_formula") is True
            and closes.get("generator_face_rhoE_slots") is True
            and closes.get("rhoE_cocycle_requirements") is True
            and closes.get("rhoE_invertibility_requirement") is True
            and closes.get("trivial_schema_smoke_test") is True
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
                    "actual_selected_rho_E_values_or_functions",
                    "proof_rho_E_comes_from_selected_bundle_E",
                    "rho_E_cocycle_certificate_for_nontrivial_data",
                    "sector_projection_maps_Q_u_d_L_e_N_H",
                    "selected_D_E_action_on_bundle_FE_basis",
                    "selected_zero_mode_representatives",
                ],
            )
            else "FAIL",
            str(open_items),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_rho_E_constructed") is False
            and guardrails.get("uses_identity_rho_E_as_selected_bundle") is False
            and guardrails.get("claims_bundle_FE_space_selected") is False
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
            if verdict.get("closes_bundle_FE_gluing_contract") is True
            and verdict.get("closes_actual_bundle_transitions") is False
            and verdict.get("closes_selected_Galerkin_space") is False
            and "rho_E" in verdict.get("next_step", "")
            and "D_E" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records contract",
            "PASS"
            if contains_all(
                paper,
                [
                    "Iwasawa Bundle Finite-Element Gluing Contract",
                    "s(gamma*z) = rho_E(gamma,z) s(z)",
                    "rho_E(gamma*delta,z)",
                    "u[source_node] - rho_E(gamma,target_node) u[target_node] = 0",
                    "rho_E(g1,target)",
                    "certificates/iwasawa_bundle_rhoE_data.template.json",
                    "3*N^6",
                    "not as selected bundle data",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa bundle finite-element gluing contract audit")
    print("==================================================")
    print()
    for n in sample_ns:
        print(f"N={n}: identity-rho bundle dofs={bundle_counts[str(n)]}")
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
