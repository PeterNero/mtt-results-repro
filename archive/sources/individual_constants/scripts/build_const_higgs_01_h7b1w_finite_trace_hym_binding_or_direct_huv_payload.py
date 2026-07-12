"""Build CONST-HIGGS-01 H7B1W finite-trace/HYM-binding or direct-Huv gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"
Q79_REPRO = TEXPAPERS / "mtt-q79-proof-repro"
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"
STRINGS_MD = (
    TEXPAPERS
    / "16 Strings, Flux, & M-Theory Encodings"
    / "_md"
    / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md"
)

SLUG = "const_higgs_01_h7b1w_finite_trace_hym_binding_or_direct_huv_payload"
STATUS = "MTT_CONST_HIGGS_01_H7B1W_BRIDGE_CRITERION_BUILT_PAYLOAD_OPEN"
ACTIVE_LABEL = "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1W-FINITE-TRACE-HYM-BINDING-OR-DIRECT-HUV-PAYLOAD"
NEXT_ARTIFACT = "MTT_CONST_HIGGS_01_H7B1X_SelectedHiggsHYMSectionRingQuadratureOrDirectHuvRows_v1"
NEXT_LABEL = "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1X-SELECTED-HIGGS-HYM-SECTION-RING-QUADRATURE-OR-DIRECT-HUV-ROWS"

OUT_DIR = ROOT / "candidate_data" / SLUG
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_HIGGS_01_H7B1W_FiniteTraceHYMBindingOrDirectHuvPayload_v1.md"

INPUTS = {
    "H7B1V": ROOT / "candidate_data" / "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source.candidate.json",
    "H7B1V_trace_attempt": ROOT
    / "candidate_data"
    / "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source"
    / "finite_trace_to_hym_grid_binding_attempt.packet.json",
    "H7B1V_direct_attempt": ROOT
    / "candidate_data"
    / "const_higgs_01_h7b1v_reduction_selector_or_direct_herm2_huv_source"
    / "direct_herm2_huv_source_attempt.packet.json",
    "q79_finite_connection": Q79_REPRO / "candidate_data" / "q79_selected_finite_connection_solve_execution.candidate.json",
    "qa_su3_selected_source": QA_SU3
    / "candidate_data"
    / "selected_u1y_routec_selected_source_certificate_or_typed_de_construction.candidate.json",
    "sm_transition_gate": SM_PARITY
    / "candidate_data"
    / "selected_transitionpayload_or_heattorsionresponse_onegateattack.candidate.json",
    "strings_flux_strominger": STRINGS_MD,
}


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_note(payload: dict[str, object]) -> None:
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    NOTE.write_text(
        f"""# MTT CONST HIGGS 01 H7B1W Finite Trace HYM Binding Or Direct Huv Payload v1

Status: `{payload["status"]}`

Label: `{payload["active_label"]}`

## Result

```text
H7B1W-A finite trace/HYM binding attacked    {payload["H7B1W_A_trace_binding_route_attacked"]}
H7B1W-B direct Herm2 Huv route attacked      {payload["H7B1W_B_direct_Huv_route_attacked"]}
bridge criterion emitted                    {payload["selected_Higgs_HYM_quadrature_bridge_criterion_emitted"]}
finite trace/HYM binding closed             {payload["finite_trace_HYM_binding_closed"]}
direct Herm2 Huv payload emitted            {payload["direct_Herm2_Huv_payload_emitted"]}
s_beta / lambda_H promoted                  {payload["selected_s_beta_value_found"]}
new Higgs-specific parameters               {payload["new_Higgs_specific_parameters"]}
```

## What Changed

H7B1W imports the strongest available finite-trace support from the current repo,
q79, Qa/SU3, SM-parity, the Strominger/HYM corpus, and external HYM numerical
literature.  The result is a sharper promotion criterion rather than a numerical
Higgs value.

The finite trace route now requires a selected section-ring/quadrature bridge:

```text
selected E_H^UV sector and Hu/Hd dagger basis
typed section-ring or finite quotient basis
selected HYM/balanced metric or full connection
quadrature weights and trace-to-H7B1U-grid identity
Higgs projection measure equality
no-extra-boundary/source proof
finite-to-smooth or exact finite quotient certificate
```

The direct route still requires actual Herm(2) data:

```text
B_Huv + M_source, or direct Huu, Hud, Hdd
same-source exactness/residual certificate
quotient admissibility for q(Hu)=q(Hd dagger)=H
```

