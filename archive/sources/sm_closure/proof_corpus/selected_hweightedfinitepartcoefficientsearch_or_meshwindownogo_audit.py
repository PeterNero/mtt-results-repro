"""Audit H-weighted finite-part coefficient inverse search / mesh-window no-go."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hweightedfinitepartcoefficientsearch_or_meshwindownogo"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
INVERSE = PACKET_DIR / "finitepart_coefficient_inverse_problem.packet.json"
RATIONAL = PACKET_DIR / "rational_coefficient_nearmiss_search.packet.json"
NOGO = PACKET_DIR / "mesh_window_nogo_and_next_source_rule.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HWeightedFinitePartCoefficientSearch_or_MeshWindowNoGo_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HWEIGHTEDFINITEPARTCOEFFICIENTSEARCH_OR_MESHWINDOWNOGO_"
    "RATIONAL_NEARMISS_REJECTED_SOURCE_RULE_REQUIRED"
)
NEXT = "MTT_Selected_FinitePartCoefficientSourceRule_or_DirectRadialOperator_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    inverse = load(INVERSE)
    rational = load(RATIONAL)
    nogo = load(NOGO)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("inverse", inverse),
        ("rational", rational),
        ("nogo", nogo),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(nogo["next_required_artifact"] == NEXT, "nogo next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(inverse["internal_target_inversion_used"] is True, "inverse flag")
    require(math.isclose(inverse["tau_H_required"], 4.018017196377461, rel_tol=0, abs_tol=1e-12), "tau")
    require(3.57 < inverse["k_required_for_exact_match"] < 3.59, "k required")

    require(rational["accepted_finitepart_coefficient_source_count"] == 0, "accepted count")
    best = rational["best_rational_near_misses"][0]
    require(best["coefficient"] == "25/7", "best rational")
    require(best["accepted_as_finitepart_coefficient_source"] is False, "best overaccepted")
    require(best["relative_residual"] < 1e-7, "best residual")
    require(rational["seed_candidates"][0]["coefficient"] in {"25/7", "pi + 3/7"}, "seed best")

    flags = nogo["mesh_window_flags"]
    require(flags["best_rational"] == "25/7", "nogo best")
    require(flags["best_rational_numerator_equals_mesh_plus_one"] is True, "mesh flag")
    require(flags["best_rational_numerator_equals_two_cutoff_plus_one"] is True, "cutoff flag")
    require(flags["denominator_has_selected_source_here"] is False, "denominator overclaim")
    require(flags["mesh_independence_proved_here"] is False, "mesh independence overclaim")

    decision = data["closure_decision"]
    require(decision["inverse_coefficient_computed"] is True, "inverse decision")
    require(decision["bounded_rational_search_executed"] is True, "rational decision")
    require(decision["accepted_finitepart_coefficient_source_count"] == 0, "decision accepted")
    require(decision["mesh_window_nogo_active"] is True, "nogo decision")
    require(decision["strict_tau_H_promoted"] is False, "tau overpromoted")
    require(decision["strict_r_H_promoted"] is False, "r overpromoted")

    for phrase in [
        "FinitePartCoefficientInverseSearchAndMeshWindowNoGoTheorem",
        "k_required",
        "k = 25/7",
        "Accepted finite-part coefficient source rows: `0`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: finite-part coefficient inverse search finds 25/7 near-miss, "
        "but mesh-window/source no-go keeps strict closure open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
