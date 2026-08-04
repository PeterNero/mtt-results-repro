"""Build narrowed Phi_fin^C1 emission or independent Hessian quadrature source gate."""

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
SCRIPTS = ROOT / "scripts"

SLUG = "selected_phifinc1emission_or_independenthessianquadraturesource"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
VALIDATOR = SCRIPTS / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"
ATTEMPT = PACKET_DIR / "current_source_emission_attempt.packet.json"
VALIDATION = PACKET_DIR / "strict_source_emission_validator_result.packet.json"
ROUTE_A = PACKET_DIR / "route_a_phifinc1_source_emission.strict_template.json"
ROUTE_B = PACKET_DIR / "route_b_independent_hessian_quadrature_source.strict_template.json"
CUTSET = PACKET_DIR / "final_source_emission_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_PhiFinC1Emission_or_IndependentHessianQuadratureSource_v1.md"

PREVIOUS = DATA / "selected_hessiancountertermsource_bvector_theoremtemplate.candidate.json"
HESSIAN_TARGET = (
    DATA
    / "selected_hessiancountertermsource_bvector_theoremtemplate"
    / "hessian_bvector_formal_target.packet.json"
)
HESSIAN_TEMPLATE = (
    DATA
    / "selected_hessiancountertermsource_bvector_theoremtemplate"
    / "hessian_bvector_source_theorem.strict_template.json"
)
VARIATION_COMPAT = (
    DATA
    / "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
    / "variation_operator_shape_compatibility.packet.json"
)
ROW_SOURCE_ATTEMPT = (
    DATA
    / "selected_routeb_actualrowsourcefill_or_primitivetheoremtemplate"
    / "current_actual_row_source_fill_attempt.packet.json"
)
ROUTE_B_BASIS = (
    DATA
    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
    / "route_b_selected_basis_independence_fill.packet.json"
)

STATUS = "MTT_SELECTED_PHIFINC1EMISSION_OR_INDEPENDENTHESSIANQUADRATURESOURCE_BUILT_FINAL_VALIDATOR_OPEN"
NEXT = "MTT_Selected_FinalSourceEmissionActualFill_or_NoGoWitness_v1"


