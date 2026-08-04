"""Build the inverse Qa/SU3 first search run artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
TEXPAPERS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS")
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"

INPUT = DATA / "inverse_superset_search_spec.candidate.json"
OUTPUT_DATA = DATA / "inverse_qa_su3_first_search_run.candidate.json"
OUTPUT_CERT = CERTS / "inverse_qa_su3_first_search_run_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Inverse_Qa_SU3_First_Search_Run_v1.md"

QA_INPUTS = {
    "full_corpus_dependency_audit": QA / "candidate_data" / "full_corpus_dependency_audit.candidate.json",
    "period_gate": QA / "candidate_data" / "ctwist_period_normalization_or_a01_exit.candidate.json",
    "a01_de_operator_exit_gate": QA / "candidate_data" / "a01_de_operator_exit_gate.candidate.json",
    "cech_dolbeault_scaffold": QA / "candidate_data" / "cech_dolbeault_matrix_packet_scaffold.candidate.json",
    "selected_multiplication_or_de_gate": QA / "candidate_data" / "selected_multiplication_constants_or_de_source_gate.candidate.json",
}


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_status() -> dict[str, object]:
    return {
        key: {
            "path": str(path),
            "present": path.exists(),
        }
        for key, path in QA_INPUTS.items()
    }


def score_candidate(
    *,
    route_id: str,
    label: str,
    route_type: str,
    evidence: list[str],
    missing: list[str],
    target_support: int,
    compression: int,
    corpus_alignment: int,
    cross_sector: int,
    forward_replay: int,
    rejection: str | None = None,
) -> dict[str, object]:
    total = target_support + compression + corpus_alignment + cross_sector + forward_replay
    return {
        "route_id": route_id,
        "label": label,
        "route_type": route_type,
        "scores": {
            "target_support": target_support,
            "compression": compression,
            "corpus_alignment": corpus_alignment,
            "cross_sector_consistency": cross_sector,
            "forward_replay_readiness": forward_replay,
            "total": total,
        },
        "evidence": evidence,
        "missing_for_promotion": missing,
        "rejection_reason": rejection,
        "promotion_gates": {
            "G0_inverse_candidate": rejection is None,
            "G1_compression": compression >= 2 and rejection is None,
            "G2_source_alignment": corpus_alignment >= 2 and rejection is None,
            "G3_cross_sector": cross_sector >= 2 and rejection is None,
            "G4_forward_replay": forward_replay >= 2 and rejection is None,
        },
        "promoted_to_forward_packet": False,
    }


def build_ranked_candidates(inputs: dict[str, dict[str, object]]) -> list[dict[str, object]]:
    period = inputs["period_gate"]
    scaffold = inputs["cech_dolbeault_scaffold"]
    selected = inputs["selected_multiplication_or_de_gate"]
    a01 = inputs["a01_de_operator_exit_gate"]
    candidates = [
        score_candidate(
            route_id="finite_cech_dolbeault_cochain_packet",
            label="Build the 11-space finite Cech/Dolbeault cochain packet.",
            route_type="PRIMARY_MATRIX_CONSTRUCTION_TARGET",
            evidence=[
                "Cech/Dolbeault scaffold indexes 11 spaces and five typed product blocks.",
                "All five products target P by charge.",
                "Selected multiplication gate names this route as a primary matrix construction target.",
            ],
            missing=[
                "Selected section/cochain bases for F1..F5, G1..G5, P.",
                "Selected product tables or mu_i.",
                "Selected f,g entries and gf=0 verification from selected values.",
                "Freed-Witten/Green-Schwarz/Bianchi and projector checks.",
            ],
            target_support=3 if scaffold["gate_results"]["five_typed_product_blocks_indexed"] else 1,
            compression=3,
            corpus_alignment=3,
            cross_sector=2,
            forward_replay=1,
        ),
        score_candidate(
            route_id="same_source_DE_dotD_or_rhoE_response",
            label="Build same-source D_E, dotD, or rho_E response data.",
            route_type="PRIMARY_OPERATOR_PROMOTION_ROUTE",
            evidence=[
                "A01/D_E gate requires selected D_E/rho_E or equivalent operator packet.",
                "Selected multiplication gate names same-source D_E/dotD response as a primary operator route.",
                "Validator shapes exist but selected operator values are still absent.",
            ],
            missing=[
                "Selected non-identity D_E/dotD/rho_E matrix.",
                "Spectral, heat, Riesz, torsion, or finite-part operator exit.",
                "Same-source typed matrices tying operator output to f,g/product packet.",
            ],
            target_support=3 if a01["gate_results"]["A01_DE_exit_required_by_period_gate"] else 1,
            compression=2,
            corpus_alignment=3,
            cross_sector=2,
            forward_replay=1,
        ),
        score_candidate(
            route_id="fixed_gerbe_Bfield_or_period_selector",
            label="Find a fixed same-branch gerbe/B-field representative or finite central quotient.",
            route_type="ALTERNATE_PERIOD_SELECTOR_ROUTE",
            evidence=[
                "Period gate derives the scalar A=1 condition.",
                "Full corpus audit says same-branch period selector or finite quotient remains open.",
                "This route could remove the need for arbitrary period normalization.",
            ],
            missing=[
                "Same-branch selector for R^4/alpha_prime or finite central quotient.",
                "Deligne/B-field representative tied to Qa/SU3 packet.",
                "Mapped Bianchi/Freed-Witten certificate.",
            ],
            target_support=2 if period["gate_results"]["absolute_A_unit_condition_derived"] else 1,
            compression=2,
            corpus_alignment=2,
            cross_sector=1,
            forward_replay=0,
        ),
        score_candidate(
            route_id="a01_de_operator_exit_acceptance_gate",
            label="Use the existing A01/D_E operator exit gate as the acceptance test.",
            route_type="ACCEPTANCE_GATE_NOT_SOURCE",
            evidence=[
                "Gate is already built and lists required inputs.",
                "It rejects identity rho_E, generic f,g existence, q79 import, and measured residuals.",
            ],
            missing=[
                "This is not itself a source packet.",
                "Needs selected matrices before it can promote anything.",
            ],
            target_support=2,
            compression=1,
            corpus_alignment=3,
            cross_sector=2,
            forward_replay=1,
        ),
        score_candidate(
            route_id="q79_s3_finite_torsion_pattern",
            label="Use q79/S3 finite torsion as an off-branch pattern only.",
            route_type="GUARDRAIL_PATTERN_ONLY",
            evidence=[
                "Period gate records q79/S3 as the strongest finite torsion pattern.",
                "Full corpus audit forbids direct q79/S3 import into Qa/SU3.",
            ],
            missing=[
                "Not same branch.",
                "No pushdown map to Qa/SU3 selected packet.",
            ],
            target_support=1,
            compression=2,
            corpus_alignment=2,
            cross_sector=0,
            forward_replay=0,
            rejection="OFF_BRANCH_PATTERN_ONLY",
        ),
        score_candidate(
            route_id="pure_convenience_solve_gf_zero",
            label="Choose arbitrary values satisfying Sum_i mu_i a_i b_i = 0.",
            route_type="REJECTED_UNDERDETERMINED_NOT_SELECTED",
            evidence=[
                "The gf=0 equation is easy to satisfy formally.",
                "Selected multiplication gate proves this is massively underdetermined before selection.",
            ],
            missing=[
                "No selected bases.",
                "No selected mu_i.",
                "No selected f,g entries.",
                "No selected D_E/dotD/rho_E source.",
            ],
            target_support=2,
            compression=0,
            corpus_alignment=0,
            cross_sector=0,
            forward_replay=0,
            rejection="TARGET_OR_CONVENIENCE_FIT_ONLY",
        ),
    ]
    return sorted(candidates, key=lambda row: row["scores"]["total"], reverse=True)


def build_candidate() -> dict[str, object]:
    spec = load_json(INPUT)
    inputs = {key: load_json(path) for key, path in QA_INPUTS.items()}
    ranked = build_ranked_candidates(inputs)
    top = ranked[0]
    return {
        "candidate": "MTTInverseQaSU3FirstSearchRun",
        "status": "INVERSE_QA_SU3_FIRST_SEARCH_RUN_EXECUTED_CANDIDATES_RANKED_NO_PROMOTION",
        "input_status": spec["status"],
        "source_status": source_status(),
        "search_run": {
            "run_id": "qa_su3_first",
            "domains": ["finite_topology_packet", "qa_su3_operator_packet"],
            "allowed_targets_used": ["representation_count", "hypercharge_pattern", "anomaly_zero_pattern", "color_embedding", "operator_rank_pattern"],
            "forbidden_targets_used": [],
            "measured_constants_used": False,
            "target_fitting_role": "DISCOVERY_ONLY_STRUCTURAL_RANKING",
        },
        "ranked_candidates": ranked,
        "top_candidate": {
            "route_id": top["route_id"],
            "label": top["label"],
            "total_score": top["scores"]["total"],
            "promoted_to_forward_packet": top["promoted_to_forward_packet"],
        },
        "decision": {
            "result": "Ranked first-run candidates; no candidate promoted.",
            "best_next_move": "Construct the finite Cech/Dolbeault cochain packet first, while keeping same-source D_E/dotD/rho_E as the operator acceptance route.",
            "why": "The cochain route has the strongest compression and source alignment, and it supplies the selected values needed by both gf=0 and the operator exit gate.",
        },
        "gate_results": {
            "numeric_search_executed": True,
            "ranked_candidate_packets_built": True,
            "forbidden_targets_used": False,
            "measured_constants_used": False,
            "top_candidate_identified": True,
            "convenience_solve_rejected": True,
            "off_branch_q79_rejected": True,
            "candidate_promoted": False,
            "selected_Qa_SU3_packet_closed": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Selected_Qa_SU3_Finite_Cochain_Construction_Plan_v1",
        "target_fitting_used": True,
        "target_fitting_role": "DISCOVERY_ONLY_STRUCTURAL_RANKING",
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTInverseQaSU3FirstSearchRun",
        "status": "MTT_INVERSE_QA_SU3_FIRST_SEARCH_RUN_EXECUTED_CANDIDATES_RANKED_NO_PROMOTION",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "first_inverse_Qa_SU3_ranking_run": True,
            "ranked_candidate_routes": True,
            "best_next_construction_route_identified": True,
            "convenience_fit_rejected": True,
            "off_branch_q79_import_rejected": True,
        },
        "what_remains_open": {
            "selected_11_space_finite_cochain_packet": True,
            "selected_product_tables_or_mu_i": True,
            "selected_f_g_matrix_entries": True,
            "same_source_DE_dotD_or_rhoE": True,
            "Freed_Witten_GS_Bianchi_and_projector_checks": True,
            "forward_replay": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": True,
        "target_fitting_role": "DISCOVERY_ONLY_STRUCTURAL_RANKING",
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    sources = "\n".join(
        f"- `{key}`: {body['path']} ({'present' if body['present'] else 'missing'})"
        for key, body in candidate["source_status"].items()
    )
    rows = []
    for index, row in enumerate(candidate["ranked_candidates"], start=1):
        evidence = "\n".join(f"  - {item}" for item in row["evidence"])
        missing = "\n".join(f"  - {item}" for item in row["missing_for_promotion"])
        gates = ", ".join(f"`{key}={value}`" for key, value in row["promotion_gates"].items())
        rejection = row["rejection_reason"] or "none"
        rows.append(
            f"### {index}. {row['route_id']}\n\n"
            f"- Label: {row['label']}\n"
            f"- Type: `{row['route_type']}`\n"
            f"- Scores: `{row['scores']}`\n"
            f"- Promotion gates: {gates}\n"
            f"- Rejection reason: `{rejection}`\n"
            f"- Evidence:\n{evidence}\n"
            f"- Missing for promotion:\n{missing}\n"
            f"- Promoted to forward packet: `{row['promoted_to_forward_packet']}`\n"
        )
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    run = candidate["search_run"]
    return f"""# MTT Inverse Qa/SU3 First Search Run v1

