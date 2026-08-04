"""Try to prove selected alpha1 source identity or typed retarded-kernel value.

This is the first proof attempt after the exact alpha1 normalization packet was
filled numerically but failed final validation.  The question is no longer the
candidate value; it is whether either legal provenance route can promote that
value:

1. same-source selected Phi_fin/Strominger/HYM operator identity, or
2. typed q79 B_N retarded-overlap alpha1 derivative.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PACKET_FILL = DATA / "selected_samesource_alpha1_normalization_packet_fill_attempt.candidate.json"
FILLED_PACKET = DATA / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"
SOURCE_DRIVER = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
TRANSPORT_REPLAY = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"

CONSTANTS_RETARDED = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-nonsm-constants-no-knob/candidate_data/"
    "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
)
CONSTANTS_CW_SOURCE = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-nonsm-constants-no-knob/certificates/"
    "selected_qa_su3_m1_cw_operator_source_proof_attempt_certificate.json"
)
CONSTANTS_ROUTE_GATE = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-nonsm-constants-no-knob/certificates/"
    "selected_qa_su3_routec_source_solve_gate_certificate.json"
)
CONSTANTS_ORIENTATION = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-nonsm-constants-no-knob/certificates/"
    "selected_qa_su3_orientation_dedotd_source_attempt_import_certificate.json"
)
Q79_DE_DOTD_CONTRACT = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro/candidate_data/"
    "q79_selected_de_green_dotd_source_for_primitive_c1/de_green_dotd_source_contract.open.json"
)

OUTPUT = DATA / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt.candidate.json"
CERT = CERTS / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt_certificate.json"
NOTE = CORPUS / "MTT_Selected_Alpha1_SourceIdentity_or_RetardedKernel_Value_Attempt_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_SOURCEIDENTITY_OR_RETARDEDKERNEL_VALUE_ATTEMPT_REDUCED_TO_SOURCE_CERTIFICATE_OPEN"
NEXT = "MTT_Selected_Visible_RouteC_SourceIdentity_Certificate_or_TypedBNRetardedDerivative_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    packet_fill = load(PACKET_FILL)
    filled_packet = load(FILLED_PACKET)
    source_driver = load(SOURCE_DRIVER)
    phifin_alpha1 = load(PHIFIN_ALPHA1)
    gauge_trace = load(GAUGE_TRACE)
    transport = load(TRANSPORT_REPLAY)
    dotd_probe = load(DOTD_PROBE)
    constants_retarded = load(CONSTANTS_RETARDED)
    constants_cw = load(CONSTANTS_CW_SOURCE)
    constants_route = load(CONSTANTS_ROUTE_GATE)
    constants_orientation = load(CONSTANTS_ORIENTATION)
    q79_contract = load(Q79_DE_DOTD_CONTRACT)

    selected_flags = source_driver["source_origin_audit"]["selected_flags"]
    payload_flags = phifin_alpha1["payload_summary"]["selected_payload_flags"]
    transfer = constants_retarded["transfer_checks"]
    q79_source_identity = q79_contract["source_identity"]

    lane_a = {
        "name": "same_source_phi_fin_strominger_hym_identity",
        "attempted": True,
        "support_closed": {
            "fixed_topological_sector_named": source_driver["source_origin_audit"]["support_closed"][
                "fixed_topological_sector_named"
            ],
            "mtt_strominger_selection_available": source_driver["source_origin_audit"][
                "support_closed"
            ]["mtt_strominger_selection_available"],
            "same_source_support_converges": source_driver["source_origin_audit"]["support_closed"][
                "same_source_support_converges"
            ],
            "gauge_transported_functional_trace": gauge_trace["theorem"]["proved"],
            "stationary_projector_source_replay": transport["validator_result"][
                "selected_source_verified"
            ],
            "transport_dotd_formula": dotd_probe["theorem"]["proved"],
        },
        "selected_source_identity_emitted": False,
        "blocking_flags": {
            name: value for name, value in selected_flags.items() if value is False
        },
        "selected_payload_flags_false": {
            name: value for name, value in payload_flags.items() if value is False
        },
        "external_prefix": {
            "cw_operator_source_prefix_closed": constants_cw["closed_prefix"],
            "cw_theorem_proved": constants_cw["theorem_proved"],
            "routec_source_gate_status": constants_route["status"],
            "routec_selected_source_constructed": not constants_route["not_closed"][
                "selected_visible_sm_bundle_or_sheaf_model"
            ],
        },
        "verdict": "OPEN",
        "reason": (
            "Lane A has strong same-source and transport support, but no theorem-derived visible/Route-C "
            "operator-source identity or selected Phi_fin alpha1 payload is emitted."
        ),
    }

    lane_b = {
        "name": "typed_bn_retarded_alpha1_derivative",
        "attempted": True,
        "support_closed": {
            "ckm_retarded_kernel_pattern_available": transfer[
                "K1_ckm_retarded_kernel_pattern_available"
            ],
            "q79_phi_fin_alpha1_support_available": transfer[
                "K2_q79_phi_fin_alpha1_support_available"
            ],
            "source_level_weyl_carrier_available": transfer[
                "K3_source_level_weyl_carrier_available"
            ],
            "q79_and_q369_reach_de_green_dotd_layer": constants_orientation["closed_now"][
                "finite_branch_data_reaches_DE_Green_dotD_layer"
            ],
        },
        "typed_bn_retarded_derivative_emitted": False,
        "blocking_flags": {
            "selected_sector_charge_or_chirality": transfer[
                "K4_selected_sector_charge_or_chirality"
            ],
            "selected_transfer_normalization": transfer[
                "K5_selected_transfer_normalization"
            ],
            "selected_BN_tangent_or_retarded_kernel": transfer[
                "K6_selected_BN_tangent_or_retarded_kernel"
            ],
            "honest_dotD_replay_from_kernel": transfer[
                "K7_honest_dotD_replay_from_kernel"
            ],
            "q79_selected_source_certificate_present": q79_source_identity[
                "selected_source_certificate_present"
            ],
            "q79_selected_routec_or_typed_de_construction_present": q79_source_identity[
                "selected_RouteC_or_typed_DE_construction_present"
            ],
        },
        "external_orientation_gate": {
            "unique_branch_selected_now": constants_orientation["branch_status"][
                "unique_branch_selected_now"
            ],
            "validator_status": constants_orientation["validator_replay"]["status"],
            "first_open_items": constants_orientation["validator_replay"]["first_open_items"],
        },
        "verdict": "OPEN",
        "reason": (
            "Lane B has retarded-pattern and finite D_E/dotD support, but lacks the typed q79 B_N "
            "alpha1 derivative, selected transfer normalization, and non-observed retarded/source selector."
        ),
    }

    packet_result = {
        "lambda_alpha1": filled_packet["source_strength_coordinate"]["lambda_alpha1"],
        "N_alpha1_h_ext": filled_packet["normalization_functional"]["N_alpha1_h_ext"],
        "tangent_residual_l2": filled_packet["tangent_equality"]["residual_l2"],
        "packet_validator_ok": packet_fill["validator_report"]["ok"],
        "selected_value_emitted": False,
        "alpha1_driver_verified": False,
        "reason": "The filled packet values are ready, but neither provenance lane emits selected theorem data.",
    }

    data = {
        "candidate": "MTTSelectedAlpha1SourceIdentityOrRetardedKernelValueAttempt",
        "status": STATUS,
        "inputs": {
            "packet_fill": rel(PACKET_FILL),
            "filled_packet": rel(FILLED_PACKET),
            "source_driver": rel(SOURCE_DRIVER),
            "phifin_alpha1": rel(PHIFIN_ALPHA1),
            "gauge_trace": rel(GAUGE_TRACE),
            "transport_replay": rel(TRANSPORT_REPLAY),
            "dotd_probe": rel(DOTD_PROBE),
            "constants_retarded": rel(CONSTANTS_RETARDED),
            "constants_cw_source": rel(CONSTANTS_CW_SOURCE),
            "constants_route_gate": rel(CONSTANTS_ROUTE_GATE),
            "constants_orientation": rel(CONSTANTS_ORIENTATION),
            "q79_de_dotd_contract": rel(Q79_DE_DOTD_CONTRACT),
        },
        "packet_result": packet_result,
        "proof_lanes": {
            "lane_A_same_source_identity": lane_a,
            "lane_B_typed_retarded_kernel": lane_b,
        },
        "comparative_verdict": {
            "lane_A_cleaner_for_rigor": True,
            "lane_B_fastest_if_retarded_selector_is_found": True,
            "neither_lane_closes_now": True,
            "minimal_common_missing_object": (
                "a selected visible/Route-C source certificate that also supplies the same-branch "
                "alpha1 derivative, or an equivalent typed B_N retarded alpha1 derivative"
            ),
        },
        "what_closes_now": {
            "two_lane_attempt_executed": True,
            "source_identity_support_audited": True,
            "retarded_kernel_support_audited": True,
            "numeric_packet_value_preserved": True,
            "minimal_common_missing_object_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_visible_or_routec_source_identity_certificate": True,
            "selected_phi_fin_alpha1_payload_values": True,
            "selected_source_strength_coordinate_theorem": True,
            "typed_BN_retarded_alpha1_derivative": True,
            "selected_transfer_normalization": True,
            "honest_dotD_replay_without_lifted_flags": True,
            "alpha1_driver_verified": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "classification": "TWO_LANE_SUPERSET_PROVENANCE_ATTACK",
            "straight_path": "same-source Phi_fin/Strominger/HYM selected source identity",
            "alternative_path": "typed B_N retarded-overlap derivative and non-observed retarded selector",
            "locked_target": "promote the already-filled alpha1 normalization packet",
            "uses_observed_constants": False,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_Alpha1_SourceIdentity_or_RetardedKernel_Value_Attempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "lambda_alpha1": packet_result["lambda_alpha1"],
        "N_alpha1_h_ext": packet_result["N_alpha1_h_ext"],
        "lane_A_selected_source_identity_emitted": False,
        "lane_B_typed_bn_retarded_derivative_emitted": False,
        "selected_value_emitted": False,
        "alpha1_driver_verified": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Alpha1 SourceIdentity or RetardedKernel Value Attempt v1

Status: `{STATUS}`.

## Result

The filled alpha1 normalization packet keeps:

```text
lambda_alpha1 = {packet_result["lambda_alpha1"]}
N_alpha1(h_ext) = {packet_result["N_alpha1_h_ext"]}
tangent residual = {packet_result["tangent_residual_l2"]}
```

Two legal provenance lanes were tested.

## Lane A: Same-Source Phi_fin/Strominger/HYM

This lane is best for rigor.  It has source-level convergence, selected
S3/GS support, gauge-transported `Phi_fin` trace, stationary projector replay,
and the transport dotD formula.  It still lacks a theorem-derived selected
visible/Route-C operator-source identity and selected `Phi_fin alpha1` payload.

## Lane B: Typed B_N Retarded Kernel

This lane has CKM/nil-survivor retarded-pattern support and q79/q369 finite
D_E/dotD layers.  It still lacks selected sector charge/chirality, selected
transfer normalization, a typed q79 `B_N` alpha1 derivative, and a non-observed
retarded/source selector.

## Next Proof

Prove one of:

```text
selected visible/Route-C source identity certificate
typed B_N retarded alpha1 derivative
```

Either one can turn the already-filled packet into selected theorem data.  No
observed constants, benchmark matrices, target fits, or lifted flags are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
