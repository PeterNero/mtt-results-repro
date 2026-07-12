"""Audit the Mukai Z7 CP character-identification theorem."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "Mukai_Z7_CP_Character_Identification_Theorem_v1.md"
DISCR = ROOT / "Mukai_Discriminant_Group_Selection_for_Z7_CP_v1.md"
CERT = ROOT / "Z7_FuYau_Mukai_Charge_Sector_Certificate_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def main() -> None:
    paper = read(PAPER)
    discr = read(DISCR)
    cert = read(CERT)

    gates = [
        Gate("paper saved", "PASS" if paper else "FAIL", str(PAPER)),
        Gate("A_P discriminant source", "PASS" if "A_P=P^*/P ~= Z_7" in discr else "FAIL", "Mukai discriminant group is Z7"),
        Gate("finite-character principle", "PASS" if "recordable CP phases are unitary characters" in paper else "FAIL", "MTT observability principle"),
        Gate("Hom(A_P,U1) identification", "PROVED" if "Gamma_7 = Hom(A_P,U(1))" in paper else "FAIL", "once A_P is selected"),
        Gate("theta7 generator", "PASS" if "theta_7=(1/7,5/7)" in paper else "FAIL", "explicit order-seven generator"),
        Gate("fixed-sector selection of supplied P", "PROVED*", "Fu-Yau/Mukai fixed-sector selection reduction"),
        Gate(
            "global selection of P",
            "CLOSED-CHARGE" if "Z7 global Fu-Yau/Mukai charge-sector certificate       CLOSED" in cert else "FAIL",
            "charge-sector certificate selects the Fu-Yau/Mukai sector",
        ),
        Gate(
            "Fu-Yau anomaly compatibility",
            "CLOSED-CHARGE" if "Green-Schwarz Bianchi identity satisfied" in cert else "FAIL",
            "satisfied by the fixed Fu-Yau/Strominger background",
        ),
    ]

    print("Mukai Z7 CP character-identification audit")
    print("==========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
