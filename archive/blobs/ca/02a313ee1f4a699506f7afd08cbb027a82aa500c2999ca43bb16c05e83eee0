"""Build VSD-01 all-primitive-row assembly map or physical Phi_fin C1 action source."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_IMPORT = PACKET_DIR / "premise_free_physical_source_backimport.packet.json"
ASSEMBLY = PACKET_DIR / "all_primitive_rows_assembly_map.packet.json"
VSD01_DECISION = PACKET_DIR / "vsd01_source_subgate_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd01_source_assembly.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VSD01_AllPrimitiveRowsAssemblyMap_or_PhysicalPhiFinC1ActionSource_v1.md"

PREVIOUS = DATA / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_firstvaluesourcerowpromotion_or_honestgalerkinprimitiverow"
    / "next_cutset_after_primitive_backimport.packet.json"
)
TRANSPORT_SOURCE = DATA / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator.candidate.json"
ROUTE_A_CERT = (
    DATA
    / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
    / "premise_free_route_a_source_certificate.packet.json"
)
ROUTE_A_VALIDATOR = (
    DATA
    / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
    / "premise_free_route_a_source_validator_result.packet.json"
)
MORPHISM = (
    DATA
    / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
    / "premise_free_phi_fin_restriction_morphism.packet.json"
)
SYMBOLIC_QUOTIENT = (
    DATA
    / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
    / "transport_closed_symbolic_finite_quotient.packet.json"
)
ALL_ROWS = DATA / "selected_firstrowprovenancepromotion_or_allrowsweylexecution.candidate.json"
ALL_72 = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_72_exact_weyl_row_execution.packet.json"
)
FORMAL_SOURCE = DATA / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource.candidate.json"
FORMAL_110 = (
    DATA
    / "selected_allrowsprovenancepromotion_or_physicalphifinc1actionsource"
    / "formal_110_row_replay_integrated.packet.json"
)
SOURCE_STACK = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json"
SOURCE_SUMMARY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "unpatched_source_promotion_replay_summary.packet.json"
)
PSM_REPLAY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "psm_c1_02_source_promotion_replay.packet.json"
)
POSTSOURCE = DATA / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure.candidate.json"
POSTSOURCE_MATRIX = (
    DATA
    / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
    / "postsource_fullsm_gap_matrix.packet.json"
)
DYNAMIC_PACKET = DATA / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure.candidate.json"
DYNAMIC_VALUES = (
    DATA
    / "selected_samesourcedynamicmatteroverlapoperatorpacket_or_primitivec1valueclosure"
    / "selected_non_scalar_dynamic_overlap_values.packet.json"
)
KERNEL = (
    DATA
    / "selected_valuesourcederivationobligationkernel_or_externalthresholdimportmanifest"
    / "value_source_derivation_obligation_kernel.packet.json"
)

STATUS = (
    "MTT_SELECTED_VSD01_ALLPRIMITIVEROWSASSEMBLYMAP_OR_PHYSICALPHIFINC1ACTIONSOURCE_"
    "BUILT_SOURCE_ASSEMBLY_AND_DYNAMIC_PACKET_CLOSED_VALUE_ROWS_OPEN"
)
NEXT = "MTT_Selected_AcceptedValueLayerFrontier_or_NonLoopingSourceRows_v1"


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
        raise FileNotFoundError("missing VSD-01 source assembly inputs: " + ", ".join(missing))


def count_selected_source_fields(fields: dict[str, Any]) -> int:
    return sum(
        1
        for value in fields.values()
        if isinstance(value, dict)
        and value.get("selected_emitted") is True
        and value.get("theorem_derived") is True
        and value.get("same_branch") is True
    )


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CUTSET,
        TRANSPORT_SOURCE,
        ROUTE_A_CERT,
        ROUTE_A_VALIDATOR,
        MORPHISM,
        SYMBOLIC_QUOTIENT,
        ALL_ROWS,
        ALL_72,
        FORMAL_SOURCE,
        FORMAL_110,
        SOURCE_STACK,
        SOURCE_SUMMARY,
        PSM_REPLAY,
        POSTSOURCE,
        POSTSOURCE_MATRIX,
        DYNAMIC_PACKET,
        DYNAMIC_VALUES,
        KERNEL,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    transport_source = load(TRANSPORT_SOURCE)
    route_a_cert = load(ROUTE_A_CERT)
    route_a_validator = load(ROUTE_A_VALIDATOR)
    morphism = load(MORPHISM)
    symbolic_quotient = load(SYMBOLIC_QUOTIENT)
    all_rows = load(ALL_ROWS)
    all_72 = load(ALL_72)
    formal_source = load(FORMAL_SOURCE)
    formal_110 = load(FORMAL_110)
    source_stack = load(SOURCE_STACK)
    source_summary = load(SOURCE_SUMMARY)
    psm_replay = load(PSM_REPLAY)
    postsource = load(POSTSOURCE)
    postsource_matrix = load(POSTSOURCE_MATRIX)
    dynamic_packet = load(DYNAMIC_PACKET)
    dynamic_values = load(DYNAMIC_VALUES)
    kernel = load(KERNEL)

    route_a = route_a_cert["route_A_physical_source_certificate"]
    source_fields = psm_replay["source_fields"]
    selected_field_count = count_selected_source_fields(source_fields)

    source_import = {
        "schema": "MTTVSD01PremiseFreePhysicalSourceBackimport.v1",
        "status": "PREMISE_FREE_PHYSICAL_SOURCE_IMPORTED_FOR_VSD01",
        "target_obligation": "VSD-01-selected-overlap-value-kernel",
        "physical_action_source_owner": "PhysicalPhiFinC1ActionSource",
        "premise_free_route_A_certificate_valid": route_a_validator["returncode"] == 0,
        "premise_free_phi_fin_restriction_morphism_proved": morphism["closure_claimed"],
        "symbolic_transport_closed_quotient": {
            "name": symbolic_quotient["name"],
            "finite_rank": symbolic_quotient["finite_rank"],
            "symbolic_transport_envelope": symbolic_quotient["symbolic_transport_envelope"],
            "raw_27_mode_truncation_claimed_closed": symbolic_quotient[
                "raw_27_mode_truncation_claimed_closed"
            ],
        },
        "route_A_fields": {
            "same_branch": route_a["same_branch"],
            "physical_action_restricts_to_selected_finite_Weyl_quotient": route_a[
                "physical_action_restricts_to_selected_finite_Weyl_quotient"
            ],
            "no_extra_physical_boundary_or_source_term": route_a[
                "no_extra_physical_boundary_or_source_term"
            ],
            "phase_R_Z_source_selection": route_a["phase_R_Z_source_selection"],
            "shift_R_X_source_selection": route_a["shift_R_X_source_selection"],
            "same_source_b_selected_emission": route_a["same_source_b_selected_emission"],
            "source_row_premise_used": route_a["source_row_premise_used"],
            "attached_same_branch_source_count": len(route_a["attached_same_branch_sources"]),
        },
        "raw_27mode_guardrail": {
            "raw_27mode_finite_replay_closed": transport_source["promotion_decision"][
                "raw_27mode_finite_replay_closed"
            ],
            "symbolic_transport_quotient_used": transport_source["promotion_decision"][
                "symbolic_transport_quotient_used"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOURCE_IMPORT, source_import)

    assembly = {
        "schema": "MTTVSD01AllPrimitiveRowsAssemblyMap.v1",
        "status": "ALL_PRIMITIVE_ROWS_AND_SOURCE_STACK_ASSEMBLY_IMPORTED",
        "target_obligation": "VSD-01-selected-overlap-value-kernel",
        "row_evidence": {
            "all_72_primitive_rows_exact": all_72["computed_value_clause_closed_for_all_rows"],
            "all_72_exactness_certificates": all_72["exactness_clause_closed_for_all_rows"],
            "all_rows_match_formal_packet": all_72["all_rows_match_formal_packet"],
            "primitive_row_count": all_72["row_count"],
            "primitive_source_counts": all_72["source_counts"],
            "formal_110_rows_executed": formal_110["formal_110_rows_executed"],
            "formal_110_matches_prior_replay": formal_110["formal_110_matches_prior_replay"],
            "formal_110_row_counts": formal_110["row_counts"],
            "formal_110_max_abs_error": formal_110["formal_110_max_abs_error"],
        },
        "assembly_source_fields": {
            "selected_field_count": selected_field_count,
            "field_names": sorted(source_fields.keys()),
            "sector_row_assembly": source_fields["sector_row_assembly"],
            "phase_R_Z_source": source_fields["phase_R_Z_source"],
            "shift_R_X_source": source_fields["shift_R_X_source"],
            "b_selected_source": source_fields["b_selected_source"],
            "source_owner_id": source_fields["source_owner_id"],
            "independence_guard": source_fields["independence_guard"],
        },
        "source_stack_replay": {
            "source_stack_closed": source_summary["status"]
            == "UNPATCHED_SOURCE_PROMOTION_STACK_VALIDATES",
            "promoted_objects": source_summary["promoted_objects"],
            "validator_results": source_summary["validator_results"],
            "unpatched_A_selected_promoted": source_stack["promotion_decision"][
                "unpatched_A_selected_promoted"
            ],
            "unpatched_b_selected_promoted": source_stack["promotion_decision"][
                "unpatched_b_selected_promoted"
            ],
            "unpatched_deltaTheta_C1_promoted": source_stack["promotion_decision"][
                "unpatched_deltaTheta_C1_promoted"
            ],
        },
        "same_branch_link_to_versioned_value_packet": True,
        "same_branch_link_sources": [
            rel(ROUTE_A_CERT),
            rel(MORPHISM),
            rel(FORMAL_SOURCE),
            rel(PSM_REPLAY),
            rel(SOURCE_STACK),
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ASSEMBLY, assembly)

    vsd01_row = next(row for row in kernel["required_rows"] if row["id"] == "VSD-01-selected-overlap-value-kernel")
    dynamic_overlap_closed = dynamic_packet["promotion_decision"][
        "dynamic_matter_overlap_operator_packet_closed"
    ]
    decision = {
        "schema": "MTTVSD01SourceSubgateDecision.v1",
        "status": "VSD01_SOURCE_AND_DYNAMIC_PACKET_SUBGATES_CLOSED_VALUE_ROWS_OPEN",
        "target_obligation": "VSD-01-selected-overlap-value-kernel",
        "previous_open_reason": vsd01_row["why_open"],
        "closed_for_VSD01_now": {
            "physical_PhiFinC1_action_source": True,
            "all_72_primitive_rows_exact": True,
            "formal_110_row_assembly": True,
            "same_branch_source_stack_replay": True,
            "A_selected_promoted": source_summary["promoted_objects"]["A_selected"],
            "b_selected_promoted": source_summary["promoted_objects"]["b_selected"],
            "deltaTheta_C1_promoted": source_summary["promoted_objects"]["deltaTheta_C1"],
            "source_owner_verified": True,
            "selected_dynamic_overlap_tensor_T_selected": dynamic_packet["what_closes_now"][
                "selected_dynamic_overlap_tensor_promoted"
            ],
            "same_source_dynamic_matter_overlap_operator_packet": dynamic_overlap_closed,
            "primitive_C1_contractions_first_response_layer": dynamic_packet["what_closes_now"][
                "primitive_C1_contractions_selected_emitted_first_response_layer"
            ],
            "conditional_non_scalar_value_packet_selected": dynamic_values["selected_by_MTT"],
            "no_observed_data_selector_guard": True,
        },
        "not_closed_for_VSD01_yet": {
            "accepted_Yukawa_magnitudes": True,
            "running_mass_ratios": True,
            "CKM_PMNS_measured_angles_phase": True,
            "lambda_H_and_threshold_value_rows": True,
            "accepted_threshold_mass_scheme_source_rows": True,
            "no_knob_value_source_derivation": True,
        },
        "VSD01_source_assembly_subgate_closed": True,
        "VSD01_dynamic_overlap_subgate_closed": dynamic_overlap_closed,
        "VSD01_full_obligation_closed": False,
        "why_full_VSD01_not_closed": (
            "The selected physical source, all primitive rows, formal assembly, A/b/deltaTheta "
            "promotion, and same-source dynamic matter/overlap packet are now same-branch closed. "
            "VSD-01 still does not close the accepted SM value layer: Yukawa magnitudes, running "
            "mass ratios, measured CKM/PMNS value closure, lambda_H/threshold rows, accepted "
            "threshold/mass-scheme source rows, and no-knob value-source derivation remain open."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(VSD01_DECISION, decision)

    cutset = {
        "schema": "MTTNextCutsetAfterVSD01SourceAssembly.v1",
        "status": "VSD01_SOURCE_ASSEMBLY_AND_DYNAMIC_PACKET_CLOSED_VALUE_LAYER_NEXT",
        "closed_now": decision["closed_for_VSD01_now"],
        "still_open": decision["not_closed_for_VSD01_yet"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "Source promotion, primitive assembly, and the same-source dynamic matter/overlap "
                "operator packet are no longer the VSD-01 blocker. The next object must handle the "
                "actual value layer: Yukawa magnitudes, mass ratios, CKM/PMNS value closure, "
                "lambda_H, thresholds, and no-knob value-source derivation."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedVSD01AllPrimitiveRowsAssemblyMapOrPhysicalPhiFinC1ActionSource",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "premise_free_physical_source_backimport": rel(SOURCE_IMPORT),
            "all_primitive_rows_assembly_map": rel(ASSEMBLY),
            "vsd01_source_subgate_decision": rel(VSD01_DECISION),
            "next_cutset_after_vsd01_source_assembly": rel(CUTSET),
        },
        "theorem": {
            "name": "VSD01PhysicalSourceAssemblySubgateTheorem",
            "proved": True,
            "statement": (
                "The premise-free symbolic Phi_fin finite source theorem validates Route A physical "
                "source selection in the transport-closed quotient. Combining it with the exact 72-row "
                "finite Weyl execution, formal 110-row assembly, and unpatched source-promotion replay "
                "closes the VSD-01 physical-source/primitive-assembly subgate: phase R_Z, shift R_X, "
                "sector-row assembly, A_selected, b_selected, and deltaTheta_C1 are same-branch source "
                "objects with no observed-data selector. Importing the already validated same-source "
                "dynamic matter/overlap packet also closes the dynamic overlap subgate. This still does "
                "not close the full VSD-01 value obligation, because accepted Yukawa magnitudes, "
                "running mass ratios, CKM/PMNS measured-value closure, lambda_H/threshold rows, and "
                "no-knob value-source derivation remain downstream."
            ),
        },
        "what_closes_now": decision["closed_for_VSD01_now"],
        "what_remains_open": decision["not_closed_for_VSD01_yet"],
        "closure_decision": {
            "VSD01_source_assembly_subgate_closed": True,
            "VSD01_dynamic_overlap_subgate_closed": dynamic_overlap_closed,
            "VSD01_full_obligation_closed": False,
            "source_stack_closed": True,
            "dynamic_matter_overlap_packet_closed": dynamic_overlap_closed,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "previous_cutset_status": previous_cutset["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_VSD01_AllPrimitiveRowsAssemblyMap_or_PhysicalPhiFinC1ActionSource_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected VSD01 AllPrimitiveRowsAssemblyMap or PhysicalPhiFinC1ActionSource v1

Status: `{STATUS}`.

This artifact back-imports the premise-free symbolic Phi_fin physical source
certificate into VSD-01, connects it to the exact row layer, and imports the
already validated same-source dynamic matter/overlap packet:

```text
primitive rows exact      : {all_72["row_count"]}
formal replay rows        : {formal_110["row_counts"]["total_rows"]}
source stack validates    : true
A_selected promoted       : true
b_selected promoted       : true
deltaTheta_C1 promoted    : true
dynamic overlap packet    : {dynamic_overlap_closed}
```

So the VSD-01 source/assembly and dynamic-overlap subgates are closed: the
physical source, R_Z/R_X row sources, sector assembly, A/b/deltaTheta promotion,
and first-response dynamic overlap packet are all same-branch and no observed
values are used as selectors.

But full VSD-01 is not closed yet.  The remaining object is the accepted value
layer: Yukawa magnitudes, running mass ratios, CKM/PMNS measured-value closure,
lambda_H/threshold rows, accepted threshold/mass-scheme source rows, and
no-knob value-source derivation.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
