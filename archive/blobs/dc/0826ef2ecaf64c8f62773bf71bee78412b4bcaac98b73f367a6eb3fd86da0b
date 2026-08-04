"""Build CONST-EW-02 B26 two-edge weak-mixing promotion contract."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"
SM = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b26_two_edge_promotion_contract"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GAUGE = BASE / "gaugekinetic_rg_source_contract.packet.json"
C1 = BASE / "primitive_c1_sourcevalue_contract.packet.json"
SYNTHESIS = BASE / "superset_route_synthesis.packet.json"
BOUNDARY = BASE / "weak_mixing_b26_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B26_TwoEdgePromotionContract_v1.md"

STATUS = "MTT_CONST_EW_02_B26_TWO_EDGE_PROMOTION_CONTRACT_BUILT_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b25_path = DATA / "const_ew_02_weak_mixing_b25_internal_lambda12_physical_frontier.candidate.json"
    b25_physical_path = DATA / "const_ew_02_weak_mixing_b25_internal_lambda12_physical_frontier" / "physical_anchor_rg_frontier.packet.json"
    b25_c1_path = DATA / "const_ew_02_weak_mixing_b25_internal_lambda12_physical_frontier" / "primitive_c1_atom_cutset_import.packet.json"
    b25_boundary_path = DATA / "const_ew_02_weak_mixing_b25_internal_lambda12_physical_frontier" / "weak_mixing_b25_boundary.packet.json"
    b23_path = DATA / "const_ew_02_weak_mixing_b23_cross_use_universal_parameter_admissibility.candidate.json"

    qa_payload_template = QA / "proof_corpus" / "Selected_U1_SU2_Internal_Overlap_Payload_Template_or_K_Gauge_Source_Fill_v1.md"
    qa_same_scheme_audit = QA / "proof_corpus" / "u1_su2_same_scheme_payloads_or_k_gauge_anchor_audit.py"
    qa_c1_missing = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_missing_leaves.json"
    sm_c1_frontier = SM / "candidate_data" / "selected_c1_frontier_after_alpha1_driver.candidate.json"

    b25 = load(b25_path)
    b25_physical = load(b25_physical_path)
    b25_c1 = load(b25_c1_path)
    b25_boundary = load(b25_boundary_path)
    b23 = load(b23_path)
    c1_missing = load(qa_c1_missing)
    sm_c1 = load(sm_c1_frontier) if sm_c1_frontier.exists() else {}

    external_refs = [
        {
            "role": "precision_SM_RG_benchmark_policy",
            "source": "Mihaila, Salomon, Steinhauser, Gauge Coupling Beta Functions in the Standard Model to Three Loops, arXiv:1201.5868",
            "url": "https://arxiv.org/abs/1201.5868",
            "imported_use": "Benchmark support for requiring a declared perturbative RG scheme before physical electroweak comparison.",
            "value_imported": False,
        },
        {
            "role": "heterotic_threshold_shape",
            "source": "Angelantonj, Florakis, Tsulaia, Generalised universality of gauge thresholds in heterotic vacua, Nucl. Phys. B 900 (2015)",
            "url": "https://www.sciencedirect.com/science/article/pii/S0550321315003156",
            "imported_use": "Structural support that heterotic gauge thresholds are model/spectrum dependent and must be source-emitted rather than assumed.",
            "value_imported": False,
        },
        {
            "role": "measured_electroweak_replay_language",
            "source": "Particle Data Group, Electroweak Model and Constraints on New Physics review",
            "url": "https://pdg.lbl.gov/2023/reviews/rpp2022-rev-standard-model.pdf",
            "imported_use": "Downstream convention support for theta_W, e=g sin(theta_W), and precision electroweak replay; not a selector.",
            "value_imported": False,
        },
    ]

    corpus_refs = [
        {
            "role": "MTT_geometry_light_democracy_identity",
            "path": "18 Theta-Closure & Execution Program/_md/Geometry__Light_Relations_in_Modal_Triplet_Theory__MTT__v2.md",
            "imported_use": "High-scale sin^2(theta_W)=3/8 identity under modal democracy; useful as a limiting check, not current physical closure.",
            "value_imported": False,
        },
        {
            "role": "heterotic_tree_gauge_function",
            "path": "16 Strings, Flux, & M-Theory Encodings/_md/Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
            "imported_use": "Tree-level f=S universal gauge kinetic shape; supports a common-action-normalization route but does not fix Re(S) or thresholds.",
            "value_imported": False,
        },
        {
            "role": "QA_SU3_same_scheme_template",
            "path": rel(qa_payload_template),
            "imported_use": "Same-scheme I_1, I_2, K_gauge acceptance template and promotion tests.",
            "value_imported": False,
        },
    ]

    gauge_contract = {
        "schema": "MTTConstEW02B26GaugeKineticRGSourceContract.v1",
        "status": "GAUGEKINETIC_RG_SOURCE_CONTRACT_BUILT_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B26-GAUGEKINETIC-NORMALIZATION-RG-SCHEME",
        "inputs": {
            "B25_candidate": rel(b25_path),
            "B25_physical_frontier": rel(b25_physical_path),
            "B25_boundary": rel(b25_boundary_path),
            "qa_same_scheme_payload_template": rel(qa_payload_template),
            "qa_same_scheme_audit": rel(qa_same_scheme_audit),
        },
        "closed_inputs_available": {
            "u_dyn": 1,
            "internal_lambda_12": b25["internal_lambda_12_value"],
            "internal_Delta_G12": b25_physical["conditional_interface"]["closed_internal_weak_split"]["Delta_G12"],
            "typed_Qa_Qc_hypercharge_threshold_map": b25_physical["closed_now"]["typed_Qa_Qc_hypercharge_threshold_map"],
        },
        "required_source_packet": {
            "K_phys_or_gauge_kinetic_matrix": {
                "required": True,
                "description": "A same-branch action normalization, equivalently a physical gauge kinetic matrix f_ab or K_phys in the same trace/action convention as the internal threshold vector.",
            },
            "mu_match": {
                "required": True,
                "description": "A selected matching surface before comparison to M_Z or any measured electroweak datum.",
            },
            "RG_and_threshold_scheme": {
                "required": True,
                "description": "Declared perturbative order, renormalization scheme, active spectra, and threshold policy.",
            },
            "full_threshold_vector": {
                "required": True,
                "description": "Delta_a^sel beyond the already imported weak split, or a theorem that the missing threshold components vanish in the selected scheme.",
            },
        },
        "forward_map_when_packet_exists": {
            "formula": "G_a^phys(mu) = K_phys * I_a + Delta_a^sel + b_a/(8*pi^2)*log(mu_match/mu)",
            "weak_angle_replay": "sin2(theta_W)(mu) = alpha_Y(mu)/(alpha_Y(mu)+alpha_2(mu)) after the selected convention map is fixed",
            "data_role": "measured alpha, sin2, masses, CKM, and PMNS may replay/check only after packet selection",
        },
        "superset_path": "straight gauge-kinetic path using MTT/heterotic/QFT overlap language",
        "external_refs": external_refs,
        "corpus_refs": corpus_refs,
        "decision": {
            "K_phys_or_f_ab_closed": False,
            "mu_match_closed": False,
            "RG_scheme_closed": False,
            "full_threshold_vector_closed": False,
            "measured_electroweak_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    c1_contract = {
        "schema": "MTTConstEW02B26PrimitiveC1SourceValueContract.v1",
        "status": "PRIMITIVE_C1_SOURCEVALUE_CONTRACT_BUILT_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B26-PRIMITIVE-C1-SOURCEVALUE-THEOREM",
        "inputs": {
            "B25_primitive_c1_cutset": rel(b25_c1_path),
            "qa_primitive_c1_missing_leaves": rel(qa_c1_missing),
            "sm_parity_c1_frontier_after_alpha1_driver": rel(sm_c1_frontier) if sm_c1_frontier.exists() else "MISSING_IN_CURRENT_SCAN",
        },
        "required_source_packet": {
            "selected_bases": {
                "count": 12,
                "description": "Same-source bases for sector/source/target rows before any atom value can be promoted.",
            },
            "primitive_atom_matrices": {
                "count": 24,
                "shape": "3x3",
                "description": "All selected primitive C1 atom matrices, not inferred from measured masses or weak angle.",
            },
            "b_and_homogeneous_zero_leaves": {
                "count": 4,
                "description": "b_selected and homogeneous-zero leaves needed to compute A_selected and b_selected.",
            },
        },
        "minimal_closing_options": b25_c1["minimal_closing_options"],
        "missing_leaf_count": len(c1_missing["missing_leaves"]),
        "missing_atom_count": b25_c1["interface"]["missing_atom_count"],
        "sm_parity_support": {
            "cross_repo_candidate_present": bool(sm_c1),
            "status": sm_c1.get("status", "NOT_IMPORTED"),
            "use": "supporting frontier only; individual-constant repo still requires a local source-value theorem",
        },
        "superset_path": "cross-encoding dynamic-C1 path using QA-SU3 atom interface plus SM-parity C1 frontier",
        "decision": {
            "primitive_C1_atoms_emitted": False,
            "A_selected_computable": False,
            "b_selected_computable": False,
            "selected_zero_tensor_promoted": False,
            "measured_electroweak_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    synthesis = {
        "schema": "MTTConstEW02B26SupersetRouteSynthesis.v1",
        "status": "TWO_ADMISSIBLE_PROMOTION_EDGES_SYNTHESIZED_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B26-SUPERSET-TWO-EDGE-SYNTHESIS",
        "locked_target": "physical weak mixing angle/electroweak coupling replay after source selection",
        "superset_strategy": {
            "straight_path": {
                "name": "gaugekinetic_rg_source_packet",
                "inputs": ["MTT gauge overlap", "heterotic f=S/threshold shape", "SM RG scheme"],
                "must_emit": ["K_phys or f_ab", "mu_match", "RG/threshold scheme", "Delta_a^sel"],
            },
            "cross_encoding_path": {
                "name": "primitive_C1_sourcevalue_packet",
                "inputs": ["QA-SU3 primitive atom interface", "SM-parity dynamic C1 frontier", "typed monad/Cech/HYM witness"],
                "must_emit": ["12 selected bases", "24 primitive atom matrices", "4 b/homogeneous-zero leaves"],
            },
            "universal_parameter_path": {
                "name": "single_declared_u_phys",
                "allowed_by_B23": b23["theorem"]["proved"],
                "use": "conditional parity/prediction lane only, not strict no-knob closure",
            },
        },
        "exclusivity_theorem": {
            "proved": True,
            "statement": "Given B24 u_dyn=1 and B25 internal lambda_12/Delta_G12 closure, physical weak-angle promotion can only enter through a same-branch physical gauge/action/RG packet, through selected primitive C1 source values that compute the missing response/threshold packet, or through a separately declared universal u_phys lane. Any route using observed weak-angle, alpha, masses, CKM, or PMNS to choose these packets is inadmissible.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B26Boundary.v1",
        "status": "PROMOTION_CONTRACT_BUILT_NO_VALUE_PROMOTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B26-BOUNDARY",
        "closed_now": {
            "two_edge_promotion_contract": True,
            "external_RG_benchmark_policy_imported": True,
            "heterotic_gaugekinetic_shape_imported_as_structure": True,
            "primitive_C1_sourcevalue_schema": True,
            "superset_paths_locked_to_same_target": True,
        },
        "still_open": {
            "K_phys_or_f_ab": True,
            "mu_match": True,
            "RG_and_threshold_scheme": True,
            "full_threshold_vector": True,
            "primitive_C1_atom_values": True,
            "A_selected": True,
            "b_selected": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "guardrails": {
            "observed_weak_angle_as_selector": False,
            "observed_alpha_as_selector": False,
            "observed_masses_CKM_PMNS_as_selector": False,
            "per_observable_retuning": False,
        },
        "allowed_claim": "the remaining promotion problem is reduced to two named source packets plus an optional separately declared universal-parameter lane",
        "forbidden_claim": "a numeric physical weak angle or no-knob electroweak closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B26NextWork.v1",
        "status": "NEXT_WORKORDER_EXECUTE_ONE_EDGE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B27-EXECUTE-GAUGEKINETIC-OR-C1-EDGE",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B27-GAUGEKINETIC-ACTION-ANCHOR-EXECUTION",
            "task": "Try to emit K_phys/f_ab and mu_match from MTT action normalization, heterotic f=S data, or a same-source compactification/action unit.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B27-PRIMITIVE-C1-ATOM-VALUE-EXECUTION",
            "task": "Try to fill selected bases and the 24 primitive C1 atom matrices from typed monad/Cech/HYM connection data or prove the selected zero tensor.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB26TwoEdgePromotionContract",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B26-PHYSICAL-GAUGE-ANCHOR-OR-C1-ATOMS",
        "output_packets": {
            "gaugekinetic_rg_source_contract": rel(GAUGE),
            "primitive_c1_sourcevalue_contract": rel(C1),
            "superset_route_synthesis": rel(SYNTHESIS),
            "weak_mixing_b26_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": synthesis["exclusivity_theorem"],
        "two_edge_contract_built": True,
        "internal_lambda_12_closed_preserved": True,
        "internal_lambda_12_value": b25["internal_lambda_12_value"],
        "u_dyn_source_derived_preserved": b25["u_dyn_source_derived"],
        "K_phys_or_f_ab_closed": False,
        "mu_match_closed": False,
        "RG_scheme_closed": False,
        "primitive_C1_atoms_emitted": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B26_TwoEdgePromotionContract_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "two_edge_contract_built": True,
        "exclusivity_theorem_proved": True,
        "internal_lambda_12_closed_preserved": True,
        "u_dyn_source_derived_preserved": True,
        "K_phys_or_f_ab_closed": False,
        "mu_match_closed": False,
        "RG_scheme_closed": False,
        "primitive_C1_atoms_emitted": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B26 Two Edge Promotion Contract v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B26-PHYSICAL-GAUGE-ANCHOR-OR-C1-ATOMS`

## What B26 Proves

With `u_dyn=1`, `lambda_12_internal={b25["internal_lambda_12_value"]}`, and
`Delta_G12_internal={b25_physical["conditional_interface"]["closed_internal_weak_split"]["Delta_G12"]}`,
the remaining physical weak-angle promotion problem has two source-admissible
edges:

```text
1. gauge-kinetic/RG edge:
   emit K_phys or f_ab, mu_match, RG/threshold scheme, and Delta_a^sel

2. primitive-C1 edge:
   emit selected bases, 24 primitive C1 atom matrices, and b/homogeneous-zero leaves
```

The optional `u_phys` lane remains a B23-style universal-parameter lane only:
declared once, reused unchanged, and never tuned per observable.

## Guardrail

Measured `sin^2(theta_W)`, `alpha`, masses, CKM, and PMNS are replay/check data
only. They cannot choose `K_phys`, `mu_match`, the RG scheme, or primitive C1
atoms.

## Next

`CONST-EW-02 / WEAK-MIXING / B27-EXECUTE-GAUGEKINETIC-OR-C1-EDGE`
"""

    for path, payload in [
        (GAUGE, gauge_contract),
        (C1, c1_contract),
        (SYNTHESIS, synthesis),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
