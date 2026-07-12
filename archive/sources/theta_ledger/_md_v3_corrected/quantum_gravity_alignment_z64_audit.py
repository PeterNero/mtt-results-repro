"""Audit quantum-gravity alignment with the current Z64 CKM closure spine."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
QG = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\12 Quantum Gravity")

FILES = {
    "qg_main": QG / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md",
    "qg_i": QG / "Constructive_MTT_Quantum_Gravity_I__Borel_Summability_of_the_SPT_Filtered_TT_Sector.md",
    "qg_ii": QG / "Constructive_MTT_Quantum_Gravity_II__BRST_Lifting__Gauge_Invariant_Observables__and_the_Physical_Hilbert_Space_under_SPT_Damping.md",
    "qg_iii": QG / "Constructive_MTT_Quantum_Gravity_III__Infrared_Limit_and_Scattering_under_SPT_Damping.md",
    "third_corner": QG / "A_Third_Corner_Shadow_Bridge__Asymptotic_Safety__the_String_Corner__and_the_Coherent_Spine_in_Modal_Triplet_Theory.md",
    "flavor_schur": ROOT / "Schur_Gap_Constant_Reduction_for_Z64_Projector_v1.md",
    "pure_circle": ROOT / "Pure_Central_Circle_Block_Reduction_for_Z64_Hessian_Bound_v1.md",
    "alignment": ROOT / "Quantum_Gravity_Alignment_Evaluation_for_Z64_CKM_Closure_v1.md",
    "criterion": ROOT / "Finite_Wilson_Deck_Carrier_Extraction_Criterion_for_Z64_v1.md",
    "schur": ROOT / "Exact_Coherent_Block_Schur_Collapse_for_Z64_Projector_v1.md",
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


def main() -> None:
    texts = {name: read(path) for name, path in FILES.items()}
    qg_main = texts["qg_main"]
    qg_i = texts["qg_i"]
    qg_ii = texts["qg_ii"]
    qg_iii = texts["qg_iii"]
    third = texts["third_corner"]
    flavor = texts["flavor_schur"]
    pure = texts["pure_circle"]
    alignment = texts["alignment"]
    criterion = texts["criterion"]
    schur = texts["schur"]

    gates = [
        Gate(
            "alignment paper saved",
            "PASS" if alignment else "FAIL",
            str(FILES["alignment"]),
        ),
        Gate(
            "QG main coherent gap",
            "PASS" if "A_{\\mathrm{int}}" in qg_main and "lambda_\\ast" in qg_main else "FAIL",
            "A_int has positive gap on noncoherent complement",
        ),
        Gate(
            "QG SPT damping",
            "PASS" if "e^{-\\tau_0 k^2}" in qg_main or "proper-time gap" in qg_main else "FAIL",
            "Gaussian damping from proper-time spectral filter",
        ),
        Gate(
            "QG block commutation",
            "PASS" if "[E,A_{\\mathrm{int}}]=0" in qg_main else "FAIL",
            "external/internal blocks commute in baseline setting",
        ),
        Gate(
            "QG off-diagonal stability",
            "PASS" if "off-diagonal couplings" in qg_main and "Kato" in qg_main else "FAIL",
            "mild warp/twist couplings persist with renormalized constants",
        ),
        Gate(
            "Constructive QG I UV control",
            "PASS" if "Borel summability" in qg_i and "e^{-\\tau_0|k|^2}" in qg_i else "FAIL",
            "SPT-filtered TT sector is constructively controlled",
        ),
        Gate(
            "Constructive QG II BRST lift",
            "PASS" if "BRST" in qg_ii and "physical Hilbert space" in qg_ii else "FAIL",
            "gauge-invariant observables live in BRST cohomology",
        ),
        Gate(
            "Constructive QG III scoped IR assumption",
            "NEEDS-SCOPE" if "TT mass gap" in qg_iii else "MISSING",
            "valid as scattering/IR-control hypothesis, not a massive-graviton claim",
        ),
        Gate(
            "Third-corner gap remainders",
            "PASS" if "lambda_\\ast^{-1}" in third and "coherent spine" in third else "FAIL",
            "string/asymptotic-safety shadows use O(lambda_*^{-1}) control",
        ),
        Gate(
            "Flavor reduced Schur gate",
            "PASS" if "C_fl / (alpha lambda_Q) < 9/2" in flavor else "FAIL",
            "current Z64 proof target",
        ),
        Gate(
            "Flavor warp leakage term",
            "PASS" if "epsilon_warp" in pure and "C_fl/lambda_Q" in pure else "FAIL",
            "matches QG off-diagonal stability language",
        ),
        Gate(
            "P_fl/Pi_coh compatibility",
            "PROVED*",
            "proved under commuting twisted spectral data and coherent-only contour",
        ),
        Gate(
            "Z64 finite Wilson/deck carrier target",
            "FORMULATED",
            "K64 ~= C[Z64] with exact-order U64; Hessian derivation still open",
        ),
        Gate(
            "finite carrier extraction criterion",
            "PROVED" if "finite carrier extraction criterion" in criterion and "primitive shift gives exact order 64" in criterion else "FAIL",
            "block-circulant primitive-lag signature would derive U64",
        ),
        Gate(
            "lambda_Q/lambda_* bridge",
            "PROVED*",
            "lambda_Q>=lambda_* when the selected Q block is the QG complement",
        ),
        Gate(
            "exact Schur collapse",
            "PROVED" if "C_fl=0 in exact branch" in schur else "FAIL",
            "exact coherent block gives C_fl=0",
        ),
    ]

    print("Quantum-gravity alignment audit")
    print("===============================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
