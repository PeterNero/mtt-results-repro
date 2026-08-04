"""Audit the Route-C selected source-origin way-forward artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "routec_selected_source_origin_way_forward_certificate.json"
DATA = REPO / "candidate_data" / "routec_selected_source_origin_way_forward.candidate.json"
NOTE = REPO / "proof_corpus" / "MTT_RouteC_Selected_Source_Origin_Way_Forward_v1.md"
SCRIPT = REPO / "scripts" / "build_routec_selected_source_origin_way_forward.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    superset = data["superset_mode"]
    sources_present = all(row["present"] for row in data["source_status"].values())
    route_ids = [row["id"] for row in data["route_ranking"]]
    checks = [
        check("status", cert["status"] == "MTT_ROUTEC_SELECTED_SOURCE_ORIGIN_WAY_FORWARD_BUILT_SOURCE_LEMMA_OPEN", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("sources present", sources_present, data["source_status"]),
        check("superset classification", cert["superset_mode"] == "SUPERSET_CONVERGENCE_TO_SOURCE_ORIGIN_PROGRAM" and superset["classification"] == "SUPERSET_CONVERGENCE_TO_SOURCE_ORIGIN_PROGRAM", superset),
        check("straight external path rejected", superset["straight_path"]["succeeds"] is False and cert["what_closes"]["external_HYM_existence_not_enough_guardrail"] is True, superset["straight_path"]),
        check("Strominger corpus hits", all(data["corpus_hits"]["strominger_selection_paper"].values()), data["corpus_hits"]["strominger_selection_paper"]),
        check("flux corpus useful but incomplete", data["corpus_hits"]["flux_compactification_paper"]["monad"] is True and data["corpus_hits"]["flux_compactification_paper"]["HYM"] is True, data["corpus_hits"]["flux_compactification_paper"]),
        check("external sources recorded", {"Fu_Yau_2006", "Andreas_Garcia_Fernandez_2010", "Fino_Grantcharov_Vezzoni_2021"}.issubset(data["external_sources"].keys()), data["external_sources"]),
        check("primary route selected", data["route_ranking"][0]["id"] == "S3_GS_Strominger_selection_instantiation", data["route_ranking"][0]),
        check("repair routes ranked", "typed_monad_Appell_Humbert_source_augmentation" in route_ids and "twisted_Chan_Paton_projective_module" in route_ids, route_ids),
        check("next artifact same lemma", data["next_required_artifact"] == "MTT_RouteC_Selected_Source_Origin_Lemma_v1" and cert["next_required_artifact"] == "MTT_RouteC_Selected_Source_Origin_Lemma_v1", cert),
        check("acceptance tests written", len(data["recommended_next_artifact"]["acceptance_tests"]) >= 4, data["recommended_next_artifact"]),
        check("closure not claimed", cert["closure_claimed"] is False and cert["what_remains_open"]["RouteC_selected_source_origin_lemma"] is True, cert),
        check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert),
        check("note records route", "superset convergence" in note and "External HYM/Strominger" in note, NOTE),
    ]
    print("\nMTT Route-C selected source-origin way-forward audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
