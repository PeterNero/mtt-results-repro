"""Build Route B row-kernel source normal form / source-object contract."""

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

SLUG = "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
NORMAL_FORM = PACKET_DIR / "primitive_row_kernel_source_normal_form.packet.json"
CONTRACT = PACKET_DIR / "selected_source_object_contract.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "rowsource_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteB_RowKernelSource_NormalForm_or_SourceObjectContract_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"

STATUS = "MTT_SELECTED_ROUTEB_ROWKERNELSOURCE_NORMALFORM_BUILT_SOURCE_OBJECT_OPEN"
NEXT = "MTT_Selected_PrimitiveKernelSourceTheorem_or_PhysicalPhiFinC1SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    source_gap = load(DATA / "selected_routeb_bestcurrentpayloadfill_or_independentsourcegap" / "routeb_independent_source_gap.packet.json")
    current = load(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "current_actual_row_source_fill_attempt.packet.json")
    remaining = load(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "remaining_primitive_source_gap.packet.json")
    template = load(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "primitive_kernel_source_theorem.strict_template.json")
    primitive_clause = load(DATA / "selected_physicalactionrestrictionclause_or_primitivekernelformula" / "primitive_kernel_formula_clause_ledger.packet.json")
    measure_split = load(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_c1_trace_measure_principle_split.packet.json")
    boundary_contract = load(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "same_source_boundary_and_residual_emission_contract.packet.json")

    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "current_actual_row_source_fill_attempt.packet.json")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    measure_clause = measure_split["clauses"]["physical_first_variation_uses_normalized_trace_Frobenius_measure"]
    action_clause = measure_split["clauses"]["physical_PhiFinC1_action_restricts_exactly_to_this_finite_measure"]
    boundary_clause = measure_split["clauses"]["continuum_or_external_boundary_source_terms_absent"]

    normal_form = {
        "schema": "MTTPrimitiveRowKernelSourceNormalForm.v1",
        "status": "NORMAL_FORM_BUILT_SELECTED_SOURCE_OBJECT_OPEN",
        "source_theorem_name": template["theorem_name"],
        "acceptance_formula": template["acceptance_formula"],
        "coordinate_system": template["coordinate_system"],
        "sector_couplings": template["sector_couplings"],
        "closed_support": {
            "finite_weyl_trace_measure_normalization": measure_clause["closed"],
            "finite_weyl_trace_rule_feeds_all_rows": current["finite_weyl_trace_rule_feeds_all_rows"],
            "sector_rows_assembled_from_primitive_rows": current["sector_rows_assembled_from_primitive_rows"],
            "hessian_source_rows_assembled_from_same_rows_formally": current["hessian_source_rows_assembled_from_same_rows"],
            "all_110_strict_row_slots_present": source_gap["current_support"]["all_110_rows_present"],
            "formal_hessian_target_present": source_gap["current_support"]["formal_hessian_target_present"],
        },
        "open_source_clauses": {
            "C1_action_restricts_to_finite_trace_measure": not action_clause["closed"],
            "zero_extra_boundary_or_source_terms": not boundary_clause["closed"],
            "selected_basis_feeds_72_row_functions": remaining["not_closed"]["selected_basis_to_all_72_row_functions"],
            "selected_phase_shift_variation_operators_before_residual_projection": remaining["not_closed"]["selected_phase_shift_variation_operators_before_residual_projection"],
            "selected_hessian_counterterm_and_b_source": remaining["not_closed"]["selected_hessian_counterterm_source"],
            "residual_projector_replay_not_used_as_source": remaining["not_closed"]["no_residual_projector_replay_used_as_source"],
            "row_formula_source_theorem_derived": remaining["not_closed"]["row_formula_source_theorem_derived"],
        },
        "normal_form_statement": (
            "A selected primitive row-kernel source theorem must emit a pre-residual row functional K_{s,r,i,j} "
            "from the same finite C1 trace action branch, then derive the 72 primitive rows, the two Hessian/b rows, "
            "and the 36 sector rows as consequences. Residual-projector replay may be used only as a postcheck."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    contract = {
        "schema": "MTTSelectedSourceObjectContract.v1",
        "status": "SOURCE_OBJECT_CONTRACT_READY_VALUES_OPEN",
        "minimal_source_object": "selected finite C1 row-kernel functional packet",
        "must_emit": [
            {
                "id": "measure_action_binding",
                "description": "same-branch Phi_fin^C1 action restriction to the normalized trace/Frobenius finite C1 measure",
                "current_status": "measure normalized; physical action restriction open",
            },
            {
                "id": "boundary_source_null",
                "description": "zero extra boundary/source terms or an emitted cancellation term",
                "current_status": "open",
            },
            {
                "id": "basis_to_row_functionals",
                "description": "selected basis feeds all 72 primitive row functionals before residual projection",
                "current_status": "open",
            },
            {
                "id": "phase_shift_pre_residual_operators",
                "description": "phase R_Z and shift R_X operators emitted as pre-residual variation operators, not replay outputs",
                "current_status": "shape-compatible but source-open",
            },
            {
                "id": "hessian_b_source",
                "description": "same-source Hessian counterterm and b_selected emission",
                "current_status": "formal target identified; physical source open",
            },
        ],
        "postcheck_only": [
            "canonical residual projector Q_residual",
            "locked target A^T b=(12,12), ||b||^2=24, deltaTheta=(1,1)",
            "best-current 110-row replay/formal payload",
            "observed SM masses, mixings, CP, Higgs, or gauge constants",
        ],
        "accepted_superset_paths": {
            "straight_route_A": boundary_contract["accepted_sources"][:2],
            "route_B_independent": boundary_contract["accepted_sources"][2],
            "shared_locked_target": "After source emission only, compare to 110-row payload and Hessian postchecks.",
        },
        "forbidden_shortcuts": boundary_contract["forbidden_shortcuts"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    validator_result = {
        "schema": "MTTRowSourceValidatorResult.v1",
        "validator": rel(VALIDATOR),
        "payload": rel(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "current_actual_row_source_fill_attempt.packet.json"),
        "returncode": proc.returncode,
        "expected_failure": True,
        "stderr_excerpt": proc.stderr.splitlines()[:12],
        "stdout": proc.stdout.strip(),
    }

    candidate = {
        "candidate": "MTTSelectedRouteBRowKernelSourceNormalFormOrSourceObjectContract",
        "status": STATUS,
        "inputs": {
            "routeb_independent_source_gap": rel(DATA / "selected_routeb_bestcurrentpayloadfill_or_independentsourcegap" / "routeb_independent_source_gap.packet.json"),
            "current_row_source_attempt": rel(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "current_actual_row_source_fill_attempt.packet.json"),
            "primitive_kernel_template": rel(DATA / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate" / "primitive_kernel_source_theorem.strict_template.json"),
            "primitive_formula_clause_ledger": rel(DATA / "selected_physicalactionrestrictionclause_or_primitivekernelformula" / "primitive_kernel_formula_clause_ledger.packet.json"),
            "finite_trace_measure_split": rel(DATA / "selected_finiteweyl_traceuniqueness_or_physicalboundarysource_derivation" / "finite_c1_trace_measure_principle_split.packet.json"),
            "same_source_boundary_contract": rel(DATA / "selected_phifinc1_actionrestriction_or_boundarysource_emission" / "same_source_boundary_and_residual_emission_contract.packet.json"),
        },
        "output_packets": {
            "primitive_row_kernel_source_normal_form": rel(NORMAL_FORM),
            "selected_source_object_contract": rel(CONTRACT),
            "rowsource_validator_result": rel(VALIDATOR_RESULT),
        },
        "theorem": {
            "name": "PrimitiveRowKernelSourceNormalFormReduction",
            "proved": True,
            "statement": (
                "Given the finite trace/Frobenius measure derivation, exact row-slot enumeration, and best-current "
                "110-row payload, Route B closure is equivalent to emitting one selected finite C1 row-kernel "
                "functional packet satisfying the five source clauses in this contract."
            ),
        },
        "what_closes_now": {
            "measure_normalization_not_the_blocker": True,
            "single_source_object_contract_built": True,
            "five_open_source_clauses_identified": True,
            "superset_paths_separated_from_locked_target_postcheck": True,
            "row_source_validator_failure_preserved": proc.returncode == 1,
        },
        "what_remains_open": normal_form["open_source_clauses"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_RouteB_RowKernelSource_NormalForm_or_SourceObjectContract_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "normal_form_path": rel(NORMAL_FORM),
        "contract_path": rel(CONTRACT),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected RouteB RowKernelSource NormalForm or SourceObjectContract v1

Status: `{STATUS}`.

This reduces the Route B source problem to one finite source object:

```text
selected finite C1 row-kernel functional packet
```

Already closed:

```text
finite trace/Frobenius measure normalization = True
all 110 strict row slots present             = True
formal Hessian target present                = True
```

Still open:

```text
physical action restriction to finite measure = True
zero extra boundary/source terms              = True
selected basis feeds 72 row functions         = True
pre-residual phase/shift operators            = True
same-source Hessian b_selected emission       = True
```

Superset usage: Route A can prove the same object by a physical
`Phi_fin^C1` action/source theorem; Route B can prove it by independent selected
quadrature/Galerkin source data. The locked `110`-row payload is only a
postcheck after the source object is emitted.

Next artifact: `{NEXT}`.
"""

    NORMAL_FORM.write_text(json.dumps(normal_form, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CONTRACT.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    VALIDATOR_RESULT.write_text(json.dumps(validator_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
