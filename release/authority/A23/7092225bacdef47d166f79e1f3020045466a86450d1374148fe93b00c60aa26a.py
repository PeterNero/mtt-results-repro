from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralmassoperator_sourceemission"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
PACKET = ROOT / "candidate_data" / SLUG / "neutral_mass_operator_source_emission.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralMassOperator_SourceEmission_v1.md"

STATUS = "MTT_SELECTED_NEUTRALMASSOPERATOR_SOURCEEMISSION_PROVENANCE_4OF8_VALUE_BLOCKS_OPEN"
NEXT = "MTT_Selected_NeutralDimensionfulBlocksAndNormalization_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    packet = load(PACKET)
    candidate = load(CANDIDATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == STATUS, "packet status changed")
    require(cert["status"] == STATUS, "certificate status changed")
    require(packet["next_required_artifact"] == NEXT, "packet next artifact changed")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact changed")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(packet["target_fitting_used"] is False, "target fitting used")
    require(cert["observed_data_used_as_selector"] is False, "cert observed selector used")
    require(cert["target_fitting_used"] is False, "cert target fitting used")

    fields = packet["required_field_acceptance"]
    require(packet["required_fields_total"] == 8, "field total changed")
    require(packet["required_fields_closed"] == 4, "field closed count changed")
    require(cert["required_fields_closed"] == 4, "cert field closed count changed")
    require(cert["required_fields_total"] == 8, "cert field total changed")
    require(fields["source_id"] is True, "source id not closed")
    require(fields["neutral_basis_L_and_Nc"] is True, "neutral basis not closed")
    require(fields["Dirac_U1_or_selected_self_character_k"] is True, "character gate not closed")
    require(fields["same_source_no_observed_selector_certificate"] is True, "source certificate not closed")
    require(fields["dimensionful_M_D_3x3"] is False, "M_D overclosed")
    require(fields["dimensionful_M_L_3x3"] is False, "M_L overclosed")
    require(fields["dimensionful_M_R_3x3"] is False, "M_R overclosed")
    require(fields["absolute_normalization_and_scheme"] is False, "normalization overclosed")

    source = packet["source_identity"]
    require(source["selected_branch"] == "q79/F/m1 retarded representative", "source branch changed")
    require(source["selected_branch_closed"] is True, "selected branch not closed")
    require(source["literal_global_HYM_witness_closed"] is True, "literal HYM witness not closed")
    require(source["global_uniqueness_closed"] is False, "global uniqueness overclosed")
    require(source["source_id_accepted_for_this_operator_attempt"] is True, "source id not accepted")

    character = packet["character_and_ontology_gate"]
    require(character["selected_1M_equals_Nc_Dirac_channel"] is True, "Dirac channel not imported")
    require(character["selected_static_action_all_six_arrows"] is True, "static action not imported")
    require(character["Majorana_admissible_characters_Z1344"] == [0, 672], "Majorana character set changed")
    require(character["Dirac_U1_or_self_character_gate_closed"] is True, "Dirac/self-character gate not closed")
    require(character["Dirac_only_completeness_closed"] is False, "Dirac-only completeness overclosed")
    require(character["separate_Majorana_operator_excluded"] is False, "Majorana extension overexcluded")

    values = packet["value_block_status"]
    require(values["dimensionless_C1_nuD_shape_rejected"] is True, "C1 shortcut not rejected")
    require(values["dimensionful_M_D_3x3_emitted"] is False, "M_D emitted unexpectedly")
    require(values["dimensionful_M_L_3x3_emitted"] is False, "M_L emitted unexpectedly")
    require(values["dimensionful_M_R_3x3_emitted"] is False, "M_R emitted unexpectedly")
    require(values["absolute_normalization_and_scheme_emitted"] is False, "normalization emitted unexpectedly")
    require(values["nil_boundary_minimal_trace_formula_closed"] is True, "nil boundary theorem lost")
    require(values["nil_boundary_source_promotion_closed"] is False, "nil boundary source overpromoted")
    require(values["ordering_selected"] is False, "ordering overselected")

    require(packet["selected_neutral_operator_accepted"] is False, "neutral operator overaccepted")
    require(packet["U5_closed"] is False, "U5 overclosed")
    require(cert["selected_neutral_operator_accepted"] is False, "cert neutral operator overaccepted")
    require(cert["U5_closed"] is False, "cert U5 overclosed")
    require(packet["hard_remaining_fields"] == [
        "dimensionful_M_D_3x3",
        "dimensionful_M_L_3x3_or_selected_zero_block_with_action_completeness",
        "dimensionful_M_R_3x3_or_selected_zero_block_with_action_completeness",
        "absolute_normalization_and_scheme",
    ], "remaining U5 fields changed")

    for phrase in [
        "Accepted neutral-operator fields are now `4/8`",
        "`source_id`",
        "`Dirac_U1_or_selected_self_character_k`",
        "No dimensionful neutral mass blocks are emitted here.",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(json.dumps({
        "U5_required_fields": "4/8",
        "source_id": True,
        "character_gate": True,
        "dimensionful_blocks": False,
        "U5_closed": False,
    }, indent=2))
    print("selected neutral mass-operator source-emission audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
