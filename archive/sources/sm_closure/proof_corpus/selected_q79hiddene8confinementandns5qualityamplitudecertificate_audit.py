from __future__ import annotations

import hashlib
import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79hiddene8confinementandns5qualityamplitudecertificate"
STATUS = (
    "MTT_U6_SECOND_E8_TYPING_AND_TWO_FUYAU_CURVATURE_HIDDEN_EXIT_NO_GO_CLOSED_"
    "SELECTED_HIDDEN_BUNDLE_AND_AMPLITUDES_OPEN"
)
NEXT = "MTT_Selected_q79HiddenBundleExistenceBianchiAllocationAndSpectrumExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79HiddenE8ConfinementAndNS5QualityAmplitudeCertificate_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def roots() -> set[tuple[Fraction, ...]]:
    result: set[tuple[Fraction, ...]] = set()
    for i, j in itertools.combinations(range(8), 2):
        for sign_i in (-1, 1):
            for sign_j in (-1, 1):
                root = [Fraction(0) for _ in range(8)]
                root[i] = Fraction(sign_i)
                root[j] = Fraction(sign_j)
                result.add(tuple(root))
    for signs in itertools.product((-1, 1), repeat=8):
        if sum(sign < 0 for sign in signs) % 2 == 0:
            result.add(tuple(Fraction(sign, 2) for sign in signs))
    return result


def dot(left: list[int] | tuple[Fraction, ...], right: list[int] | tuple[Fraction, ...]) -> Fraction:
    return sum(Fraction(x) * Fraction(y) for x, y in zip(left, right))


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    typing = outputs["typing"]
    decision = outputs["confinement_decision"]
    no_go = outputs["two_curvature_no_go"]
    ns5 = outputs["NS5_A98_envelope"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == cert["status"] == STATUS, "A101 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A101 next changed")
    require(all(candidate["checks"].values()), "one or more A101 checks failed")
    require(candidate["results"]["new_continuous_parameters"] == 0, "A101 added a continuous parameter")

    require(typing["theorem"]["proved"], "two-E8 type repair missing")
    require(typing["as_written_scope"]["gauge_connections"] == 1, "source audit changed")
    require(not typing["as_written_scope"]["selects_an_E8xE8_hidden_bundle"], "one-bundle source overpromoted")
    require(typing["theorem"]["does_not_select_P2"], "P2 was silently selected")

    require(decision["theorem"]["proved"], "confinement decision theorem missing")
    require(not decision["selected_q79_input_audit"]["hidden_confinement_decidable_now"], "hidden confinement invented")
    require(decision["candidate_exits"]["full_holonomy_E8"]["first_nonnegative_integer_k2"] == 9, "E8 index threshold")
    require(not decision["candidate_exits"]["full_holonomy_E8"]["selected_now"], "index promoted to selection")

    rows = no_go["finite_Weyl_chamber_certificate"]["dominant_rows_with_norm_below_40"]
    require(len(rows) == no_go["finite_Weyl_chamber_certificate"]["row_count"] == 40, "dominant enumeration incomplete")
    require(min(Fraction(row["A2_characteristic_lower"]) for row in rows) == 30, "global lower bound changed")
    require(no_go["finite_Weyl_chamber_certificate"]["exact_minimum"] == 30, "minimum not certified")

    witness = no_go["saturating_witness"]
    q1 = witness["q1_E8_coordinates"]
    q2 = witness["q2_E8_coordinates"]
    all_roots = roots()
    require(len(all_roots) == 240, "independent E8 root enumeration failed")
    require(not [root for root in all_roots if dot(root, q1) == 0 and dot(root, q2) == 0], "witness has a common orthogonal root")
    independent_gram = [[int(dot(q1, q1)), int(dot(q1, q2))], [int(dot(q2, q1)), int(dot(q2, q2))]]
    require(independent_gram == witness["Gram"] == [[20, -10], [-10, 20]], "witness Gram changed")
    require(independent_gram[0][0] + independent_gram[1][1] - abs(independent_gram[0][1]) == 30, "witness does not saturate")
    require(no_go["Minkowski_reduction"]["K3_source_free_budget"] == 24, "K3 budget changed")
    require(no_go["theorem"]["proved"], "two-curvature no-go missing")

    require(ns5["prefactor_refinement"]["A100_identification"] == "A_NS5=kappa/(16*pi*alpha_GUT)", "NS5 prefactor not identified")
    first = ns5["benchmark_profiles_not_MTT_predictions"][0]
    alpha_inverse = first["alpha_GUT_inverse"]
    alpha = 1.0 / alpha_inverse
    ceiling = ns5["A98_single_harmonic_envelope"]["benchmark_derivative_ceiling_GeV4"]
    mass = first["M_GUT_equals_Ms_GeV"]
    expected = 16.0 * math.pi * alpha * ceiling * math.exp(2.0 * math.pi * alpha_inverse) / mass**3
    require(math.isclose(first["kappa_times_m3_2_superpotential_ceiling_GeV"], expected, rel_tol=1e-14), "NS5 profile arithmetic")
    require(not ns5["selected_A98_pass"], "benchmark profile promoted to selected pass")

    require(frontier["selected_hidden_payload"] == {
        "fields": ["P2", "rho2", "characteristic_class", "Wilson_lines", "branching", "cohomology", "thresholds", "f_hidden"],
        "filled": 0,
        "required": 8,
    }, "hidden payload readiness inflated")
    require(frontier["selected_NS5_numerical_payload"]["filled"] == 0, "NS5 values invented")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")
    require(frontier["next_required_artifact"] == NEXT, "frontier next changed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A101 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A101 authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Two-E8 source typing repair",
        "Exact confinement decision theorem",
        "Two-Fu-Yau-curvature no-go",
        "F(q1,q2)=q1^2+q2^2-|q1.q2|",
        "A_NS5=kappa/(16*pi*alpha_GUT)",
        NEXT,
    ]:
        require(phrase in note, f"A101 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("q79 hidden E8 confinement and NS5 quality amplitude audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
