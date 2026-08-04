from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugefixedfluctuationcomplexontoweraugmentationdomains"
STATUS = "MTT_SELECTED_4D_BRST_LOGDET_WEIGHT_AND_PRIMITIVE_CHARACTER_PROJECTOR_ROUTING_CLOSED_PRODUCT_TRIPLE_MATCHING_OPEN"
NEXT = "MTT_Selected_ProductTripleGaugeFluctuationFunctorAndRelativeBoundaryCondition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    brst = load(ROOT / "candidate_data" / SLUG / "four_dimensional_brst_logdet_weight.packet.json")
    routing = load(ROOT / "candidate_data" / SLUG / "primitive_character_orbit_projector_routing.packet.json")
    execution = load(ROOT / "candidate_data" / SLUG / "a73_brst_response_exact_execution.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_product_triple_and_matching_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_GaugeFixedFluctuationComplexOnTowerAugmentationDomains_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(brst["determinant_identity"]["net_internal_logdet_weight"] == 1.0, "BRST weight")
    check(brst["A73_dimensions"]["q_gauge_one_form_equals_448"], "448 dimension")
    check(routing["q_route"]["primitive"], "q7 primitive")
    check(routing["q_route"]["projector_rank"] == 6, "P7")
    check(routing["lepton_route"]["primitive_Z4_quarter_turn"], "quarter")
    check(routing["lepton_route"]["projector_rank"] == 3, "P4")
    check(execution["e_direct_chord"]["equals_T79"], "direct T79")
    check(execution["exact_within_float_tolerance"], "A73 exact replay")
    check(all(gate["closed"].values()), "closed gate")
    check(not gate["physical_full_fluctuation_complex_closed"], "full-complex overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    for phrase in ["BRST determinant theorem", "Character-orbit routing theorem", "Exact A73 execution", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("gauge-fixed tower-augmentation fluctuation-complex audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
