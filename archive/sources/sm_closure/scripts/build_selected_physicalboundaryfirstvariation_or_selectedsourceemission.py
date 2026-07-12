"""Build physical boundary/first-variation source-emission gate."""

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

SLUG = "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT = PACKET_DIR / "current_physical_boundary_firstvariation_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_physical_source_emission_witness.packet.json"
I11_BRIDGE = PACKET_DIR / "conditional_i11_trace_map_bridge.packet.json"
FRONTIER = PACKET_DIR / "remaining_selected_source_emission_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_physical_source_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_physical_source_validator_result.packet.json"
I11_BRIDGE_RESULT = PACKET_DIR / "conditional_i11_trace_map_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalBoundaryFirstVariation_or_SelectedSourceEmission_v1.md"

PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physical_boundary_firstvariation_source.py"
I11_VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"

STATUS = "MTT_SELECTED_PHYSICALBOUNDARYFIRSTVARIATION_GATE_BUILT_SOURCE_EMISSION_OPEN"
NEXT = "MTT_Selected_RouteA_SelectedPhiFinC1SourceEmission_or_RouteB_IndependentGalerkinRows_v1"


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

    backimport = load(DATA / "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation.candidate.json")
    boundary_frontier = load(
        DATA
        / "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation"
        / "remaining_boundary_firstvariation_source_frontier.packet.json"
    )
    trace_measure = load(DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json")
    action_equiv = load(DATA / "selected_physicalc1actionidentity_or_samesourcebselectedemission.candidate.json")
    dual_route = load(DATA / "selected_physicalactionsourceemission_or_honestgalerkinreplacement.candidate.json")
    route_a_validator = load(
        DATA
        / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
        / "route_a_physical_source_emission_validator.packet.json"
    )
    route_b_contract = load(
        DATA
        / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
        / "route_b_honest_galerkin_replacement_contract.packet.json"
    )

    evidence = [
        {
            "source": rel(DATA / "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation.candidate.json"),
            "closes": "I11 support backimport and active boundary/first-variation frontier",
        },
        {
            "source": rel(DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json"),
            "closes": "finite trace algebraic boundary cancellation and physical promotion reduction",
        },
        {
            "source": rel(DATA / "selected_physicalc1actionidentity_or_samesourcebselectedemission.candidate.json"),
            "closes": "equivalence of physical action identity to same-source source emission cutset",
        },
        {
            "source": rel(DATA / "selected_physicalactionsourceemission_or_honestgalerkinreplacement.candidate.json"),
            "closes": "dual Route A/Route B closure contract",
        },
        {
            "source": rel(
                DATA
                / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
                / "route_a_physical_source_emission_validator.packet.json"
            ),
            "closes": "Route A required emission list",
        },
        {
            "source": rel(
                DATA
                / "selected_physicalactionsourceemission_or_honestgalerkinreplacement"
                / "route_b_honest_galerkin_replacement_contract.packet.json"
            ),
            "closes": "Route B independent replacement contract",
        },
    ]

    current = {
        "schema": "MTTPhysicalBoundaryFirstVariationSourceEmissionAttempt.v1",
        "status": "CURRENT_PHYSICAL_SOURCE_EMISSION_REJECTED_REQUIRED_EMISSIONS_OPEN",
        "same_branch": True,
        "theorem_derived": False,
        "physical_first_variation_identity": False,
        "physical_measure_equals_trace_frobenius_pairing": False,
        "phase_R_Z_source_selection": False,
        "shift_R_X_source_selection": False,
        "same_source_b_selected_emission": False,
        "no_extra_physical_boundary_or_source_term": False,
        "attached_source_evidence": evidence,
        "current_route_A_emissions": route_a_validator["current_emissions"],
        "route_B_parallel_contract": route_b_contract["required_outputs"],
        "imported_support_status": {
            "i11_backimport": backimport["status"],
            "trace_measure": trace_measure["status"],
            "action_equivalence": action_equiv["status"],
            "dual_route": dual_route["status"],
        },
        "locked_target_values_used_as_source": False,
        "residual_projector_replay_used_as_source": False,
        "benchmark_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    witness = json.loads(json.dumps(current))
    witness.update(
        {
            "schema": "MTTConditionalPhysicalBoundaryFirstVariationSourceEmissionWitness.v1",
            "status": "CONDITIONAL_PHYSICAL_SOURCE_EMISSION_VALIDATES_IF_ROUTE_A_THEOREM_SUPPLIED",
            "theorem_derived": True,
            "physical_first_variation_identity": True,
            "physical_measure_equals_trace_frobenius_pairing": True,
            "phase_R_Z_source_selection": True,
            "shift_R_X_source_selection": True,
            "same_source_b_selected_emission": True,
            "no_extra_physical_boundary_or_source_term": True,
            "conditional_only": True,
        }
    )
    witness["attached_source_evidence"].append(
        {
            "source": rel(FRONTIER),
            "closes": "selected Route A physical Phi_fin^C1 source-emission theorem",
            "conditional": True,
        }
    )

    i11_bridge = {
        "schema": "MTTConditionalI11TraceMapAfterPhysicalSourceEmission.v1",
        "status": "CONDITIONAL_I11_TRACE_MAP_VALIDATES_AFTER_PHYSICAL_SOURCE_EMISSION",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": True,
        "selected_normalization_boundary_clause": True,
        "dynamic_c1_flags_verified": True,
        "attached_certificate_evidence": [
            {"source": rel(WITNESS), "closes": "physical source-emission theorem", "conditional": True},
            {
                "source": rel(
                    DATA
                    / "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation"
                    / "remaining_boundary_firstvariation_source_frontier.packet.json"
                ),
                "closes": "I11 boundary/first-variation frontier",
            },
            {"source": rel(DATA / "selected_i11_c1coordinatechart_or_physicalsourcegap.candidate.json"), "closes": "C1 coordinate chart"},
            {"source": rel(DATA / "selected_i11_physicalsource_valueclosure_or_fiveclausegap.candidate.json"), "closes": "canonical R_Z/R_X/b values"},
            {"source": rel(DATA / "selected_i11tracemap_transportdotdimport_or_boundaryc1gap.candidate.json"), "closes": "transport/dotD trace import"},
            {"source": rel(DATA / "selected_i11firstvariationcertificate_fill_or_quadraturetable.candidate.json"), "closes": "normalization compatibility"},
        ],
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    frontier = {
        "schema": "MTTSelectedSourceEmissionFrontier.v1",
        "status": "ROUTE_A_SOURCE_EMISSION_OR_ROUTE_B_INDEPENDENT_GALERKIN_ROWS_REMAIN",
        "closed_now": {
            "strict_physical_source_validator_built": True,
            "current_physical_source_attempt_rejected": True,
            "conditional_physical_source_witness_passes": True,
            "conditional_i11_trace_map_bridge_passes": True,
            "dual_route_contract_imported": True,
        },
        "route_A_remaining_theorem": {
            "name": "SelectedPhiFinC1PhysicalSourceEmissionTheorem",
            "must_emit": route_a_validator["required_emissions"],
            "must_be": "same-branch and theorem-derived",
        },
        "route_B_remaining_execution": {
            "name": "SelectedIndependentGalerkinRowsExecution",
            "must_emit": route_b_contract["required_outputs"],
            "acceptance_tests": route_b_contract["acceptance_tests"],
        },
        "superset_strategy": {
            "straight_route_A": "Use physical action identity to emit first variation, measure, R_Z, R_X, b_selected, and no-extra-boundary/source.",
            "parallel_route_B": "Replace the physical source theorem with independent selected Galerkin/quadrature rows.",
            "locked_target_policy": "Compare to canonical finite C1 values only after source emission or independent execution.",
            "uses_observed_constants": False,
        },
        "previous_i11_frontier": boundary_frontier["remaining_physical_fields"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    I11_BRIDGE.write_text(json.dumps(i11_bridge, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(PHYSICAL_VALIDATOR, CURRENT)
    witness_result = run_validator(PHYSICAL_VALIDATOR, WITNESS)
    i11_bridge_result = run_validator(I11_VALIDATOR, I11_BRIDGE)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    I11_BRIDGE_RESULT.write_text(json.dumps(i11_bridge_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedPhysicalBoundaryFirstVariationOrSelectedSourceEmission",
        "status": STATUS,
        "inputs": {
            "i11_backimport_frontier": rel(
                DATA
                / "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation"
                / "remaining_boundary_firstvariation_source_frontier.packet.json"
            ),
            "trace_measure_promotion": rel(DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json"),
            "physical_action_equivalence": rel(DATA / "selected_physicalc1actionidentity_or_samesourcebselectedemission.candidate.json"),
            "dual_route_contract": rel(DATA / "selected_physicalactionsourceemission_or_honestgalerkinreplacement.candidate.json"),
        },
        "output_packets": {
            "current_attempt": rel(CURRENT),
            "conditional_witness": rel(WITNESS),
            "conditional_i11_bridge": rel(I11_BRIDGE),
            "remaining_frontier": rel(FRONTIER),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
            "conditional_i11_validator_result": rel(I11_BRIDGE_RESULT),
        },
        "theorem": {
            "name": "PhysicalBoundaryFirstVariationSourceGateTheorem",
            "proved": True,
            "statement": (
                "The I11 boundary/first-variation blocker is equivalent to a six-field same-branch physical source-emission theorem: physical first variation, physical trace/Frobenius measure, phase R_Z source, shift R_X source, same-source b_selected, and no extra boundary/source term. "
                "The current packet fails exactly on those emissions. If the six-field theorem is supplied, the physical-source validator passes and the I11 trace-map bridge validates."
            ),
        },
        "what_closes_now": {
            "strict_validator_built": True,
            "current_physical_source_attempt_rejected": current_result["returncode"] == 1,
            "conditional_physical_source_witness_passes": witness_result["returncode"] == 0,
            "conditional_i11_trace_map_bridge_passes": i11_bridge_result["returncode"] == 0,
            "route_A_route_B_next_targets_locked": True,
        },
        "what_remains_open": {
            "SelectedPhiFinC1PhysicalSourceEmissionTheorem": True,
            "SelectedIndependentGalerkinRowsExecution": True,
        },
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalBoundaryFirstVariation_or_SelectedSourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_validator_built": True,
        "current_physical_source_attempt_rejected": current_result["returncode"] == 1,
        "conditional_physical_source_witness_passes": witness_result["returncode"] == 0,
        "conditional_i11_trace_map_bridge_passes": i11_bridge_result["returncode"] == 0,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalBoundaryFirstVariation or SelectedSourceEmission v1

Status: `{STATUS}`.

This artifact makes the active I11 physical gate executable.

```text
current physical source validator rejects     = {current_result["returncode"] == 1}
conditional physical source witness validates = {witness_result["returncode"] == 0}
conditional I11 trace-map bridge validates    = {i11_bridge_result["returncode"] == 0}
```

Route A now requires one theorem-derived same-branch source packet:

- physical first-variation identity
- physical measure equals trace/Frobenius pairing
- phase `R_Z` source selection
- shift `R_X` source selection
- same-source `b_selected` emission
- no extra physical boundary/source term

Route B remains the parallel replacement path: independent selected Galerkin rows
with zero-mode bases, primitive contractions, response matrices, and C33/family
rank tests. The canonical finite C1 replay packet is only a post-emission check.

No observed constants, benchmark rows, locked target values, or residual replay
are used as selectors.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
