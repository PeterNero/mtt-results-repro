"""Audit published Higgs decay covariance import or route-A derivative status."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsrouteaformuladerivativeengines_or_officiallikelihoodimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ANCILLARY_PROFILE = PACKET_DIR / "published_ancillary_decay_correlation_profile.packet.json"
REPO_IMPORT = PACKET_DIR / "repo_basis_decay_covariance_import.packet.json"
ROUTE_A_STATUS = PACKET_DIR / "route_a_derivative_engines_status.packet.json"
PROMOTION = PACKET_DIR / "higgs_likelihood_import_promotion_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSROUTEAFORMULADERIVATIVEENGINES_OR_OFFICIALLIKELIHOODIMPORT_BUILT_PUBLISHED_DECAY_PROFILE_IMPORTED_OFFICIAL_LIKELIHOOD_OPEN"
NEXT = "MTT_Selected_HiggsImportedProfileReplay_or_OfficialLHCHXSWGLikelihood_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    ancillary = load(ANCILLARY_PROFILE)
    repo_import = load(REPO_IMPORT)
    route_a = load(ROUTE_A_STATUS)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(ancillary["accepted_as_published_external_decay_correlation_profile"] is True, "ancillary not accepted")
    require(ancillary["accepted_as_official_LHCHXSWG_likelihood"] is False, "ancillary overpromoted to official")
    require(ancillary["coverage"]["covers_repo_ten_decay_rows_after_mapping"] is True, "coverage missing")
    require(len(ancillary["source_decay_labels"]) == 10, "source decay label count mismatch")
    require(abs(ancillary["relative_uncertainties"]["bb"] - 0.0125266676) < 1e-12, "bb uncertainty mismatch")
    require(abs(ancillary["correlation_matrix"][0][1] - 0.996559302) < 1e-12, "WW-ZZ correlation mismatch")

    require(repo_import["covers_all_repo_rows"] is True, "repo row coverage missing")
    require(repo_import["accepted_as_external_full_decay_covariance_profile"] is True, "repo covariance import not accepted")
    require(repo_import["accepted_as_official_full_likelihood"] is False, "repo import overpromoted")
    require(repo_import["replaces_source_derived_covariance_model_for_replay"] is True, "replay replacement missing")
    require(repo_import["has_nontrivial_offdiagonal_correlations"] is True, "offdiagonal correlations missing")
    require(repo_import["repo_to_source_label_map"]["H_to_gamma_gamma"] == "gaga", "gamma mapping mismatch")
    require(len(repo_import["covariance_matrix_GeV2"]) == 10, "covariance row count mismatch")
    require(all(len(row) == 10 for row in repo_import["covariance_matrix_GeV2"]), "covariance col count mismatch")
    require(any(
        repo_import["covariance_matrix_GeV2"][i][j] < 0
        for i in range(10)
        for j in range(10)
        if i != j
    ), "negative anticorrelations missing")
    require(repo_import["guards"]["official_likelihood_claimed"] is False, "official likelihood guard failed")

    require(route_a["external_decay_covariance_profile_imported"] is True, "route A status missing external import")
    require(route_a["route_A_derivative_engines_built"] is False, "route A engines overbuilt")
    require(route_a["route_A_partial_width_formula_rows_differentiated"] == 0, "route A rows over-differentiated")

    require(promotion["published_external_decay_profile_imported"] is True, "promotion import missing")
    require(promotion["accepted_as_external_full_decay_covariance_profile"] is True, "promotion external profile missing")
    require(promotion["accepted_as_official_LHCHXSWG_likelihood"] is False, "promotion official overclaimed")
    require(promotion["route_A_derivative_engines_built"] is False, "promotion route A overbuilt")
    require(promotion["precision_total_width_closed"] is False, "precision total overclosed")
    require(promotion["precision_branching_ratios_closed"] is False, "precision branching overclosed")

    require(data["closure_decision"]["external_full_decay_covariance_profile_imported"] is True, "candidate import missing")
    require(data["closure_decision"]["accepted_as_official_LHCHXSWG_likelihood"] is False, "candidate official overclaimed")
    require(data["closure_decision"]["route_A_derivative_engines_built"] is False, "candidate route A overbuilt")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not promoted to an official LHCHXSWG likelihood/profile" in note, "note missing guard")

    for packet in [ancillary, repo_import, route_a, promotion, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
