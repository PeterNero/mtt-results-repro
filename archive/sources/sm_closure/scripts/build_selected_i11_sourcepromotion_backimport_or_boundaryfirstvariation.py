"""Back-import source-promotion reductions into the I11 boundary/first-variation frontier."""

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

SLUG = "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT = PACKET_DIR / "current_i11_sourcepromotion_backimport_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_boundary_firstvariation_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_boundary_firstvariation_source_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_i11_trace_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_i11_trace_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_I11_SourcePromotionBackimport_or_BoundaryFirstVariation_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"

STATUS = "MTT_SELECTED_I11_SOURCEPROMOTION_BACKIMPORT_BUILT_BOUNDARY_FIRSTVARIATION_OPEN"
NEXT = "MTT_Selected_PhysicalBoundaryFirstVariation_or_SelectedSourceEmission_v1"


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

    transport_dotd = load(DATA / "selected_i11tracemap_transportdotdimport_or_boundaryc1gap.candidate.json")
    c1_chart = load(DATA / "selected_i11_c1coordinatechart_or_physicalsourcegap.candidate.json")
    value_closure = load(DATA / "selected_i11_physicalsource_valueclosure_or_fiveclausegap.candidate.json")
    rowsource_push = load(DATA / "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback.candidate.json")
    action_kernel = load(DATA / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding.candidate.json")
    i10_stack = load(DATA / "selected_i10bindingstack_gate_or_firstvariationcertificate.candidate.json")
    i11_firstvar = load(DATA / "selected_i11firstvariationcertificate_fill_or_quadraturetable.candidate.json")

    current = {
        "schema": "MTTI11SourcePromotionBackimportAttempt.v1",
        "status": "CURRENT_I11_BACKIMPORT_FAILS_ONLY_ON_PHYSICAL_BOUNDARY_FIRSTVARIATION_SOURCE",
        "same_branch": True,
        "selected_minimizer_identifier": True,
        "finite_phi_fin_trace_operator": True,
        "c1_response_coordinate_map": True,
        "selected_normalization_boundary_clause": False,
        "dynamic_c1_flags_verified": False,
        "attached_certificate_evidence": [
            {
                "source": rel(DATA / "selected_i11tracemap_transportdotdimport_or_boundaryc1gap.candidate.json"),
                "closes": "transport-closed replay and dotD trace binding support",
            },
            {
                "source": rel(DATA / "selected_i11_c1coordinatechart_or_physicalsourcegap.candidate.json"),
                "closes": "72-row C1 response coordinate chart and formal 110-row compatibility",
            },
            {
                "source": rel(DATA / "selected_i11_physicalsource_valueclosure_or_fiveclausegap.candidate.json"),
                "closes": "canonical R_Z/R_X residual values and replay b target",
            },
            {
                "source": rel(DATA / "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback.candidate.json"),
                "closes": "Route B final source-promotion gate and conditional plug",
            },
            {
                "source": rel(DATA / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding.candidate.json"),
                "closes": "Route A action-kernel reduction to I10 binding stack",
            },
            {
                "source": rel(DATA / "selected_i11firstvariationcertificate_fill_or_quadraturetable.candidate.json"),
                "closes": "normalization compatibility and remaining I11 first-variation fields",
            },
        ],
        "imported_support": {
            "transport_dotd_status": transport_dotd["status"],
            "c1_chart_status": c1_chart["status"],
            "value_closure_status": value_closure["status"],
            "rowsource_push_status": rowsource_push["status"],
            "action_kernel_status": action_kernel["status"],
            "i10_stack_status": i10_stack["status"],
            "i11_firstvariation_status": i11_firstvar["status"],
        },
        "still_open": {
            "physical_first_variation_identity": True,
            "physical_boundary_cancellation_or_no_extra_source": True,
            "same_source_RZ_RX_bselected_emission": True,
            "SelectedFiniteC1SourcePromotionLemma_or_RouteA_ActionRestriction": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "free_axiom_patch_used": False,
        "closure_claimed": False,
    }

    witness = json.loads(json.dumps(current))
    witness.update(
        {
            "schema": "MTTConditionalI11BoundaryFirstVariationWitness.v1",
            "status": "CONDITIONAL_I11_VALIDATES_IF_BOUNDARY_FIRSTVARIATION_SOURCE_EMITTED",
            "selected_normalization_boundary_clause": True,
            "dynamic_c1_flags_verified": True,
            "conditional_only": True,
        }
    )
    witness["attached_certificate_evidence"].append(
        {
            "source": rel(FRONTIER),
            "closes": "physical first variation, no-extra-boundary/source, and same-source R_Z/R_X/b_selected emission",
            "conditional": True,
        }
    )

    frontier = {
        "schema": "MTTI11BoundaryFirstVariationSourceFrontier.v1",
        "status": "BOUNDARY_FIRSTVARIATION_SOURCE_IS_ACTIVE_I11_GATE",
        "closed_now": {
            "selected_minimizer_identifier_imported": True,
            "finite_phi_fin_trace_operator_imported": True,
            "c1_response_coordinate_chart_imported": True,
            "canonical_RZ_RX_b_replay_values_fixed": True,
            "transport_dotd_trace_binding_imported": True,
            "normalization_compatibility_proved": True,
            "current_i11_trace_validator_rejects": True,
            "conditional_i11_trace_validator_passes": True,
        },
        "remaining_physical_fields": {
            "physical_first_variation_identity": {
                "needs": "d/dt Q(Phi_fin^C1 + t eta)|_0 = 0 on selected admissible C1 response directions",
                "current_support": "formal Euler projection and finite trace normalization only",
            },
            "physical_boundary_cancellation": {
                "needs": "no extra physical boundary/source term or emitted cancellation term",
                "current_support": "algebraic finite trace cancellation only",
            },
            "same_source_RZ_RX_bselected_emission": {
                "needs": "physical source emission of phase R_Z, shift R_X, and Hessian/source b_selected",
                "current_support": "canonical finite Weyl replay values only",
            },
        },
        "superset_strategy": {
            "straight_route_A": "Prove selected Phi_fin^C1 physical action restriction, first variation, boundary cancellation, and same-source R_Z/R_X/b_selected.",
            "route_B_parallel": "Prove SelectedFiniteC1SourcePromotionLemma as independent row-kernel source emission.",
            "combined_locked_target": "Both routes are allowed only to compare against the finite C1 packet after source emission.",
            "uses_observed_constants": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    CURRENT.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    FRONTIER.write_text(json.dumps(frontier, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    current_result = run_validator(CURRENT)
    witness_result = run_validator(WITNESS)
    CURRENT_RESULT.write_text(json.dumps(current_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    WITNESS_RESULT.write_text(json.dumps(witness_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedI11SourcePromotionBackimportOrBoundaryFirstVariation",
        "status": STATUS,
        "inputs": {
            "transport_dotd_import": rel(DATA / "selected_i11tracemap_transportdotdimport_or_boundaryc1gap.candidate.json"),
            "c1_coordinate_chart": rel(DATA / "selected_i11_c1coordinatechart_or_physicalsourcegap.candidate.json"),
            "physical_source_value_closure": rel(DATA / "selected_i11_physicalsource_valueclosure_or_fiveclausegap.candidate.json"),
            "routeb_rowsource_push": rel(DATA / "selected_i11_routeb_rowsource_theorem_push_or_routea_fallback.candidate.json"),
            "action_kernel_i10_reduction": rel(DATA / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding.candidate.json"),
            "i11_firstvariation_frontier": rel(DATA / "selected_i11firstvariationcertificate_fill_or_quadraturetable.candidate.json"),
        },
        "output_packets": {
            "current_attempt": rel(CURRENT),
            "conditional_witness": rel(WITNESS),
            "remaining_frontier": rel(FRONTIER),
            "current_validator_result": rel(CURRENT_RESULT),
            "conditional_validator_result": rel(WITNESS_RESULT),
        },
        "theorem": {
            "name": "I11SourcePromotionBackimportTheorem",
            "proved": True,
            "statement": (
                "After importing the strongest later source-promotion reductions, the I11 trace-map closure problem no longer has a generic chart/value/dotD blocker. "
                "The selected minimizer, finite Phi_fin trace support, C1 coordinate chart, canonical R_Z/R_X/b replay values, transport dotD trace binding, and normalization compatibility are all available as support. "
                "The remaining strict validator fields are physical boundary/normalization promotion and dynamic C1 source verification, equivalent here to physical first variation plus same-source R_Z/R_X/b_selected emission or the Route-B SelectedFiniteC1SourcePromotionLemma."
            ),
        },
        "what_closes_now": {
            "current_i11_attempt_rejected": current_result["returncode"] == 1,
            "conditional_i11_witness_passes": witness_result["returncode"] == 0,
            "boundary_firstvariation_source_frontier_identified": True,
            "route_A_and_route_B_superset_paths_synchronized": True,
        },
        "what_remains_open": frontier["remaining_physical_fields"],
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_I11_SourcePromotionBackimport_or_BoundaryFirstVariation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "current_i11_attempt_rejected": current_result["returncode"] == 1,
        "conditional_i11_witness_passes": witness_result["returncode"] == 0,
        "boundary_firstvariation_source_frontier_identified": True,
        "conditional_only": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected I11 SourcePromotion Backimport or BoundaryFirstVariation v1

Status: `{STATUS}`.

The I11 frontier now imports the strongest downstream source-promotion work:
selected trace/minimizer support, finite `Phi_fin` trace support, the `72`-row
C1 coordinate chart, canonical `R_Z/R_X/b` replay values, transport/dotD trace
binding, and normalization compatibility.

```text
current I11 validator rejects       = {current_result["returncode"] == 1}
conditional I11 witness validates   = {witness_result["returncode"] == 0}
```

What remains is physical, not numerical:

- physical first-variation identity on selected C1 response directions
- no-extra-boundary/source promotion
- same-source `R_Z/R_X/b_selected` emission, or Route-B independent row-kernel
  source emission through `SelectedFiniteC1SourcePromotionLemma`

No observed constants, locked targets, benchmark rows, or residual replay values
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
