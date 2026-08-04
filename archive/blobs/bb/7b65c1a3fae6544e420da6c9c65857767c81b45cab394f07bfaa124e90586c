from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "candidate_data" / "selected_neutralnilboundarymassfunctional" / "neutral_nil_boundary_mass_functional.packet.json"
CERT = ROOT / "certificates" / "selected_neutralnilboundarymassfunctional_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    action = packet["selected_static_action"]
    functional = packet["minimal_trace_mass_functional"]
    candidates = packet["ordering_candidates_postcheck_only"]

    require(action["all_six_SM_slot_arrows"] is True, "SM-slot source missing")
    require(action["selected_Dirac_channel"] is True, "Dirac channel missing")
    require(action["accepted_Majorana_mass_operator_rows"] == 0, "unexpected Majorana row")
    require(action["fundamental_Majorana_extension_excluded"] is False, "Majorana extension overexcluded")
    require(packet["neutral_character_cut"]["solutions"] == [0, 672], "neutral character cut changed")
    require(functional["mathematical_theorem_proved"] is True, "minimal trace theorem missing")
    require(functional["selected_MTT_neutral_source_principle_proved"] is False, "source premise overclaimed")

    for ordering in ["normal_ordering", "inverted_ordering"]:
        row = candidates[ordering]
        require(row["lightest_mass_eV"] == 0.0, f"{ordering} lightest mass changed")
        require(min(row["masses_eV"]) == 0.0, f"{ordering} positivity boundary missing")
        require(math.isclose(sum(row["masses_eV"]), row["sum_masses_eV"], rel_tol=0.0, abs_tol=1e-15), f"{ordering} sum mismatch")
    require(0.058 < candidates["normal_ordering"]["sum_masses_eV"] < 0.060, "NO postcheck changed")
    require(0.100 < candidates["inverted_ordering"]["sum_masses_eV"] < 0.102, "IO postcheck changed")
    require(candidates["ordering_selected_by_MTT"] is False, "ordering overclaimed")
    require(len(packet["U5_reduced_source_clauses"]) == 3, "U5 cutset count changed")
    require(packet["U5_absolute_mass_functional_formula_closed"] is True, "absolute mass formula missing")
    require(packet["U5_absolute_mass_source_promoted"] is False, "absolute mass source overpromoted")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(cert["remaining_source_clause_count"] == 3, "certificate cutset changed")

    print(
        json.dumps(
            {
                "minimal_trace_theorem": cert["minimal_trace_boundary_theorem_proved"],
                "conditional_lightest_mass_eV": cert["conditional_lightest_mass_eV"],
                "NO_sum_postcheck_eV": cert["normal_ordering_sum_postcheck_eV"],
                "IO_sum_postcheck_eV": cert["inverted_ordering_sum_postcheck_eV"],
                "remaining_source_clauses": cert["remaining_source_clause_count"],
            },
            indent=2,
        )
    )
    print("selected neutral nil-boundary mass functional audit passed")


if __name__ == "__main__":
    main()
