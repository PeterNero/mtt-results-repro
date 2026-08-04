from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugeinsertionintertwinerandfinitematchingcondition"
STATUS = "MTT_SELECTED_96_48_DIMENSION_COINCIDENCE_TESTED_EQUIVARIANT_MATTER_INTERTWINER_REJECTED_GAUGE_COMPLEX_SOURCE_OPEN"
NEXT = "MTT_Selected_GaugeFixedFluctuationComplexOnTowerAugmentationDomains_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    dimension = load(ROOT / "candidate_data" / SLUG / "tower_augmentation_vs_sm_carrier_dimension_test.packet.json")
    equivariance = load(ROOT / "candidate_data" / SLUG / "finite_character_equivariance_obstruction.packet.json")
    product = load(ROOT / "candidate_data" / SLUG / "canonical_product_domain_construction.packet.json")
    matching = load(ROOT / "candidate_data" / SLUG / "finite_matching_condition_status.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_GaugeInsertionIntertwinerAndFiniteMatchingCondition_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(dimension["A73_active_domains"]["q_dimension"] == 96, "q dimension")
    check(dimension["A73_active_domains"]["e_return_dimension"] == 48, "e dimension")
    check(all(dimension["coincidences"].values()), "dimension coincidences")
    check(equivariance["q_factor_test"]["hom_Z7_to_Z3_times_Z2_is_trivial"], "Z7 obstruction")
    check(equivariance["e_factor_test"]["hom_Z4_to_Z3_is_trivial"], "Z4 obstruction")
    check(not equivariance["q_factor_test"]["equivariant_intertwiner_promoted"], "q overclaim")
    check(not equivariance["e_factor_test"]["equivariant_intertwiner_promoted"], "e overclaim")
    check(product["canonical_projectors"]["P7_rank"] == 6, "P7")
    check(product["canonical_projectors"]["P4_rank"] == 3, "P4")
    check(not product["physical_source"]["strict_intertwiner_closed"], "physical overclaim")
    check(matching["new_continuous_parameters"] == 0, "parameters")
    for phrase in ["Exact dimension coincidence", "Equivariance obstruction", "Constructed product domains", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("gauge insertion intertwiner and matching audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
