"""Audit the selected visible Chern-Weil/operator-source reduction artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_visible_chern_weil_operator_source.candidate.json"
CERT = REPO / "certificates" / "selected_visible_chern_weil_operator_source_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Visible_Chern_Weil_Operator_Source_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    mode = data["superset_mode"]
    closed = data["closed_support"]
    retired = data["retired_or_demoted"]
    open_gates = data["open_gates"]
    packet = data["selected_source_packet"]

    checks = [
        check("status", data["status"] == "MTT_SELECTED_VISIBLE_CW_OPERATOR_SOURCE_REDUCED_TO_SAME_SOURCE_NONABELIAN_OR_ROUTEC_PACKET", data["status"]),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check("superset classification", mode["classification"] == "SUPERSET_CONVERGENCE_WITH_REPAIR", mode),
        check("straight path retired", mode["straight_path_result"]["classification"] == "STRAIGHT_PATH_RETIRED" and mode["straight_path_result"]["succeeds"] is False, mode["straight_path_result"]),
        check("primary branch locked", mode["primary_path"]["candidate_id"] == "rank2_non_split_extension_preferred_L_1_-2_0" and mode["primary_path"]["classification"] == "SUPERSET_CONVERGENCE_PRIMARY", mode["primary_path"]),
        check("route c preserved", mode["parallel_repair_path"]["classification"] == "SUPERSET_REPAIR_PARALLEL" and mode["parallel_repair_path"]["succeeds"] is False, mode["parallel_repair_path"]),
        check("diagnostic not proof", mode["diagnostic_backfit_only"]["used_as_proof"] is False and data["target_fitting_used"] is False, mode["diagnostic_backfit_only"]),
        check("closed support imported", all(closed.values()), closed),
        check("split source retired", retired["split_line_or_diagonal_cartan_HYM_final_source"] is True and retired["abelian_row_retained_only_as_chern_bianchi_support"] is True, retired),
        check("patchwork rejected", retired["patchwork_constituent_proof_rejected"] is True, retired),
        check("source not overclaimed", open_gates["selected_visible_operator_source_closed"] is False and cert["closure_claimed"] is False, open_gates),
        check("cut set retained", open_gates["same_source_cut_set"]["selected_D_E_dotD_Riesz_Green"] is True and open_gates["same_source_cut_set"]["Chern_Weil_row_derived_from_selected_source"] is True, open_gates["same_source_cut_set"]),
        check("packet fields include same-source operators", "same_source_D_E_operator_block" in packet["visible_required_fields"] and "Riesz_projector_and_reduced_Green_packet" in packet["visible_required_fields"], packet["visible_required_fields"]),
        check("acceptance tests include h1 ext and residual", any("H^1" in item for item in packet["acceptance_tests"]) and any("Route-C" in item for item in packet["acceptance_tests"]), packet["acceptance_tests"]),
        check("next artifact", cert["primary_next_artifact"] == "MTT_Selected_NonSplit_Rank2_or_RouteC_SameSource_Packet_v1", cert),
        check("note records path classes", "Straight path" in note and "Superset convergence" in note and "Superset repair" in note, NOTE),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected visible Chern-Weil/operator-source reduction audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
