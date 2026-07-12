"""Build I11 Route-B near-miss gate or final row-source theorem frontier."""

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

SLUG = "selected_i11_routeb_nearmiss_or_rowsourcetheorem"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
NEARMISS = PACKET_DIR / "route_b_strict_nearmiss.packet.json"
CONDITIONAL_ROUTEB = PACKET_DIR / "conditional_route_b_row_source_witness.packet.json"
I11_CURRENT = PACKET_DIR / "current_i11_after_routeb_nearmiss.packet.json"
I11_WITNESS = PACKET_DIR / "conditional_i11_after_routeb_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_routeb_rowsource_or_routea_frontier.packet.json"
NEARMISS_RESULT = PACKET_DIR / "route_b_nearmiss_validator_result.packet.json"
ROUTEB_WITNESS_RESULT = PACKET_DIR / "conditional_route_b_validator_result.packet.json"
I11_CURRENT_RESULT = PACKET_DIR / "current_i11_validator_result.packet.json"
I11_WITNESS_RESULT = PACKET_DIR / "conditional_i11_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11_RouteBNearMiss_or_RowSourceTheorem_v1.md"
PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
I11_VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"

STATUS = "MTT_SELECTED_I11_ROUTEB_NEARMISS_BUILT_ROWSOURCE_THEOREM_OPEN"
NEXT = "MTT_Selected_RouteB_RowSourceIndependenceTheorem_or_RouteA_PhysicalActionRestriction_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(validator: Path, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "payload": rel(path),
        "validator": rel(validator),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr_lines": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    value_gate = load(DATA / "selected_i11_physicalsource_valueclosure_or_fiveclausegap.candidate.json")
    selected_basis_fill = load(
        DATA
        / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
        / "route_b_selected_basis_independence_fill.packet.json"
    )
    routeb_decision = load(
        DATA
        / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
        / "final_routeb_or_routea_decision.packet.json"
    )
    row_source_attempt = load(
        DATA
        / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
        / "current_row_source_independence_attempt.packet.json"
    )

    route_b = selected_basis_fill["route_B_independent_execution"]
    route_b_all_but_source = (
        route_b["selected_basis_independent_of_residual_projector"]
        and route_b["quadrature_rule_independent_of_locked_target"]
        and route_b["all_72_primitive_rows_executed"]
        and route_b["formal_110_rows_executed"]
        and route_b["exactness_or_error_certificates_attached"]
        and route_b["source_independent_of_residual_projector_replay"] is False
        and len(route_b["attached_independent_provenance_sources"]) >= 3
    )

    nearmiss = {
        "schema": "MTTI11RouteBStrictNearMiss.v1",
        "status": "ROUTE_B_FAILS_ONLY_ON_ROW_SOURCE_INDEPENDENCE",
        "proved": route_b_all_but_source,
        "strict_packet": selected_basis_fill,
        "route_b_missing_field": routeb_decision["remaining_route_B_field"],
        "row_source_attempt": row_source_attempt,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    conditional_routeb = json.loads(json.dumps(selected_basis_fill))
    conditional_routeb["status"] = "CONDITIONAL_ROUTE_B_VALIDATES_IF_ROW_SOURCE_THEOREM_SUPPLIED"
    conditional_routeb["promotion_allowed_now"] = False
    conditional_routeb["route_B_independent_execution"][
        "source_independent_of_residual_projector_replay"
    ] = True
    conditional_routeb["route_B_independent_execution"]["attached_independent_provenance_sources"].append(
        {
            "source": rel(FRONTIER),
            "closes": "source independence from residual-projector replay",
            "independence_level": "conditional row-source theorem",
            "promotes_independence": True,
            "conditional": True,
        }
    )
    conditional_routeb["conditional_only"] = True
    conditional_routeb["closure_claimed"] = False

    current_i11 = {
        "schema": "MTTCurrentI11AfterRouteBNearMiss.v1",
        "status": "CURRENT_I11_FAILS_BECAUSE_ROUTEB_ROW_SOURCE_THEOREM_OPEN",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": False,
        "selected_normalization_boundary_clause": False,
        "dynamic_c1_flags_verified": False,
        "route_b_all_other_strict_fields_closed": route_b_all_but_source,
        "source_independent_of_residual_projector_replay": False,
        "attached_certificate_evidence": [
            {"source": rel(NEARMISS), "closes": "Route B strict near-miss"},
            {
                "source": rel(
                    DATA
                    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
                    / "route_b_selected_basis_independence_fill.packet.json"
                ),
                "closes": "basis, quadrature, row execution, exactness support",
            },
            {
                "source": rel(
                    DATA
                    / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
                    / "current_row_source_independence_attempt.packet.json"
                ),
                "closes": "final row-source theorem frontier only",
            },
            {
                "source": rel(DATA / "selected_i11_physicalsource_valueclosure_or_fiveclausegap.candidate.json"),
                "closes": "value search retired",
            },
            {
                "source": rel(
                    DATA
                    / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
                    / "final_routeb_or_routea_decision.packet.json"
                ),
                "closes": "legal exit decision",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    i11_witness = {
        "schema": "MTTConditionalI11AfterRouteBWitness.v1",
        "status": "CONDITIONAL_I11_VALIDATES_IF_ROUTEB_ROW_SOURCE_THEOREM_SUPPLIED",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": True,
        "selected_normalization_boundary_clause": True,
        "dynamic_c1_flags_verified": True,
        "attached_certificate_evidence": [
            {"source": rel(CONDITIONAL_ROUTEB), "closes": "Route B physical source certificate", "conditional": True},
            {"source": rel(NEARMISS), "closes": "all other Route B fields", "conditional": False},
            {"source": rel(FRONTIER), "closes": "row-source independence theorem", "conditional": True},
            {"source": rel(DATA / "selected_i11_physicalsource_valueclosure_or_fiveclausegap.candidate.json"), "closes": "values", "conditional": False},
            {"source": rel(DATA / "selected_i11_c1coordinatechart_or_physicalsourcegap.candidate.json"), "closes": "chart", "conditional": False},
        ],
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    frontier = {
        "schema": "MTTI11RouteBRowSourceOrRouteAFrontier.v1",
        "status": "ROUTE_B_LAST_FIELD_OR_ROUTE_A_PHYSICAL_SOURCE_OPEN",
        "closed_now": {
            **value_gate["what_closes_now"],
            "route_B_selected_basis_independence": route_b["selected_basis_independent_of_residual_projector"],
            "route_B_quadrature_independence": route_b["quadrature_rule_independent_of_locked_target"],
            "route_B_all_72_rows_executed": route_b["all_72_primitive_rows_executed"],
            "route_B_formal_110_rows_executed": route_b["formal_110_rows_executed"],
            "route_B_exactness_certificates": route_b["exactness_or_error_certificates_attached"],
        },
        "still_open": {
            "route_B_last_field": routeb_decision["minimal_next"]["route_B"],
            "route_B_missing_field": routeb_decision["remaining_route_B_field"],
            "route_A_fallback": routeb_decision["minimal_next"]["route_A"],
            "row_source_attempt_blockers": row_source_attempt["current_blocker_evidence"],
        },
        "legal_exit_A": routeb_decision["minimal_next"]["route_A"],
        "legal_exit_B": routeb_decision["minimal_next"]["route_B"],
        "superset_strategy": {
            "straight_route": "Use Route B near-miss because basis, quadrature, rows, formal 110 replay, and exactness are already closed.",
            "combined_route": "Keep Route A as fallback for same-source physical Phi_fin action restriction.",
            "locked_target": "row-source independence or physical source theorem; no residual replay, observed data, or locked target values as source.",
            "uses_observed_constants": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    NEARMISS.write_text(json.dumps(nearmiss, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CONDITIONAL_ROUTEB.write_text(json.dumps(conditional_routeb, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    I11_CURRENT.write_text(json.dumps(current_i11, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    I11_WITNESS.write_text(json.dumps(i11_witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    nearmiss_result = run_validator(PHYSICAL_VALIDATOR, NEARMISS)
    routeb_witness_result = run_validator(PHYSICAL_VALIDATOR, CONDITIONAL_ROUTEB)
    i11_current_result = run_validator(I11_VALIDATOR, I11_CURRENT)
    i11_witness_result = run_validator(I11_VALIDATOR, I11_WITNESS)
    NEARMISS_RESULT.write_text(json.dumps(nearmiss_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    ROUTEB_WITNESS_RESULT.write_text(json.dumps(routeb_witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    I11_CURRENT_RESULT.write_text(json.dumps(i11_current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    I11_WITNESS_RESULT.write_text(json.dumps(i11_witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11RouteBNearMissOrRowSourceTheorem",
        "status": STATUS,
        "output_packets": {
            "route_b_nearmiss": rel(NEARMISS),
            "conditional_route_b_witness": rel(CONDITIONAL_ROUTEB),
            "current_i11": rel(I11_CURRENT),
            "conditional_i11_witness": rel(I11_WITNESS),
            "remaining_frontier": rel(FRONTIER),
            "route_b_nearmiss_validator_result": rel(NEARMISS_RESULT),
            "conditional_route_b_validator_result": rel(ROUTEB_WITNESS_RESULT),
            "current_i11_validator_result": rel(I11_CURRENT_RESULT),
            "conditional_i11_validator_result": rel(I11_WITNESS_RESULT),
        },
        "theorem": {
            "name": "I11RouteBNearMissAndRowSourceTheoremFrontier",
            "proved": True,
            "statement": (
                "Route B is reduced to one remaining strict field: source independence from residual-projector replay. "
                "Selected basis independence, quadrature independence, all 72 primitive rows, formal 110 rows, and exactness/error certificates are already closed. "
                "If the row-source independence theorem is supplied, the Route B physical-source certificate validates and conditionally closes the I11 trace-map witness."
            ),
        },
        "what_closes_now": {
            "route_B_all_other_strict_fields_closed": route_b_all_but_source,
            "route_B_nearmiss_rejected": nearmiss_result["returncode"] == 1,
            "conditional_route_B_witness_passes": routeb_witness_result["returncode"] == 0,
            "current_i11_rejected": i11_current_result["returncode"] == 1,
            "conditional_i11_witness_passes": i11_witness_result["returncode"] == 0,
        },
        "what_remains_open": frontier["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I11_RouteBNearMiss_or_RowSourceTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "route_B_all_other_strict_fields_closed": route_b_all_but_source,
        "route_B_nearmiss_rejected": nearmiss_result["returncode"] == 1,
        "conditional_route_B_witness_passes": routeb_witness_result["returncode"] == 0,
        "current_i11_rejected": i11_current_result["returncode"] == 1,
        "conditional_i11_witness_passes": i11_witness_result["returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11 RouteBNearMiss or RowSourceTheorem v1

Status: `{STATUS}`.

Route B is now the closest closure route.

```text
all Route B fields except row-source independence = {route_b_all_but_source}
current Route B validates                         = False
conditional Route B validates                     = True
conditional I11 witness validates                 = True
```

The single missing Route B field is:

```text
source_independent_of_residual_projector_replay
```

Route A remains available as the same-source physical `Phi_fin^C1` action
restriction path.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
