"""Build a Qa/SU3-specific twisted-source promotion packet interface."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

HUNT = DATA / "projective_rhoe_or_de_response_source_hunt.candidate.json"
FILL = DATA / "gerbe_twisted_local_system_response_fill_attempt.candidate.json"
OUTPUT_DATA = DATA / "twisted_source_promotion_packet_interface.candidate.json"
OUTPUT_CERT = CERTS / "twisted_source_promotion_packet_interface_certificate.json"
OUTPUT_TEMPLATE = CERTS / "twisted_source_promotion_packet.template.json"
OUTPUT_NOTE = PROOF / "Selected_Qa_SU3_Twisted_Source_Promotion_Packet_Interface_v1.md"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def template() -> dict[str, object]:
    return {
        "status": "OPEN_SELECTED_QA_SU3_TWISTED_SOURCE_PROMOTION_PACKET_REQUIRED",
        "schema": "SelectedQaSU3TwistedSourcePromotionPacket.v1",
        "source_evidence": {
            "selected_by_mtt": None,
            "same_branch_Qa_SU3": None,
            "source_kind": None,
            "fixed_differential_cohomology_class": None,
            "Deligne_Cech_or_B_field_representative": None,
            "map_to_central_cocycle_verified": None,
            "period_denominator_or_smooth_unit": None,
        },
        "admissibility": {
            "Green_Schwarz_Bianchi_verified": None,
            "Freed_Witten_verified": None,
            "stability_or_HYM_verified": None,
            "twisted_projector_retains_sector": None,
            "zero_mode_policy": None,
        },
        "projective_rhoE": {
            "rank": 3,
            "projective_mesh_tables": None,
            "central_corner_cocycle": None,
            "metric_compatibility": None,
            "sector_maps": None,
            "nontrivial_central_twist": None,
        },
        "operator_response": {
            "D_E": None,
            "dotD": None,
            "Riesz_projector": None,
            "Green_operator": None,
            "heat_zeta_or_torsion_finite_part": None,
            "trace_normalization": None,
        },
        "monad_bridge": {
            "twisted_section_bases": None,
            "twisted_multiplication_constants": None,
            "g_f_zero_checked": None,
            "same_source_bridge_to_operator": None,
        },
        "guardrails": {
            "no_q79_value_import": None,
            "no_target_fitting": None,
            "validator_pass_not_source_selection": None,
        },
    }


def build() -> tuple[dict[str, object], dict[str, object], dict[str, object], str]:
    hunt = load(HUNT)
    fill = load(FILL)
    tmpl = template()
    candidate = {
        "candidate": "SelectedQaSU3TwistedSourcePromotionPacketInterface",
        "status": "QA_SU3_TWISTED_SOURCE_PROMOTION_PACKET_INTERFACE_BUILT_VALUES_OPEN",
        "input_status": {
            "projective_source_hunt": hunt["status"],
            "gerbe_response_fill_attempt": fill["status"],
        },
        "template_path": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "template": tmpl,
        "interface_checks": {
            "projective_validator_pattern_available": hunt["hunt_result"]["projective_rhoe_validator_available"],
            "twisted_promotion_contract_available": hunt["hunt_result"]["twisted_promotion_contract_available"],
            "source_family_available": fill["fill_result"]["source_family_filled"],
            "strict_selected_fields_open": True,
            "closure_claimed": False,
        },
        "promotion_rule": [
            "selected_by_mtt and same_branch_Qa_SU3 must be true before any rho_E or D_E table can promote",
            "map_to_central_cocycle_verified must bind the selected representative to the c-twist generator",
            "Bianchi, Freed-Witten, HYM/stability, projector, and zero-mode policies must pass on the same branch",
            "projective rho_E tables must pass mesh, metric, and sector checks with nontrivial central twist",
            "D_E/dotD/Riesz/Green or heat/zeta/torsion finite response must be same-source",
            "the monad bridge must preserve g*f=0 in selected twisted bases",
        ],
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "Selected_Qa_SU3_Twisted_Source_Promotion_Packet_Fill_Attempt_v1",
    }
    certificate = {
        "certificate": candidate["candidate"],
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "template_path": str(OUTPUT_TEMPLATE.relative_to(ROOT)),
        "what_closes": {
            "qa_su3_promotion_schema_built": True,
            "q79_contract_translated_without_value_import": True,
            "strict_selected_source_fields_named": True,
        },
        "what_remains_open": {
            "selected_source_evidence": True,
            "central_cocycle_map": True,
            "admissibility_flags": True,
            "projective_rhoE_or_DE_response": True,
            "monad_bridge": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    note = f"""# Selected Qa/SU3 Twisted Source Promotion Packet Interface v1

This is the local Qa/SU3 promotion contract for the projective gerbe route.

It reuses the q79 validator discipline without importing q79 values.

## Promotion Requires

```text
selected-by-MTT same-branch source evidence,
Deligne/Cech, B-field, or differential-cohomology representative,
map to the central c-twist cocycle,
Green-Schwarz/Bianchi and Freed-Witten checks,
HYM/stability, projector retention, and zero-mode policy,
projective rho_E mesh/metric/sector validation,
same-source D_E/dotD/Riesz/Green or heat/zeta/torsion response,
twisted section constants and g*f=0 bridge.
```

All selected fields are still open. This interface is a gate, not a closure.

Next required artifact:

```text
{candidate["next_required_artifact"]}
```

closure claimed: no
target fitting used: no
"""
    return candidate, certificate, tmpl, note


def main() -> None:
    candidate, certificate, tmpl, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    tmpl_text = json.dumps(tmpl, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_TEMPLATE.write_text(tmpl_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
