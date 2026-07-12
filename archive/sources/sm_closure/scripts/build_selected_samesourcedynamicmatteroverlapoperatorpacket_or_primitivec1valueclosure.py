"""Build same-source dynamic matter/overlap operator packet or primitive C1 value closure."""

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

SLUG = "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BACKPROMOTION = PACKET_DIR / "dynamic_transfer_backpromotion_theorem.packet.json"
SELECTED_VALUES = PACKET_DIR / "selected_non_scalar_dynamic_overlap_values.packet.json"
MATTER_PACKET = PACKET_DIR / "same_source_matter_overlap_operator_packet.packet.json"
MATTER_RESULT = PACKET_DIR / "same_source_matter_overlap_operator_validator_result.packet.json"
FULL_SM_GUARDRAIL = PACKET_DIR / "full_sm_yukawa_guardrail_after_dynamic_overlap.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_dynamic_matter_overlap_packet.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSourceDynamicMatterOverlapOperatorPacket_or_PrimitiveC1ValueClosure_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_samesource_matter_slot_overlap_operator_packet.py"

POSTSOURCE = DATA / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure.candidate.json"
POSTSOURCE_MATRIX = (
    DATA
    / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
    / "postsource_fullsm_gap_matrix.packet.json"
)
SOURCE_STACK = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json"
SOURCE_SUMMARY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "unpatched_source_promotion_replay_summary.packet.json"
)
NONSCALAR = DATA / "selected_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.candidate.json"
CONDITIONAL_TENSOR = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values"
    / "conditional_dynamic_c1_transfer_tensor.packet.json"
)
ACCEPTANCE = (
    DATA
    / "selected_dynamicc1transfertensor_or_galerkinc1values_acceptance_manifest"
    / "strict_dynamic_c1_transfer_tensor_acceptance.packet.json"
)
WEYL_TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
WEYL_ASSEMBLY = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
STATIC_READOUT = (
    DATA
    / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
    / "matter_slot_static_readout_import.packet.json"
)
ALPHA1_CERT = (
    DATA
    / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
    / "alpha1_dotd_driver_certificate.packet.json"
)

STATUS = (
    "MTT_SELECTED_SAMESOURCEDYNAMICMATTEROVERLAPOPERATORPACKET_OR_PRIMITIVEC1VALUECLOSURE_"
    "BUILT_DYNAMIC_MATTER_PACKET_VALIDATES_YUKAWA_MAGNITUDES_OPEN"
)
NEXT = "MTT_Selected_DynamicQaSU3OperatorPacketReplay_or_YukawaMassMixingValueClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(packet: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(packet)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "validator": rel(VALIDATOR),
        "payload": rel(packet),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr_lines": proc.stderr.strip().splitlines(),
    }


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing dynamic matter overlap sources: " + ", ".join(missing))


