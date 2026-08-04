"""Build the U5 neutral mass-operator source-emission successor packet.

This artifact advances A21 without mutating it.  A21 proved that U5 reduces to
one selected complex-symmetric neutral operator, but only the neutral basis was
accepted.  Here we import the later selected branch/HYM/Dirac-channel evidence
and fill only the source-provenance fields it actually justifies.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralmassoperator_sourceemission"
OUT_DIR = ROOT / "candidate_data" / SLUG
OUT_CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
OUT_PACKET = OUT_DIR / "neutral_mass_operator_source_emission.packet.json"
OUT_CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralMassOperator_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_NEUTRALMASSOPERATOR_SOURCEEMISSION_PROVENANCE_4OF8_VALUE_BLOCKS_OPEN"
NEXT = "MTT_Selected_NeutralDimensionfulBlocksAndNormalization_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(
        ROOT
        / "candidate_data"
        / "selected_neutraloperatorunificationandinventoryaudit"
        / "selected_neutral_operator_contract.packet.json"
    )
    branch = load(
        ROOT / "certificates" / "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness_certificate.json"
    )
    hym = load(ROOT / "certificates" / "selected_hymvalidatedfourierresidualtailbound_certificate.json")
    neutrino_cp = load(ROOT / "certificates" / "selected_neutrinoandstrongcp_strictupgradeattack_certificate.json")
    static_action = load(ROOT / "certificates" / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json")
    neutral_boundary = load(ROOT / "certificates" / "selected_neutralnilboundarymassfunctional_certificate.json")

    source_id_closed = (
        branch["orientation_level_selection_closed"]
        and branch["time_oriented_q79_representative_closed"]
        and hym["literal_global_HYM_witness_closed"]
    )
    character_gate_closed = (
        neutrino_cp["selected_Dirac_channel_closed"]
        and neutrino_cp["Majorana_admissible_characters"] == [0, 672]
        and static_action["selected_SMSlotFunctor_all_six_arrows_claimed"]
    )

    required_fields = {
        "source_id": source_id_closed,
        "neutral_basis_L_and_Nc": previous["required_field_acceptance"]["neutral_basis_L_and_Nc"],
        "dimensionful_M_D_3x3": False,
        "dimensionful_M_L_3x3": False,
        "dimensionful_M_R_3x3": False,
        "Dirac_U1_or_selected_self_character_k": character_gate_closed,
        "absolute_normalization_and_scheme": False,
        "same_source_no_observed_selector_certificate": True,
    }

    packet = {
        "schema": "MTTSelectedNeutralMassOperatorSourceEmission.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralOperatorUnificationAndInventoryAudit_v1",
        "operator_contract": previous["operator_contract"],
        "source_identity": {
            "selected_branch": "q79/F/m1 retarded representative",
            "selected_branch_closed": source_id_closed,
            "literal_global_HYM_witness_closed": hym["literal_global_HYM_witness_closed"],
            "global_uniqueness_closed": branch["U9_full_superset_uniqueness_closed"],
            "source_id_accepted_for_this_operator_attempt": source_id_closed,
        },
        "character_and_ontology_gate": {
            "selected_1M_equals_Nc_Dirac_channel": neutrino_cp["selected_Dirac_channel_closed"],
            "selected_static_action_all_six_arrows": static_action["selected_SMSlotFunctor_all_six_arrows_claimed"],
            "Majorana_admissible_characters_Z1344": neutrino_cp["Majorana_admissible_characters"],
            "Dirac_U1_or_self_character_gate_closed": character_gate_closed,
            "Dirac_only_completeness_closed": False,
            "separate_Majorana_operator_excluded": False,
            "reason": (
                "The selected action emits the neutral Dirac route and the only admissible Majorana "
                "self-characters are k=0,672.  This closes the character gate for a neutral mass "
                "operator, but it does not prove that every admissible successor excludes a separate "
                "Majorana block."
            ),
        },
        "value_block_status": {
            "dimensionless_C1_nuD_shape_rejected": previous["current_inventory"]["nuD_shape_is_dimensionful_mass_operator"] is False,
            "dimensionful_M_D_3x3_emitted": False,
            "dimensionful_M_L_3x3_emitted": False,
            "dimensionful_M_R_3x3_emitted": False,
            "absolute_normalization_and_scheme_emitted": False,
            "nil_boundary_minimal_trace_formula_closed": neutral_boundary["minimal_trace_boundary_theorem_proved"],
            "nil_boundary_source_promotion_closed": neutral_boundary["neutral_source_promotion_closed"],
            "ordering_selected": neutral_boundary["ordering_selected"],
        },
        "required_field_acceptance": required_fields,
        "required_fields_closed": sum(bool(value) for value in required_fields.values()),
        "required_fields_total": len(required_fields),
        "selected_neutral_operator_accepted": all(required_fields.values()),
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "hard_remaining_fields": [
            "dimensionful_M_D_3x3",
            "dimensionful_M_L_3x3_or_selected_zero_block_with_action_completeness",
            "dimensionful_M_R_3x3_or_selected_zero_block_with_action_completeness",
            "absolute_normalization_and_scheme",
        ],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralMassOperator_SourceEmission_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": True,
        "source_id_closed": required_fields["source_id"],
        "neutral_basis_closed": required_fields["neutral_basis_L_and_Nc"],
        "Dirac_U1_or_selected_self_character_k_closed": required_fields[
            "Dirac_U1_or_selected_self_character_k"
        ],
        "same_source_no_observed_selector_certificate_closed": required_fields[
            "same_source_no_observed_selector_certificate"
        ],
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "required_fields_closed": packet["required_fields_closed"],
        "required_fields_total": packet["required_fields_total"],
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Mass Operator Source Emission v1

## What closes here

This successor imports the selected q79/F/m1 retarded representative, the
literal global HYM witness, the selected `1_M=N^c` Dirac route, and the
`Z1344` Majorana self-character criterion.

Accepted neutral-operator fields are now `{packet["required_fields_closed"]}/{packet["required_fields_total"]}`:

- `source_id`
- `neutral_basis_L_and_Nc`
- `Dirac_U1_or_selected_self_character_k`
- `same_source_no_observed_selector_certificate`

The old C1 `nuD` response remains rejected as an absolute mass operator.

## What does not close

No dimensionful neutral mass blocks are emitted here.  In particular, this
packet does not provide a dimensionful `M_D`, does not prove selected zero
Majorana blocks by action-completeness, does not emit a separate `M_L` or `M_R`,
and does not select the absolute normalization/scheme.

Therefore U5 remains partial.  The next required artifact is
`{NEXT}`.
"""

    dump(OUT_PACKET, packet)
    dump(OUT_CANDIDATE, packet)
    dump(OUT_CERT, cert)
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
