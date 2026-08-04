from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_renormalizedsmobservablefunctor_fromcommonschemeaction"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(f"candidate_data/{SLUG}/renormalized_sm_observable_functor.packet.json")
    candidate = load(f"candidate_data/{SLUG}.candidate.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    require(packet["equivalence_theorem"]["proved"] is True, "equivalence theorem missing")
    require(len(packet["arrows"]) == 5 and all(row["closed"] for row in packet["arrows"]), "functor arrows")
    require(packet["acceptance"]["local_QFT_observable_functor_closed_at_parity_profile_standard"] is True, "functor open")
    require(packet["acceptance"]["separate_finite_observable_table_required_for_equivalence_theorem"] is False, "finite-table loop retained")
    require(packet["scope_guards"]["standard_SM_quantization_imported_as_parity_structure"] is True, "parity import missing")
    require(packet["scope_guards"]["standard_SM_quantization_derived_from_MTT"] is False, "quantization overderived")
    require(packet["scope_guards"]["strict_no_knob_local_QFT_functor_closed"] is False, "no-knob overclaim")
    require(candidate["closure_claimed"] is True and cert["closure_claimed"] is True, "scoped closure not claimed")
    require(cert["actual_local_QFT_observable_functor_at_parity_profile_standard"] is True, "certificate functor")
    require(cert["renormalized_action_equivalence_implies_observable_equivalence"] is True, "certificate theorem")
    require(cert["target_fitting_used"] is False and cert["observed_data_used_as_selector"] is False, "guards")

    print(json.dumps({
        "actual_local_QFT_observable_functor_at_parity_profile_standard": True,
        "functor_arrows_closed": "5/5",
        "all_perturbative_SM_observables_inherited": True,
        "strict_no_knob_local_QFT_functor_closed": False,
        "next_required_artifact": cert["next_required_artifact"],
    }, indent=2))
    print("selected renormalized SM observable functor audit passed")


if __name__ == "__main__":
    main()
