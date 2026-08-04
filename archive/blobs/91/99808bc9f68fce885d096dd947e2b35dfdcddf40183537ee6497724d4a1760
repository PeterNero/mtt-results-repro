"""Audit stable labels for the post-SM-parity work breakdown."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_postsmparity_workbreakdown_labels"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LABELS = PACKET_DIR / "canonical_work_labels.packet.json"
MATRIX = PACKET_DIR / "remaining_work_status_matrix.packet.json"
ROUTE_MAP = PACKET_DIR / "route_label_map.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostSMParity_WorkBreakdown_Labels_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_POSTSMPARITY_WORKBREAKDOWN_LABELS_BUILT"
NEXT_ARTIFACT = "MTT_Selected_SameSourceDynamicPhiFinC1_or_HonestGalerkinExecution_RouteTest_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    labels = load(LABELS)
    matrix = load(MATRIX)
    route_map = load(ROUTE_MAP)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem mismatch")
    require(data["next_required_artifact"] == NEXT_ARTIFACT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next mismatch")

    coverage = labels["coverage"]
    require(coverage["labels_cover_frontier"] is True, "labels do not cover frontier")
    require(coverage["route_ids_match_frontier_contract"] is True, "routes do not match frontier")
    require(coverage["remaining_label_count"] == 10, "remaining label count mismatch")
    require(coverage["closed_label_count"] == 3, "closed label count mismatch")
    require(coverage["route_label_count"] == 3, "route label count mismatch")

    remaining = {item["id"]: item for item in labels["remaining_labels"]}
    expected = [
        "PSM-DYN-01",
        "PSM-C1-01",
        "PSM-C1-02",
        "PSM-C1-03",
        "PSM-C1-04",
        "PSM-C1-05",
        "PSM-C1-06",
        "PSM-S2-01",
        "PSM-QFT-01",
        "PSM-NK-01",
    ]
    require(list(remaining) == expected, "remaining label order mismatch")
    require(remaining["PSM-C1-01"]["status"] == "OPEN_PRIMARY", "PSM-C1-01 should be primary")
    require(remaining["PSM-C1-04"]["subcategory"] == "b_selected", "b label mismatch")
    require(remaining["PSM-C1-05"]["status"] == "OPEN_DEPENDS_ON_PSM-C1-03_PSM-C1-04", "delta dependency mismatch")
    require(remaining["PSM-NK-01"]["status"] == "OPEN_STRONGER_THAN_TRUE_EQUIVALENCE", "no-knob status mismatch")

    closed = {item["id"]: item for item in labels["closed_labels"]}
    require(closed["DONE-PARITY-00"]["status"] == "CLOSED_FROZEN", "parity not frozen")
    require(closed["DONE-SOURCE-00"]["status"] == "CLOSED_FROZEN", "source not frozen")
    require(closed["DONE-DYN-SUPPORT-00"]["status"] == "CLOSED_SUPPORT", "support status mismatch")

    routes = {item["id"]: item for item in route_map["routes"]}
    require(routes["ROUTE-A"]["status"] == "OPEN_PRIMARY", "route A not primary")
    require("PSM-C1-01" in routes["ROUTE-A"]["owns_labels"], "route A ownership missing")
    require("PSM-DYN-01" in routes["ROUTE-B"]["owns_labels"], "route B ownership missing")
    require("PSM-QFT-01" in routes["ROUTE-C"]["owns_labels"], "route C ownership missing")

    require(matrix["current_active_label"] == "PSM-C1-01", "active label mismatch")
    require(matrix["current_active_route"] == "ROUTE-A", "active route mismatch")
    require(matrix["dependency_order"][0] == "PSM-C1-01", "dependency start mismatch")
    require(matrix["dependency_order"][-1] == "PSM-NK-01", "dependency end mismatch")

    require(data["closure_decision"]["label_artifact_closed"] is True, "label artifact not closed")
    require(data["closure_decision"]["SM_parity_reopened"] is False, "SM parity reopened")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(data["what_closes_now"]["current_active_label_selected"] == "PSM-C1-01", "active label flag missing")

    for token in ["PSM-C1-01", "PSM-C1-04", "PSM-DYN-01", "PSM-QFT-01", "ROUTE-A", "ROUTE-B", "ROUTE-C"]:
        require(token in note, f"note missing {token}")

    for packet in [data, labels, matrix, route_map, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
