"""Import selected Route-C non-identity rho_E and B_N construction."""

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

PREVIOUS = CERTS / "routec_selected_primitive_emission_search_import_certificate.json"
UPSTREAM_PACKET = SM / "candidate_data" / "selected_routec_nonidentity_rhoe_bn_construction.candidate.json"
UPSTREAM_CERT = SM / "certificates" / "selected_routec_nonidentity_rhoe_bn_construction_certificate.json"

OUTPUT_PACKET = DATA / "routec_nonidentity_rhoe_bn_construction_import.candidate.json"
OUTPUT_CERT = CERTS / "routec_nonidentity_rhoe_bn_construction_import_certificate.json"
OUTPUT_NOTE = CORPUS / "RouteC_NonIdentity_RhoE_BN_Construction_Import_v1.md"

STATUS = "ROUTEC_NONIDENTITY_RHOE_PACKET_IMPORTED_SMOOTH_BN_OPEN"
PREVIOUS_STATUS = "ROUTEC_SELECTED_PRIMITIVE_SEARCH_IMPORTED_NONIDENTITY_RHOE_BN_OPEN"
UPSTREAM_STATUS = "MTT_SELECTED_ROUTEC_NONIDENTITY_RHOE_NUMERICAL_PACKET_BUILT_BN_STILL_OPEN"
NEXT = "MTT_Selected_RouteC_Smooth_BN_Galerkin_Lift_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    upstream = load(UPSTREAM_PACKET)
    upstream_cert = load(UPSTREAM_CERT)
    rho = upstream["rho_E_candidate"]
    gates = rho["numeric_gates"]
    basis = upstream["B_N_scaffold"]
    straight = upstream["superset_mode"]["straight_path"]

    checks = {
        "F0_previous_import_matches": previous["status"] == PREVIOUS_STATUS
        and previous["next_required_artifact"] == "MTT_Selected_RouteC_NonIdentity_RhoE_and_BN_Construction_v1",
        "F1_upstream_packet_proved": upstream["status"] == UPSTREAM_STATUS
        and upstream["theorem"]["proved"] is True
        and upstream["closure_claimed"] is False
        and upstream["target_fitting_used"] is False
        and upstream["next_required_artifact"] == NEXT,
        "F2_certificate_agrees": upstream_cert["status"] == UPSTREAM_STATUS
        and upstream_cert["candidate_path"].endswith("selected_routec_nonidentity_rhoe_bn_construction.candidate.json"),
        "F3_rhoe_numeric_packet_passes": gates["passes_numeric_packet_gate"] is True
        and gates["nonidentity_norm"] > 0.1
        and gates["unitary_residual_max"] < 1e-10
        and gates["order3_residual_max"] < 1e-10
        and gates["projective_commutator_residual"] < 1e-10,
        "F4_selected_deck_shadow_used": gates["uses_only_selected_active_generators_g1_g2"] is True
        and gates["kernel_generators_identity"] is True
        and gates["active_deck_rank_over_F3"] == 2,
        "F5_source_promotion_open": rho["selected_by_mtt"] is False
        and upstream["what_remains_open"]["R2_source_promotion_for_rhoE"] is True,
        "F6_bn_scaffold_not_payload": basis["quotient_constraints_encoded"] is True
        and basis["passes_B_N_payload_gate"] is False
        and basis["smooth_scalar_basis_phi_m_emitted"] is False
        and basis["selected_D_E_action_emitted"] is False,
        "F7_missing_bn_fields_preserved": upstream["contract_comparison"]["still_missing_after_this_attempt"]["smooth_scalar_basis_functions_phi_m"] is True
        and upstream["contract_comparison"]["still_missing_after_this_attempt"]["selected_D_E_action_on_basis"] is True
        and upstream["contract_comparison"]["still_missing_after_this_attempt"]["gap_error_certificate"] is True,
        "F8_straight_path_partial": straight["nonidentity_projective_rhoE_packet_built"] is True
        and straight["BN_payload_built"] is False
        and straight["honest_replay_ready"] is False,
    }

    return {
        "packet": "RouteC_NonIdentity_RhoE_BN_Construction_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "upstream_candidate": str(UPSTREAM_PACKET),
            "upstream_certificate": str(UPSTREAM_CERT),
        },
        "theorem": {
            "name": "RouteCNonIdentityRhoEBNConstructionImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected F3^2 deck shadow admits a canonical non-identity "
                "three-dimensional Heisenberg/Weyl projective rho_E numerical "
                "packet.  This replaces identity smoke as the live rho_E "
                "candidate, but source promotion and smooth quotient-valid B_N "
                "with quadrature, D_E action, and gap/error bounds remain open."
            ),
        },
        "checks": checks,
        "upstream_nonidentity_rhoe_bn": upstream,
        "what_closes_now": upstream["what_closes_now"],
        "what_remains_open": upstream["what_remains_open"],
        "guardrails": {
            "claims_rhoE_source_promoted": False,
            "claims_BN_payload_built": False,
            "claims_smooth_scalar_basis_phi_m": False,
            "claims_selected_DE_action_on_basis": False,
            "claims_gap_error_certificate": False,
            "claims_honest_replay_ready": False,
            "claims_full_SM_or_no_knob_closure": False,
            "uses_observed_or_benchmark_inputs": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "RouteCNonIdentityRhoEBNConstructionImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "what_closes_now": packet["what_closes_now"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any]) -> str:
    return f"""# RouteC NonIdentity RhoE BN Construction Import v1

Status: `{cert["status"]}`.

The identity `rho_E` smoke branch has been replaced by a canonical non-identity
Heisenberg/Weyl projective `rho_E` numerical packet on the selected `F3^2` deck
shadow.  The packet passes the finite unitary, order-three, and projective
commutator gates.

This is not full promotion.  The packet is not yet theorem-derived from the
selected Strominger/HYM minimizer, and the `B_N` data is only a finite twisted
deck/fiber scaffold.  Smooth scalar Galerkin functions, metric quadrature,
selected `D_E` action, Gram/stiffness data, eigenpairs, and gap/error bounds
remain open.

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
