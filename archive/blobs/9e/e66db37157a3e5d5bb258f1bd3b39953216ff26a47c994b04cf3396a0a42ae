from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
TEXPAPERS = Path(os.environ.get("MTT_TEXPAPERS_ROOT", ROOT.parent))
REPOSITORIES = {
    "20 Mathematical Language Discovery Program": ROOT,
    "12 Quantum Gravity": Path(
        os.environ.get(
            "MTT_QG_ROOT",
            TEXPAPERS / "12 Quantum Gravity",
        )
    ),
}
PACKET = (
    ROOT / "q79_augmented_heterotic_total_complex_route_correction.packet.json"
)
NOTE = ROOT / "Q79_AUGMENTED_HETEROTIC_TOTAL_COMPLEX_ROUTE_CORRECTION_v1.md"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix(
    values: list[list[object]],
    extra_locals: dict[str, object] | None = None,
) -> sp.Matrix:
    local_symbols: dict[str, object] = {"I": sp.I}
    if extra_locals:
        local_symbols.update(extra_locals)
    return sp.Matrix(
        [
            [sp.sympify(value, locals=local_symbols) for value in row]
            for row in values
        ]
    )


def verify_inputs(packet: dict) -> dict[str, Path]:
    resolved: dict[str, Path] = {}
    for label, record in packet["inputs"].items():
        repository = record["repository"]
        require(repository in REPOSITORIES, f"unknown repository: {repository}")
        path = REPOSITORIES[repository] / Path(record["relative_path"])
        require(path.is_file(), f"missing input: {label}")
        require(sha256(path) == record["sha256"], f"stale input hash: {label}")
        resolved[label] = path
    return resolved


