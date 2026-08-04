from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2lefschetzperiodreduction"
STATUS = (
    "MTT_U6_Q79_EXPLICIT_GENUS2_LEFSCHETZ_FIBRATION_90_NODES_AND_"
    "PRYM_NORMAL_FUNCTION_INPUT_CLOSED_CERTIFIED_PERIOD_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoMonodromyBetaPeriodExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoLefschetzPeriodReduction_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expression_from_terms(terms: list[dict], variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    expression = 0
    for term in terms:
        monomial = 1
        for variable, power in zip(variables, term["powers_xyz"]):
            monomial *= variable**power
        expression += term["coefficient"] * monomial
    return sp.expand(expression)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    certificate = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    fibration = outputs["genus_two_fibration"]
    discriminant = outputs["nodal_discriminant"]
    prym = outputs["Prym_residue_normal_function"]
    period = outputs["period_execution_open"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A111 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A111 next changed")
    require(all(candidate["checks"].values()), "one or more A111 checks failed")
    require(sp.__version__ == "1.14.0", "unlocked SymPy version")

    model_path = (
        ROOT
        / "candidate_data"
        / "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate"
        / "explicit_splitting_conic_K3_model.packet.json"
    )
    model = load(model_path)
    x, y, z, t, a, b = sp.symbols("x y z t a b")
    tables = model["coefficient_tables"]
    f6 = expression_from_terms(tables["F6"], (x, y, z))
    g3 = expression_from_terms(tables["G3"], (x, y, z))
    q2 = expression_from_terms(tables["Q2"], (x, y, z))
    h4 = expression_from_terms(tables["H4"], (x, y, z))
    substitution = {x: 1, y: t, z: -a - b * t}
    f_ab = sp.expand(f6.subs(substitution))
    g_ab = sp.expand(g3.subs(substitution))
    q_ab = sp.expand(q2.subs(substitution))
    h_ab = sp.expand(h4.subs(substitution))
    require(sp.expand(f_ab - g_ab**2 - q_ab * h_ab) == 0, "fiber splitting identity")
    require(sp.degree(f_ab, t) == 6, "fiber sextic degree")
    require(q_ab == -a - b * t - t**2, "fiber splitting quadratic")
    require(fibration["fiber_chart"]["genus"] == 2, "fiber genus")
    require(fibration["theorem"]["proved"], "fibration theorem missing")

    raw_disc = sp.discriminant(f_ab, t)
    reduced_disc = sp.rem(
        sp.Poly(raw_disc, b, domain=sp.QQ[a]),
        sp.Poly(b**2 - a**3 + a, b, domain=sp.QQ[a]),
    ).as_expr()
    disc_poly = sp.Poly(reduced_disc, b, domain=sp.QQ[a])
    p45 = sp.expand(disc_poly.coeff_monomial(1))
    q43 = sp.expand(disc_poly.coeff_monomial(b))
    norm90 = sp.expand(p45**2 - (a**3 - a) * q43**2)
    n_poly = sp.Poly(norm90, a, domain=sp.QQ)

    require(sp.Poly(p45, a).degree() == 45, "P degree")
    require(sp.Poly(q43, a).degree() == 43, "Q degree")
    require(n_poly.degree() == 90, "norm degree")
    require(sp.gcd(n_poly, sp.Poly(sp.diff(norm90, a), a)).as_expr() == 1, "norm not square-free")
    require(sp.gcd(sp.Poly(p45, a), sp.Poly(q43, a)).as_expr() == 1, "P/Q not coprime")
    norm_packet = discriminant["norm_certificate"]
    require(norm_packet["coefficients_descending"] == [int(c) for c in n_poly.all_coeffs()], "norm coefficient mismatch")
    require(
        norm_packet["sha256_of_expanded_expression"]
        == hashlib.sha256(str(norm90).encode("ascii")).hexdigest(),
        "norm expression hash mismatch",
    )
    require(discriminant["infinity_check"]["discriminant_zero_at_O"] is False, "infinity zero")
    consequences = discriminant["consequences"]
    require(consequences["distinct_discriminant_points_on_E"] == 90, "critical count")
    require(consequences["singular_fiber_type"] == "one ordinary node at each discriminant point", "node type")
    require(consequences["Euler_crosscheck_exact"], "Euler mismatch")
    require(consequences["b2_from_Euler"] == 92, "b2 mismatch")
    require(discriminant["theorem"]["proved"], "discriminant theorem missing")

    residues = prym["residue_forms"]
    require(residues["trace_free_form_count"] == 8, "residue count")
    require(residues["exact_linear_rank"] == 8, "residue rank")
    require(len(residues["numerators_L_M"]) == 8, "residue numerator table")
    require(prym["delta_fiber_divisor"]["relative_degree"] == 0, "delta degree")
    require("P_1+P_2" in prym["delta_fiber_divisor"]["degree_zero_divisor"], "delta divisor missing")
    require(len(prym["Poincare_transgression"]["Cech_to_Leray_chain"]) == 5, "Cech-Leray chain")
    require("H^2(O^*)=0" in prym["Poincare_transgression"]["fiberwise_vanishing_reason"], "fiberwise gerbe argument")
    require(not prym["Poincare_transgression"]["beta_C_zero_decided"], "beta decision invented")
    require(prym["theorem"]["proved"], "normal-function theorem missing")

    require(period["closed_input"]["fiber_H1_rank"] == 4, "fiber H1 rank")
    require(period["closed_input"]["surface_H2_rank"] == 92, "surface H2 rank")
    require(len(period["execution_steps"]) == 8, "execution step count")
    require(not any(period["acceptance"].values()), "period decision invented")
    require(frontier["old_good_cover_as_only_route_retired"], "old route not retired")
    require(frontier["beta_C_period_rows_emitted"] == 0, "beta rows invented")
    require(not frontier["actual_exact_gerbe_zero"], "gerbe zero invented")
    require(not frontier["trial_tau_i_and_identity_alignment_selected"], "trial selected")
    require(frontier["strict_MTT_source_moduli_removed"] == 0, "source moduli removed")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A111 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "A new exact projection",
        "Exact discriminant theorem",
        "gcd(N90,N90')=1",
        "there are exactly 90",
        "The eight forms are now explicit",
        "D_delta(e)=P_1+P_2-P_infinity_plus-P_infinity_minus",
        "Remaining certified execution",
        "source moduli are removed",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A111 q79 genus-two Lefschetz period reduction audit: PASS")
    print(f"status={STATUS}")
    print("genus-two family: exact splitting sextic over E_i")
    print("discriminant: 90 simple points, 90 nodal fibers, b2(C)=92")
    print("Prym input: 8 explicit residue forms plus algebraic delta normal function")
    print("certified monodromy, beta periods, integral branch, selection and U6 remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
