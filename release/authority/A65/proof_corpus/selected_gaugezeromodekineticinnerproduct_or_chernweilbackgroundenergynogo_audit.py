from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugezeromodekineticinnerproduct_or_chernweilbackgroundenergynogo"
STATUS = "MTT_SELECTED_GAUGE_ZERO_MODE_KINETIC_HESSIAN_IDENTIFIED_SECTOR_WEIGHT_RANK_TWO_PROXY_CROSSUSE_REJECTED_WEIGHT_SOURCE_OPEN"
NEXT = "MTT_Selected_FiniteKineticWeightOperatorSource_or_CircleLensNilZeroModeGramExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    kinetic = load(ROOT / "candidate_data" / SLUG / "finite_gauge_zero_mode_kinetic_weight_theorem.packet.json")
    exclusions = load(ROOT / "candidate_data" / SLUG / "background_energy_and_scalar_proxy_exclusion.packet.json")
    contract = load(ROOT / "candidate_data" / SLUG / "selected_kinetic_weight_operator_contract.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_GaugeZeroModeKineticInnerProduct_or_ChernWeilBackgroundEnergyNoGo_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == contract["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()) and all(kinetic["checks"].values()), "source checks")
    check(kinetic["finite_form"]["relative_rank"] == 2, "weight rank")
    check(max(abs(value - 6.0) for value in kinetic["finite_form"]["identity_weight_trace"]) < 1e-14, "identity trace")
    check(max(abs(value) for value in kinetic["finite_form"]["identity_weight_relative"]) < 1e-14, "identity shape")
    check(len(exclusions["rejected_promotions"]) == cert["cross_functional_shortcuts_rejected"] == 3, "exclusions")
    check(not cert["selected_W_kin_emitted"], "weight overclaim")
    check(cert["native_nonuniversal_K_rows_emitted"] == 0 and cert["native_nonuniversal_K_rows_required"] == 3, "row count")
    check(not cert["no_knob_gauge_coupling_prediction_closed"], "prediction overclaim")
    check(cert["new_continuous_parameters"] == 0, "parameters")
    for phrase in ["Correct observable", "Three rejected shortcuts", "W_kin 0/1", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("gauge zero-mode kinetic inner-product audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
