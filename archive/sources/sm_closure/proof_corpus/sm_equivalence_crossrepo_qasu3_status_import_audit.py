"""Audit cross-repo Qa/SU3 status import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_crossrepo_qasu3_status_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_CrossRepo_QaSU3_Status_Import_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_crossrepo_qasu3_status_import.py"

STATUS = "MTT_SM_EQUIVALENCE_CROSSREPO_QASU3_STATUS_IMPORTED_NO_FINAL_PACKET_FOUND"
NEXT = "MTT_SM_Equivalence_SelectedQaSU3Packet_or_RGTransport_ValueFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(len(data["repos_scanned"]) == 4, "repo scan count mismatch")
    require(any(scan["repo"] == "mtt-qa-su3-packet-proof" and scan["exists"] for scan in data["repos_scanned"]), "Qa/SU3 repo not scanned")
    require(any(scan["repo"] == "mtt-nonsm-constants-no-knob" and scan["exists"] for scan in data["repos_scanned"]), "non-SM constants repo not scanned")
    require(sum(scan["json_files_scanned"] for scan in data["repos_scanned"]) > 0, "no JSON files scanned")

    require(data["any_promotable_qasu3_packet_found"] is False, "unexpected promotable Qa/SU3 closure found")
    require(data["promotable_qasu3_hits"] == [], "promotable hit list should be empty")
    require(data["explicit_open_flag_count"] > 0, "open flags should be visible")
    require(data["interpretation"]["support_layers_are_not_discarded"] is True, "support layer import lost")
    require(data["interpretation"]["support_layers_promote_final_packet"] is False, "support layers overpromoted")

    policy = data["sm_parity_evaluation_policy"]
    require(policy["this_repo_view"] == "SM_PARITY_FIRST", "this repo lens mismatch")
    require(policy["sibling_repo_default_view"] == "NO_KNOB_RESEARCH", "sibling repo lens mismatch")
    require("do not need to derive all numerical constants" in policy["relevance_rule"], "parity relevance rule missing")
    require(len(policy["qa_su3_parity_acceptance_requires"]) == 4, "parity acceptance list incomplete")
    require(len(policy["qa_su3_no_knob_acceptance_would_also_require"]) == 3, "no-knob distinction incomplete")
    require("future typed selected packet can close the parity gate" in policy["current_decision"], "future parity closure rule missing")

    reusable = data["reusable_cross_repo_inputs"]
    require(len(reusable) >= 6, "too few reusable inputs")
    require(all(row["exists"] for row in reusable[:6]), "core reusable inputs missing")
    require(any("Typed_Monad" in row["path"] for row in reusable), "typed monad input missing")
    require(any("a01_de_operator_exit_gate" in row["path"] for row in reusable), "A01 gate input missing")

    superset = data["superset_strategy_position"]
    require(superset["using_straight_path"] is False, "should be superset import")
    require(superset["using_superset_paths"] is True, "superset paths not marked")
    require(superset["measured_constants_used_as_selector"] is False, "measured selector misuse")
    require(superset["locked_target"] == "selected Qa/SU3 color/operator packet, then selected SM packet certificate", "locked target mismatch")

    closes = data["what_closes_now"]
    for key in [
        "cross_repo_scan_performed",
        "no_missed_promotable_qasu3_closure_found",
        "sm_parity_lens_for_QaSU3_installed",
        "support_layers_imported_as_reusable_inputs",
        "QaSU3_final_packet_remains_active_blocker",
        "overclaim_guardrail_installed",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_QaSU3_color_operator_packet",
        "selected_D_E_rho_E_operator_values",
        "typed_monad_or_section_ring_operator_transfer_values",
        "same_branch_period_selector_or_finite_quotient",
        "selected_SM_packet_final_certificate",
        "common_scale_Yukawa_Higgs_transport",
        "true_SM_equivalence_closure",
    ]:
        require(remains[key] is True, f"remaining gate missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["source_boundary_preserved"] is True, "source boundary not preserved")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("This is a superset move" in note, "note missing superset explanation")
    require("This repo evaluates Qa/SU3 in the SM-parity view" in note, "note missing SM-parity lens")
    require("promotable true hits: 0" in note, "note missing zero-hit result")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
