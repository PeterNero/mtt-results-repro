from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_postu5tierledger_and_u9globalbranchmeasure"
STATUS = (
    "MTT_U9_SELECTED_ANTIUNITARY_ORBIT_INVARIANT_MEASURE_AND_RETARDED_CONDITIONAL_"
    "PROBABILITY_ONE_CLOSED_GLOBAL_CARRIER_MEASURE_UNDEFINED"
)
NEXT = "MTT_Selected_FluxThresholdAxionCurrentAnomalyMatchingMap_v1"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostU5TierLedger_and_U9GlobalBranchMeasure_v1.md"


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
    measure = outputs["finite_measure"]
    global_audit = outputs["global_audit"]
    tier = outputs["U9_tier"]
    ledger = outputs["upgrade_ledger"]
    plan = outputs["next_plan"]

    require(candidate["status"] == cert["status"] == STATUS, "A95 status changed")
    require(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "A95 next changed")
    require(all(candidate["checks"].values()), "one or more A95 checks failed")
    require(measure["invariant_probability_measure"]["mu_q79"] == 0.5, "q79 invariant weight")
    require(measure["invariant_probability_measure"]["mu_q369"] == 0.5, "q369 invariant weight")
    require(measure["orientation_conditioning"]["mu_q79_given_retarded"] == 1.0, "retarded q79")
    require(measure["orientation_conditioning"]["mu_q369_given_advanced"] == 1.0, "advanced q369")
    require(measure["observed_CP_data_used"] is False, "observed CP used")
    require(global_audit["readiness"] == {"filled": 0, "required": 6}, "global readiness")
    require(global_audit["logical_boundary"]["global_uniqueness_false"] is False, "global uniqueness falsely rejected")
    require(global_audit["logical_boundary"]["global_uniqueness_proved"] is False, "global uniqueness overproved")
    require(tier["adopted_selected_orbit_standard"]["closed"] is True, "adopted U9 open")
    require(tier["strict_global_superset_standard"]["closed"] is False, "strict U9 overclosed")
    require(ledger["adopted_1_to_3_primitive_and_selected_orbit_tier"]["counts"] == {"closed": 4, "partial": 4, "dependency_blocked": 1}, "adopted counts")
    require(ledger["strict_no_knob_ledger"]["closed"] == 2 and ledger["strict_no_knob_ledger"]["partial"] == 6 and ledger["strict_no_knob_ledger"]["open_or_blocked"] == 1, "strict counts")
    require(plan["ordered_steps"][0]["target"] == "U6 strong CP selection", "next target")
    for item in candidate["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing A95 authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"A95 authority hash mismatch: {path}")
    note = NOTE.read_text(encoding="utf-8")
    for phrase in ["Finite orbit measure", "mu(q79 | retarded)=1", "not yet a", "4 closed / 4 partial / 1 dependency-blocked", NEXT]:
        require(phrase in note, f"A95 note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("post-U5 U9 branch-measure tier audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
