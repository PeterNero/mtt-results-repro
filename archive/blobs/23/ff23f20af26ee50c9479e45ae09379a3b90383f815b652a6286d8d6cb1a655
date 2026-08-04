"""Audit Route-C dependency cutset import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_dependency_cutset_import.candidate.json"
CERT = ROOT / "certificates" / "routec_dependency_cutset_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_DependencyCutset_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_dependency_cutset.py"

STATUS = "ROUTEC_DEPENDENCY_CUTSET_IMPORTED_ORTHOGONAL_COMPLETION_OR_INDEPENDENT_SOLVE_OPEN"
NEXT = "MTT_Selected_DifferentiatedC1OrthogonalCompletionPrinciple_or_IndependentQuadratureHessianSolve_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")
    require(all(data["checks"].values()), "not all checks passed")

    summary = data["dependency_cutset_summary"]
    require(summary["patched_spine_closure_preserved"] is True, "patched closure not preserved")
    require(summary["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(summary["independent_galerkin_closed"] is False, "independent Galerkin overclaimed")
    require(summary["algebraic_Q_residual_uniqueness_closed"] is True, "Q uniqueness missing")
    require(summary["physical_PhiFinC1_application_open"] is True, "PhiFinC1 gap missing")
    require(summary["strict_replay_passes"] is True, "replay missing")
    require(summary["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "ATA mismatch")
    require(summary["A_transpose_b"] == [12.0, 12.0], "ATb mismatch")
    require(summary["deltaTheta_C1"] == [1.0, 1.0], "delta mismatch")
    require(summary["minimal_exits"] == [
        "DifferentiatedC1OrthogonalCompletionPrinciple",
        "IndependentGalerkinQuadratureHessianSolve",
    ], "minimal exits mismatch")

    upstream = data["upstream_candidate"]
    require(upstream["patched_spine_closure_preserved"] is True, "upstream patch missing")
    require(upstream["unpatched_theorem_closure_claimed"] is False, "upstream unpatched overclaim")
    require(upstream["closure_claimed"] is False, "upstream closure overclaim")
    for key in [
        "derive_differentiated_C1_orthogonal_completion_principle",
        "prove_physical_PhiFinC1_applies_Q_residual",
        "emit_independent_selected_zero_mode_basis",
        "compute_independent_primitive_contractions",
        "emit_independent_hessian_b_selected",
        "close_unpatched_SM_parity_dynamic_packet",
        "true_SM_equivalence_closure",
    ]:
        require(upstream["what_remains_open"][key] is True, f"remaining gate missing: {key}")

    packets = data["upstream_packets"]
    require(packets["independence_dependency_audit"]["status"] == "DEPENDENCY_FOUND_REPLAY_NOT_INDEPENDENT", "dependency status mismatch")
    require(packets["residual_projector_derivation_ladder"]["status"] == "ALGEBRAIC_UNIQUENESS_CLOSED_PHYSICAL_APPLICATION_OPEN", "ladder status mismatch")
    require(packets["minimal_next_source_contract"]["status"] == "TWO_MINIMAL_SOURCE_OPTIONS_DECLARED", "contract status mismatch")

    for key in [
        "claims_unpatched_SM_dynamic_closure",
        "claims_unpatched_A_selected",
        "claims_unpatched_b_selected",
        "claims_independent_Galerkin_C1",
        "claims_true_SM_equivalence",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(data["guardrails"][key] is False, f"guardrail overclaimed: {key}")

    require("dependency cutset is now sharp" in note, "note missing cutset summary")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
