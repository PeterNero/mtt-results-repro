from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralrecursivesharedcirclediracdomainandspinbranchreduction"
STATUS = (
    "MTT_NEUTRAL_RECURSIVE_SHAREDCIRCLE_X6_DOMAIN_CLOSED_DIRAC_FAMILY_CONSTRUCTED_"
    "FLAT_LENS_PHASE_ROUTE_REJECTED_DETERMINANT_PATH_SHARPENED"
)
NEXT = "MTT_Selected_NeutralLensNilDeterminantHolonomyExecution_or_OneScaleFinality_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralRecursiveSharedCircleDiracDomainAndSpinBranchReduction_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")],
        cwd=ROOT,
        check=True,
    )
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    geometry = outputs["geometry"]
    spin = outputs["spin"]
    dirac = outputs["dirac_family"]
    flat = outputs["flat_holonomy_no_go"]
    contract = outputs["contract"]
    frontier = outputs["U5_frontier"]

    require(candidate["status"] == cert["status"] == STATUS, "A92 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A92 next changed")
    require(all(candidate["checks"].values()), "one or more A92 checks failed")
    require(geometry["recursive_dimension_check"]["physical_internal_manifold"] == "X6=L(3,1) x (Gamma\\Nil3)", "X6 changed")
    require(geometry["literal_dimension_check"]["literal_cartesian_product_spacetime_dimension"] == 11, "literal dimension check")
    require(geometry["recursive_dimension_check"]["internal_rank"] == 6, "recursive rank check")
    require(spin["topological_calculation"]["spin_structures_L31"] == 1, "lens spin count")
    require(spin["topological_calculation"]["spin_structures_Nil3"] == 4, "nil spin count")
    require(spin["topological_calculation"]["spin_structures_X6"] == 4, "X6 spin count")
    require(dirac["construction_readiness"] == {"filled": 6, "required": 6, "family_defined": True}, "Dirac family incomplete")
    require(flat["lens_fiber"]["shape_has_exact_twofold_degeneracy"] is True, "flat lens degeneracy")
    require(flat["nil_flat_characters"]["every_one_dimensional_character_sends_center_to_identity"] is True, "nil center no-go")
    require(flat["pi_over_120_available_from_flat_internal_character"] is False, "pi/120 overclosed")
    require(contract["physical_source_selection"]["filled"] == 0 and contract["physical_source_selection"]["required"] == 8, "physical selection overclosed")
    require(frontier["strict_phase_source_closed"] is False and frontier["strict_scale_source_closed"] is False, "U5 overclosed")
    require(frontier["new_continuous_parameters_added"] == 0, "A92 added a parameter")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A92 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A92 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["cannot be a literal", "four spin structures", "mathematical family is `6/6`", "Exact flat-holonomy no-go", NEXT]:
        require(phrase in note, f"A92 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("neutral recursive shared-circle Dirac-domain audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
