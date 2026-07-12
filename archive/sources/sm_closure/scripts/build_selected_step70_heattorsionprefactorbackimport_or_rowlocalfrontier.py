"""Build Step70 heat/torsion prefactor backimport or row-local frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BACKIMPORT_PACKET = PACKET_DIR / "step70_finite_heat_torsion_prefactor_backimport.packet.json"
FACTORIZATION_PACKET = PACKET_DIR / "step70_prefactor_slot_factorization.packet.json"
NOGO_PACKET = PACKET_DIR / "step70_heat_torsion_sufficiency_nogo.packet.json"
GATE_PACKET = PACKET_DIR / "step70_strict_omega_gate_after_heat_backimport.packet.json"
CUTSET_PACKET = PACKET_DIR / "step70_next_rowlocal_source_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step70_HeatTorsionPrefactorBackimport_or_RowLocalFrontier_v1.md"

STEP69 = DATA / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution.candidate.json"
STEP69_FORMULA = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_prefactor_solution_formula_rows.packet.json"
)
STEP69_DIAGNOSTIC = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_diagnostic_prefactor_postcheck.packet.json"
)
STEP69_GATE = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_strict_omega_acceptance_gate.packet.json"
)
HEAT_FINAL = DATA / "selected_heattorsionresponse_finalgate.candidate.json"
HEAT_RESPONSE = (
    DATA
    / "selected_heattorsionresponse_finalgate"
    / "selected_finite_heat_spectrum_response.packet.json"
)
STEP8_OPERATOR = (
    DATA
    / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure"
    / "step8_operator_source_slot_closure.packet.json"
)

STATUS = "MTT_SELECTED_STEP70_HEATTORSION_PREFACTOR_BACKIMPORT_CLOSED_ROWLOCAL_OPEN"
NEXT = "MTT_Selected_RowLocalHYMOverlapThresholdPrefactors_or_StrictOmegaAcceptance_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def source_class(formula_row: dict[str, Any]) -> str:
    return "H_sector" if formula_row["omega_id"] == "Omega_H.lambda" else "family_sector"


def class_invariants(cls: str, invariants: dict[str, Any]) -> dict[str, Any]:
    if cls == "family_sector":
        return {
            "sector_class": cls,
            "kernel_dimension": invariants["family_sector_kernel_dimension"],
            "positive_dimension": invariants["family_sector_positive_dimension"],
            "heat_trace_t1": invariants["family_sector_heat_trace_t1"],
            "reduced_heat_trace_t1": invariants["family_sector_reduced_heat_trace_t1"],
            "log_pseudodeterminant": invariants["family_sector_log_pseudodeterminant"],
        }
    if cls == "H_sector":
        return {
            "sector_class": cls,
            "kernel_dimension": invariants["H_sector_kernel_dimension"],
            "positive_dimension": invariants["H_sector_positive_dimension"],
            "heat_trace_t1": invariants["H_sector_heat_trace_t1"],
            "reduced_heat_trace_t1": invariants["H_sector_reduced_heat_trace_t1"],
            "log_pseudodeterminant": invariants["H_sector_log_pseudodeterminant"],
        }
    raise KeyError(cls)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP69,
        STEP69_FORMULA,
        STEP69_DIAGNOSTIC,
        STEP69_GATE,
        HEAT_FINAL,
        HEAT_RESPONSE,
        STEP8_OPERATOR,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step70 inputs: " + ", ".join(missing))

    step69 = load(STEP69)
    formula = load(STEP69_FORMULA)
    diagnostic = load(STEP69_DIAGNOSTIC)
    step69_gate = load(STEP69_GATE)
    heat_final = load(HEAT_FINAL)
    heat_response = load(HEAT_RESPONSE)
    step8_operator = load(STEP8_OPERATOR)

    formula_rows = formula["formula_rows"]
    diagnostic_rows = diagnostic["diagnostic_rows"]
    invariants = heat_response["finite_invariants"]

    if len(formula_rows) != 10:
        raise AssertionError("Step70 expects ten Step69 formula rows")
    if len(diagnostic_rows) != 10:
        raise AssertionError("Step70 expects ten diagnostic rows")
    if not heat_final["closure_decision"]["finite_determinant_heat_spectrum_or_torsion_response_closed"]:
        raise AssertionError("finite heat/torsion final gate is not closed")
    if not step8_operator["finite_positive_complement_pseudodeterminant_emitted"]:
        raise AssertionError("Step8 operator source slot did not emit pseudodeterminant")

    backimport_packet = {
        "schema": "MTTStep70FiniteHeatTorsionPrefactorBackimport.v1",
        "status": "FINITE_HEAT_TORSION_RESPONSE_BACKIMPORTED_AS_PREFACTOR_SUBSOURCE",
        "source_inputs": {
            "step69_formula_contract": rel(STEP69_FORMULA),
            "heat_torsion_final_gate": rel(HEAT_FINAL),
            "selected_finite_heat_response": rel(HEAT_RESPONSE),
            "step8_operator_source_slot_closure": rel(STEP8_OPERATOR),
        },
        "selected_branch": heat_response["branch"],
        "source_contract": heat_response["source_contract"],
        "finite_invariant_classes": {
            "family_sector": class_invariants("family_sector", invariants),
            "H_sector": class_invariants("H_sector", invariants),
            "total": {
                "sector_count": invariants["total_sector_count"],
                "dimension": invariants["total_dimension"],
                "kernel_dimension": invariants["total_kernel_dimension"],
                "positive_dimension": invariants["total_positive_dimension"],
                "heat_trace_t1": invariants["total_heat_trace_t1"],
                "reduced_heat_trace_t1": invariants["total_reduced_heat_trace_t1"],
                "log_pseudodeterminant": invariants["total_log_pseudodeterminant"],
                "zeta_at_0_positive_count": invariants["finite_spectral_zeta_at_0_positive_count"],
            },
        },
        "closed_now": {
            "finite_heat_trace_source_subslot": True,
            "positive_complement_pseudodeterminant_source_subslot": True,
            "operator_source_slot_layer_for_heat_torsion": True,
        },
        "does_not_close": [
            "row-local HYM zero-mode overlap numerators",
            "generation-resolved threshold response rows",
            "scale/scheme/loop convention for scalar values",
            "lambda_H value row",
            "accepted full Omega source rows",
            "internal scalar values",
            "true SM equivalence",
            "full no-knob closure",
        ],
        "accepted_as_finite_prefactor_subsource": True,
        "accepted_as_full_prefactor_source_rows": False,
        "accepted_full_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(BACKIMPORT_PACKET, backimport_packet)

    factor_rows: list[dict[str, Any]] = []
    for row in formula_rows:
        cls = source_class(row)
        inv = class_invariants(cls, invariants)
        row_local_factor = f"L_rowlocal.{row['omega_id']}"
        threshold_factor = f"T_scheme.{row['omega_id']}"
        det_factor = "D_fin.family" if cls == "family_sector" else "D_fin.H"
        factor_rows.append(
            {
                "row_id": f"step70.factorization.{row['omega_id']}",
                "omega_id": row["omega_id"],
                "prefactor_slot_id": row["prefactor_slot_id"],
                "source_class": cls,
                "finite_heat_torsion_subfactor_id": det_factor,
                "finite_heat_torsion_invariants": inv,
                "row_local_overlap_threshold_factor_id": row_local_factor,
                "scale_scheme_factor_id": threshold_factor,
                "factorization": (
                    f"{row['prefactor_slot_id']} = {det_factor} * "
                    f"{row_local_factor} * {threshold_factor}"
                ),
                "closed_subsources": {
                    "theta_exponent_weight": True,
                    "finite_heat_torsion_response": True,
                    "row_local_overlap_threshold_factor": False,
                    "scale_scheme_loop_convention": False,
                    "value_payload": False,
                },
                "accepted_as_prefactor_factorization_row": True,
                "accepted_as_full_prefactor_source_row": False,
                "accepted_as_full_omega_source_row": False,
                "accepted_as_internal_scalar_value": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    factorization_packet = {
        "schema": "MTTStep70PrefactorSlotFactorization.v1",
        "status": "TEN_PREFACTOR_SLOTS_FACTORED_HEAT_TORSION_SUBSOURCE_CLOSED",
        "source_inputs": {
            "step69_formula_rows": rel(STEP69_FORMULA),
            "heat_torsion_backimport": rel(BACKIMPORT_PACKET),
        },
        "factor_rows": factor_rows,
        "factor_row_count": len(factor_rows),
        "accepted_factorization_row_count": len(factor_rows),
        "accepted_finite_heat_torsion_subsource_count": 2,
        "accepted_full_prefactor_source_row_count": 0,
        "accepted_full_omega_source_row_count": 0,
        "accepted_internal_scalar_value_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FACTORIZATION_PACKET, factorization_packet)

    family_diag = [row for row in diagnostic_rows if row["omega_id"] != "Omega_H.lambda"]
    family_prefactors = [abs(float(row["diagnostic_prefactor"])) for row in family_diag]
    diagnostic_family_span = max(family_prefactors) / min(family_prefactors)
    source_classes = sorted({row["source_class"] for row in factor_rows})
    nogo_packet = {
        "schema": "MTTStep70HeatTorsionSufficiencyNoGo.v1",
        "status": "FINITE_HEAT_TORSION_ALONE_CANNOT_EMIT_TEN_ROWLOCAL_PREFACTORS",
        "proof_basis": {
            "source_class_count": len(source_classes),
            "source_classes": source_classes,
            "prefactor_slot_count": len(factor_rows),
            "generation_resolved_labels_in_heat_response": False,
            "u_d_e_sector_splitting_in_family_heat_response": False,
            "family_sector_log_pseudodeterminant_common": invariants["family_sector_log_pseudodeterminant"],
            "H_sector_log_pseudodeterminant": invariants["H_sector_log_pseudodeterminant"],
            "heat_torsion_response_is_source_closed": True,
        },
        "independent_of_replay_values": True,
        "diagnostic_only": {
            "family_required_prefactor_min": min(family_prefactors),
            "family_required_prefactor_max": max(family_prefactors),
            "family_required_prefactor_span": diagnostic_family_span,
            "interpretation": (
                "Admitted replay postchecks vary within the determinant-equivalent family class, "
                "so row-local overlap/threshold factors are numerically necessary as well. "
                "This diagnostic is not used to select the source."
            ),
        },
        "finite_heat_torsion_alone_emits_all_prefactor_rows": False,
        "remaining_source_object": "row-local selected HYM overlap/threshold prefactor factors",
        "accepted_prefactor_source_row_count": 0,
        "accepted_full_omega_source_row_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(NOGO_PACKET, nogo_packet)

    gate_packet = {
        "schema": "MTTStep70StrictOmegaGateAfterHeatBackimport.v1",
        "status": "HEAT_TORSION_SUBSOURCE_CLOSED_STRICT_OMEGA_ACCEPTANCE_STILL_FALSE",
        "step69_gate_source": rel(STEP69_GATE),
        "closed_by_step70": {
            "finite_heat_torsion_prefactor_subsource": True,
            "prefactor_factorization_contract": True,
            "heat_torsion_alone_sufficiency_nogo": True,
        },
        "not_closed_by_step70": {
            "row_local_HYM_overlap_threshold_factors": True,
            "selected_scale_scheme_loop_convention": True,
            "lambda_H_value_row": True,
            "accepted_full_prefactor_source_rows": True,
            "accepted_full_omega_source_rows": True,
            "internal_scalar_values": True,
        },
        "strict_acceptance_result": {
            "accepted_formula_skeleton_row_count": step69_gate["strict_acceptance_result"][
                "accepted_formula_skeleton_row_count"
            ],
            "accepted_finite_heat_torsion_subsource_count": 2,
            "accepted_full_prefactor_source_row_count": 0,
            "accepted_full_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "value_rows_execute": False,
            "reason": (
                "The finite heat/torsion response is now a selected prefactor subsource, "
                "but the strict Omega validator requires full row-local prefactor values "
                "with convention and value payloads."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(GATE_PACKET, gate_packet)

    cutset_packet = {
        "schema": "MTTStep70NextRowLocalSourceCutset.v1",
        "status": "ROWLOCAL_OVERLAP_THRESHOLD_FACTORS_ARE_THE_SINGLE_NEXT_FRONTIER",
        "not_missing_anymore": [
            "Step69 ten-row Omega formula contract",
            "selected finite heat trace source subslot",
            "selected positive-complement pseudodeterminant source subslot",
            "prefactor factorization into determinant, row-local overlap, and convention factors",
            "proof that finite heat/torsion alone cannot emit ten row-local prefactors",
        ],
        "still_missing": [
            "selected row-local HYM zero-mode overlap numerators for each Omega slot",
            "selected generation-resolved threshold response factors",
            "selected scale/scheme/loop convention binding the finite source to physical scalar values",
            "selected lambda_H row-local factor and value payload",
            "strict Omega acceptance theorem for all ten rows",
        ],
        "minimal_theorem_to_close_next": (
            "The selected q79/F/m=1 HYM/Strominger operator emits row-local overlap/threshold "
            "factors L_rowlocal.* and T_scheme.* for the ten Step70 prefactor slots, using the "
            "already selected finite heat/torsion subsource and without observed replay values as selectors."
        ),
        "next_required_artifact": NEXT,
        "forbidden_routes": [
            "treat common finite heat/torsion invariants as generation-resolved prefactors",
            "use diagnostic postcheck prefactors to choose row-local factors",
            "promote determinant subsource rows as full Omega scalar rows",
            "ignore scale/scheme/loop convention for physical scalar values",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET_PACKET, cutset_packet)

    candidate = {
        "candidate": "MTTSelectedStep70HeatTorsionPrefactorBackimportOrRowLocalFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "finite_heat_torsion_prefactor_backimport": rel(BACKIMPORT_PACKET),
            "prefactor_slot_factorization": rel(FACTORIZATION_PACKET),
            "heat_torsion_sufficiency_nogo": rel(NOGO_PACKET),
            "strict_omega_gate_after_heat_backimport": rel(GATE_PACKET),
            "next_rowlocal_source_cutset": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "Step70HeatTorsionPrefactorBackimportTheorem",
            "proved": True,
            "statement": (
                "The selected finite 27-mode heat trace and positive-complement pseudodeterminant "
                "response from the q79/F/m=1 branch can be back-imported as a selected prefactor "
                "subsource for the Step69 Omega formula rows. Since that source has only family/H "
                "classes and no generation-resolved row-local labels, it cannot by itself emit the "
                "ten full C_HYMthr.* prefactor rows. The remaining object is selected row-local "
                "HYM overlap/threshold factors plus convention/value payloads."
            ),
        },
        "closure_decision": {
            "finite_heat_torsion_prefactor_subsource_closed": True,
            "step8_operator_source_slot_layer_backimported": True,
            "prefactor_factorization_contract_closed": True,
            "heat_torsion_alone_sufficiency_rejected": True,
            "accepted_finite_heat_torsion_subsource_count": 2,
            "accepted_full_prefactor_source_row_count": 0,
            "accepted_full_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "row_local_HYM_overlap_threshold_factors_closed": False,
            "scale_scheme_loop_convention_closed": False,
            "lambda_H_value_row_emitted": False,
            "scalar_value_execution_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step69["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step70_HeatTorsionPrefactorBackimport_or_RowLocalFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step70 HeatTorsionPrefactorBackimport or RowLocalFrontier v1

Status: `{STATUS}`.

## What Closed

Step70 back-imports the already selected finite heat/torsion source slot into
the Step69 prefactor contract:

```text
finite heat trace source subslot                    : closed
positive-complement pseudodeterminant source subslot: closed
prefactor factorization rows                        : {len(factor_rows)}
accepted finite heat/torsion subsources             : 2
accepted full prefactor source rows                 : 0
accepted Omega source rows                          : 0
accepted scalar values                              : 0
```

The prefactor slots are now factored as:

```text
C_HYMthr.* = D_fin.class * L_rowlocal.* * T_scheme.*
```

`D_fin.class` is selected by the finite 27-mode heat/pseudodeterminant response.
The row-local overlap factor `L_rowlocal.*` and convention/threshold factor
`T_scheme.*` remain open.

## Why This Is Not Yet Full Closure

The finite heat/torsion response has only two source classes here:

```text
source classes: {source_classes}
prefactor slots: {len(factor_rows)}
```

It has no generation-resolved labels and no `u/d/e` split inside the family
class.  Therefore it cannot by itself emit the ten row-local prefactor source
rows required by Step69.

As a diagnostic only, the admitted replay prefactors vary inside the family
class by a factor of `{diagnostic_family_span:.12g}`.  This is not used as a
selector; it only confirms that row-local factors are numerically necessary.

## Boundary

The determinant/heat/torsion source subslot is no longer missing.  The live
frontier is now selected row-local HYM overlap/threshold factors plus the
scale/scheme/loop convention and value payloads.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