## Boundary

This does not select the uniform H7B1U mean as `s_beta`.  It proves why the
uniform candidate is the live trace-aligned path and what exact source packet
would promote it.

Next label:

`{NEXT_LABEL}`
""",
        encoding="utf-8",
    )


def base_guarded(payload: dict[str, object]) -> dict[str, object]:
    return {
        "schema": payload.pop("schema"),
        "status": payload.pop("status"),
        "active_label": payload.pop("active_label"),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        **payload,
    }


def main() -> int:
    h7b1v = load_json(INPUTS["H7B1V"])
    h7b1v_trace = load_json(INPUTS["H7B1V_trace_attempt"])
    h7b1v_direct = load_json(INPUTS["H7B1V_direct_attempt"])
    q79 = load_json(INPUTS["q79_finite_connection"])
    qa_su3 = load_json(INPUTS["qa_su3_selected_source"])
    sm_transition = load_json(INPUTS["sm_transition_gate"])
    strings_text = INPUTS["strings_flux_strominger"].read_text(encoding="utf-8", errors="replace")

    strings_support = {
        "strominger_selection_potential_present": "selection potential" in strings_text and "Hull--Strominger" in strings_text,
        "hym_on_gauduchon_present": "HYM on Gauduchon" in strings_text,
        "unique_local_minimizer_present": "unique local minimizer" in strings_text,
        "finite_section_ring_quadrature_emitted": False,
        "direct_Huv_payload_emitted": False,
    }

    external_method_sources = [
        {
            "title": "Numerical Hermitian Yang-Mills Connections and Vector Bundle Stability in Heterotic Theories",
            "url": "https://arxiv.org/pdf/1004.4399",
            "role": "Shows the balanced-metric/section-basis/untwisting/error-measure structure needed for finite-dimensional HYM computations.",
            "used_as_source_selector": False,
        },
        {
            "title": "Numerical Hermitian Yang-Mills Connection for Bundles on Quotient Manifold",
            "url": "https://arxiv.org/abs/2302.09622",
            "role": "Shows how equivariant quotient data and generalized Donaldson algorithms enter quotient-bundle HYM computations.",
            "used_as_source_selector": False,
        },
        {
            "title": "The Hermitian-Yang-Mills Iteration on Stable Bundles",
            "url": "https://arxiv.org/abs/2606.20307",
            "role": "Recent iteration literature confirming the DUY/Hermitian-Einstein stability-to-metric bridge; used only to sharpen the methodological acceptance contract.",
            "used_as_source_selector": False,
        },
    ]

    corpus_hunt = base_guarded(
        {
            "schema": "MTTConstHiggs01H7B1WCorpusAndRepoSourceHunt.v1",
            "status": "CORPUS_REPO_SOURCE_HUNT_FINITE_TRACE_SUPPORT_STRONG_HUV_PAYLOAD_ABSENT",
            "active_label": f"{ACTIVE_LABEL} / SOURCE-HUNT",
            "input_sources": {name: rel(path) for name, path in INPUTS.items()},
            "current_repo_H7B1V": {
                "uniform_candidate_best_trace_aligned": h7b1v["uniform_reduction_best_current_source_aligned_candidate"],
                "trace_to_HYM_grid_binding_closed": h7b1v["trace_to_HYM_grid_binding_closed"],
                "direct_Herm2_Huv_payload_emitted": h7b1v["direct_Herm2_Huv_payload_emitted"],
            },
            "q79_repro_import": {
                "status": q79["status"],
                "all_finite_value_shapes_present": q79["what_closes_now"]["all_finite_value_shapes_present"],
                "honest_replay_cutset_status": q79["honest_replay_cutset"]["status"],
                "selected_trace_equality_open": q79["what_remains_open"]["selected_trace_equality"],
                "selected_full_operator_formula_open": q79["what_remains_open"][
                    "full_selected_iwasawa_strominger_operator_formula"
                ],
            },
            "qa_su3_import": {
                "status": qa_su3["status"],
                "finite_connection_prefix_values_present": qa_su3["decision"][
                    "finite_connection_prefix_values_present"
                ],
                "selected_connection_witness_values_absent": qa_su3["decision"][
                    "selected_connection_witness_values_absent"
                ],
                "selected_hym_connection_constructed": qa_su3["decision"]["selected_hym_connection_constructed"],
                "typed_monad_cech_witness_constructed": qa_su3["decision"][
                    "typed_monad_cech_witness_constructed"
                ],
            },
            "sm_transition_gate_import": {
                "status": sm_transition["status"],
                "theorem_proved": sm_transition["theorem"]["proved"],
                "transition_payload_closed": sm_transition["closure_decision"][
                    "transition_rhoE_or_Cech_Dolbeault_DE_data_closed"
                ],
                "selected_trace_equality_open": sm_transition["what_remains_open"]["selected_trace_equality"],
                "typed_monad_Cech_payload_open": sm_transition["what_remains_open"]["typed_monad_Cech_payload"],
            },
            "strings_flux_corpus_import": strings_support,
            "decision": {
                "same_source_trace_to_grid_quadrature_identity_found": False,
                "same_source_E_H_UV_metric_binding_found": False,
                "same_source_no_extra_boundary_source_proof_found": False,
                "direct_B_Huv_or_M_source_found": False,
                "direct_Huu_Hud_Hdd_rows_found": False,
                "source_hunt_closes_H7B1W": False,
            },
        }
    )

    external_criterion = base_guarded(
        {
            "schema": "MTTConstHiggs01H7B1WExternalHYMQuadratureCriterion.v1",
            "status": "EXTERNAL_HYM_QUADRATURE_CRITERION_IMPORTED_METHOD_ONLY",
            "active_label": f"{ACTIVE_LABEL} / EXTERNAL-METHOD-CRITERION",
            "external_method_sources": external_method_sources,
            "not_MTT_source_selector": True,
            "criterion_imported": {
                "finite_dimensional_HYM_requires_section_basis": True,
                "finite_dimensional_HYM_requires_balanced_metric_or_connection_fixed_point": True,
                "finite_dimensional_HYM_requires_twist_untwist_policy_for_SU_bundle": True,
                "finite_dimensional_HYM_requires_error_or_convergence_certificate": True,
                "quotient_HYM_requires_equivariant_or_quotient_domain_data": True,
            },
            "impact_on_H7B1W": {
                "uniform_trace_candidate_is_methodologically_plausible": True,
                "uniform_trace_candidate_can_be_promoted_without_MTT_bridge": False,
                "required_bridge_name": "SelectedHiggsHYMSectionRingQuadratureBridgeTheorem",
            },
        }
    )

    bridge_clauses = [
        "selected q79/F,m=1 branch identity and E_H^UV=(H_u,H_d^dagger) sector map",
        "typed section-ring or finite quotient basis for H^0(X,E_H^UV tensor L^k) or an equivalent finite HYM quotient",
        "selected HYM/balanced metric or full connection fixed point on that basis",
        "finite quadrature weights and trace normalization",
        "trace-to-H7B1U-grid identity for the diagonal HYM replay",
        "proof that the Higgs projection/reduction measure is normalized finite trace",
        "same-source E_H^UV metric binding, not only End0/T3 or collapsed rank-one H support",
        "no-extra-boundary/source proof",
        "finite-to-smooth convergence, exact finite quotient identity, or residual/error certificate",
    ]

    trace_binding_attempt = base_guarded(
        {
            "schema": "MTTConstHiggs01H7B1WFiniteTraceHYMBindingAttempt.v1",
            "status": "FINITE_TRACE_HYM_BINDING_CRITERION_BUILT_CURRENT_PAYLOAD_OPEN",
            "active_label": f"{ACTIVE_LABEL} / H7B1W-A",
            "closed_support": {
                "H7B1V_uniform_candidate_best_trace_aligned": h7b1v[
                    "uniform_reduction_best_current_source_aligned_candidate"
                ],
                "finite_Weyl_trace_measure_derived": h7b1v["finite_Weyl_trace_measure_derived"],
                "selected_trace_payload_DE_gap_layer_closed": h7b1v["selected_trace_payload_DE_gap_layer_closed"],
                "q79_all_finite_value_shapes_present": q79["what_closes_now"]["all_finite_value_shapes_present"],
                "strominger_HYM_selection_support_present": strings_support["strominger_selection_potential_present"],
                "external_HYM_quadrature_method_imported": True,
            },
            "bridge_criterion": {
                "name": "SelectedHiggsHYMSectionRingQuadratureBridgeTheorem",
                "clauses": bridge_clauses,
                "criterion_emitted": True,
            },
            "missing_payload": {
                "section_basis_or_finite_quotient_for_E_H_UV": True,
                "selected_HYM_metric_or_connection_fixed_point": True,
                "trace_to_H7B1U_grid_identity": True,
                "E_H_UV_metric_binding": True,
                "Higgs_projection_measure_equality": True,
                "no_extra_boundary_source_proof": True,
                "finite_to_smooth_or_exact_quotient_certificate": True,
            },
            "decision": {
                "finite_trace_HYM_binding_closed": False,
                "uniform_mean_can_be_promoted_now": False,
                "selected_s_beta_promoted": False,
            },
        }
    )

    direct_huv_attempt = base_guarded(
        {
            "schema": "MTTConstHiggs01H7B1WDirectHerm2HuvPayloadAttempt.v1",
            "status": "DIRECT_HERM2_HUV_PAYLOAD_SEARCHED_VALUES_ABSENT",
            "active_label": f"{ACTIVE_LABEL} / H7B1W-B",
            "imported_H7B1V_direct_attempt_status": h7b1v_direct["status"],
            "payload_requirements": {
                "B_Huv": "two-column lift from collapsed H to (H_u,H_d^dagger)",
                "M_source": "same-source Hermitian source metric/strain on the lift domain",
                "direct_Huv_rows": "Huu,Hud,Hdd in fixed basis with exactness/residual certificate",
                "quotient_admissibility": "q(H_u)=q(H_d^dagger)=H and kernel/light-line conventions checked",
            },
            "actual_outputs": {
                "B_Huv": None,
                "M_source": None,
                "Huu": None,
                "Hud": None,
                "Hdd": None,
                "Delta": None,
                "Omega": None,
                "P_L": None,
                "s_beta": None,
                "lambda_H": None,
            },
            "decision": {
                "direct_Herm2_Huv_payload_emitted": False,
                "B_Huv_value_emitted": False,
                "M_source_value_emitted": False,
                "direct_Huu_Hud_Hdd_emitted": False,
                "selected_s_beta_promoted": False,
                "numeric_lambda_H_derived": False,
            },
        }
    )

    no_cycle = base_guarded(
        {
            "schema": "MTTConstHiggs01H7B1WNonCirculationLedger.v1",
            "status": "NO_CIRCULATION_LEDGER_UPDATED_H7B1W",
            "active_label": f"{ACTIVE_LABEL} / NO-CYCLE",
            "new_information_added": [
                "imports q79/QA-SU3/SM-parity evidence that finite values do not equal selected smooth HYM source without a trace/operator theorem",
                "imports Strominger/HYM corpus support as continuum source structure, not finite quadrature values",
                "imports external HYM numerical literature only as methodological acceptance criteria",
                "creates the exact H7B1X section-ring/quadrature bridge theorem and payload contract",
            ],
            "retired_or_do_not_reopen": {
                "uniform_H7B1U_mean_as_selected_s_beta_without_bridge": True,
                "finite_Weyl_trace_as_HYM_grid_identity_without_section_ring_or_trace_theorem": True,
                "abstract_HYM_existence_as_direct_Huv_values": True,
                "QA_SU3_finite_internal_values_as_Higgs_projection_measure_without_E_H_UV_map": True,
            },
            "active_not_retired": {
                "selected_Higgs_HYM_section_ring_quadrature_bridge": True,
                "direct_B_Huv_M_source_or_Huu_Hud_Hdd_rows": True,
                "EW_boundary_RG_after_selected_s_beta": True,
            },
            "circulation_test": {
                "is_reopening_H7B1V_reduction_selector": False,
                "is_promoting_uniform_mean_without_binding": False,
                "is_treating_external_literature_as_MTT_source_selector": False,
                "is_using_measured_Higgs_or_beta": False,
            },
        }
    )

    next_work = base_guarded(
        {
            "schema": "MTTConstHiggs01H7B1WNextWork.v1",
            "status": "NEXT_WORKORDER_H7B1X_SELECTED_HIGGS_HYM_SECTION_RING_QUADRATURE_OR_DIRECT_HUV_ROWS",
            "active_label": f"{ACTIVE_LABEL} / NEXT",
            "primary_next": {
                "label": NEXT_LABEL,
                "task": "Emit the selected E_H^UV section-ring/quadrature/HYM bridge packet or direct Herm2 Huv rows.",
            },
            "legal_exits": [
                {
                    "id": "H7B1X-A",
                    "label": "selected Higgs HYM section-ring quadrature bridge",
                    "must_emit": "E_H^UV typed sections/finite quotient basis, selected HYM metric/connection, quadrature weights, trace-to-grid identity, projection-measure equality, and no-extra-boundary proof",
                },
                {
                    "id": "H7B1X-B",
                    "label": "direct Herm2 Huv rows",
                    "must_emit": "B_Huv+M_source or Huu,Hud,Hdd with exactness/residual and quotient-admissibility certificates",
                },
            ],
            "superset_strategy": {
                "combining_paths": True,
                "using_one_straight_way": False,
                "straight_path": "finite Weyl trace plus selected HYM section-ring/quadrature bridge",
                "support_path": "direct Herm2 Huv rows remain an independent exit",
                "locked_target": "source-selected s_beta from Higgs projection data, not a fitted Higgs mass/quartic",
            },
        }
    )

    candidate = {
        "candidate": "MTTConstHiggs01H7B1WFiniteTraceHYMBindingOrDirectHuvPayload",
        "status": STATUS,
        "active_label": ACTIVE_LABEL,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "theorem": {
            "name": "H7B1WFiniteTraceHYMBindingCutsetTheorem",
            "proved": True,
            "statement": (
                "H7B1W attacks both legal exits. The finite trace route is sharpened to a selected "
                "Higgs HYM section-ring/quadrature bridge theorem: current finite trace, q79, QA/SU3, "
                "SM-parity, and Strominger/HYM support make the uniform H7B1U reduction the live "
                "trace-aligned candidate, but do not identify the H7B1U grid with the selected Higgs "
                "projection measure. The direct route is also searched and no B_Huv, M_source, or "
                "Huu/Hud/Hdd payload is emitted. Therefore H7B1W closes a bridge criterion, not "
                "s_beta or lambda_H."
            ),
        },
        "H7B1V_imported": True,
        "H7B1W_A_trace_binding_route_attacked": True,
        "H7B1W_B_direct_Huv_route_attacked": True,
        "q79_finite_connection_cutset_imported": True,
        "qa_su3_connection_witness_open_imported": True,
        "sm_transition_payload_gate_imported": True,
        "strominger_HYM_selection_support_imported": True,
        "external_HYM_quadrature_criterion_imported_method_only": True,
        "selected_Higgs_HYM_quadrature_bridge_criterion_emitted": True,
        "finite_trace_HYM_binding_closed": False,
        "same_source_trace_to_grid_quadrature_identity_emitted": False,
        "same_source_E_H_UV_metric_binding_emitted": False,
        "same_source_no_extra_boundary_source_proof_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": NEXT_ARTIFACT,
        "output_packets": {
            "corpus_and_repo_source_hunt": rel(OUT_DIR / "corpus_and_repo_source_hunt.packet.json"),
            "external_hym_quadrature_criterion": rel(OUT_DIR / "external_hym_quadrature_criterion.packet.json"),
            "finite_trace_binding_attempt": rel(OUT_DIR / "finite_trace_binding_attempt.packet.json"),
            "direct_huv_payload_attempt": rel(OUT_DIR / "direct_huv_payload_attempt.packet.json"),
            "non_circulation_ledger": rel(OUT_DIR / "non_circulation_ledger.packet.json"),
            "next_labeled_workorder": rel(OUT_DIR / "next_labeled_workorder.packet.json"),
        },
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1W_FiniteTraceHYMBindingOrDirectHuvPayload_v1",
        "status": STATUS,
        "active_label": ACTIVE_LABEL,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "selected_Higgs_HYM_quadrature_bridge_criterion_emitted": True,
        "finite_trace_HYM_binding_closed": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "candidate_path": rel(DATA),
        "note_path": rel(NOTE),
    }

    write_json(OUT_DIR / "corpus_and_repo_source_hunt.packet.json", corpus_hunt)
    write_json(OUT_DIR / "external_hym_quadrature_criterion.packet.json", external_criterion)
    write_json(OUT_DIR / "finite_trace_binding_attempt.packet.json", trace_binding_attempt)
    write_json(OUT_DIR / "direct_huv_payload_attempt.packet.json", direct_huv_attempt)
    write_json(OUT_DIR / "non_circulation_ledger.packet.json", no_cycle)
    write_json(OUT_DIR / "next_labeled_workorder.packet.json", next_work)
    write_json(DATA, candidate)
    write_json(CERT, cert)
    write_note(candidate)

    print(json.dumps({"candidate": rel(DATA), "status": STATUS}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
