from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_quarkleptondoubletresolvedpositivedensitysource_or_kineticweightemission"
STATUS = "MTT_SELECTED_MINIMAL_QL_RESOLVED_DENSITY_RECONSTRUCTED_TWOFACTOR_COST_NEARMISS_FOUND_STRICT_SOURCE_OPEN"
NEXT = "MTT_Selected_QuarkOrderAndSharedCircleCostSpectrum_or_TwoFactorDensityValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    reconstruction = load(ROOT / "candidate_data" / SLUG / "minimal_twofactor_positive_density_reconstruction.packet.json")
    rational = load(ROOT / "candidate_data" / SLUG / "selected_rational_cost_nearmiss.packet.json")
    contract = load(ROOT / "candidate_data" / SLUG / "next_quarkorder_sharedcircle_cost_source_contract.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_QuarkLeptonDoubletResolvedPositiveDensitySource_or_KineticWeightEmission_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == contract["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(reconstruction["one_factor_no_go"]["proved_not_exact"], "one-factor no-go")
    check(reconstruction["unique_twofactor_inverse"]["positive"], "positivity")
    check(reconstruction["unique_twofactor_inverse"]["unique"], "uniqueness")
    check(reconstruction["unique_twofactor_inverse"]["absolute_residual"] < 1e-14, "inverse")
    check(not rational["source_assessment"]["exact_profile_match"], "near-miss exactness")
    check(not rational["source_assessment"]["accepted_as_source"], "source overclaim")
    check(rational["source_assessment"]["colored_cost_has_composite_corpus_factorization"], "colored factorization")
    check(rational["corpus_factorization_clue"]["promotion_status"] == "PARTIAL_SOURCE_FACTORIZATION_ONLY", "factorization overclaim")
    check(not cert["strict_source_closed"], "closure overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict row overclaim")
    check(cert["new_continuous_parameters"] == 0, "parameter overclaim")
    for phrase in ["Exact reduction", "Unique two-factor reconstruction", "Source-native clue", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("quark/lepton resolved density audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
