"""Attempt to fill the Qa/SU3 twisted-source promotion packet."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

TEMPLATE = CERTS / "twisted_source_promotion_packet.template.json"
INTERFACE = DATA / "twisted_source_promotion_packet_interface.candidate.json"
GERBE_FILL = DATA / "gerbe_twisted_local_system_response_fill_attempt.candidate.json"
PROJECTIVE_HUNT = DATA / "projective_rhoe_or_de_response_source_hunt.candidate.json"
NORMALIZATION = DATA / "complex_rotated_ctwist_normalization.candidate.json"
CTWIST_SOURCE = DATA / "ctwist_source_value_search.candidate.json"
TWIST_GATE = DATA / "twisted_section_ring_and_gerbe_source_gate.candidate.json"

OUTPUT_DATA = DATA / "twisted_source_promotion_packet_fill_attempt.candidate.json"
OUTPUT_CERT = CERTS / "twisted_source_promotion_packet_fill_attempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Twisted_Source_Promotion_Packet_Fill_Attempt_v1.md"

SOURCES = {
    "strominger_selection": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "iwasawa_flux": OBSIDIAN
    / "16 Strings, Flux, & M-Theory Encodings"
    / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "q79_time_oriented_gerbe_period": Q79 / "certificates" / "time_oriented_m1_gerbe_period_table_certificate.json",
    "q79_deck_cech_lift": Q79 / "certificates" / "time_oriented_m1_deck_cech_lift_certificate.json",
    "q79_visible_twisted_s3": Q79 / "certificates" / "visible_twisted_s3_class_restriction_closure_certificate.json",
    "q79_projective_rhoe_mesh": Q79 / "certificates" / "iwasawa_projective_rhoe_mesh_validator_certificate.json",
    "q79_promotion_gate": Q79 / "certificates" / "iwasawa_twisted_source_promotion_gate_certificate.json",
}


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {
        "path": str(path),
        "present": True,
        "terms": {key: needle.lower() in text for key, needle in terms.items()},
    }


def build() -> tuple[dict[str, object], dict[str, object], str]:
    template = load(TEMPLATE)
    interface = load(INTERFACE)
    gerbe_fill = load(GERBE_FILL)
    projective_hunt = load(PROJECTIVE_HUNT)
    normalization = load(NORMALIZATION)
    ctwist_source = load(CTWIST_SOURCE)
    twist_gate = load(TWIST_GATE)

    source_scans = {
        "strominger_selection": scan(
            SOURCES["strominger_selection"],
            {
                "fixed_topological_sector": "fixed topological sector",
                "fixed_differential_class": "fixed differential",
                "Deligne_or_gerbe": "gerbe",
                "B_field": "B",
                "Bianchi": "Bianchi",
                "bounded_projector": "bounded twisted projector",
            },
        ),
        "iwasawa_flux": scan(
            SOURCES["iwasawa_flux"],
            {
                "Iwasawa": "Iwasawa",
                "integral_periods": "integral periods",
                "global_gerbe": "gerbe is globally",
                "Bianchi_componentwise": "Bianchi identity is solved componentwise",
                "HYM": "HYM",
            },
        ),
        "q79_time_oriented_gerbe_period": scan(
            SOURCES["q79_time_oriented_gerbe_period"],
            {
                "closed_finite_table": "CLOSED",
                "smooth_Deligne_open": "full geometric Deligne",
                "selected_DE_open": "selected D_E",
                "projector_retention_open": "projector",
            },
        ),
        "q79_deck_cech_lift": scan(
            SOURCES["q79_deck_cech_lift"],
            {
                "deck_cech_lift": "Cech",
                "finite_lift_closed": "CLOSED",
                "smooth_representative_open": "smooth",
                "selected_DE_open": "D_E",
            },
        ),
        "q79_visible_twisted_s3": scan(
            SOURCES["q79_visible_twisted_s3"],
            {
                "central_cocycle": "central",
                "Freed_Witten": "Freed-Witten",
                "projector": "projector",
                "operator_source_open": "OPERATOR_SOURCE_OPEN",
            },
        ),
        "q79_projective_rhoe_mesh": scan(
            SOURCES["q79_projective_rhoe_mesh"],
            {
                "validator": "VALIDATOR",
                "projective_rhoe": "rho",
                "not_source": "source",
            },
        ),
        "q79_promotion_gate": scan(
            SOURCES["q79_promotion_gate"],
            {
                "promotion_contract": "PROMOTION",
                "selected_source_open": "OPEN",
                "D_E_open": "D_E",
                "dotD_open": "dotD",
            },
        ),
    }

    packet = copy.deepcopy(template)
    packet["status"] = "PARTIAL_QA_SU3_TWISTED_SOURCE_PROMOTION_PACKET_BLOCKED_AT_CENTRAL_MAP_AND_RESPONSE"
    packet["source_evidence"] = {
        "selected_by_mtt": "PARTIAL_SOURCE_FAMILY_SELECTED_NOT_REPRESENTATIVE",
        "same_branch_Qa_SU3": "PARTIAL: Strominger/Iwasawa source family is same branch, but no selected Qa/SU3 c-twist representative/action is printed",
        "source_kind": "Deligne_Cech_gerbe_or_B_field_fixed_differential_class_context",
        "fixed_differential_cohomology_class": True,
        "Deligne_Cech_or_B_field_representative": None,
        "map_to_central_cocycle_verified": False,
        "period_denominator_or_smooth_unit": None,
    }
    packet["admissibility"] = {
        "Green_Schwarz_Bianchi_verified": "PARTIAL_GLOBAL_STROMINGER_BIANCHI_NOT_MAPPED_TO_QA_SU3_TWISTED_MODULE",
        "Freed_Witten_verified": False,
        "stability_or_HYM_verified": "PARTIAL_STROMINGER_HYM_CONTEXT_NOT_SELECTED_MODULE_STABILITY",
        "twisted_projector_retains_sector": False,
        "zero_mode_policy": None,
    }
    packet["projective_rhoE"] = {
        "rank": 3,
        "projective_mesh_tables": None,
        "central_corner_cocycle": "GUARDRAIL_ONLY: q79/visible central cocycle patterns exist, but no Qa/SU3 selected map is verified",
        "metric_compatibility": None,
        "sector_maps": None,
        "nontrivial_central_twist": False,
    }
    packet["operator_response"] = {
        "D_E": None,
        "dotD": None,
        "Riesz_projector": None,
        "Green_operator": None,
        "heat_zeta_or_torsion_finite_part": None,
        "trace_normalization": None,
    }
    packet["monad_bridge"] = {
        "twisted_section_bases": None,
        "twisted_multiplication_constants": None,
        "g_f_zero_checked": "TYPING_ONLY: five F_i G_i twists cancel and land in P, but no selected section constants or numeric cochain product are supplied",
        "same_source_bridge_to_operator": False,
    }
    packet["guardrails"] = {
        "no_q79_value_import": True,
        "no_target_fitting": True,
        "validator_pass_not_source_selection": True,
    }

    fill_result = {
        "source_family_selected": bool(gerbe_fill["fill_result"]["source_family_filled"]),
        "fixed_differential_class_context_found": source_scans["strominger_selection"]["terms"]["fixed_differential_class"],
        "global_bianchi_context_found": source_scans["strominger_selection"]["terms"]["Bianchi"]
        or source_scans["iwasawa_flux"]["terms"]["Bianchi_componentwise"],
        "primitive_central_support_available": bool(gerbe_fill["fill_result"]["primitive_complex_central_support_filled"]),
        "twist_cancellation_table_available": bool(gerbe_fill["fill_result"]["twist_cancellation_table_filled"]),
        "projective_validator_pattern_available": bool(projective_hunt["hunt_result"]["projective_rhoe_validator_available"]),
        "selected_Qa_SU3_representative_found": False,
        "central_cocycle_map_verified": False,
        "period_denominator_or_smooth_unit_selected": False,
        "mapped_Freed_Witten_verified": False,
        "twisted_projector_retention_verified": False,
        "projective_rhoE_tables_supplied": False,
        "selected_D_E_dotD_response_supplied": False,
        "monad_bridge_numeric_gf_zero_checked": False,
        "qa_su3_packet_closed": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "SelectedQaSU3TwistedSourcePromotionPacketFillAttempt",
        "status": "QA_SU3_TWISTED_SOURCE_PROMOTION_PACKET_FILL_ATTEMPT_PARTIAL_SOURCE_CONTEXT_BLOCKED",
        "input_status": {
            "interface": interface["status"],
            "gerbe_fill": gerbe_fill["status"],
            "projective_hunt": projective_hunt["status"],
            "normalization": normalization["status"],
            "ctwist_source": ctwist_source["status"],
            "twist_gate": twist_gate["status"],
        },
        "source_scans": source_scans,
        "partial_packet": packet,
        "fill_result": fill_result,
        "what_promotes": [
            "same-branch Strominger/Iwasawa fixed differential-class context",
            "global Bianchi/HYM context as background admissibility evidence",
            "primitive complex-polarized central support from the c-twist computation",
            "typed F_i/G_i twist-cancellation table as a bridge constraint",
            "q79 projective rho_E and twisted-source promotion contracts as validators only",
        ],
        "what_does_not_promote": [
            "q79/S3 finite Deligne or Cech tables as Qa/SU3 source values",
            "global gerbe existence as the selected central cocycle map",
            "primitive slants as a selected period denominator or smooth unit",
            "typed twist cancellation as section bases or multiplication constants",
            "projective rho_E validator availability as a selected rho_E table",
            "Bianchi/HYM context as Freed-Witten or projector retention for the mapped module",
        ],
        "blocker": {
            "clean_statement": "The source context is filled, but the selected representative-to-central-cocycle map and finite/projective response payload are not.",
            "first_missing_object": "selected Qa/SU3 Deligne/Cech or B-field representative with period denominator/smooth unit",
            "second_missing_object": "verified map from that representative to the central c-twist cocycle/action",
            "third_missing_object": "same-source projective rho_E or D_E/dotD response with admissibility and projector checks",
        },
        "decision": {
            "result": "Promotion fill attempt is partial and blocked.",
            "why": "The current corpus supports the gerbe/Strominger container and typed twist bridge, but does not select the central cocycle map or response matrices required by the promotion contract.",
            "next_move": "Build a source-augmentation request specifically for the central-cocycle map and response payload, or derive those objects from the selected Hessian/retarded kernel if they exist in another encoding.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Central_Cocycle_Map_Source_Augmentation_Request_v1",
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "source_family_selected": fill_result["source_family_selected"],
            "fixed_differential_class_context_found": fill_result["fixed_differential_class_context_found"],
            "global_bianchi_context_found": fill_result["global_bianchi_context_found"],
            "primitive_central_support_available": fill_result["primitive_central_support_available"],
            "twist_cancellation_table_available": fill_result["twist_cancellation_table_available"],
            "projective_validator_pattern_available": fill_result["projective_validator_pattern_available"],
        },
        "what_remains_open": {
            "selected_Qa_SU3_representative_found": fill_result["selected_Qa_SU3_representative_found"],
            "central_cocycle_map_verified": fill_result["central_cocycle_map_verified"],
            "period_denominator_or_smooth_unit_selected": fill_result["period_denominator_or_smooth_unit_selected"],
            "mapped_Freed_Witten_verified": fill_result["mapped_Freed_Witten_verified"],
            "twisted_projector_retention_verified": fill_result["twisted_projector_retention_verified"],
            "projective_rhoE_tables_supplied": fill_result["projective_rhoE_tables_supplied"],
            "selected_D_E_dotD_response_supplied": fill_result["selected_D_E_dotD_response_supplied"],
            "monad_bridge_numeric_gf_zero_checked": fill_result["monad_bridge_numeric_gf_zero_checked"],
            "qa_su3_packet_closed": fill_result["qa_su3_packet_closed"],
        },
        "blocker": candidate["blocker"],
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    note = f"""# Selected Qa/SU3 Twisted Source Promotion Packet Fill Attempt v1

