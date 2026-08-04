from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
STATUS = "MTT_U6_Q79_EXPLICIT_SMOOTH_SPECTRAL_SURFACE_AND_TORSOR_POINCARE_CECH_FORMULA_CLOSED_BETA_PERIOD_OPEN"
NEXT = "MTT_Selected_q79ExplicitSpectralCechBetaPeriodEvaluation_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79ExplicitModelRelativeDeligneGerbeZeroOrNoGoExecution_v1.md"


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
    spectral = outputs["spectral_surface"]
    smooth = outputs["spectral_smoothness"]
    torsor = outputs["torsor_transitions"]
    gerbe = outputs["Poincare_gerbe_formula"]
    beta = outputs["beta_period_open"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A110 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A110 next changed")
    require(all(candidate["checks"].values()), "one or more A110 checks failed")
    require(sp.__version__ == "1.14.0", "unlocked SymPy version")

    elliptic = spectral["elliptic_curve"]
    require(elliptic["discriminant"] == 64, "elliptic discriminant")
    require(elliptic["j_invariant"] == 1728, "elliptic j")
    require(elliptic["analytic_modulus_up_to_SL2Z"] == "tau=i", "elliptic modulus")
    require(spectral["alignment"]["A_PGL3_trial"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "trial alignment")
    require(not spectral["alignment"]["accepted_as_MTT_selected_alignment"], "trial A selected")
    require(not spectral["alignment"]["accepted_as_gerbe_zero_alignment"], "trial A zero invented")
    require(spectral["smooth"], "spectral surface not smooth")

    require(smooth["elliptic_curve_smoothness"]["all_projective_charts_unit"], "elliptic singular")
    mutual = smooth["mutual_Gauss_system"]
    require(mutual["all_nine_product_charts_unit"], "mutual Gauss system nonempty")
    require(len(mutual["charts"]) == 9, "product chart count")
    for chart in mutual["charts"].values():
        require(chart["Groebner_basis"] == ["1"] and chart["unit_ideal"], "nonunit product chart")
    require(smooth["theorem"]["proved"], "spectral smoothness theorem missing")

    transitions = torsor["O_delta_transitions"]
    require(torsor["R_plus_cover"]["surface_relation_residual"] == "0", "split ratio residual")
    require(torsor["refined_cover"]["patch_count"] == 9, "torsor patch count")
    require(transitions["ordered_nonidentity_transition_count"] == 72, "transition count")
    require(transitions["inverse_checks_exact"] == 72, "inverse checks")
    require(transitions["triple_cocycle_checks_exact"] == 729, "cocycle checks")
    require(transitions["all_checks_pass"], "transition table failed")
    require(torsor["elliptic_torsor"]["Chern_pair"] == ["delta", 0], "torsor Chern pair")
    require(not torsor["elliptic_torsor"]["explicit_good_cover_log_branch_values_filled"], "log branches invented")
    require(torsor["theorem"]["proved"], "torsor theorem missing")

    filled = gerbe["filled_A104_formula_fields"]
    require(filled["FuYau_torsor_transition_functions"], "torsor formula missing")
    require(filled["relative_Poincare_discrepancy_line_bundles_on_double_overlaps"], "discrepancy formula missing")
    require(filled["restricted_scalar_gerbe_cocycle_alpha_ijk_formula"], "alpha formula missing")
    require(not filled["restricted_scalar_gerbe_cocycle_alpha_ijk_values_on_good_cover"], "alpha values invented")
    require(gerbe["triple_overlap_scalar"]["zero_section_normalization"] == "alpha_ijk(0)=1", "gerbe normalization")
    require(gerbe["Dixmier_Douady_class"]["restriction_to_C_integrally_zero"], "DD restriction lost")
    require(gerbe["theorem"]["proved"], "gerbe formula theorem missing")

    require(not any(beta["acceptance"].values()), "beta decision invented")
    require(all(value is None or (isinstance(value, list) and all(item is None for item in value)) for value in beta["open"].values()), "open beta field filled")
    require(frontier["A104_formula_fields_promoted"] == 3, "formula field count")
    require(frontier["A104_good_cover_numeric_or_exact_value_fields_promoted"] == 0, "value fields invented")
    require(frontier["beta_C_period_rows_emitted"] == 0, "beta rows invented")
    require(not frontier["tau_i_strictly_selected"], "tau selected")
    require(not frontier["trial_PGL3_identity_proved_gerbe_zero"], "identity zero invented")
    require(frontier["strict_MTT_source_moduli_removed"] == 0, "source moduli removed")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A110 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "New exact spectral carrier",
        "Spectral-surface smoothness theorem",
        "all nine product",
        "all 72 ordered inverse checks and all 729 triple",
        "alpha_ijk(e_hat)=chi_ehat(n_ijk,0)",
        "Remaining analytic calculation",
        "zero strict source moduli are removed",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A110 explicit spectral Cech/Poincare packet audit: PASS")
    print(f"status={STATUS}")
    print("spectral surface: exact mutual-Gauss ideal empty on all 9 product charts")
    print("O(delta): 9 patches, 72 inverse checks, 729 triple cocycle checks")
    print("Fu-Yau torsor and normalized Poincare alpha formula closed")
    print("good-cover log values, eight beta periods, exact zero/no-go, selection and U6 remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
