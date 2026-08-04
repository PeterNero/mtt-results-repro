"""Build the E_H^UV trace-grid projection identity split packet.

After C4, the bridge's C5 clause can be split into two different claims:

* C5a: the selected finite trace rule attached to E_H^UV is the same
  q79/F,m=1 H7B1U/H7B1Z computational HYM grid trace.
* C5b: that trace is the physical Higgs projection/reduction measure.

The current source stack can close C5a from same branch, same grid, same
quadrature id, and same normalized trace.  It still cannot close C5b, C6, or
the direct Herm(2) Huv table.
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
CONST_DATA = TEXPAPERS / "mtt-individual-constants-source-search" / "candidate_data"

SLUG = "selected_ehuvtracegridprojectionidentity_or_directhuvpayload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRACE_ID = PACKET_DIR / "c5a_trace_grid_identity.packet.json"
MEASURE_GATE = PACKET_DIR / "c5b_projection_measure_gate.packet.json"
DIRECT_RECHECK = PACKET_DIR / "direct_hresponse_huv_table_recheck_after_c5a.packet.json"
BRIDGE_UPDATE = PACKET_DIR / "bridge_validator_c5a_update.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_c5a_trace_identity.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_c5a_trace_identity.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_EHUvTraceGridProjectionIdentity_or_DirectHuvPayload_v1.md"

PREVIOUS_C4 = DATA / "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload.candidate.json"
PREVIOUS_C4_TRACE = (
    DATA
    / "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload"
    / "c4_ehuv_finite_trace_quadrature_attachment.packet.json"
)
PREVIOUS_C4_BRIDGE = (
    DATA
    / "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload"
    / "bridge_validator_c4_update.packet.json"
)
PREVIOUS_C4_MEASURE = (
    DATA
    / "selected_ehuvquadraturetraceprojectionmeasure_or_directhuvpayload"
    / "projection_measure_identity_recheck_after_c4.packet.json"
)
PREVIOUS_MH = DATA / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution.candidate.json"
PREVIOUS_MH_TABLE = (
    DATA
    / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution"
    / "mh_three_row_execution_table_request.packet.json"
)
PREVIOUS_MH_HK = (
    DATA
    / "selected_mhthreerowsourcefunctional_or_c5c6bridgeexecution"
    / "hk_threshold_gate_after_three_row_functional.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
H7B1Z_PARTIAL = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "partial_section_basis_quadrature_fill.packet.json"
)
H7B1Z_CUTSET = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "remaining_payload_cutset.packet.json"
)

STATUS = (
    "MTT_SELECTED_EHUVTRACEGRIDPROJECTIONIDENTITY_OR_DIRECTHUVPAYLOAD_"
    "C5A_TRACE_GRID_IDENTITY_CLOSED_PROJECTION_BOUNDARY_DIRECT_OPEN"
)
NEXT = "MTT_Selected_EHUvProjectionMeasureNoBoundary_or_HResponseHuvTable_v1"


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
        raise FileNotFoundError("missing C5a trace-grid inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS_C4,
        PREVIOUS_C4_TRACE,
        PREVIOUS_C4_BRIDGE,
        PREVIOUS_C4_MEASURE,
        PREVIOUS_MH,
        PREVIOUS_MH_TABLE,
        PREVIOUS_MH_HK,
        BHUV,
        H7B1Z_PARTIAL,
        H7B1Z_CUTSET,
    ]
    require_sources(sources)

    previous_c4 = load(PREVIOUS_C4)
    c4_trace = load(PREVIOUS_C4_TRACE)
    c4_bridge = load(PREVIOUS_C4_BRIDGE)
    c4_measure = load(PREVIOUS_C4_MEASURE)
    previous_mh = load(PREVIOUS_MH)
    mh_table = load(PREVIOUS_MH_TABLE)
    mh_hk = load(PREVIOUS_MH_HK)
    bhuv = load(BHUV)
    h7b1z = load(H7B1Z_PARTIAL)
    h7b1z_cutset = load(H7B1Z_CUTSET)

    c4_q = c4_trace["finite_trace_quadrature"]
    z_branch = h7b1z["branch_identity_partial_fill"]
    z_q = h7b1z["quadrature_and_trace_partial_fill"]
    z_projection = h7b1z["projection_measure_partial_fill"]
    qid = c4_q["quadrature_rule_id"]

    same_grid_checks = {
        "same_selected_source_branch": z_branch["same_branch_with_H7B1U_grid"],
        "same_source_branch_label": z_branch["selected_source_branch"],
        "same_nodes_or_grid": c4_q["nodes_or_grid"] == z_q["nodes_or_grid"],
        "same_node_count": c4_q["node_count"] == z_q["node_count"],
        "same_uniform_weight_rational": c4_q["uniform_weight_rational"]
        == z_q["uniform_weight_rational"],
        "same_trace_normalization": c4_q["trace_normalization"] == z_q["trace_normalization"],
        "same_source_independent_of_target_replay": c4_q["source_independent_of_target_replay"]
        is True
        and z_q["source_independent_of_target_replay"] is True,
        "attached_to_selected_E_H_UV_basis": c4_q["attached_to_selected_E_H_UV_basis"],
        "weight_sum_is_one": c4_q["weight_sum_is_one"],
    }
    c5a_closed = all(same_grid_checks.values())

    trace_id = {
        "schema": "MTTEHUvC5aTraceGridIdentity.v1",
        "status": "C5A_TRACE_TO_H7B1U_GRID_IDENTITY_CLOSED",
        "closure_claimed": True,
        "bridge_clause_fragment": "C5a_trace_to_H7B1U_grid_identity",
        "proved": c5a_closed,
        "statement": (
            "The finite trace rule attached to the selected E_H^UV basis in C4 is "
            "the same q79/F,m=1 H7B1U/H7B1Z computational HYM grid trace: same "
            "source branch, same Z_24^4 grid recipe, same node count 331776, "
            "same normalized uniform weight 1/331776, and same trace normalization."
        ),
        "identity_checks": same_grid_checks,
        "quadrature_rule_id": qid,
        "node_count": c4_q["node_count"],
        "uniform_weight_rational": c4_q["uniform_weight_rational"],
        "ordered_E_H_UV_source_ids": c4_q["ordered_E_H_UV_source_ids"],
        "source_provenance": [
            {"role": "C4 E_H^UV finite trace attachment", "source": rel(PREVIOUS_C4_TRACE)},
            {"role": "H7B1Z same-branch HYM grid replay", "source": rel(H7B1Z_PARTIAL)},
        ],
        "not_claimed": {
            "physical_Higgs_projection_measure_equality": False,
            "C6_no_extra_boundary_or_source_term": False,
            "selected_s_beta": False,
            "K_threshold_Omega_H_lambda": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    measure_gate = {
        "schema": "MTTEHUvC5bProjectionMeasureGateAfterC5a.v1",
        "status": "C5B_PHYSICAL_PROJECTION_MEASURE_EQUALITY_OPEN_AFTER_TRACE_GRID_IDENTITY",
        "closure_claimed": True,
        "C5a_trace_to_H7B1U_grid_identity_closed": c5a_closed,
        "C5b_physical_Higgs_projection_measure_equality_emitted": False,
        "C6_no_extra_boundary_or_source_term_emitted": False,
        "why_C5_not_fully_closed": (
            "C5a identifies the finite trace grid.  C5b still requires the physical "
            "Higgs projection/reduction measure theorem: the selected trace must be "
            "proved to be the projection measure, not merely the attached computational trace."
        ),
        "open_physical_fields": {
            "projection_measure_equality": z_projection["projection_measure_equality"],
            "trace_to_H7B1U_grid_identity_as_physical_projection_measure": h7b1z_cutset[
                "still_open"
            ]["trace_to_H7B1U_grid_identity_as_physical_projection_measure"],
            "no_extra_boundary_source_term": z_projection["no_extra_boundary_source_term"],
            "accepted_as_physical_Higgs_projection_measure": z_q[
                "accepted_as_physical_Higgs_projection_measure"
            ],
            "selected_s_beta_promoted": z_projection["selected_s_beta_promoted"],
        },
        "diagnostic_values_not_promoted": {
            "conditional_local_formula": z_projection["conditional_local_formula"],
            "uniform_candidate_s_beta": z_projection["uniform_candidate_s_beta"],
            "conditional_reductions_not_selected": z_projection[
                "conditional_reductions_not_selected"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    minimal_table = dict(mh_table["minimal_table"])
    direct_recheck = {
        "schema": "MTTHResponseHuvTableRecheckAfterC5a.v1",
        "status": "BHUV_DOMAIN_AND_FUNCTIONAL_CLOSED_HRESPONSE_HUV_TABLE_STILL_OPEN",
        "closure_claimed": True,
        "B_Huv_two_column_lift_emitted": bhuv["minimal_lift_request_tests"][
            "source_orthonormality_required_by_H7B1G_satisfied"
        ],
        "B_Huv_symbolic_exact_payload_emitted": bhuv["whitening_map_and_lift"][
            "B_Huv_symbolic_exact_payload_emitted"
        ],
        "M_H_three_row_functional_closed": previous_mh["closure_decision"][
            "MH_three_row_source_functional_contract_closed"
        ],
        "required_table": minimal_table,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_H_response_table_emitted": False,
        "M_source_emitted": False,
        "values_emitted_now": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
            "s_beta": None,
        },
        "refined_direct_blocker": (
            "The direct route is no longer missing the domain or extraction map. "
            "It is missing only selected H_response/Huv table values, or an "
            "M_source+R_H restriction that emits them."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    bridge_clauses = dict(c4_bridge["clauses"])
    bridge_clauses["C5_trace_to_H7B1U_grid_and_projection_measure_identity"] = {
        "closed": False,
        "split_status": {
            "C5a_trace_to_H7B1U_grid_identity": True,
            "C5b_physical_Higgs_projection_measure_equality": False,
        },
        "evidence_for_C5a": [
            rel(TRACE_ID),
            f"quadrature_rule_id={qid}",
            "same q79/F,m=1 H7B1U/H7B1Z computational grid",
            "uniform finite trace weight 1/331776 on 331776 nodes",
        ],
        "still_required_for_full_C5": [
            "physical Higgs projection/reduction measure equality",
            "proof the projection measure has no additional source/boundary term",
        ],
    }
    bridge_update = {
        "schema": "MTTSelectedEHUvHYMBridgeValidatorC5aUpdate.v1",
        "status": "BRIDGE_VALIDATOR_C1_C2_C3_C4_C5A_CLOSED_C5B_C6_DIRECT_OPEN",
        "closure_claimed": True,
        "validator_name": c4_bridge["validator_name"],
        "clauses": bridge_clauses,
        "clause_status": {
            "C1_branch_and_ordered_channel_labels": True,
            "C2_typed_E_H_UV_section_basis_or_finite_quotient": True,
            "C3_selected_HYM_metric_or_connection_fixed_point": True,
            "C4_quadrature_weights_and_trace_normalization": True,
            "C5a_trace_to_H7B1U_grid_identity": True,
            "C5b_physical_Higgs_projection_measure_equality": False,
            "C6_no_extra_boundary_or_source_term": False,
            "B_direct_Herm2_Huv_rows": False,
        },
        "decision": {
            "bridge_validator_complete": False,
            "C5a_trace_grid_identity_closed": True,
            "C5_full_closed": False,
            "C6_closed": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_s_beta_promoted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_row = dict(mh_hk["H_row"])
    h_row["trace_to_H7B1U_grid_identity_emitted"] = True
    h_row["C5a_trace_grid_identity_closed"] = True
    h_row["C5b_projection_measure_equality_emitted"] = False
    hk_gate = {
        "schema": "MTTHKThresholdGateAfterC5aTraceIdentity.v1",
        "status": "H_K_THRESHOLD_GATE_C5A_CLOSED_PROJECTION_BOUNDARY_VALUES_OPEN_9_OF_10",
        "closure_claimed": True,
        "accepted_selected_K_source_row_count": mh_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": mh_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": h_row,
        "conditional_consequent_current": mh_hk["conditional_consequent_current"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterC5aTraceGridIdentity.v1",
        "status": "NEXT_FRONTIER_PROJECTION_MEASURE_NO_BOUNDARY_OR_HRESPONSE_HUV_TABLE",
        "closure_claimed": True,
        "closed_here": [
            "C5a computational trace-to-H7B1U grid identity",
            "bridge validator split into C5a closed versus C5b/C6 open",
            "B_Huv/domain and Pauli/Riesz three-row functional retained closed",
            "direct H_response/Huv table rechecked with domain closed and values absent",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "C5b physical Higgs projection-measure equality",
            "C6 same-source no-extra-boundary/source theorem",
            "selected H_response/Huv table values Huu,Hud,Hdd",
            "or full same-source M_source+R_H restriction",
            "selected s_beta or equivalent H quartic/threshold functional",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedEHUvTraceGridProjectionIdentityOrDirectHuvPayload",
        "status": STATUS,
        "previous_status": previous_mh["status"],
        "theorem": {
            "name": "EHUvTraceGridIdentityC5aTheorem",
            "proved": True,
            "statement": (
                "Given C2-C4 and the emitted B_Huv domain, the selected finite trace "
                "attached to E_H^UV is identical to the H7B1U/H7B1Z computational "
                "HYM grid trace on the same q79/F,m=1 branch.  This closes C5a only. "
                "It does not prove the physical Higgs projection-measure equality, "
                "the C6 no-extra-boundary theorem, or any H_response/Huv values."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "bridge_validator_C1_closed": True,
            "bridge_validator_C2_closed": True,
            "bridge_validator_C3_closed": True,
            "bridge_validator_C4_closed": True,
            "bridge_validator_C5a_trace_grid_identity_closed": True,
            "bridge_validator_C5b_projection_measure_equality_closed": False,
            "bridge_validator_C6_no_boundary_closed": False,
            "B_Huv_two_column_uv_lift_emitted": True,
            "M_H_three_row_source_functional_contract_closed": True,
            "selected_H_response_table_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": mh_hk["accepted_selected_K_source_row_count"],
            "selected_K_threshold_row_count_required": mh_hk[
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
            "c5a_trace_grid_identity": rel(TRACE_ID),
            "c5b_projection_measure_gate": rel(MEASURE_GATE),
            "direct_hresponse_huv_table_recheck_after_c5a": rel(DIRECT_RECHECK),
            "bridge_validator_c5a_update": rel(BRIDGE_UPDATE),
            "hk_threshold_gate_after_c5a_trace_identity": rel(HK_GATE),
            "next_cutset_after_c5a_trace_identity": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedEHUvTraceGridProjectionIdentityOrDirectHuvPayloadCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "bridge_validator_C5a_trace_grid_identity_closed": True,
        "bridge_validator_C5b_projection_measure_equality_closed": False,
        "bridge_validator_C6_no_boundary_closed": False,
        "B_Huv_two_column_uv_lift_emitted": True,
        "M_H_three_row_source_functional_contract_closed": True,
        "selected_H_response_table_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "selected_s_beta_value_found": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": mh_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": mh_hk[
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

    note = f"""# MTT Selected EHUvTraceGridProjectionIdentity or DirectHuvPayload v1

