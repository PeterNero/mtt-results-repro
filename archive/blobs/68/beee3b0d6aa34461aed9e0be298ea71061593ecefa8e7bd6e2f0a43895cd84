"""Audit selected Route-C/Strominger Galerkin solve spec import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_strominger_galerkin_solve_spec_import.candidate.json"
CERT = ROOT / "certificates" / "routec_strominger_galerkin_solve_spec_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_Strominger_Galerkin_SolveSpec_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_strominger_galerkin_solve_spec.py"

STATUS = "ROUTEC_STROMINGER_GALERKIN_SOLVE_SPEC_IMPORTED_FIRST_RUN_OPEN"
NEXT = "MTT_Selected_RouteC_Strominger_Galerkin_First_Run_v1"


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

    upstream = data["upstream_routec_solve_spec"]
    require(upstream["mesh_scaffold"]["matches_certificate_counts"] is True, "mesh accounting mismatch")
    require(upstream["promotion_gate"]["must_pass_after_outputs_exist"] is True, "promotion gate missing")
    require(upstream["residual_acceptance"]["positive_gates"]["mtt_hessian_min_eigenvalue"] is None, "positive gate overfilled")
    require(upstream["currently_blocked_by"]["actual_selected_values"] is True, "selected values not open")

    guard = data["guardrails"]
    for key in [
        "claims_actual_selected_small_N_solve",
        "claims_selected_rhoE_metric_connection_values",
        "claims_actual_basis_BN_or_quadrature",
        "claims_selected_DE_Riesz_Green_dotD_outputs",
        "claims_spectral_gap_error_numbers",
        "claims_zero_mode_bases_or_C1_primitives",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_masses_mixings_or_benchmark_matrices",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("executable spec" in note, "note missing executable spec")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
