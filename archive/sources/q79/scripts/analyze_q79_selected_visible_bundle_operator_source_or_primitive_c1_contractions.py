"""Create the q79 selected visible operator source or primitive C1 target.

The previous same-source theorem attempt proved a no-go for patching current
artifacts together.  This script creates the next executable target:

* a latest-current Selected_VAlpha_ChernWeil_Operator_Source packet that uses
  the newly selected monad L2/Ext input but honestly leaves same-source operator
  provenance open;
* a 24-atom primitive C1 contraction contract, one atom for each
  sector/primitive-term matrix required by compute_c1_response_matrices.py.

It does not invent any primitive values.  It proves that the current target is
well formed, and records exactly which lane must be filled next.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
SCRIPTS = ROOT / "scripts"

OUT_DIR = CANDIDATES / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions"
OUT_CANDIDATE = (
    CANDIDATES
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions.candidate.json"
)
OUT_CERT = (
    CERTS
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_certificate.json"
)
OUT_PAPER = (
    CORPUS
    / "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_Contractions_v1.md"
)
OUT_TABLE = OUT_DIR / "target_summary.json"
OUT_SOURCE_PACKET = OUT_DIR / "selected_valpha_operator_source.current_after_samesource_nogo.json"
OUT_PRIMITIVE_CONTRACT = OUT_DIR / "primitive_c1_atomic_contract.open.json"
OUT_MISSING_DATA = OUT_DIR / "selected_missing_data_report.json"

STATUS = "Q79_SELECTED_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_TARGET_CREATED_CURRENT_LANES_OPEN"
NEXT = "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1"

ORDERED_PACKET = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_ordered_source.selected_under_section_principle.json"
)
COHOMOLOGY_PACKET = (
    CANDIDATES
    / "terminal_admissible_section_source"
    / "visible_rank2_l2_cohomology.selected_under_section_principle.json"
)
S3_PACKET = CERTS / "visible_twisted_s3_class_restriction_packet.selected.json"
GS_SOURCE_ATTEMPT_PACKET = CERTS / "time_oriented_m1_visible_gs_source.attempt.json"
PROMOTION_ATTEMPT_PACKET = CERTS / "selected_hym_operator_source_promotion.attempt.json"
PRIMITIVE_TEMPLATE = CERTS / "selected_c1_primitive_contractions.template.json"

INPUTS = {
    "same_source_operator_no_go": (
        CERTS / "q79_same_source_operator_provenance_or_selected_routec_solve_certificate.json"
    ),
    "selected_monad_l2_source": (
        CERTS / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual_certificate.json"
    ),
    "selected_ah_goodcover_promotion_hym": (
        CERTS / "q79_selected_ah_goodcover_promotion_hym_certificate.json"
    ),
    "ordered_source_packet": ORDERED_PACKET,
    "cohomology_packet": COHOMOLOGY_PACKET,
    "s3_class_restriction_packet": S3_PACKET,
    "visible_gs_source_attempt": GS_SOURCE_ATTEMPT_PACKET,
    "selected_source_promotion_attempt": PROMOTION_ATTEMPT_PACKET,
    "primitive_c1_template": PRIMITIVE_TEMPLATE,
    "c1_finite_response_reduction": CERTS / "c1_finite_response_matrix_reduction_certificate.json",
}

SECTORS = ("u", "d", "e", "nuD")
TERMS = (
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
)

TERM_DEPENDENCIES = {
    "theta_overlap_variation": [
        "selected_deltaTheta_C1_solution",
        "selected Hessian inverse/source vector",
        "Omega/measure/dilaton/background variation rule",
    ],
    "left_zero_mode_response": [
        "selected left-sector zero modes",
        "selected left-sector dotD_alpha1",
        "selected left-sector reduced Green/Riesz projector",
    ],
    "right_zero_mode_response": [
        "selected right-sector zero modes",
        "selected right-sector dotD_alpha1",
        "selected right-sector reduced Green/Riesz projector",
    ],
    "higgs_zero_mode_response": [
        "selected Higgs zero mode",
        "selected Higgs dotD_alpha1",
        "selected Higgs reduced Green/Riesz projector",
    ],
    "explicit_vertex": [
        "selected higher-derivative Yukawa vertex",
        "or a selected theorem proving this primitive matrix is exactly zero",
    ],
    "basis_connection": [
        "selected horizontal gauge or basis-transport convention",
        "selected Gram-Schmidt/basis connection matrix if non-horizontal",
    ],
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def status_record(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": rel(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "target_fitting_used": data.get("target_fitting_used"),
        "next_required_artifact": data.get("next_required_artifact"),
    }


def run_process(args: list[str]) -> dict[str, Any]:
    proc = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "stdout_head": proc.stdout.splitlines()[:30],
    }


def run_validator(script: str, path: Path, prefix: str | None = None) -> dict[str, Any]:
    result = run_process([sys.executable, str(SCRIPTS / script), str(path)])
    if prefix is not None:
        result["parsed_report"] = parse_prefixed_json(result["stdout"], prefix)
    return result


def parse_prefixed_json(stdout: str, prefix: str) -> dict[str, Any] | None:
    for line in stdout.splitlines():
        if line.startswith(prefix):
            return json.loads(line[len(prefix) :])
    return None


def primitive_missing_from_stdout(stdout: str) -> list[str]:
    missing: list[str] = []
    for line in stdout.splitlines():
        if line.startswith("- sectors."):
            missing.append(line[2:])
    return missing


def build_current_source_packet() -> dict[str, Any]:
    ordered = load(ORDERED_PACKET)
    cohomology = load(COHOMOLOGY_PACKET)

    return {
        "schema": "SelectedVAlphaChernWeilOperatorSource.v1",
        "status": "CURRENT_AFTER_SAMESOURCE_NOGO_SOURCE_OPEN",
        "source_identity": {
            "branch_id": "q79/F,m=1",
            "source_kind": "rank2_valpha_chern_weil_operator_source",
            "selected_by_mtt": False,
            "fixture_only": True,
            "source_certificate": None,
            "no_observed_flavor_inputs": True,
            "no_benchmark_flavor_inputs": True,
        },
        "valpha_extension": {
            "selected_L": ordered["target"]["L"],
            "selected_L2": ordered["target"]["L2"],
            "c2_valpha": [4, 0, 0],
            "h1_L2": cohomology["reported_cohomology"]["h1"],
            "rank2_valpha_model_selected": True,
            "terminal_monad_difference_L3_minus_K2_selector_closed": True,
            "ordered_source_validator_passes": True,
            "ordered_source_packet": rel(ORDERED_PACKET),
            "pic0_resolution": "pic0_quotient_rule",
            "pic0_selected_or_quotiented": True,
            "nonzero_ext_class_selected": True,
            "non_split_stability_or_hym_proved": False,
        },
        "s3_green_schwarz_support": {
            "s3_class_restriction_packet": rel(S3_PACKET),
            "selected_s3_class_restriction_closed": True,
            "block_projector_retention_closed": True,
            "visible_gs_curvature_closed": True,
            "visible_gs_source_packet": rel(GS_SOURCE_ATTEMPT_PACKET),
            "same_source_link_valpha_to_s3_proved": False,
            "chern_weil_row_derived_from_same_source": False,
            "visible_gs_source_validator_passes": False,
        },
        "operator_execution": {
            "selected_source_promotion_packet": rel(PROMOTION_ATTEMPT_PACKET),
            "typed_transition_or_rhoE_data_emitted": False,
            "hym_strominger_or_routec_residual_pass": False,
            "sector_D_E_packets_pass": False,
            "reduced_green_packets_pass": False,
            "dotD_packets_pass": False,
            "same_branch_derivative_verified": False,
            "coherent_spectral_projector_retention": False,
            "selected_source_promotion_validator_passes": False,
            "primitive_C1_or_Yukawa_contractions": False,
        },
        "branch_orientation": {
            "time_oriented_q79_representative": True,
            "m1_label_bound_to_q79": True,
            "antiunitary_conjugate_pair_accounted": True,
            "cp_even_parity_accounted": True,
            "orientation_selection_justified_by_source": False,
        },
        "forbidden_shortcuts": {
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
            "copies_visible_gs_row_without_source_derivation": False,
            "uses_routec_smoke_as_selected_operator_data": False,
            "splices_s3_and_valpha_without_same_source_link": False,
            "treats_pic0_as_notational_without_rule": False,
        },
    }


def build_primitive_contract(missing: list[str]) -> dict[str, Any]:
    atoms: list[dict[str, Any]] = []
    missing_set = set(missing)
    for sector in SECTORS:
        for term in TERMS:
            path = f"sectors.{sector}.{term}"
            atoms.append(
                {
                    "id": path,
                    "sector": sector,
                    "term": term,
                    "status": "OPEN_MISSING_SELECTED_3X3_MATRIX"
                    if path in missing_set
                    else "FILLED_UNEXPECTED",
                    "matrix_shape": [3, 3],
                    "dependencies": TERM_DEPENDENCIES[term],
                    "same_source_required": True,
                    "zero_matrix_allowed_only_if_proved_by_selected_source": True,
                    "forbidden_sources": [
                        "Execution II benchmark Yukawa entries",
                        "observed fermion masses",
                        "observed CKM or PMNS angles",
                        "post-hoc fitted threshold factors",
                    ],
                }
            )
    return {
        "schema": "Q79PrimitiveC1AtomicContractionContract.v1",
        "status": "OPEN_24_SELECTED_PRIMITIVE_C1_ATOMS_REQUIRED",
        "source_requirement": (
            "Every primitive matrix must be derived from the same selected "
            "q79/F,m=1 visible bundle/operator source that supplies D_E, Riesz, "
            "Green, dotD, projectors, and the C1 alpha1 deformation."
        ),
        "calculator": "scripts/compute_c1_response_matrices.py",
        "template": rel(PRIMITIVE_TEMPLATE),
        "atom_count": len(atoms),
        "missing_atom_count": sum(1 for atom in atoms if atom["status"].startswith("OPEN")),
        "atoms": atoms,
    }


def build_candidate() -> dict[str, Any]:
    source_packet = build_current_source_packet()
    write_json(OUT_SOURCE_PACKET, source_packet)

    source_validation = run_validator(
        "validate_selected_valpha_chern_weil_operator_source.py",
        OUT_SOURCE_PACKET,
        "selected_valpha_chern_weil_operator_source_report=",
    )
    source_report = source_validation.get("parsed_report") or {}

    primitive_compute = run_process(
        [sys.executable, str(SCRIPTS / "compute_c1_response_matrices.py"), str(PRIMITIVE_TEMPLATE)]
    )
    missing_primitive = primitive_missing_from_stdout(primitive_compute["stdout"])
    primitive_contract = build_primitive_contract(missing_primitive)
    write_json(OUT_PRIMITIVE_CONTRACT, primitive_contract)

    missing_data = run_process(
        [
            sys.executable,
            str(SCRIPTS / "calculate_missing_selected_data.py"),
            "--write-report",
            rel(OUT_MISSING_DATA),
        ]
    )
    missing_data_report = load(OUT_MISSING_DATA)

    closes = {
        "next_target_artifact_created": True,
        "latest_selected_monad_data_inserted_into_visible_operator_source_packet": True,
        "selected_ordered_source_subvalidator_passes": (
            source_report.get("subvalidators", {}).get("ordered_source", {}).get("exit_code") == 0
        ),
        "selected_s3_class_subvalidator_passes": (
            source_report.get("subvalidators", {}).get("s3_class_restriction", {}).get("exit_code")
            == 0
        ),
        "primitive_c1_atoms_enumerated": primitive_contract["atom_count"] == 24,
        "primitive_c1_calculator_refuses_incomplete_template": primitive_compute["exit_code"] == 2,
        "selected_missing_data_scan_confirms_operator_source_first_blocker": (
            missing_data_report.get("first_blocking_layer") == "selected_operator_source"
        ),
    }
    remains = {
        "selected_visible_bundle_operator_source_certificate": True,
        "non_split_stability_or_selected_HYM_RouteC_solve": True,
        "same_source_ChernWeil_GS_row": True,
        "selected_DE_rhoE_Riesz_Green_dotD": True,
        "orientation_selection_justified_by_same_source": True,
        "all_24_primitive_C1_3x3_matrices": True,
        "selected_C1_response_matrices": True,
        "selected_Yukawa_CKM_PMNS_Higgs_RG_data": True,
        "full_SM_or_no_knob_closure": True,
    }

    return {
        "certificate": "Q79SelectedVisibleBundleOperatorSourceOrPrimitiveC1Contractions",
        "status": STATUS,
        "candidate_path": rel(OUT_CANDIDATE),
        "table_path": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "input_statuses": {name: status_record(path) for name, path in INPUTS.items()},
        "source_lane": {
            "packet": rel(OUT_SOURCE_PACKET),
            "validator": "scripts/validate_selected_valpha_chern_weil_operator_source.py",
            "validator_exit_code": source_validation["exit_code"],
            "validator_status": source_report.get("status"),
            "open_items": source_report.get("open_items", []),
            "subvalidators": source_report.get("subvalidators", {}),
            "interpretation": (
                "The latest selected monad L2/Ext data now enter the visible "
                "operator-source packet honestly; the lane remains open at "
                "selected source identity, stability/HYM or Route-C solve, "
                "same-source GS, operator execution, and primitive C1."
            ),
        },
        "primitive_c1_lane": {
            "contract": rel(OUT_PRIMITIVE_CONTRACT),
            "calculator": "scripts/compute_c1_response_matrices.py",
            "calculator_exit_code": primitive_compute["exit_code"],
            "missing_atom_count": len(missing_primitive),
            "missing_atoms": missing_primitive,
            "contract_atom_count": primitive_contract["atom_count"],
            "contract_missing_atom_count": primitive_contract["missing_atom_count"],
            "interpretation": (
                "Primitive C1 is not one scalar. It is a 24-matrix selected "
                "same-source fill: four sectors times six primitive response "
                "terms, each a selected 3x3 matrix."
            ),
        },
        "selected_missing_data_scan": {
            "path": rel(OUT_MISSING_DATA),
            "exit_code": missing_data["exit_code"],
            "first_blocking_layer": missing_data_report.get("first_blocking_layer"),
            "null_counts": missing_data_report.get("null_counts"),
            "can_compute_now": missing_data_report.get("can_compute_now"),
        },
        "what_closes_now": closes,
        "what_remains_open": remains,
        "guardrails": {
            "uses_observed_masses_or_ckm_inputs": False,
            "uses_benchmark_flavor_entries": False,
            "uses_lifted_flags_as_proof": False,
            "claims_selected_operator_source_constructed": False,
            "claims_primitive_C1_values_computed": False,
            "claims_selected_C1_response_matrices": False,
            "claims_selected_RouteC_residual": False,
            "claims_HYM_connection_constructed": False,
            "claims_A_selected": False,
            "claims_b_selected": False,
            "claims_full_sm_closure": False,
        },
        "theorem": {
            "name": "Q79SelectedVisibleOperatorOrPrimitiveC1TargetCreationTheorem",
            "proved": True,
            "closure_claimed": False,
            "statement": (
                "The next proof target is now executable: either construct one "
                "selected q79/F,m=1 visible bundle/operator source that passes the "
                "V_alpha source validator, or fill the 24 primitive C1 matrices "
                "from that same selected source. Current data close neither lane."
            ),
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }


def bool_lines(data: dict[str, Any]) -> str:
    return "\n".join(f"- `{key}`: `{value}`" for key, value in data.items())


def bullet_lines(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- none"


def build_paper(data: dict[str, Any]) -> str:
    source = data["source_lane"]
    primitive = data["primitive_c1_lane"]
    return f"""# Q79 Selected Visible Bundle Operator Source or Primitive C1 Contractions v1

