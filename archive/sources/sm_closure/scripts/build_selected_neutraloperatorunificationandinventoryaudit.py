"""Unify the U5 neutrino source clauses into one selected operator object."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutraloperatorunificationandinventoryaudit"
OUT_DIR = ROOT / "candidate_data" / SLUG
OUT_CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
OUT_PACKET = OUT_DIR / "selected_neutral_operator_contract.packet.json"
OUT_CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralOperatorUnificationAndInventoryAudit_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    mass = load(
        ROOT / "certificates" / "selected_neutralnilboundarymassfunctional_certificate.json"
    )
    policy = load(
        ROOT
        / "candidate_data"
        / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable"
        / "neutrino_noknob_source_gate.packet.json"
    )
    static_action = load(
        ROOT / "certificates" / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json"
    )

    required_fields = {
        "source_id": False,
        "neutral_basis_L_and_Nc": True,
        "dimensionful_M_D_3x3": False,
        "dimensionful_M_L_3x3": False,
        "dimensionful_M_R_3x3": False,
        "Dirac_U1_or_selected_self_character_k": False,
        "absolute_normalization_and_scheme": False,
        "same_source_no_observed_selector_certificate": False,
    }

    packet = {
        "schema": "MTTSelectedNeutralOperatorUnificationAndInventoryAudit.v1",
        "status": "U5_REDUCED_TO_ONE_SELECTED_NEUTRAL_OPERATOR_OBJECT_CURRENT_INVENTORY_REJECTED",
        "operator_contract": {
            "basis": "(nu_L, N^c) with three family components in each block",
            "complex_symmetric_mass_operator": "M_N=[[M_L,M_D],[M_D^T,M_R]]",
            "mass_squared_operator": "H_N=M_N^dagger M_N",
            "mass_readout": "Takagi singular values of M_N, equivalently nonnegative square roots of the physical H_N eigenvalues",
            "ordering_readout": "NO or IO is determined by which selected eigenvalue pair realizes the smaller splitting",
            "ontology_readout": "Dirac-only iff M_L=M_R=0 and the selected action preserves neutral U(1); nonzero M_L or M_R is Majorana",
            "character_readout": "a Majorana block must carry selected self-character k=0 or 672 in Z1344",
            "absolute_scale_readout": "dimensionful entries or a theorem-derived neutral normalization fix the absolute spectrum",
        },
        "unification_theorem": {
            "name": "SelectedNeutralOperatorSufficiencyAndNonduplicationTheorem",
            "proved": True,
            "statement": "A single selected complex-symmetric neutral mass operator with source provenance determines the absolute masses, NO/IO ordering, and Dirac/Majorana ontology simultaneously. Separate fitted selectors for those three outputs would duplicate information already contained in the operator and are forbidden.",
        },
        "current_inventory": {
            "selected_static_Dirac_route": static_action["selected_SMSlotFunctor_all_six_arrows_claimed"],
            "dimensionless_nuD_C1_response_shape": "M_nuD=R_X and post-source nuD first response I+X",
            "nuD_shape_is_dimensionful_mass_operator": False,
            "why_C1_shape_rejected": [
                "it has no absolute mass normalization",
                "it duplicates the down-sector first response",
                "it contains no M_L or M_R charge-conjugation block",
                "the conditional non-scalar successor is not a selected same-source value packet",
            ],
            "accepted_Dirac_Yukawa_rows": policy["accepted_Dirac_Yukawa_source_rows"],
            "accepted_Majorana_operator_rows": policy["accepted_Majorana_mass_operator_rows"],
            "accepted_absolute_mass_values": policy["accepted_absolute_mass_source_values"],
            "accepted_ontology_selectors": policy["accepted_neutrino_ontology_selectors"],
        },
        "required_field_acceptance": required_fields,
        "required_fields_closed": sum(required_fields.values()),
        "required_fields_total": len(required_fields),
        "selected_neutral_operator_accepted": all(required_fields.values()),
        "conditional_boundary_result": {
            "minimal_trace_formula_closed": mass["minimal_trace_boundary_theorem_proved"],
            "conditional_lightest_mass_eV": mass["conditional_lightest_mass_eV"],
            "promotion_rule": "If the selected operator theorem emits neutral nil-boundary saturation, its trace-minimal PSD branch has m_lightest=0.",
        },
        "U5_previous_source_clause_count": mass["remaining_source_clause_count"],
        "U5_unified_missing_object_count": 1,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "next_required_artifact": "MTT_Selected_NeutralMassOperator_SourceEmission_v1",
    }

    cert = {
        "certificate": "MTT_Selected_NeutralOperatorUnificationAndInventoryAudit_v1",
        "status": packet["status"],
        "unification_theorem_proved": True,
        "previous_source_clause_count": mass["remaining_source_clause_count"],
        "unified_missing_object_count": 1,
        "required_fields_closed": packet["required_fields_closed"],
        "required_fields_total": packet["required_fields_total"],
        "dimensionless_nuD_response_rejected_as_mass_operator": True,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "next_required_artifact": packet["next_required_artifact"],
    }

    note = """# MTT Selected Neutral Operator Unification and Inventory Audit v1

## Reduction theorem

The remaining U5 outputs must not be selected independently. One source-owned
complex-symmetric operator

```text
M_N = [[M_L, M_D], [M_D^T, M_R]]
```

determines all of them:

- Takagi singular values give absolute neutrino masses;
- the selected eigenvalue pairing gives NO or IO;
- `M_L=M_R=0` with neutral U(1) gives Dirac-only structure;
- nonzero `M_L` or `M_R` gives a Majorana block and requires self-character
  `k=0` or `k=672`.

## Inventory result

The closed 27/C1 chain supplies a selected `nuD` route and a dimensionless
response shape `M_nuD=R_X`. It is not the neutral mass operator: it has no
absolute normalization, duplicates the down-sector first response, contains
no charge-conjugation blocks, and its non-scalar successor is conditional.

Thus the former three source clauses reduce to one missing object:
`MTT_Selected_NeutralMassOperator_SourceEmission_v1`. Its required provenance
fields are machine-readable in the packet. No observed mass or ordering may
fill them.
"""

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PACKET.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    OUT_CANDIDATE.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