VALIDATOR_SOURCE = r'''"""Validate narrowed Phi_fin^C1 source emission or independent Hessian quadrature source."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROUTE_A_FIELDS = [
    "same_branch",
    "physical_phifin_c1_action_emitted",
    "finite_weyl_action_restriction_derived",
    "no_extra_boundary_or_source_term",
    "selected_phase_shift_variation_operators_pre_residual",
    "selected_hessian_counterterm_source",
    "same_source_b_selected_emitted",
    "row_formula_source_theorem_derived",
]

ROUTE_B_FIELDS = [
    "selected_basis_independent_of_residual_projector",
    "quadrature_rule_independent_of_locked_target",
    "all_72_primitive_rows_executed",
    "formal_110_rows_executed",
    "independent_hessian_quadrature_source_emitted",
    "selected_b_vector_source",
    "source_independent_of_residual_projector_replay",
    "exactness_or_error_certificates_attached",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence(node: dict[str, Any], key: str) -> list[Any]:
    value = node.get(key, [])
    return value if isinstance(value, list) else []


def validate(payload: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if payload.get("observed_data_used_as_selector") is not False:
        errors.append("observed_data_used_as_selector must be false")
    if payload.get("target_fitting_used") is not False:
        errors.append("target_fitting_used must be false")
    if payload.get("locked_target_values_used_as_source") is not False:
        errors.append("locked_target_values_used_as_source must be false")

    route_a = payload.get("route_A_phifinc1_source_emission", {})
    route_b = payload.get("route_B_independent_hessian_quadrature_source", {})

    missing_a = [field for field in ROUTE_A_FIELDS if route_a.get(field) is not True]
    missing_b = [field for field in ROUTE_B_FIELDS if route_b.get(field) is not True]
    evidence_a = evidence(route_a, "attached_same_branch_source_evidence")
    evidence_b = evidence(route_b, "attached_independent_quadrature_evidence")

    route_a_ok = not missing_a and len(evidence_a) >= 6
    route_b_ok = not missing_b and len(evidence_b) >= 5

    if missing_a:
        errors.append("Route A missing: " + ", ".join(missing_a))
    if len(evidence_a) < 6:
        errors.append("Route A needs at least six same-branch evidence sources")
    if missing_b:
        errors.append("Route B missing: " + ", ".join(missing_b))
    if len(evidence_b) < 5:
        errors.append("Route B needs at least five independent quadrature evidence sources")
    if not (route_a_ok or route_b_ok):
        errors.append("neither narrowed Route A nor narrowed Route B validates")
    return route_a_ok or route_b_ok, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_selected_phifinc1emission_or_independenthessianquadraturesource.py <packet.json>", file=sys.stderr)
        return 2
    ok, errors = validate(load(Path(argv[1])))
    if ok:
        print(f"PASS {argv[1]}")
        return 0
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
'''


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    VALIDATOR.write_text(VALIDATOR_SOURCE, encoding="utf-8")

    previous = load(PREVIOUS)
    hessian_target = load(HESSIAN_TARGET)
    hessian_template = load(HESSIAN_TEMPLATE)
    variation = load(VARIATION_COMPAT)
    row_attempt = load(ROW_SOURCE_ATTEMPT)
    route_b_basis = load(ROUTE_B_BASIS)

    route_a = {
        "schema": "MTTNarrowedRouteAPhiFinC1SourceEmission.v1",
        "status": "STRICT_TEMPLATE_READY_NOT_FILLED",
        "same_branch": False,
        "physical_phifin_c1_action_emitted": False,
        "finite_weyl_action_restriction_derived": False,
        "no_extra_boundary_or_source_term": False,
        "selected_phase_shift_variation_operators_pre_residual": False,
        "selected_hessian_counterterm_source": False,
        "same_source_b_selected_emitted": False,
        "row_formula_source_theorem_derived": False,
        "attached_same_branch_source_evidence": [],
    }

    route_b = {
        "schema": "MTTNarrowedRouteBIndependentHessianQuadratureSource.v1",
        "status": "STRICT_TEMPLATE_READY_NOT_EXECUTED",
        "selected_basis_independent_of_residual_projector": route_b_basis[
            "route_B_independent_execution"
        ]["selected_basis_independent_of_residual_projector"],
        "quadrature_rule_independent_of_locked_target": route_b_basis[
            "route_B_independent_execution"
        ]["quadrature_rule_independent_of_locked_target"],
        "all_72_primitive_rows_executed": row_attempt["closed_support_imported"][
            "all_72_row_values_exact"
        ],
        "formal_110_rows_executed": hessian_target["formal_110_rows_executed"],
        "independent_hessian_quadrature_source_emitted": False,
        "selected_b_vector_source": False,
        "source_independent_of_residual_projector_replay": False,
        "exactness_or_error_certificates_attached": row_attempt["closed_support_imported"][
            "all_72_row_exactness_certificates"
        ],
        "attached_independent_quadrature_evidence": [
            {
                "source": rel(ROUTE_B_BASIS),
                "closes": "selected basis and trace/quadrature independence support",
                "promotes_source_independence": False,
            },
            {
                "source": rel(HESSIAN_TARGET),
                "closes": "formal two-row Hessian target",
                "promotes_source_independence": False,
            },
        ],
    }

    attempt = {
        "schema": "MTTNarrowedPhiFinC1EmissionOrIndependentHessianQuadratureAttempt.v1",
        "status": "CURRENT_ATTEMPT_REJECTED_FINAL_SOURCE_EMISSION_OPEN",
        "route_A_phifinc1_source_emission": route_a,
        "route_B_independent_hessian_quadrature_source": route_b,
        "support_closed": {
            "variation_operator_shape_compatibility": variation[
                "compatible_with_72_slot_table"
            ],
            "formal_hessian_target_identified": True,
            "A_transpose_b": hessian_target["A_transpose_b"],
            "b_norm_sq": hessian_target["b_norm_sq"],
            "deltaTheta_C1": hessian_target["deltaTheta_C1"],
            "hessian_source_theorem_template_exists": hessian_template[
                "theorem_name"
            ],
        },
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    write_json(ROUTE_A, route_a)
    write_json(ROUTE_B, route_b)
    write_json(ATTEMPT, attempt)
    validation = run_validator(ATTEMPT)

    cutset = {
        "schema": "MTTFinalSourceEmissionCutset.v1",
        "status": "FINAL_SOURCE_EMISSION_CUTSET_EXECUTABLE_VALIDATOR_REJECTS_CURRENT_ATTEMPT",
        "strict_validator": rel(VALIDATOR),
        "current_attempt_validates": validation["ok"],
        "closed_support": attempt["support_closed"],
        "remaining_route_A": {
            "physical_phifin_c1_action_emitted": True,
            "finite_weyl_action_restriction_derived": True,
            "no_extra_boundary_or_source_term": True,
            "selected_phase_shift_variation_operators_pre_residual": True,
            "selected_hessian_counterterm_source": True,
            "same_source_b_selected_emitted": True,
            "row_formula_source_theorem_derived": True,
        },
        "remaining_route_B": {
            "independent_hessian_quadrature_source_emitted": True,
            "selected_b_vector_source": True,
            "source_independent_of_residual_projector_replay": True,
        },
        "why_this_is_now_the_frontier": [
            "row slots, variation-operator shapes, formal Hessian rows, and locked target algebra are already closed as support",
            "the validator requires a source emission, not another replay of the same target values",
            "either same-branch Phi_fin^C1 emission or independent Hessian/quadrature provenance would close the narrowed gate",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhiFinC1EmissionOrIndependentHessianQuadratureSource",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "hessian_formal_target": rel(HESSIAN_TARGET),
            "hessian_source_template": rel(HESSIAN_TEMPLATE),
            "variation_shape_compatibility": rel(VARIATION_COMPAT),
            "row_source_attempt": rel(ROW_SOURCE_ATTEMPT),
            "route_b_basis": rel(ROUTE_B_BASIS),
        },
        "output_packets": {
            "route_a_template": rel(ROUTE_A),
            "route_b_template": rel(ROUTE_B),
            "current_source_emission_attempt": rel(ATTEMPT),
            "strict_source_emission_validator_result": rel(VALIDATION),
            "final_source_emission_cutset": rel(CUTSET),
            "validator": rel(VALIDATOR),
        },
        "what_closes_now": {
            "narrowed_final_source_validator_built": True,
            "same_branch_phifin_lane_locked": True,
            "independent_hessian_quadrature_lane_locked": True,
            "current_nonpromotion_verified": validation["exit_code"] == 1,
        },
        "what_remains_open": {
            "same_branch_phifin_c1_source_emission": True,
            "independent_hessian_quadrature_source": True,
            "source_independent_of_residual_projector_replay": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "theorem": {
            "name": "NarrowedFinalSourceEmissionDisjunctionTheorem",
            "proved": True,
            "statement": (
                "After row-slot coverage, variation-shape compatibility, formal Hessian target "
                "identification, and exact row support are closed, the remaining promotion gate is "
                "the executable disjunction between same-branch Phi_fin^C1 source emission and an "
                "independent Hessian/quadrature source with residual-projector-independent provenance."
            ),
        },
        "closure_claimed": False,
        "previous_gate_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1Emission_or_IndependentHessianQuadratureSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "validator_path": rel(VALIDATOR),
        "validator_exit_code": validation["exit_code"],
        "validator_rejects_current_attempt": validation["exit_code"] == 1,
        "same_branch_phifin_source_closed": False,
        "independent_hessian_quadrature_source_closed": False,
        "route_B_promoted_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFinC1Emission or IndependentHessianQuadratureSource v1

Status: `{STATUS}`

This artifact builds the narrowed final source-emission validator. The already
closed support now includes row-slot coverage, variation-operator shape
compatibility, formal Hessian/`b_selected` target identification, exact row
values, and exactness certificates.

The current attempt is intentionally rejected. The remaining proof is the real
source-emission step:

1. same-branch physical `Phi_fin^C1` emits the finite Weyl action restriction,
   phase/shift variation operators, Hessian counterterm, and `b_selected`; or
2. independent Hessian/quadrature source data emits the same packet with
   provenance independent of residual-projector replay.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
ATTEMPT = ROOT / "candidate_data" / "{SLUG}" / "current_source_emission_attempt.packet.json"
CUTSET = ROOT / "candidate_data" / "{SLUG}" / "final_source_emission_cutset.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1Emission_or_IndependentHessianQuadratureSource_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "disjunction theorem not proved")
    require(attempt["support_closed"]["variation_operator_shape_compatibility"] is True, "variation support missing")
    require(attempt["support_closed"]["formal_hessian_target_identified"] is True, "hessian target missing")
    require(attempt["locked_target_values_used_as_source"] is False, "locked targets used")
    require(attempt["route_A_phifinc1_source_emission"]["physical_phifin_c1_action_emitted"] is False, "Route A overclosed")
    require(attempt["route_B_independent_hessian_quadrature_source"]["independent_hessian_quadrature_source_emitted"] is False, "Route B hessian overclosed")
    require(attempt["route_B_independent_hessian_quadrature_source"]["selected_basis_independent_of_residual_projector"] is True, "Route B basis support missing")
    require(attempt["route_B_independent_hessian_quadrature_source"]["quadrature_rule_independent_of_locked_target"] is True, "Route B quadrature support missing")
    require(proc.returncode == 1, "validator should reject current attempt")
    require(any("neither narrowed Route A nor narrowed Route B validates" in line for line in proc.stderr.splitlines()), "missing final rejection")
    require(cutset["current_attempt_validates"] is False, "cutset should reject")
    require(cutset["remaining_route_A"]["same_source_b_selected_emitted"] is True, "Route A b gap missing")
    require(cutset["remaining_route_B"]["independent_hessian_quadrature_source_emitted"] is True, "Route B hessian gap missing")
    require(cert["validator_rejects_current_attempt"] is True, "cert should reject")
    require(cert["same_branch_phifin_source_closed"] is False, "cert Route A overclosed")
    require(cert["independent_hessian_quadrature_source_closed"] is False, "cert Route B overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("current attempt is intentionally rejected" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(VALIDATION, validation)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    print(f"Validator exit: {validation['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
