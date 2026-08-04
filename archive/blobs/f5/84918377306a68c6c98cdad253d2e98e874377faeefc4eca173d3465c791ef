#!/usr/bin/env python3
"""Verify the unified-source research contract, not the source hypothesis."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LOCK_PATH = ROOT / "state" / "upstream-lock.json"
FRONTIER_PATH = ROOT / "state" / "frontier.json"

REQUIRED_FILES = (
    ROOT / "README.md",
    ROOT / "HYPOTHESIS.md",
    ROOT / "PLAN.md",
    ROOT / "docs" / "BRANCH_DECISION.md",
    ROOT / "docs" / "CANDIDATE_MATRIX.md",
    ROOT / "docs" / "SOURCE_CERTIFICATE.md",
    ROOT / "docs" / "G3D_PHYSICAL_SPECTRAL_OBJECT_CUTSET.md",
    ROOT / "docs" / "WORKER_INSTRUCTIONS.md",
    ROOT / "UST_G1_AUGMENTED_SOURCE_TYPE_ADJUDICATION_THEOREM_v1.md",
    ROOT / "UST_G1E_BUNDLE_COHESIVE_EMBEDDING_AND_REPRESENTABILITY_CUTSET_v1.md",
    ROOT / "UST_G2_FULL_RESIDUAL_HODGE_DECOMPOSITION_THEOREM_v1.md",
    ROOT / "UST_G2P_G5A_PHYSICAL_RESIDUAL_AND_FINITE_TRANSFER_INGESTION_v1.md",
    ROOT / "UST_G3A_MINIMAL_SOURCE_INGESTION_AND_ANTI_SPLICING_THEOREM_v1.md",
    ROOT / "UST_G3B_SCALE_ORBIT_AND_DIMENSIONLESS_READOUT_THEOREM_v1.md",
    ROOT / "UST_G3C_SOURCE_METRIC_COMMUTANT_AND_CONNECTED_BINDING_THEOREM_v1.md",
    ROOT / "UST_G3D_SPECTRAL_TO_COMMON_GAUDUCHON_HYM_CHAMBER_THEOREM_v1.md",
    ROOT / "state" / "ust_g1_candidate_adjudication.packet.json",
    ROOT / "state" / "ust_g1e_bundle_cohesive_embedding.packet.json",
    ROOT / "state" / "ust_g2_full_residual_hodge.packet.json",
    ROOT / "state" / "ust_g2p_g5a_physical_residual_transfer.packet.json",
    ROOT / "state" / "ust_g3_source_ingestion.schema.json",
    ROOT / "state" / "ust_g3_candidate.template.json",
    ROOT / "state" / "ust_g3_current_candidate_audit.packet.json",
    ROOT / "state" / "ust_g3b_scale_orbit.packet.json",
    ROOT / "state" / "ust_g3c_target_metric.schema.json",
    ROOT / "state" / "ust_g3c_reference_metric.packet.json",
    ROOT / "state" / "ust_g3c_candidate.template.json",
    ROOT / "state" / "ust_g3d_common_gauduchon_chamber.schema.json",
    ROOT / "state" / "ust_g3d_candidate.template.json",
    ROOT / "state" / "ust_g3d_reference_common_chamber.packet.json",
    ROOT / "state" / "ust_g3d_common_gauduchon_chamber.packet.json",
    ROOT / "verify_ust_g1_candidate_adjudication.py",
    ROOT / "verify_ust_g1e_bundle_cohesive_embedding.py",
    ROOT / "verify_ust_g2_full_residual_hodge.py",
    ROOT / "verify_ust_g2p_g5a_physical_residual_transfer.py",
    ROOT / "verify_ust_g3_source_ingestion.py",
    ROOT / "verify_ust_g3b_scale_orbit.py",
    ROOT / "verify_ust_g3c_target_metric.py",
    ROOT / "verify_ust_g3d_common_gauduchon_chamber.py",
    LOCK_PATH,
    FRONTIER_PATH,
)

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
WINDOWS_ABSOLUTE = re.compile(
    r"[A-Za-z]:\\(?:Users|Windows|Program Files|ProgramData|Temp)\\",
    re.IGNORECASE,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def verify_dependency_graph(gates: list[dict]) -> None:
    gate_ids = {gate["id"] for gate in gates}
    require(len(gate_ids) == len(gates), "gate ids must be unique")
    graph = {
        gate["id"]: [item for item in gate["depends_on"] if item in gate_ids]
        for gate in gates
    }
    temporary: set[str] = set()
    permanent: set[str] = set()

    def visit(node: str) -> None:
        require(node not in temporary, f"dependency cycle at {node}")
        if node in permanent:
            return
        temporary.add(node)
        for dependency in graph[node]:
            visit(dependency)
        temporary.remove(node)
        permanent.add(node)

    for gate_id in graph:
        visit(gate_id)


def main() -> None:
    for path in REQUIRED_FILES:
        require(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")

    lock = load_json(LOCK_PATH)
    frontier = load_json(FRONTIER_PATH)

    require(lock["schema"] == "mtt.unified-source.upstream-lock.v1", "bad lock schema")
    require(frontier["schema"] == "mtt.unified-source.frontier.v1", "bad frontier schema")
    model_hash = lock["kernel_model"]["state_sha256"]
    require(bool(HEX64.fullmatch(model_hash)), "invalid Kernel model hash")
    require(frontier["kernel_model_sha256"] == model_hash, "Kernel model locks disagree")

    repository_ids = [item["id"] for item in lock["repositories"]]
    require(len(repository_ids) == len(set(repository_ids)), "repository ids must be unique")
    for repository in lock["repositories"]:
        require(bool(HEX40.fullmatch(repository["commit"])), f"bad commit for {repository['id']}")
        for source in repository["sources"]:
            require(bool(HEX40.fullmatch(source["git_blob"])), f"bad blob for {source['path']}")
            if "sha256" in source:
                require(bool(HEX64.fullmatch(source["sha256"])), f"bad sha256 for {source['path']}")
            if "git_blob_sha256" in source:
                require(bool(HEX64.fullmatch(source["git_blob_sha256"])), f"bad blob-byte sha256 for {source['path']}")

    authority_ids = [item["id"] for item in lock["authorities"]]
    require(len(authority_ids) == len(set(authority_ids)), "authority ids must be unique")
    require("A01" in authority_ids and "A13" in authority_ids, "missing downstream authority locks")

    hypothesis = frontier["hypothesis"]
    require(hypothesis["id"] == "UST.H1", "unexpected hypothesis id")
    require(hypothesis["state"] == "HYPOTHESIS", "hypothesis was silently promoted")
    require(hypothesis["physical_promotion"] is False, "physical promotion must remain false")
    require("25-block" in frontier["frontier_current"], "current rank-102 frontier missing")
    require("physical T_fin" in frontier["frontier_current"], "current finite-map boundary missing")

    verify_dependency_graph(frontier["gates"])
    gate_states = {gate["id"]: gate["state"] for gate in frontier["gates"]}
    require(gate_states["UST.G0"] == "closed", "contract gate must be closed")
    require(gate_states["UST.G1"] == "closed_exact_two_presentation_classification", "G1 classification state")
    require(gate_states["UST.G1E"] == "partial_exact_embedding_reverse_physical_representability_open", "G1E representability state")
    require(gate_states["UST.G2"] == "closed_exact_universal_physical_K_open", "G2 theorem state")
    require(gate_states["UST.G2P"] == "closed_exact_symbolic_endpoint_coefficients_open", "G2P symbolic residual state")
    require(gate_states["UST.G3A"] == "closed_exact_contract_zero_current_promotable_candidates", "G3A ingestion state")
    require(gate_states["UST.G3B"] == "closed_exact_common_scale_physical_normalization_open", "G3B scale state")
    require(gate_states["UST.G3C"] == "closed_exact_criterion_physical_target_metric_open", "G3C target metric state")
    require(gate_states["UST.G3D"] == "closed_exact_universal_criterion_physical_spectral_objects_open", "G3D common chamber state")
    require(gate_states["UST.G5A"] == "closed_exact_criterion_physical_Tfin_open", "G5A transfer state")
    require(gate_states["UST.G3"] == "blocked_upstream", "physical source gate must remain blocked")

    hypothesis_text = (ROOT / "HYPOTHESIS.md").read_text(encoding="utf-8")
    require("## 7. Falsifiers" in hypothesis_text, "hypothesis needs explicit falsifiers")
    require("## 8. Explicit Nonclaims" in hypothesis_text, "hypothesis needs explicit nonclaims")
    require("does not prove" in hypothesis_text, "hypothesis must state its proof boundary")

    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.suffix in {".md", ".json", ".py"}:
            text = path.read_text(encoding="utf-8")
            require(
                WINDOWS_ABSOLUTE.search(text) is None,
                f"machine-specific absolute path in {path.relative_to(ROOT)}",
            )

    adjudication = subprocess.run(
        [sys.executable, str(ROOT / "verify_ust_g1_candidate_adjudication.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    print(adjudication.stdout.strip())

    embedding = subprocess.run(
        [sys.executable, str(ROOT / "verify_ust_g1e_bundle_cohesive_embedding.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    print(embedding.stdout.strip())

    full_residual = subprocess.run(
        [sys.executable, str(ROOT / "verify_ust_g2_full_residual_hodge.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    print(full_residual.stdout.strip())

    physical_residual_transfer = subprocess.run(
        [sys.executable, str(ROOT / "verify_ust_g2p_g5a_physical_residual_transfer.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    print(physical_residual_transfer.stdout.strip())

    source_ingestion = subprocess.run(
        [sys.executable, str(ROOT / "verify_ust_g3_source_ingestion.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    print(source_ingestion.stdout.strip())

    scale_orbit = subprocess.run(
        [sys.executable, str(ROOT / "verify_ust_g3b_scale_orbit.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    print(scale_orbit.stdout.strip())

    target_metric = subprocess.run(
        [sys.executable, str(ROOT / "verify_ust_g3c_target_metric.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    print(target_metric.stdout.strip())

    common_chamber = subprocess.run(
        [sys.executable, str(ROOT / "verify_ust_g3d_common_gauduchon_chamber.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    print(common_chamber.stdout.strip())

    print("mtt unified-source research contract: PASS")
    print(f"kernel model: {model_hash}")
    print(f"hypothesis: {hypothesis['id']} [{hypothesis['state']}]")
    print(f"gates: {len(frontier['gates'])}; physical promotion: false")


if __name__ == "__main__":
    main()
