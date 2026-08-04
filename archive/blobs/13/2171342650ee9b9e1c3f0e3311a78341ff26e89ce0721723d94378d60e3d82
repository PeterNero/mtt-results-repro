from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79normalizedpoincaregerbeandpgl3prymreduction"
STATUS = "MTT_U6_Q79_GERBE_RESIDUE_REDUCED_TO_8X8_PGL3_PRYM_SYSTEM_JACOBIAN_VALUES_OPEN"
NEXT = "MTT_Selected_q79PGL3ToPrymGerbeJacobianExecution_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79NormalizedPoincareGerbeAndPGL3PrymReduction_v1.md"


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
    push = outputs["spectral_trace_decomposition"]
    prym = outputs["normalized_gerbe_Prym_reduction"]
    square = outputs["PGL3_Prym_square_system"]
    open_jac = outputs["PGL3_Prym_open_Jacobian"]
    frontier = outputs["U6_frontier"]

    require(candidate["status"] == certificate["status"] == STATUS, "A105 status changed")
    require(candidate["next_required_artifact"] == certificate["next_required_artifact"] == NEXT, "A105 next changed")
    require(all(candidate["checks"].values()), "one or more A105 checks failed")
    require(candidate["results"]["new_fitted_continuous_parameters"] == 0, "fitted parameter added")

    exact = push["spectral_exact_sequence"]
    require(exact["H0_E_O_minus3"] == 0, "negative degree H0")
    require(exact["H1_E_O_minus3_dimension"] == 3, "negative degree H1")
    pushed = push["pushforward_to_K3"]
    require(pushed["rank_K"] == 2, "trace-free rank")
    require(pushed["K_identification"] == "K = phi_H^* Omega^1_P2", "Euler identification")
    require(pushed["split_canonical_in_characteristic_zero"], "trace split not canonical")
    cohom = push["cohomology_split"]
    require(cohom["H2_O_K3_dimension"] == 1, "K3 H2O")
    require(cohom["H2_K_dimension"] == 8, "trace-free H2")
    require(cohom["H2_O_C_dimension"] == 9, "surface H2O")
    require(cohom["trace_component_dimension"] + cohom["Prym_trace_free_component_dimension"] == 9, "1+8 split")

    norm = prym["base_Brauer_normalization"]
    require(norm["zero_section_restriction"] == 0, "zero normalization")
    require(norm["normalization_unique"], "base Brauer ambiguity retained")
    biext = prym["biextension_norm_identity"]
    require(biext["spectral_determinant"] == "y1+y2+y3=0 in E on every fiber", "determinant zero lost")
    require(biext["norm_alpha_C_to_K3"] == 0, "gerbe norm nonzero")
    require(biext["trace_beta_C_to_K3"] == 0, "beta trace nonzero")
    residue = prym["Prym_residue"]
    require(residue["A104_ambient_H2O_dimension"] == 9, "A104 dimension lost")
    require(residue["trace_component_removed"] == 1, "wrong trace removal")
    require(residue["remaining_complex_tangent_dimension"] == 8, "wrong Prym dimension")
    require(not residue["beta_C_zero_proved"], "beta overclosed")

    serre = square["Serre_duality"]
    require(serre["H0_T_P2_dimension"] == 8, "PGL3 vector fields")
    require(serre["H0_T_P2_minus3_dimension"] == 0, "double-cover extra sections")
    require(serre["H0_phi_pullback_T_dimension"] == 8, "pullback tangent dimension")
    require(serre["identification"] == "H2(K)^* = H0(phi_H^*T_P2) = pgl3", "duality typing")
    require(serre["perfect_dimension_match"], "dimension match lost")
    mapping = square["alignment_to_residue_map"]
    require(mapping["domain_complex_dimension"] == 8, "PGL3 domain dimension")
    require(mapping["codomain_fiber_complex_tangent_dimension"] == 8, "Prym codomain dimension")
    require("relative" in mapping["codomain"], "varying Prym target flattened globally")
    require("Gauss-Manin" in mapping["local_Jacobian"], "local Prym trivialization missing")
    require(mapping["Jacobian_shape"] == [8, 8], "Jacobian shape")
    require(not mapping["Jacobian_entries_computed"], "Jacobian values invented")
    require(not mapping["Jacobian_determinant_computed"], "Jacobian determinant invented")
    require(not mapping["zero_alignment_found"], "alignment zero invented")
    require(not square["selection_logic"]["observed_data_used"], "observed selector used")

    require(len(open_jac["basis"]["pgl3_generators_8"]) == 8, "pgl3 basis template")
    require(len(open_jac["basis"]["trace_free_H2_K_basis_8"]) == 8, "Prym basis template")
    matrix = open_jac["same_branch_data"]["d_beta_d_alignment_8x8"]
    require(len(matrix) == 8 and all(len(row) == 8 for row in matrix), "open 8x8 template")
    require(all(value is None for row in matrix for value in row), "Jacobian entries fabricated")
    require(open_jac["same_branch_data"]["local_Gauss_Manin_or_holomorphic_Prym_trivialization"] is None, "Prym trivialization fabricated")
    require(not any(open_jac["acceptance"].values()), "open Jacobian accepted")

    require(frontier["analytic_residue_ambient_dimension_A104"] == 9, "A104 residue hidden")
    require(frontier["analytic_residue_active_Prym_dimension"] == 8, "active residue dimension")
    require(frontier["alignment_domain_dimension"] == 8, "alignment dimension")
    require(frontier["square_Jacobian_shape"] == [8, 8], "frontier square system")
    require(not frontier["actual_FuYau_balanced_HYM_proved"], "HYM overclosed")
    require(not frontier["actual_FuYau_nonpullback_Bianchi_proved"], "Bianchi overclosed")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A105 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in [
        "Trace decomposition",
        "p_*O_C = O_K3 direct_sum K",
        "9 = 1 + 8",
        "Normalize the Poincare gerbe",
        "Nm(alpha_0|C)=0",
        "The 8 by 8 theorem",
        "H^2(K)^* = pgl3",
        "This dimension match is not itself an existence theorem",
    ]:
        require(phrase in note, f"proof note missing: {phrase}")

    print("A105 normalized-Poincare/PGL3-Prym reduction audit: PASS")
    print(f"status={STATUS}")
    print("H2(O_C)=trace(1) direct_sum Prym(8); determinant-zero kills trace")
    print("Prym tangent is dual to pgl3; remaining same-branch test is 8x8")
    print("Jacobian entries, transverse zero, HYM and Bianchi remain open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
