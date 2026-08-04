from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate"
STATUS = "MTT_U6_Q79_EXPLICIT_SMOOTH_MARKED_SPLITTING_CONIC_K3_CLOSED_PERIOD_GERBE_AND_SELECTION_OPEN"
NEXT = "MTT_Selected_q79ExplicitModelRelativeDeligneGerbeZeroOrNoGoExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79K3PeriodDomainXiHessianExecutionOrMarkedModelGerbeCertificate_v1.md"


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
    model = outputs["explicit_model"]
    smooth = outputs["smoothness_certificate"]
    lattice = outputs["marked_lattice"]
    period = outputs["relative_period_input"]
    scope = outputs["selection_scope_guard"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A109 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A109 next changed")
    require(all(candidate["checks"].values()), "one or more A109 checks failed")
    require(sp.__version__ == "1.14.0", "unlocked SymPy version")

    require(model["exact_identity"]["residual"] == "0", "splitting identity")
    require(model["construction_provenance"]["accepted_attempt"] == 1, "model provenance")
    require(not model["construction_provenance"]["observed_physics_values_used"], "observed value used")
    require(not model["construction_provenance"]["MTT_selection_used"], "selection invented")

    for test_name in [
        "conic_Q2_smooth",
        "branch_sextic_F6_smooth",
        "Q2_G3_intersection_transverse",
        "H4_nonzero_on_Q2_cap_G3",
    ]:
        test = smooth[test_name]
        require(test["all_projective_charts_unit"], f"{test_name} failed")
        require(set(test["charts"]) == {"x", "y", "z"}, f"{test_name} chart cover")
        for chart in test["charts"].values():
            require(chart["Groebner_basis"] == ["1"], f"{test_name} nonunit basis")
            require(chart["unit_ideal"], f"{test_name} nonunit chart")
    require(smooth["gcd_Q2_G3"] == "1", "Q2/G3 common component")
    require(smooth["Euler_identity"]["residual"] == "0", "Euler identity")
    require(all(smooth["consequences"].values()), "smoothness consequence missing")
    require(smooth["theorem"]["proved"], "smoothness theorem missing")

    intersections = lattice["intersection_derivation"]
    require(intersections["Gram_H_delta"] == [[2, 0], [0, -4]], "wrong marked lattice")
    require(intersections["R_plus_dot_R_minus"] == 6, "wrong root intersection")
    require(lattice["primitivity"]["delta_primitive"], "delta not primitive")
    require(lattice["primitivity"]["span_H_delta_primitive"], "marked span not primitive")
    require(lattice["primitivity"]["nonzero_isotropic_classes"] == 0, "even overlattice remains")
    isotropic = [
        entry["class"]
        for entry in lattice["primitivity"]["discriminant_form_classes"]
        if entry["isotropic"]
    ]
    require(isotropic == [[0, 0]], "discriminant-form enumeration")
    require(lattice["theorem"]["proved"], "lattice theorem missing")

    require(period["strict_direct_fields_filled"] == 4, "direct route count")
    require(period["strict_direct_fields_required"] == 8, "direct route denominator")
    require(period["conditional_bridge_fields_filled"] == 5, "conditional route count")
    require(not period["conditional_Z4_bridge"]["accepted_as_strict_source"], "tau bridge overpromoted")
    require(all(value is None for value in period["open"].values()), "open period value invented")

    accounting = scope["parameter_accounting"]
    require(accounting["observed_or_fitted_physics_parameters_added"] == 0, "fit added")
    require(accounting["strict_MTT_source_moduli_removed"] == 0, "source moduli falsely removed")
    require("18-complex-dimensional" in accounting["unsourced_model_choice"], "model-choice guard")
    require(scope["theorem"]["proved"], "selection guard theorem missing")

    require(frontier["strict_direct_model_fields_filled"] == 4, "frontier direct count")
    require(frontier["actual_period_gradient_or_Hessian_rows"] == 0, "period rows invented")
    require(not frontier["actual_exact_gerbe_zero"], "gerbe zero invented")
    require(not frontier["actual_MTT_marked_K3_selection"], "MTT selection invented")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A109 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Constructive result",
        "Exact smoothness certificate",
        "Gram(H,delta)=diag(2,-4)",
        "no nonzero isotropic class",
        "A109 fills four exactly",
        "Selection guard",
        "removes zero strict source moduli",
        "No observed physics value and no fitted physics parameter was used",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A109 explicit marked splitting-conic K3 audit: PASS")
    print(f"status={STATUS}")
    print("exact smoothness: four projective ideal tests x three charts all reduce to [1]")
    print("marked lattice: Gram(H,delta)=diag(2,-4), primitive span (no nonzero isotropic class)")
    print("direct A106 route: 4/8 strict fields filled; 5/8 only under open Z4 bridge")
    print("period rows, exact gerbe zero, MTT selection, HYM/Bianchi and U6 closure remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
