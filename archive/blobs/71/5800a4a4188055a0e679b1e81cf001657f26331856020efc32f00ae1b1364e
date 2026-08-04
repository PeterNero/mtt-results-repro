"""Build the inverse superset search specification artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

INPUT = DATA / "inverse_superset_reconstruction.candidate.json"
OUTPUT_DATA = DATA / "inverse_superset_search_spec.candidate.json"
OUTPUT_CERT = CERTS / "inverse_superset_search_spec_certificate.json"
OUTPUT_NOTE = CORPUS / "MTT_Inverse_Superset_Search_Spec_v1.md"


SEARCH_DOMAINS = [
    {
        "id": "finite_topology_packet",
        "sector": "selected SM source packet",
        "variables": [
            {"name": "finite_quotient", "kind": "DISCRETE", "domain": "corpus-supported finite quotients and period selectors"},
            {"name": "family_index", "kind": "INTEGER", "domain": "index or holonomy values compatible with three families"},
            {"name": "line_bundle_charge_packet", "kind": "INTEGER_VECTOR", "domain": "topology-only hypercharge/anomaly-compatible charge lattice"},
            {"name": "representation_table", "kind": "FINITE_TABLE", "domain": "SM candidate reps with source maps"},
        ],
        "fit_targets": ["representation_count", "hypercharge_pattern", "anomaly_zero_pattern"],
        "non_target_constraints": ["source_map_exists", "three_family_index", "generic_anomaly_formula_matches"],
        "promotion_output": "selected representation/anomaly packet candidate",
    },
    {
        "id": "qa_su3_operator_packet",
        "sector": "color/operator source gate",
        "variables": [
            {"name": "D_E_or_rho_E", "kind": "ALGEBRAIC_OPERATOR", "domain": "typed operator candidates from Qa/SU3 and non-SM packet repos"},
            {"name": "typed_monad_maps", "kind": "MATRIX_OR_MAP_PACKET", "domain": "Cech-Dolbeault, monad, or section-ring map candidates"},
            {"name": "section_ring_generators", "kind": "FINITE_GENERATOR_SET", "domain": "candidate source generators with multiplication rules"},
            {"name": "Freed_Witten_Bianchi_source", "kind": "BOOLEAN_CERTIFICATE", "domain": "mapped-source consistency certificate"},
        ],
        "fit_targets": ["color_embedding", "operator_rank_pattern", "selected_representation_support"],
        "non_target_constraints": ["Bianchi_or_Freed_Witten_pass", "same_branch_selector", "typed_maps_compose"],
        "promotion_output": "Qa/SU3 color/operator packet candidate",
    },
    {
        "id": "theta_gauge_threshold_packet",
        "sector": "gauge coupling thresholds",
        "variables": [
            {"name": "heat_kernel_spectrum", "kind": "SPECTRAL_PACKET", "domain": "finite/zeta/determinant spectra from theta and non-SM work"},
            {"name": "threshold_packet", "kind": "ALGEBRAIC_PACKET", "domain": "allowed threshold kernels"},
            {"name": "normalization_index", "kind": "RATIONAL_OR_INTEGER", "domain": "U1/SU2/SU3 embedding normalization candidates"},
            {"name": "renormalization_scheme_map", "kind": "CONVENTION_MAP", "domain": "declared convention transforms only"},
        ],
        "fit_targets": ["alpha_em", "sin2_theta_w", "alpha_s"],
        "non_target_constraints": ["same_source_branch_as_sm_packet", "scheme_declared", "thresholds_not_free_per_constant"],
        "promotion_output": "selected gauge threshold packet candidate",
    },
    {
        "id": "flavor_overlap_packet",
        "sector": "Yukawa, CKM, PMNS, CP",
        "variables": [
            {"name": "overlap_kernel_blocks", "kind": "MATRIX_PACKET", "domain": "theta/string overlap and heavy-link candidates"},
            {"name": "q79_cp_character", "kind": "FINITE_CHARACTER", "domain": "q79 or compatible finite branch characters"},
            {"name": "Higgs_carrier_section", "kind": "SECTION", "domain": "Higgs carrier/source candidates"},
            {"name": "family_basis_map", "kind": "UNITARY_OR_INTEGER_MAP", "domain": "basis maps tied to family index, not CKM targets"},
        ],
        "fit_targets": ["mass_ratios", "CKM", "PMNS", "CP_phase"],
        "non_target_constraints": ["same_family_selector", "same_Higgs_carrier", "finite_CP_branch_matches"],
        "promotion_output": "selected flavor overlap packet candidate",
    },
    {
        "id": "absolute_normalization_packet",
        "sector": "dimensionful normalization",
        "variables": [
            {"name": "modal_gap", "kind": "POSITIVE_REAL_OR_ALGEBRAIC", "domain": "candidate internal gap values"},
            {"name": "internal_volume", "kind": "POSITIVE_REAL_OR_ALGEBRAIC", "domain": "selected compactification/geometry volume candidates"},
            {"name": "shared_circle_scale", "kind": "POSITIVE_REAL_OR_ALGEBRAIC", "domain": "shared-circle scale candidates"},
            {"name": "unit_dictionary_anchor", "kind": "CONVENTION_MAP", "domain": "unit conversion anchors with provenance"},
        ],
        "fit_targets": ["G_N", "Planck_scale", "absolute_unit_scale"],
        "non_target_constraints": ["compatible_with_GR_response", "compatible_with_nonSM_status", "single_anchor_not_per_constant"],
        "promotion_output": "absolute normalization candidate",
    },
]


SCORING_TERMS = [
    {
        "id": "target_residual",
        "role": "RANKING_ONLY",
        "definition": "Dimensionless residual against measured constants after declared conventions are applied.",
        "weight_policy": "May rank candidates inside inverse search; cannot select final proof object alone.",
    },
    {
        "id": "complexity_penalty",
        "role": "ANTI_OVERFIT",
        "definition": "Penalize continuous degrees of freedom, per-target knobs, large arbitrary tables, and unexplained precision.",
        "weight_policy": "High penalty for one knob per measured constant.",
    },
    {
        "id": "discreteness_bonus",
        "role": "PROMOTION_SIGNAL",
        "definition": "Reward integer, finite, algebraic, index-theoretic, or section-ring data over continuous free values.",
        "weight_policy": "Required for promotion unless an independent source-selection theorem exists.",
    },
    {
        "id": "corpus_alignment_score",
        "role": "PROMOTION_SIGNAL",
        "definition": "Reward explicit support from topology-only, theta, string/flux, q79, Qa/SU3, non-SM, or GR artifacts.",
        "weight_policy": "A numerically good candidate with zero source alignment is rejected.",
    },
    {
        "id": "cross_sector_consistency",
        "role": "REJECTION_AND_RANKING",
        "definition": "Require the same branch to support SM packet, color/operator data, thresholds, flavor, and normalization where applicable.",
        "weight_policy": "Hard reject for branch mismatch on promoted candidates.",
    },
    {
        "id": "forward_replay_score",
        "role": "PROMOTION_GATE",
        "definition": "Recompute observables from candidate packet with measured constants removed from selector inputs.",
        "weight_policy": "Mandatory before any candidate can enter a forward proof ledger.",
    },
]


REJECTION_RULES = [
    "Reject any candidate whose only support is target residual minimization.",
    "Reject any candidate using separate independent continuous knobs for each measured constant.",
    "Reject any candidate that changes branch between gauge, flavor, color, and normalization sectors.",
    "Reject any candidate that uses CKM, PMNS, masses, or couplings to choose the family index or representation packet.",
    "Reject any candidate with no typed source map for the selected operator or representation data.",
    "Reject any candidate that cannot be replayed forward without measured constants as selectors.",
]


PROMOTION_GATES = [
    {
        "id": "G0_inverse_candidate",
        "requirement": "Candidate found by inverse search and fully labeled as discovery-only.",
        "closes": "search hit, not proof",
    },
    {
        "id": "G1_compression",
        "requirement": "Fitted knobs compress to discrete, algebraic, finite, or independently corpus-selected data.",
        "closes": "anti-overfit plausibility gate",
    },
    {
        "id": "G2_source_alignment",
        "requirement": "Candidate has explicit support in the corpus or adjacent proof repos.",
        "closes": "corpus legitimacy gate",
    },
    {
        "id": "G3_cross_sector",
        "requirement": "Same branch supports the relevant SM packet, Qa/SU3, theta, flavor, and normalization sectors.",
        "closes": "superset coherence gate",
    },
    {
        "id": "G4_forward_replay",
        "requirement": "Measured targets are removed from selectors and observables are recomputed from candidate source data.",
        "closes": "candidate can enter forward proof obligations",
    },
]


def load_input() -> dict[str, object]:
    return json.loads(INPUT.read_text(encoding="utf-8"))


def build_candidate() -> dict[str, object]:
    input_data = load_input()
    return {
        "candidate": "MTTInverseSupersetSearchSpec",
        "status": "INVERSE_SUPERSET_SEARCH_SPEC_BUILT_NUMERIC_RUN_OPEN",
        "input_status": input_data["status"],
        "search_domains": SEARCH_DOMAINS,
        "scoring_terms": SCORING_TERMS,
        "rejection_rules": REJECTION_RULES,
        "promotion_gates": PROMOTION_GATES,
        "required_first_run": {
            "run_id": "qa_su3_first",
            "reason": "The current forward blocker is the selected Qa/SU3 color/operator packet.",
            "domains": ["finite_topology_packet", "qa_su3_operator_packet"],
            "targets_allowed": ["representation_count", "hypercharge_pattern", "anomaly_zero_pattern", "color_embedding", "operator_rank_pattern"],
            "targets_forbidden_as_selectors": ["masses", "CKM", "PMNS", "gauge_coupling_values"],
            "expected_output": "ranked candidate packets plus rejection/promotion labels",
        },
        "gate_results": {
            "search_space_defined": True,
            "scoring_defined": True,
            "rejection_rules_defined": True,
            "promotion_gates_defined": True,
            "first_run_selected": True,
            "numeric_search_executed": False,
            "candidate_promoted": False,
            "sm_parity_closure_claimed": False,
            "no_knob_closure_claimed": False,
        },
        "next_required_artifact": "MTT_Inverse_Qa_SU3_First_Search_Run_v1",
        "target_fitting_used": True,
        "target_fitting_role": "DISCOVERY_ONLY_SPEC",
    }


def build_certificate(candidate: dict[str, object]) -> dict[str, object]:
    return {
        "certificate": "MTTInverseSupersetSearchSpec",
        "status": "MTT_INVERSE_SUPERSET_SEARCH_SPEC_BUILT_NUMERIC_RUN_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "what_closes": {
            "inverse_search_space": True,
            "scoring_policy": True,
            "anti_overfit_rejection_rules": True,
            "promotion_gates": True,
            "first_numeric_run_scope": True,
        },
        "what_remains_open": {
            "actual_numeric_inverse_search": True,
            "ranked_candidate_packets": True,
            "compression_scores": True,
            "corpus_alignment_scores": True,
            "forward_replay": True,
            "selected_Qa_SU3_color_operator_packet": True,
            "sm_parity_closed": False,
            "no_knob_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": True,
        "target_fitting_role": "DISCOVERY_ONLY_SPEC",
    }


def render_note(candidate: dict[str, object], certificate: dict[str, object]) -> str:
    domains = []
    for domain in candidate["search_domains"]:
        variables = "\n".join(
            f"  - `{item['name']}` ({item['kind']}): {item['domain']}"
            for item in domain["variables"]
        )
        targets = ", ".join(f"`{item}`" for item in domain["fit_targets"])
        constraints = "\n".join(f"  - `{item}`" for item in domain["non_target_constraints"])
        domains.append(
            f"### {domain['id']}: {domain['sector']}\n\n"
            f"- Variables:\n{variables}\n"
            f"- Discovery targets: {targets}\n"
            f"- Non-target constraints:\n{constraints}\n"
            f"- Promotion output: {domain['promotion_output']}\n"
        )
    scoring = "\n".join(
        f"### {row['id']}\n\n"
        f"- Role: `{row['role']}`\n"
        f"- Definition: {row['definition']}\n"
        f"- Weight policy: {row['weight_policy']}\n"
        for row in candidate["scoring_terms"]
    )
    rejections = "\n".join(f"- {item}" for item in candidate["rejection_rules"])
    gates = "\n".join(
        f"### {row['id']}\n\n"
        f"- Requirement: {row['requirement']}\n"
        f"- Closes: {row['closes']}\n"
        for row in candidate["promotion_gates"]
    )
    first = candidate["required_first_run"]
    closes = "\n".join(f"- {name}" for name, value in certificate["what_closes"].items() if value)
    open_items = "\n".join(f"- {name}" for name, value in certificate["what_remains_open"].items() if value)
    return f"""# MTT Inverse Superset Search Spec v1