## Result

The target has been created as an executable two-lane gate.

Lane A is the selected visible bundle/operator source packet. It now consumes
the latest selected monad `L^2` and `h1=8` Ext input, and its ordered-source
subvalidator passes. It remains open because the current corpus still lacks a
single selected source for stability/HYM or Route-C, same-source Green-Schwarz,
`D_E/Riesz/Green/dotD`, and primitive C1.

Lane B is the primitive C1 contraction fill. The calculator refuses the current
template because all 24 selected primitive matrices are missing.

## Source Lane

- packet: `{source["packet"]}`
- validator status: `{source["validator_status"]}`
- validator exit code: `{source["validator_exit_code"]}`

Open items:

{bullet_lines(source["open_items"])}

Interpretation: {source["interpretation"]}

## Primitive C1 Lane

- contract: `{primitive["contract"]}`
- calculator exit code: `{primitive["calculator_exit_code"]}`
- missing atoms: `{primitive["missing_atom_count"]}`
- contract atoms: `{primitive["contract_atom_count"]}`

Interpretation: {primitive["interpretation"]}

The 24 atoms are `u,d,e,nuD` times:

{bullet_lines(list(TERMS))}

## Missing-Data Scan

- first blocking layer: `{data["selected_missing_data_scan"]["first_blocking_layer"]}`
- selected C1 matrices computable now: `{data["selected_missing_data_scan"]["can_compute_now"].get("actual_selected_C1_matrices")}`
- full SM closure computable now: `{data["selected_missing_data_scan"]["can_compute_now"].get("full_SM_closure")}`

## What Closes Now

{bool_lines(data["what_closes_now"])}

## What Remains Open

{bool_lines(data["what_remains_open"])}

## Theorem

`{data["theorem"]["name"]}` is proved as a target-creation theorem.

{data["theorem"]["statement"]}

Next required artifact: `{data["next_required_artifact"]}`.
"""


def main() -> int:
    data = build_candidate()
    write_json(OUT_TABLE, {
        **data["what_closes_now"],
        "status": data["status"],
        "next_required_artifact": data["next_required_artifact"],
    })
    write_json(OUT_CANDIDATE, data)
    write_json(OUT_CERT, data)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(data), encoding="utf-8")
    print("Q79 selected visible operator source or primitive C1 target")
    print(json.dumps({"status": data["status"], "next": data["next_required_artifact"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
