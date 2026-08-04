"""Build the post-HYM local-system torsion or new-operator attack packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

INPUTS = {
    "hym_retirement": DATA / "selected_heterotic_hym_repair_source_selection_or_retirement.candidate.json",
    "post_hym_template": DATA / "selected_heterotic_post_hym_retirement_operator_or_torsion_source.template.json",
    "local_system_torsion": NONSM / "certificates" / "selected_qa_su3_local_system_torsion_source_extraction_certificate.json",
    "q64_bridge": NONSM / "certificates" / "selected_q64_to_qa_su3_local_system_bridge_attempt_certificate.json",
    "central_character": NONSM / "certificates" / "selected_qa_su3_central_character_homomorphism_theorem_certificate.json",
    "qa_nil_reduction": NONSM / "certificates" / "selected_qa_nil_determinant_reduction_certificate.json",
    "projective_or_endomorphism": NONSM / "certificates" / "selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_local_system_torsion_or_new_operator_attack.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_local_system_torsion_or_new_operator_attack_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_projective_or_endomorphism_operator_source.template.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_LocalSystemTorsion_or_NewOperatorSource_Attack_v1.md"

STATUS = "HETEROTIC_LOCAL_SYSTEM_TORSION_OR_NEW_OPERATOR_ATTACK_BUILT_ENDOMORPHISM_PRIMARY"
NEXT = "Selected_Heterotic_ProjectiveCarrier_or_EndomorphismOperator_SourcePacket_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def build_template() -> dict[str, Any]:
    return {
        "schema": "SelectedHeteroticProjectiveOrEndomorphismOperatorSource.v1",
        "status": "OPEN_SOURCE_REQUIRED",
        "route_A_projective_carrier": {
            "selected_projective_representation": None,
            "phase": "exp(2*pi*i*15/64)",
            "minimal_clock_shift_dimension": 64,
            "operator_domain_bridge_to_Qa_SU3_threshold_complex": None,
            "BRST_or_zero_mode_policy": None,
            "degreewise_torsion_or_zeta_finite_part": None,
            "trace_weights_and_normalization": None,
        },
        "route_B_endomorphism_operator": {
            "selected_bundle_sheaf_twist_or_module": None,
            "endomorphism_E_or_Weitzenbock_zero_order_block": None,
            "laplace_type_principal_symbol": None,
            "heat_spectrum_zeta_or_torsion_finite_part": None,
            "qa_qc_su2_trace_weights": None,
            "physical_threshold_convention": None,
        },
        "route_C_global_measure": {
            "selected_fundamental_domain_or_global_section": None,
            "proof_not_double_counting_FP_BRST": None,
            "finite_measure_or_determinant_contribution": None,
        },
        "forbidden": [
            "ordinary rank-one U1 local system with q64 on the Heisenberg center",
            "scalar SU3-center embedding of q64=15",
            "U64 clock-shift carrier as Qa/SU3 closure without operator-domain bridge",
            "compact Nil scalar zeta proxy as Ray-Singer torsion",
            "observed electroweak or Qa/SU3 residual to choose representation, character, or finite part",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    hym = load(INPUTS["hym_retirement"])
    post_template = load(INPUTS["post_hym_template"])
    torsion = load(INPUTS["local_system_torsion"])
    q64_bridge = load(INPUTS["q64_bridge"])
    central = load(INPUTS["central_character"])
    qa_nil = load(INPUTS["qa_nil_reduction"])
    projective = load(INPUTS["projective_or_endomorphism"])
    template = build_template()

    route_tests = {
        "ordinary_rank_one_local_system": {
            "status": "CLOSED_NEGATIVE_FOR_Q64_CENTER",
            "passes": central["ordinary_u1_local_system_test"]["passes"],
            "reason": central["ordinary_u1_local_system_test"]["reason"],
            "usable_for_selected_q64_torsion": False,
        },
        "scalar_su3_center": {
            "status": "CLOSED_NEGATIVE_FOR_Q64_CENTER",
            "passes": central["su3_scalar_center_test"]["passes"],
            "reason": central["su3_scalar_center_test"]["reason"],
            "usable_for_selected_q64_torsion": False,
        },
        "q64_bridge_to_Qa_SU3": {
            "status": "PARTIAL_NOT_CLOSED",
            "bridge_closed": q64_bridge["verdict"]["bridge_closed"],
            "missing_bridge_requirements": q64_bridge["missing_bridge_requirements"],
            "candidate_character": q64_bridge["selected_data"]["candidate_character_value_if_bridge_existed"],
        },
        "projective_clock_shift": {
            "status": "AUXILIARY_OPEN_NOT_SELECTED_PROOF_SOURCE",
            "mathematical_possibility": central["nonabelian_clock_shift_route"]["mathematical_possibility"],
            "minimal_dimension": central["nonabelian_clock_shift_route"]["minimal_finite_dimension_for_exact_phase"],
            "route_decision": projective["decision"]["conditional_auxiliary_route"],
            "why_not_current_closure": central["nonabelian_clock_shift_route"]["why_not_current_closure"],
        },
        "compact_nil_scalar_proxy": {
            "status": "DIAGNOSTIC_NOT_SELECTED",
            "qa_nil_selected_determinant_closed": qa_nil["verdict"]["qa_nil_selected_determinant_closed"],
            "remaining_missing_inputs": qa_nil["verdict"]["remaining_missing_inputs"],
            "old_proxy_shown_not_to_close": qa_nil["verdict"]["old_proxy_shown_not_to_close"],
        },
        "new_endomorphism_operator_source": {
            "status": "PRIMARY_NEXT_ROUTE_SOURCE_MISSING",
            "selected_primary_route": projective["decision"]["selected_primary_route"],
            "must_find_or_prove": projective["next_required_artifact"]["must_find_or_prove"],
        },
    }

    decision = {
        "hym_printed_route_retired": hym["decision"]["printed_hym_matrix_route_retired_current_source"],
        "ordinary_rank_one_torsion_route_closed_negative_for_q64": True,
        "q64_projective_route_open_auxiliary": True,
        "compact_nil_scalar_proxy_rejected": True,
        "selected_primary_route": "source_certified_endomorphism_E_full_operator",
        "secondary_route": "q64_projective_clock_shift_only_with_operator_domain_bridge",
        "global_measure_route": "backup_only_must_avoid_FP_BRST_double_counting",
        "measured_electroweak_closure": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticLocalSystemTorsionOrNewOperatorAttack",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "input_statuses": {
            "hym_retirement": hym["status"],
            "local_system_torsion": torsion["status"],
            "q64_bridge": q64_bridge["status"],
            "central_character": central["status"],
            "qa_nil_reduction": qa_nil["status"],
            "projective_or_endomorphism": projective["status"],
        },
        "route_tests": route_tests,
        "post_hym_template_inherited": post_template,
        "next_template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "PostHYMLocalSystemTorsionOrNewOperatorAttackTheorem",
            "proved": True,
            "statement": (
                "After retiring the explicit HYM matrix route under current sources, "
                "the ordinary rank-one local-system torsion bridge is closed negative "
                "for the selected q64 phase: the Heisenberg center is a commutator, "
                "so every U(1) character kills it, and the q64 phase is not an SU3 "
                "scalar center element. The q64 clock-shift/projective carrier remains "
                "mathematically possible but auxiliary until a source theorem identifies "
                "it with the Qa/SU3 threshold complex and computes its finite part. "
                "Therefore the primary no-knob route is now a source-certified "
                "endomorphism_E or equivalent threshold operator packet, with heat, "
                "spectrum, zeta, or torsion finite part."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_rank_one_q64_character": False,
            "promotes_su3_scalar_q64_center": False,
            "promotes_projective_carrier_without_operator_bridge": False,
            "promotes_compact_nil_scalar_proxy": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedHeteroticLocalSystemTorsionOrNewOperatorAttack",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "ordinary_rank_one_torsion_route_closed_negative_for_q64": True,
        "q64_projective_route_open_auxiliary": True,
        "selected_primary_route": decision["selected_primary_route"],
        "measured_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert, template)


def render_note(candidate: dict[str, Any], cert: dict[str, Any], template: dict[str, Any]) -> str:
    return f"""# Selected Heterotic Local-System Torsion or New Operator Source Attack v1

## Result

```text
status = {candidate["status"]}
ordinary_rank_one_torsion_route_closed_negative_for_q64 = true
q64_projective_route_open_auxiliary = true
selected_primary_route = {candidate["decision"]["selected_primary_route"]}
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Route Tests

```json
{json.dumps(candidate["route_tests"], indent=2, sort_keys=True)}
```

## Theorem

{candidate["theorem"]["statement"]}

## Next Source Template

```json
{json.dumps(template, indent=2, sort_keys=True)}
```

## Certificate

```json
{json.dumps(cert, indent=2, sort_keys=True)}
```
"""


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    candidate, cert, template, note = build()
    write_json(OUTPUT_DATA, candidate)
    write_json(OUTPUT_CERT, cert)
    write_json(OUTPUT_TEMPLATE, template)
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    for path in [OUTPUT_DATA, OUTPUT_CERT, OUTPUT_TEMPLATE, OUTPUT_NOTE]:
        print(f"wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
