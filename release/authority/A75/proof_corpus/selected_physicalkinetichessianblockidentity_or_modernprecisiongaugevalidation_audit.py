from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalkinetichessianblockidentity_or_modernprecisiongaugevalidation"
STATUS = "MTT_SELECTED_GAUSSIAN_LOGDET_SHAPE_AND_CENTER_TRACE_CLOSED_GAUGE_INSERTION_INTERTWINER_MATCHING_OPEN"
NEXT = "MTT_Selected_GaugeInsertionIntertwinerAndFiniteMatchingCondition_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    gaussian = load(ROOT / "candidate_data" / SLUG / "gaussian_determinant_and_center_valued_trace.packet.json")
    intertwiner = load(ROOT / "candidate_data" / SLUG / "physical_gauge_insertion_intertwiner_audit.packet.json")
    counterterm = load(ROOT / "candidate_data" / SLUG / "relative_counterterm_and_matching_no_go.packet.json")
    contract = load(ROOT / "candidate_data" / SLUG / "selected_gauge_insertion_intertwiner_and_matching_condition.template.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_PhysicalKineticHessianBlockIdentity_or_ModernPrecisionGaugeValidation_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(gaussian["finite_complex_gaussian_theorem"]["proved"], "Gaussian theorem")
    check(gaussian["center_valued_trace_theorem"]["proved"], "center trace theorem")
    check(not gaussian["A73_scope_correction"]["one_scalar_direct_sum_weighting_forced_by_A74"], "central weight overclaim")
    check(intertwiner["domain_separation_theorem"]["proved"], "domain theorem")
    check(intertwiner["target_blocks"]["Hq_dimension"] == 112, "Hq dimension")
    check(intertwiner["target_blocks"]["He_dimension"] == 64, "He dimension")
    check(not intertwiner["strict_block_identity_closed"], "physical identity overclaim")
    check(counterterm["theorem"]["relative_rank"] == 2, "counterterm rank")
    check(not contract["strict_source_acceptance"], "empty contract accepted")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    for phrase in ["Determinant theorem", "Domain theorem", "Counterterm theorem", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("physical kinetic Hessian block identity audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
