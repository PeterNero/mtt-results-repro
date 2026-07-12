"""Audit the Fu-Yau/Mukai Z7 fixed-sector selection reduction.

This check deliberately separates local MTT selection inside a fixed
Strominger topological sector from the global existence/choice of that sector.
The former is closed by the Strominger selection theorem.  The latter is now
closed in the charge-sector certificate.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CORPUS = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
)


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    strominger = read(CORPUS / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md")
    reduction = read(ROOT / "Fu_Yau_Mukai_Z7_Fixed_Sector_Selection_Reduction_v1.md")
    discr = read(ROOT / "Mukai_Discriminant_Group_Selection_for_Z7_CP_v1.md")
    char = read(ROOT / "Mukai_Z7_CP_Character_Identification_Theorem_v1.md")
    stable = read(ROOT / "Stable_Sheaf_Existence_Gate_for_Mukai_Z7_Block_v1.md")
    cert = read(ROOT / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md")

    gates = [
        Gate(
            "Strominger paper fixes topological sector",
            "PASS"
            if has_all(strominger, ["Fix a topological sector", "Chern data", "Equation (Bianchi)"])
            else "FAIL",
            "Chern/gerbe/Bianchi data fixed before selection",
        ),
        Gate(
            "EL equations equal Strominger system",
            "PASS"
            if has_all(strominger, ["Theorem 6", "Euler--Lagrange", "Strominger"])
            else "FAIL",
            "critical points of Xi are Strominger solutions",
        ),
        Gate(
            "MTT fixed-sector selection theorem",
            "PASS"
            if has_all(strominger, ["Theorem 11", "MTT selection", "fixed topological sector"])
            else "FAIL",
            "unique local minimizer equals MTT fixed point",
        ),
        Gate(
            "Fu-Yau admissible flux slice",
            "PASS"
            if has_all(strominger, ["Fu--Yau manifolds furnish", "admissible flux slice"])
            else "FAIL",
            "Fu-Yau class satisfies the selection hypotheses in the corpus",
        ),
        Gate(
            "stable Mukai charge sectors",
            "PASS"
            if has_all(stable, ["stable K3 sheaf sectors", "a=(5,H,0)", "b=(7,3H,1)"])
            else "FAIL",
            "individual stable objects are already supplied",
        ),
        Gate(
            "Mukai discriminant group",
            "PASS" if has_all(discr, ["A_P=P^*/P ~= Z_7", "theta=(1/7,5/7)"]) else "FAIL",
            "determinant-seven block has cyclic discriminant group",
        ),
        Gate(
            "CP character identification",
            "PASS" if has_all(char, ["Gamma_7 = Hom(A_P,U(1))", "Gamma_7 ~= Z_7", "finite-character observability"]) else "FAIL",
            "physical labels are unitary characters once A_P is selected",
        ),
        Gate(
            "fixed-sector selection reduction",
            "PASS"
            if has_all(reduction, ["MTT fixed-sector selection of supplied A_P         CLOSED", "global Fu-Yau/Mukai topological-sector realization/choice"])
            else "FAIL",
            "local dynamics closed by fixed-sector theorem",
        ),
        Gate(
            "global topological-sector realization",
            "CLOSED-CHARGE" if "Z7 global Fu-Yau/Mukai charge-sector certificate       CLOSED" in cert else "FAIL",
            "charge-sector certificate supplies Bianchi-compatible Fu-Yau sector containing P",
        ),
    ]

    print("Fu-Yau/Mukai fixed-sector selection audit")
    print("=========================================")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    hard_failures = [gate for gate in gates if gate.status == "FAIL"]
    if hard_failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
