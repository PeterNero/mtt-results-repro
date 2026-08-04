from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralfinitegammarowsoractioncostsource"
PACKET = ROOT / "candidate_data" / SLUG / "neutral_finite_gamma_channel_rows.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralFiniteGammaRowsOrActionCostSource_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_FINITE_GAMMA_CHANNEL_ROWS_CLOSED_ACTION_WEIGHTS_OPEN"
NEXT = "MTT_Selected_NeutralActionCostPrefactorOrDiracMajoranaCompletion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(PACKET)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(packet == candidate, "candidate/packet mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(packet["target_fitting_used"] is False, "target fitting used")
    require(packet["theorem"]["proved"] is True, "channel theorem not proved")

    finite = packet["finite_operator"]
    expected = [[1.0, 1.0, 0.0], [0.0, 1.0, 1.0], [1.0, 0.0, 1.0]]
    require(finite["Gamma_nu_channel_matrix_I3_plus_X3"] == expected, "I+X matrix changed")
    require(finite["X3_cubed_equals_I3"] is True, "X order changed")
    require(finite["exact_selected_packet_match"] is True, "selected packet mismatch")
    require(finite["operator_rank"] == 3 and finite["determinant"] == 2.0, "operator invariant changed")
    require(finite["active_cell_count"] == 6 and finite["zero_cell_count"] == 3, "support count changed")

    rows = packet["Gamma_nu_finite_channel_rows"]
    require(len(rows) == packet["finite_Gamma_nu_row_count"] == 9, "row count changed")
    require(packet["finite_Gamma_nu_rows_selected"] == 9, "selected row count changed")
    require({row["cell"] for row in rows} == {f"Gamma_nu[{i},{j}]" for i in range(3) for j in range(3)}, "cell IDs changed")
    for row in rows:
        require(row["selected_emitted"] is True and row["theorem_derived"] is True, f"unselected row {row['cell']}")
        require(row["physical_amplitude_emitted"] is False, f"physical amplitude overclosed {row['cell']}")
        require(row["action_cost_S_gamma_emitted"] is False, f"action cost overclosed {row['cell']}")
        require(row["prefactor_A_gamma_emitted"] is False, f"prefactor overclosed {row['cell']}")
        require(row["retarded_sign_emitted"] is False, f"retarded sign overclosed {row['cell']}")

    closes = packet["what_closes_here"]
    require(closes["finite_Gamma_nu_ij_channel_sets"] is True, "finite channel sets open")
    require(closes["nine_dimensionless_channel_multiplicity_rows"] is True, "multiplicity rows open")
    require(closes["finite_channel_exactness"] is True, "finite exactness open")
    for key in [
        "neutral_action_cost_rows_S_gamma",
        "neutral_prefactors_A_gamma",
        "neutral_retarded_sign_rows",
        "physical_Gamma_nu_amplitudes",
        "Dirac_only_action_completeness",
    ]:
        require(closes[key] is False, f"overclosed: {key}")

    require(packet["readiness_subfields_closed"] == 8 and packet["readiness_subfields_total"] == 13, "readiness changed")
    require(packet["readiness_subfields"]["Gamma_nu_ij_channel_sets"] is True, "readiness channel set open")
    require(packet["neutral_overlap_OK_gates_closed"] == 6 and packet["neutral_overlap_OK_gates_total"] == 9, "OK count changed")
    require(packet["neutral_overlap_OK_gate_acceptance"]["OK5_finite_neutral_overlap_channel_sets"] is True, "OK5 open")
    require(packet["neutral_overlap_OK_gate_acceptance"]["OK6_action_costs_prefactors_characters_retarded_signs"] is False, "OK6 overclosed")
    require(packet["new_dimensionless_channel_rows_closed_here"] == 9, "dimensionless row count changed")
    require(packet["new_absolute_value_fields_closed_here"] == 0, "absolute values overclosed")
    require(packet["accepted_route_exit_count"] == 0, "route overaccepted")
    for field in ["dimensionful_M_D_3x3_closed", "dimensionful_M_L_3x3_closed", "dimensionful_M_R_3x3_closed", "absolute_normalization_and_scheme_closed", "selected_neutral_operator_accepted", "U5_closed"]:
        require(packet[field] is False and cert[field] is False, f"overclosed: {field}")

    for phrase in ["Gamma_nu^chan = I3 + X3", "channel multiplicities", "`6/9`", "`8/13`", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps({"finite_Gamma_rows": "9/9", "active_channels": 6, "exact_zeros": 3, "neutral_OK_gates": "6/9", "readiness": "8/13", "absolute_value_fields": 0, "next": NEXT}, indent=2))
    print("selected neutral finite Gamma rows / action-cost source audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
