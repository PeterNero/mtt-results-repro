from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "candidate_data" / "selected_e6centralgeneratorqcdanomalyaudit" / "e6_qpsi_qcd_anomaly.packet.json"
CERT = ROOT / "certificates" / "selected_e6centralgeneratorqcdanomalyaudit_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def anomaly(rows: list[dict]) -> int:
    return sum(
        row["colored_multiplicity"] * row["two_T_fund"] * row["Q_psi"]
        for row in rows
    )


def main() -> None:
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    trace = packet["colored_anomaly_trace"]
    wall = packet["domain_wall_diagnostic"]

    require(packet["inputs"]["E6_branching"] == "27 -> 16_1 + 10_-2 + 1_4", "E6 branching changed")
    require(packet["inputs"]["selected_all_six_SM_slot_arrows"] is True, "selected matter slots missing")
    require(packet["primitive_E6_central_generator"]["branching_charges"] == {"16_M": 1, "10_H_or_exotic": -2, "1_S": 4}, "Qpsi charges changed")
    require(packet["primitive_E6_central_generator"]["generator_is_selected_as_surviving_global_PQ"] is False, "Qpsi survival overclaimed")

    matter_per_family = anomaly(trace["matter_rows"])
    exotic_per_27 = anomaly(trace["exotic_rows_per_27"])
    require(matter_per_family == trace["matter_anomaly_per_family"] == 4, "matter anomaly changed")
    require(trace["matter_anomaly_total"] == 3 * matter_per_family == 12, "three-family anomaly changed")
    require(exotic_per_27 == trace["exotic_anomaly_per_27"] == -4, "exotic anomaly changed")
    require(trace["exotic_anomaly_total_for_three_27s"] == -12, "three-27 exotic anomaly changed")
    require(trace["complete_three_27_anomaly"] == 0, "complete E6 anomaly does not cancel")

    require(wall["singlet_breaking_charge"] == 4, "singlet charge changed")
    require(wall["naive_N_DW_after_singlet_identification"] == 3, "diagnostic domain-wall number changed")
    require(wall["N_DW_1_obtained"] is False, "N_DW=1 overclaim")
    require(wall["is_selected_prediction"] is False, "diagnostic promoted")
    require(packet["theorem"]["proved"] is True, "anomaly cancellation theorem missing")
    require(packet["U6_reduced_missing_object"] == "SelectedFluxThresholdAxionCurrentAnomalyMatchingMap", "U6 target changed")
    require(packet["U6_selected_QCD_anomaly_closed"] is False, "U6 anomaly overclosed")
    require(packet["U6_strong_CP_closed"] is False, "strong CP overclosed")
    require(packet["observed_data_used_as_selector"] is False, "observed selector used")
    require(cert["U6_reduced_missing_object_count"] == 1, "U6 did not contract to one object")

    print(
        json.dumps(
            {
                "matter_A3": cert["matter_anomaly_three_families"],
                "exotic_A3": cert["exotic_anomaly_three_27s"],
                "complete_27_A3": cert["complete_three_27_anomaly"],
                "naive_reduced_N_DW": cert["naive_matter_only_singlet_reduced_N_DW"],
                "selected_anomaly_open": not cert["representation_only_nonzero_PQ_anomaly_proved"],
            },
            indent=2,
        )
    )
    print("selected E6 central-generator QCD anomaly audit passed")


if __name__ == "__main__":
    main()
