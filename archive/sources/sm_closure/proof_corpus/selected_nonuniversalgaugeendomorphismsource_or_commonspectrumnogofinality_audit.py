from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_nonuniversalgaugeendomorphismsource_or_commonspectrumnogofinality"
STATUS = "MTT_SELECTED_NONUNIVERSAL_GAUGE_ENDOMORPHISM_RESPONSE_RANK_CLOSED_EXISTING_SOURCE_CLASSES_EXHAUSTED_SAME_SOURCE_HESSIAN_OPEN"
NEXT = "MTT_Selected_SameSourceGaugeHessianCrossUse_or_SectorEndomorphismValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    rank = load(ROOT / "candidate_data" / SLUG / "sector_endomorphism_gauge_response_rank.packet.json")
    inventory = load(ROOT / "candidate_data" / SLUG / "existing_source_candidate_inventory.packet.json")
    contract = load(ROOT / "candidate_data" / SLUG / "next_same_source_gauge_hessian_contract.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NonUniversalGaugeEndomorphismSource_or_CommonSpectrumNoGoFinality_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == contract["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()) and all(rank["checks"].values()), "source checks")
    check(rank["relative_response_rank"] == 2, "full response rank")
    check(rank["basis_directions"]["full_weyl_common"]["rank"] == 0, "family/common no-go")
    check(rank["basis_directions"]["charged_u_d_e"]["rank"] == 1, "charged rank")
    check(rank["basis_directions"]["one_Higgs"]["rank"] == 1, "H rank")
    check(rank["basis_directions"]["charged_plus_Higgs"]["rank"] == 2, "minimal basis")
    check(not inventory["charged_K_execution"]["accepted_as_gauge_Hessian_source"], "charged cross-use overclaim")
    check(cert["existing_selected_same_source_gauge_Hessian_count"] == 0, "source count")
    check(not cert["no_knob_gauge_coupling_prediction_closed"], "prediction overclaim")
    check(cert["new_continuous_parameters"] == 0, "parameter count")
    for phrase in ["rank(RM)=2", "Family splitting alone is insufficient", "not yet the prediction", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("nonuniversal gauge endomorphism response audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
