"""Audit b/c/tau formula import or R_theta mass-scheme derivation artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SOURCE_FAMILIES = PACKET_DIR / "external_bct_formula_source_families.packet.json"
ROW_ATTEMPT = PACKET_DIR / "bottom_charm_tau_formula_row_acceptance_attempt.packet.json"
RTHETA_GAP = PACKET_DIR / "rtheta_bct_mass_scheme_derivation_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bct_formula_source_import.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_BottomCharmTauFormulaImport_or_RThetaMassSchemeDerivation_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_BOTTOMCHARMTAUFORMULAIMPORT_OR_RTHETAMASSSCHEMEDERIVATION_"
    "BUILT_FORMULA_FAMILIES_IMPORTED_ROWS_OPEN"
)
NEXT = "MTT_Selected_BottomCharmTauRunDecReplay_or_RThetaMassSchemeRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    source_families = load(SOURCE_FAMILIES)
    row_attempt = load(ROW_ATTEMPT)
    rtheta_gap = load(RTHETA_GAP)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    for key in [
        "closure_claimed",
        "unpatched_theorem_closure_claimed",
        "observed_data_used_as_selector",
        "target_fitting_used",
    ]:
        require(data[key] is False, f"candidate guardrail overclaimed: {key}")
        require(cert[key] is False, f"certificate guardrail overclaimed: {key}")

    require(
        source_families["status"] == "BOTTOM_CHARM_TAU_EXTERNAL_FORMULA_SOURCE_FAMILIES_IMPORTED",
        "source-family status mismatch",
    )
    require(source_families["accepted_formula_family_count"] == 6, "wrong source-family count")
    require(
        source_families["bottom_charm_quark_running_formula_family_closed"] is True,
        "quark running formula family not closed",
    )
    require(source_families["tau_running_table_formula_family_closed"] is True, "tau family not closed")
    require(source_families["machine_replay_or_table_values_imported"] is False, "values imported too early")
    require(source_families["accepted_map_rows_emitted"] is False, "map rows emitted too early")
    require(source_families["closure_claimed"] is True, "source family should close locally")
    expected_urls = {
        "https://arxiv.org/abs/hep-ph/0004189",
        "https://arxiv.org/abs/1201.6149",
        "https://arxiv.org/abs/1703.03751",
        "https://pdg.lbl.gov/2023/reviews/rpp2023-rev-quark-masses.pdf",
        "https://arxiv.org/abs/2009.04851",
        "https://arxiv.org/abs/0712.1419",
    }
    require({source["url"] for source in source_families["formula_sources"]} == expected_urls, "source URLs changed")

    require(
        row_attempt["status"] == "FORMULA_FAMILIES_AVAILABLE_NO_BCT_ROWS_ACCEPTED",
        "row-attempt status mismatch",
    )
    require(len(row_attempt["row_requirements"]) == 3, "wrong b/c/tau requirement count")
    require(row_attempt["accepted_bottom_charm_tau_map_rows"] == [], "b/c/tau rows overaccepted")
    require(row_attempt["accepted_bottom_charm_tau_map_row_count"] == 0, "wrong accepted b/c/tau count")
    require(row_attempt["formula_family_import_closes_rows"] is False, "formula family closes rows")
    require(row_attempt["residual_rows_are_source_rows"] is False, "residual rows treated as source rows")
    require(row_attempt["closure_claimed"] is False, "row attempt overclosed")
    for row in row_attempt["row_requirements"]:
        require(row["formula_family_available"] is True, f"formula family missing: {row['id']}")
        require(row["native_residual_inventory_available"] is True, f"native residual missing: {row['id']}")
        require(row["versioned_replay_values_imported"] is False, f"row replayed too early: {row['id']}")
        require(row["accepted_as_external_map_row"] is False, f"row overaccepted external: {row['id']}")
        require(row["accepted_as_Rtheta_source_row"] is False, f"row overaccepted Rtheta: {row['id']}")

    require(
        rtheta_gap["status"] == "FORMULA_FAMILIES_IMPORTED_SELECTED_RTHETA_DERIVATION_OPEN",
        "Rtheta gap status mismatch",
    )
    require(rtheta_gap["precoefficient_skeletons_present"] is True, "Rtheta skeleton missing")
    require(rtheta_gap["selected_Rtheta_mass_scheme_derivation_closed"] is False, "Rtheta overclosed")
    require(
        rtheta_gap["minimal_internal_missing_object"] == "SelectedRouteCStromingerGalerkinResidualSolve",
        "wrong Rtheta missing object",
    )
    require(rtheta_gap["formula_families_may_validate_Rtheta"] is True, "Rtheta validation relation missing")
    require(rtheta_gap["formula_families_select_Rtheta"] is False, "formula families select Rtheta")
    require(rtheta_gap["closure_claimed"] is False, "Rtheta gap overclosed")

    require(cutset["status"] == "NEXT_ATTACK_RUNDEC_REPLAY_OR_RTHETA_MASS_SCHEME_ROWS", "cutset status mismatch")
    for key in [
        "external_formula_source_families_imported",
        "bottom_charm_quark_running_formula_family",
        "tau_running_table_formula_family",
        "formula_import_nonselector_gap",
    ]:
        require(cutset["closed_now"][key] is True, f"cutset closed flag missing: {key}")
    for key in [
        "versioned_RunDec_or_table_replay_values",
        "accepted_bottom_charm_tau_map_rows",
        "selected_Rtheta_mass_scheme_derivation",
        "W_Z_H_electroweak_matching_rows",
        "full_covariance_profile_likelihood",
        "true_SM_equivalence",
        "full_no_knob",
    ]:
        require(cutset["still_open"][key] is True, f"cutset open flag missing: {key}")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    closure = data["closure_decision"]
    require(closure["external_formula_source_families_imported"] is True, "source import not recorded")
    require(closure["bottom_charm_quark_running_formula_family_closed"] is True, "quark family not recorded")
    require(closure["tau_running_table_formula_family_closed"] is True, "tau family not recorded")
    require(closure["accepted_bottom_charm_tau_map_row_count"] == 0, "candidate overcounts b/c/tau rows")
    for key in [
        "accepted_bottom_charm_tau_map_rows_closed",
        "versioned_RunDec_or_table_replay_values_closed",
        "selected_Rtheta_mass_scheme_derivation_closed",
        "W_Z_H_electroweak_matching_rows_closed",
        "full_covariance_profile_likelihood_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(closure[key] is False, f"candidate overclosed: {key}")

    require("external formula source families imported : true" in note, "note missing source import line")
    require("accepted b/c/tau map rows                 : 0" in note, "note missing row count")
    require(NEXT in note, "note missing next artifact")
    print(json.dumps({"audit": SLUG, "status": "ok"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