## What Filled

The fill attempt succeeds only at the source-context layer:

```text
source family selected: yes
fixed differential-class context: yes
global Bianchi/HYM context: yes
primitive central support: yes
typed twist cancellation: yes
projective rho_E validator pattern: yes
target fitting used: no
```

This is useful because it says the route is not blocked by generic gerbe
existence or by the old literal `c`-axis typing problem.

## What Did Not Fill

The promotion packet still does not close:

```text
selected Qa/SU3 Deligne/Cech or B-field representative: no
map from representative to central c-twist cocycle/action: no
period denominator or smooth unit: no
Freed-Witten check for the mapped module: no
projector retention and zero-mode policy: no
projective rho_E tables: no
selected D_E/dotD response: no
numeric g*f=0 in selected twisted bases: no
```

So the q79 projective machinery remains a validator pattern, not a value
source. The Strominger/Iwasawa source family gives the container; it does not
yet print the Qa/SU3 central-cocycle map or operator response.

## Correct Next Object

The next object should be narrower than another broad source search:

```text
{candidate["next_required_artifact"]}
```

It must provide either:

```text
selected representative -> central cocycle/action -> projective rho_E/D_E response
```

or a source-augmented theorem explaining why those are computed by the selected
Hessian and retarded overlap kernel.

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, note


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