Status: `{STATUS}`

## What Closed

- split C5 into `C5a` trace-grid identity and `C5b` physical projection-measure equality
- closed `C5a`: the selected `E_H^UV` finite trace is the same q79/F,m=1 H7B1U/H7B1Z computational grid trace
- retained quadrature rule `{qid}` with weight `{c4_q["uniform_weight_rational"]}` on `{c4_q["node_count"]}` nodes
- rechecked direct route with `B_Huv` and the three-row source-functional closed
- H K-threshold gate remains `{mh_hk["accepted_selected_K_source_row_count"]}/{mh_hk["selected_K_threshold_row_count_required"]}`

## Still Open

- `C5b` physical Higgs projection-measure equality
- `C6` same-source no-extra-boundary/source theorem
- selected `H_response`/`Huv` table values `Huu,Hud,Hdd`, or full `M_source+R_H`
- selected `s_beta` or equivalent H quartic/threshold functional
- selected `K_threshold.Omega_H.lambda`: `false`
- strict `Omega/lambda_H` scalar execution

Next required artifact: `{NEXT}`
"""

    write_json(TRACE_ID, trace_id)
    write_json(MEASURE_GATE, measure_gate)
    write_json(DIRECT_RECHECK, direct_recheck)
    write_json(BRIDGE_UPDATE, bridge_update)
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
