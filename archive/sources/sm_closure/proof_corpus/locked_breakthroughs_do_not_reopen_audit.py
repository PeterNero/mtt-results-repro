from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    pew = load_json(
        "certificates/selected_strictpewdenominatorselectiontheorem_or_directkpromotion_certificate.json"
    )
    precision = load_json(
        "certificates/selected_precisionequivalencerows_or_truesmclosureaudit_certificate.json"
    )
    candidate = load_json("candidate_data/locked_breakthroughs_do_not_reopen.candidate.json")

    require(pew.get("denominator_selection_theorem_proved") is True, "EW denominator theorem is not proved")
    require(pew.get("accepted_global_strict_P_EW_source_rows") == 1, "strict P_EW row is not locked")
    require(
        pew.get("accepted_global_direct_K_threshold_Omega_H_lambda_rows") == 1,
        "direct K_threshold.Omega_H.lambda row is not locked",
    )
    require(pew.get("strict_zero_primitive_K_threshold_row_count") == 10, "ten-K ledger is not locked")
    require(pew.get("strict_zero_primitive_ten_K_closed") is True, "ten-K closure flag is false")
    require(precision.get("strict_PEW_directK_blocker_closed") is True, "post-PEW ledger reopens EW/direct-K")
    require(precision.get("accepted_global_strict_P_EW_source_rows") == 1, "precision ledger lost strict P_EW")
    require(
        precision.get("accepted_global_direct_K_threshold_Omega_H_lambda_rows") == 1,
        "precision ledger lost direct-K row",
    )
    require(
        candidate["closure_decision"]["do_not_reopen_as_active_blockers"]
        == [
            "strict_P_EW",
            "direct_K_threshold.Omega_H.lambda",
            "ten_row_K_threshold_ledger",
            "EW_denominator_selection",
        ],
        "locked breakthrough list changed unexpectedly",
    )

    print(
        json.dumps(
            {
                "candidate": "candidate_data/locked_breakthroughs_do_not_reopen.candidate.json",
                "status": candidate["status"],
                "strict_P_EW_rows": pew["accepted_global_strict_P_EW_source_rows"],
                "direct_K_rows": pew["accepted_global_direct_K_threshold_Omega_H_lambda_rows"],
                "K_threshold_rows": pew["strict_zero_primitive_K_threshold_row_count"],
                "strict_PEW_directK_blocker_closed": precision["strict_PEW_directK_blocker_closed"],
            },
            indent=2,
        )
    )
    print("locked breakthroughs do-not-reopen audit passed")


if __name__ == "__main__":
    main()
