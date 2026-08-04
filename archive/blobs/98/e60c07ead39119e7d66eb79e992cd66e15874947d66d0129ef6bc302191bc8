from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(f"candidate_data/{SLUG}/branch_orbit_retarded_representative_and_global_measure_cutset.packet.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    require(len(packet["selected_unoriented_orbit"]["members"]) == 2, "orbit")
    require(packet["selected_unoriented_orbit"]["operator_entries_compared"] == 1629, "operator comparison")
    require(packet["selected_unoriented_orbit"]["maximum_conjugation_error"] < 2e-16, "conjugation")
    require(packet["observable_parity"]["CP_even_failures"] == 0, "CP even")
    require(packet["observable_parity"]["complex_conjugation_failures"] == 0, "conjugation parity")
    require(packet["retarded_representative_selection"]["CRT_q"] == 79, "CRT q")
    require(packet["retarded_representative_selection"]["q79_time_oriented_representative_selected"] is True, "q79 selection")
    require(packet["retarded_representative_selection"]["observed_CP_sign_used_as_selector"] is False, "observed selector")
    require(packet["decision"]["orientation_level_branch_selection_closed"] is True, "orientation closure")
    require(packet["decision"]["U9_full_superset_uniqueness_closed"] is False, "global uniqueness overclaim")
    require(all(value is False for value in packet["guards"].values()), "guard")
    require(cert["time_oriented_q79_representative_closed"] is True, "certificate q79")

    print(json.dumps({
        "selected_unoriented_orbit": "{q79/F/m1, q369/F*/m2}",
        "operator_entries_compared": 1629,
        "time_oriented_representative": "q79/F/m1",
        "orientation_level_selection_closed": True,
        "full_MTT_superset_uniqueness": False,
    }, indent=2))
    print("branch-orbit and retarded-representative audit passed")


if __name__ == "__main__":
    main()
