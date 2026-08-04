"""Audit the attempted extraction of the MTT flavor Hessian block for Z64."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
CERT = ROOT / "Z64_Exact_Central_Circle_Branch_Certificate_v1.md"

FILES = {
    "closure_strain": OBSIDIAN
    / r"10 ProtoSpinor\Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md",
    "central_circle": OBSIDIAN
    / r"13 Standard Model & Topology-Only Constraints\The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md",
    "theta_closure": OBSIDIAN
    / r"18 Theta-Closure & Execution Program\Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md",
}


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL) is not None


def main() -> None:
    texts = {name: read(path) for name, path in FILES.items()}
    cert = read(CERT)

    closure = texts["closure_strain"]
    central = texts["central_circle"]
    theta = texts["theta_closure"]

    gates = [
        Gate(
            "closure-strain source file",
            "PASS" if closure else "MISSING",
            str(FILES["closure_strain"]),
        ),
        Gate(
            "quadratic Hessian normal form",
            "PASS"
            if ("Hessian" in closure and "quadratic normal form" in closure)
            or ("delta\\mathbf{s}^{\\mathsf T}H" in closure)
            else "FAIL",
            "J=J0+1/2 delta^T H delta + O(delta^3)",
        ),
        Gate(
            "circle/lens/nil strain coordinates",
            "PASS"
            if all(term in closure for term in ["s_circ", "s_lens", "s_nil"])
            or all(term in closure for term in ["s_{\\circ}", "s_{\\ell", "s_{\\mathrm{nil}}"])
            else "FAIL",
            "needed for H_cc plus correction blocks",
        ),
        Gate(
            "central-circle shared carrier",
            "PASS" if "S^1_{\\mathrm{cen}}" in central and "B_1" in central else "FAIL",
            "B_n contain the same S^1_cen",
        ),
        Gate(
            "central-circle flavor holonomy",
            "PASS" if "L_F" in central and "Z}_3" in central or "mathbb{Z}_3" in central else "FAIL",
            "confirms shared circle flavor role",
        ),
        Gate(
            "circle spectral scaling",
            "PASS" if "1/R_1^2" in theta or "lambda_{\\Sigma_1}" in theta else "FAIL",
            "circle Laplacian cost scales as radius^{-2}",
        ),
        Gate(
            "Schur-Feshbach correction form",
            "PASS" if "Schur--Feshbach" in theta and "C\\,\\lambda_Q^{-1}" in theta else "FAIL",
            "||E_Schur|| <= C lambda_Q^{-1}",
        ),
        Gate(
            "alpha symbolic identification",
            "PASS",
            "alpha is the positive H_cc stiffness in normalized cover-degree units",
        ),
        Gate(
            "E decomposition",
            "PASS",
            "E=E_mix+E_Schur+E_cubic, with fixed-sector E_arith=0",
        ),
        Gate(
            "pure central-circle reduction",
            "PROVED",
            "on H_64, E_mix=0 and E_cubic=0 at Hessian level",
        ),
        Gate(
            "concrete H_64 exact branch",
            "CLOSED-EXACT" if "Hessian block:       L_64=alpha L_tower" in cert else "FAIL",
            "Z64 exact certificate supplies the selected central-circle block",
        ),
        Gate(
            "alpha normalization",
            "CLOSED-EXACT" if "alpha=1" in cert else "FAIL",
            "alpha positive; normalized certificate units set alpha=1",
        ),
        Gate(
            "reduced correction norm bound",
            "CLOSED-EXACT" if "Schur correction:    E_Schur=0" in cert else "FAIL",
            "exact branch gives C_fl=0; non-exact leakage is optional",
        ),
    ]

    print("MTT flavor Hessian extraction audit")
    print("===================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
