"""Audit the finite emission morphism Phi_fin attempt artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "finite_emission_morphism_phifin.candidate.json"
CERT = REPO / "certificates" / "finite_emission_morphism_phifin_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Finite_Emission_Morphism_Phi_fin_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    schema = data["phifin_schema"]
    obstruction = data["obstruction"]
    flags = schema["selected_flags"]

    checks = [
        check("status", data["status"] == "MTT_FINITE_EMISSION_MORPHISM_PHIFIN_SCHEMA_BUILT_SELECTED_VALUES_OPEN", data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check("superset classification", data["superset_mode"]["classification"] == "SUPERSET_REPAIR_SCHEMA_NOT_SELECTED_VALUES", data["superset_mode"]),
        check("no target fitting", data["target_fitting_used"] is False and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False, data["superset_mode"]["diagnostic_backfit_only"]),
        check("shape gates pass", all(schema["shape_gates"].values()) is True and cert["what_closes"]["Phi_fin_codomain_schema_built"] is True, schema["shape_gates"]),
        check("sectors complete", schema["sectors"] == ["H", "L", "N", "Q", "d", "e", "u"], schema["sectors"]),
        check("selected flags fail honestly", any(value is False for value in flags.values()) and obstruction["selected_payload_closed"] is False, flags),
        check("identity rhoE rejected", obstruction["identity_rhoE_smoke"] is True and cert["what_closes"]["identity_rhoE_smoke_rejected"] is True, obstruction),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Selected_NonIdentity_RhoE_Transition_Source_v1" and cert["next_required_artifact"] == "MTT_Selected_NonIdentity_RhoE_Transition_Source_v1", cert),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["Phi_fin_selected_payload"] is True, cert),
        check("note records smoke rejection", "identity smoke" in note and "cannot be promoted" in note, NOTE),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT finite emission morphism Phi_fin audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
