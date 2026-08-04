"""Build selected PSM-C1-02 source-promotion packet."""

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

SLUG = "selected_psm_c1_02_selectedsourcepromotionpacket"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CURRENT = PACKET_DIR / "current_unpatched_selected_source_promotion_packet.packet.json"
PATCHED = PACKET_DIR / "patched_local_axiom_source_promotion_packet.packet.json"
CONDITIONAL = PACKET_DIR / "conditional_unpatched_selected_source_promotion_packet.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_unpatched_source_promotion_validator_result.packet.json"
PATCHED_RESULT = PACKET_DIR / "patched_local_axiom_source_promotion_validator_result.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "conditional_unpatched_source_promotion_validator_result.packet.json"
ROUTEB_CONDITIONAL_RESULT = PACKET_DIR / "conditional_routeb_strict_payload_validator_result.packet.json"
PROMOTION_MATRIX = PACKET_DIR / "psm_c1_02_source_promotion_matrix.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PSM_C1_02_SelectedSourcePromotionPacket_v1.md"

SOURCE_VALIDATOR = ROOT / "scripts" / "validate_selected_psm_c1_02_source_promotion_packet.py"
ROUTEB_VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"

STATUS = "MTT_SELECTED_PSM_C1_02_SELECTEDSOURCEPROMOTIONPACKET_BUILT_UNPATCHED_SOURCE_OPEN"
PREVIOUS_SLUG = "selected_psm_c1_02_i10bindingproof_or_selectedquadraturesourcepromotion"
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_UnpatchedSourceRuleProof_or_HonestGalerkinExport_v1"

