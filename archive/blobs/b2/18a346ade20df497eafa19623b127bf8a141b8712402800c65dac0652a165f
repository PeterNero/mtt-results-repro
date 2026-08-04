"""Audit L_rowlocal/T_scheme/lambda_H product reduction and import boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PRODUCT_CONTRACT = PACKET_DIR / "combined_threshold_kernel_k_row_contract.packet.json"
SOURCE_ATTEMPT = PACKET_DIR / "source_selected_k_row_execution_attempt.packet.json"
EMPIRICAL_IMPORT = PACKET_DIR / "controlled_empirical_k_import_contract.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_k_product_reduction.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LRowlocalTSchemeLambdaH_SourceExecution_or_ControlledEmpiricalImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_LROWLOCALTSCHEMELAMBDAH_SOURCEEXECUTION_OR_CONTROLLEDEMPIRICALIMPORT_"
    "BUILT_PRODUCT_REDUCTION_SOURCE_K_ROWS_OPEN"
)
NEXT = "MTT_Selected_CombinedThresholdKernelKRows_SourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector violation")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting violation")
    require(packet.get("closure_claimed") is True, f"{label} should close its theorem")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    product = load(PRODUCT_CONTRACT)
    source_attempt = load(SOURCE_ATTEMPT)
    empirical = load(EMPIRICAL_IMPORT)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("certificate", cert),
        ("product contract", product),
        ("source attempt", source_attempt),
        ("empirical import", empirical),
        ("cutset", cutset),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    decision = data["closure_decision"]
    require(decision["product_reduction_closed"] is True, "product reduction not closed")
    require(decision["combined_K_row_contract_built"] is True, "K contract not built")
    require(decision["source_selected_K_execution_attempted"] is True, "source attempt missing")
    require(decision["accepted_combined_K_source_row_count"] == 0, "K source rows overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["lambda_H_value_row_emitted"] is False, "lambda_H overemitted")
    require(decision["controlled_empirical_K_import_available"] is True, "empirical K import unavailable")
    require(
        decision["controlled_empirical_K_import_selected_for_no_knob"] is False,
        "empirical K import promoted to no-knob",
    )
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(product["row_count"] == 10, "K contract row count mismatch")
    require(product["product_reduction_closed"] is True, "product contract did not close")
    require(
        product["reduced_row_formula"] == "Omega_i = D_fin[class(i)] * K_threshold_i * exp(-2*pi*n_i)",
        "reduced formula mismatch",
    )
    require(product["combined_kernel_definition"] == "K_threshold_i = L_rowlocal_i * T_scheme_i", "definition mismatch")
    require(product["accepted_combined_K_source_row_count"] == 0, "product contract overaccepted")
    for row in product["combined_kernel_rows"]:
        require(row["product_sufficient_for_scalar_execution"] is True, f"{row['omega_id']} product not sufficient")
        require(
            row["split_L_T_required_before_scalar_execution"] is False,
            f"{row['omega_id']} incorrectly requires split before scalar execution",
        )
        require(row["internal_selected_K_row_accepted"] is False, f"{row['omega_id']} K row overaccepted")
        require(row["empirical_K_import_available"] is True, f"{row['omega_id']} empirical K import missing")
        require(
            "no selected source functional currently emits K_i" in row["why_open"],
            f"{row['omega_id']} missing source-open reason",
        )

    require(source_attempt["accepted_combined_K_source_row_count"] == 0, "source attempt overaccepted K")
    require(source_attempt["accepted_internal_scalar_value_row_count"] == 0, "source attempt overaccepted scalars")
    require(source_attempt["lambda_H_value_row_emitted"] is False, "source attempt emitted lambda_H")
    for key in [
        "theta_exponents_closed",
        "finite_heat_torsion_D_fin_closed",
        "omega_formula_skeleton_closed",
        "internal_external_decision_boundary_closed",
        "product_reduction_closed",
    ]:
        require(source_attempt["closed_support"][key] is True, f"support not closed: {key}")

    require(empirical["external_import_lane_available"] is True, "empirical import lane unavailable")
    require(empirical["empirical_K_row_count"] == 10, "empirical K row count mismatch")
    require(empirical["can_replay_ten_scalar_slots_under_empirical_layer"] is True, "empirical replay unavailable")
    require(empirical["selected_for_no_knob_closure"] is False, "empirical no-knob promotion")
    require(empirical["selected_for_true_SM_equivalence"] is False, "empirical true SM promotion")
    for row in empirical["empirical_K_rows"]:
        require(row["selected_for_no_knob"] is False, f"{row['omega_id']} empirical row promoted")
        require(row["allowed_use"] == "controlled empirical replay/import only", f"{row['omega_id']} allowed use mismatch")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    for phrase in [
        "L_rowlocal/T_scheme split reduced to combined K_threshold rows for scalar execution",
        "ten empirical K rows typed as controlled import data",
        "source-selected K execution attempted with zero accepted source rows",
    ]:
        require(phrase in cutset["closed_here"], f"cutset closed_here missing {phrase}")
    for phrase in [
        "selected source theorem for ten K_threshold rows",
        "selected H-sector K row emitting lambda_H",
        "strict Omega acceptance after K rows emit",
        "matrix-level CKM/offdiagonal mixing extension",
    ]:
        require(phrase in cutset["still_open"], f"cutset still_open missing {phrase}")

    for phrase in [
        "combined K source rows accepted : 0",
        "empirical K import available     : true",
        "empirical K selected for no-knob  : false",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
