"""Audit the Iwasawa R_+ support row feeding C1."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT.parent / "certificates" / "c1_iwasawa_rplus_support_certificate.json"
C1_SOURCE_CERT = ROOT.parent / "certificates" / "c1_curvature_weight_source_audit_certificate.json"
C1_INSERTION_CERT = ROOT.parent / "certificates" / "c1_curvature_insertion_formula_certificate.json"
SEED_CERT = ROOT.parent / "certificates" / "iwasawa_rank_one_yukawa_seed_certificate.json"
FLUX_SOURCE = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Flux_Compactifications_in_Heterotic_String_Theory_v3.md"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    c1_source_cert = load_json(C1_SOURCE_CERT)
    c1_insertion_cert = load_json(C1_INSERTION_CERT)
    seed_cert = load_json(SEED_CERT)
    flux = read(FLUX_SOURCE)
    paper = read(ROOT / "C1_Iwasawa_Rplus_Support_Reduction_for_Rank_One_Lift_v1.md")

    rplus = cert.get("rplus_support", {})
    bianchi = cert.get("bianchi_support", {})
    consequence = cert.get("consequence_for_C1", {})
    closed = cert.get("closed", {})
    open_fields = cert.get("open", {})

    has_invariant_basis = contains_all(
        flux,
        ["alpha_1:=a\\wedge b", "alpha_2:=a\\wedge c", "alpha_3:=b\\wedge c"],
    )
    has_alpha1_rplus = contains_all(
        flux,
        [
            "\\mathrm{Tr}_{\\mathrm{grav}} R_+^2",
            "\\tilde v_1(R,r_3)\\,\\alpha_1",
            "no* components along $\\alpha_2$ or $\\alpha_3$",
        ],
    )
    has_v1_coefficient = contains_all(
        flux,
        ["\\tilde v_1(R,r_3)", "8\\,\\frac{r_3^2}{r_1^2 r_2^2}"],
    )
    has_bianchi_component = contains_all(
        flux,
        ["v_2=v_3=0", "u_2=v_2=0", "u_3=v_3=0", "u_1-v_1 = \\frac{16}{\\alpha'}\\,r_3^2"],
    )
    has_r3_solution = contains_all(
        flux,
        ["r_3^2 = \\frac{8(2\\pi)^2}", "\\tfrac{16}{\\alpha'}+\\tfrac{8}{R^4}"],
    )
    has_coherent_projection = contains_all(
        flux,
        ["Invariant truncation as a coherent projection", "\\Pi_{\\mathrm{coh}}", "spectral projector"],
    )
    has_yukawa_seed = contains_all(
        flux,
        ["three orthonormal harmonic representatives", "\\lambda_{123}", "rank one"],
    )

    gates = [
        Gate(
            "certificate status",
            "SUPPORT-CLOSED"
            if cert.get("status") == "C1_IWASAWA_RPLUS_INVARIANT_SUPPORT_CLOSED_OVERLAPS_OPEN"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "C1 source input",
            "ADMISSIBLE-OPEN"
            if c1_source_cert.get("status") == "C1_CURVATURE_WEIGHT_SOURCE_ADMISSIBLE_VALUES_OPEN"
            else "FAIL",
            str(c1_source_cert.get("status")),
        ),
        Gate(
            "C1 insertion input",
            "FORMULATED-OPEN"
            if c1_insertion_cert.get("status") == "C1_CURVATURE_INSERTION_FORMULATED_VALUES_OPEN"
            else "FAIL",
            str(c1_insertion_cert.get("status")),
        ),
        Gate(
            "Iwasawa seed input",
            "PASS" if seed_cert.get("tree_level_seed", {}).get("rank") == 1 else "FAIL",
            "rank-one Iwasawa seed available",
        ),
        Gate(
            "invariant basis",
            "PASS" if has_invariant_basis else "FAIL",
            "alpha_1, alpha_2, alpha_3 basis present",
        ),
        Gate(
            "Rplus alpha_1 support",
            "PASS" if has_alpha1_rplus and rplus.get("alpha_2_component") == 0 and rplus.get("alpha_3_component") == 0 else "FAIL",
            str(rplus.get("formula")),
        ),
        Gate(
            "Rplus coefficient",
            "PASS" if has_v1_coefficient and "8 r3^2/(r1^2 r2^2)" in rplus.get("coefficient", "") else "FAIL",
            str(rplus.get("coefficient")),
        ),
        Gate(
            "Bianchi support",
            "PASS" if has_bianchi_component and "u1 - v1" in bianchi.get("component_equations", "") else "FAIL",
            str(bianchi.get("component_equations")),
        ),
        Gate(
            "equal-radius r3 solution",
            "PASS" if has_r3_solution and "16/alpha_prime" in rplus.get("equal_radius_specialization", {}).get("fixed_r3_squared", "") else "FAIL",
            str(rplus.get("equal_radius_specialization", {}).get("fixed_r3_squared")),
        ),
        Gate(
            "coherent projection",
            "PASS" if has_coherent_projection and closed.get("coherent_projection_context") is True else "FAIL",
            "invariant truncation is a coherent spectral projection",
        ),
        Gate(
            "Yukawa seed same branch",
            "PASS" if has_yukawa_seed else "FAIL",
            "rank-one Yukawa seed is on the same Iwasawa source",
        ),
        Gate(
            "curvature driver count",
            "PASS"
            if consequence.get("curvature_driver_count_in_invariant_branch") == 1
            and closed.get("C1_independent_curvature_knob_count_reduced") is True
            else "FAIL",
            "C1 invariant curvature driver is one alpha_1 row",
        ),
        Gate(
            "no rank overclaim",
            "OPEN"
            if open_fields.get("rank_lift_nonzero_test") is True
            and "OPEN" in consequence.get("rank_lift_status", "")
            else "FAIL",
            "rank lift still depends on dotD_a and zero-mode contractions",
        ),
        Gate(
            "paper records theorem",
            "PASS" if "Iwasawa Rplus Support Theorem" in paper else "FAIL",
            "support theorem is written",
        ),
    ]

    print("C1 Iwasawa Rplus support audit")
    print("==============================")
    print()
    print(f"rplus_formula={rplus.get('formula')}")
    print(f"rplus_coefficient={rplus.get('coefficient')}")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