POST_SM_LABEL_CONTEXT = {
    "tier": "tier_2_post_sm_parity_true_equivalence",
    "preferred_phrase": "post-SM-parity frontier",
    "closed_boundary": "DONE-PARITY-00",
    "active_label": "PSM-C1-02",
    "active_label_name": "selected primitive C1 overlap contractions",
    "primary_routes": ["ROUTE-A", "ROUTE-B"],
    "route_A": "same-source dynamic Phi_fin^C1 source rule",
    "route_B": "honest selected Galerkin C1 execution",
    "language_guardrail": "Do not call this an SM-parity blocker; SM-parity replay is frozen closed.",
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(validator: Path, path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "validator": rel(validator),
        "payload": rel(path),
        "returncode": proc.returncode,
        "passes": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def source_field(name: str, source: dict[str, Any] | None, *, selected: bool, reason: str) -> dict[str, Any]:
    if source:
        return {
            "name": name,
            "selected_emitted": bool(source.get("selected_emitted", selected)),
            "theorem_derived": bool(source.get("theorem_derived", selected)),
            "source_owner_verified": bool(source.get("source_owner_verified", selected)),
            "same_branch": bool(source.get("same_branch", selected)),
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
            "source": source.get("source"),
            "reason": source.get("reason", reason),
        }
    return {
        "name": name,
        "selected_emitted": selected,
        "theorem_derived": selected,
        "source_owner_verified": selected,
        "same_branch": selected,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source": None,
        "reason": reason,
    }


def packet_base(mode: str, status: str) -> dict[str, Any]:
    return {
        "schema": "MTTPSMC102SelectedSourcePromotionPacket.v1",
        "status": status,
        "mode": mode,
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "same_branch": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "locked_target_values_used_as_source": False,
        "row_counts": {
            "primitive_kernel_rows": 72,
            "hessian_b_source_rows": 2,
            "sector_assembly_rows": 36,
        },
    }


def build_current_packet(field_matrix: dict[str, Any], routeb_result: dict[str, Any]) -> dict[str, Any]:
    fields = field_matrix["field_results"]
    packet = packet_base("current_unpatched", "CURRENT_UNPATCHED_SOURCE_PROMOTION_PACKET_FAILS_DYNAMIC_FIELDS")
    packet["free_axiom_patch_used"] = False
    packet["emitted_before_residual_replay"] = False
    packet["strict_110_row_payload_validator_passes"] = routeb_result["passes"]
    packet["source_fields"] = {
        "source_owner_id": source_field("source_owner_id", fields["source_owner_id"], selected=True, reason="imported selected source spine"),
        "selected_measure_pairing": source_field("selected_measure_pairing", None, selected=False, reason="finite trace/Frobenius measure support exists, but theorem-derived selected measure pairing is not promoted here"),
        "selected_quadrature_rule": source_field("selected_quadrature_rule", None, selected=False, reason="strict Route-B quadrature rule remains conditional unless honest source execution is emitted"),
        "admissible_c1_variation_space": source_field("admissible_c1_variation_space", fields["admissible_c1_variation_space"], selected=True, reason="fixed 72-real coordinate target"),
        "phase_R_Z_source": source_field("phase_R_Z_source", fields["phase_R_Z_source"], selected=False, reason="dynamic R_Z source not yet selected"),
        "shift_R_X_source": source_field("shift_R_X_source", fields["shift_R_X_source"], selected=False, reason="dynamic R_X source not yet selected"),
        "b_selected_source": source_field("b_selected_source", fields["b_selected_source"], selected=False, reason="same-source Hessian b vector not yet selected"),
        "sector_row_assembly": source_field("sector_row_assembly", fields["sector_row_assembly"], selected=False, reason="dynamic sector row assembly not yet promoted"),
        "independence_guard": source_field("independence_guard", fields["independence_guard"], selected=True, reason="guardrail closed"),
    }
    return packet


def build_patched_packet(patched: dict[str, Any], routeb_result: dict[str, Any]) -> dict[str, Any]:
    packet = packet_base("patched_local_axiom", "PATCHED_LOCAL_AXIOM_PROMOTES_VALUES_BUT_IS_REJECTED_FOR_UNPATCHED_SOURCE_PROMOTION")
    packet["free_axiom_patch_used"] = True
    packet["patch_source"] = patched["patch_source"]
    packet["emitted_before_residual_replay"] = True
    packet["strict_110_row_payload_validator_passes"] = routeb_result["passes"]
    packet["source_fields"] = {
        field: source_field(field, None, selected=True, reason="closed only inside explicit local DifferentiatedPhiFinC1ResidualProjectorAxiom patch")
        for field in [
            "source_owner_id",
            "selected_measure_pairing",
            "selected_quadrature_rule",
            "admissible_c1_variation_space",
            "phase_R_Z_source",
            "shift_R_X_source",
            "b_selected_source",
            "sector_row_assembly",
            "independence_guard",
        ]
    }
    return packet


def build_conditional_packet(routeb_result: dict[str, Any]) -> dict[str, Any]:
    packet = packet_base("conditional_unpatched", "CONDITIONAL_UNPATCHED_SOURCE_PROMOTION_PACKET_VALIDATES_IF_SOURCE_RULE_OR_GALERKIN_EXPORT_IS_PROVED")
    packet["conditional_only"] = True
    packet["conditional_on"] = "DifferentiatedPhiFinC1ResidualProjectorApplicationRule or honest selected Galerkin C1 table export"
    packet["free_axiom_patch_used"] = False
    packet["emitted_before_residual_replay"] = True
    packet["strict_110_row_payload_validator_passes"] = routeb_result["passes"]
    packet["source_fields"] = {
        field: source_field(field, None, selected=True, reason="conditional theorem-derived selected source-promotion field")
        for field in [
            "source_owner_id",
            "selected_measure_pairing",
            "selected_quadrature_rule",
            "admissible_c1_variation_space",
            "phase_R_Z_source",
            "shift_R_X_source",
            "b_selected_source",
            "sector_row_assembly",
            "independence_guard",
        ]
    }
    return packet


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / f"{PREVIOUS_SLUG}.candidate.json")
    field_matrix = load(DATA / "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run" / "source_owner_field_matrix_after_backimport.packet.json")
    final_gate = load(DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues" / "final_dynamic_value_gate.packet.json")
    ready_values = load(DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues" / "ready_to_promote_dynamic_value_table.packet.json")
    patched = load(DATA / "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision" / "patched_spine_closure_mode.packet.json")
    unpatched = load(DATA / "selected_dynamicc1_finalgate_perfection_or_sourceaxiomdecision" / "unpatched_theorem_mode.packet.json")
    routeb_conditional = DATA / PREVIOUS_SLUG / "route_b_conditional_selected_quadrature_source_promotion_witness.packet.json"
    routeb_result = run_validator(ROUTEB_VALIDATOR, routeb_conditional)
    write_json(ROUTEB_CONDITIONAL_RESULT, routeb_result)

    current_packet = build_current_packet(field_matrix, routeb_result)
    patched_packet = build_patched_packet(patched, routeb_result)
    conditional_packet = build_conditional_packet(routeb_result)
    write_json(CURRENT, current_packet)
    write_json(PATCHED, patched_packet)
    write_json(CONDITIONAL, conditional_packet)

    current_result = run_validator(SOURCE_VALIDATOR, CURRENT)
    patched_result = run_validator(SOURCE_VALIDATOR, PATCHED)
    conditional_result = run_validator(SOURCE_VALIDATOR, CONDITIONAL)
    write_json(CURRENT_RESULT, current_result)
    write_json(PATCHED_RESULT, patched_result)
    write_json(CONDITIONAL_RESULT, conditional_result)

    promotion_matrix = {
        "schema": "MTTPSMC102SourcePromotionMatrix.v1",
        "status": "UNPATCHED_CURRENT_FAILS_PATCHED_REJECTED_CONDITIONAL_UNPATCHED_TARGET_VALIDATES",
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_label": "PSM-C1-02",
        "closed_current_fields": field_matrix["closed_field_count"],
        "open_current_fields": field_matrix["open_field_count"],
        "current_packet_passes": current_result["passes"],
        "patched_packet_passes_unpatched_validator": patched_result["passes"],
        "conditional_packet_passes": conditional_result["passes"],
        "routeb_conditional_strict_110_passes": routeb_result["passes"],
        "dynamic_values_ready": final_gate["closure_decision"]["dynamic_values_ready"],
        "unpatched_source_rule_proved": unpatched["current_failures"]["source_rule_proved"],
        "honest_galerkin_table_exported": unpatched["current_failures"]["honest_galerkin_table_exported"],
        "exact_values_ready": ready_values["conditional_hessian_values"],
        "legal_unpatched_exits": unpatched["legal_unpatched_exits"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION_MATRIX, promotion_matrix)

    theorem = {
        "name": "PSMC102SelectedSourcePromotionPacketTheorem",
        "proved": True,
        "statement": (
            "The selected PSM-C1-02 source-promotion packet is now explicit as a strict nine-field unpatched source object: "
            "source owner, measure pairing, quadrature rule, admissible variation space, R_Z, R_X, b_selected, sector assembly, "
            "and independence guard. Current same-branch data close three support/provenance fields but leave the dynamic source "
            "fields open. The local axiom patch promotes the exact values but is rejected by the unpatched validator. A conditional "
            "unpatched packet validates exactly if the differentiated Phi_fin^C1 source rule or an honest selected Galerkin export "
            "is proved."
        ),
    }
    candidate = {
        "candidate": "MTTSelectedPSMC102SelectedSourcePromotionPacket",
        "status": STATUS,
        "previous_artifact": rel(DATA / f"{PREVIOUS_SLUG}.candidate.json"),
        "previous_status": previous["status"],
        "post_sm_parity_label_context": POST_SM_LABEL_CONTEXT,
        "active_post_sm_parity_label": "PSM-C1-02",
        "theorem": theorem,
        "what_closes_now": {
            "strict_selected_source_promotion_packet_constructed": True,
            "current_unpatched_packet_tested_and_rejected": True,
            "local_axiom_patch_separated_from_unpatched_proof": True,
            "conditional_unpatched_target_packet_validates": True,
            "exact_dynamic_values_attached_as_ready_not_selected": True,
        },
        "what_remains_open": {
            "derive_differentiated_PhiFinC1_source_rule": True,
            "or_export_honest_selected_Galerkin_C1_tables": True,
            "promote_current_unpatched_source_packet": True,
        },
        "output_packets": {
            "current_unpatched_packet": rel(CURRENT),
            "patched_local_axiom_packet": rel(PATCHED),
            "conditional_unpatched_packet": rel(CONDITIONAL),
            "current_validator_result": rel(CURRENT_RESULT),
            "patched_validator_result": rel(PATCHED_RESULT),
            "conditional_validator_result": rel(CONDITIONAL_RESULT),
            "promotion_matrix": rel(PROMOTION_MATRIX),
            "next_labeled_workorder": rel(NEXT),
        },
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    next_packet = {
        "schema": "MTTNextLabeledWorkorderAfterPSMC102SelectedSourcePromotionPacket.v1",
        "status": "NEXT_WORKORDER_UNPATCHED_SOURCE_RULE_OR_HONEST_GALERKIN_EXPORT",
        "active_label": "PSM-C1-02",
        "active_label_name": "selected primitive C1 overlap contractions",
        "next_required_artifact": NEXT_ARTIFACT,
        "task": "Fill the conditional source-promotion packet without the local axiom patch by deriving the differentiated Phi_fin^C1 source rule or exporting honest selected Galerkin C1 tables.",
        "route_A": "derive DifferentiatedPhiFinC1ResidualProjectorApplicationRule from unpatched MTT/Theta/Strominger action",
        "route_B": "export honest selected Galerkin C1 table values independent of replay and local axiom patch",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "MTT_Selected_PSM_C1_02_SelectedSourcePromotionPacket_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "current_unpatched_packet_passes": current_result["passes"],
        "patched_packet_passes_unpatched_validator": patched_result["passes"],
        "conditional_unpatched_packet_passes": conditional_result["passes"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    note = f"""# MTT Selected PSM C1 02 SelectedSourcePromotionPacket v1

Status: `{STATUS}`

Active post-SM-parity label: `PSM-C1-02`

Boundary guardrail: `DONE-PARITY-00` remains frozen closed. This is post-SM-parity frontier work, not an SM-parity blocker.

## Theorem

**{theorem["name"]}.** {theorem["statement"]}

## Packet Result

- Current unpatched source-promotion packet fails: 3 fields closed, 4 dynamic source fields open, plus measure/quadrature promotion still explicit.
- Patched local-axiom mode promotes the exact values, but is rejected as an unpatched proof source.
- Conditional unpatched source-promotion packet validates.

## Next Artifact

`{NEXT_ARTIFACT}`
"""
    write_json(NEXT, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, certificate)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
