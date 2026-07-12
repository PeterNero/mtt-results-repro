"""Audit the smooth B_N Galerkin lift scaffold."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
CERT = REPO / "certificates" / "selected_routec_smooth_bn_galerkin_lift_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1.md"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def is_identity(matrix: list[list[float]]) -> bool:
    return all(abs(value - (1.0 if i == j else 0.0)) < 1e-12 for i, row in enumerate(matrix) for j, value in enumerate(row))


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    lift = data["B_N_lift"]
    gates = data["gates"]
    straight = data["superset_mode"]["straight_path"]
    fields = data["contract_comparison"]["fields_emitted_now"]
    missing = data["contract_comparison"]["still_missing_for_full_contract"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_ROUTEC_SMOOTH_BN_GALERKIN_LIFT_SCAFFOLD_BUILT_SELECTED_DE_STILL_OPEN",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert["status"]),
        check("basis dimension", lift["dimension"] == 27 and len(lift["basis"]) == 27, lift["dimension"]),
        check("quadrature emitted", len(lift["quadrature_rule"]["nodes"]) == 9 and fields["metric_volume_quadrature"] is True, lift["quadrature_rule"]),
        check("Gram positive", is_identity(lift["gram_matrix"]) and gates["Gram_matrix_positive_definite"] is True, gates),
        check("kernel dimension three", lift["zero_cluster"]["dimension"] == 3 and gates["kernel_dimension_is_three"] is True, lift["zero_cluster"]),
        check("positive gap", lift["complement_gap"] > 0 and gates["complement_gap_positive"] is True, lift["complement_gap"]),
        check("Riesz and Green emitted", fields["Riesz_projectors"] is True and fields["reduced_Green_operators"] is True, fields),
        check("extends beyond invariant", gates["basis_extends_beyond_left_invariant_forms"] is True, gates),
        check(
            "projective only",
            lift["bundle_equivariance"]["ordinary_bundle_equivariance"] is False
            and lift["bundle_equivariance"]["projective_equivariance_up_to_central_phase"] is True,
            lift["bundle_equivariance"],
        ),
        check(
            "not full BN payload",
            straight["full_BN_payload_gate"] is False
            and gates["selected_D_E_action_on_basis"] is False
            and missing["selected_D_E_action_on_basis"] is True,
            {"straight": straight, "missing": missing},
        ),
        check("no target fitting", data["target_fitting_used"] is False, data["target_fitting_used"]),
        check("closure not claimed", data["closure_claimed"] is False, data["what_remains_open"]),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_DE_Action_on_Smooth_BN_v1",
            data["next_required_artifact"],
        ),
        check("note records scaffold", "not a full straight proof" in note and "complement gap" in note, NOTE),
    ]
    print("\nMTT selected Route-C smooth BN Galerkin lift audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
