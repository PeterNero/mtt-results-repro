from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79splittingconick3periodselectororexactgerbeexecution"
STATUS = "MTT_U6_Q79_FIXED_SECTOR_RECONCILED_PERIOD_SCHUR_AND_JOINT_GERBE_SYSTEM_CLOSED_NUMERIC_SOURCE_OPEN"
NEXT = "MTT_Selected_q79K3PeriodDomainXiHessianExecutionOrMarkedModelGerbeCertificate_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79SplittingConicK3PeriodSelectorOrExactGerbeExecution_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    certificate = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    scope = outputs["fixed_sector_scope"]
    rigor = outputs["Xi_rigor_audit"]
    schur = outputs["K3_period_Schur"]
    joint = outputs["joint_period_gerbe_contract"]
    open_source = outputs["open_source"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A108 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A108 next changed")
    require(all(candidate["checks"].values()), "one or more A108 checks failed")
    require(candidate["results"]["new_fitted_continuous_parameters"] == 0, "fitted parameter added")

    printed = scope["printed_configuration_space"]
    require(printed["J"] == "fixed complex structure", "printed J scope changed")
    require(printed["E"] == "fixed holomorphic bundle", "printed E scope changed")
    require(not printed["K3_period_or_complex_structure_varied"], "old theorem falsely varies periods")
    require(scope["theorem"]["proved"], "fixed-sector scope theorem missing")

    ou = rigor["OU_term"]
    require(not ou["if_lambda_is_varied"]["automatically_nonnegative"], "OU sign invented")
    require(ou["if_lambda_is_fixed"]["second_variation"] == 0, "fixed OU second variation")
    require(not ou["if_lambda_is_fixed"]["lifts_moduli"], "constant OU lifts moduli")
    gap = rigor["fiber_gap"]
    require("epsilon^2" in gap["fiber_Laplacian_scaling"], "fiber scaling missing")
    require(not gap["uniform_positive_gap_as_epsilon_to_zero_from_fiber"], "false uniform gap retained")
    hessian = rigor["Hessian_and_flow"]
    require(not hessian["principal_symbol_block_ellipticity_implies_full_positive_Hessian"], "principal symbol overpromoted")
    require(not hessian["typed_FP_variable_to_Strominger_field_map_present"], "missing field map invented")
    require(not hessian["current_fixed_field_Huu_accepted_as_unconditional_source_certificate"], "Huu overpromoted")
    require(rigor["theorem"]["proved"], "rigor theorem missing")

    geometry = schur["geometry"]
    require(geometry["complex_dimension"] == 18 and geometry["real_dimension"] == 36, "period dimensions")
    require(schur["extension"]["effective_Hessian"] == "H_eff=H_pp-H_pu H_uu^(-1) H_up", "Schur formula")
    guard = schur["dimension_guard"]
    require(guard["generic_real_Hessian_shape"] == [36, 36], "real Hessian shape")
    require(not guard["Hermitian_18x18_block_alone_sufficient"], "18x18 block overpromoted")
    payload = schur["required_source_payload"]
    require(payload["required_fields"] == 7, "period payload size")
    require(payload["accepted_actual_fields"] == 0, "actual period rows invented")
    unit = schur["exact_formula_unit_test"]
    require(unit["determinant_identity_exact"], "Schur determinant unit test")
    require(unit["det_full"] == unit["det_Huu_times_det_Heff"], "Schur determinant mismatch")
    require(unit["H_eff_positive"], "unit-test Schur complement not positive")
    require(schur["theorem"]["proved"], "conditional Schur theorem missing")

    route = joint["conditional_Z4_tau_i_route"]
    require(route["unknowns"]["total_real"] == 52, "joint unknown count")
    require(route["equations"]["total_real"] == 52, "joint equation count")
    jacobian = joint["real_Jacobian"]
    require(jacobian["shape"] == [52, 52], "joint Jacobian shape")
    require("|det_C(D_A F)|^2" in jacobian["determinant_factorization"], "realification determinant")
    require("complex-linear" in jacobian["determinant_factorization"], "complex-linearity guard")
    require("16x16 realification" in jacobian["non_complex_linear_fallback"], "full-real fallback")
    require(joint["strict_unselected_tau_route"]["unknowns_real"] == 54, "strict tau count")
    require(joint["theorem"]["proved"], "joint-system theorem missing")

    require(not any(open_source["acceptance"].values()), "open source falsely accepted")
    require(frontier["actual_period_derivative_source_fields"] == 0, "frontier rows invented")
    require(frontier["required_period_derivative_source_fields"] == 7, "frontier payload count")
    require(not frontier["fixed_sector_field_selection_unconditional"], "old selection overpromoted")
    require(frontier["fixed_sector_field_selection_conditional_on_C_Xi_fixed"], "conditional fixed-sector use lost")
    require(not frontier["actual_marked_K3_selected"], "marked K3 invented")
    require(not frontier["actual_exact_gerbe_zero"], "gerbe zero invented")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A108 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Fixed-sector theorem: exact scope",
        "Rigor corrections needed before using the field block",
        "Conditional K3-period Schur theorem",
        "H_eff=H_pp-H_pu H_uu^(-1) H_up",
        "52 equations in 52 real unknowns",
        "det J_joint=det(H_eff) |det_C(D_A F)|^2",
        "complex linearity for free",
        "No observed value and no fitted continuous parameter enters A108",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A108 q79 K3-period selector and joint-gerbe audit: PASS")
    print(f"status={STATUS}")
    print("old Strominger theorem reclassified: fixed-sector conditional correspondence only")
    print("period selector: exact 36-real Schur complement; 7 actual source fields remain")
    print("conditional tau=i joint system: 52 real equations in 52 unknowns")
    print("actual marked K3, exact gerbe zero, downstream HYM/Bianchi and U6 closure remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
