"""Import Route-C Weyl-pair source-provenance reduction."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "routec_weylpair_conditional_a_solve_import_certificate.json"
SM_PROVENANCE = SM / "candidate_data" / "selected_routec_weylpair_source_provenance_lemma.candidate.json"
SM_TRANSFER = SM / "candidate_data" / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
Q79_PROVENANCE = Q79 / "candidate_data" / "q79_routec_weylpair_source_provenance_lemma.candidate.json"

OUTPUT_PACKET = DATA / "routec_weylpair_source_provenance_reduction_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_weylpair_source_provenance_reduction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_WeylPair_Source_Provenance_Reduction_Import_v1.md"

STATUS = "ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_IMPORTED_CARRIER_CLOSED_SECTOR_CHARGE_OPEN"
PREVIOUS_STATUS = "ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_IMPORTED_SOURCE_PROVENANCE_OPEN"
NEXT = "Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_prov = load(SM_PROVENANCE)
    sm_transfer = load(SM_TRANSFER)
    q79 = load(Q79_PROVENANCE)
    qred = q79["source_provenance_reduction"]

    checks = {
        "J0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "J1_source_level_carrier_closed": sm_prov["source_level_weyl_carrier"]["proved"] is True
        and sm_prov["source_level_weyl_carrier"]["source_level_flags"]["selected_by_mtt_at_s3_level"]
        is True
        and sm_prov["source_level_weyl_carrier"]["source_level_flags"][
            "source_level_projective_class_selected"
        ]
        is True
        and sm_prov["source_level_weyl_carrier"]["source_level_flags"][
            "operator_level_projective_rhoE_promoted"
        ]
        is False,
        "J2_active_shift_provenance_closed": sm_prov["active_shift_provenance"]["proved"] is True
        and sm_prov["active_shift_provenance"]["nonzero_active_shifts"] == [[1, 1]],
        "J3_conditional_transfer_exact": sm_transfer["conditional_transfer_map"]["conditional_exact"] is True
        and sm_transfer["conditional_transfer_map"]["phase_residual"] == 0.0
        and sm_transfer["conditional_transfer_map"]["shift_residual"] == 0.0
        and sm_transfer["selected_status"]["selected_transfer_map_emitted"] is False
        and sm_transfer["selected_status"]["selected_sector_routing_emitted"] is False,
        "J4_q79_sector_routing_not_selected": qred["sector_routing"]["proved_by_locked_columns"] is True
        and qred["sector_routing"]["source_data_independently_selects_route"] is False
        and qred["sector_routing"]["proved_by_selected_source"] is False
        and qred["sector_routing"]["fully_proved"] is False
        and len(qred["sector_routing"]["exact_rows_relative_to_locked_columns"]) == 1,
        "J5_q79_decision_guardrails": q79["decision"]["source_level_weyl_carrier_and_active_shift_proved"]
        is True
        and q79["decision"]["conditional_source_to_C1_transfer_exact"] is True
        and q79["decision"]["selected_sector_route_independently_proved"] is False
        and q79["decision"]["selected_transfer_map_emitted"] is False
        and q79["decision"]["conditional_A_promoted_to_A_selected"] is False
        and q79["guardrails"]["claims_conditional_transfer_is_selected_C1_map"] is False
        and q79["guardrails"]["uses_locked_target_columns_as_source_selector"] is False
        and q79["target_fitting_used"] is False,
    }

    return {
        "packet": "RouteC_WeylPair_Source_Provenance_Reduction_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_source_provenance": str(SM_PROVENANCE),
            "sm_source_to_c1_transfer": str(SM_TRANSFER),
            "q79_source_provenance": str(Q79_PROVENANCE),
        },
        "theorem": {
            "name": "RouteCWeylPairSourceProvenanceReductionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected q79/S3/Green-Schwarz source-level qutrit Weyl "
                "carrier is closed: the phase generator Z, shift generator X, "
                "and active shift (1,1) have source provenance. The transfer "
                "from that carrier to the C1 phase/shift columns is conditionally "
                "exact, but current source data do not independently select the "
                "sector route {u,e}|{d,nuD} or transfer normalization. The next "
                "non-circular gate is a selected sector-charge/chirality certificate."
            ),
        },
        "checks": checks,
        "sm_source_provenance": sm_prov,
        "sm_source_to_c1_transfer": sm_transfer,
        "q79_source_provenance": q79,
        "source_level_closure": {
            "carrier_proved": True,
            "phase_Z_residual": qred["source_level_carrier"]["g1_equals_phase_Z_residual"],
            "shift_X_residual": qred["source_level_carrier"]["g2_equals_shift_X_residual"],
            "projective_commutator_residual": qred["source_level_carrier"][
                "projective_commutator_residual_imported"
            ],
            "active_shift": qred["active_shift"]["nonzero_active_shifts"],
        },
        "conditional_transfer": qred["source_to_c1_transfer"],
        "sector_routing_reduction": qred["sector_routing"],
        "what_closes_now": {
            "source_level_phase_Z_carrier_provenance": True,
            "source_level_shift_X_carrier_provenance": True,
            "active_shift_1_1_provenance": True,
            "conditional_source_to_C1_transfer_exact": True,
            "sector_routing_gap_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": q79["still_open"],
        "guardrails": q79["guardrails"],
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCWeylPairSourceProvenanceReductionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "source_level_closure": packet["source_level_closure"],
        "conditional_transfer": packet["conditional_transfer"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    source = cert["source_level_closure"]
    transfer = cert["conditional_transfer"]
    return f"""# RouteC WeylPair Source Provenance Reduction Import v1

Status: `{cert["status"]}`.

The source-level qutrit Weyl carrier is now closed: the selected S3/GS source
supplies the phase/clock `Z`, the shift/translation `X`, and active shift
`(1,1)`.

```text
phase_Z_residual              = {source["phase_Z_residual"]}
shift_X_residual              = {source["shift_X_residual"]}
projective_commutator_residual = {source["projective_commutator_residual"]}
active_shift                  = {source["active_shift"]}
```

The transfer map is conditionally exact:

```text
{transfer["formula"]["phase_column"]}
{transfer["formula"]["shift_column"]}
phase_residual = {transfer["phase_residual"]}
shift_residual = {transfer["shift_residual"]}
```

This still does not promote the conditional transfer to selected `A_selected`.
The missing object is an independent selected sector-charge/chirality certificate
that derives the route `{{u,e}}|{{d,nuD}}` and its normalization without using the
locked target columns as selector.

No observed masses, mixings, CP phase, benchmark matrices, or target residuals
are used as selectors.

Next artifact: `{cert["next_required_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
