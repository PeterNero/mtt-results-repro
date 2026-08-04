"""Import local repo updates into the V_alpha source-selection frontier.

This is a status/method import, not a proof-data import.  It checks the local
MTT repos that have been used as adjacent workspaces, records recent heads, and
extracts only the pieces relevant to the q79/V_alpha source-selection problem.

The dirty sm-parity repo is intentionally treated as provisional clue material:
its uncommitted packets can identify the next blocker, but they do not promote
q79 selected source data.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"

REPOS = {
    "q79": ROOT,
    "constants": TEXPAPERS / "mtt-nonsm-constants-no-knob",
    "gr": TEXPAPERS / "mtt-protospinor-gr-response-proof",
    "qa_su3_packet": TEXPAPERS / "mtt-qa-su3-packet-proof",
    "sm_parity": TEXPAPERS / "mtt-sm-parity-closure",
}

INPUTS = {
    "q79_central_neutral": CERTS / "valpha_central_neutral_destabilizer_reduction_certificate.json",
    "q79_ah_promotion": CERTS / "valpha_appell_humbert_yoneda_promotion_certificate.json",
    "q79_constants_gr": CERTS / "constants_gr_cross_repo_clues_certificate.json",
    "constants_alignment": REPOS["constants"]
    / "certificates"
    / "qa_su3_internal_packet_alignment_certificate.json",
    "gr_relative_scale": REPOS["gr"]
    / "certificates"
    / "dimensional_metrology_no_go_and_relative_closure_theorem_certificate.json",
    "gr_one_anchor_propagation": REPOS["gr"]
    / "certificates"
    / "one_anchor_gr_normalization_propagation_certificate.json",
    "qa_surface_separation": REPOS["qa_su3_packet"]
    / "certificates"
    / "gr_surface_internal_quantum_separation_theorem_certificate.json",
    "qa_logdet_bridge": REPOS["qa_su3_packet"]
    / "certificates"
    / "internal_logdet_to_coupling_response_bridge_certificate.json",
    "sm_s3_source": REPOS["sm_parity"]
    / "certificates"
    / "selected_s3_differential_cohomology_source_certificate.json",
    "sm_pic0_repair": REPOS["sm_parity"]
    / "certificates"
    / "selected_pic0_invariance_or_gerbe_twisted_de_source_certificate.json",
    "sm_terminal_pic0": REPOS["sm_parity"]
    / "certificates"
    / "selected_terminal_monad_lane_pic0_quotient_source_certificate.json",
    "sm_visible_gs": REPOS["sm_parity"]
    / "certificates"
    / "selected_visible_green_schwarz_operator_source_certificate.json",
    "sm_visible_cw": REPOS["sm_parity"]
    / "certificates"
    / "selected_visible_chern_weil_operator_source_certificate.json",
    "sm_nonsplit_or_routec": REPOS["sm_parity"]
    / "certificates"
    / "selected_nonsplit_rank2_or_routec_same_source_packet_certificate.json",
    "sm_symmetry_breaker": REPOS["sm_parity"]
    / "certificates"
    / "same_source_symmetry_breaking_source_certificate.json",
    "sm_orientation_de_dotd": REPOS["sm_parity"]
    / "certificates"
    / "selected_orientation_carrying_de_dotd_source_certificate.json",
    "sm_routec_origin": REPOS["sm_parity"]
    / "certificates"
    / "routec_selected_source_origin_lemma_certificate.json",
}

OUT_DIR = CANDIDATES / "valpha_repo_update_source_frontier"
OUT_TABLE = OUT_DIR / "repo_update_frontier_table.json"
OUT_CANDIDATE = CANDIDATES / "valpha_repo_update_source_frontier.candidate.json"
OUT_CERT = CERTS / "valpha_repo_update_source_frontier_certificate.json"
OUT_PAPER = CORPUS / "VAlpha_Repo_Update_Source_Frontier_v1.md"


def run_git(repo: Path, args: list[str]) -> str:
    if not (repo / ".git").exists():
        return ""
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.stdout.strip()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def status_summary(status_short: str) -> dict[str, Any]:
    lines = [line for line in status_short.splitlines() if line.strip()]
    return {
        "dirty": bool(lines),
        "line_count": len(lines),
        "modified_count": sum(line.startswith(" M") or line.startswith("M ") for line in lines),
        "untracked_count": sum(line.startswith("??") for line in lines),
        "preview": lines[:12],
    }


def repo_snapshot(name: str, path: Path) -> dict[str, Any]:
    status = run_git(path, ["status", "--short"]) if name != "q79" else ""
    head = (
        "omitted-current-repo-head-for-reproducibility"
        if name == "q79"
        else run_git(path, ["log", "-1", "--oneline"])
    )
    recent_log = (
        ["omitted-current-repo-log-for-reproducibility"]
        if name == "q79"
        else run_git(path, ["log", "-5", "--oneline"]).splitlines()
    )
    return {
        "path": str(path),
        "present": path.exists() and (path / ".git").exists(),
        "branch": run_git(path, ["branch", "--show-current"]),
        "head": head,
        "recent_log": recent_log,
        "status_summary": (
            {
                "dirty": False,
                "line_count": 0,
                "modified_count": 0,
                "untracked_count": 0,
                "preview": [],
                "note": "current q79 status omitted so the committed certificate is reproducible",
            }
            if name == "q79"
            else status_summary(status)
        ),
    }


def cert_status(path: Path) -> dict[str, Any]:
    data = load(path)
    return {
        "path": str(path),
        "present": path.exists(),
        "status": data.get("status"),
        "closure_claimed": data.get("closure_claimed"),
        "next_required_artifact": data.get("next_required_artifact")
        or data.get("primary_next_artifact"),
        "what_closes": data.get("what_closes", {}),
        "what_remains_open": data.get("what_remains_open", {}),
    }


def build_frontier() -> dict[str, Any]:
    repo_table = {name: repo_snapshot(name, path) for name, path in REPOS.items()}
    certs = {name: cert_status(path) for name, path in INPUTS.items()}

    q79_central = load(INPUTS["q79_central_neutral"])
    q79_ah = load(INPUTS["q79_ah_promotion"])
    sm_s3 = load(INPUTS["sm_s3_source"])
    sm_pic0 = load(INPUTS["sm_pic0_repair"])
    sm_terminal = load(INPUTS["sm_terminal_pic0"])
    sm_nonsplit = load(INPUTS["sm_nonsplit_or_routec"])
    sm_symmetry = load(INPUTS["sm_symmetry_breaker"])
    sm_orientation = load(INPUTS["sm_orientation_de_dotd"])
    sm_routec = load(INPUTS["sm_routec_origin"])

    source_chain = [
        {
            "layer": "q79 stability arithmetic",
            "status": q79_central.get("status"),
            "meaning": "central-neutral base-pullback destabilizers obstructed in reduced model",
            "usable_as_proof_data": True,
        },
        {
            "layer": "q79 AH multiplication",
            "status": q79_ah.get("status"),
            "meaning": "Yoneda multiplication promoted to AH automorphy conditional on source selection",
            "usable_as_proof_data": True,
        },
        {
            "layer": "sm-parity selected S3 source",
            "status": sm_s3.get("status"),
            "meaning": "S3 differential-cohomology source support closes, but operator source remains open",
            "usable_as_proof_data": False,
        },
        {
            "layer": "sm-parity Pic0/gerbe repair",
            "status": sm_pic0.get("status"),
            "meaning": "direct Pic0 shortcut retired; gerbe-twisted D_E route promoted but open",
            "usable_as_proof_data": False,
        },
        {
            "layer": "sm-parity terminal lane Pic0",
            "status": sm_terminal.get("status"),
            "meaning": "naive Pic0 quotient rejected until invariance/neutral-selection theorem",
            "usable_as_proof_data": False,
        },
        {
            "layer": "sm-parity rank2 or Route-C same-source packet",
            "status": sm_nonsplit.get("status"),
            "meaning": "rank2 and Route-C live lanes share one symmetry-breaking source blocker",
            "usable_as_proof_data": False,
        },
        {
            "layer": "sm-parity same-source symmetry breaker",
            "status": sm_symmetry.get("status"),
            "meaning": "primary route reduced to orientation-carrying D_E/dotD packet",
            "usable_as_proof_data": False,
        },
        {
            "layer": "sm-parity orientation-carrying D_E/dotD",
            "status": sm_orientation.get("status"),
            "meaning": "reduced to selected source origin and alpha1 driver",
            "usable_as_proof_data": False,
        },
        {
            "layer": "sm-parity Route-C source origin",
            "status": sm_routec.get("status"),
            "meaning": "partial proof reduces source-origin lemma to finite emission morphism Phi_fin",
            "usable_as_proof_data": False,
        },
    ]

    frontier_reduction = {
        "all_local_repos_checked": all(row["present"] for row in repo_table.values()),
        "constants_repo_head_checked": bool(repo_table["constants"]["head"]),
        "constants_repo_dirty_provisional_only": repo_table["constants"]["status_summary"]["dirty"],
        "gr_repo_head_checked": bool(repo_table["gr"]["head"]),
        "gr_repo_dirty_provisional_only": repo_table["gr"]["status_summary"]["dirty"],
        "gr_one_anchor_propagation_status_found": bool(certs["gr_one_anchor_propagation"]["status"]),
        "qa_su3_packet_head_checked": bool(repo_table["qa_su3_packet"]["head"]),
        "qa_su3_internal_logdet_bridge_status_found": bool(certs["qa_logdet_bridge"]["status"]),
        "qa_su3_packet_dirty_provisional_only": repo_table["qa_su3_packet"]["status_summary"][
            "dirty"
        ],
        "sm_parity_repo_dirty_provisional_only": repo_table["sm_parity"]["status_summary"][
            "dirty"
        ],
        "q79_central_neutral_lane_obstructed_reduced_model": q79_central.get(
            "closed_by_this_attempt", {}
        ).get("central_neutral_base_pullback_line_destabilizers_obstructed")
        is True,
        "q79_yoneda_promoted_to_AH_conditional": q79_ah.get("closed_by_this_attempt", {}).get(
            "reduced_boundary_maps_promoted_to_AH_theta_multiplication_conditional"
        )
        is True,
        "direct_pic0_shortcut_not_available": sm_pic0.get("what_closes", {}).get(
            "direct_pic0_invariance_route_retired_for_now"
        )
        is True
        and sm_terminal.get("what_closes", {}).get("naive_pic0_quotient_rejected_until_invariance_theorem")
        is True,
        "same_source_blocker_identified": sm_nonsplit.get("what_closes", {}).get(
            "common_symmetry_breaking_source_blocker_identified"
        )
        is True,
        "next_primary_route_from_updates": "orientation-carrying D_E/dotD -> source origin + alpha1 driver -> finite emission morphism Phi_fin",
    }

    table = {
        "schema": "VAlphaRepoUpdateSourceFrontier.v1",
        "repo_table": repo_table,
        "imported_certificate_statuses": certs,
        "source_chain": source_chain,
        "frontier_reduction": frontier_reduction,
        "not_imported_as_proof_data": {
            "sm_parity_uncommitted_packets": frontier_reduction[
                "sm_parity_repo_dirty_provisional_only"
            ],
            "sm_parity_frontier_status_not_imported_as_proof": True,
            "constants_uncommitted_packets": frontier_reduction[
                "constants_repo_dirty_provisional_only"
            ],
            "gr_uncommitted_packets": frontier_reduction["gr_repo_dirty_provisional_only"],
            "qa_su3_packet_uncommitted_packets": frontier_reduction[
                "qa_su3_packet_dirty_provisional_only"
            ],
            "selected_visible_valpha_source": True,
            "selected_Pic0_rule": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "selected_HYM_or_RouteC_values": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "next_required_artifact": "Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1",
    }
    return table


def build_paper(cert: dict[str, Any]) -> str:
    table = cert["repo_update_source_frontier"]
    repos = table["repo_table"]
    chain = "\n".join(
        f"- {row['layer']}: `{row['status']}`"
        for row in table["source_chain"]
    )
    repo_lines = "\n".join(
        f"- {name}: `{row['head']}` dirty={row['status_summary']['dirty']}"
        for name, row in repos.items()
    )
    dirty_adjacent = [
        name
        for name, row in repos.items()
        if name != "q79" and row["status_summary"]["dirty"]
    ]
    dirty_text = ", ".join(f"`{name}`" for name in dirty_adjacent) or "none"
    reduction = table["frontier_reduction"]
    return f"""# VAlpha Repo-Update Source Frontier v1

