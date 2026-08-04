"""Audit Step70 heat/torsion prefactor backimport or row-local frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BACKIMPORT_PACKET = PACKET_DIR / "step70_finite_heat_torsion_prefactor_backimport.packet.json"
FACTORIZATION_PACKET = PACKET_DIR / "step70_prefactor_slot_factorization.packet.json"
NOGO_PACKET = PACKET_DIR / "step70_heat_torsion_sufficiency_nogo.packet.json"
GATE_PACKET = PACKET_DIR / "step70_strict_omega_gate_after_heat_backimport.packet.json"
CUTSET_PACKET = PACKET_DIR / "step70_next_rowlocal_source_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_Step70_HeatTorsionPrefactorBackimport_or_RowLocalFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_STEP70_HEATTORSION_PREFACTOR_BACKIMPORT_CLOSED_ROWLOCAL_OPEN"
NEXT = "MTT_Selected_RowLocalHYMOverlapThresholdPrefactors_or_StrictOmegaAcceptance_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    backimport = load(BACKIMPORT_PACKET)
    factorization = load(FACTORIZATION_PACKET)
    nogo = load(NOGO_PACKET)
    gate = load(GATE_PACKET)
    cutset = load(CUTSET_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem missing")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    for item in [data, backimport, factorization, nogo, gate, cutset, cert]:
        require(item.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(item.get("target_fitting_used") is False, "target fitting violation")

    require(backimport["accepted_as_finite_prefactor_subsource"] is True, "finite subsource not accepted")
    require(backimport["accepted_as_full_prefactor_source_rows"] is False, "full prefactors overaccepted")
    require(backimport["accepted_full_omega_source_row_count"] == 0, "Omega rows overaccepted")
    require(backimport["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    for key in [
        "finite_heat_trace_source_subslot",
        "positive_complement_pseudodeterminant_source_subslot",
        "operator_source_slot_layer_for_heat_torsion",
    ]:
        require(backimport["closed_now"][key] is True, f"backimport did not close {key}")
    for phrase in [
        "row-local HYM zero-mode overlap numerators",
        "generation-resolved threshold response rows",
        "scale/scheme/loop convention for scalar values",
        "accepted full Omega source rows",
    ]:
        require(phrase in backimport["does_not_close"], f"backimport missing guard: {phrase}")

    inv_classes = backimport["finite_invariant_classes"]
    require(inv_classes["family_sector"]["positive_dimension"] == 24, "family positive dimension mismatch")
    require(inv_classes["H_sector"]["positive_dimension"] == 26, "H positive dimension mismatch")
    require(inv_classes["total"]["positive_dimension"] == 170, "total positive dimension mismatch")
    require(inv_classes["total"]["kernel_dimension"] == 19, "total kernel dimension mismatch")

    rows = factorization["factor_rows"]
    require(factorization["factor_row_count"] == 10, "factor row count mismatch")
    require(factorization["accepted_factorization_row_count"] == 10, "factorization count mismatch")
    require(factorization["accepted_finite_heat_torsion_subsource_count"] == 2, "subsource count mismatch")
    require(factorization["accepted_full_prefactor_source_row_count"] == 0, "prefactor rows overaccepted")
    require(factorization["accepted_full_omega_source_row_count"] == 0, "Omega rows overaccepted")
    require(factorization["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require({row["source_class"] for row in rows} == {"family_sector", "H_sector"}, "source classes mismatch")
    require(sum(1 for row in rows if row["source_class"] == "family_sector") == 9, "family class count mismatch")
    require(sum(1 for row in rows if row["source_class"] == "H_sector") == 1, "H class count mismatch")
    for row in rows:
        closed = row["closed_subsources"]
        require(closed["theta_exponent_weight"] is True, f"theta not closed {row['omega_id']}")
        require(closed["finite_heat_torsion_response"] is True, f"heat not closed {row['omega_id']}")
        require(closed["row_local_overlap_threshold_factor"] is False, f"row-local overclosed {row['omega_id']}")
        require(closed["scale_scheme_loop_convention"] is False, f"scheme overclosed {row['omega_id']}")
        require(row["accepted_as_prefactor_factorization_row"] is True, f"factor row missing {row['omega_id']}")
        require(row["accepted_as_full_prefactor_source_row"] is False, f"prefactor overaccepted {row['omega_id']}")
        require(row["accepted_as_full_omega_source_row"] is False, f"Omega overaccepted {row['omega_id']}")
        require("D_fin." in row["factorization"], f"missing determinant factor {row['omega_id']}")
        require("L_rowlocal." in row["factorization"], f"missing row-local factor {row['omega_id']}")
        require("T_scheme." in row["factorization"], f"missing scheme factor {row['omega_id']}")

    proof = nogo["proof_basis"]
    require(nogo["finite_heat_torsion_alone_emits_all_prefactor_rows"] is False, "nogo overclosed")
    require(nogo["independent_of_replay_values"] is True, "nogo should be structural")
    require(proof["source_class_count"] == 2, "source class count mismatch")
    require(proof["prefactor_slot_count"] == 10, "prefactor slot count mismatch")
    require(proof["generation_resolved_labels_in_heat_response"] is False, "generation labels overclaimed")
    require(proof["u_d_e_sector_splitting_in_family_heat_response"] is False, "u/d/e split overclaimed")
    require(proof["heat_torsion_response_is_source_closed"] is True, "heat source should be closed")
    require(nogo["diagnostic_only"]["family_required_prefactor_span"] > 10.0, "diagnostic span should show row-local need")
    require(nogo["accepted_prefactor_source_row_count"] == 0, "nogo prefactor rows overaccepted")
    require(nogo["accepted_full_omega_source_row_count"] == 0, "nogo Omega rows overaccepted")

    strict = gate["strict_acceptance_result"]
    require(gate["closed_by_step70"]["finite_heat_torsion_prefactor_subsource"] is True, "gate heat subsource missing")
    require(gate["closed_by_step70"]["prefactor_factorization_contract"] is True, "gate factorization missing")
    require(gate["closed_by_step70"]["heat_torsion_alone_sufficiency_nogo"] is True, "gate nogo missing")
    for key in [
        "row_local_HYM_overlap_threshold_factors",
        "selected_scale_scheme_loop_convention",
        "lambda_H_value_row",
        "accepted_full_prefactor_source_rows",
        "accepted_full_omega_source_rows",
        "internal_scalar_values",
    ]:
        require(gate["not_closed_by_step70"][key] is True, f"gate overclosed: {key}")
    require(strict["accepted_formula_skeleton_row_count"] == 10, "strict formula count mismatch")
    require(strict["accepted_finite_heat_torsion_subsource_count"] == 2, "strict subsource count mismatch")
    require(strict["accepted_full_prefactor_source_row_count"] == 0, "strict prefactors overaccepted")
    require(strict["accepted_full_omega_source_row_count"] == 0, "strict Omega overaccepted")
    require(strict["accepted_internal_scalar_value_row_count"] == 0, "strict scalar overaccepted")
    require(strict["value_rows_execute"] is False, "strict values executed early")

    for phrase in [
        "selected row-local HYM zero-mode overlap numerators for each Omega slot",
        "selected generation-resolved threshold response factors",
        "selected scale/scheme/loop convention binding the finite source to physical scalar values",
        "strict Omega acceptance theorem for all ten rows",
    ]:
        require(phrase in cutset["still_missing"], f"cutset missing: {phrase}")
    for phrase in [
        "treat common finite heat/torsion invariants as generation-resolved prefactors",
        "use diagnostic postcheck prefactors to choose row-local factors",
        "promote determinant subsource rows as full Omega scalar rows",
    ]:
        require(phrase in cutset["forbidden_routes"], f"forbidden route missing: {phrase}")

    decision = data["closure_decision"]
    for key in [
        "finite_heat_torsion_prefactor_subsource_closed",
        "step8_operator_source_slot_layer_backimported",
        "prefactor_factorization_contract_closed",
        "heat_torsion_alone_sufficiency_rejected",
    ]:
        require(decision[key] is True, f"decision did not close {key}")
        require(cert[key] is True, f"certificate did not close {key}")
    for key in [
        "row_local_HYM_overlap_threshold_factors_closed",
        "scale_scheme_loop_convention_closed",
        "lambda_H_value_row_emitted",
        "scalar_value_execution_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision overclosed {key}")
        require(cert[key] is False, f"certificate overclosed {key}")
    require(decision["accepted_full_prefactor_source_row_count"] == 0, "decision prefactors overaccepted")
    require(decision["accepted_full_omega_source_row_count"] == 0, "decision Omega overaccepted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "decision scalar overaccepted")

    for phrase in [
        "finite heat trace source subslot                    : closed",
        "positive-complement pseudodeterminant source subslot: closed",
        "prefactor factorization rows                        : 10",
        "accepted full prefactor source rows                 : 0",
        "C_HYMthr.* = D_fin.class * L_rowlocal.* * T_scheme.*",
        NEXT,
    ]:
        require(phrase in note, f"note missing: {phrase}")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
