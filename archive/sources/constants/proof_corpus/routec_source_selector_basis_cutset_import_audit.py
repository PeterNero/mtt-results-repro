"""Audit selected Route-C source-selector and basis cutset import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_source_selector_basis_cutset_import.candidate.json"
CERT = ROOT / "certificates" / "routec_source_selector_basis_cutset_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_SourceSelector_BasisCutset_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_source_selector_basis_cutset.py"

STATUS = "ROUTEC_SOURCE_SELECTOR_BASIS_CUTSET_IMPORTED_PROVENANCE_OR_BASIS_OPEN"
NEXT = "MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1"


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

    upstream = data["upstream_cutset"]
    comparison = upstream["calculation"]["root_vs_formal_payload_diff"]
    require(comparison["total_difference_count"] == 36, "unexpected flag-diff count")
    require(comparison["all_differences_are_allowed_flags"] is True, "non-flag diff found")
    require(upstream["calculation"]["basis_skeleton_verdict"]["closes_actual_basis_functions"] is False, "basis overclosed")
    require(upstream["what_closes_now"]["root_formal_matrix_equality_modulo_flags"] is True, "matrix equality not closed")
    require(upstream["what_remains_open"]["selected_source_provenance_theorem"] is True, "source provenance overclosed")
    require(upstream["what_remains_open"]["quotient_valid_BN_basis_certificate"] is True, "BN basis overclosed")

    guard = data["guardrails"]
    for key in [
        "claims_selected_source_provenance_theorem",
        "claims_quotient_valid_BN_basis_certificate",
        "claims_selected_spectral_error_budget_from_actual_BN",
        "claims_primitive_C1_contractions_after_honest_source",
        "claims_root_manifest_honestly_passes",
        "promotes_lifted_flags_to_proof",
        "claims_full_SM_or_no_knob_closure",
        "uses_observed_or_benchmark_inputs",
        "target_fitting_used",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("total difference is `36`" in note, "note missing exact cutset count")
    require("matrix-disagreement" in note, "note missing matrix-disagreement closure")
    require(NEXT in note, "note missing next artifact")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
