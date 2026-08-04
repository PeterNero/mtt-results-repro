"""Audit CONST-HIGGS-01 H7B1M C1-to-Huv projection route decision."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_higgs_01_h7b1m_c1_to_huv_projection_or_honest_huv_row_export"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
C1_TARGET_AUDIT = BASE / "c1_target_sector_support_audit.packet.json"
PROJECTION_DECISION = BASE / "c1_to_huv_projection_route_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1M_C1ToHuvProjectionRouteDecision_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1M_C1_TO_HUV_PROJECTION_TEST_BUILT_HSECTOR_EXTENSION_REQUIRED"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} closure overclaim")


def all_none(packet: dict[str, object], name: str) -> None:
    for key, value in packet.items():
        require(value is None, f"{name} emitted {key}")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    c1_audit = load(C1_TARGET_AUDIT)
    projection = load(PROJECTION_DECISION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("c1_audit", c1_audit),
        ("projection", projection),
        ("next_work", next_work),
        ("cert", cert),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["H7B1L_gate_imported"] is True, "H7B1L import")
    require(candidate["current_C1_target_sector_set"] == ["d", "e", "nuD", "u"], "sector set")
    require(candidate["current_C1_target_contains_H_sector"] is False, "candidate H sector")
    require(candidate["plain_C1_to_Huv_projection_route_passes"] is False, "plain route pass")
    require(candidate["plain_C1_to_Huv_projection_route_retired_current_target"] is True, "plain route retired")
    require(candidate["H_sector_dynamic_C1_extension_required"] is True, "extension required")
    require(candidate["honest_Huv_row_export_still_live"] is True, "honest rows live")
    for key in [
        "B_Huv_value_emitted",
        "M_source_value_emitted",
        "selected_offdiagonal_Omega_found",
        "selected_s_beta_value_found",
        "numeric_lambda_H_derived",
        "strict_no_knob_Higgs_closure",
    ]:
        require(candidate[key] is False, f"candidate overclosed {key}")
    require(candidate["new_Higgs_specific_parameters"] == 0, "candidate params")
    require(
        candidate["selected_next_artifact"] == "MTT_CONST_HIGGS_01_H7B1N_HSectorDynamicExtensionOrHonestHuvRows_v1",
        "candidate next",
    )

    require(c1_audit["status"] == "C1_TARGET_HAS_MATTER_SECTORS_NO_HUV_SECTOR", "c1 status")
    c1 = c1_audit["c1_response_target"]
    require(c1["sector_norm_sq_keys"] == ["d", "e", "nuD", "u"], "c1 keys")
    require(c1["sector_norm_sq"] == {"d": 6.0, "e": 6.0, "nuD": 6.0, "u": 6.0}, "c1 norms")
    require(c1["inferred_real_dimension"] == 72, "c1 dim")
    require(c1["contains_H_sector"] is False, "c1 H")
    require(c1["contains_Hu_sector"] is False, "c1 Hu")
    require(c1["contains_Hd_dagger_sector"] is False, "c1 Hd")
    require(c1["selected_A_selected_emitted"] is False, "c1 A")
    require(c1["selected_b_selected_emitted"] is False, "c1 b")
    require(c1["conditional_Gram_exact"] is True, "c1 Gram")
    huv = c1_audit["huv_required_target"]
    require(huv["ordered_basis"] == ["H_u", "H_d^dagger"], "Huv basis")
    require(huv["basis_labels_currently_emitted"] is False, "Huv labels")
    require(huv["matrix_values_currently_emitted"] is False, "Huv matrix")
    require(huv["basis_invariant_functor_proved_conditionally"] is True, "Huv functor")
    require(huv["conditional_values_open"] is True, "Huv values open")
    mismatch = c1_audit["target_mismatch_result"]
    require(mismatch["plain_C1_target_can_supply_Huv_projection_now"] is False, "mismatch route")

    require(projection["status"] == "PLAIN_C1_TO_HUV_PROJECTION_ROUTE_RETIRED_CURRENT_TARGET", "projection status")
    route = projection["route_A_plain_C1_projection"]
    require(route["tested"] is True, "route tested")
    require(route["passes"] is False, "route pass")
    require(route["retired_for_current_target"] is True, "route retired")
    require(len(route["why"]) == 4, "route reasons")
    require(projection["route_A_refined"]["label"] == "H-sector dynamic C1 extension", "route refined")
    require(projection["route_B_still_live"]["label"] == "honest source-owned Huv row export", "route B")
    all_none(projection["strict_outputs"], "strict output")
    require(projection["superset_strategy"]["combining_paths"] is True, "superset")

    require(next_work["status"] == "NEXT_WORKORDER_H7B1N_HSECTOR_DYNAMIC_EXTENSION_OR_HONEST_HUV_ROWS", "next status")
    require(next_work["primary_next"]["label"].endswith("H7B1N-HSECTOR-DYNAMIC-EXTENSION-OR-HONEST-HUV-ROWS"), "next label")
    require(len(next_work["two_legal_exits"]) == 2, "next exits")
    require(len(next_work["do_not_repeat"]) == 4, "next guardrails")

    require(cert["status"] == STATUS, "cert status")
    require(cert["current_C1_target_contains_H_sector"] is False, "cert H")
    require(cert["plain_C1_to_Huv_projection_route_passes"] is False, "cert pass")
    require(cert["plain_C1_to_Huv_projection_route_retired_current_target"] is True, "cert retired")
    require(cert["H_sector_dynamic_C1_extension_required"] is True, "cert extension")
    require(cert["honest_Huv_row_export_still_live"] is True, "cert honest")
    require(cert["new_Higgs_specific_parameters"] == 0, "cert params")

    require("current C1 target sectors                  d, e, nuD, u" in note, "note sectors")
    require("plain route retired for current target      True" in note, "note retired")
    require("H7B1N-HSECTOR-DYNAMIC-EXTENSION-OR-HONEST-HUV-ROWS" in note, "note next")

    print("CONST-HIGGS-01 H7B1M C1-to-Huv projection route audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
