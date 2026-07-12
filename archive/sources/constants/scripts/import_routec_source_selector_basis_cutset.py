"""Import selected Route-C source-selector and basis cutset theorem."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "routec_strominger_galerkin_first_run_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_source_selector_and_basis_theorem.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_source_selector_and_basis_theorem_certificate.json"

OUTPUT_PACKET = DATA / "routec_source_selector_basis_cutset_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_source_selector_basis_cutset_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_SourceSelector_BasisCutset_Import_v1.md"

STATUS = "ROUTEC_SOURCE_SELECTOR_BASIS_CUTSET_IMPORTED_PROVENANCE_OR_BASIS_OPEN"
PREVIOUS_STATUS = "ROUTEC_STROMINGER_GALERKIN_FIRST_RUN_IMPORTED_SELECTOR_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_SOURCE_SELECTOR_AND_BASIS_CALCULATION_LOCKED_SELECTOR_OPEN"
NEXT = "MTT_Selected_RouteC_Source_Provenance_or_Basis_Certificate_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    comparison = upstream["calculation"]["root_vs_formal_payload_diff"]
    basis = upstream["calculation"]["basis_skeleton_verdict"]
    locked = upstream["locked_conditions"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_Source_Selector_and_Basis_Theorem_v1",
        "F1_upstream_cutset_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["closure_claimed"] is False
        and upstream_cert["target_fitting_used"] is False
        and upstream_cert["primary_next_artifact"] == NEXT,
        "F3_root_formal_delta_exactly_flags": comparison["all_differences_are_allowed_flags"] is True
        and comparison["changed_terminal_keys"]
        == ["alpha1_driver_verified", "selected_dotD_source_verified", "selected_source_verified"]
        and comparison["total_difference_count"] == 36,
        "F4_no_matrix_mismatch_hidden": upstream["what_closes_now"]["root_formal_matrix_equality_modulo_flags"] is True
        and upstream["what_closes_now"]["downstream_algebra_conditional_pass_confirmed"] is True
        and upstream["calculation"]["formal_lift_lower_validators_all_pass"] is True
        and upstream["calculation"]["formal_lift_de_response_promotion_passes"] is True,
        "F5_honest_failures_retained": "route_c_residual" in upstream["calculation"]["honest_root_failures"]
        and upstream["calculation"]["honest_root_failures"]["route_c_residual"]["exit_code"] == 1,
        "F6_basis_gap_retained": basis["closes_basis_skeleton"] is True
        and basis["closes_actual_basis_functions"] is False
        and upstream["what_remains_open"]["quotient_valid_BN_basis_certificate"] is True,
        "F7_locked_conditions_exact": set(locked) == {"C1_source_selector_condition", "C2_basis_condition"}
        and locked["C1_source_selector_condition"]["name"] == "selected source provenance"
        and locked["C2_basis_condition"]["name"] == "quotient-valid selected Galerkin basis",
        "F8_no_overclaim": upstream["what_remains_open"]["full_SM_or_no_knob_closure"] is True
        and upstream["what_remains_open"]["selected_source_provenance_theorem"] is True
        and upstream["what_remains_open"]["selected_spectral_error_budget_from_actual_BN"] is True,
    }

    return {
        "packet": "RouteC_SourceSelector_BasisCutset_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "RouteCSourceSelectorBasisCutsetImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The honest root and formal-lift Route-C/Strominger first-run "
                "payloads have identical finite matrices modulo 36 provenance "
                "flag flips.  Thus the remaining proof is not matrix repair; it "
                "is a selected-source provenance theorem plus a quotient-valid "
                "B_N basis/operator extraction certificate."
            ),
        },
        "checks": checks,
        "upstream_cutset": upstream,
        "locked_conditions": locked,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_selected_source_provenance_theorem": False,
            "claims_quotient_valid_BN_basis_certificate": False,
            "claims_selected_spectral_error_budget_from_actual_BN": False,
            "claims_primitive_C1_contractions_after_honest_source": False,
            "claims_root_manifest_honestly_passes": False,
            "promotes_lifted_flags_to_proof": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCSourceSelectorBasisCutsetImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "locked_conditions": packet["locked_conditions"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    return f"""# RouteC SourceSelector BasisCutset Import v1

Status: `{cert["status"]}`.

The remaining Route-C/Strominger Galerkin calculation is now an exact cutset.
The honest root manifest and formal-lift diagnostic manifest use the same
finite matrices; their total difference is `36` false-to-true provenance flags.

This closes matrix-disagreement as the blocker.  It does not close proof
promotion.  The two live proof objects are:

- selected-source provenance for the Route-C residual, operators, Riesz/Green,
  dotD source, and alpha1 driver flags
- quotient-valid selected `B_N` basis/operator extraction, including basis
  functions, deck constraints, bundle transitions, quadrature, stiffness/Gram
  entries, and selected `D_E` action

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