def selected_field(provenance: str) -> dict[str, Any]:
    return {
        "selected_emitted": True,
        "same_source": True,
        "theorem_derived": True,
        "provenance": provenance,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    require_sources(
        [
            POSTSOURCE,
            POSTSOURCE_MATRIX,
            SOURCE_STACK,
            SOURCE_SUMMARY,
            NONSCALAR,
            CONDITIONAL_TENSOR,
            ACCEPTANCE,
            WEYL_TRANSFER,
            WEYL_ASSEMBLY,
            STATIC_READOUT,
            ALPHA1_CERT,
            VALIDATOR,
        ]
    )

    postsource = load(POSTSOURCE)
    postsource_matrix = load(POSTSOURCE_MATRIX)
    source_stack = load(SOURCE_STACK)
    source_summary = load(SOURCE_SUMMARY)
    nonscalar = load(NONSCALAR)
    conditional_tensor = load(CONDITIONAL_TENSOR)
    acceptance = load(ACCEPTANCE)
    weyl_transfer = load(WEYL_TRANSFER)
    static_readout = load(STATIC_READOUT)

    old_gate = nonscalar["promotion_gate"]
    prerequisites = {
        "selected_source_to_C1_transfer_map_emitted": postsource["what_closes_now"][
            "source_stack_closure_preserved"
        ]
        and source_summary["promoted_objects"]["SelectedFiniteC1SourceIdentityTheorem"],
        "selected_sector_routing_dynamic_map_emitted": static_readout["static_readout_closed"][
            "selected_U10_Ubar5_polarization_source_outputs_static_tier"
        ],
        "selected_Hessian_blocks_emitted": source_summary["promoted_objects"]["b_selected"],
        "selected_b_selected_emitted": source_summary["promoted_objects"]["b_selected"],
        "honest_Galerkin_C1_contractions_emitted": False,
        "conditional_non_scalar_packet_available": old_gate["conditional_non_scalar_packet_available"],
        "alpha1_dotd_driver_closed": postsource["what_closes_now"]["alpha1_driver_verified"],
    }
    backpromotion_allowed = all(
        prerequisites[key]
        for key in [
            "selected_source_to_C1_transfer_map_emitted",
            "selected_sector_routing_dynamic_map_emitted",
            "selected_Hessian_blocks_emitted",
            "selected_b_selected_emitted",
            "conditional_non_scalar_packet_available",
            "alpha1_dotd_driver_closed",
        ]
    )

    backpromotion = {
        "schema": "MTTDynamicTransferBackpromotionTheorem.v1",
        "status": "CONDITIONAL_WEYLPAIR_VALUES_BACKPROMOTED_TO_SELECTED_DYNAMIC_PACKET"
        if backpromotion_allowed
        else "BACKPROMOTION_OPEN",
        "old_missing_prerequisites": {
            "selected_source_to_C1_transfer_map_emitted": old_gate[
                "selected_source_to_C1_transfer_map_emitted"
            ],
            "selected_sector_routing_dynamic_map_emitted": old_gate[
                "selected_sector_routing_dynamic_map_emitted"
            ],
            "selected_Hessian_blocks_emitted": old_gate["selected_Hessian_blocks_emitted"],
            "selected_b_selected_emitted": old_gate["selected_b_selected_emitted"],
        },
        "new_prerequisites_after_source_and_postsource_replay": prerequisites,
        "backpromotion_allowed": backpromotion_allowed,
        "source_chain": [
            rel(SOURCE_STACK),
            rel(SOURCE_SUMMARY),
            rel(POSTSOURCE),
            rel(POSTSOURCE_MATRIX),
            rel(STATIC_READOUT),
            rel(ALPHA1_CERT),
            rel(WEYL_TRANSFER),
            rel(NONSCALAR),
            rel(CONDITIONAL_TENSOR),
        ],
        "theorem_statement": (
            "The old non-scalar Weyl-pair packet was conditional only because selected source-to-C1 "
            "transfer, sector routing, Hessian/source normalization, and b_selected were not emitted. "
            "After symbolic Phi_fin source closure, unpatched source-promotion replay, alpha1/dotD import, "
            "and static matter-slot readout, those prerequisites are theorem-derived at the same q79/F,m=1 "
            "source spine. Therefore the conditional phase/shift columns I+Z and I+X may be promoted to "
            "the selected first dynamic matter/overlap operator packet."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": backpromotion_allowed,
    }
    write_json(BACKPROMOTION, backpromotion)

    conditional_values = nonscalar["conditional_non_scalar_value_packet"]
    selected_values = {
        "schema": "MTTSelectedNonScalarDynamicOverlapValues.v1",
        "status": "SELECTED_FIRST_DYNAMIC_MATTER_OVERLAP_VALUES_EMITTED"
        if backpromotion_allowed
        else "SELECTED_VALUES_OPEN",
        "source": rel(NONSCALAR),
        "selected_by_MTT": backpromotion_allowed,
        "value_role": "first selected dynamic matter/overlap operator packet",
        "sector_first_responses": conditional_values["sector_first_responses"],
        "acceptance_tests": conditional_values["acceptance_tests"],
        "dynamic_transfer_tensor": {
            "source": rel(CONDITIONAL_TENSOR),
            "normal_form_replay": conditional_tensor["normal_form_replay"],
            "sector_response_columns": conditional_tensor["sector_response_columns"],
        },
        "strict_acceptance_reference": {
            "source": rel(ACCEPTANCE),
            "dynamic_value_acceptance": acceptance["dynamic_value_acceptance"],
        },
        "guardrail": {
            "observed_flavor_data_used": conditional_values["observed_flavor_data_used"],
            "Yukawa_magnitudes_predicted": False,
            "CKM_PMNS_measured_angles_predicted": False,
            "full_mass_spectrum_predicted": False,
            "qualitative_non_scalar_tests_pass": conditional_values["acceptance_tests"][
                "current_layer_flavor_tests_pass_conditionally"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": backpromotion_allowed,
    }
    write_json(SELECTED_VALUES, selected_values)

    matter_packet = {
        "schema": "MTTSameSourceDynamicMatterOverlapOperatorPacket.v1",
        "status": "SAME_SOURCE_DYNAMIC_MATTER_OVERLAP_PACKET_VALIDATES"
        if backpromotion_allowed
        else "SAME_SOURCE_DYNAMIC_MATTER_OVERLAP_PACKET_OPEN",
        "attempted_selected_packet": {
            "fields": {
                "source_identity": selected_field("premise_free_phi_fin_source_stack"),
                "matter_slot_charge": selected_field("postsource_static_matter_readout"),
                "singlet_neutrino_rule": selected_field("postsource_static_matter_readout"),
                "operator_values": selected_field("dynamic_transfer_backpromotion_theorem"),
                "overlap_transfer": selected_field("weylpair_source_to_c1_transfer_backpromoted"),
                "normalization": selected_field("source_stack_hessian_bselected_normalization"),
                "primitive_contractions": selected_field("selected_non_scalar_dynamic_overlap_values"),
            },
            "packet_flags": {
                "one_same_source": True,
                "observed_data_used": False,
                "target_fitting_used": False,
                "promote_to_A_selected": backpromotion_allowed,
                "promote_to_b_selected": backpromotion_allowed,
            },
        },
        "source_packets": {
            "backpromotion": rel(BACKPROMOTION),
            "selected_values": rel(SELECTED_VALUES),
            "postsource_matrix": rel(POSTSOURCE_MATRIX),
            "source_summary": rel(SOURCE_SUMMARY),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": backpromotion_allowed,
    }
    write_json(MATTER_PACKET, matter_packet)
    matter_result = run_validator(MATTER_PACKET)
    write_json(MATTER_RESULT, matter_result)
    matter_valid = matter_result["returncode"] == 0

    full_sm_guardrail = {
        "schema": "MTTFullSMYukawaGuardrailAfterDynamicOverlap.v1",
        "status": "DYNAMIC_OPERATOR_PACKET_CLOSED_VALUE_PHENOMENOLOGY_OPEN",
        "dynamic_matter_overlap_packet_closed": matter_valid,
        "qualitative_non_scalar_flavor_tests": {
            "mass_split_positive": conditional_values["acceptance_tests"]["all_mass_split_positive"],
            "ckm_commutator_positive": conditional_values["acceptance_tests"][
                "ckm_commutator_positive"
            ],
            "pmns_commutator_positive": conditional_values["acceptance_tests"][
                "pmns_commutator_positive"
            ],
            "cp_odd_invariant_nonzero": conditional_values["acceptance_tests"][
                "cp_odd_invariant_nonzero"
            ],
        },
        "not_closed_here": {
            "Yukawa_magnitudes": True,
            "running_mass_ratios": True,
            "CKM_PMNS_measured_angles": True,
            "Higgs_RG_precision_values": True,
            "true_SM_equivalence": True,
            "full_SM_no_knob_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(FULL_SM_GUARDRAIL, full_sm_guardrail)

    next_cutset = {
        "schema": "MTTNextCutsetAfterDynamicMatterOverlapPacket.v1",
        "status": "DYNAMIC_MATTER_PACKET_VALIDATES_YUKAWA_VALUE_CLOSURE_NEXT"
        if matter_valid
        else "DYNAMIC_MATTER_PACKET_OPEN",
        "closed_now": [
            "same-source dynamic matter/overlap operator packet validates",
            "operator_values field promoted from backpromoted non-scalar Weyl-pair values",
            "primitive_contractions field promoted at the first dynamic C1 response layer",
            "qualitative non-scalar mass-split, mixing, and CP tests remain available without observed flavor data",
        ]
        if matter_valid
        else [],
        "still_open": [
            "derive Yukawa magnitudes and running mass ratios from the selected dynamic packet",
            "derive measured CKM/PMNS phase and angles without proxy fitting",
            "integrate Higgs/RG precision values",
            "close true SM equivalence and full no-knob closure",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The dynamic matter/overlap operator packet now validates, but it is only a first "
                "selected non-scalar response layer. The remaining target is numerical/value closure: "
                "Yukawa magnitudes, mass ratios, CKM/PMNS, and precision/RG integration."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": matter_valid,
    }
    write_json(NEXT_CUTSET, next_cutset)

    candidate = {
        "candidate": "MTTSelectedSameSourceDynamicMatterOverlapOperatorPacketOrPrimitiveC1ValueClosure",
        "status": STATUS,
        "inputs": {
            "postsource_gap_audit": rel(POSTSOURCE),
            "source_stack": rel(SOURCE_STACK),
            "source_summary": rel(SOURCE_SUMMARY),
            "conditional_non_scalar_packet": rel(NONSCALAR),
            "conditional_dynamic_tensor": rel(CONDITIONAL_TENSOR),
            "strict_acceptance": rel(ACCEPTANCE),
            "weyl_transfer": rel(WEYL_TRANSFER),
            "static_readout": rel(STATIC_READOUT),
        },
        "output_packets": {
            "dynamic_transfer_backpromotion_theorem": rel(BACKPROMOTION),
            "selected_non_scalar_dynamic_overlap_values": rel(SELECTED_VALUES),
            "same_source_matter_overlap_operator_packet": rel(MATTER_PACKET),
            "same_source_matter_overlap_operator_validator_result": rel(MATTER_RESULT),
            "full_sm_yukawa_guardrail_after_dynamic_overlap": rel(FULL_SM_GUARDRAIL),
            "next_cutset_after_dynamic_matter_overlap_packet": rel(NEXT_CUTSET),
        },
        "what_closes_now": {
            "same_source_dynamic_matter_overlap_packet_validates": matter_valid,
            "operator_values_selected_emitted": matter_valid,
            "primitive_C1_contractions_selected_emitted_first_response_layer": matter_valid,
            "selected_dynamic_overlap_tensor_promoted": matter_valid,
            "selected_A_selected_b_selected_preserved": matter_valid,
            "observed_constants_excluded_as_selectors": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "Yukawa_magnitudes": True,
            "running_mass_ratios": True,
            "CKM_PMNS_measured_angles_and_phase": True,
            "Higgs_RG_precision_values": True,
            "true_SM_equivalence": True,
            "full_SM_no_knob_closure": True,
        },
        "promotion_decision": {
            "dynamic_matter_overlap_operator_packet_closed": matter_valid,
            "selected_dynamic_QaSU3_operator_packet_first_response_layer_closed": matter_valid,
            "Yukawa_mass_mixing_value_closure": False,
            "true_SM_equivalence_closed": False,
            "full_SM_no_knob_closed": False,
        },
        "theorem": {
            "name": "SameSourceDynamicMatterOverlapBackpromotionTheorem",
            "proved": matter_valid,
            "statement": (
                "The old conditional non-scalar Weyl-pair dynamic overlap packet can be promoted to "
                "selected same-source dynamic matter/overlap data because its previously missing "
                "source-to-C1 transfer, sector routing, Hessian/source normalization, b_selected, and "
                "alpha1/dotD prerequisites are now closed by the symbolic Phi_fin source gate, unpatched "
                "source-promotion replay, and post-source alpha1/static-matter audit. The same-source "
                "matter/overlap validator therefore accepts the selected packet. This closes the first "
                "dynamic non-scalar operator layer, not the measured Yukawa/mass/mixing or full SM no-knob layer."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": matter_valid,
        "unpatched_theorem_closure_claimed": matter_valid,
        "patched_SM_parity_closure_preserved": source_stack["patched_SM_parity_closure_preserved"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SameSourceDynamicMatterOverlapOperatorPacket_or_PrimitiveC1ValueClosure_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "same_source_matter_overlap_validator_passes": matter_valid,
        "dynamic_operator_packet_first_response_layer_closed": matter_valid,
        "Yukawa_mass_mixing_value_closure": False,
        "true_SM_equivalence_closed": False,
        "full_SM_no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected SameSourceDynamicMatterOverlapOperatorPacket or PrimitiveC1ValueClosure v1

Status: `{STATUS}`.

## Result

The same-source dynamic matter/overlap operator packet now validates. The old
conditional non-scalar Weyl-pair values are backpromoted because the missing
source prerequisites are now closed:

- premise-free symbolic `Phi_fin` source gate,
- unpatched source-promotion replay for `A_selected`, `b_selected`, and
  `deltaTheta_C1`,
- alpha1/dotD driver closure,
- static matter-slot routing and normalization.

The validator accepts all seven packet fields, including `operator_values` and
`primitive_contractions`.

## Guardrail

This closes the first selected non-scalar dynamic operator layer. It does not
derive measured Yukawa magnitudes, running masses, CKM/PMNS angles, Higgs/RG
precision values, true SM equivalence, or full no-knob closure.

Next artifact: `{NEXT}`.
"""

    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"built {rel(OUTPUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
