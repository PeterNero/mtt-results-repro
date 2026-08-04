from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finalglobaltruesmclosureaudit_aftermultiloopprecision"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(f"candidate_data/{SLUG}/final_global_true_sm_closure_audit.packet.json")
    candidate = load(f"candidate_data/{SLUG}.candidate.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    require(packet["closed_obligation_count"] == packet["obligation_count"] == 12, "obligations not closed")
    require(all(row["closed"] for row in packet["obligations"]), "open final obligation")
    require(packet["decision"]["true_SM_equivalence_closed_at_declared_standard"] is True, "true equivalence not closed")
    require(packet["decision"]["full_no_knob_closed"] is False, "no-knob overclaim")
    require(packet["decision"]["MTT_uniquely_selects_observed_universe"] is False, "unique branch overclaim")
    require(packet["decision"]["MTT_proved_superior_to_SM"] is False, "superiority overclaim")
    require(len(packet["strict_upgrades_not_part_of_claim"]) == 9, "upgrade ledger changed")
    require(all(value is False for key, value in packet["guards"].items() if key.endswith("overclaimed") or key.endswith("predictions")), "guard overclaim")
    require(packet["guards"]["target_fitting_used"] is False, "target fitting")
    require(packet["guards"]["observed_data_used_as_source_selector"] is False, "observed selector")
    require(candidate["closure_claimed"] is True and cert["closure_claimed"] is True, "scoped closure not claimed")
    require(candidate["true_SM_equivalence_closed_at_declared_standard"] is True, "candidate true equivalence")
    require(cert["true_SM_equivalence_closed_at_declared_standard"] is True, "certificate true equivalence")
    require(cert["full_no_knob_closed"] is False, "certificate no-knob overclaim")
    require(cert["next_required_artifact"] == "MTT_Selected_StrictNoKnobUpgradeLedger_AfterTrueSMEquivalence_v1", "next artifact")

    print(json.dumps({
        "closure_scope": cert["closure_scope"],
        "obligations_closed": "12/12",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed_at_declared_standard": True,
        "full_no_knob_closed": False,
        "next_required_artifact": cert["next_required_artifact"],
    }, indent=2))
    print("final global true-SM closure audit passed")


if __name__ == "__main__":
    main()
