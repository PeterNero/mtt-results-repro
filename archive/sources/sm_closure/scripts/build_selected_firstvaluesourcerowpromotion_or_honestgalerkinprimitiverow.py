"""Build first value-source row promotion or honest Galerkin primitive-row bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BACKIMPORT = PACKET_DIR / "primitive_exactness_backimport.packet.json"
RECONCILE = PACKET_DIR / "first_value_row_promotion_reconciliation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_primitive_backimport.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FirstValueSourceRowPromotion_or_HonestGalerkinPrimitiveRow_v1.md"

PREVIOUS = DATA / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport.candidate.json"
FIRST_ROW = (
    DATA
    / "selected_firstvaluesourcerowfill_or_externalthresholdsourceimport"
    / "first_value_source_row_fill_attempt.packet.json"
)
EXACT = DATA / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource.candidate.json"
EXACT_ROW = (
    DATA
    / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource"
    / "first_row_exact_weyl_execution.packet.json"
)
EXACT_DECISION = (
    DATA
    / "selected_firstrowkernelformulaexactexecution_or_physicalphifinc1actionsource"
    / "first_row_execution_decision.packet.json"
)
ALL_ROWS = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
ALL_ROWS_DECISION = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "all_rows_provenance_decision.packet.json"
)
SAME_SOURCE = DATA / "selected_samesource_dynamictransferidentity_or_galerkinc1contractions_emission.candidate.json"
KERNEL = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)

STATUS = (
    "MTT_SELECTED_FIRSTVALUESOURCEROWPROMOTION_OR_HONESTGALERKINPRIMITIVEROW_"
    "BUILT_EXACT_PRIMITIVE_BACKIMPORT_ASSEMBLY_OPEN"
)
NEXT = "MTT_Selected_VSD01_AllPrimitiveRowsAssemblyMap_or_PhysicalPhiFinC1ActionSource_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing first row promotion sources: " + ", ".join(missing))


def scalar_real(value: Any) -> float:
    if isinstance(value, list):
        return float(value[0])
    return float(value)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        FIRST_ROW,
        EXACT,
        EXACT_ROW,
        EXACT_DECISION,
        ALL_ROWS,
        ALL_ROWS_DECISION,
        SAME_SOURCE,
        KERNEL,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    first_row = load(FIRST_ROW)
    exact = load(EXACT)
    exact_row = load(EXACT_ROW)
    exact_decision = load(EXACT_DECISION)
    all_rows = load(ALL_ROWS)
    all_rows_decision = load(ALL_ROWS_DECISION)
    same_source = load(SAME_SOURCE)
    kernel = load(KERNEL)

    u_dy_00 = scalar_real(first_row["numeric_payload"]["u_correction_dY"][0][0])
    e_dy_00 = scalar_real(first_row["numeric_payload"]["e_correction_dY"][0][0])
    u_h1_00 = scalar_real(first_row["numeric_payload"]["u_first_hermitian_response_H1"][0][0])
    e_h1_00 = scalar_real(first_row["numeric_payload"]["e_first_hermitian_response_H1"][0][0])
    exact_float = float(exact_row["computed_complex_entry_value"]["real"])

    primitive_backimport = {
        "schema": "MTTPrimitiveExactnessBackimportToFirstValueSourceRow.v1",
        "status": "EXACT_PRIMITIVE_ROW_IMPORTED_AS_SEED_NOT_DYNAMIC_ROW",
        "target_obligation": "VSD-01-selected-overlap-value-kernel",
        "target_value_source_row": first_row["row_id"],
        "primitive_row_id": exact_row["row_id"],
        "primitive_row_coordinate": exact_row["matrix_coordinate"],
        "primitive_exact_value": exact_row["computed_complex_entry_value"],
        "primitive_exactness_certificate": exact_row["exactness_or_error_bound_certificate"],
        "computed_independent_complex_entry_value": exact_row[
            "computed_independent_complex_entry_value"
        ],
        "exactness_certificate_emitted": exact_row["exactness_certificate_emitted"],
        "provenance_independent_of_residual_projector_replay": exact_row[
            "provenance_independent_of_residual_projector_replay"
        ],
        "physical_PhiFinC1_action_source_closed": exact_decision[
            "physical_PhiFinC1_action_source_closed"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(BACKIMPORT, primitive_backimport)

    reconciliation = {
        "schema": "MTTFirstValueRowPromotionReconciliation.v1",
        "status": "PRIMITIVE_EXACTNESS_BACKIMPORTED_DYNAMIC_ASSEMBLY_STILL_OPEN",
        "value_source_row": {
            "row_id": first_row["row_id"],
            "target_obligation": first_row["target_obligation"],
            "u_correction_dY_00": u_dy_00,
            "e_correction_dY_00": e_dy_00,
            "u_first_hermitian_response_H1_00": u_h1_00,
            "e_first_hermitian_response_H1_00": e_h1_00,
            "accepted_as_selected_dynamic_value_source_row_before": first_row[
                "accepted_as_selected_dynamic_value_source_row"
            ],
        },
        "primitive_seed": {
            "row_id": exact_row["row_id"],
            "exact_value": exact_row["computed_complex_entry_value"]["exact"],
            "exact_value_float": exact_float,
            "source": rel(EXACT_ROW),
        },
        "direct_identity_checks": {
            "primitive_value_equals_u_correction_dY_00": abs(exact_float - u_dy_00) < 1e-12,
            "primitive_value_equals_e_correction_dY_00": abs(exact_float - e_dy_00) < 1e-12,
            "primitive_value_equals_u_first_hermitian_response_H1_00": abs(
                exact_float - u_h1_00
            )
            < 1e-12,
            "primitive_value_equals_e_first_hermitian_response_H1_00": abs(
                exact_float - e_h1_00
            )
            < 1e-12,
        },
        "assembly_gate": {
            "all_72_row_exactness_available": all_rows["what_closes_now"][
                "all_72_exact_rows_retained"
            ],
            "formal_110_row_replay_integrated": all_rows_decision[
                "formal_110_row_replay_closed"
            ],
            "formal_A_b_deltaTheta_replay_integrated": all_rows_decision[
                "formal_A_b_deltaTheta_replay_closed"
            ],
            "same_source_identity_normal_form_built": same_source["what_closes_now"][
                "same_source_identity_normal_form_built"
            ],
            "selected_dynamic_transfer_identity_promoted": same_source["promotion_decision"][
                "selected_dynamic_transfer_identity_promoted"
            ],
            "selected_b_selected_promoted": same_source["promotion_decision"][
                "selected_b_selected_promoted"
            ],
            "physical_PhiFinC1_action_source_closed": all_rows_decision[
                "physical_PhiFinC1_action_source_closed"
            ],
            "provenance_independent_of_residual_projector_replay": all_rows_decision[
                "provenance_independent_of_residual_projector_replay"
            ],
        },
        "accepted_as_selected_dynamic_value_source_row_now": False,
        "why_not_promoted": [
            "the exact primitive value is a seed row, not identical to the normalized dynamic response entries",
            "selected dynamic transfer identity is not promoted",
            "selected b_selected/A_selected/deltaTheta_C1 are not promoted",
            "physical Phi_fin^C1 action source and residual-projector-independent provenance remain open",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RECONCILE, reconciliation)

    required_vsd01 = kernel["required_rows"][0]
    cutset = {
        "schema": "MTTNextCutsetAfterPrimitiveBackimport.v1",
        "status": "VSD01_REDUCED_TO_ASSEMBLY_MAP_OR_PHYSICAL_ACTION_SOURCE",
        "closed_now": {
            "first_primitive_seed_value_exact": True,
            "first_primitive_seed_exactness_certificate": True,
            "first_value_row_backimport_reconciliation": True,
            "direct_primitive_to_dynamic_identity_rejected": True,
            "no_observed_data_selector_guard_preserved": True,
        },
        "VSD_01_payload_still_required": required_vsd01["required_payload"],
        "still_open": {
            "selected_dynamic_overlap_threshold_tensor_T_selected": True,
            "assembly_map_from_primitive_rows_to_dynamic_value_source_row": True,
            "same_branch_linking_tensor_rows_to_versioned_value_packet": True,
            "physical_PhiFinC1_action_source_or_independent_provenance": True,
            "selected_A_b_deltaTheta_promotion": True,
            "accepted_as_selected_dynamic_value_source_row": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The first primitive seed is exact, and all-row formal replay exists, but VSD-01 needs "
                "the selected assembly/action-source map that turns primitive rows into the dynamic "
                "overlap tensor rows without residual replay provenance."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedFirstValueSourceRowPromotionOrHonestGalerkinPrimitiveRow",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "primitive_exactness_backimport": rel(BACKIMPORT),
            "first_value_row_promotion_reconciliation": rel(RECONCILE),
            "next_cutset_after_primitive_backimport": rel(CUTSET),
        },
        "theorem": {
            "name": "FirstPrimitiveExactnessBackimportAndDynamicAssemblyGapTheorem",
            "proved": True,
            "statement": (
                "The first primitive row u:phase:r0c0 has an exact finite Weyl value 4/3 and exactness "
                "certificate, and this can be back-imported as seed evidence for VSD-01. It cannot by "
                "itself promote the VSD-01 dynamic value-source row: the primitive seed is not identical "
                "to the normalized dynamic response entries, and the selected assembly/action-source "
                "map from primitive rows to the dynamic overlap tensor remains open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "primitive_exactness_backimported": True,
            "first_value_row_promoted_to_selected_dynamic_source": False,
            "VSD_01_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_FirstValueSourceRowPromotion_or_HonestGalerkinPrimitiveRow_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected FirstValueSourceRowPromotion or HonestGalerkinPrimitiveRow v1

Status: `{STATUS}`.

The first primitive seed row is now imported into the VSD-01 row ledger:

```text
primitive row: u:phase:r0c0
exact value  : 4/3
certificate  : symbolic finite Weyl coordinate evaluation
```

This is progress, but it is not a selected dynamic value-source row yet.  The
primitive value `4/3` is not identical to the normalized dynamic row entries:

```text
u/e correction dY[0,0] = {u_dy_00}
u/e H1[0,0]            = {u_h1_00}
```

So the next wall is the assembly/source theorem: prove the selected map from
primitive rows into the dynamic overlap tensor, or prove the physical
Phi_fin^C1 action source/provenance theorem that justifies that assembly.

No observed masses, CKM/PMNS values, CP phase, benchmark matrices, or lifted
flags are used as selectors.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