## Purpose

This artifact turns inverse reconstruction into an executable search
specification.  It defines the superset search domains, discovery targets,
non-target constraints, scoring terms, rejection rules, and promotion gates.

It still does not run the numeric search.  It closes the specification needed
to run it without confusing backfitting with no-knob proof.

## Search Domains

{chr(10).join(domains)}

## Scoring Terms

{scoring}

## Rejection Rules

{rejections}

## Promotion Gates

{gates}

## Required First Run

- Run id: `{first["run_id"]}`
- Reason: {first["reason"]}
- Domains: {", ".join(f"`{item}`" for item in first["domains"])}
- Targets allowed: {", ".join(f"`{item}`" for item in first["targets_allowed"])}
- Targets forbidden as selectors: {", ".join(f"`{item}`" for item in first["targets_forbidden_as_selectors"])}
- Expected output: {first["expected_output"]}

## Search Spec Theorem

The inverse program is well-posed only if target residuals are demoted to
ranking evidence and promotion requires compression, corpus alignment,
cross-sector consistency, and forward replay.  Under this policy, backfitting
can be used as a disciplined discovery method for the missing selected packet
without claiming no-knob derivation.

The first run should focus on the Qa/SU3 and finite-topology packet because
that is the current forward SM-parity blocker.

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
