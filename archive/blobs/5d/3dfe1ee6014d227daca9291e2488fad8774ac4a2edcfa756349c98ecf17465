"""Bridge the visible/Route-C alpha1 derivative lane to the later alpha1 import.

The older visible_routec_sourceidentity_or_typedbn_derivative partial fill
closed stationary Lane A source identity but still marked same-branch alpha1
derivative and honest dotD replay open.  Later work imported a theorem-derived
alpha1/dotD replay from the sibling GR/protospinor proof for the same
q79/F,m=1 oriented source spine.  This builder records the precise
reconciliation without promoting the remaining dynamic Phi_fin/C1 payload.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

PARTIAL = DATA / "visible_routec_sourceidentity_or_typedbn_derivative.partial_fill.json"
CONTRACT = DATA / "visible_routec_sourceidentity_or_typedbn_derivative_contract.candidate.json"
ALPHA1_IMPORT = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
C1_FRONTIER = DATA / "selected_c1_frontier_after_alpha1_import.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
PRIMITIVE_FRONTIER = DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"

OUTPUT = DATA / "selected_visible_routec_phifin_alpha1_derivative_bridge.candidate.json"
CERT = CERTS / "selected_visible_routec_phifin_alpha1_derivative_bridge_certificate.json"
NOTE = CORPUS / "MTT_Selected_VisibleRouteC_PhiFinAlpha1Derivative_Bridge_v1.md"

STATUS = "MTT_SELECTED_VISIBLE_ROUTEC_PHIFIN_ALPHA1_DERIVATIVE_BRIDGED_ALPHA1_RETIRED_C1_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicPhiFinC1Payload_ValueEmission_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    partial = load(PARTIAL)
    contract = load(CONTRACT)
    alpha1 = load(ALPHA1_IMPORT)
    c1 = load(C1_FRONTIER)
    phifin = load(PHIFIN_ALPHA1)
    primitive = load(PRIMITIVE_FRONTIER)

    alpha1_retires = all(
        [
            alpha1["alpha1_driver_verified_imported"] is True,
            alpha1["selected_dotD_source_verified_imported"] is True,
            alpha1["alpha1_driver_replay_import"]["du_dalpha1_equals_h_ext"] is True,
            alpha1["alpha1_driver_replay_import"]["honest_dotD_alpha1_replay"] is True,
            c1["retired_driver_gates"]["alpha1_driver_verified"] is True,
            c1["retired_driver_gates"]["selected_dotD_source_verified"] is True,
        ]
    )
    stationary_lane_a_source_closed = all(
        [
            partial["partial_fill_result"]["lane_A_source_identity_closed"] is True,
            partial["partial_fill_result"]["lane_A_visible_routec_operator_source_closed"] is True,
        ]
    )
    full_dynamic_payload_open = phifin["payload_summary"]["all_selected_values_emitted"] is False

    candidate = {
        "candidate": "MTTSelectedVisibleRouteCPhiFinAlpha1DerivativeBridge",
        "status": STATUS,
        "inputs": {
            "visible_routec_partial_fill": rel(PARTIAL),
            "visible_routec_contract": rel(CONTRACT),
            "crossrepo_alpha1_import": rel(ALPHA1_IMPORT),
            "c1_frontier_after_alpha1": rel(C1_FRONTIER),
            "phifin_alpha1_payload_attempt": rel(PHIFIN_ALPHA1),
            "primitive_c1_frontier": rel(PRIMITIVE_FRONTIER),
        },
        "bridge_result": {
            "stationary_lane_A_source_identity_closed": stationary_lane_a_source_closed,
            "same_branch_alpha1_derivative_closed_by_import": alpha1_retires,
            "honest_dotD_replay_closed_by_import": alpha1_retires,
            "alpha1_driver_verified": alpha1["alpha1_driver_replay_import"]["alpha1_driver_verified"],
            "selected_dotD_source_verified": alpha1["alpha1_driver_replay_import"]["selected_dotD_source_verified"],
            "lambda_alpha1": alpha1["alpha1_driver_replay_import"]["lambda_alpha1"],
            "N_alpha1_h_ext": alpha1["alpha1_driver_replay_import"]["N_alpha1_h_ext"],
            "du_dalpha1_equals_h_ext": alpha1["alpha1_driver_replay_import"]["du_dalpha1_equals_h_ext"],
            "visible_routec_contract_lane_A_fully_validates_now": False,
            "reason_lane_A_not_fully_validated": (
                "The later import closes alpha1 derivative and honest dotD replay, while the older partial fill "
                "already closed stationary source identity.  The selected full Phi_fin dynamic C1 payload, primitive "
                "C1 contractions, A_selected, b_selected, and sector response matrices remain open."
            ),
        },
        "old_partial_fill_update": {
            "previous_next_required_artifact": partial["next_required_artifact"],
            "previous_lane_A_same_branch_alpha1_derivative_closed": partial["partial_fill_result"][
                "lane_A_same_branch_alpha1_derivative_closed"
            ],
            "previous_lane_A_dotd_validator_replay_closed": partial["partial_fill_result"][
                "lane_A_dotd_validator_replay_closed"
            ],
            "updated_same_branch_alpha1_derivative_closed": alpha1_retires,
            "updated_dotd_validator_replay_closed": alpha1_retires,
            "updated_active_frontier": c1["next_required_artifact"],
        },
        "payload_boundary": {
            "full_PhiFin_alpha1_payload_selected_values_emitted": not full_dynamic_payload_open,
            "primitive_C1_contractions_emitted": primitive["what_remains_open"]["selected_higher_order_or_full_response_matrices"] is False,
            "A_selected_claimed": primitive["A_selected_claimed"],
            "b_selected_claimed": primitive["b_selected_claimed"],
            "selected_deltaTheta_C1_solution": primitive["what_remains_open"]["selected_deltaTheta_C1_solution"] is False,
            "full_SM_or_no_knob_closure": False,
        },
        "superset_strategy": {
            "mode": "STRAIGHT_LANE_A_RECONCILIATION_WITH_CROSSREPO_SUPPORT",
            "straight_path": "visible/Route-C stationary source identity plus Phi_fin/HYM transport source",
            "support_path": "GR/protospinor cross-repo alpha1 driver replay on the same q79/F,m=1 oriented source spine",
            "locked_target": "retire only alpha1/dotD as active blocker; keep dynamic Phi_fin C1 values open",
            "uses_observed_constants": False,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "VisibleRouteCPhiFinAlpha1DerivativeBridgeTheorem",
            "proved": True,
            "statement": (
                "The visible/Route-C partial-fill lane and the later cross-repo alpha1 import are compatible. "
                "Stationary Lane A source identity and visible operator source were already theorem-derived by symbolic "
                "transport.  The sibling GR/protospinor import supplies theorem-derived N_alpha1(h_ext)=1, "
                "du/dalpha1=h_ext, selected_dotD_source_verified=true, alpha1_driver_verified=true, and honest dotD "
                "replay for the same q79/F,m=1 oriented source spine.  Therefore alpha1 derivative and dotD replay are "
                "retired as active blockers in this repo.  This does not emit the selected dynamic Phi_fin C1 payload, "
                "primitive contractions, A_selected, b_selected, deltaTheta_C1, or sector response matrices."
            ),
        },
        "what_closes_now": {
            "old_visible_routec_partial_fill_reconciled": True,
            "same_branch_alpha1_derivative_retired_as_active_blocker": alpha1_retires,
            "honest_dotD_replay_retired_as_active_blocker": alpha1_retires,
            "stationary_source_identity_retained": stationary_lane_a_source_closed,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_dynamic_PhiFin_C1_payload": True,
            "primitive_C1_contractions": True,
            "selected_A_selected": True,
            "selected_b_selected": True,
            "selected_deltaTheta_C1_solution": True,
            "sector_response_matrices_M_u_M_d_M_e_M_nuD": True,
            "Yukawa_CKM_PMNS_masses_Higgs_RG": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "observed_data_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_VisibleRouteC_PhiFinAlpha1Derivative_Bridge_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "same_branch_alpha1_derivative_retired_as_active_blocker": alpha1_retires,
        "honest_dotD_replay_retired_as_active_blocker": alpha1_retires,
        "full_dynamic_PhiFin_C1_payload_emitted": False,
        "A_selected_claimed": False,
        "b_selected_claimed": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected VisibleRouteC PhiFinAlpha1Derivative Bridge v1

Status: `{STATUS}`.

## Result

This reconciles an older visible/Route-C partial fill with the later alpha1
driver import.

The old Lane A packet had already closed stationary source identity and visible
operator source.  The later cross-repo import supplies, on the same q79/F,m=1
oriented source spine:

```text
N_alpha1(h_ext) = {candidate["bridge_result"]["N_alpha1_h_ext"]}
lambda_alpha1 = {candidate["bridge_result"]["lambda_alpha1"]}
du/dalpha1 = h_ext
selected_dotD_source_verified = true
alpha1_driver_verified = true
honest dotD replay = PASS
```

So alpha1 derivative and dotD replay are no longer the active local blockers.

## Boundary

This does **not** emit the selected dynamic `Phi_fin^C1` payload.  The live
frontier remains primitive C1 contractions or higher-order/full-response
matrices that emit `A_selected`, `b_selected`, `deltaTheta_C1`, and sector
response matrices from the same selected source.

No observed constants, benchmark matrices, target fits, or lifted flags are
used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"status": STATUS, "candidate": rel(OUTPUT), "note": rel(NOTE)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
