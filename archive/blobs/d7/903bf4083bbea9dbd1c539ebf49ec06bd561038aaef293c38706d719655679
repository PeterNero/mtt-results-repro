from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitematchingcompletenessfromunifiedaction_or_explicitboundaryadoptionandheldoutvalidation"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteMatchingCompletenessFromUnifiedAction_or_ExplicitBoundaryAdoptionAndHeldOutValidation_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    cert = load(CERT)
    outputs = {key: load(ROOT / value) for key, value in candidate["outputs"].items()}
    bare = outputs["bare_completeness"]
    scheme = outputs["scheme_separation"]
    ledger = outputs["tier_ledger"]
    freeze = outputs["heldout_freeze"]

    require(all(candidate["checks"].values()), "one or more finite-matching checks failed")
    require(bare["theorem"]["proved_at_corpus_spectral_action_tier"], "bare CSGA2 theorem not proved at stated tier")
    require(not bare["scope_guard"]["derived_from_primitive_MTT_core_axioms"], "primitive-core derivation overclaimed")
    require(bare["relative_counterterm_space"]["rank"] == 2, "relative counterterm rank changed")
    require(bare["relative_counterterm_space"]["common_vector_image"] == [0, 0], "common normalization is not in kernel")
    require(scheme["theorem"]["proved"], "bare/renormalized scheme separation not proved")
    require(scheme["current_profile_tier"]["selected_multiloop_common_scheme_fixed"], "current common scheme not fixed")
    require(not scheme["strict_no_knob_tier"]["renormalization_condition_derived_from_primitive_MTT_core"], "strict scheme overclaimed")
    require(ledger["remaining_structural_action_clauses_at_corpus_action_current_profile_tier"] == 0, "current-tier action clause remains")
    require(ledger["remaining_structural_action_clauses_at_primitive_no_knob_tier"] == 1, "strict tier guard changed")
    require(ledger["strict_gauge_values_accepted"] == 0, "strict gauge values overpromoted")
    require(not freeze["held_out_validation_executed"], "known profile mislabeled as held out")
    for item in freeze["freeze"]["authority_hashes"]:
        path = Path(item["path"])
        require(path.exists(), f"missing frozen authority: {path}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f"authority hash mismatch: {path}")
    require(cert["status"] == candidate["status"], "certificate status mismatch")
    require(cert["next_required_artifact"] == candidate["next_required_artifact"], "next artifact mismatch")
    require(NOTE.exists(), "theorem note missing")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
