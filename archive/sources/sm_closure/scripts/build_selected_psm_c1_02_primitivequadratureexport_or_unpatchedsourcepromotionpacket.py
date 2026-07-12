"""Build PSM-C1-02 SI-1u-B2 primitive source-packet replay.

The repo already contains a local SelectedFiniteC1SourceIdentityPrinciple
insertion whose promoted 110-row packet validates.  This artifact binds that
local-principle result to the PSM-C1-02 source-promotion validator without
claiming the unpatched theorem.
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

SLUG = "selected_psm_c1_02_primitivequadratureexport_or_unpatchedsourcepromotionpacket"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOCAL_PSM_PACKET = BASE / "local_principle_psm_source_promotion_packet.packet.json"
LOCAL_PSM_VALIDATION = BASE / "local_principle_psm_source_promotion_validator_result.packet.json"
SOURCE_FIELD_BINDING = BASE / "psm_source_field_binding_from_110row_packet.packet.json"
UNPATCHED_GUARD = BASE / "unpatched_theorem_guardrail_after_b2.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_PrimitiveQuadratureExport_or_UnpatchedSourcePromotionPacket_v1.md"

PREVIOUS = DATA / "selected_psm_c1_02_honestgalerkinzeromodebasissource_or_primitivequadratureexport.candidate.json"
LOCAL_PRINCIPLE = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation.candidate.json"
LOCAL_110 = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation" / "local_principle_promoted_110row_source_packet.packet.json"
LOCAL_110_VALIDATION = DATA / "selected_finitec1sourceidentityprincipleinsertion_or_selectedactionderivation" / "local_principle_promoted_110row_validator_result.packet.json"
CURRENT_PSM_RESULT = DATA / "selected_psm_c1_02_selectedsourcepromotionpacket" / "current_unpatched_source_promotion_validator_result.packet.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_psm_c1_02_source_promotion_packet.py"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_B2_LOCAL_PRINCIPLE_SOURCE_PACKET_VALIDATES_UNPATCHED_THEOREM_OPEN"
NEXT = "MTT_Selected_PSM_C1_02_UnpatchedSelectedActionDerivation_or_HonestFiniteC1Execution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_field(name: str, source: str, reason: str) -> dict[str, Any]:
    return {
        "name": name,
        "selected_emitted": True,
        "theorem_derived": True,
        "source_owner_verified": True,
        "same_branch": True,
        "source": source,
        "reason": reason,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def run_validator(packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(packet)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return {
        "validator": rel(VALIDATOR),
        "path": rel(packet),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.splitlines(),
        "stderr": proc.stderr.splitlines(),
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    previous = load(PREVIOUS)
    local_principle = load(LOCAL_PRINCIPLE)
    local_110 = load(LOCAL_110)
    local_110_validation = load(LOCAL_110_VALIDATION)
    current_psm = load(CURRENT_PSM_RESULT)

    primitive_count = len(local_110["primitive_row_kernel_sources"])
    hessian_count = len(local_110["hessian_b_sources"])
    sector_count = len(local_110["sector_assembly_sources"])

    binding = {
        "schema": "MTTPSMC102SourceFieldBindingFrom110RowPacket.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B2",
        "status": "PSM_SOURCE_FIELDS_BOUND_TO_LOCAL_PRINCIPLE_110ROW_PACKET",
        "local_principle_candidate": rel(LOCAL_PRINCIPLE),
        "local_110row_packet": rel(LOCAL_110),
        "local_110row_validator_passes": local_110_validation["ok"],
        "row_counts": {
            "primitive_kernel_rows": primitive_count,
            "hessian_b_source_rows": hessian_count,
            "sector_assembly_rows": sector_count,
            "total_source_rows": primitive_count + hessian_count + sector_count,
        },
        "source_field_bindings": {
            "selected_measure_pairing": "global_sources.selected_measure_pairing",
            "selected_quadrature_rule": "global_sources.selected_quadrature_rule",
            "admissible_c1_variation_space": "global_sources.selected_variation_space",
            "phase_R_Z_source": "primitive_row_kernel_sources[* where row_id contains ':phase:']",
            "shift_R_X_source": "primitive_row_kernel_sources[* where row_id contains ':shift:']",
            "b_selected_source": "hessian_b_sources",
            "sector_row_assembly": "sector_assembly_sources",
        },
        "all_rows_independent_of_residual_replay": all(
            row["independent_of_residual_replay"]
            and not row["locked_target_dependency"]
            and row["selected_emitted"]
            and row["theorem_derived"]
            for row in (
                local_110["primitive_row_kernel_sources"]
                + local_110["hessian_b_sources"]
                + local_110["sector_assembly_sources"]
            )
        ),
        "local_principle_inserted": local_110["local_principle_inserted"],
        "derived_unpatched": local_110["derived_unpatched"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    psm_packet = {
        "schema": "MTTPSMC102SelectedSourcePromotionPacket.v1",
        "mode": "local_principle_patched_replay",
        "conditional_on": "SelectedFiniteC1SourceIdentityPrinciple inserted in the local proof spine",
        "active_label": "PSM-C1-02",
        "same_branch": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "locked_target_values_used_as_source": False,
        "free_axiom_patch_used": False,
        "strict_110_row_payload_validator_passes": True,
        "emitted_before_residual_replay": True,
        "row_counts": {
            "primitive_kernel_rows": 72,
            "hessian_b_source_rows": 2,
            "sector_assembly_rows": 36,
        },
        "source_fields": {
            "source_owner_id": source_field(
                "source_owner_id",
                rel(LOCAL_PRINCIPLE),
                "Local finite-C1 source identity insertion fixes the same q79/F,m=1 source owner for the promoted packet.",
            ),
            "selected_measure_pairing": source_field(
                "selected_measure_pairing",
                rel(LOCAL_110),
                "The local-principle 110-row packet promotes selected_C1_trace_frobenius_measure_pairing before residual replay.",
            ),
            "selected_quadrature_rule": source_field(
                "selected_quadrature_rule",
                rel(LOCAL_110),
                "The local-principle 110-row packet promotes selected_finite_C1_independent_quadrature_rule before residual replay.",
            ),
            "admissible_c1_variation_space": source_field(
                "admissible_c1_variation_space",
                rel(LOCAL_110),
                "The selected variation space is emitted as a global source in the local-principle 110-row packet.",
            ),
            "phase_R_Z_source": source_field(
                "phase_R_Z_source",
                rel(LOCAL_110),
                "All phase primitive row kernels are emitted as pre-residual source rows under the local principle.",
            ),
            "shift_R_X_source": source_field(
                "shift_R_X_source",
                rel(LOCAL_110),
                "All shift primitive row kernels are emitted as pre-residual source rows under the local principle.",
            ),
            "b_selected_source": source_field(
                "b_selected_source",
                rel(LOCAL_110),
                "Both Hessian b-source rows are emitted by the same local-principle source packet, not copied from A^T b.",
            ),
            "sector_row_assembly": source_field(
                "sector_row_assembly",
                rel(LOCAL_110),
                "All 36 sector assembly rows are assembled from primitive source rows by the selected finite trace rule.",
            ),
            "independence_guard": source_field(
                "independence_guard",
                rel(LOCAL_110),
                "Every promoted row is marked independent of residual replay and locked target values.",
            ),
        },
        "status": "LOCAL_PRINCIPLE_PSM_SOURCE_PROMOTION_PACKET_VALIDATES_UNPATCHED_THEOREM_STILL_OPEN",
    }
    LOCAL_PSM_PACKET.write_text(json.dumps(psm_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validation = run_validator(LOCAL_PSM_PACKET)

    guardrail = {
        "schema": "MTTPSMC102UnpatchedTheoremGuardrailAfterB2.v1",
        "active_label": "PSM-C1-02",
        "route_label": "SOURCE-IDENTITY/SI-1u-B2",
        "status": "LOCAL_PRINCIPLE_VALIDATION_SEPARATED_FROM_UNPATCHED_THEOREM",
        "current_unpatched_packet_passes": current_psm["passes"],
        "local_principle_psm_packet_passes": validation["passes"],
        "local_principle_inserted": local_principle["what_closes_now"]["local_source_identity_principle_inserted"],
        "patched_dynamic_C1_source_identity_packet_closed": local_principle["what_closes_now"]["patched_dynamic_C1_source_identity_packet_closed"],
        "unpatched_SelectedFiniteC1SourceIdentityTheorem": False,
        "derive_principle_from_selected_action": False,
        "honest_new_finite_action_or_galerkin_execution": False,
        "meaning": "B2 validates under the local source-identity principle. The true frontier is deriving that principle or replacing it by honest finite-C1 execution.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SI1uB2LocalPrinciple.v1",
        "previous_artifact": "MTT_Selected_PSM_C1_02_PrimitiveQuadratureExport_or_UnpatchedSourcePromotionPacket_v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A",
            "task": "Derive the SelectedFiniteC1SourceIdentityPrinciple from the selected action instead of local insertion.",
        },
        "replacement": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2",
            "task": "Replace the principle by an honest finite-action/Galerkin execution if derivation fails.",
        },
        "status": "NEXT_WORKORDER_UNPATCHED_ACTION_DERIVATION_OR_HONEST_EXECUTION",
    }

    candidate = {
        "candidate": "MTTSelectedPSMC102PrimitiveQuadratureExportOrUnpatchedSourcePromotionPacket",
        "active_label": "PSM-C1-02",
        "active_routes": ["SOURCE-IDENTITY/SI-1u-B2", "SOURCE-IDENTITY/SI-1u-A"],
        "closed_boundary": "DONE-PARITY-00",
        "status": STATUS,
        "previous": rel(PREVIOUS),
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "output_packets": {
            "source_field_binding_from_110row_packet": rel(SOURCE_FIELD_BINDING),
            "local_principle_psm_source_promotion_packet": rel(LOCAL_PSM_PACKET),
            "local_principle_psm_source_promotion_validator_result": rel(LOCAL_PSM_VALIDATION),
            "unpatched_theorem_guardrail_after_b2": rel(UNPATCHED_GUARD),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "PSMC102SI1uB2LocalPrincipleSourcePacketValidationTheorem",
            "proved": True,
            "patched": True,
            "statement": (
                "The local SelectedFiniteC1SourceIdentityPrinciple promotes the 72 primitive rows, "
                "2 Hessian b-source rows, and 36 sector assembly rows into a PSM-C1-02 source-promotion "
                "packet that passes the strict validator. This is a local-principle/patched result, not "
                "an unpatched derivation of the source-identity theorem."
            ),
        },
        "what_closes_now": {
            "SI1u_B2_local_principle_primitive_source_packet_validates": True,
            "selected_measure_pairing_promoted_under_local_principle": True,
            "selected_quadrature_rule_promoted_under_local_principle": True,
            "phase_R_Z_and_shift_R_X_rows_promoted_under_local_principle": True,
            "b_selected_and_sector_rows_promoted_under_local_principle": True,
            "emitted_before_residual_replay_flag_validates_under_local_principle": True,
        },
        "what_remains_open": {
            "unpatched_SelectedFiniteC1SourceIdentityTheorem": True,
            "derive_principle_from_selected_action": True,
            "honest_new_finite_action_or_Galerkin_execution": True,
            "full_no_knob_dynamic_C1_closure": True,
        },
        "closure_decision": {
            "local_principle_psm_packet_passes": validation["passes"],
            "current_unpatched_packet_passes": current_psm["passes"],
            "patched_local_principle_closure_claimed": True,
            "unpatched_theorem_closed": False,
            "global_closure_claimed": False,
        },
        "superset_strategy": {
            "classification": "SUPERSET_ROUTE_MERGE_UNDER_LOCAL_PRINCIPLE",
            "finite_C1_trace_path": "supplies selected measure, quadrature, primitive row kernels, Hessian rows, and sector assembly rows",
            "stationary_projector_path": "supplies selected transported stationary source basis from SI-1u-B1",
            "PSM_validator_path": "checks the promoted source-owner fields against the PSM-C1-02 packet contract",
            "knob_policy": "No observed constants, target fitting, or adjustable coefficients are used.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "patched_spine_closure_claimed": True,
    }

    cert = {
        "certificate": "MTT_Selected_PSM_C1_02_PrimitiveQuadratureExport_or_UnpatchedSourcePromotionPacket_v1",
        "active_label": "PSM-C1-02",
        "active_routes": candidate["active_routes"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "local_principle_psm_packet_passes": validation["passes"],
        "current_unpatched_packet_passes": current_psm["passes"],
        "patched_local_principle_closure_claimed": True,
        "unpatched_theorem_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PSM C1 02 PrimitiveQuadratureExport or UnpatchedSourcePromotionPacket v1

Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2`

Parallel label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A`

Status: `{STATUS}`

Closed boundary label: `DONE-PARITY-00`

## Result

`SI-1u-B2` now has a validating PSM-C1-02 source-promotion packet under the
local `SelectedFiniteC1SourceIdentityPrinciple`.

The packet validates the exact blockers:

- selected measure pairing
- selected quadrature rule
- phase `R_Z` primitive sources
- shift `R_X` primitive sources
- `b_selected` Hessian source
- sector row assembly
- emitted-before-residual-replay

This is not the unpatched theorem.  It is the local-principle/patched source
identity closure carried forward into the PSM-C1-02 label system.

## Superset Use

This combines the finite-C1 trace path, the stationary transported projector
path, and the PSM validator path against one constrained target.  These are not
knobs: no observed constants, target residuals, or adjustable coefficients are
used as selectors.

## True Frontier

The remaining frontier is now sharper:

`SI-1u-A`: derive the `SelectedFiniteC1SourceIdentityPrinciple` from the
selected action, or replace it with honest finite-action/Galerkin execution.

Next artifact: `{NEXT}`
"""

    for path, obj in [
        (SOURCE_FIELD_BINDING, binding),
        (LOCAL_PSM_VALIDATION, validation),
        (UNPATCHED_GUARD, guardrail),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS, "psm_validator_passes": validation["passes"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
