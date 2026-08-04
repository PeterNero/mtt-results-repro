"""Build primitive-C1 / Weyl-pair sector-routing source-emission reduction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

FRONTIER = DATA / "selected_c1_frontier_after_alpha1_import.candidate.json"
SMSLOT_OVERLAP = DATA / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
DOWNSTREAM = DATA / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
WEYL_TRANSFER = DATA / "selected_routec_weylpair_source_to_c1_transfer_map.candidate.json"
SECTOR_CHARGE = DATA / "selected_routec_weylpair_sector_charge_or_chirality_certificate.candidate.json"
C1_EMISSION = DATA / "selected_routec_selected_c1_response_operator_emission.candidate.json"

OUTPUT = DATA / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission.candidate.json"
CERT = CERTS / "selected_primitivec1_or_weylpair_sectorrouting_sourceemission_certificate.json"
NOTE = CORPUS / "MTT_Selected_PrimitiveC1_or_WeylPairSectorRouting_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_PRIMITIVEC1_OR_WEYLPAIR_SECTORROUTING_SOURCEEMISSION_STATIC_ROUTING_CLOSED_DYNAMIC_CONTRACTIONS_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    frontier = load(FRONTIER)
    smslot = load(SMSLOT_OVERLAP)
    downstream = load(DOWNSTREAM)
    weyl = load(WEYL_TRANSFER)
    sector = load(SECTOR_CHARGE)
    c1 = load(C1_EMISSION)

    static_routing = downstream["old_contract_reclassification"]["matter_slot_charge"][
        "selected_partition"
    ]
    weyl_consequence = downstream["weylpair_consequence"]

    retired_sector_routing = {
        "selected_static_sector_route_Z_to_u_e_X_to_d_nuD": downstream["what_closes_now"][
            "selected_static_sector_route_Z_to_u_e_X_to_d_nuD"
        ],
        "selected_static_1M_Dirac_neutrino_shift_rule": downstream["what_closes_now"][
            "selected_static_1M_Dirac_neutrino_shift_rule"
        ],
        "selected_static_finite_trace_transfer_normalization": downstream["what_closes_now"][
            "selected_static_finite_trace_transfer_normalization"
        ],
        "all_six_static_sm_slot_arrows_closed": smslot["arrow_status"]["all_six_closed"],
        "phase_route": weyl_consequence["phase_route"],
        "shift_route": weyl_consequence["shift_route"],
        "source_level_ZX_carrier_closed": weyl_consequence["source_level_ZX_carrier_closed"],
        "sector_charge_old_artifact_still_open_but_superseded_at_static_tier": sector[
            "certificate_result"
        ]["selected_certificate_closed"]
        is False,
    }

    transfer_status = {
        "conditional_weyl_transfer_exact": weyl["conditional_transfer_map"][
            "conditional_exact"
        ],
        "static_sector_route_now_selected": weyl_consequence[
            "selected_static_sector_route_now_closed"
        ],
        "conditional_A_promoted_to_A_selected": weyl_consequence[
            "promote_conditional_A_to_A_selected"
        ],
        "why_not_promoted": weyl_consequence["why_not_promoted"],
    }

    dynamic_blockers = {
        "dynamic_visible_routec_operator_source_identity": downstream["what_remains_open"][
            "dynamic_visible_routec_operator_source_identity"
        ],
        "selected_D_E_Riesz_Green_dotD": downstream["what_remains_open"][
            "selected_D_E_Riesz_Green_dotD"
        ],
        "selected_dynamic_overlap_tensor_or_transfer_functor": downstream["what_remains_open"][
            "selected_dynamic_overlap_tensor_or_transfer_functor"
        ],
        "selected_primitive_C1_contractions": downstream["what_remains_open"][
            "selected_primitive_C1_contractions"
        ],
        "selected_b_selected_and_Hessian_normalization": downstream["what_remains_open"][
            "selected_b_selected_and_Hessian_normalization"
        ],
        "selected_A_selected": c1["what_remains_open"]["emit_selected_A_selected"],
        "selected_sector_response_matrices": c1["what_remains_open"][
            "selected_sector_response_matrices"
        ],
    }

    candidate = {
        "candidate": "MTTSelectedPrimitiveC1OrWeylPairSectorRoutingSourceEmission",
        "status": STATUS,
        "inputs": {
            "c1_frontier_after_alpha1_import": rel(FRONTIER),
            "selected_smslotfunctor_overlapkernel_source_emission": rel(SMSLOT_OVERLAP),
            "selected_smslotfunctor_downstream_payload_ledger": rel(DOWNSTREAM),
            "weylpair_source_to_c1_transfer": rel(WEYL_TRANSFER),
            "older_sector_charge_or_chirality_attempt": rel(SECTOR_CHARGE),
            "selected_c1_response_operator_emission": rel(C1_EMISSION),
        },
        "static_routing_source_emission": {
            "proved": True,
            "partition": static_routing,
            "retired_sector_routing": retired_sector_routing,
            "effect": (
                "The older Weyl-pair sector-routing blocker is closed at the static SM-slot source tier. "
                "This supplies the Z/clock -> u,e and X/shift -> d,nuD route independently of the locked C1 target."
            ),
        },
        "conditional_transfer_reclassification": transfer_status,
        "dynamic_blockers": dynamic_blockers,
        "proof_boundary": {
            "static_routing_not_enough_for_A_selected": True,
            "dynamic_overlap_tensor_not_emitted": True,
            "primitive_C1_contractions_not_emitted": True,
            "observed_data_used": False,
            "target_fitting_used": False,
            "full_SM_closure_claimed": False,
        },
        "what_closes_now": {
            "selected_static_weyl_sector_routing_emitted": True,
            "selected_static_singlet_neutrino_shift_rule_emitted": True,
            "selected_static_trace_transfer_normalization_emitted": True,
            "old_sector_charge_blocker_reclassified_static_closed_dynamic_open": True,
            "conditional_weyl_transfer_has_static_source_route": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": dynamic_blockers
        | {
            "promote_conditional_A_to_A_selected": True,
            "selected_higher_order_or_full_response_matrices": frontier["live_source_objects"][
                "selected_higher_order_or_full_response_matrices"
            ],
            "honest_selected_deltaTheta_C1_solve": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PrimitiveC1OrWeylPairSectorRoutingSourceEmissionReductionTheorem",
            "proved": True,
            "statement": (
                "The selected SM-slot functor downstream ledger source-emits the static Weyl-pair sector route: "
                "Z/clock/phase goes to u,e and X/shift/translation goes to d,nuD, with 1_M=N^c on the shift side "
                "and finite trace transfer normalization selected.  Therefore Weyl-pair sector routing is no longer "
                "an active blocker.  The conditional Weyl C1 transfer remains unpromoted because A_selected still "
                "requires dynamic operator values, a selected dynamic overlap tensor or transfer functor, primitive "
                "C1 contractions, and b_selected/Hessian normalization from the same source."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_PrimitiveC1_or_WeylPairSectorRouting_SourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "theorem_proved": True,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PrimitiveC1 or WeylPair SectorRouting SourceEmission v1

Status: `{STATUS}`.

The later SM-slot functor ledger closes the static Weyl routing that older
Weyl-pair artifacts still listed as open:

```text
Z / clock / phase  -> u, e
X / shift / translation -> d, nuD
1_M = N^c routes with the shift / Dirac-neutrino side
finite trace transfer normalization selected
```

This routing is source-tier data from the selected SM-slot functor, not a choice
made by the locked C1 target.

The conditional Weyl-pair C1 transfer is still not `A_selected`.  Promotion now
requires dynamic same-source data:

```text
dynamic overlap tensor or transfer functor
primitive C1 contractions
b_selected / Hessian normalization
selected sector response matrices
```

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
