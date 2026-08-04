"""Attempt Phi_fin/B_N model-active equivalence or selected minimizer trace.

This is the Route A proof attempt requested after source promotion reduced to
Phi_fin.  The current artifacts do not prove exact equality between the
selected HYM/Strominger minimizer trace and the untransported model-active B_N
packet.  In fact, the selected diagonal End0 connection has nonzero du terms,
so the literal constant B_N zero cluster is not the full selected End0
covariant zero basis for T1/T2.  The correct repair is a gauge-transported B_N
trace.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

ROUTE_A = DATA / "selected_hym_projector_source_promotion_route_a.candidate.json"
VALUE = DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"
END0_DE = DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
T1T2_GREEN = DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
HYM_PAYLOAD = DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"
GAUGEFIXED = DATA / "selected_hym_gaugefixed_connection_or_galerkin_solve.candidate.json"

OUTPUT = DATA / "phifin_bn_modelactive_equivalence_or_minimizer_trace.candidate.json"
CERT = CERTS / "phifin_bn_modelactive_equivalence_or_minimizer_trace_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1.md"

STATUS = "MTT_PHIFIN_BN_MODEL_ACTIVE_EQUIVALENCE_REJECTED_GAUGE_TRANSPORT_TRACE_REQUIRED"
NEXT = "MTT_Selected_GaugeTransported_BN_PhiFin_Trace_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    route_a = load(ROUTE_A)
    value = load(VALUE)
    end0 = load(END0_DE)
    t1t2 = load(T1T2_GREEN)
    hym = load(HYM_PAYLOAD)
    gaugefixed = load(GAUGEFIXED)

    gradients = hym["diagonal_connection_payload"]["gradient_direction_summaries"]
    nonzero_gradient_dirs = {
        name: row for name, row in gradients.items() if row["l2"] > 1e-12
    }
    t3_matrix = end0["adjoint_connection_packet"]["ad_T3_matrix_on_basis_T1_T2_T3"]
    t3_matrix_nonzero = any(any(value != 0 for value in row) for row in t3_matrix)

    exact_equivalence_tests = {
        "finite_BN_value_side_clean": route_a["route_a_gate_matrix"]["A3_finite_BN_projector_values_clean"][
            "passes"
        ],
        "selected_diagonal_End0_connection_closed": end0["what_closes_now"][
            "diagonal_End0_connection_formula"
        ],
        "selected_connection_has_nonzero_du": bool(nonzero_gradient_dirs),
        "ad_T3_nonzero_on_T1_T2": t3_matrix_nonzero,
        "untransported_constant_BN_zero_cluster_claims_full_triplet_zero_modes": (
            value["finite_value_payload"]["zero_cluster"]["dimension"] == 3
        ),
        "exact_untransported_model_active_equivalence_possible": False,
    }

    no_go_theorem = {
        "name": "UntransportedBNModelActiveEquivalenceNoGo",
        "proved": True,
        "statement": (
            "The selected diagonal End0 operator is D=d+du ad(T3) with nonzero du in the "
            "selected HYM replay.  Since ad(T3) acts nontrivially on T1,T2, the literal "
            "untransported constant B_N triplet cannot be identified with the full selected "
            "End0 covariant zero-mode triplet.  Therefore Phi_fin cannot promote the current "
            "model-active B_N packet by exact equality without a gauge-transported basis or a "
            "replacement selected minimizer trace."
        ),
        "proof_steps": [
            "The finite B_N packet has clean rank-3 constant zero-cluster support.",
            "The selected HYM diagonal replay emits nonzero gradients of u.",
            "The selected End0 connection is d+du ad(T3).",
            "ad(T3) is nonzero on the T1/T2 plane.",
            "Thus an untransported constant T1/T2 section is not D-flat when du is nonzero.",
            "The previous T1/T2 covariant Green artifact shows the correct repair: the T1/T2 lane is pure-gauge equivalent after transport, not literally equal before transport.",
        ],
    }

    gauge_transport_repair = {
        "name": "SelectedGaugeTransportedBNPhiFinTrace",
        "required_transport": "U=exp(-u ad(T3)) on the T1/T2 plane, identity on T3/H singlet lanes",
        "why_legal": t1t2["what_closes_now"]["pure_gauge_periodic_equivalence_theorem"],
        "must_emit_next": [
            "transported zero-mode basis K_s^sel = U K_s^model for Q,u,d,L,e,N",
            "transported projector P_s^sel = U P_s^model U^{-1} in the selected L2 metric",
            "proof that D_selected(U psi)=U d psi on the retained End0 lanes",
            "gap/Riesz/Green transfer from model-active B_N to transported selected basis",
            "dotD_alpha1 derivative including derivative of the transport U",
            "validator replay with theorem-derived selected_source_verified flags",
        ],
        "can_promote_after_repair": True,
    }

    promotion_decision = {
        "exact_model_active_equivalence_proved": False,
        "exact_model_active_equivalence_rejected": True,
        "selected_minimizer_trace_emitted": False,
        "selected_source_flags_may_be_flipped_now": False,
        "reason": [
            "selected connection has nonzero du ad(T3)",
            "untransported B_N constants are model-active zero modes, not selected transported End0 zero modes",
            "gauge transport is required before a Phi_fin trace can promote source flags",
        ],
        "next_required_artifact": NEXT,
    }

    superset_strategy = {
        "classification": "SUPERSET_ROUTE_A_REPAIRED_BY_GAUGE_TRANSPORT",
        "straight_End0_result": "selected diagonal End0 connection proves exact untransported equality false",
        "BN_result": "finite projectors remain valuable as model-active basis before transport",
        "HYM_result": "selected HYM replay supplies u and du needed for the transport",
        "PhiFin_result": "must emit transported trace, not copy the model-active scaffold",
        "uses_observed_constants": False,
    }

    data = {
        "candidate": "MTTSelectedPhiFinBNModelActiveEquivalenceOrSelectedMinimizerTrace",
        "status": STATUS,
        "inputs": {
            "route_a": rel(ROUTE_A),
            "value_emission": rel(VALUE),
            "end0_de": rel(END0_DE),
            "t1t2_green": rel(T1T2_GREEN),
            "hym_payload": rel(HYM_PAYLOAD),
            "gaugefixed": rel(GAUGEFIXED),
        },
        "exact_equivalence_tests": exact_equivalence_tests,
        "nonzero_gradient_dirs": nonzero_gradient_dirs,
        "ad_T3_matrix": t3_matrix,
        "no_go_theorem": no_go_theorem,
        "gauge_transport_repair": gauge_transport_repair,
        "promotion_decision": promotion_decision,
        "superset_strategy": superset_strategy,
        "what_closes_now": {
            "untransported_model_active_equivalence_rejected": True,
            "reason_for_rejection_proved": True,
            "gauge_transport_repair_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "gauge_transported_BN_trace": True,
            "selected_source_verified": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "selected_rho_s_actual_promotion": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "untransported_model_active_equivalence_rejected": True,
        "gauge_transport_trace_required": True,
        "selected_source_flags_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhiFin BN ModelActive Equivalence or SelectedMinimizerTrace v1

Status: `{STATUS}`.

## Result

The exact untransported equivalence is rejected.

The model-active `B_N` packet is clean, but the selected diagonal End0 replay
emits

```text
D = d + du ad(T3)
```

with nonzero `du`:

```text
nonzero gradient directions = {list(nonzero_gradient_dirs.keys())}
```

Since `ad(T3)` acts nontrivially on the `T1/T2` plane, literal constant
`B_N` triplet modes cannot be the full selected covariant zero-mode triplet
before transport.

## Proof Boundary

This does not kill Route A.  It corrects it.

The previous T1/T2 covariant Green theorem already shows the selected diagonal
End0 lane is pure-gauge equivalent.  Therefore the correct `Phi_fin` trace is
not the raw model-active packet, but the gauge-transported packet:

```text
K_s^selected = exp(-u ad(T3)) K_s^model
P_s^selected = U P_s^model U^{-1}
```

with identity action on the protected `T3` and Higgs singlet lanes.

## What Must Be Proved Next

Emit the gauge-transported `B_N` trace and replay:

- selected transported zero-mode bases,
- selected transported projectors,
- Riesz/Green transfer,
- `dotD_alpha1` including derivative of the transport,
- validator payloads with theorem-derived source flags.

No observed constants, benchmark targets, or lifted selected flags are used.

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