def main() -> None:
    packet = load(PACKET)
    require(
        packet["schema"]
        == "MTTQ79AugmentedHeteroticTotalComplexRouteCorrection.v1",
        "schema",
    )
    require(
        packet["status"].startswith(
            "Q79_HOLOMORPHIC_TWO_FORM_SURVIVAL"
        ),
        "status",
    )
    require(NOTE.is_file(), "theorem note")
    paths = verify_inputs(packet)

    prior_bridge = load(paths["prior_Maurer_Cartan_Hodge_bridge"])
    physical_seed = load(paths["physical_rank102_deformation_seed"])
    hs_target = load(paths["gauge_fixed_Hull_Strominger_target"])
    bht = load(paths["q79_BHT_holomorphic_elliptic_eligibility"])

    require(
        prior_bridge["physical_q79_compatibility_contract"]["closed"] == 4,
        "prior contract boundary",
    )
    require(
        prior_bridge["next_required_object"]["name"]
        == "q79HeteroticMaurerCartanToPhysicalDbarCompatibility.v1",
        "prior target",
    )
    require(
        physical_seed["physical_preprojection_deformation_complex"][
            "total_fiber_rank_complex"
        ]
        == 102,
        "rank-102 physical carrier",
    )
    require(
        not any(
            physical_seed["current_execution"][
                "minimal_source_rows"
            ].values()
        ),
        "physical endpoint boundary",
    )
    require(
        not any(hs_target["physical_execution_rows"].values()),
        "Hull-Strominger execution boundary",
    )
    require(
        bht["BHT_eligibility"]["complex_geometric_condition"]
        == (
            "the selected Fu-Yau complex structure makes X a holomorphic "
            "principal elliptic bundle"
        ),
        "q79 holomorphic fibration source",
    )

    # Independently reconstruct the pullback calculation.
    d_pi = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    omega_k3 = sp.Matrix([[0, 1], [-1, 0]])
    omega_pullback = d_pi.T * omega_k3 * d_pi
    require(d_pi.rank() == 2, "submersion witness")
    require(omega_k3.T == -omega_k3, "base two-form skew")
    require(omega_k3.rank() == 2, "base two-form nonzero")
    require(omega_pullback != sp.zeros(3), "pullback nonzero")
    require(omega_pullback.rank() == 2, "pullback rank")

    pullback = packet["holomorphic_two_form_survival_theorem"]
    finite_pullback = pullback["finite_pointwise_witness"]
    require(matrix(finite_pullback["d_pi"]) == d_pi, "serialized d pi")
    require(
        matrix(finite_pullback["Omega_K3"]) == omega_k3,
        "serialized K3 form",
    )
    require(
        matrix(finite_pullback["pullback_Omega"]) == omega_pullback,
        "serialized pullback",
    )
    require(
        finite_pullback["pullback_rank"] == 2,
        "serialized pullback rank",
    )
    require(
        "h^(2,0)(X_q79)>=1"
        in pullback["q79_specialization"]["conclusion"],
        "h20 conclusion",
    )
    require(
        "ell_1(0,b_K3)=0"
        in pullback["q79_specialization"][
            "explicit_linear_kernel_direction"
        ],
        "pulled-back b kernel direction",
    )
    require(
        pullback["tier"]
        == "CLOSED_EXACT_CONDITIONAL_ON_SELECTED_Q79_"
        "HOLOMORPHIC_ELLIPTIC_STRUCTURE",
        "pullback theorem tier",
    )

    # Independently reconstruct the symbolic triangular complex and Hodge
    # compression.
    d0, d1, a0, a1, c0, c1 = sp.symbols(
        "d0 d1 a0 a1 c0 c1",
        real=True,
    )
    half = sp.Rational(1, 2)
    l0 = sp.Matrix([[d0, half * a0], [0, c0]])
    l1 = sp.Matrix([[d1, -half * a1], [0, c1]])
    composition = sp.simplify(l1 * l0)
    delta_y = sp.simplify(l1.T * l1 + l0 * l0.T)
    delta_q = sp.simplify(d1**2 + d0**2)
    q_compression = sp.simplify(delta_y[0, 0])
    correction = sp.simplify(q_compression - delta_q)
    inclusion_q = sp.Matrix([[1], [0]])
    projection_q = sp.Matrix([[1, 0]])
    projection_b = sp.Matrix([[0, 1]])

    require(
        composition
        == sp.Matrix(
            [
                [d1 * d0, half * (d1 * a0 - a1 * c0)],
                [0, c1 * c0],
            ]
        ),
        "cochain block formula",
    )
    require(l0 * inclusion_q == inclusion_q * d0, "Q inclusion L0")
    require(l1 * inclusion_q == inclusion_q * d1, "Q inclusion L1")
    require(
        projection_b * l0 == c0 * projection_b,
        "B quotient L0",
    )
    require(
        projection_b * l1 == c1 * projection_b,
        "B quotient L1",
    )
    require(
        projection_q * l0 - d0 * projection_q
        == half * a0 * projection_b,
        "Q projection chain defect",
    )
    require(
        q_compression == delta_q + sp.Rational(1, 4) * a0**2,
        "Q Hodge compression",
    )
    require(
        correction == sp.Rational(1, 4) * a0**2,
        "positive correction",
    )

    symbolic = packet["symbolic_block_certificate"]
    symbols = {
        str(symbol): symbol
        for symbol in (d0, d1, a0, a1, c0, c1)
    }
    require(matrix(symbolic["L0"], symbols) == l0, "serialized L0")
    require(matrix(symbolic["L1"], symbols) == l1, "serialized L1")
    require(
        matrix(symbolic["L1_L0"], symbols) == composition,
        "serialized composition",
    )
    require(
        matrix(symbolic["Delta_Y_degree1"], symbols) == delta_y,
        "serialized Delta Y",
    )
    require(
        sp.sympify(symbolic["Delta_Q_degree1"], locals=symbols) == delta_q,
        "serialized Delta Q",
    )
    require(
        sp.sympify(symbolic["Q_compression"], locals=symbols)
        == q_compression,
        "serialized Q compression",
    )
    require(
        sp.sympify(symbolic["Q_correction"], locals=symbols) == correction,
        "serialized Q correction",
    )

    # Independently reconstruct the nontrivial exact witness.
    witness_values = {
        d0: 0,
        d1: 1,
        a0: 2,
        a1: 2,
        c0: 1,
        c1: 0,
    }
    l0_witness = l0.subs(witness_values)
    l1_witness = l1.subs(witness_values)
    delta_y_witness = (
        l1_witness.T * l1_witness
        + l0_witness * l0_witness.T
    )
    delta_q_witness = sp.Integer(1)
    q_compression_witness = (
        projection_q * delta_y_witness * inclusion_q
    )[0]
    require(l1_witness * l0_witness == sp.zeros(2), "witness cochain")
    require(
        l0_witness * inclusion_q == sp.zeros(2, 1),
        "witness Q inclusion degree zero",
    )
    require(
        l1_witness * inclusion_q == inclusion_q,
        "witness Q inclusion degree one",
    )
    require(
        projection_q * l0_witness != sp.zeros(1, 2),
        "witness Q projection not chain",
    )
    require(delta_q_witness == 1, "witness Delta Q")
    require(q_compression_witness == 2, "witness compression")
    require(
        q_compression_witness
        == delta_q_witness + sp.Rational(1, 4) * 2**2,
        "witness correction formula",
    )

    witness = packet["finite_nontrivial_total_complex_witness"]
    require(matrix(witness["L0"]) == l0_witness, "serialized witness L0")
    require(matrix(witness["L1"]) == l1_witness, "serialized witness L1")
    require(
        matrix(witness["L1_L0"]) == sp.zeros(2),
        "serialized witness cochain",
    )
    require(
        matrix(witness["Delta_Y_degree1"]) == delta_y_witness,
        "serialized witness Delta Y",
    )
    require(witness["Delta_Q_degree1"] == "1", "serialized witness Delta Q")
    require(witness["Q_compression"] == "2", "serialized witness compression")
    require(
        witness["positive_correction"] == "1",
        "serialized witness correction",
    )

    total_complex = packet["primary_heterotic_total_complex"]
    require(
        total_complex["short_exact_sequence"].startswith(
            "0 -> (Omega^(0,*)(Q_phys),Dbar_Q)"
        ),
        "short exact sequence",
    )
    require(
        total_complex["block_form"].startswith(
            "L_n=[[D_n,(1/2)(-1)^n A_n]"
        ),
        "graded block sign",
    )
    require(
        total_complex["graded_sign"]
        == (
            "the off-diagonal sign is + at degree zero and - at "
            "degree one"
        ),
        "graded sign declaration",
    )
    require(
        total_complex["cochain_conditions"][2]
        == "D_(n+1) A_n-A_(n+1) C_n=0",
        "graded mixed cochain identity",
    )
    require(
        total_complex["tier"]
        == "CLOSED_EXACT_STRUCTURAL_ROUTE_CORRECTION",
        "total complex tier",
    )
    hodge = packet["Hodge_compression_theorem"]
    require(
        hodge["correction"] == "(1/4)A_0 A_0*",
        "Hodge correction statement",
    )
    require(
        hodge["tier"] == "CLOSED_EXACT_UNIVERSAL_BLOCK_HODGE_THEOREM",
        "Hodge theorem tier",
    )

    superseded = packet["superseded_direct_target"]
    require(
        superseded["prior_name"]
        == "q79HeteroticMaurerCartanToPhysicalDbarCompatibility.v1",
        "retired direct target",
    )
    require(
        superseded["replacement"]
        == "q79AugmentedHeteroticTotalComplexPhysicalInstantiation.v1",
        "replacement target",
    )
    require(
        superseded["preserved_subclaim"]
        == "Dbar_Q is the invariant diagonal Q_phys subcomplex",
        "preserved rank-102 role",
    )

    readiness = packet["corrected_upper_action_readiness"]
    structural = readiness["structural_gates"]
    physical = readiness["physical_instantiation_gates"]
    require(readiness["structural_closed"] == 8, "structural closed count")
    require(readiness["structural_total"] == 8, "structural total count")
    require(
        all(row["closed"] for row in structural.values()),
        "structural gates",
    )
    require(readiness["physical_closed"] == 0, "physical closed count")
    require(readiness["physical_total"] == 6, "physical total count")
    require(
        not any(row["closed"] for row in physical.values()),
        "physical gates",
    )

    require(
        packet["next_required_object"]["name"]
        == "q79AugmentedHeteroticTotalComplexPhysicalInstantiation.v1",
        "next object",
    )
    require(packet["new_continuous_fit_parameters"] == 0, "fit parameters")
    require(all(packet["checks"].values()), "builder checks")
    require(
        not any(packet["guardrails"].values()),
        "guardrails must remain false",
    )

    note = NOTE.read_text(encoding="utf-8")
    for required_text in (
        "The previous result correctly proved",
        "h^(2,0)(X_q79) >= 1",
        "ell_1(0,b_K3)=0",
        "0 -> (Q_*,D) -> (Y_*,L) -> (B_*,C) -> 0",
        "Delta_Q,1 + 1/4 A_0A_0*",
        "q79AugmentedHeteroticTotalComplexPhysicalInstantiation.v1",
        "may become a four-dimensional scalar or axionic mode",
    ):
        require(required_text in note, f"note content: {required_text}")

    print("Q79_AUGMENTED_HETEROTIC_TOTAL_COMPLEX_ROUTE_CORRECTION_VERIFY_PASS")


if __name__ == "__main__":
    main()
