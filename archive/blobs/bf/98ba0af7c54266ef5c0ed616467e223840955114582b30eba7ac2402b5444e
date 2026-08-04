"""Audit Higgs homogeneous-profile assessment or route-A covariance model."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgshomogeneousprofile_or_routeaformulacovariance"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
HOMOGENEOUS_ASSESSMENT = PACKET_DIR / "homogeneous_profile_route_assessment.packet.json"
CORRELATED_MODEL = PACKET_DIR / "source_derived_correlated_covariance_model.packet.json"
ROUTE_A_STATUS = PACKET_DIR / "route_a_formula_covariance_status.packet.json"
PROMOTION = PACKET_DIR / "higgs_precision_promotion_after_covariance_model.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsHomogeneousProfile_or_RouteAFormulaCovariance_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSHOMOGENEOUSPROFILE_OR_ROUTEAFORMULACOVARIANCE_BUILT_CORRELATED_COVARIANCE_MODEL_FULL_PROFILE_OPEN"
NEXT = "MTT_Selected_HiggsOfficialProfile_or_RouteAFormulaDifferentiation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    homogeneous = load(HOMOGENEOUS_ASSESSMENT)
    model = load(CORRELATED_MODEL)
    route_a = load(ROUTE_A_STATUS)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(homogeneous["single_source_profile_found"] is False, "homogeneous profile overfound")
    require(homogeneous["full_covariance_or_nuisance_profile_found"] is False, "full covariance overfound")
    require(homogeneous["accepted_as_homogeneous_correlated_profile"] is False, "homogeneous profile overaccepted")
    require(len(homogeneous["primary_source_rows_covered"]) == 9, "primary source coverage mismatch")
    require(homogeneous["separate_source_rows_required"] == ["H_to_ss"], "separate strange row not recorded")

    require(model["status"] == "SOURCE_DERIVED_CORRELATED_COVARIANCE_MODEL_BUILT_NOT_OFFICIAL_PROFILE", "model status mismatch")
    require(model["row_basis"][0] == "H_to_bb" and len(model["row_basis"]) == 10, "model row basis mismatch")
    require(model["nuisance_basis"] == ["total_width_norm", "branching_ratio_parametric", "branching_ratio_theory"], "nuisance basis mismatch")
    require(model["is_symmetric"] is True, "symmetry flag missing")
    require(model["is_psd_by_gram_construction"] is True, "PSD Gram flag missing")
    require(model["rank_bound"] == 3, "rank bound mismatch")
    require(model["improves_over_diagonal_sidecar"] is True, "diagonal upgrade missing")
    require(model["accepted_as_source_derived_covariance_model"] is True, "source model not accepted")
    require(model["accepted_as_official_full_correlated_profile"] is False, "official profile overaccepted")
    require(model["accepted_as_route_A_formula_covariance"] is False, "route A covariance overaccepted")
    require(model["guardrails"]["aggregate_uncertainty_model_not_official_likelihood"] is True, "official-likelihood guard missing")
    require(model["guardrails"]["route_A_formula_rows_not_computed"] is True, "route A guard missing")
    covariance = model["covariance_matrix_GeV2"]
    require(len(covariance) == 10 and all(len(row) == 10 for row in covariance), "covariance shape mismatch")
    require(all(covariance[i][i] > 0 for i in range(10)), "positive diagonal variance missing")
    require(any(covariance[i][j] > 0 for i in range(10) for j in range(10) if i != j), "correlations missing")
    require(all(abs(covariance[i][j] - covariance[j][i]) < 1e-30 for i in range(10) for j in range(10)), "covariance not symmetric")
    require(model["relative_response_matrix"]["H_to_bb"]["total_width_norm"] == 0.0387, "width response mismatch")

    require(route_a["route_A_formula_rows_computed"] == 0, "route A rows overcomputed")
    require(route_a["route_A_formula_covariance_contributions_computed"] == 0, "route A covariance overcomputed")
    require(route_a["source_derived_covariance_model_available"] is True, "source model availability missing")
    require(route_a["source_model_can_replace_route_A_formula_covariance"] is False, "source model overpromoted")

    require(promotion["source_derived_correlated_covariance_model_built"] is True, "promotion model missing")
    require(promotion["diagonal_sidecar_upgraded_to_correlated_model"] is True, "diagonal upgrade not promoted")
    require(promotion["homogeneous_single_source_profile_closed"] is False, "homogeneous overclosed")
    require(promotion["official_full_covariance_or_nuisance_profile_closed"] is False, "official covariance overclosed")
    require(promotion["route_A_formula_covariance_closed"] is False, "route A covariance overclosed")
    require(promotion["precision_total_width_closed"] is False, "precision total overclosed")
    require(promotion["precision_branching_ratios_closed"] is False, "precision branching overclosed")

    require(data["closure_decision"]["correlated_covariance_model_built"] is True, "candidate covariance model missing")
    require(data["closure_decision"]["accepted_as_official_full_correlated_profile"] is False, "candidate official profile overaccepted")
    require(data["closure_decision"]["route_A_formula_covariance_closed"] is False, "candidate route A overclosed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not an official full LHCHXSWG nuisance profile" in note, "note missing guard")

    for packet in [homogeneous, model, route_a, promotion, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
