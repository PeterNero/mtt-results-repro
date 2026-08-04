"""Audit rho/tau shadow guard after common-carrier co-emission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject.py"

SLUG = "selected_rhotau_shadowguard_after_commoncarrier_or_selectedsourceobject"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RhoTauShadowGuard_AfterCommonCarrier_or_SelectedSourceObject_v1.md"
SHADOW_PACKET = PACKET_DIR / "rho_tau_shadow_guard.packet.json"
STATEMENT_PACKET = PACKET_DIR / "source_emission_statement_revalidation_after_shadowguard.packet.json"
FIELD_PACKET = PACKET_DIR / "source_object_field_revalidation_after_shadowguard.packet.json"
BRANCH_PACKET = PACKET_DIR / "selected_source_object_gate_after_shadowguard.packet.json"
NEXT_PACKET = PACKET_DIR / "next_selectedsourceobject_or_nolift_or_cechhym_contract.packet.json"

STATUS = (
    "MTT_SELECTED_RHOTAU_SHADOWGUARD_AFTER_COMMONCARRIER_"
    "NINE_OF_ELEVEN_FIELDS_PROMOTED_SELECTEDSOURCEOBJECT_OPEN"
)
NEXT = "MTT_Selected_SelectedSourceObjectSQaSU3BN27_or_NoLiftReplay_or_CechHYMConnectionValues_v1"
PROMOTED_FIELD = "eleven_label_rho_tau_shadow_embeds_but_is_not_threshold_domain"
ACCEPTED_STATEMENTS = [
    "full_F3xF3_carrier_emitted_before_finite_comparison",
    "kernel_and_trace_policies_source_owned",
    "RouteC_row_internal_not_external",
]
REMAINING_STATEMENTS = [
    "C_tau_and_PhiFin_DE_coemitted_by_source",
    "S_QaSU3_BN27_is_selected_threshold_source",
    "no_lift_replay_audit_from_emitted_fields",
]
REMAINING_FIELDS = [
    "no_lifted_flags_full_replay_audit",
    "selected_source_object_S_QaSU3_BN27",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    shadow = load(SHADOW_PACKET)
    statements = load(STATEMENT_PACKET)
    fields = load(FIELD_PACKET)
    branch = load(BRANCH_PACKET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")

    for payload in [candidate, cert, shadow, statements, fields, branch, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    require(shadow["promotes_source_object_field"] == PROMOTED_FIELD, "shadow promoted field")
    require(shadow["label_embedding_candidate_built"] is True, "label embedding missing")
    require(shadow["projection_pair_candidate_valid_as_injection"] is True, "projection injection missing")
    require(shadow["rhoE_character_intertwines"] is True, "rhoE intertwiner missing")
    require(shadow["D_E_or_EQa_intertwines"] is False, "D_E/EQa overclaim")
    require(shadow["finitepart_regularization_same_scheme"] is False, "finitepart scheme overclaim")
    require(shadow["orientation_functor_closed"] is True, "orientation functor missing")
    require(shadow["threshold_magnitude_functor_closed"] is False, "magnitude overclaim")
    require(shadow["rho_shadow_embedding_retained"] is True, "shadow embedding not retained")
    require(shadow["orientation_shadow_still_valid"] is True, "orientation shadow invalid")
    require(shadow["retired_as_threshold_proof_source"] is True, "shadow not retired")
    require(shadow["shadow_product"] == 16, "shadow product")
    require(shadow["required_full_orbit_product"] == 9600 * 9600, "full orbit product")
    require(shadow["missing_multiplier"] == 5760000, "missing multiplier")
    require(shadow["shadow_product"] * shadow["missing_multiplier"] == shadow["required_full_orbit_product"], "multiplier arithmetic")
    require(shadow["missing_positive_oriented_row_count"] == 10, "missing row count")
    for key in [
        "projective_rhoE_BN27_lift_closed",
        "selected_source_object_closed",
        "source_branch_identity_closed",
        "oriented_logdet_promoted",
        "no_lift_replay_allowed",
    ]:
        require(shadow[key] is False, f"shadow overclaim: {key}")

    require(statements["previous_emitted_source_statement_count"] == 3, "previous statement count")
    require(statements["emitted_source_statement_count"] == 3, "statement count changed")
    require(statements["required_source_statement_count"] == 6, "required statements")
    require(statements["accepted_statements"] == ACCEPTED_STATEMENTS, "accepted statements")
    require(statements["remaining_statements"] == REMAINING_STATEMENTS, "remaining statements")
    for statement in ACCEPTED_STATEMENTS:
        require(statements["rows"][statement]["emitted_as_source_owned"] is True, f"statement not retained: {statement}")
    for statement in REMAINING_STATEMENTS:
        require(statements["rows"][statement]["emitted_as_source_owned"] is False, f"statement overpromoted: {statement}")
    require(statements["rows"]["S_QaSU3_BN27_is_selected_threshold_source"]["rho_tau_shadow_guard_closed"] is True, "statement guard missing")
    require(statements["rho_tau_shadow_guard_closed"] is True, "statement shadow flag")
    for key in ["same_branch_coemission_closed", "direct_source_theorem_closed", "selected_source_object_closed"]:
        require(statements[key] is False, f"statement overclaim: {key}")

    require(fields["previous_promoted_source_object_field_count"] == 8, "previous field count")
    require(fields["promoted_source_object_field_count"] == 9, "field count")
    require(fields["required_source_object_field_count"] == 11, "required fields")
    require(fields["newly_promoted_source_object_fields"] == [PROMOTED_FIELD], "new field")
    require(fields["fields"][PROMOTED_FIELD]["source_owned"] is True, "shadow field not promoted")
    require(
        fields["fields"][PROMOTED_FIELD]["scope"] == "negative_guard_retiring_projective_shadow_as_threshold_source",
        "field scope guard",
    )
    require(fields["remaining_source_object_fields"] == REMAINING_FIELDS, "remaining fields")
    for field in REMAINING_FIELDS:
        require(fields["fields"][field]["source_owned"] is False, f"field overpromoted: {field}")
    require(fields["rho_tau_shadow_guard_closed"] is True, "field shadow flag")
    require(fields["selected_source_object_S_QaSU3_BN27"] is False, "field selected source overclaim")
    require(fields["no_lifted_flags_full_replay_audit"] is False, "field no-lift overclaim")
    require(fields["oriented_logdet_promoted"] is False, "field logdet overclaim")
    require(fields["unconditional_replay_allowed"] is False, "field replay overclaim")

    require(branch["rho_tau_shadow_guard_closed"] is True, "branch guard")
    require(branch["projective_shadow_retired_as_threshold_proof_source"] is True, "branch retired guard")
    require(branch["retired_root_clause"] == "eleven_label_to_full_BN27_threshold_carrier", "retired clause")
    require(branch["final_connection_tables_accepted"] == 4, "branch table count")
    for key in [
        "selected_source_object_S_QaSU3_BN27_closed",
        "same_source_owns_both_branches",
        "source_branch_identity_closed",
        "no_lift_replay_closed",
    ]:
        require(branch[key] is False, f"branch overclaim: {key}")
    require("selected_Cech_HYM_connection_values" in branch["remaining_root_clauses"], "cech/hym root missing")

    decision = candidate["closure_decision"]
    require(decision["source_emission_statement_count"] == 3, "decision statement count")
    require(decision["source_object_field_count"] == 9, "decision field count")
    require(decision["newly_promoted_source_object_fields"] == [PROMOTED_FIELD], "decision field")
    require(decision["rho_tau_shadow_guard_closed"] is True, "decision shadow guard")
    require(decision["projective_shadow_retired_as_threshold_proof_source"] is True, "decision retired")
    require(decision["shadow_product"] == 16, "decision shadow product")
    require(decision["required_full_orbit_product"] == 9600 * 9600, "decision full product")
    require(decision["missing_multiplier"] == 5760000, "decision multiplier")
    require(decision["missing_positive_oriented_row_count"] == 10, "decision row count")
    for key in [
        "selected_source_object_S_QaSU3_BN27",
        "C_tau_and_PhiFin_DE_coemitted_by_source",
        "same_source_owns_both_branches",
        "source_branch_identity_closed",
        "oriented_logdet_promoted",
        "no_lifted_flags_connection_replay_promoted",
        "strict_no_knob_closed",
        "true_SM_equivalence_closed",
    ]:
        require(decision[key] is False, f"decision overclaim: {key}")
        require(cert[key] is False, f"cert overclaim: {key}")
    require(decision["final_connection_tables_accepted"] == 4, "decision table count")
    require(cert["final_connection_tables_accepted"] == 4, "cert table count")

    require(next_packet["source_emission_statement_count"] == "3/6", "next statement count")
    require(next_packet["source_object_field_count"] == "9/11", "next field count")
    require(next_packet["final_connection_table_count"] == "4/8", "next table count")
    require(
        any("do not use the 11-label rho/tau shadow" in item for item in next_packet["forbidden_loopback"]),
        "loopback guard",
    )
    require("`8/11` to `9/11`" in note, "note missing 9/11 move")
    require("missing multiplier: `5760000`" in note, "note missing multiplier")
    require(NEXT in note, "note missing next")

    print("Rho/tau shadow guard after common-carrier audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
