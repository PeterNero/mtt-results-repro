"""Audit Higgs external central-profile data or route-A formula row fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_higgsexternalprofiledata_or_routeaformularows"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CENTRAL_PROFILE = PACKET_DIR / "hybrid_external_central_profile_values.packet.json"
UNCERTAINTY_SIDECAR = PACKET_DIR / "diagonal_uncertainty_sidecar.packet.json"
ROUTE_A_STATUS = PACKET_DIR / "route_a_formula_rows_fill_status.packet.json"
PROMOTION = PACKET_DIR / "higgs_precision_promotion_after_central_values.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HiggsExternalProfileData_or_RouteAFormulaRows_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_HIGGSEXTERNALPROFILEDATA_OR_ROUTEAFORMULAROWS_BUILT_HYBRID_CENTRAL_VALUES_FULL_PROFILE_OPEN"
NEXT = "MTT_Selected_HiggsHomogeneousProfile_or_RouteAFormulaCovariance_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    central = load(CENTRAL_PROFILE)
    sidecar = load(UNCERTAINTY_SIDECAR)
    route_a = load(ROUTE_A_STATUS)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(central["filled_now"] is True, "central profile not filled")
    require(central["accepted_as_downstream_central_replay_seed"] is True, "central replay seed not accepted")
    require(central["accepted_as_single_correlated_profile"] is False, "single correlated profile overaccepted")
    require(central["full_covariance_or_nuisance_profile_supplied"] is False, "full covariance overclaimed")
    require(central["hybrid_source_warning"] is True, "hybrid warning missing")
    require(len(central["row_basis"]) == 10, "row basis mismatch")
    require(set(central["central_widths_GeV"]) == set(central["row_basis"]), "width basis mismatch")
    require(all(value > 0 for value in central["central_widths_GeV"].values()), "central width not positive")
    require(abs(central["central_widths_GeV"]["H_to_bb"] - 0.002346) < 1e-15, "bb width mismatch")
    require(abs(central["central_widths_GeV"]["H_to_ss"] - 8.62512e-7) < 1e-18, "ss width mismatch")
    require(0.0005 < central["documented_residual_branching_ratio"] < 0.0006, "documented residual mismatch")
    require(central["guards"]["used_to_select_source"] is False, "source selector guard failed")
    require(central["guards"]["benchmark_ratio_used_as_correction"] is False, "benchmark ratio guard failed")

    require(sidecar["is_symmetric"] is True, "sidecar symmetry missing")
    require(sidecar["is_psd_by_diagonal_nonnegative"] is True, "sidecar PSD guard missing")
    require(sidecar["is_full_correlated_profile"] is False, "sidecar overpromoted to full profile")
    require(len(sidecar["covariance_matrix_GeV2"]) == 10, "covariance row count mismatch")
    require(all(len(row) == 10 for row in sidecar["covariance_matrix_GeV2"]), "covariance col count mismatch")
    require(all(sidecar["covariance_matrix_GeV2"][i][i] > 0 for i in range(10)), "diagonal variance missing")
    require(all(
        sidecar["covariance_matrix_GeV2"][i][j] == 0.0
        for i in range(10)
        for j in range(10)
        if i != j
    ), "sidecar should be diagonal")

    require(route_a["summary"]["row_count"] == 10, "route A row count mismatch")
    require(route_a["summary"]["route_A_formula_rows_filled"] == 0, "route A formulas overfilled")
    require(route_a["summary"]["external_central_values_filled_for_rows"] == 10, "external central row fill missing")
    require(route_a["summary"]["accepted_route_A_formula_rows"] == 0, "route A formulas overaccepted")
    require(all(row["filled_by_external_central_profile"] is True for row in route_a["rows"]), "external central row missing")
    require(all(row["filled_by_route_A_formula"] is False for row in route_a["rows"]), "route A formula overfilled")

    require(promotion["external_profile_packet_filled"] is True, "profile packet not filled")
    require(promotion["accepted_as_downstream_central_replay_seed"] is True, "central replay promotion missing")
    require(promotion["accepted_as_single_correlated_profile"] is False, "single profile overaccepted")
    require(promotion["route_A_formula_values_filled"] == 0, "route A values overfilled")
    require(promotion["central_total_width_value_filled"] is True, "total width central value missing")
    require(promotion["central_branching_ratio_values_filled"] is True, "BR central values missing")
    require(promotion["full_correlated_profile_semantics_closed"] is False, "correlated profile overclosed")
    require(promotion["precision_total_width_closed"] is False, "precision total overclosed")
    require(promotion["precision_branching_ratios_closed"] is False, "precision branching overclosed")
    require(len(promotion["why_not_full_promotion"]) == 4, "promotion caveats mismatch")

    require(data["closure_decision"]["central_values_filled"] is True, "candidate central values missing")
    require(data["closure_decision"]["accepted_as_single_correlated_profile"] is False, "candidate overaccepted")
    require(data["closure_decision"]["route_A_formula_values_filled"] == 0, "candidate route A overfilled")
    require(cert["next_required_artifact"] == NEXT, "next artifact mismatch")
    require("not promoted to a full precision-profile proof" in note, "note missing guard")

    for packet in [central, sidecar, route_a, promotion, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