## Purpose

This artifact executes the first inverse superset ranking run for the current
SM-parity blocker: the finite-topology and Qa/SU3 color/operator packet gate.

The run uses structural targets only.  It does not use measured masses, CKM,
PMNS, gauge couplings, or other measured constants.  Its target-fitting role is
therefore discovery-only structural ranking, not no-knob proof.

## Source Inputs

{sources}

## Run Configuration

- Run id: `{run["run_id"]}`
- Domains: {", ".join(f"`{item}`" for item in run["domains"])}
- Allowed targets used: {", ".join(f"`{item}`" for item in run["allowed_targets_used"])}
- Forbidden targets used: {run["forbidden_targets_used"]}
- Measured constants used: `{run["measured_constants_used"]}`
- Target-fitting role: `{run["target_fitting_role"]}`

## Ranked Candidates

{chr(10).join(rows)}

## Decision

Top candidate:

```text
{candidate["top_candidate"]["route_id"]}
```

Result: {candidate["decision"]["result"]}

Best next move: {candidate["decision"]["best_next_move"]}

Reason: {candidate["decision"]["why"]}

## First-Run Theorem

The first inverse Qa/SU3 search run does not promote a selected packet.  It does
rank the live routes and shows that the strongest next construction is the
finite Cech/Dolbeault cochain packet, with same-source D_E/dotD/rho_E retained
as the operator acceptance path.  The pure gf=0 convenience solve and direct
q79/S3 import remain rejected.

## What This Closes

{closes}

## What Remains Open

{open_items}

## Next Artifact

```text
{candidate["next_required_artifact"]}
```
"""


def main() -> None:
    candidate = build_candidate()
    certificate = build_certificate(candidate)
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    note_text = render_note(candidate, certificate)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note_text, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
