from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_producttriplegaugefluctuationfunctorandrelativeboundarycondition"
STATUS = "MTT_SELECTED_CENTER_RESPONSE_TO_KINETIC_DENSITY_FUNCTOR_CLOSED_DUAL_LEPTON_SIGN_AND_STRICT_ACTION_COMPLETENESS_OPEN"
NEXT = "MTT_Selected_ChargedLeptonDualMetricSignAndSpectralActionCompleteness_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    readout = load(ROOT / "candidate_data" / SLUG / "center_response_to_sector_kinetic_density_functor.packet.json")
    branches = load(ROOT / "candidate_data" / SLUG / "charged_lepton_dual_metric_sign_branch_execution.packet.json")
    boundary = load(ROOT / "candidate_data" / SLUG / "relative_spectral_action_boundary_condition.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_sign_and_action_completeness_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_ProductTripleGaugeFluctuationFunctorAndRelativeBoundaryCondition_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(readout["functor"]["mathematically_well_defined"], "readout")
    check(readout["selected_sector_support"]["projectors_disjoint"], "projectors")
    check(branches["branch_count"] == 2, "branches")
    check(branches["dual_branch_max_abs_residual_to_A72"] < 1e-14, "A72 replay")
    check(not branches["binary_sign_selected_by_current_source"], "sign overclaim")
    check(boundary["A51_tree_boundary"]["relative_coordinates_zero"], "tree boundary")
    check(boundary["adopted_closure_tier"]["one_shared_physical_normalization_primitive"], "one primitive")
    check(not boundary["strict_no_knob_tier"]["A51_spectral_action_proved_complete_microscopic_MTT_action"], "action overclaim")
    check(all(gate["closed"].values()), "closed gate")
    check(gate["discrete_source_bits_remaining_for_relative_ratios"] == 1, "sign bit")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    for phrase in ["Center-to-sector functor", "Binary sign execution", "Relative boundary", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("product-triple gauge fluctuation functor audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