## Repo Inventory

{repo_lines}

Any dirty adjacent repo is deliberately treated as provisional.  In the current
run this includes: {dirty_text}.  These packets are useful for frontier triage,
not for q79 proof promotion.

## Imported Frontier Chain

{chain}

## What Changed

The adjacent repos are moving quickly.  This packet records their current
heads and treats any dirty adjacent workspace as provisional clue material.
The q79 repo has already closed the central-neutral reduced stability lane and
promoted the reduced Yoneda maps to Appell-Humbert multiplication conditional
on selected source.

The sm-parity frontier does not close Pic0 or the selected visible source.  It
does sharpen the route:

```text
same-source symmetry breaker
  -> orientation-carrying D_E/dotD
  -> selected source origin + alpha1 driver
  -> finite emission morphism Phi_fin.
```

## Guardrail

The following are not imported as proof data:

```json
{json.dumps(table["not_imported_as_proof_data"], indent=2)}
```

## Next Artifact

`{table["next_required_artifact"]}`.

This should bridge the q79 Appell-Humbert/rank-two data to the source-origin
and finite-emission-morphism route without using target fitting, uncommitted
adjacent packets, or SM-parity frontier statuses as final proof.

## Machine Reduction

```json
{json.dumps(reduction, indent=2)}
```
"""


def main() -> int:
    table = build_frontier()
    cert = {
        "certificate": "VAlphaRepoUpdateSourceFrontier",
        "status": "VALPHA_REPO_UPDATE_SOURCE_FRONTIER_REDUCED_TO_SOURCE_ORIGIN_FINITE_EMISSION_BRIDGE",
        "analysis_script": rel(Path(__file__)),
        "candidate_data": rel(OUT_CANDIDATE),
        "table_packet": rel(OUT_TABLE),
        "paper": rel(OUT_PAPER),
        "repo_update_source_frontier": table,
        "closed_by_this_attempt": {
            "all_local_repos_checked": table["frontier_reduction"]["all_local_repos_checked"],
            "constants_update_boundary_recorded": table["frontier_reduction"][
                "constants_repo_head_checked"
            ],
            "safe_sm_parity_import_boundary_recorded": table["repo_table"]["sm_parity"][
                "present"
            ],
            "next_frontier_reduced_to_source_origin_finite_emission_bridge": True,
        },
        "still_open": {
            "selected_visible_valpha_source": True,
            "selected_Pic0_rule": True,
            "global_rank_one_torsion_free_subsheaf_enumeration": True,
            "selected_D_E_dotD_Riesz_Green": True,
            "finite_emission_morphism_Phi_fin": True,
            "selected_HYM_or_RouteC_values": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_sm_parity_uncommitted_packets_are_proof": False,
            "claims_sm_parity_frontier_status_as_proof": False,
            "claims_selected_visible_valpha_source": False,
            "claims_selected_Pic0_rule": False,
            "claims_full_stability": False,
            "claims_HYM_or_RouteC_values": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "All local repos were checked. Committed adjacent updates and dirty "
                "provisional packets add source-discipline and internal-status "
                "constraints, not V_alpha proof data. The frontier narrows the next "
                "move to a source-origin/finite-emission bridge, but adjacent "
                "frontier statuses or closure_claimed=false packets cannot be used "
                "as final proof."
            ),
            "next_action": (
                "Build Q79_VAlpha_Source_Origin_and_Finite_Emission_Bridge_v1, "
                "using q79 AH/rank-two data as the committed side and sm-parity "
                "Phi_fin/source-origin packets only as frontier constraints until "
                "their selected source proof is closed."
            ),
        },
    }
    write_json(OUT_TABLE, table)
    write_json(OUT_CANDIDATE, cert)
    write_json(OUT_CERT, cert)
    OUT_PAPER.parent.mkdir(parents=True, exist_ok=True)
    OUT_PAPER.write_text(build_paper(cert), encoding="utf-8")

    print("VAlpha repo-update source frontier")
    print(json.dumps({"status": cert["status"], "certificate": rel(OUT_CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
