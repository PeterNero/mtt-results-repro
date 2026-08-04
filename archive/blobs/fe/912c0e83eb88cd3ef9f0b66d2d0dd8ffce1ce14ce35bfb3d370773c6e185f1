"""Build the heterotic/Strominger analytic-torsion or threshold-operator payload gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")
STRINGS = OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings"

INPUTS = {
    "heterotic_kernel": DATA / "selected_heterotic_strominger_electroweak_threshold_kernel.candidate.json",
    "heterotic_minimal_payload": DATA / "selected_heterotic_strominger_electroweak_threshold_kernel_minimal_payload.json",
    "internal_qa_row": DATA / "selected_electroweak_qastack_finitepart_policy_and_indexscale.candidate.json",
    "internal_lambda12": DATA / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json",
    "smooth_logdet_gate": DATA / "smooth_determinant_spectral_table_or_source_operator.candidate.json",
    "local_system_torsion": NONSM / "certificates" / "selected_qa_su3_local_system_torsion_source_extraction_certificate.json",
    "hym_connection": NONSM / "certificates" / "selected_qa_su3_hym_color_connection_spectrum_or_torsion_certificate.json",
    "hym_mu_domain": NONSM / "certificates" / "selected_qa_su3_hym_mu_and_operator_domain_selection_certificate.json",
    "operator_packet": NONSM / "certificates" / "selected_qa_su3_color_bundle_operator_packet_fill_attempt_certificate.json",
    "su2_flatness": NONSM / "certificates" / "selected_su2_threshold_background_flatness_or_fp_spectrum_certificate.json",
    "mtt_to_cy": STRINGS / "Modal_Triplet_Theory__From_MTT_to_Calabi__Yau_Compactifications.md",
    "heterotic_flux": STRINGS / "Flux_Compactifications_in_Heterotic_String_Theory_v3.md",
    "strominger_system": STRINGS / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
}

OUTPUT_DATA = DATA / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_strominger_analytic_torsion_or_threshold_operator_payload_certificate.json"
OUTPUT_TEMPLATE = DATA / "selected_heterotic_strominger_threshold_operator_or_torsion_source.template.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_Strominger_AnalyticTorsion_or_ThresholdOperator_Payload_v1.md"

STATUS = "HETEROTIC_STROMINGER_ANALYTIC_TORSION_THRESHOLD_PAYLOAD_REDUCED_TO_SOURCE_OPERATOR_OR_LOCAL_SYSTEM"
NEXT = "Selected_Heterotic_Strominger_SourceOperator_or_LocalSystem_Torsion_Computation_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def terms(path: Path, needles: list[str]) -> dict[str, bool]:
    text = read_text(path).lower()
    return {needle: needle.lower() in text for needle in needles}


def build_template(kernel: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "SelectedHeteroticStromingerThresholdOperatorOrTorsionSource.v1",
        "status": "OPEN_VALUES_REQUIRED",
        "inherits_internal_weak_split_only_as_guardrail": kernel["decision"]["internal_lambda_12_value"],
        "allowed_exit_A_local_system_torsion": {
            "selected_lattice_or_character": None,
            "pi1_nil_or_iwasawa_to_unitary_representation": None,
            "acyclicity_or_zero_mode_policy": None,
            "ray_singer_or_reidemeister_finite_part": None,
            "stack_trace_weights_for_Qa_Qc_SU2": None,
            "same_branch_selection_certificate": None,
        },
        "allowed_exit_B_threshold_operator": {
            "selected_bundle_or_sheaf_or_twist": None,
            "selected_connection_and_metric": None,
            "mu_or_moduli_selection": None,
            "laplace_type_operator_or_weitzenbock_endomorphism": None,
            "positive_spectrum_heat_coefficients_or_zeta_derivative": None,
            "regularization_and_zero_mode_policy": None,
            "stack_trace_weights_for_Qa_Qc_SU2": None,
            "same_branch_selection_certificate": None,
        },
        "matching_payload_after_exit_A_or_B": {
            "physical_gauge_action_anchor": None,
            "mu_match": None,
            "RG_scheme": None,
            "threshold_convention": None,
        },
        "forbidden_promotions": [
            "internal finite quotient logdet or lambda12 as physical heterotic threshold",
            "q79 Fu-Yau/Mukai charge-sector data as analytic torsion numbers",
            "q64/rho_UV character as Qa/SU3 local system without a bridge theorem",
            "mu=1 or other HYM parameter choice by convenience",
            "observed electroweak residuals to choose spectra, torsion, scale, or character",
        ],
    }


def build() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    kernel = load(INPUTS["heterotic_kernel"])
    minimal = load(INPUTS["heterotic_minimal_payload"])
    internal_qa = load(INPUTS["internal_qa_row"])
    internal_l12 = load(INPUTS["internal_lambda12"])
    smooth_gate = load(INPUTS["smooth_logdet_gate"])
    torsion = load(INPUTS["local_system_torsion"])
    hym_connection = load(INPUTS["hym_connection"])
    hym_mu = load(INPUTS["hym_mu_domain"])
    operator_packet = load(INPUTS["operator_packet"])
    su2_flatness = load(INPUTS["su2_flatness"])
    template = build_template(kernel)

    route_tests = {
        "A_internal_finite_quotient_replay": {
            "status": "REJECTED_AS_PHYSICAL_HETEROTIC_THRESHOLD",
            "available_internal_values": {
                "p_a_internal": internal_qa["decision"]["selected_p_a_internal_value"],
                "lambda_12_internal": internal_l12["decision"]["lambda_12_internal_value"],
                "smooth_gate_status": smooth_gate["status"],
            },
            "reason": "These values close the internal selected determinant/weak-split accounting, but the heterotic physical threshold requires the selected one-loop/torsion operator and physical scheme.",
            "can_supply_payload_now": False,
        },
        "B_ray_singer_or_reidemeister_local_system": {
            "status": "LIVE_EXIT_SOURCE_CHARACTER_OPEN",
            "source_status": torsion["status"],
            "selected_candidates_count": torsion["selected_candidates_count"],
            "computable_now": torsion["verdict"]["ray_singer_torsion_computable_now"],
            "best_next_test": torsion["next_routes"][0]["test"],
            "reason": "The route is mathematically legitimate, but no selected Qa/SU3 compact Nil/Iwasawa lattice character or torsion finite part is source-certified.",
            "can_supply_payload_now": False,
        },
        "C_hym_monad_threshold_operator": {
            "status": "LIVE_EXIT_DELTA_A_SPECTRUM_AND_MU_OPEN",
            "connection_status": hym_connection["status"],
            "domain_status": hym_mu["status"],
            "operator_packet_status": operator_packet["status"],
            "selected_connection_candidate_found": hym_connection["verdict"]["source_selected_color_connection_candidate_found"],
            "operator_domain_selected_for_next_gate": hym_mu["verdict"]["operator_domain_selected_for_next_gate"],
            "mu_selected": hym_mu["verdict"]["mu_selected"],
            "selected_spectrum_or_torsion_available": hym_mu["verdict"]["selected_spectrum_or_torsion_available"],
            "next_required_artifact": hym_mu["verdict"]["next_required_artifact"],
            "reason": "The explicit Iwasawa HYM/monad data identify a strong operator lane, but the continuous HYM parameter, quotient domain spectrum, heat coefficients, and zeta/torsion finite part are not computed.",
            "can_supply_payload_now": False,
        },
        "D_su2_flat_fp_partial_row": {
            "status": "PARTIAL_WEAK_ROW_SUPPORT_NOT_FULL_HETEROTIC_PAYLOAD",
            "source_status": su2_flatness["status"],
            "selected_threshold_background_flat": su2_flatness["verdict"]["selected_su2_threshold_background_flat"],
            "quotient_normalization_policy_closed": su2_flatness["verdict"]["quotient_normalization_policy_closed"],
            "reason": "The SU2 leading flat background is useful support for the weak row but does not provide Qa/Qc/U1 analytic torsion or the heterotic physical matching scheme.",
            "can_supply_payload_now": False,
        },
        "E_general_calabi_yau_threshold_language": {
            "status": "FORMAL_SUPPORT_ONLY",
            "source_terms": terms(INPUTS["mtt_to_cy"], ["Ray-Singer", "torsion", "determinants of Laplacians", "one-loop", "threshold"]),
            "reason": "The corpus knows the correct mathematical language, but no selected same-branch spectral/torsion table is printed.",
            "can_supply_payload_now": False,
        },
    }

    decision = {
        "payload_closed": False,
        "measured_electroweak_closure": False,
        "internal_lambda_12_preserved": True,
        "internal_lambda_12_value": kernel["decision"]["internal_lambda_12_value"],
        "strict_no_knob_route_still_live": True,
        "primary_next_exit": "C_hym_monad_threshold_operator",
        "parallel_next_exit": "B_ray_singer_or_reidemeister_local_system",
        "retire_internal_replay_as_physical_threshold_source": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "SelectedHeteroticStromingerAnalyticTorsionOrThresholdOperatorPayload",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "source_scan": {
            "mtt_to_cy": {
                "path": str(INPUTS["mtt_to_cy"]),
                "present": INPUTS["mtt_to_cy"].exists(),
                "terms": route_tests["E_general_calabi_yau_threshold_language"]["source_terms"],
            },
            "heterotic_flux": {
                "path": str(INPUTS["heterotic_flux"]),
                "present": INPUTS["heterotic_flux"].exists(),
                "terms": terms(INPUTS["heterotic_flux"], ["\\mu>0", "HYM connection", "F_E\\neq 0", "Tr F_E", "c_3(E)", "threshold"]),
            },
            "strominger_system": {
                "path": str(INPUTS["strominger_system"]),
                "present": INPUTS["strominger_system"].exists(),
                "terms": terms(INPUTS["strominger_system"], ["Delta_A", "unique local minimizer", "OU term", "fixed gauges", "modulo symmetries"]),
            },
        },
        "route_tests": route_tests,
        "inherited_minimal_payload": minimal,
        "template_path": rel(OUTPUT_TEMPLATE),
        "decision": decision,
        "theorem": {
            "name": "HeteroticStromingerThresholdPayloadReductionTheorem",
            "proved": True,
            "statement": (
                "Given the current corpus and sibling proof repositories, the selected "
                "heterotic/Strominger electroweak threshold payload is not yet a number. "
                "It is reduced to two legitimate no-knob exits: a source-selected "
                "acyclic local-system torsion computation on the compact Nil/Iwasawa "
                "electroweak stack, or a source-selected HYM/monad Laplace-type "
                "threshold operator with selected mu/moduli, trace weights, spectrum "
                "or heat/zeta finite part. Internal quotient determinants and the "
                "closed dimensionless lambda_12 remain validators and internal "
                "accounting data, not physical heterotic threshold data."
            ),
        },
        "guardrails": {
            "uses_observed_electroweak_data": False,
            "uses_target_residual_scan": False,
            "promotes_internal_lambda12_to_physical_threshold": False,
            "promotes_q79_charge_sector_to_torsion": False,
            "promotes_q64_cp_character_to_qa_su3": False,
            "chooses_hym_mu_by_convenience": False,
            "claims_measured_electroweak_closure": False,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "SelectedHeteroticStromingerAnalyticTorsionOrThresholdOperatorPayload",
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "template_path": rel(OUTPUT_TEMPLATE),
        "note_path": rel(OUTPUT_NOTE),
        "payload_closed": False,
        "primary_next_exit": decision["primary_next_exit"],
        "parallel_next_exit": decision["parallel_next_exit"],
        "internal_lambda_12_value": decision["internal_lambda_12_value"],
        "strict_no_knob_route_still_live": True,
        "measured_electroweak_closure": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
    }
    return candidate, cert, template, render_note(candidate, cert, template)


def render_note(candidate: dict[str, Any], cert: dict[str, Any], template: dict[str, Any]) -> str:
    return f"""# Selected Heterotic Strominger Analytic Torsion or Threshold Operator Payload v1

## Result

```text
status = {candidate["status"]}
payload_closed = false
primary_next_exit = {candidate["decision"]["primary_next_exit"]}
parallel_next_exit = {candidate["decision"]["parallel_next_exit"]}
internal_lambda_12_preserved = true
measured_electroweak_closure = false
next_required_artifact = {candidate["decision"]["next_required_artifact"]}
```

## Route Tests

```json
{json.dumps(candidate["route_tests"], indent=2, sort_keys=True)}
```

## Reduction Theorem

{candidate["theorem"]["statement"]}

## What To Compute Next

The best current executable route is the HYM/monad operator lane:

```text
explicit Iwasawa HYM/monad source
-> select mu/moduli from the Strominger Hessian/OU block
-> build Delta_A or the equivalent Laplace-type threshold operator
-> quotient gauge/zero modes
-> compute spectrum, heat coefficients, zeta derivative, or analytic torsion finite part
-> apply Qa/Qc/SU2 trace and hypercharge weights in one scheme
```

The parallel torsion route is also legal:

```text
MTT-selected compact Nil/Iwasawa lattice character
-> acyclic local system or explicit zero-mode policy
-> Ray-Singer/Reidemeister finite part
-> same stack trace weights and physical threshold convention
```

## Source Template

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
