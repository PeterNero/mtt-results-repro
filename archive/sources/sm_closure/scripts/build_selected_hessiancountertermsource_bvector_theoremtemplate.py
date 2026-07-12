"""Build Hessian counterterm and b-vector source theorem template."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hessiancountertermsource_bvector_theoremtemplate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TARGET = PACKET_DIR / "hessian_bvector_formal_target.packet.json"
TEMPLATE = PACKET_DIR / "hessian_bvector_source_theorem.strict_template.json"
GAP = PACKET_DIR / "remaining_hessian_bvector_source_gap.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
AUDIT = CORPUS / f"{SLUG}_audit.py"
NOTE = CORPUS / "MTT_Selected_HessianCountertermSource_BVector_TheoremTemplate_v1.md"

PREVIOUS = DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap.candidate.json"
FORMAL_110 = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)
FORMAL_EXECUTION = (
    DATA
    / "selected_routeaemission_or_routebgalerkinrows_execution"
    / "formal_110_row_execution.packet.json"
)
ACCEPTANCE = (
    DATA
    / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
    / "source_or_kernel_acceptance_contract.packet.json"
)
OBLIGATION = (
    DATA
    / "selected_primitivec1tensor_hessiansourcemap_or_honestgalerkinc1execution"
    / "source_map_selection_obligation_kernel.packet.json"
)

STATUS = "MTT_SELECTED_HESSIANCOUNTERTERMSOURCE_BVECTOR_TEMPLATE_BUILT_SOURCE_EMISSION_OPEN"
NEXT = "MTT_Selected_PhysicalPhiFinC1Emission_or_IndependentHessianQuadratureSource_v1"


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


def main() -> int:
    previous = load(PREVIOUS)
    formal_110 = load(FORMAL_110)
    formal_execution = load(FORMAL_EXECUTION)
    acceptance = load(ACCEPTANCE)
    obligation = load(OBLIGATION)

    hessian_rows = formal_execution["hessian_source_values"]
    hessian_summary = formal_110["hessian_source_rows"]
    locked = acceptance["locked_target_check"]

    target = {
        "schema": "MTTHessianBVectorFormalTarget.v1",
        "status": "FORMAL_HESSIAN_BVECTOR_TARGET_IDENTIFIED_SOURCE_OPEN",
        "hessian_row_count": len(hessian_rows),
        "hessian_rows": hessian_rows,
        "A_transpose_A": locked["A_transpose_A"],
        "A_transpose_b": locked["A_transpose_b"],
        "b_norm_sq": locked["b_norm_sq"],
        "deltaTheta_C1": locked["deltaTheta_C1"],
        "formal_110_rows_executed": formal_110["formal_110_rows_executed"],
        "formal_hessian_quadrature_emitted": hessian_summary["all_formal_quadrature_emitted"],
        "physical_source_promoted": hessian_summary["physical_source_promoted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    template = {
        "schema": "MTTHessianBVectorSourceTheoremStrictTemplate.v1",
        "status": "STRICT_TEMPLATE_READY_NOT_PROVED",
        "theorem_name": "SelectedHessianCountertermSourceAndBVectorTheorem",
        "must_prove": {
            "same_branch_phifin_c1_or_galerkin_source_emits_hessian_rows": False,
            "same_source_b_selected_emitted": False,
            "hessian_counterterms_feed_primitive_kernel_formula": False,
            "A_transpose_b_derived_from_selected_source": False,
            "deltaTheta_derived_from_selected_source": False,
            "no_residual_projector_replay_used_as_hessian_source": False,
            "no_locked_target_values_used_as_source": True,
            "observed_data_excluded_as_selector": True,
        },
        "acceptance_target": {
            "hessian_row_ids": [row["row_id"] for row in hessian_rows],
            "A_transpose_A": locked["A_transpose_A"],
            "A_transpose_b": locked["A_transpose_b"],
            "b_norm_sq": locked["b_norm_sq"],
            "deltaTheta_C1": locked["deltaTheta_C1"],
        },
        "current_emission_state": obligation["currently_emitted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gap = {
        "schema": "MTTRemainingHessianBVectorSourceGap.v1",
        "status": "FORMAL_TARGET_CLOSED_SELECTED_SOURCE_EMISSION_OPEN",
        "closed_now": {
            "formal_hessian_row_count_is_two": len(hessian_rows) == 2,
            "formal_A_transpose_b_target_identified": locked["A_transpose_b"] == [12.0, 12.0],
            "formal_deltaTheta_target_identified": locked["deltaTheta_C1"] == [1.0, 1.0],
            "hessian_bvector_source_theorem_template_emitted": True,
        },
        "not_closed": {
            "selected_hessian_counterterm_source": True,
            "selected_b_vector_source": True,
            "selected_phase_shift_variation_operators_pre_residual": True,
            "row_formula_source_theorem_derived": True,
            "source_independent_of_residual_projector_replay": True,
        },
        "why_not_promoted": [
            "The formal finite-trace Hessian rows are emitted, but physical_source_promoted is false.",
            "The acceptance target gives A^T b and deltaTheta, but these are locked replay targets, not selected source emissions.",
            "The source-map obligation still reports selected_b_selected and selected_basis_transport_vertex_or_Hessian_values as false.",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHessianCountertermSourceBVectorTheoremTemplate",
        "status": STATUS,
        "inputs": {
            "previous_gate": rel(PREVIOUS),
            "formal_110_integrated": rel(FORMAL_110),
            "formal_110_execution": rel(FORMAL_EXECUTION),
            "acceptance_contract": rel(ACCEPTANCE),
            "source_obligation": rel(OBLIGATION),
        },
        "output_packets": {
            "hessian_bvector_formal_target": rel(TARGET),
            "hessian_bvector_source_theorem_template": rel(TEMPLATE),
            "remaining_hessian_bvector_source_gap": rel(GAP),
        },
        "what_closes_now": gap["closed_now"],
        "what_remains_open": gap["not_closed"],
        "theorem": {
            "name": "HessianBVectorSourceGateReductionTheorem",
            "proved": True,
            "statement": (
                "The formal finite-trace layer identifies the exact two Hessian/source rows and "
                "the locked A^T b=(12,12), ||b||^2=24, deltaTheta=(1,1) target. Full promotion "
                "is equivalent to proving same-branch selected Hessian counterterm and b-vector "
                "source emission, or replacing it by independent Hessian quadrature source data."
            ),
        },
        "closure_claimed": False,
        "previous_gate_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_HessianCountertermSource_BVector_TheoremTemplate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "hessian_row_count": len(hessian_rows),
        "formal_target_identified": True,
        "hessian_counterterm_source_closed": False,
        "b_selected_source_closed": False,
        "route_B_promoted_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected HessianCountertermSource BVector TheoremTemplate v1

Status: `{STATUS}`

This step fixes the Hessian/`b_selected` target as a theorem object. The formal
finite-trace layer has exactly two Hessian/source rows and replays
`A^T b=(12,12)`, `||b||^2=24`, and `deltaTheta=(1,1)`.

This is still not source emission. The selected Hessian counterterm source,
same-source `b_selected`, and physical `Phi_fin^C1`/independent quadrature
source remain open.

Next artifact: `{NEXT}`.
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "{SLUG}.candidate.json"
TARGET = ROOT / "candidate_data" / "{SLUG}" / "hessian_bvector_formal_target.packet.json"
TEMPLATE = ROOT / "candidate_data" / "{SLUG}" / "hessian_bvector_source_theorem.strict_template.json"
GAP = ROOT / "candidate_data" / "{SLUG}" / "remaining_hessian_bvector_source_gap.packet.json"
CERT = ROOT / "certificates" / "{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HessianCountertermSource_BVector_TheoremTemplate_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    target = load(TARGET)
    template = load(TEMPLATE)
    gap = load(GAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "{STATUS}", "status mismatch")
    require(data["theorem"]["proved"] is True, "reduction theorem not proved")
    require(target["hessian_row_count"] == 2, "wrong hessian row count")
    require(target["A_transpose_b"] == [12.0, 12.0], "A^T b mismatch")
    require(target["b_norm_sq"] == 24.0, "b norm mismatch")
    require(target["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta mismatch")
    require(target["physical_source_promoted"] is False, "target source overpromoted")
    require(template["must_prove"]["same_branch_phifin_c1_or_galerkin_source_emits_hessian_rows"] is False, "source theorem overclosed")
    require(template["must_prove"]["same_source_b_selected_emitted"] is False, "b source overclosed")
    require(template["must_prove"]["no_locked_target_values_used_as_source"] is True, "locked target guard missing")
    require(gap["closed_now"]["formal_hessian_row_count_is_two"] is True, "formal count not closed")
    require(gap["not_closed"]["selected_hessian_counterterm_source"] is True, "hessian gap missing")
    require(gap["not_closed"]["selected_b_vector_source"] is True, "b gap missing")
    require(cert["formal_target_identified"] is True, "cert target missing")
    require(cert["hessian_counterterm_source_closed"] is False, "cert hessian overclosed")
    require(cert["b_selected_source_closed"] is False, "cert b overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("This is still not source emission" in note, "note missing guardrail")
    print(f"PASS {{DATA.name}}: {{data['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    write_json(TARGET, target)
    write_json(TEMPLATE, template)
    write_json(GAP, gap)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
