from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution.candidate.json"
)
CERTIFICATE = (
    ROOT
    / "certificates"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution.certificate.json"
)
OUT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
TRANSGRESSION = OUT / "normalized_Deligne_Leray_transgression.packet.json"
BETA_VECTOR = OUT / "selected_beta_period_vector.floating.packet.json"
BRANCH_OPEN = OUT / "integral_branch_and_gerbe_decision.open.json"
FRONTIER = OUT / "U6_frontier_after_A121.packet.json"
A110_CECH = (
    ROOT
    / "candidate_data"
    / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
    / "normalized_Poincare_gerbe_Cech_formula.packet.json"
)
A119_PERIODS = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2handleandlerayperiodexecution"
    / "full_integral_basis_period_table.packet.json"
)
A120_PRODUCTION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution"
    / "normal_function_handles.production.packet.json"
)
A120_TIGHT = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2normalfunctionbetaandintegralbranchexecution"
    / "normal_function_handles.tight.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def handle(packet: dict, name: str) -> dict:
    rows = [row for row in packet["handles"] if row["name"] == name]
    require(len(rows) == 1, f"unique {name} handle")
    return rows[0]


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    transgression = load(TRANSGRESSION)
    beta = load(BETA_VECTOR)
    branch = load(BRANCH_OPEN)
    frontier = load(FRONTIER)
    cech = load(A110_CECH)
    periods = load(A119_PERIODS)
    production = load(A120_PRODUCTION)
    tight = load(A120_TIGHT)

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    require(
        cech["triple_overlap_scalar"]["formula"]
        == "alpha_ijk(e_hat)=chi_ehat(n_ijk,0)",
        "A110 source marking",
    )
    require(
        transgression["source_marking"]["selected_DD_generator"]
        == "DD(alpha)=delta cup u_A",
        "selected DD generator",
    )
    require(
        transgression["torus_transgression"]["selected_representative"]
        == "z_r=R_B,r",
        "B-handle transgression",
    )
    require(
        transgression["theorem"]["proved"],
        "transgression theorem",
    )

    require(periods["period_matrix_shape"] == [8, 92], "period matrix shape")
    require(
        beta["form_order"] == periods["form_order"],
        "period form order",
    )
    production_b = handle(production, "B")
    tight_b = handle(tight, "B")
    z_production = np.asarray(
        [parse_complex(value) for value in beta["production_values"]]
    )
    z_tight = np.asarray(
        [parse_complex(value) for value in beta["tight_values"]]
    )
    expected_production = np.asarray(
        [parse_complex(value) for value in production_b["relative_periods"]]
    )
    expected_tight = np.asarray(
        [parse_complex(value) for value in tight_b["relative_periods"]]
    )
    require(np.array_equal(z_production, expected_production), "production z")
    require(np.array_equal(z_tight, expected_tight), "tight z")
    maximum_difference = float(np.max(np.abs(z_production - z_tight)))
    require(maximum_difference < 6.0e-10, "floating convergence")
    require(
        abs(
            maximum_difference
            - float(beta["maximum_absolute_difference"])
        )
        < 1.0e-20,
        "reported convergence",
    )

    require(not branch["open"]["exact_membership_proved"], "membership invented")
    require(
        not branch["open"]["exact_nonmembership_proved"],
        "nonmembership invented",
    )
    require(branch["guard"]["nearest_lattice_not_accepted"], "lattice guard")
    require(
        frontier["floating_beta_C_period_rows_emitted"] == 8,
        "floating beta row count",
    )
    require(
        frontier["interval_beta_C_period_rows_emitted"] == 0,
        "interval rows invented",
    )
    require(
        not frontier["integral_period_branch_selected"],
        "integral branch invented",
    )
    require(
        not frontier["beta_C_zero_or_nonzero_decided"],
        "beta decision invented",
    )
    require(
        certificate["normalized_Deligne_transgression_functional_closed"],
        "certificate functional",
    )
    require(not certificate["beta_C_decided"], "certificate beta overclaim")
    require(not candidate["checks"]["target_fitting_used"], "target fitting")

    print("q79 A121 Deligne beta-period transgression audit: PASS")
    print("closed: exact quotient functional beta_C=[R_B]")
    print(f"floating z_8 max production-tight difference: {maximum_difference:.3e}")
    print("open: exact Z^92 membership, beta_C zero/no-go, PGL3 Jacobian")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
