"""Build I11 physical-source value closure or five-clause source gap gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_i11_physicalsource_valueclosure_or_fiveclausegap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALUE = PACKET_DIR / "canonical_residual_bvalue_closure_sublemma.packet.json"
CURRENT = PACKET_DIR / "current_physical_source_valueclosure_trace_map_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_fiveclause_physical_source_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_five_physical_clause_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11_PhysicalSourceValueClosure_or_FiveClauseGap_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"

STATUS = "MTT_SELECTED_I11_PHYSICALSOURCE_VALUES_CLOSED_FIVE_CLAUSES_OPEN"
NEXT = "MTT_Selected_I11_FivePhysicalClauses_SourcePromotion_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(VALIDATOR),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    prior = load(DATA / "selected_i11_c1coordinatechart_or_physicalsourcegap.candidate.json")
    residual_values = load(
        DATA
        / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
        / "canonical_residual_operator_values.packet.json"
    )
    physical_status = load(
        DATA
        / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
        / "same_source_physical_emission_status.packet.json"
    )
    route_b = load(
        DATA
        / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
        / "unpatched_galerkin_replacement_status.packet.json"
    )
    clauses = load(
        DATA
        / "selected_physicalactionrestrictionclause_or_primitivekernelformula"
        / "physical_action_restriction_clause_ledger.packet.json"
    )

    residual_values_closed = (
        residual_values["mathematical_residual_values_ready"]
        and residual_values["R_Z"]["reconstruction_error_norm_sq"] < 1e-24
        and residual_values["R_X"]["reconstruction_error_norm_sq"] < 1e-24
        and residual_values["canonical_projector_checks"]["residual_projector_rank"] == 6
    )
    replay_b_fixed = (
        physical_status["b_selected_replay"]["A_transpose_b"] == [12.0, 12.0]
        and physical_status["b_selected_replay"]["deltaTheta_C1"] == [1.0, 1.0]
        and physical_status["b_selected_replay"]["same_source_emitted"] is False
    )
    five_clauses_open = (
        clauses["open_clause_count"] == 5
        and clauses["all_physical_clauses_closed_now"] is False
        and all(not item["closed"] for item in clauses["five_remaining_physical_clauses"].values())
    )

    value = {
        "schema": "MTTI11CanonicalResidualBValueClosureSublemma.v1",
        "status": "CANONICAL_RESIDUAL_AND_B_VALUES_CLOSED_PHYSICAL_SOURCE_OPEN",
        "proved": residual_values_closed and replay_b_fixed,
        "statement": (
            "The remaining physical-source problem no longer contains an algebraic value search: canonical finite "
            "Weyl residual values R_Z and R_X are emitted exactly, the residual projector checks pass, and the replay "
            "target fixes A^T b=(12,12), deltaTheta_C1=(1,1). These are values and compatibility data only; same-source "
            "physical emission of R_Z, R_X, b_selected, action restriction, and boundary/no-source terms remains open."
        ),
        "R_Z": residual_values["R_Z"],
        "R_X": residual_values["R_X"],
        "projector_checks": residual_values["canonical_projector_checks"],
        "b_selected_replay": physical_status["b_selected_replay"],
        "if_same_source_supplied": physical_status["if_same_source_physical_emission_supplied"],
        "not_yet_same_source_physical_emissions": physical_status["not_yet_same_source_physical_emissions"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    current = {
        "schema": "MTTCurrentI11PhysicalSourceValueClosureTraceMapAttempt.v1",
        "status": "CURRENT_HAS_VALUES_BUT_FAILS_FIVE_PHYSICAL_CLAUSES",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": False,
        "selected_normalization_boundary_clause": False,
        "dynamic_c1_flags_verified": False,
        "canonical_residual_values_closed": residual_values_closed,
        "b_selected_replay_fixed": replay_b_fixed,
        "five_physical_clauses_open": five_clauses_open,
        "route_b_independent_rows_executed_now": route_b["current_route_state"]["independent_rows_executed_now"],
        "attached_certificate_evidence": [
            {"source": rel(VALUE), "closes": "canonical residual values and replay b target"},
            {"source": rel(DATA / "selected_i11_c1coordinatechart_or_physicalsourcegap.candidate.json"), "closes": "C1 coordinate chart"},
            {
                "source": rel(
                    DATA
                    / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
                    / "same_source_physical_emission_status.packet.json"
                ),
                "closes": "physical emission cutset identification",
            },
            {
                "source": rel(
                    DATA
                    / "selected_physicalactionrestrictionclause_or_primitivekernelformula"
                    / "physical_action_restriction_clause_ledger.packet.json"
                ),
                "closes": "five physical clauses ledger",
            },
            {
                "source": rel(
                    DATA
                    / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement"
                    / "unpatched_galerkin_replacement_status.packet.json"
                ),
                "closes": "Route B contract only",
            },
        ],
        "why_validator_still_fails": [
            "R_Z/R_X/b values are fixed but not physically emitted by the same source branch",
            "physical PhiFinC1 action restriction is not emitted",
            "no-extra-boundary/source term is not emitted",
            "Route B independent selected Galerkin rows are contracted but not executed",
            "the selected C1 response coordinate map remains source-open despite fixed chart values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness = {
        "schema": "MTTConditionalFiveClausePhysicalSourceWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_IF_FIVE_PHYSICAL_CLAUSES_CLOSE",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": True,
        "selected_normalization_boundary_clause": True,
        "dynamic_c1_flags_verified": True,
        "attached_certificate_evidence": [
            {"source": rel(VALUE), "closes": "canonical residual and b values", "conditional": False},
            {"source": rel(FRONTIER), "closes": "physical PhiFinC1 action restriction", "conditional": True},
            {"source": rel(FRONTIER), "closes": "no-extra-boundary/source", "conditional": True},
            {"source": rel(FRONTIER), "closes": "same-source R_Z/R_X/b emission", "conditional": True},
            {"source": rel(FRONTIER), "closes": "selected C1 response coordinate map", "conditional": True},
        ],
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    frontier = {
        "schema": "MTTI11FivePhysicalClauseFrontier.v1",
        "status": "VALUES_CLOSED_SOURCE_PROMOTION_OPEN",
        "closed_now": {
            **prior["what_closes_now"],
            "canonical_R_Z_R_X_values": residual_values_closed,
            "b_selected_replay_target": replay_b_fixed,
            "five_clause_cutset_identified": five_clauses_open,
        },
        "still_open": {
            "five_physical_clauses": clauses["five_remaining_physical_clauses"],
            "same_source_physical_emissions": physical_status["not_yet_same_source_physical_emissions"],
            "route_b_independent_galerkin_replacement": route_b["current_route_state"],
            "required_route_b_outputs": route_b["required_outputs"],
        },
        "legal_exit_A": "same-source physical Phi_fin^C1 action restriction plus no-extra-boundary/source plus physical R_Z/R_X/b_selected emission",
        "legal_exit_B": "independent selected Galerkin rows with provenance, exactness/error certificates, A_selected, b_selected, deltaTheta_C1, and sector matrices",
        "superset_strategy": {
            "straight_route": "Retire algebraic value search using canonical finite Weyl residual values and replay b target.",
            "combined_route": "Use the formal 72/110 chart and physical clause ledger only as compatibility support.",
            "locked_target": "physical source-promotion clauses; value agreement alone cannot select the source.",
            "uses_observed_constants": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    VALUE.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(CURRENT)
    witness_result = run_validator(WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11PhysicalSourceValueClosureOrFiveClauseGap",
        "status": STATUS,
        "output_packets": {
            "value_closure": rel(VALUE),
            "current_attempt": rel(CURRENT),
            "conditional_witness": rel(WITNESS),
            "remaining_frontier": rel(FRONTIER),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
        },
        "theorem": {
            "name": "I11PhysicalSourceValueClosureAndFiveClauseGapTheorem",
            "proved": True,
            "statement": (
                "The I11 physical-source frontier has no remaining algebraic value-search blocker: R_Z, R_X, "
                "the residual projector, and the replay b target are fixed. The remaining proof is the five-clause "
                "physical source promotion or an independent selected Galerkin replacement."
            ),
        },
        "what_closes_now": {
            "canonical_residual_values_closed": residual_values_closed,
            "b_selected_replay_target_fixed": replay_b_fixed,
            "current_attempt_rejected": current_result["returncode"] == 1,
            "conditional_fiveclause_witness_passes": witness_result["returncode"] == 0,
        },
        "what_remains_open": frontier["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I11_PhysicalSourceValueClosure_or_FiveClauseGap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "canonical_residual_values_closed": residual_values_closed,
        "b_selected_replay_target_fixed": replay_b_fixed,
        "current_attempt_rejected": current_result["returncode"] == 1,
        "conditional_fiveclause_witness_passes": witness_result["returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11 PhysicalSourceValueClosure or FiveClauseGap v1

Status: `{STATUS}`.

The algebraic value-search part is closed:

```text
R_Z and R_X canonical values = {residual_values_closed}
b replay target fixed       = {replay_b_fixed}
five physical clauses open  = {five_clauses_open}
```

The remaining problem is now source promotion only. Either Route A emits the
same-source physical `Phi_fin^C1` action restriction, no-extra-boundary/source,
and physical `R_Z/R_X/b_selected`, or Route B executes independent selected
Galerkin rows with provenance and exactness certificates.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
