"""Build CONST-EW-02 B24 u_dyn source-derivation import.

B24 imports the QA-SU3 alpha1 driver replay closure. This source-derives the
unit source-strength normalization N_alpha1(h_ext)=1 and du/dalpha1=h_ext, so
the B22 no-threshold bridge can set u_dyn=1 in the source-strength lane without
empirical calibration. Physical weak-angle closure still remains open because
RG/threshold, lambda_12, primitive C1 atoms, and matching scheme are separate.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b24_udyn_source_derivation_import"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = BASE / "qa_su3_alpha1_driver_import.packet.json"
UDYN_PACKET = BASE / "udyn_source_derivation_decision.packet.json"
CROSS_USE_PACKET = BASE / "cross_use_prediction_update.packet.json"
BOUNDARY = BASE / "weak_mixing_b24_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B24_UDynSourceDerivationImport_v1.md"

STATUS = "MTT_CONST_EW_02_B24_UDYN_SOURCE_DERIVED_PHYSICAL_WEAKANGLE_OPEN"


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


def sin2_no_threshold(r12: float, y: float) -> float:
    b1 = 41 / 10
    b2 = -19 / 6
    return 3 * (1 + b2 * y) / (3 * (1 + b2 * y) + 5 * (1 / r12 + b1 * y))


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b23_path = DATA / "const_ew_02_weak_mixing_b23_cross_use_universal_parameter_admissibility.candidate.json"
    b23_boundary_path = DATA / "const_ew_02_weak_mixing_b23_cross_use_universal_parameter_admissibility" / "weak_mixing_b23_boundary.packet.json"
    b22_replay_path = DATA / "const_ew_02_weak_mixing_b22_parameterized_bridge_replay" / "symbolic_weak_angle_replay.packet.json"

    qa_candidate_path = QA / "candidate_data" / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"
    qa_cert_path = QA / "certificates" / "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap_certificate.json"
    qa_note_path = QA / "proof_corpus" / "Selected_U1Y_RouteC_Alpha1_Driver_Replay_from_OrientedOverlap_v1.md"
    qa_primitive_gate_path = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_contractions_or_lambda12_gate.candidate.json"

    b23 = load(b23_path)
    b23_boundary = load(b23_boundary_path)
    b22_replay = load(b22_replay_path)
    qa_candidate = load(qa_candidate_path)
    qa_cert = load(qa_cert_path)
    primitive_gate = load(qa_primitive_gate_path)

    r12 = b22_replay["general_one_loop_formula"]["r12"]
    y_unit = math.sqrt(15 / math.log(448)) / (8 * math.pi**2)
    source_udyn = qa_candidate["promoted_value"]["lambda_alpha1"]
    source_y = source_udyn * y_unit
    source_sin2 = sin2_no_threshold(r12, source_y)

    qa_import = {
        "schema": "MTTConstEW02B24QASU3Alpha1DriverImport.v1",
        "status": "QA_SU3_ALPHA1_DRIVER_IMPORTED_SOURCE_DERIVED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B24-U-DYN-SOURCE-DERIVATION",
        "inputs": {
            "B23_candidate": rel(b23_path),
            "B23_boundary": rel(b23_boundary_path),
            "B22_symbolic_replay": rel(b22_replay_path),
            "qa_su3_alpha1_driver_candidate": rel(qa_candidate_path),
            "qa_su3_alpha1_driver_certificate": rel(qa_cert_path),
            "qa_su3_alpha1_driver_note": rel(qa_note_path),
            "qa_su3_primitive_c1_lambda12_gate": rel(qa_primitive_gate_path),
        },
        "imported_closure": {
            "selected_N_alpha1_h_ext_value": qa_cert["selected_N_alpha1_h_ext_value"],
            "du_dalpha1_equals_h_ext": qa_cert["du_dalpha1_equals_h_ext"],
            "alpha1_driver_verified": qa_cert["alpha1_driver_verified"],
            "honest_dotD_validator_closed": qa_cert["honest_dotD_validator_closed"],
            "observed_data_used": qa_cert["observed_data_used"],
            "target_fitting_used": qa_cert["target_fitting_used"],
        },
        "promoted_value": qa_candidate["promoted_value"],
        "guardrails_imported": qa_candidate["guardrails"],
        "residual_open_imported": qa_candidate["residual_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    udyn_decision = {
        "schema": "MTTConstEW02B24UDynSourceDerivationDecision.v1",
        "status": "U_DYN_RETIRED_IN_SOURCE_STRENGTH_NO_THRESHOLD_BRIDGE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B24-U-DYN-SOURCE-DERIVATION",
        "decision": {
            "u_dyn_source_derived": True,
            "u_dyn_value": source_udyn,
            "source": "QA-SU3 selected U1Y Route-C alpha1 driver replay from oriented overlap",
            "reason": "The same q79/F,m=1 oriented functional HYM/End0 layer promotes N_alpha1(h_ext)=1 and du/dalpha1=h_ext without observed data.",
            "scope": "source-strength/no-threshold bridge normalization only",
            "not_a_physical_weak_angle_closure": True,
        },
        "bridge_replay_update": {
            "formula": b22_replay["no_threshold_bridge_lane"]["formula"],
            "u_dyn": source_udyn,
            "y_source": source_y,
            "sin2_no_threshold_source_bridge": source_sin2,
            "matches_B22_u_dyn_1": abs(source_sin2 - b22_replay["no_threshold_bridge_lane"]["u_dyn_1_conditional_sin2"]) < 1e-15,
        },
        "still_not_closed": [
            "physical RG/matching scheme",
            "selected threshold vector or proof of no-threshold physical lane",
            "selected lambda_12 local determinant/spectral table",
            "primitive C1 atom table",
            "A_selected and b_selected",
            "alpha_phys/u_phys physical unit anchor",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cross_use = {
        "schema": "MTTConstEW02B24CrossUsePredictionUpdate.v1",
        "status": "CROSS_USE_TEST_SUCCEEDS_FOR_SOURCE_STRENGTH_PREFIX",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B24-FIT-ONCE-PREDICT-ELSEWHERE-CROSS-USE-TEST",
        "calibration_mode": "source_derived",
        "parameter": "u_dyn",
        "single_value": source_udyn,
        "cross_uses": {
            "alpha1_source_strength": {
                "status": "closed",
                "value": "N_alpha1(h_ext)=1; du/dalpha1=h_ext",
                "source_derived": True,
            },
            "weak_mixing_no_threshold_bridge": {
                "status": "conditional replay",
                "value": source_sin2,
                "source_derived_parameter_used": True,
                "physical_closure": False,
            },
            "dynamic_C1_dotD_prefix": {
                "status": "closed for honest dotD replay",
                "primitive_C1_atoms_closed": False,
            },
        },
        "prediction_tier": "source-derived prefix with physical weak-angle closure still gated",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B24Boundary.v1",
        "status": "U_DYN_SOURCE_DERIVED_FOR_PREFIX_PHYSICAL_EW_GATES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B24-BOUNDARY",
        "closed_now": {
            "B23_cross_use_policy_preserved": b23["cross_use_tier_formalized"],
            "u_dyn_source_derived_for_source_strength_lane": True,
            "u_dyn_value_locked_to_1": True,
            "alpha1_driver_verified_imported": True,
            "selected_dotD_source_verified_imported": qa_candidate["decision"]["selected_dotD_source_verified"],
            "honest_dotD_replay_closed_imported": True,
            "B22_no_threshold_bridge_replayed_with_source_udyn": True,
        },
        "still_open": {
            "u_phys_source_derivation_or_single_calibration": b23_boundary["still_open"]["u_phys_source_derivation_or_single_calibration"],
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
            "physical_RG_matching_scheme": True,
            "selected_threshold_or_no_threshold_physical_policy": True,
            "selected_lambda12_spectral_table": primitive_gate["what_remains_open"]["selected_lambda12_spectral_table"],
            "all_24_primitive_C1_atoms": primitive_gate["what_remains_open"]["all_24_primitive_C1_atoms"],
            "A_selected": primitive_gate["what_remains_open"]["A_selected"],
            "b_selected": primitive_gate["what_remains_open"]["b_selected"],
            "Yukawa_magnitudes": primitive_gate["what_remains_open"]["Yukawa_magnitudes"],
        },
        "claim_language": {
            "allowed": "u_dyn is source-derived for the source-strength/no-threshold bridge prefix.",
            "forbidden": "full physical weak-angle or no-knob electroweak closure.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B24NextWork.v1",
        "status": "NEXT_WORKORDER_PHYSICAL_EW_GATES_OR_U_PHYS",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B25-PHYSICAL-EW-GATES-OR-U-PHYS",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B25-LAMBDA12-SPECTRAL-TABLE-OR-THRESHOLD-POLICY",
            "task": "Emit selected lambda_12/local determinant spectral table or a same-source physical no-threshold policy and RG/matching scheme.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B25-U-PHYS-SOURCE-DERIVATION",
            "task": "Derive or single-calibrate u_phys through central-circle rod/clock, M-theory/modal-gap, or another global metrology theorem.",
        },
        "c1": {
            "label": "CONST-EW-02 / WEAK-MIXING / B25-PRIMITIVE-C1-ATOM-TABLE",
            "task": "Emit the 24 primitive C1 atoms needed for A_selected, b_selected, sector responses, and Yukawa/mixing closure.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB24UDynSourceDerivationImport",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B24-CROSS-USE-TEST-OR-SOURCE-DERIVATION",
        "output_packets": {
            "qa_su3_alpha1_driver_import": rel(IMPORT_PACKET),
            "udyn_source_derivation_decision": rel(UDYN_PACKET),
            "cross_use_prediction_update": rel(CROSS_USE_PACKET),
            "weak_mixing_b24_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B24UDynSourceDerivationImportTheorem",
            "proved": True,
            "statement": (
                "The QA-SU3 oriented overlap theorem source-derives the alpha1 "
                "source-strength normalization N_alpha1(h_ext)=1 and "
                "du/dalpha1=h_ext without observed data. Therefore the B22 "
                "source-strength/no-threshold bridge may set u_dyn=1 as a "
                "source-derived prefix value. This replays the conditional weak "
                "angle value, but physical weak-angle closure still requires "
                "RG/matching, threshold or no-threshold policy, lambda_12, and "
                "the remaining primitive C1/source tables."
            ),
        },
        "u_dyn_source_derived": True,
        "u_dyn_value": source_udyn,
        "source_strength_prefix_closed": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B24_UDynSourceDerivationImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "u_dyn_source_derived": True,
        "u_dyn_value": source_udyn,
        "alpha1_driver_verified_imported": True,
        "selected_dotD_source_verified_imported": True,
        "honest_dotD_replay_closed_imported": True,
        "source_sin2_no_threshold_bridge": source_sin2,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B24 UDyn Source Derivation Import v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B24-CROSS-USE-TEST-OR-SOURCE-DERIVATION`

## Result

Imported QA-SU3 selected U1Y Route-C alpha1 driver replay:

```text
N_alpha1(h_ext) = 1
du/dalpha1 = h_ext
alpha1_driver_verified = true
selected_dotD_source_verified = true
honest dotD replay = closed
```

This source-derives:

```text
u_dyn = 1
```

for the source-strength/no-threshold bridge prefix. It was not calibrated from
the observed weak angle.

## Replay

```text
y = sqrt(15/log(448))/(8*pi^2) = {source_y}
sin2_bridge = {source_sin2}
```

## Still Open

```text
physical RG/matching scheme
selected threshold vector or selected no-threshold physical policy
selected lambda_12 spectral/local determinant table
24 primitive C1 atoms
A_selected and b_selected
u_phys / alpha physical-unit anchor
```
"""

    for path, payload in [
        (IMPORT_PACKET, qa_import),
        (UDYN_PACKET, udyn_decision),
        (CROSS_USE_PACKET, cross_use),
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
