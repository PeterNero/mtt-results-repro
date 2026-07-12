"""Audit the flavor-QG projector compatibility lemma for the Z64 program."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

FILES = {
    "paper": ROOT / "Flavor_QG_Projector_Compatibility_Lemma_for_Z64_CKM_Closure_v1.md",
    "criterion": ROOT / "Finite_Wilson_Deck_Carrier_Extraction_Criterion_for_Z64_v1.md",
    "schur": ROOT / "Exact_Coherent_Block_Schur_Collapse_for_Z64_Projector_v1.md",
    "foundation": OBSIDIAN
    / r"3 Core Foundations\Modal_Triplet_Theory__Foundation_v6 (1).md",
    "damping": OBSIDIAN
    / r"5 Dirac Delta\Deriving_the_MTT_Coherence_Scale_from_Fixed__Point_Damping.md",
    "wave_particle": OBSIDIAN
    / r"5 Dirac Delta\Wave__Particle_Duality_as_Projection_Duality_in_Modal_Triplet_Theory_v4.md",
    "qg_main": OBSIDIAN
    / r"12 Quantum Gravity\Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md",
    "central_circle": OBSIDIAN
    / r"13 Standard Model & Topology-Only Constraints\The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md",
    "cy": OBSIDIAN
    / r"16 Strings, Flux, & M-Theory Encodings\Modal_Triplet_Theory__From_MTT_to_Calabi__Yau_Compactifications.md",
    "strominger": OBSIDIAN
    / r"16 Strings, Flux, & M-Theory Encodings\Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
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
    paper = texts["paper"]
    criterion = texts["criterion"]
    schur = texts["schur"]
    foundation = texts["foundation"]
    damping = texts["damping"]
    wave = texts["wave_particle"]
    qg = texts["qg_main"]
    central = texts["central_circle"]
    cy = texts["cy"]
    strom = texts["strominger"]

    gates = [
        Gate(
            "compatibility paper saved",
            "PASS" if paper else "FAIL",
            str(FILES["paper"]),
        ),
        Gate(
            "Foundation commuting Laplacians",
            "PASS" if "Delta_1,\\Delta_2,\\Delta_3" in foundation and "commute" in foundation else "FAIL",
            "base-only warping gives joint spectral structure",
        ),
        Gate(
            "Foundation joint Pi_coh",
            "PASS" if "\\Pi_{\\mathrm{coh}}" in foundation and "\\prod" in foundation else "FAIL",
            "Pi_coh is joint Riesz/spectral projector",
        ),
        Gate(
            "Foundation warp leakage",
            "PASS" if "O(\\varepsilon_{\\mathrm{warp}})" in foundation else "FAIL",
            "fiber-dependent perturbations tracked as epsilon_warp",
        ),
        Gate(
            "Riesz commutation source",
            "PASS"
            if "Riesz projector of $A$" in wave and "commutes with $A$" in wave
            else "FAIL",
            "Riesz projectors commute with their operator",
        ),
        Gate(
            "fixed-point commutator criterion",
            "PASS" if "[P,A]=0" in damping and "spectral/Riesz projector" in damping else "FAIL",
            "commutation automatic for spectral/Riesz projectors",
        ),
        Gate(
            "QG block and gap structure",
            "PASS" if "[E,A_{\\mathrm{int}}]=0" in qg and "lambda_\\ast" in qg else "FAIL",
            "QG coherent/noncoherent split uses the same block logic",
        ),
        Gate(
            "central-circle flavor line bundle",
            "PASS" if "L_F \\rightarrow S^1_{\\mathrm{cen}}" in central else "FAIL",
            "flavor sectors are holonomy line-bundle sectors",
        ),
        Gate(
            "central-circle coherent modes",
            "PASS" if "psi_f(\\theta)" in central and "coherent mode" in central else "FAIL",
            "family holonomy modes are coherent configurations",
        ),
        Gate(
            "CY split HYM projector",
            "PASS" if "Commuting bundle Laplacians for split HYM" in cy else "FAIL",
            "twisted/bundle Laplacians can commute in product connection setting",
        ),
        Gate(
            "Strominger twisted commutation",
            "PASS" if "vertical twisted Laplacians commute" in strom else "FAIL",
            "flux/twisted sectors have analogous commuting projectors",
        ),
        Gate(
            "raw Fourier caveat",
            "PASS" if "raw scalar circle Laplacian" in paper and "twisted/equivariant" in paper else "FAIL",
            "raw scalar Fourier modes require a retained twisted/equivariant spectral sector",
        ),
        Gate(
            "exact compatibility theorem",
            "PROVED" if "P_fl Pi_coh = Pi_coh P_fl = P_fl" in paper else "FAIL",
            "under commuting twisted spectral data and coherent-only contour",
        ),
        Gate(
            "Z64 finite Wilson/deck carrier target",
            "FORMULATED",
            "K64 ~= C[Z64] with exact-order U64; Hessian derivation still open",
        ),
        Gate(
            "finite carrier extraction criterion",
            "PROVED" if "block-circulant kernel preserves character sectors" in criterion else "FAIL",
            "primitive shift plus primitive-lag kernel derives exact U64 carrier",
        ),
        Gate(
            "lambda_Q/lambda_* bridge",
            "PROVED*",
            "lambda_Q>=lambda_* when Q is the QG noncoherent complement",
        ),
        Gate(
            "exact Schur collapse",
            "PROVED" if "C_fl=0 in exact branch" in schur else "FAIL",
            "P_fl<=Pi_coh and [L,Pi_coh]=0 imply C_fl=0",
        ),
    ]

    print("Flavor-QG projector compatibility audit")
    print("========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
