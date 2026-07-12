"""Audit spectral Galerkin projector-retention reduction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "spectral_galerkin_projector_retention_reduction_import.candidate.json"
CERT = ROOT / "certificates" / "spectral_galerkin_projector_retention_reduction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "SpectralGalerkin_ProjectorRetention_Reduction_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_spectral_galerkin_projector_retention_reduction.py"

STATUS = "SPECTRAL_GALERKIN_PROJECTOR_RETENTION_IMPORTED_ROUTEC_SOLVE_OPEN"
NEXT = "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1"


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

    upstream = data["upstream_spectral_projector_retention"]
    two = upstream["two_layer_projector_audit"]
    require(two["block_projector_layer"]["block_family_Higgs_projector_retention"] is True, "block retention missing")
    require(two["spectral_projector_layer"]["coherent_spectral_zero_mode_projector_retention"] is False, "spectral retention overclosed")
    require(two["spectral_projector_layer"]["selected_D_E_dotD_Riesz_Green"] is False, "DE/dotD overclosed")
    require(upstream["selected_solve_contract"]["name"] == "SelectedRouteCStromingerGalerkinResidualSolve", "wrong solve contract")

    guard = data["guardrails"]
    for key in [
        "claims_coherent_spectral_projector_retention",
        "claims_selected_DE_Riesz_Green_dotD_values",
        "claims_selected_HYM_Strominger_metric_connection",
        "claims_operator_level_projective_rhoE",
        "claims_zero_mode_bases_or_primitive_C1",
        "claims_finite_C1_Hessian_deltaTheta_dotD",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("Block-sector projector retention is closed" in note, "note missing block layer")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
