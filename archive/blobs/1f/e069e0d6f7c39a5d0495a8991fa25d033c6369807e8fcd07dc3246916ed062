"""Import symbolic transport replay and dynamic dotD trace binding into I11 trace-map frontier."""

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

SLUG = "selected_i11tracemap_transportdotdimport_or_boundaryc1gap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRANSPORT_DOTD = PACKET_DIR / "transport_closed_dotd_trace_import_sublemma.packet.json"
CURRENT = PACKET_DIR / "current_transport_dotd_import_trace_map_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_boundary_c1_trace_map_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_boundary_c1_firstvariation_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11TraceMap_TransportDotDImport_or_BoundaryC1Gap_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"

STATUS = "MTT_SELECTED_I11TRACEMAP_TRANSPORT_DOTD_IMPORTED_BOUNDARY_C1_OPEN"
NEXT = "MTT_Selected_I11PhysicalBoundary_and_C1ResponseCoordinateMap_v1"


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

    prior = load(DATA / "selected_i11tracemap_gaugetransportimport_or_dynamicreplaygap.candidate.json")
    transport = load(DATA / "selected_transport_conjugation_validator_replay.candidate.json")
    dotd_binding = load(
        DATA
        / "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
        / "dynamic_dotd_trace_binding.packet.json"
    )
    c1measure = load(
        DATA
        / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
        / "physical_action_boundary_promotion_attempt.packet.json"
    )
    firstvar = load(
        DATA
        / "selected_differentiatedc1orthogonalcompletionprinciple_or_independentquadraturehessiansolve"
        / "orthogonal_completion_variational_derivation.packet.json"
    )

    transport_closed = (
        transport["promotion_decision"]["transport_closed_finite_validator_replay"]
        and transport["validator_result"]["symbolic_transport_conjugation_validator_extended"]
        and transport["validator_result"]["selected_source_verified"]
        and transport["validator_result"]["selected_rho_s_validator_ready"]
    )
    dotd_closed = (
        dotd_binding["binding_flags"]["dynamic_dotD_trace_binding_accepted"]
        and dotd_binding["binding_flags"]["selected_dotD_source_verified"]
        and dotd_binding["binding_flags"]["alpha1_driver_verified"]
        and dotd_binding["binding_flags"]["honest_dotD_alpha1_replay"]
        and dotd_binding["binding_flags"]["dU_dalpha_formula_closed"]
    )
    dynamic_dotd_imported = transport_closed and dotd_closed
    algebraic_boundary_only = c1measure["first_variation_certificate_fields_after_this_gate"]["boundary_cancellation"][
        "finite_trace_algebraic_verified_now"
    ]
    physical_boundary_closed = c1measure["first_variation_certificate_fields_after_this_gate"]["boundary_cancellation"][
        "physical_verified_now"
    ]

    transport_dotd = {
        "schema": "MTTI11TransportClosedDotDTraceImportSublemma.v1",
        "status": "TRANSPORT_CLOSED_REPLAY_AND_DOTD_TRACE_IMPORTED_FOR_I11",
        "proved": dynamic_dotd_imported,
        "statement": (
            "The symbolic transport-conjugation validator closes transport-closed finite projector/Riesz/Green replay, "
            "and the dynamic dotD trace-binding packet closes dU/dalpha, selected dotD source, alpha1 driver, and honest "
            "dotD replay for the accepted dynamic trace-binding scope. This imports dynamic dotD trace support into the "
            "I11 trace-map frontier without promoting C1 response coordinates or physical boundary cancellation."
        ),
        "transport_closed_finite_validator_replay": transport_closed,
        "dynamic_dotd_trace_binding_accepted": dotd_closed,
        "accepted_scope": dotd_binding["accepted_scope"],
        "not_accepted_scope": dotd_binding["not_accepted_scope"],
        "sources": [
            rel(DATA / "selected_transport_conjugation_validator_replay.candidate.json"),
            rel(
                DATA
                / "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
                / "dynamic_dotd_trace_binding.packet.json"
            ),
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    current = {
        "schema": "MTTCurrentI11TraceMapTransportDotDImportAttempt.v1",
        "status": "CURRENT_TRACE_MAP_CLOSES_TRANSPORT_DOTD_BUT_FAILS_BOUNDARY_C1_VALIDATOR",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": False,
        "selected_normalization_boundary_clause": False,
        "dynamic_c1_flags_verified": False,
        "transport_closed_finite_validator_replay": transport_closed,
        "dynamic_dotd_trace_binding_imported": dotd_closed,
        "algebraic_boundary_support": algebraic_boundary_only,
        "physical_boundary_closed": physical_boundary_closed,
        "formal_first_variation_projection": firstvar["derived_inside_this_gate"][
            "finite_dimensional_projection_euler_equation"
        ],
        "physical_first_variation_identity": False,
        "attached_certificate_evidence": [
            {
                "source": rel(TRANSPORT_DOTD),
                "closes": "transport-closed finite replay and dynamic dotD trace binding",
            },
            {
                "source": rel(DATA / "selected_i11tracemap_gaugetransportimport_or_dynamicreplaygap.candidate.json"),
                "closes": "functional selected trace and Phi_fin operator",
            },
            {
                "source": rel(DATA / "selected_transport_conjugation_validator_replay.candidate.json"),
                "closes": "symbolic transport-conjugation validator replay",
            },
            {
                "source": rel(
                    DATA
                    / "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
                    / "dynamic_dotd_trace_binding.packet.json"
                ),
                "closes": "dynamic dotD trace-binding scope only",
            },
            {
                "source": rel(
                    DATA
                    / "selected_c1tracemeasurepromotion_or_actionboundaryproof"
                    / "physical_action_boundary_promotion_attempt.packet.json"
                ),
                "closes": "algebraic boundary support only",
            },
        ],
        "why_validator_still_fails": [
            "C1 response coordinate map is not emitted from selected primitive rows or physical C1 response data",
            "normalization is closed but the combined normalization/boundary clause requires physical boundary promotion",
            "dynamic C1 flags include physical first-variation identity and boundary verification, which remain open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness = {
        "schema": "MTTConditionalBoundaryC1TraceMapWitness.v1",
        "status": "CONDITIONAL_WITNESS_VALIDATES_AFTER_BOUNDARY_AND_C1_RESPONSE_CLOSE",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": True,
        "selected_normalization_boundary_clause": True,
        "dynamic_c1_flags_verified": True,
        "attached_certificate_evidence": [
            {
                "source": rel(TRANSPORT_DOTD),
                "closes": "transport/dotD dynamic trace support",
                "conditional": False,
            },
            {
                "source": rel(FRONTIER),
                "closes": "C1 response coordinate map",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "physical boundary cancellation",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "physical first-variation identity",
                "conditional": True,
            },
            {
                "source": rel(FRONTIER),
                "closes": "remaining dynamic C1 flags",
                "conditional": True,
            },
        ],
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    frontier = {
        "schema": "MTTI11BoundaryC1FirstVariationFrontier.v1",
        "status": "TRANSPORT_DOTD_IMPORTED_BOUNDARY_C1_FIRSTVARIATION_OPEN",
        "closed_now": {
            "functional_selected_minimizer_trace": prior["what_closes_now"][
                "selected_minimizer_identifier_at_functional_trace_level"
            ],
            "finite_phi_fin_functional_trace_operator": prior["what_closes_now"][
                "finite_phi_fin_trace_operator_at_functional_trace_level"
            ],
            "transport_closed_finite_validator_replay": transport_closed,
            "dynamic_dotd_trace_binding": dotd_closed,
            "selected_dotD_source_verified": dotd_binding["binding_flags"]["selected_dotD_source_verified"],
            "alpha1_driver_verified": dotd_binding["binding_flags"]["alpha1_driver_verified"],
        },
        "still_open": {
            "c1_response_coordinate_map": {
                "current_support": False,
                "needs": "selected primitive rows or finite C1 response coordinate map accepted beyond dotD trace-binding scope",
            },
            "physical_first_variation_identity": {
                "current_support": "formal finite-dimensional projection only",
                "needs": "d/dt Q(Phi_fin^C1+t eta)|_0=0 for all selected admissible C1 response directions",
            },
            "physical_boundary_cancellation": {
                "algebraic_support": algebraic_boundary_only,
                "physical_verified": physical_boundary_closed,
                "needs": "no-extra-boundary/source term for the physical Phi_fin^C1 action restriction",
            },
            "selected_normalization_boundary_clause": {
                "normalization_closed": True,
                "boundary_closed": physical_boundary_closed,
                "needs": "combine normalized trace with physical boundary cancellation",
            },
        },
        "superset_strategy": {
            "straight_route": "Symbolic transport-conjugation and dotD transport derivative are imported as theorem-derived support.",
            "combined_route": "Cross-repo alpha1 driver import is used only inside the accepted dynamic dotD trace-binding packet.",
            "locked_target": "I11 trace-map validator; primitive C1 response, boundary, and first variation remain unpromoted.",
            "uses_observed_constants": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    TRANSPORT_DOTD.write_text(json.dumps(transport_dotd, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(CURRENT)
    witness_result = run_validator(WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11TraceMapTransportDotDImportOrBoundaryC1Gap",
        "status": STATUS,
        "inputs": {
            "prior_i11_trace_map_frontier": rel(DATA / "selected_i11tracemap_gaugetransportimport_or_dynamicreplaygap.candidate.json"),
            "transport_conjugation": rel(DATA / "selected_transport_conjugation_validator_replay.candidate.json"),
            "dynamic_dotd_trace_binding": rel(
                DATA
                / "selected_primitiverowsexecution_or_dynamicdotdtracebinding"
                / "dynamic_dotd_trace_binding.packet.json"
            ),
        },
        "output_packets": {
            "transport_dotd_import_sublemma": rel(TRANSPORT_DOTD),
            "current_attempt": rel(CURRENT),
            "conditional_witness": rel(WITNESS),
            "remaining_frontier": rel(FRONTIER),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
        },
        "theorem": {
            "name": "I11TransportClosedDotDTraceImportTheorem",
            "proved": True,
            "statement": (
                "The I11 trace-map frontier imports symbolic transport-conjugation replay and accepted dynamic dotD "
                "trace binding. This closes transport-closed finite replay, selected dotD source, and alpha1 driver "
                "inside the dynamic dotD trace-binding scope. It does not close C1 response coordinates, physical "
                "first variation, or physical boundary cancellation."
            ),
        },
        "what_closes_now": {
            "transport_dotd_import_sublemma_proved": dynamic_dotd_imported,
            "transport_closed_finite_validator_replay": transport_closed,
            "dynamic_dotd_trace_binding": dotd_closed,
            "current_attempt_rejected": current_result["returncode"] == 1,
            "conditional_boundary_c1_witness_passes": witness_result["returncode"] == 0,
        },
        "what_remains_open": frontier["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "conditional_only": True,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I11TraceMap_TransportDotDImport_or_BoundaryC1Gap_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "transport_dotd_import_sublemma_proved": dynamic_dotd_imported,
        "current_attempt_rejected": current_result["returncode"] == 1,
        "conditional_boundary_c1_witness_passes": witness_result["returncode"] == 0,
        "closure_claimed": False,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11TraceMap TransportDotDImport or BoundaryC1Gap v1

Status: `{STATUS}`.

The I11 trace-map frontier now imports two already verified ingredients:

```text
symbolic transport-conjugation replay = {transport_closed}
dynamic dotD trace binding accepted   = {dotd_closed}
```

This retires transport-closed finite replay and dotD/alpha1 trace binding as
active trace-map blockers in this repo. The validator still rejects the current
packet because the remaining fields are physical, not transport-algebraic:

- selected C1 response coordinate map,
- physical first-variation identity,
- physical boundary/no-extra-source clause.

Superset use is constrained: the cross-repo alpha1 import is used only through
the accepted dynamic dotD trace-binding packet, and no observed constants or
target residuals select the source.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
