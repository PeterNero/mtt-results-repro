"""Build oriented Phi_fin End(E)-basis / nonidentity-rhoE value insertion gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "oriented_fill": DATA / "selected_heterotic_orientedphifin_sourcetheorem_fillattempt_or_directsmootheqapayload.candidate.json",
    "oriented_packet": DATA / "selected_heterotic_orientedphifin_sourcetheorem_fillattempt_packet.json",
    "typedcech_or_rhoe_attempt": DATA / "selected_heterotic_typedcechende_basis_or_projectiverhoe_fill_attempt.candidate.json",
    "typedtables_or_rhoe_sourcefill": DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_sourcefill.candidate.json",
    "missing_leaves": DATA / "selected_heterotic_typedmaptables_or_projectiverhoetables_missing_leaves.json",
    "domain_or_rhoe_gate": DATA / "selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion.candidate.json"
OUTPUT_INSERTION = DATA / "selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_ende_basis_or_nonidentityrhoe_valueinsertion_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_EndE_Basis_or_NonidentityRhoE_ValueInsertion_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_ENDE_OR_RHOE_VALUEINSERTION_CURRENT_SOURCE_NOGO_REPAIR_SPLIT"
NEXT = "Selected_Heterotic_OrientedPhiFin_DirectFiniteResponse_or_ProjectiveRhoE_SourceAmendment_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    oriented_fill = load(INPUTS["oriented_fill"])
    oriented_packet = load(INPUTS["oriented_packet"])
    typed_attempt = load(INPUTS["typedcech_or_rhoe_attempt"])
    sourcefill = load(INPUTS["typedtables_or_rhoe_sourcefill"])
    missing = load(INPUTS["missing_leaves"])
    domain_or_rhoe = load(INPUTS["domain_or_rhoe_gate"])

    lane_a = {
        "id": "A_selected_typed_EndE_basis",
        "attempted": True,
        "value_inserted": False,
        "support_strength": {
            "typed_sourcefill_filled_leaf_count": sourcefill["lane_a_typed"]["filled_leaf_count"],
            "typed_sourcefill_required_leaf_count": sourcefill["lane_a_typed"]["required_leaf_count"],
            "monad_topology_source_printed": typed_attempt["lane_a_typed_cech"]["support"]["topological_monad_data"] == "PASS_SOURCE_PRINTED",
            "charge_compatibility": sourcefill["lane_a_typed"]["support_imported"]["charge_compatibility"],
        },
        "blocking_fields": [
            item["path"] for item in missing["typed_missing"] if item["filled"] is False
        ],
        "first_blockers": [
            "typed f,g map coefficient tables",
            "Cech/Dolbeault matrices or End(E) cochain basis",
            "g*f=0 machine-checkable matrix product",
            "trace inner product and zero-mode/shared-line quotient policy",
        ],
        "verdict": "STRUCTURAL_SUPPORT_ONLY_NO_SELECTED_ENDE_BASIS",
    }

    lane_b = {
        "id": "B_selected_nonidentity_projective_rhoE",
        "attempted": True,
        "value_inserted": False,
        "support_strength": {
            "projective_sourcefill_filled_leaf_count": sourcefill["lane_b_projective"]["filled_leaf_count"],
            "projective_sourcefill_required_leaf_count": sourcefill["lane_b_projective"]["required_leaf_count"],
            "twist_cancellation_context": sourcefill["lane_b_projective"]["support_imported"]["twist_cancellation_table_available"],
            "projective_validator_pattern_available": sourcefill["lane_b_projective"]["support_imported"]["projective_validator_pattern_available"],
        },
        "blocking_fields": [
            item["path"] for item in missing["projective_missing"] if item["filled"] is False
        ],
        "first_blockers": [
            "selected Deligne/Cech or B-field representative",
            "representative-to-central-cocycle map",
            "rho_E generator or boundary matrices",
            "projective cocycle law, nonidentity check, and finite response exit",
        ],
        "verdict": "GERBE_SUPPORT_ONLY_NO_SELECTED_PROJECTIVE_RHOE_TABLES",
    }

    lane_c = {
        "id": "C_direct_same_source_finite_response",
        "attempted": False,
        "value_inserted": False,
        "why_introduced": (
            "Both table lanes are blocked at source-value emission. A direct finite response "
            "could legally bypass typed tables and projective rhoE tables if it emits D_E/dotD, "
            "Riesz/Green, heat/zeta/torsion finitepart, trace normalization, source certificate, "
            "and map to the oriented B_N quotient from the same source."
        ),
        "required_payload": {
            "same_branch_source_certificate": False,
            "selected_domain_or_quotient_map_to_oriented_BN": False,
            "D_E_or_EQa_matrix": False,
            "Riesz_or_Green_operator": False,
            "positive_spectrum_or_heat_zeta_torsion": False,
            "finitepart_trace_identity": False,
            "no_double_count_replay": oriented_packet["leaf_status_after_attempt"]["kernel_policy_closed"]["closed"],
        },
        "verdict": "PROMOTED_AS_NEXT_REPAIR_LANE_NOT_YET_ATTEMPTED",
    }

    insertion_packet = {
        "schema": "SelectedHeterotic.OrientedPhiFin.EndEOrRhoE.ValueInsertionPacket.v1",
        "lane_A_typed_EndE_basis": lane_a,
        "lane_B_nonidentity_projective_rhoE": lane_b,
        "lane_C_direct_same_source_finite_response": lane_c,
        "legal_minimal_repairs": missing["legal_minimal_repairs"],
        "selected_next_repair": "C_direct_same_source_finite_response_or_B_projective_rhoE_source_amendment",
        "reason": (
            "Lane A has many structural typed-table leaves but still lacks the basic typed f,g "
            "value tables. Lane B is closer to the existing oriented/gerbe support, but lacks "
            "the representative and rhoE tables. Lane C is kept as a bypass because it can "
            "close the oriented source theorem without first solving the whole section ring."
        ),
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_INSERTION.write_text(json.dumps(insertion_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "value_insertion_attempted": True,
        "typed_EndE_basis_inserted": False,
        "nonidentity_projective_rhoE_inserted": False,
        "direct_same_source_finite_response_inserted": False,
        "oriented_source_theorem_closed": False,
        "new_oriented_leaf_closed": False,
        "current_source_nogo": True,
        "repair_split_built": True,
        "selected_next_repair": insertion_packet["selected_next_repair"],
        "next_required_artifact": NEXT,
        "insertion_packet_path": rel(OUTPUT_INSERTION),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinEndEBasisOrNonidentityRhoEValueInsertion",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "oriented_fill": oriented_fill["status"],
            "typedcech_or_rhoe_attempt": typed_attempt["status"],
            "typedtables_or_rhoe_sourcefill": sourcefill["status"],
            "domain_or_rhoe_gate": domain_or_rhoe["status"],
        },
        "insertion_packet_path": rel(OUTPUT_INSERTION),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinEndEOrRhoEValueInsertionCurrentSourceNoGo",
            "proved": True,
            "statement": (
                "The oriented Phi_fin value-insertion attempt imports the complete typed-Cech "
                "and projective-rhoE fill attempts. Neither emits selected finite End(E) "
                "basis/cochains nor selected nonidentity heterotic rho_E tables. Therefore "
                "the oriented threshold source theorem remains open. The repair front is now "
                "split into three legal minimal repairs: source-amended typed f,g/End(E) "
                "tables, source-amended projective rho_E representative tables, or a direct "
                "same-source finite response payload that bypasses both table lanes."
            ),
        },
        "guardrails": {
            "does_not_promote_structural_typed_support_to_EndE_basis": True,
            "does_not_promote_gerbe_context_to_rhoE_tables": True,
            "does_not_import_routec_values_as_heterotic_values": True,
            "does_not_promote_oriented_logdets": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "insertion_packet_path": rel(OUTPUT_INSERTION),
        "note_path": rel(OUTPUT_NOTE),
        "typed_EndE_basis_inserted": False,
        "nonidentity_projective_rhoE_inserted": False,
        "direct_same_source_finite_response_inserted": False,
        "oriented_source_theorem_closed": False,
        "selected_next_repair": insertion_packet["selected_next_repair"],
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin EndE Basis or NonidentityRhoE ValueInsertion v1

## Result

```text
status = {STATUS}
typed_EndE_basis_inserted = false
nonidentity_projective_rhoE_inserted = false
direct_same_source_finite_response_inserted = false
oriented_source_theorem_closed = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Insertion Packet

```text
{rel(OUTPUT_INSERTION)}
```

## Selected Next Repair

```text
{insertion_packet["selected_next_repair"]}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_INSERTION)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
