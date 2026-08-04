from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_quantizationandnonperturbativeqft_strictupgradeaudit"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    q = load(f"candidate_data/{SLUG}/quantization_derivation_status.packet.json")
    np = load(f"candidate_data/{SLUG}/nonperturbative_4d_qft_status.packet.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    require(len(q["closed_or_conditional_results"]) == 6, "quantization result count")
    require(len(q["missing_derivations"]) == 5, "quantization gap count")
    require(q["decision"]["standard_quantization_parity_interface_closed"] is True, "parity interface")
    require(q["decision"]["U7_MTT_derived_quantization_closed"] is False, "U7 overclaim")
    require(q["decision"]["Born_rule_fully_first_principles_from_current_MTT_axioms"] is False, "Born overclaim")
    require(len(np["closed_or_conditional_results"]) == 4, "constructive results")
    require(len(np["standing_assumptions_not_derived"]) == 6, "constructive assumptions")
    require(len(np["limits_not_closed"]) == 5, "constructive limits")
    require(np["decision"]["U8_has_real_constructive_partial_result"] is True, "U8 partial")
    require(np["decision"]["U8_constructive_nonperturbative_4D_QFT_closed"] is False, "U8 overclaim")
    require(np["decision"]["finite_filtered_TT_result_mislabeled_as_full_SM_QFT"] is False, "scope overclaim")
    require(cert["U7_MTT_derived_quantization_closed"] is False, "certificate U7")
    require(cert["U8_constructive_nonperturbative_4D_QFT_closed"] is False, "certificate U8")

    print(json.dumps({
        "U7_conditional_results": 6,
        "U7_missing_derivations": 5,
        "U7_closed": False,
        "U8_constructive_partial_results": 4,
        "U8_undischarged_assumptions": 6,
        "U8_closed": False,
    }, indent=2))
    print("quantization and nonperturbative-QFT strict-upgrade audit passed")


if __name__ == "__main__":
    main()
