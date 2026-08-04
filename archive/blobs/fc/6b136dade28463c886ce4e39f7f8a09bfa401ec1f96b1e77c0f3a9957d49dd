"""Audit the Route-C selected source-origin lemma attempt artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "routec_selected_source_origin_lemma.candidate.json"
CERT = REPO / "certificates" / "routec_selected_source_origin_lemma_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_RouteC_Selected_Source_Origin_Lemma_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    gates = data["gate_matrix"]
    lemma = data["lemma_evaluation"]
    morphism = data["finite_emission_morphism_contract"]

    checks = [
        check("status", data["status"] == "MTT_ROUTEC_SELECTED_SOURCE_ORIGIN_LEMMA_REDUCED_TO_FINITE_EMISSION_MORPHISM", data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check("superset classification", data["superset_mode"]["classification"] == "SUPERSET_CONVERGENCE_PARTIAL_PROOF", data["superset_mode"]),
        check("no diagnostic fitting", data["target_fitting_used"] is False and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False, data["superset_mode"]["diagnostic_backfit_only"]),
        check("fixed sector gate passes", gates["G1_fixed_topological_sector_named"]["passes"] is True, gates["G1_fixed_topological_sector_named"]),
        check("Strominger selection gate passes", gates["G2_MTT_Strominger_selection_available"]["passes"] is True, gates["G2_MTT_Strominger_selection_available"]),
        check("same-source convergence gate passes", gates["G3_same_source_support_converges"]["passes"] is True, gates["G3_same_source_support_converges"]),
        check("finite morphism still open", gates["G4_minimizer_to_finite_packet_morphism"]["passes"] is False and cert["what_remains_open"]["FiniteEmissionMorphism_Phi_fin"] is True, gates["G4_minimizer_to_finite_packet_morphism"]),
        check("operator payload still open", gates["G5_operator_payload_emitted"]["passes"] is False and cert["what_remains_open"]["selected_D_E_dotD_Riesz_Green"] is True, gates["G5_operator_payload_emitted"]),
        check("full lemma not claimed", lemma["fully_proved"] is False and cert["closure_claimed"] is False, lemma),
        check("next artifact selected", data["next_required_artifact"] == "MTT_Finite_Emission_Morphism_Phi_fin_v1" and cert["next_required_artifact"] == "MTT_Finite_Emission_Morphism_Phi_fin_v1", cert),
        check("morphism contract complete", all(key in morphism for key in ["domain", "codomain", "must_commute_with", "acceptance_tests"]) and len(morphism["must_commute_with"]) >= 5, morphism),
        check("note records reduction", "FiniteEmissionMorphism_Phi_fin" in note and "not closed yet" in note, NOTE),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT Route-C selected source-origin lemma audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
