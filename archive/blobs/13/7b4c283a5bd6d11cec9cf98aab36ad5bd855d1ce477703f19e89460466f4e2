"""Audit Higgs official-profile assessment or route-A replay differentiation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsofficialprofile_or_routeaformuladifferentiation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
OFFICIAL_ASSESSMENT = PACKET_DIR / "official_profile_import_assessment.packet.json"
REPLAY_JACOBIAN = PACKET_DIR / "total_width_and_branching_ratio_replay_jacobian.packet.json"
PROPAGATED = PACKET_DIR / "propagated_width_and_branching_covariance.packet.json"
ROUTE_A_STATUS = PACKET_DIR / "route_a_formula_differentiation_status.packet.json"
PROMOTION = PACKET_DIR / "higgs_precision_promotion_after_replay_differentiation.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsOfficialProfile_or_RouteAFormulaDifferentiation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSOFFICIALPROFILE_OR_ROUTEAFORMULADIFFERENTIATION_BUILT_REPLAY_JACOBIAN_FORMULA_DIFF_OPEN"
NEXT = "MTT_Selected_HiggsRouteAFormulaDerivativeEngines_or_OfficialLikelihoodImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    official = load(OFFICIAL_ASSESSMENT)
    jac = load(REPLAY_JACOBIAN)
    propagated = load(PROPAGATED)
    route_a = load(ROUTE_A_STATUS)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(official["official_full_profile_imported"] is False, "official profile overimported")
    require(official["official_likelihood_or_nuisance_profile_imported"] is False, "official likelihood overimported")
    require(official["accepted_official_profile"] is False, "official profile overaccepted")

    require(jac["accepted_as_replay_map_differentiation"] is True, "replay differentiation missing")
    require(jac["accepted_as_route_A_physics_formula_differentiation"] is False, "route A differentiation overclaimed")
    require(len(jac["input_width_basis"]) == 10, "input width basis mismatch")
    require(len(jac["output_observable_basis"]) == 11, "observable basis mismatch")
    require(all(value == 1.0 for value in jac["jacobian_rows"]["Gamma_total_tracked"]), "total-width Jacobian mismatch")
    require(abs(sum(jac["tracked_branching_ratios"].values()) - 1.0) < 1e-12, "tracked BRs do not sum to one")

    require(propagated["accepted_as_propagated_covariance_for_current_source_model"] is True, "propagated covariance not accepted")
    require(propagated["accepted_as_official_precision_covariance"] is False, "official precision covariance overaccepted")
    require(propagated["is_symmetric"] is True, "symmetry flag missing")
    require(propagated["psd_inherited_by_jacobian_congruence"] is True, "PSD inheritance missing")
    require(propagated["tracked_total_width_variance_GeV2"] > 0, "total variance missing")
    require(len(propagated["branching_ratio_covariance"]) == 10, "BR covariance row count mismatch")
    require(all(len(row) == 10 for row in propagated["branching_ratio_covariance"]), "BR covariance col count mismatch")
    require(any(
        abs(propagated["branching_ratio_covariance"][i][j]) > 0
        for i in range(10)
        for j in range(10)
        if i != j
    ), "BR covariance has no off-diagonal entries")

    require(route_a["replay_map_differentiated"] is True, "route A status replay flag missing")
    require(route_a["partial_width_formula_rows_differentiated"] == 0, "partial-width formulas over-differentiated")
    require(route_a["route_A_physics_formula_differentiation_closed"] is False, "route A formula differentiation overclosed")

    require(promotion["replay_map_differentiated"] is True, "promotion replay flag missing")
    require(promotion["propagated_covariance_built"] is True, "promotion covariance flag missing")
    require(promotion["accepted_as_current_source_model_observable_covariance"] is True, "current covariance not promoted")
    require(promotion["accepted_as_official_precision_profile"] is False, "official precision overpromoted")
    require(promotion["precision_total_width_closed"] is False, "precision total overclosed")
    require(promotion["precision_branching_ratios_closed"] is False, "precision BR overclosed")

    require(data["closure_decision"]["replay_map_differentiation_closed"] is True, "candidate replay closure missing")
    require(data["closure_decision"]["official_profile_imported"] is False, "candidate official overimported")
    require(data["closure_decision"]["route_A_physics_formula_differentiation_closed"] is False, "candidate route A overclosed")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("This closes replay-map differentiation only" in note, "note missing guard")

    for packet in [official, jac, propagated, route_a, promotion, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
