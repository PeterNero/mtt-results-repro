"""Audit q79 selected visible operator source or primitive C1 target."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_same_source_operator_provenance_or_selected_routec_solve.py"
SCRIPT = (
    ROOT
    / "scripts"
    / "analyze_q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions.py"
)
CERT = (
    ROOT
    / "certificates"
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions_certificate.json"
)
CANDIDATE = (
    ROOT
    / "candidate_data"
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions.candidate.json"
)
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions"
    / "target_summary.json"
)
CONTRACT = (
    ROOT
    / "candidate_data"
    / "q79_selected_visible_bundle_operator_source_or_primitive_c1_contractions"
    / "primitive_c1_atomic_contract.open.json"
)
PAPER = (
    ROOT
    / "proof_corpus"
    / "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_Contractions_v1.md"
)

STATUS = "Q79_SELECTED_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_TARGET_CREATED_CURRENT_LANES_OPEN"
NEXT = "Q79_Selected_DE_Green_DotD_Source_for_Primitive_C1_v1"
SECTORS = {"u", "d", "e", "nuD"}
TERMS = {
    "theta_overlap_variation",
    "left_zero_mode_response",
    "right_zero_mode_response",
    "higgs_zero_mode_response",
    "explicit_vertex",
    "basis_connection",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TABLE, CONTRACT, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    contract = load(CONTRACT)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table["status"] == cert["status"], "summary table status mismatch", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    source = cert["source_lane"]
    primitive = cert["primitive_c1_lane"]
    scan = cert["selected_missing_data_scan"]
    closes = cert["what_closes_now"]
    remaining = cert["what_remains_open"]

    require(source["validator_exit_code"] == 2, "source lane should stay open", failures)
    require(source["validator_status"] == "OPEN", "source validator status should be OPEN", failures)
    require(
        source["subvalidators"]["ordered_source"]["exit_code"] == 0,
        "ordered-source subvalidator should pass",
        failures,
    )
    require(
        source["subvalidators"]["s3_class_restriction"]["exit_code"] == 0,
        "S3 class subvalidator should pass",
        failures,
    )
    require(
        source["subvalidators"]["visible_gs_source"]["exit_code"] == 1,
        "visible GS source should still fail selected source evidence",
        failures,
    )
    require(
        source["subvalidators"]["selected_source_promotion"]["exit_code"] == 1,
        "selected source promotion should still fail",
        failures,
    )
    for expected in (
        "selected_by_mtt must be true",
        "non_split_stability_or_hym_proved must be true",
        "same_source_link_valpha_to_s3_proved must be true",
        "typed_transition_or_rhoE_data_emitted must be true",
        "primitive_C1_or_Yukawa_contractions must be true",
        "orientation_selection_justified_by_source must be true",
    ):
        require(expected in source["open_items"], f"source lane missing open item: {expected}", failures)

    require(primitive["calculator_exit_code"] == 2, "primitive calculator should refuse template", failures)
    require(primitive["missing_atom_count"] == 24, "primitive missing count must be 24", failures)
    require(primitive["contract_atom_count"] == 24, "contract atom count must be 24", failures)
    require(primitive["contract_missing_atom_count"] == 24, "contract missing atom count must be 24", failures)
    require(contract["schema"] == "Q79PrimitiveC1AtomicContractionContract.v1", "contract schema changed", failures)
    require(contract["atom_count"] == 24, "contract atom count changed", failures)
    require(contract["missing_atom_count"] == 24, "contract missing count changed", failures)
    atom_ids = {atom["id"] for atom in contract["atoms"]}
    require(len(atom_ids) == 24, "atom ids not unique", failures)
    require({atom["sector"] for atom in contract["atoms"]} == SECTORS, "sector set changed", failures)
    require({atom["term"] for atom in contract["atoms"]} == TERMS, "term set changed", failures)
    require(
        all(atom["same_source_required"] is True for atom in contract["atoms"]),
        "some atom lacks same-source requirement",
        failures,
    )
    require(
        all(atom["zero_matrix_allowed_only_if_proved_by_selected_source"] is True for atom in contract["atoms"]),
        "some atom permits unproved zero matrix",
        failures,
    )

    require(scan["first_blocking_layer"] == "selected_operator_source", "wrong first blocking layer", failures)
    require(
        scan["can_compute_now"]["actual_selected_C1_matrices"] is False,
        "selected C1 matrices overclaimed",
        failures,
    )
    require(scan["can_compute_now"]["full_SM_closure"] is False, "full SM overclaimed", failures)

    for key in (
        "next_target_artifact_created",
        "latest_selected_monad_data_inserted_into_visible_operator_source_packet",
        "selected_ordered_source_subvalidator_passes",
        "selected_s3_class_subvalidator_passes",
        "primitive_c1_atoms_enumerated",
        "primitive_c1_calculator_refuses_incomplete_template",
        "selected_missing_data_scan_confirms_operator_source_first_blocker",
    ):
        require(closes[key] is True, f"close flag false: {key}", failures)

    for key in (
        "selected_visible_bundle_operator_source_certificate",
        "non_split_stability_or_selected_HYM_RouteC_solve",
        "same_source_ChernWeil_GS_row",
        "selected_DE_rhoE_Riesz_Green_dotD",
        "all_24_primitive_C1_3x3_matrices",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"open flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "executable two-lane gate",
        "subvalidator passes",
        "all 24 selected primitive matrices are missing",
        "Primitive C1 is not one scalar",
        "first blocking layer",
        "Q79SelectedVisibleOperatorOrPrimitiveC1TargetCreationTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected visible operator/primitive C1 target audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected visible operator/primitive C1 target audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
