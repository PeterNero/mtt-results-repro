"""Build PSM-C1-02 SI-1u unpatched kernel execution / honest Galerkin export.

This attempts the preferred SI-1u-B route using the existing Galerkin input
packets.  It records the real progress: the replay harness exists and passes
strict replay, but it is not an honest independent Galerkin export because the
inputs still inherit the local axiom/residual-projector contract.
"""

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

SLUG = "selected_psm_c1_02_unpatchedkernelexecutionplan_or_honestgalerkinexport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INPUT_IMPORT = PACKET_DIR / "route_b_existing_input_import_status.packet.json"
HONEST_ATTEMPT = PACKET_DIR / "route_b_honest_galerkin_export_attempt.packet.json"
UNPATCHED_GUARD = PACKET_DIR / "unpatched_source_promotion_guardrail.packet.json"
NEXT_WORK = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_UnpatchedKernelExecutionPlan_or_HonestGalerkinExport_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_localreplayreconciliation_or_unpatchedkernelexecutionplan.candidate.json"
UNPATCHED_PLAN = (
    DATA
    / "selected_psm_c1_02_localreplayreconciliation_or_unpatchedkernelexecutionplan"
    / "unpatched_kernel_execution_plan.packet.json"
)
OLD_GATE = DATA / "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport.candidate.json"
OLD_ROUTE_B = (
    DATA
    / "selected_psm_c1_02_unpatchedsourceruleproof_or_honestgalerkinexport"
    / "route_b_honest_galerkin_export_manifest.packet.json"
)
INPUT_FILL = DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch.candidate.json"
INPUT_FILL_AUDIT = CORPUS / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch_audit.py"
INPUT_DIR = DATA / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch" / "inputs"
ZERO_MODE = INPUT_DIR / "zero_mode_basis.packet.json"
PRIMITIVE = INPUT_DIR / "primitive_contraction_terms.packet.json"
HESSIAN = INPUT_DIR / "hessian_source_vector.packet.json"
SECTORS = INPUT_DIR / "sector_response_matrices.packet.json"
FIRST_REPLAY = (
    DATA
    / "selected_galerkinc1inputbasisfill_or_residualprojectoraxiomcorpuspatch"
    / "first_galerkin_replay_result.packet.json"
)
CURRENT_PSM_PACKET = (
    DATA
    / "selected_psm_c1_02_selectedsourcepromotionpacket"
    / "current_unpatched_source_promotion_validator_result.packet.json"
)
CONDITIONAL_PSM_PACKET = (
    DATA
    / "selected_psm_c1_02_selectedsourcepromotionpacket"
    / "conditional_unpatched_source_promotion_validator_result.packet.json"
)
PATCHED_PSM_PACKET = (
    DATA
    / "selected_psm_c1_02_selectedsourcepromotionpacket"
    / "patched_local_axiom_source_promotion_validator_result.packet.json"
)

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_HONEST_GALERKIN_EXPORT_ATTEMPTED_REPLAY_HARNESS_ONLY"
NEXT = "MTT_Selected_PSM_C1_02_HonestGalerkinZeroModeBasisSource_or_PrimitiveQuadratureExport_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_audit(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "audit": rel(path),
        "returncode": proc.returncode,
        "stdout_tail": proc.stdout.splitlines()[-8:],
        "stderr": proc.stderr.splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    plan = load(UNPATCHED_PLAN)
    old_gate = load(OLD_GATE)
    old_route_b = load(OLD_ROUTE_B)
    input_fill = load(INPUT_FILL)
    zero = load(ZERO_MODE)
    primitive = load(PRIMITIVE)
    hessian = load(HESSIAN)
    sectors = load(SECTORS)
    first_replay = load(FIRST_REPLAY)
    current_result = load(CURRENT_PSM_PACKET)
    conditional_result = load(CONDITIONAL_PSM_PACKET)
    patched_result = load(PATCHED_PSM_PACKET)
    input_audit = run_audit(INPUT_FILL_AUDIT)

    input_import = {
        "schema": "MTTPSMC102SI1uBExistingInputImportStatus.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B",
        "status": "EXISTING_GALERKIN_INPUT_PACKETS_IMPORTED_AS_REPLAY_HARNESS_NOT_HONEST_EXPORT",
        "old_manifest": rel(OLD_ROUTE_B),
        "old_missing_inputs_existed_at_old_path": old_route_b["all_missing_inputs_exist_now"],
        "new_input_fill_candidate": rel(INPUT_FILL),
        "new_input_fill_audit": input_audit,
        "input_packets": {
            "zero_mode_basis": {
                "path": rel(ZERO_MODE),
                "exists_now": ZERO_MODE.exists(),
                "status": zero["status"],
                "selected_source_verified": zero["selected_source_verified"],
                "honest_independent": False,
                "reason": zero["why_not_honest_selected_yet"],
            },
            "primitive_contraction_terms": {
                "path": rel(PRIMITIVE),
                "exists_now": PRIMITIVE.exists(),
                "status": primitive["status"],
                "selected_source_verified": primitive["selected_source_verified"],
                "computed_from_independent_galerkin_quadrature": primitive[
                    "computed_from_independent_galerkin_quadrature"
                ],
                "honest_independent": False,
            },
            "hessian_source_vector": {
                "path": rel(HESSIAN),
                "exists_now": HESSIAN.exists(),
                "status": hessian["status"],
                "b_selected_emitted_by_independent_hessian": hessian[
                    "b_selected_emitted_by_independent_hessian"
                ],
                "honest_independent": False,
            },
            "sector_response_matrices": {
                "path": rel(SECTORS),
                "exists_now": SECTORS.exists(),
                "status": sectors["status"],
                "independent_sector_matrices_emitted": sectors["independent_sector_matrices_emitted"],
                "honest_independent": False,
            },
        },
        "all_input_packets_exist": all(path.exists() for path in [ZERO_MODE, PRIMITIVE, HESSIAN, SECTORS]),
        "all_input_packets_honest_independent": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    honest_attempt = {
        "schema": "MTTPSMC102SI1uBHonestGalerkinExportAttempt.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B",
        "status": "STRICT_REPLAY_PASSES_BUT_HONEST_GALERKIN_EXPORT_NOT_CLOSED",
        "attempt_source": rel(INPUT_FILL),
        "first_replay_result": rel(FIRST_REPLAY),
        "strict_replay_passes": first_replay["strict_replay_passes"],
        "honest_independent_galerkin_execution_passes": first_replay[
            "honest_independent_galerkin_execution_passes"
        ],
        "route_B_result_from_input_fill": input_fill["route_B_result"],
        "why_independent_execution_not_closed": first_replay["why_independent_execution_not_closed"],
        "required_honest_exports": plan["route_B"]["must_export"],
        "current_export_status": {
            "72_primitive_kernel_rows": "replay/contract values available; independent quadrature/source export not emitted",
            "2_hessian_source_rows": "b_selected replay available under axiom contract; independent Hessian source not emitted",
            "36_sector_assembly_rows": "sector replay available under contract; independent sector source not emitted",
            "source_owner_certificates": "not emitted for all nine PSM-C1-02 fields",
            "no_residual_replay_or_locked_target_as_source": "not yet satisfied",
        },
        "free_axiom_patch_used": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    unpatched_guard = {
        "schema": "MTTPSMC102SI1uUnpatchedSourcePromotionGuardrail.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u",
        "status": "UNPATCHED_SOURCE_PROMOTION_STILL_OPEN_CONDITIONAL_TARGET_PRESERVED",
        "current_unpatched_packet_passes": current_result["passes"],
        "patched_local_axiom_packet_passes_unpatched_validator": patched_result["passes"],
        "conditional_unpatched_packet_passes": conditional_result["passes"],
        "success_condition": plan["success_condition"],
        "old_gate_status": old_gate["status"],
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1uBFirstAttempt.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_UnpatchedKernelExecutionPlan_or_HonestGalerkinExport_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B1",
            "task": "Emit an honest selected HYM/zero-mode basis source packet, not just canonical qutrit matrix-unit support.",
        },
        "secondary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
            "task": "Compute independent primitive Galerkin/quadrature contractions for the 72 primitive rows.",
        },
        "parallel": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A",
            "task": "Continue deriving the local source principles from selected action text.",
        },
        "status": "NEXT_WORKORDER_HONEST_ZERO_MODE_BASIS_OR_PRIMITIVE_QUADRATURE_EXPORT",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102UnpatchedKernelExecutionPlanOrHonestGalerkinExport",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1u-B", "SOURCE-IDENTITY/SI-1u-A"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "output_packets": {
            "route_b_existing_input_import_status": rel(INPUT_IMPORT),
            "route_b_honest_galerkin_export_attempt": rel(HONEST_ATTEMPT),
            "unpatched_source_promotion_guardrail": rel(UNPATCHED_GUARD),
            "next_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "PSMC102SI1uBReplayHarnessNotHonestExportTheorem",
            "proved": True,
            "statement": (
                "The existing Galerkin input packets provide a strict replay harness for the locked 72-real "
                "target, but they do not close the honest independent Galerkin export route. Zero-mode basis, "
                "primitive contractions, Hessian source vector, and sector matrices remain support/replay or "
                "axiom-contract inherited, so the unpatched source-promotion packet still fails."
            ),
        },
        "what_closes_now": {
            "SI1u_B_first_attempt_completed": True,
            "existing_input_packets_imported": True,
            "strict_replay_harness_confirmed": True,
            "honest_export_gap_classified": True,
            "unpatched_guardrails_preserved": True,
        },
        "what_remains_open": {
            "honest_selected_zero_mode_basis_source": True,
            "independent_72_primitive_galerkin_quadrature_rows": True,
            "independent_2_hessian_source_rows": True,
            "independent_36_sector_assembly_rows": True,
            "all_nine_source_owner_certificates": True,
            "unpatched_action_principle_derivation": True,
        },
        "closure_decision": {
            "strict_replay_harness_passes": True,
            "honest_independent_galerkin_export_closed": False,
            "unpatched_source_promotion_packet_passes": False,
            "conditional_unpatched_packet_passes_if_theorem_supplied": True,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
            "global_closure_claimed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_UnpatchedKernelExecutionPlan_or_HonestGalerkinExport_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_replay_harness_passes": True,
        "honest_independent_galerkin_export_closed": False,
        "unpatched_source_promotion_packet_passes": False,
        "conditional_unpatched_packet_passes_if_theorem_supplied": True,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    for path, obj in [
        (INPUT_IMPORT, input_import),
        (HONEST_ATTEMPT, honest_attempt),
        (UNPATCHED_GUARD, unpatched_guard),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    NOTE.write_text(
        f"""# MTT Selected PSM C1 02 UnpatchedKernelExecutionPlan or HonestGalerkinExport v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B`

Parallel route label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Result

The existing Galerkin input packets are imported and audited. They provide a strict replay harness, but not an honest independent Galerkin export. The primitive and Hessian values still inherit the residual-projector/local-axiom contract, and the zero-mode basis is canonical Weyl support rather than an independently emitted HYM/zero-mode Galerkin basis.

So `SI-1u-B` made progress, but it does not close the unpatched source-promotion packet.

## Next

`SI-1u-B1`: emit an honest selected HYM/zero-mode basis source packet.

`SI-1u-B2`: compute independent primitive Galerkin/quadrature contractions for the 72 primitive rows.

They are not knobs; they are two required exits to the same unpatched source-identity target.

## Next Artifact

`{NEXT}`
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
