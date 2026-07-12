"""Audit the selected non-identity rho_E transition-source gate artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_nonidentity_rhoe_transition_source.candidate.json"
CERT = REPO / "certificates" / "selected_nonidentity_rhoe_transition_source_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_NonIdentity_RhoE_Transition_Source_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    gates = data["gate_results"]
    projective = data["projective_candidate"]
    blockers = data["promotion_blockers"]

    checks = [
        check("status", data["status"] == "MTT_SELECTED_NONIDENTITY_RHOE_SOURCE_REDUCED_TO_PROJECTIVE_GERBE_PROMOTION", data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check("superset repair", data["superset_mode"]["classification"] == "SUPERSET_REPAIR_TO_PROJECTIVE_TWISTED_RHOE", data["superset_mode"]),
        check("no target fitting", data["target_fitting_used"] is False and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False, data["superset_mode"]["diagnostic_backfit_only"]),
        check("ordinary route retired", gates["ordinary_rhoE_route_retired"] is True and cert["what_closes"]["ordinary_nonidentity_rhoE_route_retired"] is True, data["ordinary_no_go"]),
        check("projective candidate locked", gates["projective_twisted_rhoE_candidate_locked"] is True and projective["finite_model"]["matches_qutrit_projective_cocycle"] is True, projective),
        check("selection not closed", gates["selected_projective_rhoE_source_closed"] is False and cert["closure_claimed"] is False, blockers),
        check("promotion blockers honest", blockers["selected_projective_twist_source_found"] is False and blockers["selected_D_E_dotD_constructed"] is False, blockers),
        check("next packet selected", data["next_required_artifact"] == "MTT_Projective_Gerbe_RhoE_Source_Promotion_v1" and cert["next_required_artifact"] == "MTT_Projective_Gerbe_RhoE_Source_Promotion_v1", cert),
        check("open items retained", cert["what_remains_open"]["selected_projective_gerbe_rhoE_source"] is True and cert["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True, cert),
        check("note records retirement and projective route", "ordinary non-identity `rho_E` route is retired" in note and "projective/twisted `rho_E` source" in note, NOTE),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected non-identity rho_E transition-source audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
