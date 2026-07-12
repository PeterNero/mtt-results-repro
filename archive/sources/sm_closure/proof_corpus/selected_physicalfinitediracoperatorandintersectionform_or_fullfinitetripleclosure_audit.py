from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalfinitediracoperatorandintersectionform_or_fullfinitetripleclosure"
STATUS = "MTT_PROFILE_DF_CLOSED_NATIVE_THREE_SUMMAND_NOGO_PROVED_MINIMAL_NEUTRAL_COMPLETION_AXIOMS_CLOSED_SELECTION_OPEN"
NEXT = "MTT_Selected_NeutralAlgebraSummandOrEquivalentAxiomRevision_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "physical_DF_and_finite_triple.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_PhysicalFiniteDiracOperatorAndIntersectionForm_or_FullFiniteTripleClosure_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(cert["profile_physical_DF_closed"] is True, "profile D_F open")
    require(cert["native_three_summand_full_finite_triple_impossible"] is True, "native no-go not proved")
    require(cert["minimal_CN_completion_finite_axioms_closed"] is True, "minimal completion open")
    require(cert["orientability_cycle_terms"] == 17, "cycle term count changed")
    require(cert["intersection_determinant_one_family"] == 4, "intersection determinant changed")
    require(cert["strict_no_knob_DF_closed"] is False, "profile values promoted to no-knob")
    require(cert["CN_selected_by_MTT"] is False, "C_N selection overclaimed")
    require(cert["full_native_finite_Connes_triple_closed"] is False, "native triple overclaimed")
    require(packet["physical_DF"]["dimension"] == 96, "D_F dimension changed")
    require(packet["native_A48_obstruction"]["intersection_determinant"] == 0, "native duality obstruction lost")
    require(packet["minimal_completion"]["intersection_determinant_three_families"] == 324, "three-family determinant changed")
    require(max(packet["residuals"].values()) < 1e-11, "finite-triple residual failed")
    require(packet["epistemic_policy"]["new_continuous_parameters_added_by_finite_axiom_completion"] == 0, "completion added a continuous parameter")
    for phrase in ["96x96", "Native Three-Summand No-Go", "sqrt(2)", "17-term", "determinant `4`", "A47 did not select", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("physical finite Dirac and intersection-form audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
