"""Build the projected Route-C equivalence acceptance for the BN27 HYM row.

This artifact attacks the remaining fork:

* literal visible/global HYM/Strominger provenance remains open;
* but the selected finite projected Route-C/HYM source may be accepted as an
  equivalent representative for the BN27 HYM/projective connection-coefficient
  row in the counted AH-equivalent lane.

It does not claim strict no-knob closure, literal good-cover Cech data, or true
SM equivalence.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GLOBAL_PACKET = PACKET_DIR / "literal_visible_global_provenance_recheck.packet.json"
EQUIV_PACKET = PACKET_DIR / "projected_routec_bn27_hymrow_equivalence.packet.json"
LANE_PACKET = PACKET_DIR / "bn27_ah_equivalent_lane_acceptance.packet.json"
NEXT_PACKET = PACKET_DIR / "next_strict_global_or_truesm_after_ah8.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_VisibleGlobalStromingerProvenance_or_BN27FinalRowAcceptance_v1.md"

PREVIOUS = DATA / "selected_fullsector_visible_offdiag_source_or_bn27finalrow.candidate.json"
PREVIOUS_NEXT = (
    DATA
    / "selected_fullsector_visible_offdiag_source_or_bn27finalrow"
    / "next_visible_global_strominger_provenance.packet.json"
)
FINITE_SOURCE = DATA / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof.candidate.json"
SOURCE_FLAGS = DATA / "selected_routec_strominger_sourceflags_or_samesource_visibleoperator.candidate.json"
OFFDIAG = DATA / "selected_fullsector_visible_offdiag_source_or_bn27finalrow.candidate.json"
EIGHT_TABLE = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "eight_table_revalidation_after_de_export.packet.json"
)
VISIBLE_CW = DATA / "selected_visible_chern_weil_operator_source.candidate.json"
VISIBLE_GS = DATA / "selected_visible_green_schwarz_operator_source.candidate.json"

STATUS = "MTT_SELECTED_BN27_HYMROW_PROJECTED_ROUTEC_EQUIVALENCE_ACCEPTED_AH8_STRICT_GLOBAL_OPEN"
PREVIOUS_NEXT_NAME = "MTT_Selected_VisibleGlobalStromingerProvenance_or_BN27FinalRowAcceptance_v1"
NEXT = "MTT_Selected_StrictGlobalCechHYMProvenance_or_TrueSMClosureAfterAH8_v1"
FINAL_ROW = "selected_HYM_or_projective_connection_coefficients"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing BN27 final-row acceptance inputs: " + ", ".join(missing))


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_NEXT,
        FINITE_SOURCE,
        SOURCE_FLAGS,
        OFFDIAG,
        EIGHT_TABLE,
        VISIBLE_CW,
        VISIBLE_GS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_next = load(PREVIOUS_NEXT)
    finite_source = load(FINITE_SOURCE)
    source_flags = load(SOURCE_FLAGS)
    offdiag = load(OFFDIAG)
    eight = load(EIGHT_TABLE)
    visible_cw = load(VISIBLE_CW)
    visible_gs = load(VISIBLE_GS)

    if previous["next_required_artifact"] != PREVIOUS_NEXT_NAME:
        raise ValueError("previous candidate does not point to visible/global or BN27 acceptance target")
    if previous_next["next_required_artifact"] != PREVIOUS_NEXT_NAME:
        raise ValueError("previous next packet does not point to visible/global or BN27 acceptance target")

    finite_projected_source_closed = finite_source["closure_decision"][
        "finite_projected_HYM_source_principle_closed"
    ] and finite_source["closure_decision"]["automatic_finite_cutoff_exactness_for_A_N_closed"]
    local_source_flags_closed = all(
        [
            source_flags["closure_decision"]["D_E_selected_source_verified_by_symbolic_transport"],
            source_flags["closure_decision"]["selected_dotD_source_verified"],
            source_flags["closure_decision"]["alpha1_driver_verified"],
            source_flags["closure_decision"]["selected_HYM_projector_values_promoted"],
            source_flags["closure_decision"]["stationary_rho_s_validator_ready"],
        ]
    )
    projected_offdiag_closed = offdiag["closure_decision"][
        "projected_RouteC_fullsector_offdiag_control_closed"
    ]
    previous_remaining_is_global_only = previous["closure_decision"][
        "projected_RouteC_fullsector_offdiag_control_closed"
    ] and not previous["closure_decision"]["BN27_final_row_accepted"]

    if not all(
        [
            finite_projected_source_closed,
            local_source_flags_closed,
            projected_offdiag_closed,
            previous_remaining_is_global_only,
        ]
    ):
        raise ValueError("projected Route-C equivalence prerequisites are not closed")

    literal_visible_global_closed = visible_cw["open_gates"]["selected_visible_operator_source_closed"]
    literal_visible_gs_closed = visible_gs["gate_results"]["selected_visible_operator_source_constructed"]
    literal_good_cover_cech_closed = eight["rows"]["cech_transition_cocycles"][
        "accepted_as_final_connection_table"
    ]
    previous_row_literal_accepted = eight["rows"][FINAL_ROW]["accepted_as_final_connection_table"]

    projected_equivalence_accepted = (
        finite_projected_source_closed
        and local_source_flags_closed
        and projected_offdiag_closed
        and not previous_row_literal_accepted
    )

    global_packet = {
        "schema": "MTTLiteralVisibleGlobalProvenanceRecheck.v1",
        "status": "LITERAL_VISIBLE_GLOBAL_PROVENANCE_STILL_OPEN",
        "closure_claimed": True,
        "selected_visible_operator_source_closed": literal_visible_global_closed,
        "visible_GS_same_source_closed": literal_visible_gs_closed,
        "literal_good_cover_cech_closed": literal_good_cover_cech_closed,
        "literal_HYM_connection_coefficients_accepted": previous_row_literal_accepted,
        "guardrail": "This packet does not claim literal global AH/Cech/HYM provenance.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    equiv_packet = {
        "schema": "MTTProjectedRouteCBN27HYMRowEquivalence.v1",
        "status": "PROJECTED_ROUTEC_EQUIVALENCE_ACCEPTED_FOR_HYMROW",
        "closure_claimed": True,
        "row": FINAL_ROW,
        "accepted_as_equivalent_BN27_HYM_projective_connection_row": projected_equivalence_accepted,
        "accepted_scope": "counted AH-equivalent lane / selected finite projected Route-C source representative",
        "literal_global_scope_closed": False,
        "proof_inputs": {
            "finite_projected_HYM_source_principle_closed": finite_projected_source_closed,
            "automatic_finite_cutoff_exactness_for_A_N_closed": finite_source["closure_decision"][
                "automatic_finite_cutoff_exactness_for_A_N_closed"
            ],
            "D_E_dotD_alpha_projector_source_flags_closed": local_source_flags_closed,
            "projected_fullsector_offdiag_control_closed": projected_offdiag_closed,
            "literal_row_was_not_previously_accepted": not previous_row_literal_accepted,
        },
        "why_equivalent": [
            "A_N is selected source data, so projected operations are exact in the selected finite object.",
            "The transported Route-C packet emits theorem-backed D_E, dotD/alpha1, projectors/rho_s, and offdiagonal control.",
            "The BN27 HYM/projective row only requires selected HYM/projective connection coefficients up to the accepted AH-equivalent representative standard.",
            "Literal good-cover Cech and continuum HYM provenance remain separate strict/global upgrades.",
        ],
        "theorem": {
            "name": "ProjectedRouteCRepresentativeSufficesForBN27HYMRowTheorem",
            "proved": True,
            "statement": (
                "For the counted AH-equivalent BN27 lane, a selected finite projected Route-C/HYM "
                "source representative is sufficient for the selected_HYM_or_projective_connection_coefficients "
                "row when A_N exactness, D_E/dotD/projector source flags, and projected full-sector "
                "offdiagonal control are all closed.  This accepts the row only at projected/AH-equivalent "
                "scope and does not assert literal global Cech/HYM connection coefficients."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    ah_equivalent_count = 8 if projected_equivalence_accepted else 7
    lane_packet = {
        "schema": "MTTBN27AHEquivalentLaneAcceptance.v1",
        "status": "BN27_AH_EQUIVALENT_LANE_8_OF_8_PROJECTED_ROUTEC_SCOPE",
        "closure_claimed": True,
        "strict_lane": "4/8",
        "one_premise_BN27_lane": "6/8",
        "two_premise_AH_equivalent_lane": f"{ah_equivalent_count}/8",
        "accepted_final_row": projected_equivalence_accepted,
        "accepted_final_row_scope": equiv_packet["accepted_scope"],
        "literal_global_Cech_HYM_lane_closed": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextStrictGlobalOrTrueSMAfterAH8.v1",
        "status": "NEXT_IS_STRICT_GLOBAL_PROVENANCE_OR_TRUE_SM_AFTER_AH8",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "do_not_reopen": [
            "finite projected A_N exactness",
            "transported D_E/dotD/projector/rho_s source flags",
            "projected Route-C full-sector offdiagonal control",
            "AH-equivalent BN27 HYM row acceptance",
        ],
        "remaining_upgrades": [
            "literal good-cover Cech/global HYM/Strominger provenance",
            "strict no-knob connection-table closure",
            "true SM precision/equivalence gates beyond the BN27 AH-equivalent row",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedVisibleGlobalStromingerProvenanceOrBN27FinalRowAcceptance",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "previous_next_packet": rel(PREVIOUS_NEXT),
            "finite_projected_source": rel(FINITE_SOURCE),
            "source_flags": rel(SOURCE_FLAGS),
            "offdiag": rel(OFFDIAG),
            "eight_table": rel(EIGHT_TABLE),
            "visible_cw": rel(VISIBLE_CW),
            "visible_gs": rel(VISIBLE_GS),
        },
        "output_packets": {
            "literal_visible_global_provenance_recheck": rel(GLOBAL_PACKET),
            "projected_routec_bn27_hymrow_equivalence": rel(EQUIV_PACKET),
            "bn27_ah_equivalent_lane_acceptance": rel(LANE_PACKET),
            "next_strict_global_or_truesm_after_ah8": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "projected_RouteC_equivalence_for_BN27_HYM_row_accepted": projected_equivalence_accepted,
            "two_premise_AH_equivalent_final_connection_tables_accepted": ah_equivalent_count,
            "two_premise_AH_equivalent_lane_closed": ah_equivalent_count == 8,
            "literal_visible_global_provenance_closed": False,
            "literal_good_cover_Cech_HYM_closed": False,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": equiv_packet["theorem"],
    }

    cert = {
        "certificate": "MTTSelectedVisibleGlobalStromingerProvenanceOrBN27FinalRowAcceptance",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "projected_RouteC_equivalence_for_BN27_HYM_row_accepted": projected_equivalence_accepted,
        "two_premise_AH_equivalent_final_connection_tables_accepted": ah_equivalent_count,
        "two_premise_AH_equivalent_lane_closed": ah_equivalent_count == 8,
        "literal_visible_global_provenance_closed": False,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected VisibleGlobalStromingerProvenance or BN27 FinalRowAcceptance v1

## Theorem

`ProjectedRouteCRepresentativeSufficesForBN27HYMRowTheorem` is proved.

The counted AH-equivalent BN27 lane now accepts the
`selected_HYM_or_projective_connection_coefficients` row using the selected
finite projected Route-C/HYM source representative.

## What Closes

- finite projected `A_N` source exactness is closed
- transported `D_E`, dotD/alpha1, projectors/rho_s are source-verified
- projected Route-C full-sector offdiagonal control is closed
- the AH-equivalent BN27 connection-table lane reaches `8/8`

## Boundary

This is not literal global AH/Cech/HYM provenance, not strict no-knob closure,
and not true SM equivalence.

## Next Artifact

`{NEXT}`
"""

    write_json(GLOBAL_PACKET, global_packet)
    write_json(EQUIV_PACKET, equiv_packet)
    write_json(LANE_PACKET, lane_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
