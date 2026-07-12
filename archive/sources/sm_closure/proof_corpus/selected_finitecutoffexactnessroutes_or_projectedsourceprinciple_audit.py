"""Audit finite-cutoff exactness route classification."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitecutoffexactnessroutes_or_projectedsourceprinciple"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTES = PACKET_DIR / "finite_cutoff_exactness_route_inventory.packet.json"
CLASSIFICATION = PACKET_DIR / "current_hym_cutoff_classification.packet.json"
PRINCIPLE = PACKET_DIR / "projected_source_principle_candidate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_source_rule_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteCutoffExactnessRoutes_or_ProjectedSourcePrinciple_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FINITECUTOFFEXACTNESSROUTES_OR_PROJECTEDSOURCEPRINCIPLE_"
    "CONTINUUM_AUTOEXACTNESS_BLOCKED_PROJECTED_SOURCE_ROUTE_SELECTED"
)
NEXT = "MTT_Selected_FiniteProjectedHYMSourcePrinciple_or_BandlimitExactnessProof_v1"


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
    routes = load(ROUTES)
    classification = load(CLASSIFICATION)
    principle = load(PRINCIPLE)
    next_packet = load(NEXT_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("routes", routes),
        ("classification", classification),
        ("principle", principle),
        ("next", next_packet),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(next_packet["next_required_artifact"] == NEXT, "next packet")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(routes["selected_route"] == "selected finite projected source exactness", "selected route")
    viable = [item for item in routes["routes"] if item["route"] == "selected finite projected source exactness"][0]
    require(viable["can_attach_to_current_continuum_HYM"] is True, "projected route viability")

    require(classification["continuum_bandlimit_exactness"]["proved"] is False, "bandlimit overproof")
    require(classification["continuum_homogeneous_bergman_exactness"]["proved"] is False, "homogeneous overproof")
    require(classification["discrete_projected_exactness"]["viable"] is True, "projected exactness missing")
    require(classification["finite_replay_data"]["tau_residual_below_replay_floor"] is True, "floor condition")

    require(principle["principle_name"] == "FiniteProjectedHYMSourcePrinciple", "principle name")
    require(principle["accepted_as_strict_source_now"] is False, "principle overaccepted")
    require(principle["conditional_if_principle_proved"] is True, "conditional missing")
    require(principle["finite_objects_to_emit"]["A_N_mode_or_grid_basis"] is False, "object overemitted")

    decision = data["closure_decision"]
    require(decision["automatic_finite_cutoff_exactness_possible"] is True, "exactness possibility")
    require(decision["continuum_bandlimit_exactness_proved"] is False, "bandlimit decision")
    require(decision["selected_projected_source_route_viable"] is True, "route decision")
    require(decision["projected_source_principle_proved"] is False, "principle overproved")
    require(decision["accepted_source_rows_total"] == 0, "accepted source rows")

    for phrase in [
        "FiniteCutoffExactnessRouteClassificationTheorem",
        "FiniteProjectedHYMSourcePrinciple",
        "not proved continuum-bandlimited",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: continuum finite-cutoff autoexactness is blocked; "
        "finite projected source exactness is the selected viable route."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
