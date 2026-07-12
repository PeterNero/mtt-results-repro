from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutrinoandstrongcp_strictupgradeattack"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    neutrino = load(f"candidate_data/{SLUG}/neutrino_operator_ontology_and_absolute_scale_cutset.packet.json")
    cp = load(f"candidate_data/{SLUG}/strong_cp_central_charge_anomaly_cutset.packet.json")
    cert = load(f"certificates/{SLUG}_certificate.json")

    require(neutrino["closed"]["selected_same_source_SM_slot_functor_all_six_arrows"] is True, "SM-slot functor")
    require(neutrino["closed"]["ambient_Z1344_Majorana_characters"] == [0, 672], "Majorana characters")
    require(neutrino["closed"]["CP_characters_are_not_Majorana_self_characters"] is True, "CP/Majorana separation")
    require(neutrino["continuous_absolute_mass_degeneracy"]["oscillation_rows_fix_absolute_scale"] is False, "absolute mass overclaim")
    require(all(value is False for value in neutrino["guards"].values()), "neutrino guard")
    require(cp["closed"]["conditional_PQ_relaxation_theorem"] is True, "PQ theorem")
    require(cp["central_charge_kernel_obstruction"]["kernel"] == "integer multiples of (1,1,1)", "charge kernel")
    require(cp["central_charge_kernel_obstruction"]["one_may_choose_NDW_1_is_source_derivation"] is False, "chosen charge overclaim")
    require(cp["decision"]["strong_CP_problem_solved"] is False, "strong CP overclaim")
    require(all(value is False for value in cp["guards"].values()), "strong CP guard")
    require(cert["absolute_neutrino_mass_closed"] is False, "certificate neutrino")
    require(cert["strong_CP_problem_solved"] is False, "certificate strong CP")

    print(json.dumps({
        "selected_Dirac_channel": True,
        "Majorana_admissible_characters": [0, 672],
        "absolute_neutrino_mass": False,
        "conditional_PQ_theorem": True,
        "axion_ratios": True,
        "selected_QCD_anomaly_coefficient": False,
        "strong_CP_solved": False,
    }, indent=2))
    print("neutrino and strong-CP strict-upgrade attack audit passed")


if __name__ == "__main__":
    main()
