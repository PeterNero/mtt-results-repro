from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fullanchordefecthessianactionownershipandspectatorcancellation"
STATUS = "MTT_SELECTED_RANKONE_ANCHOR_TO_COMPLEMENT_DEFECT_FUNCTOR_CLOSED_KNOWN_SPECTATORS_NEUTRAL_BASELINE_MULTIPLICITIES_OPEN"
NEXT = "MTT_Selected_BaselineCostMultiplicitySourceAndNoncentralSpectatorExclusion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    recenter = load(ROOT / "candidate_data" / SLUG / "lens_rankone_anchor_projective_tangent_recentering.packet.json")
    functor = load(ROOT / "candidate_data" / SLUG / "unital_anchor_to_sector_complement_functor.packet.json")
    spectators = load(ROOT / "candidate_data" / SLUG / "known_spectator_cancellation_ledger.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_baseline_multiplicity_and_noncentral_spectator_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_FullAnchorDefectHessianActionOwnershipAndSpectatorCancellation_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(recenter["unitary_recentring"]["U P_invariant_perp U*=P_quarter_perp"], "unitary recenter")
    check(recenter["normalized_trace"]["all_equal_three_over_four"], "trace")
    check(recenter["all_determinant_samples_equal"], "determinant")
    check(recenter["projective_tangent_theorem"]["proved"], "tangent Hessian")
    check(all(functor["theorem"].values()), "center functor")
    check(functor["action_response"]["exact_match"], "A80 response")
    check(spectators["known_classes_closed"] == spectators["known_class_count"] == 6, "known spectators")
    check(not spectators["all_possible_spectators_excluded"], "spectator overclaim")
    check(all(gate["closed"].values()), "closed gate")
    check(not gate["relative_sign_or_anchor_complement_map_still_open"], "sign map")
    check(not cert["baseline_source_closed"], "baseline overclaim")
    check(not cert["all_spectator_completeness_closed"], "completeness overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    for phrase in ["Lens projector recentering theorem", "Unique anchor-to-sector functor", "Spectator audit", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("full-anchor defect action ownership/spectator audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
