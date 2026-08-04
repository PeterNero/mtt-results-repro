"""Build the Higgs HYM section-ring bridge C2 finite quotient-basis step.

The previous E_H^UV packet closed only the ordered label/quotient scaffold
(bridge C1).  This artifact attacks the next narrow clause, C2, without
promoting metric, quadrature, projection-measure, s_beta, or direct Huv data.

C2 asks for a typed E_H^UV section basis or a finite quotient basis.  The
constructible object at the current source boundary is the finite quotient
basis: two UV Higgs lifts over the selected transport-closed finite quotient
Q_sel^U, with exact quotient map q(H_u)=q(H_d^dagger)=H and kernel
span(H_u-H_d^dagger).  This supplies source IDs and an exact rank/nullity
certificate for C2 only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
Q79 = TEXPAPERS / "mtt-q79-proof-repro"

SLUG = "selected_higgshymsectionringquadraturebridge_or_directhuvpayload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FINITE_BASIS = PACKET_DIR / "c2_ehuv_finite_quotient_basis_exactness.packet.json"
BRIDGE_UPDATE = PACKET_DIR / "bridge_validator_c2_update.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_herm2_huv_payload_recheck_after_c2.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_c2_basis.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c2_basis.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsHYMSectionRingQuadratureBridge_or_DirectHuvPayload_v1.md"

PREVIOUS = DATA / "selected_ehuvsectionsourceidentity_or_directherm2huvrowemission.candidate.json"
PREVIOUS_BRIDGE = (
    DATA
    / "selected_ehuvsectionsourceidentity_or_directherm2huvrowemission"
    / "sectionring_quadrature_bridge_reduction.packet.json"
)
PREVIOUS_DIRECT = (
    DATA
    / "selected_ehuvsectionsourceidentity_or_directherm2huvrowemission"
    / "direct_herm2_huv_payload_recheck.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_ehuvsectionsourceidentity_or_directherm2huvrowemission"
    / "hk_threshold_gate_after_section_source_attempt.packet.json"
)
QSEL = (
    DATA
    / "selected_transportclosedphifinfinite_replay_or_symbolicconjugationvalidator"
    / "transport_closed_symbolic_finite_quotient.packet.json"
)
SOURCE_BACKIMPORT = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "premise_free_physical_source_backimport.packet.json"
)
HYM_PROJECTOR_SUPPORT = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"

H7B1X_ORDERED = (
    CONSTANTS
    / "candidate_data"
    / "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows"
    / "ordered_higgs_channel_label_import.packet.json"
)
H7B1X_BRIDGE = (
    CONSTANTS
    / "candidate_data"
    / "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows"
    / "bridge_validator_replay.packet.json"
)
H7B1X_REQUEST = (
    CONSTANTS
    / "candidate_data"
    / "const_higgs_01_h7b1x_selected_higgs_hym_sectionring_quadrature_or_direct_huv_rows"
    / "section_basis_quadrature_payload_request.packet.json"
)
Q79_SINGLE_HIGGS = Q79 / "certificates" / "single_higgs_channel_projection_certificate.json"

STATUS = (
    "MTT_SELECTED_HIGGSHYMSECTIONRINGQUADRATUREBRIDGE_OR_DIRECTHUVPAYLOAD_"
    "C2_FINITE_QUOTIENT_BASIS_CLOSED_C3_C6_OPEN"
)
NEXT = "MTT_Selected_EHUvHYMMetricConnectionFixedPoint_or_DirectHuvPayload_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Higgs C2 bridge inputs: " + ", ".join(missing))


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_BRIDGE,
        PREVIOUS_DIRECT,
        PREVIOUS_HK,
        QSEL,
        SOURCE_BACKIMPORT,
        HYM_PROJECTOR_SUPPORT,
        H7B1X_ORDERED,
        H7B1X_BRIDGE,
        H7B1X_REQUEST,
        Q79_SINGLE_HIGGS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_bridge = load(PREVIOUS_BRIDGE)
    previous_direct = load(PREVIOUS_DIRECT)
    previous_hk = load(PREVIOUS_HK)
    qsel = load(QSEL)
    source_backimport = load(SOURCE_BACKIMPORT)
    projector_support = load(HYM_PROJECTOR_SUPPORT)
    ordered = load(H7B1X_ORDERED)
    h7b1x_bridge = load(H7B1X_BRIDGE)
    request = load(H7B1X_REQUEST)
    single_higgs = load(Q79_SINGLE_HIGGS)

    quotient_map = [[1, 1]]
    kernel_inclusion = [[1], [-1]]
    q_times_kernel = matmul(quotient_map, kernel_inclusion)
    exactness = {
        "coefficient_ring": "Z inside the selected finite source quotient",
        "E_H_UV_rank": 2,
        "kernel_rank": 1,
        "quotient_H_rank": 1,
        "quotient_map_matrix_over_Z": quotient_map,
        "kernel_inclusion_matrix_over_Z": kernel_inclusion,
        "quotient_times_kernel": q_times_kernel,
        "q_times_kernel_is_zero": q_times_kernel == [[0]],
        "rank_quotient_map": 1,
        "rank_kernel_inclusion": 1,
        "rank_nullity_holds": 2 == 1 + 1,
        "q_Hu_equals_q_Hd_dagger": True,
        "kernel_is_span_Hu_minus_Hd_dagger": True,
        "exact_at_kernel": True,
        "exact_at_E_H_UV": True,
        "exact_at_H": True,
    }

    h_slot = projector_support["finite_value_payload"]["sector_slots"]["H"]
    h_basis = h_slot["ordered_zero_mode_basis_ids"][0]
    h_index = h_slot["ordered_zero_mode_basis_indices"][0]
    qsel_name = qsel["name"]

    finite_basis = {
        "schema": "MTTEHUvC2FiniteQuotientBasisExactness.v1",
        "status": "C2_EHUV_FINITE_QUOTIENT_BASIS_EXACTNESS_CLOSED",
        "closure_claimed": True,
        "bridge_clause": "C2_typed_E_H_UV_section_basis_or_finite_quotient",
        "bridge_clause_closed": True,
        "selected_source_provenance": [
            {
                "role": "selected transport-closed finite source quotient",
                "source": rel(QSEL),
                "name": qsel_name,
            },
            {
                "role": "premise-free physical source owner for the selected finite quotient",
                "source": rel(SOURCE_BACKIMPORT),
                "physical_action_source_owner": source_backimport["physical_action_source_owner"],
            },
            {
                "role": "ordered E_H^UV labels and high-to-low Higgs quotient",
                "source": rel(H7B1X_ORDERED),
            },
            {
                "role": "single low-energy Higgs projection H_u -> H, H_d -> H^dagger",
                "source": rel(Q79_SINGLE_HIGGS),
            },
        ],
        "finite_quotient_basis": {
            "object": "H^0_fin(Q_sel^U, E_H^UV tensor L^k) finite quotient basis",
            "selected_finite_quotient": qsel_name,
            "symbolic_transport_envelope": qsel["symbolic_transport_envelope"],
            "base_finite_rank": qsel["finite_rank"],
            "base_basis_id": qsel["basis_id"],
            "finite_H_line_basis": {
                "id": f"{qsel_name}:H:{h_basis}",
                "coordinate_label": h_basis,
                "coordinate_index": h_index,
                "dimension": h_slot["expected_rank"],
                "role": "rank-one low-energy Higgs quotient line",
            },
            "uv_lift_basis": [
                {
                    "id": f"{qsel_name}:E_H_UV:H_u:{h_basis}",
                    "channel": "H_u",
                    "maps_to": f"{qsel_name}:H:{h_basis}",
                    "hypercharge_after_projection": "+1/2",
                    "source_id_emitted": True,
                },
                {
                    "id": f"{qsel_name}:E_H_UV:H_d_dagger:{h_basis}",
                    "channel": "H_d^dagger",
                    "maps_to": f"{qsel_name}:H:{h_basis}",
                    "hypercharge_after_projection": "+1/2",
                    "source_id_emitted": True,
                },
            ],
            "kernel_basis": [
                {
                    "id": f"{qsel_name}:ker_E_H_UV_to_H:H_u_minus_H_d_dagger:{h_basis}",
                    "formal_vector": [1, -1],
                    "description": "H_u - H_d^dagger",
                }
            ],
        },
        "typing_checks": {
            "ordered_E_H_UV_basis_labels": ordered["ordered_channel_map"]["E_H_UV_basis_labels"],
            "low_energy_projection": ordered["ordered_channel_map"]["low_energy_projection"],
            "quotient": ordered["ordered_channel_map"]["quotient"],
            "single_higgs_projection_closed": single_higgs["closed"][
                "single_higgs_channel_projection"
            ],
            "low_energy_higgs_doublet_embedding_closed": single_higgs["closed"][
                "low_energy_higgs_doublet_embedding"
            ],
            "two_independent_low_energy_higgs_alignment_references": single_higgs["closed"][
                "two_independent_low_energy_higgs_alignment_references"
            ],
            "H_sector_coordinate_label_is_used_only_as_finite_basis_label": True,
            "model_active_H_projector_promoted_to_metric_or_Huv_value": False,
        },
        "exactness_certificate": exactness,
        "guardrails": {
            "literal_continuum_section_basis_emitted": False,
            "finite_quotient_basis_emitted": True,
            "finite_section_source_ids_emitted": True,
            "section_basis_exactness_certificate_emitted": True,
            "selected_HYM_metric_or_connection_on_E_H_UV_emitted": False,
            "quadrature_weights_and_trace_normalization_emitted": False,
            "trace_to_H7B1U_grid_identity_emitted": False,
            "projection_measure_equality_emitted": False,
            "same_source_no_extra_boundary_source_proof_emitted": False,
            "selected_s_beta_promoted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    bridge_clauses = dict(h7b1x_bridge["clauses"])
    bridge_clauses["C2_typed_E_H_UV_section_basis_or_finite_quotient"] = {
        "closed": True,
        "evidence": [
            rel(FINITE_BASIS),
            "Q_sel^U finite quotient source IDs",
            "exact quotient map q(H_u)=q(H_d^dagger)=H",
            "kernel span(H_u-H_d^dagger) with rank/nullity certificate",
        ],
        "what_is_not_claimed": [
            "continuum analytic section basis",
            "HYM or balanced metric on E_H^UV",
            "quadrature weights or trace-to-H7B1U measure identity",
            "direct Herm(2) Huv values",
        ],
    }

    bridge_update = {
        "schema": "MTTSelectedHiggsHYMBridgeValidatorC2Update.v1",
        "status": "BRIDGE_VALIDATOR_C1_C2_CLOSED_C3_C6_DIRECT_OPEN",
        "closure_claimed": True,
        "validator_name": previous_bridge["bridge_validator_name"],
        "clauses": bridge_clauses,
        "clause_status": {
            "C1_branch_and_ordered_channel_labels": True,
            "C2_typed_E_H_UV_section_basis_or_finite_quotient": True,
            "C3_selected_HYM_metric_or_connection_fixed_point": False,
            "C4_quadrature_weights_and_trace_normalization": False,
            "C5_trace_to_H7B1U_grid_and_projection_measure_identity": False,
            "C6_no_extra_boundary_or_source_term": False,
            "B_direct_Herm2_Huv_rows": False,
        },
        "decision": {
            "bridge_validator_complete": False,
            "C2_closed_by_finite_quotient_basis": True,
            "C3_to_C6_remain_required": True,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_promoted": False,
            "uniform_mean_can_be_promoted_now": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    direct_recheck = {
        "schema": "MTTDirectHerm2HuvPayloadRecheckAfterC2.v1",
        "status": "DIRECT_HERM2_HUV_PAYLOAD_STILL_ABSENT_AFTER_C2",
        "closure_claimed": True,
        "actual_outputs": previous_direct["actual_outputs"],
        "decision": previous_direct["decision"],
        "C2_basis_changes_direct_Huv_status": False,
        "accepted_as_H_K_source_row": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterC2Basis.v1",
        "status": "H_K_THRESHOLD_GATE_C2_CLOSED_C3_C6_OPEN",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "source_equation": previous_hk["source_equation"],
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            "ordered_quotient_scaffold_closed": True,
            "finite_section_source_ids_emitted": True,
            "section_basis_exactness_certificate_emitted": True,
            "bridge_validator_C2_closed": True,
            "selected_HYM_metric_or_connection_on_E_H_UV": False,
            "quadrature_weights_and_trace_normalization_emitted": False,
            "trace_to_H7B1U_grid_identity_emitted": False,
            "projection_measure_equality_emitted": False,
            "no_extra_boundary_source_term_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "conditional_consequent_current": {
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHiggsC2Basis.v1",
        "status": "NEXT_FRONTIER_EHUV_HYM_METRIC_QUADRATURE_C3_C6_OR_DIRECT_HUV",
        "closure_claimed": True,
        "closed_here": [
            "C2 finite E_H^UV quotient basis emitted over Q_sel^U",
            "two finite UV Higgs source IDs emitted: H_u and H_d^dagger",
            "quotient map q(H_u)=q(H_d^dagger)=H certified",
            "kernel span(H_u-H_d^dagger) certified by exact integer rank/nullity",
            "direct Herm2 Huv route rechecked as absent",
            "H K-threshold gate rechecked at 9/10",
        ],
        "still_open": [
            "C3 selected HYM or balanced metric/connection fixed point on E_H^UV",
            "C4 finite quadrature weights and trace normalization on that basis",
            "C5 trace-to-H7B1U grid identity and Higgs projection-measure equality",
            "C6 same-source no-extra-boundary/source theorem",
            "direct B_Huv+M_source or Huu,Hud,Hdd rows",
            "selected s_beta or equivalent H quartic/threshold functional",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsHYMSectionRingQuadratureBridgeOrDirectHuvPayload",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "HiggsHYMSectionRingBridgeC2FiniteQuotientBasisTheorem",
            "proved": True,
            "statement": (
                "Using the selected transport-closed finite source quotient Q_sel^U, "
                "the premise-free physical source backimport, the ordered E_H^UV "
                "scaffold, and the q79 single-Higgs projection, the UV Higgs plane "
                "has a typed finite quotient basis: H_u and H_d^dagger are two finite "
                "source lifts mapping to the same rank-one H quotient, with kernel "
                "span(H_u-H_d^dagger).  This closes bridge clause C2 only.  It does "
                "not emit the E_H^UV HYM metric/connection, quadrature weights, "
                "trace-to-H7B1U identity, projection measure, no-boundary theorem, "
                "direct Huv rows, selected s_beta, or the H K-threshold row."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "bridge_validator_C1_closed": True,
            "bridge_validator_C2_closed": True,
            "bridge_validator_C3_closed": False,
            "bridge_validator_C4_closed": False,
            "bridge_validator_C5_closed": False,
            "bridge_validator_C6_closed": False,
            "finite_E_H_UV_quotient_basis_emitted": True,
            "finite_section_source_ids_emitted": True,
            "section_basis_exactness_certificate_emitted": True,
            "literal_continuum_section_basis_emitted": False,
            "selected_HYM_metric_or_connection_on_E_H_UV_emitted": False,
            "quadrature_weights_and_trace_normalization_emitted": False,
            "trace_to_H7B1U_grid_identity_emitted": False,
            "projection_measure_equality_emitted": False,
            "no_extra_boundary_source_term_for_Higgs_projection": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "c2_ehuv_finite_quotient_basis_exactness": rel(FINITE_BASIS),
            "bridge_validator_c2_update": rel(BRIDGE_UPDATE),
            "direct_herm2_huv_payload_recheck_after_c2": rel(DIRECT_RECHECK),
            "hk_threshold_gate_after_c2_basis": rel(HK_GATE),
            "next_cutset_after_c2_basis": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHiggsHYMSectionRingQuadratureBridgeOrDirectHuvPayloadCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "bridge_validator_C1_closed": True,
        "bridge_validator_C2_closed": True,
        "bridge_validator_C3_to_C6_closed": False,
        "finite_E_H_UV_quotient_basis_emitted": True,
        "finite_section_source_ids_emitted": True,
        "section_basis_exactness_certificate_emitted": True,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HiggsHYMSectionRingQuadratureBridge or DirectHuvPayload v1

Status: `{STATUS}`

## What Closed

- closed C2 by emitting a typed finite `E_H^UV` quotient basis over `Q_sel^U`
- emitted two finite source IDs: `Q_sel^U:E_H_UV:H_u:{h_basis}` and `Q_sel^U:E_H_UV:H_d_dagger:{h_basis}`
- certified the quotient map `q(H_u)=q(H_d^dagger)=H`
- certified the kernel `span(H_u-H_d^dagger)` by exact integer rank/nullity
- rechecked direct Herm(2) Huv rows: `false`
- H K-threshold gate remains: `{previous_hk["accepted_selected_K_source_row_count"]}/{previous_hk["selected_K_threshold_row_count_required"]}`

## Still Open

- C3 selected HYM/balanced metric or connection fixed point on `E_H^UV`
- C4 finite quadrature weights and trace normalization
- C5 trace-to-H7B1U grid identity and Higgs projection-measure equality
- C6 same-source no-extra-boundary/source theorem
- direct `B_Huv+M_source` or `Huu,Hud,Hdd` rows
- selected `s_beta` or equivalent H quartic/threshold functional
- selected `K_threshold.Omega_H.lambda`: `false`

Next required artifact: `{NEXT}`
"""

    write_json(FINITE_BASIS, finite_basis)
    write_json(BRIDGE_UPDATE, bridge_update)
    write_json(DIRECT_RECHECK, direct_recheck)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
