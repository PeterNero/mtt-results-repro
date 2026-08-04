#!/usr/bin/env python3
"""Verify the UST.G3A source-ingestion contract and current candidate audit."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LOCK = ROOT / "state" / "upstream-lock.json"
SCHEMA = ROOT / "state" / "ust_g3_source_ingestion.schema.json"
AUDIT = ROOT / "state" / "ust_g3_current_candidate_audit.packet.json"

ROW_IDS = ["amplitude", "local_freeness", "topology", "augmentation", "metric", "dynamics", "readout"]
GRADES = {"PASS", "FAIL", "PARTIAL", "CONDITIONAL", "OPEN", "NOT_SOURCE"}
PRIMITIVES = {"U_eta9", "W9_tau", "positive_chamber", "tangent_connection"}
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def promotable(candidate: dict) -> bool:
    rows = candidate["rows"]
    return (
        [row["id"] for row in rows] == ROW_IDS
        and all(row["grade"] == "PASS" for row in rows)
        and candidate["normalization_state"] in {"DERIVED", "BOUND"}
    )


def validate_binding(binding: dict, source_orbit_id: str, label: str) -> bool:
    require(binding["state"] in {"BOUND", "MISSING"}, f"binding state {label}")
    if binding["state"] == "BOUND":
        require(binding["source_orbit_id"] == source_orbit_id, f"same source binding {label}")
        require(bool(binding["artifact"]), f"binding artifact {label}")
        require(HEX64.fullmatch(binding["sha256"]) is not None, f"binding hash {label}")
        return True
    require(binding["artifact"] == "" and binding["sha256"] == "", f"missing binding is empty {label}")
    return False


def validate_candidate_packet(candidate: dict, locked_commits: set[str]) -> bool:
    require(candidate["schema"] == "mtt.unified-source.g3-candidate.v1", "candidate schema")
    source_orbit_id = candidate["source_orbit_id"]
    require(bool(source_orbit_id), "candidate source orbit")
    require(HEX40.fullmatch(candidate["source_commit"]) is not None, "candidate source commit")

    bindings = candidate["primitive_bindings"]
    require(set(bindings) == PRIMITIVES, "candidate primitive keys")
    primitive_results = [
        validate_binding(bindings[key], source_orbit_id, key)
        for key in sorted(PRIMITIVES)
    ]
    primitive_complete = all(primitive_results)

    normalization = candidate["normalization_binding"]
    require(normalization["state"] in {"DERIVED", "BOUND", "MISSING"}, "candidate normalization state")
    normalization_complete = normalization["state"] in {"DERIVED", "BOUND"}
    if normalization_complete:
        require(normalization["source_orbit_id"] == source_orbit_id, "same-source normalization")
        require(bool(normalization["artifact"]), "normalization certificate")
        require(HEX64.fullmatch(normalization["sha256"]) is not None, "normalization hash")
    else:
        require(normalization["artifact"] == "" and normalization["sha256"] == "", "missing normalization is empty")

    readout_complete = validate_binding(candidate["readout_binding"], source_orbit_id, "T_fin")
    rows = candidate["rows"]
    require([row["id"] for row in rows] == ROW_IDS, "candidate seven ordered rows")
    require(all(row["grade"] in GRADES and bool(row["reason"]) for row in rows), "candidate row evidence")
    rows_complete = all(row["grade"] == "PASS" for row in rows)

    computed_promotion = primitive_complete and normalization_complete and readout_complete and rows_complete
    require(candidate["physical_promotion"] is computed_promotion, "candidate promotion truth value")
    if computed_promotion:
        require(candidate["source_commit"] in locked_commits, "promoted candidate commit must be locked")
    return computed_promotion


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, help="validate one UST.G3 candidate packet")
    args = parser.parse_args()

    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))

    require(schema["$id"] == "mtt.unified-source.g3-ingestion.schema.v1", "schema id")
    require(set(schema["$defs"]["row"]["properties"]["grade"]["enum"]) == GRADES, "schema grades")
    require(schema["properties"]["rows"]["minItems"] == schema["properties"]["rows"]["maxItems"] == 7, "seven schema rows")

    require(audit["schema"] == "mtt.unified-source.g3-current-candidate-audit.v1", "audit schema")
    require(audit["theorem_id"] == "UST.G3A", "theorem id")
    require(HEX40.fullmatch(audit["source_commit"]) is not None, "source commit")
    require(audit["row_ids"] == ROW_IDS, "row order")
    require(set(audit["evidence_grades"]) == GRADES, "audit grades")
    require(set(audit["primitive_geometric_source_rows"]) == PRIMITIVES, "four primitive geometric rows")
    normalization = audit["normalization_row"]
    require(normalization["allowed_states"] == ["DERIVED", "BOUND", "MISSING"], "normalization states")
    require(normalization["current_state"] == "MISSING", "normalization remains open")
    require(normalization["maximum_independent_positive_scale_rays"] == 1, "at most one scale ray")
    require("K" in audit["derived_not_primitive"], "K is derived")
    require(audit["readout_certificate"] == "T_fin", "finite readout certificate")

    closure_repo = next(item for item in lock["repositories"] if item["id"] == "closure-dynamics")
    locked_commits = {item["commit"] for item in lock["repositories"]}
    locked_sources = {item["path"]: item.get("sha256") for item in closure_repo["sources"]}
    require(audit["source_commit"] == closure_repo["commit"], "locked closure commit")
    source_ids = set()
    for source in audit["source_locks"]:
        require(source["id"] not in source_ids, "unique source lock id")
        source_ids.add(source["id"])
        require(HEX64.fullmatch(source["sha256"]) is not None, f"source hash {source['id']}")
        require(locked_sources.get(source["path"]) == source["sha256"], f"source lock match {source['id']}")

    dependencies = audit["row_dependencies"]
    require(list(dependencies) == ROW_IDS, "dependency rows")
    for row_id, deps in dependencies.items():
        allowed = PRIMITIVES | {"lambda_act", "T_fin"}
        require(set(deps).issubset(allowed), f"known dependencies {row_id}")
    require(set(dependencies["dynamics"]) == PRIMITIVES | {"lambda_act"}, "all primitives and normalization source dynamics")
    require(set(dependencies["readout"]) == PRIMITIVES | {"lambda_act", "T_fin"}, "readout binds same source")

    candidate_ids = set()
    strict_count = 0
    excluded_by_fail = set()
    for candidate in audit["candidates"]:
        require(candidate["id"] not in candidate_ids, "unique candidate id")
        candidate_ids.add(candidate["id"])
        require(bool(candidate["source_orbit_id"]), f"source orbit {candidate['id']}")
        require(candidate["normalization_state"] in normalization["allowed_states"], f"normalization state {candidate['id']}")
        require([row["id"] for row in candidate["rows"]] == ROW_IDS, f"seven ordered rows {candidate['id']}")
        require(all(row["grade"] in GRADES for row in candidate["rows"]), f"known grades {candidate['id']}")
        require(all(set(row["source_refs"]).issubset(source_ids) for row in candidate["rows"]), f"locked row refs {candidate['id']}")
        pass_count = sum(row["grade"] == "PASS" for row in candidate["rows"])
        require(candidate["strict_pass_count"] == pass_count, f"strict pass count {candidate['id']}")
        computed = promotable(candidate)
        require(candidate["promotable"] is computed, f"promotion truth value {candidate['id']}")
        strict_count += int(computed)
        if any(row["grade"] == "FAIL" for row in candidate["rows"]):
            excluded_by_fail.add(candidate["id"])

    require(excluded_by_fail == {"C.REFERENCE_HS_BUNDLE_PAIR", "C.S_HS_COHESIVE_BENCHMARK"}, "two exact benchmark exclusions")
    require(strict_count == audit["promotable_candidate_count"] == 0, "no current promotable candidate")
    require(not audit["anti_splicing"]["transport_certificate_present"], "no cross-source transport")
    require(not audit["anti_splicing"]["mixed_candidate_promotion_allowed"], "anti-splicing enforced")
    require(not audit["physical_promotion"], "physical source remains open")

    # A synthetic all-pass packet establishes that the decision rule itself has
    # an accepting branch; current rejection is evidence-driven, not hard-coded.
    synthetic = {
        "normalization_state": "BOUND",
        "rows": [
            {"id": row_id, "grade": "PASS", "source_refs": ["S.PHYSICAL_SEED"], "reason": "witness"}
            for row_id in ROW_IDS
        ]
    }
    require(promotable(synthetic), "accepting branch witness")

    if args.candidate is not None:
        candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
        promoted = validate_candidate_packet(candidate, locked_commits)
        print(f"candidate packet: PASS; physical promotion: {str(promoted).lower()}")

    print("UST.G3A source-ingestion and anti-splicing contract: PASS")
    print("primitive continuum source rows: 4")
    print("maximum independent positive normalization rays: 1")
    print("same-source finite readout certificates: 1")
    print(f"current candidate count: {len(audit['candidates'])}")
    print("current promotable candidates: 0")


if __name__ == "__main__":
    main()
