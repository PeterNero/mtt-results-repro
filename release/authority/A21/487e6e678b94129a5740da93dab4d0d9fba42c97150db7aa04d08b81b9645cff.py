from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "candidate_data" / "selected_neutraloperatorunificationandinventoryaudit" / "selected_neutral_operator_contract.packet.json"
CERT = ROOT / "certificates" / "selected_neutraloperatorunificationandinventoryaudit_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    contract = packet["operator_contract"]
    inventory = packet["current_inventory"]
    fields = packet["required_field_acceptance"]

    require(packet["unification_theorem"]["proved"] is True, "neutral operator theorem missing")
    require("M_L,M_D" in contract["complex_symmetric_mass_operator"], "neutral block operator changed")
    require("Takagi" in contract["mass_readout"], "mass readout changed")
    require("NO or IO" in contract["ordering_readout"], "ordering readout changed")
    require("Dirac-only" in contract["ontology_readout"], "ontology readout changed")
    require("k=0 or 672" in contract["character_readout"], "character cut changed")

    require(inventory["selected_static_Dirac_route"] is True, "selected Dirac route lost")
    require(inventory["nuD_shape_is_dimensionful_mass_operator"] is False, "C1 shape overpromoted")
    require(len(inventory["why_C1_shape_rejected"]) == 4, "C1 rejection cutset changed")
    require(inventory["accepted_Dirac_Yukawa_rows"] == 0, "unexpected Dirac value row")
    require(inventory["accepted_Majorana_operator_rows"] == 0, "unexpected Majorana row")
    require(inventory["accepted_absolute_mass_values"] == 0, "unexpected absolute mass source")
    require(inventory["accepted_ontology_selectors"] == 0, "unexpected ontology selector")

    require(fields["neutral_basis_L_and_Nc"] is True, "neutral basis missing")
    require(sum(fields.values()) == packet["required_fields_closed"] == 1, "field acceptance count changed")
    require(packet["required_fields_total"] == 8, "field total changed")
    require(packet["selected_neutral_operator_accepted"] is False, "operator overaccepted")
    require(packet["conditional_boundary_result"]["minimal_trace_formula_closed"] is True, "boundary formula lost")
    require(packet["U5_previous_source_clause_count"] == 3, "previous U5 cutset changed")
    require(packet["U5_unified_missing_object_count"] == 1, "U5 did not contract to one object")
    require(packet["U5_closed"] is False, "U5 overclosed")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(cert["next_required_artifact"] == "MTT_Selected_NeutralMassOperator_SourceEmission_v1", "next target changed")

    print(
        json.dumps(
            {
                "previous_source_clauses": cert["previous_source_clause_count"],
                "unified_missing_objects": cert["unified_missing_object_count"],
                "required_fields": f"{cert['required_fields_closed']}/{cert['required_fields_total']}",
                "C1_response_rejected": cert["dimensionless_nuD_response_rejected_as_mass_operator"],
                "U5_closed": cert["U5_closed"],
            },
            indent=2,
        )
    )
    print("selected neutral operator unification and inventory audit passed")


if __name__ == "__main__":
    main()
