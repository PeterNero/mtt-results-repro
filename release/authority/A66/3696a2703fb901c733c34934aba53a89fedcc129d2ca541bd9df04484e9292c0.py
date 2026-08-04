from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitekineticweightoperatorsource_or_circlelensnilzeromodegramexecution"
STATUS = "MTT_SELECTED_FINITE_KINETIC_WEIGHT_SOURCE_AUDITED_CURRENT_OPERATORS_UNIVERSAL_CASIMIR_TRIALS_REJECTED_COMMON_POSITIVE_SECTOR_DENSITY_OPEN"
NEXT = "MTT_Selected_PositiveSectorDensitySourceTheorem_or_CommonGaugeFlavorWeightEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    source = load(ROOT / "candidate_data" / SLUG / "current_kinetic_weight_source_audit.packet.json")
    trials = load(ROOT / "candidate_data" / SLUG / "predeclared_casimir_heat_weight_trials.packet.json")
    superset = load(ROOT / "candidate_data" / SLUG / "common_positive_sector_density_superset_contract.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_FiniteKineticWeightOperatorSource_or_CircleLensNilZeroModeGramExecution_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == superset["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "source checks")
    check(source["selected_W_kin_count"] == cert["current_selected_W_kin_count"] == 0, "weight count")
    check(len(trials["trials"]) == cert["predeclared_Casimir_trials_executed"], "trial count")
    check(trials["exact_match_count"] == cert["predeclared_exact_matches"] == 0, "trial promotion")
    check(cert["common_positive_sector_density_interface_closed"], "superset interface")
    check(not cert["positive_sector_density_values_emitted"], "density overclaim")
    check(cert["nonuniversal_gauge_rows_emitted"] == cert["strict_flavor_rows_from_common_density_emitted"] == 0, "row count")
    check(not cert["no_knob_gauge_coupling_prediction_closed"], "prediction overclaim")
    check(cert["new_continuous_parameters"] == 0, "parameters")
    for phrase in ["Current source audit", "Forward trials", "Superset reduction", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("finite kinetic weight source audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
