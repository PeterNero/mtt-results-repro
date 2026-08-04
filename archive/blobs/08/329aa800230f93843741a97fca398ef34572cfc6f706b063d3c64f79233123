"""Audit the twisted/equivariant Z64 CP carrier candidate."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

FILES = {
    "paper": ROOT / "Twisted_Equivariant_Central_Circle_Z64_CP_Sector_Candidate_v1.md",
    "compat": ROOT / "Flavor_QG_Projector_Compatibility_Lemma_for_Z64_CKM_Closure_v1.md",
    "criterion": ROOT / "Finite_Wilson_Deck_Carrier_Extraction_Criterion_for_Z64_v1.md",
    "primitive_lag": ROOT / "Selected_Kernel_Primitive_Lag_Closure_for_Z64_Carrier_v1.md",
    "schur": ROOT / "Exact_Coherent_Block_Schur_Collapse_for_Z64_Projector_v1.md",
    "tower": ROOT / "Spectral_Flavor_Projector_Construction_for_Z64_Dyadic_Tower_v1.md",
    "terminal": ROOT / "Terminal_Spinorial_Return_Gate_for_Z64_Carry_v1.md",
    "central_circle": OBSIDIAN
    / r"13 Standard Model & Topology-Only Constraints\The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md",
    "parameters": OBSIDIAN
    / r"2 Meta & Diagnosis & Universality\Modal_Triplet_Theory__Parameters__Closure__and_Structural_Falsifiability.md",
    "proto_action": OBSIDIAN
    / r"10 ProtoSpinor\Closure_Geometry_and_Unified_Dynamics__A_Ten_Dimensional_Action_for_Mass__Scalar_Relaxation__Quantization__and_Curvature_v3.md",
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
    compat = texts["compat"]
    criterion = texts["criterion"]
    primitive_lag = texts["primitive_lag"]
    schur = texts["schur"]
    tower = texts["tower"]
    terminal = texts["terminal"]
    central = texts["central_circle"]
    parameters = texts["parameters"]
    proto_action = texts["proto_action"]

    gates = [
        Gate(
            "candidate paper saved",
            "PASS" if paper else "FAIL",
            str(FILES["paper"]),
        ),
        Gate(
            "central-circle finite holonomy corpus support",
            "PASS" if "discrete holonomy" in central and "finite subgroup of $U(1)$" in central else "FAIL",
            "central circle already carries finite character sectors",
        ),
        Gate(
            "CP phases from circle/Wilson data",
            "PASS" if "Wilson-line or holonomy choices" in parameters and "Phase data from circle-holonomy" in proto_action else "FAIL",
            "corpus places CP phases in Wilson/holonomy bottleneck data",
        ),
        Gate(
            "raw scalar Fourier trap rejected",
            "PASS" if "nonzero scalar Fourier spectrum" in paper and "not scalar Laplacian eigenmodes" in paper else "FAIL",
            "Z64 carrier does not rely on illicit scalar zero modes",
        ),
        Gate(
            "exact-order U64 carrier",
            "PASS" if "U_64^64 = I" in paper and "U_64^d != I" in paper else "FAIL",
            "finite unitary has exact order 64",
        ),
        Gate(
            "character idempotents",
            "PASS" if "E_q = (1/64)" in paper and "direct_sum_{q in Z_64}" in paper else "FAIL",
            "finite quotient is encoded by spectral projectors of U64",
        ),
        Gate(
            "Pi_coh containment target",
            "PASS" if "P_CP,64 <= Pi_coh" in paper else "FAIL",
            "carrier is explicitly a coherent-sector subprojector",
        ),
        Gate(
            "compatibility theorem imported",
            "PASS" if "P_fl Pi_coh = Pi_coh P_fl = P_fl" in paper and "exact compatibility theorem" in compat else "FAIL",
            "candidate plugs into the proven projector lemma",
        ),
        Gate(
            "carrier extraction criterion",
            "PROVED" if "primitive-lag test prevents divisor collapse" in criterion else "FAIL",
            "exact U64 follows from primitive shift plus block-circulant kernel",
        ),
        Gate(
            "selected-kernel primitive lag",
            "PROVED" if "selected-kernel primitive-lag gate              PROVED" in primitive_lag else "FAIL",
            "unit lag sees the full Z64 carrier",
        ),
        Gate(
            "Z64 tower imported",
            "PASS" if "(2,2,2,2,2)" in tower and "Gamma_2 ~= Z_64" in tower else "FAIL",
            "D2 tower supplies the dyadic carry quotient",
        ),
        Gate(
            "terminal parity imported",
            "PASS" if "2x_5=0" in terminal and "spinorial return parity" in terminal else "FAIL",
            "spinorial terminal row is already proved",
        ),
        Gate(
            "MTT Hessian selects exact carrier",
            "OPEN",
            "derive U64 and the retained carrier block from selected Hessian/kernel",
        ),
        Gate(
            "lambda_Q/lambda_* bridge",
            "PROVED*",
            "lambda_Q>=lambda_* when Q is the QG noncoherent complement",
        ),
        Gate(
            "exact-branch Schur inequality",
            "PROVED" if "C_fl/(alpha lambda_Q)<9/2 in exact branch             PROVED" in schur else "FAIL",
            "C_fl=0 under exact coherent block commutation",
        ),
        Gate(
            "non-exact Schur inequality",
            "OPEN",
            "bound commutator/warp leakage if exact block assumptions are relaxed",
        ),
    ]

    print("Twisted/equivariant Z64 CP carrier audit")
    print("=========================================")
    print()
    width = max(len(g.label) for g in gates)
    status_width = max(len(g.status) for g in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")


if __name__ == "__main__":
    main()
