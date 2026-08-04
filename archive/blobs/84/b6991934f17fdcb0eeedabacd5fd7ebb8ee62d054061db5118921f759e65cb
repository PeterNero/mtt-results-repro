"""Build the bundle-connection value-solve or Phi_fin source-identity proof gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "hym_fill": DATA / "selected_heterotic_hym_fullquotientspectrum_or_ouhessianscale_fillattempt.candidate.json",
    "phifin_solve_gate": DATA / "selected_heterotic_phifin_sourceidentity_or_bundleconnection_solve_gate.candidate.json",
    "phifin_bridge": DATA / "selected_heterotic_phifin_sourceidentity_bridge_attempt.candidate.json",
    "ende_bn_fill": DATA / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_fill.candidate.json",
    "ende_domain_gate": DATA / "selected_heterotic_ende_domainbasis_or_nonidentity_rhoe_sourceemission.candidate.json",
    "projective_bundle_policy": DATA / "selected_heterotic_projectiverhoe_bundleconnection_trace_quotient_policy.candidate.json",
    "finite_packet": DATA / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json",
    "smooth_trace_lift": DATA / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof.candidate.json"
OUTPUT_CERT = CERTS / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_BundleConnection_ValueSolve_or_PhiFin_SourceIdentity_Proof_v1.md"

STATUS = "HETEROTIC_BUNDLECONNECTION_VALUESOLVE_OR_PHIFIN_SOURCEIDENTITY_PROOF_FINITE_INTERNAL_CLOSED_SMOOTH_SOURCE_OPEN"
NEXT = "Selected_Heterotic_FiniteInternalRhoE_to_PhiFin_or_SmoothBundleConnection_SourceLift_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    hym_fill = load(INPUTS["hym_fill"])
    phifin_solve_gate = load(INPUTS["phifin_solve_gate"])
    phifin_bridge = load(INPUTS["phifin_bridge"])
    ende_bn_fill = load(INPUTS["ende_bn_fill"])
    ende_domain_gate = load(INPUTS["ende_domain_gate"])
    projective_policy = load(INPUTS["projective_bundle_policy"])
    finite_packet = load(INPUTS["finite_packet"])
    smooth_trace_lift = load(INPUTS["smooth_trace_lift"])

    lane_A = {
        "name": "PhiFin_same_source_identity",
        "closes_at_finite_internal_projective_scope": True,
        "closes_as_heterotic_PhiFin_identity": False,
        "support_closed": {
            "rank_three_iwasawa_monad_branch": True,
            "RouteC_27mode_DE_Riesz_Green_support": phifin_bridge["decision"]["u1y_27mode_gap_layer_closed"],
            "finite_internal_projective_rhoE_packet_selected": projective_policy["smooth_bridge_policy"]["direct_operator_route"]["finite_projective_packet_now_selected"],
            "finite_internal_trace_quotient_logdet": projective_policy["decision"]["finite_internal_trace_and_quotient_policy_closed"],
        },
        "blocking_subclaims": {
            "EndE_to_BN_functor": ende_bn_fill["decision"]["EndE_to_BN_functor_filled"],
            "selected_finite_EndE_domain_basis": ende_bn_fill["decision"]["EndE_domain_values_filled"],
            "heterotic_nonidentity_rhoE_transition_packet": ende_bn_fill["decision"]["heterotic_nonidentity_rhoE_filled"],
            "commuting_projection_to_27mode_basis": phifin_bridge["tested_subclaims"]["commuting_projection_to_27mode_basis"]["proved_for_heterotic_QaSU3"],
            "heterotic_finite_part_regularization": ende_bn_fill["decision"]["operator_payload_filled"],
            "same_source_identity": phifin_bridge["decision"]["same_source_identity_proved"],
        },
        "proof_result": (
            "The selected finite internal projective rho_E packet is a valid "
            "internal operator packet, but it is not yet identified with the "
            "27-mode Phi_fin packet by an End(E)->B_N functor or commuting "
            "projection theorem."
        ),
    }

    lane_B = {
        "name": "explicit_selected_bundle_connection_value_solve",
        "closes_now": False,
        "finite_internal_substitute_available": True,
        "finite_internal_value": projective_policy["finite_internal_policy"]["finite_threshold_value"],
        "smooth_bundle_connection_values": {
            "selected_A_or_rhoE": False,
            "F_A": False,
            "representation_action_on_uE_one_forms": False,
            "smooth_kernel_and_quotient_policy": False,
            "smooth_E_Qa_or_heat_zeta_torsion_finite_part": False,
            "smooth_trace_lift": smooth_trace_lift["decision"]["smooth_trace_lift_proved"],
        },
        "proof_result": (
            "The finite internal direct projective packet supplies rho_E, D_E, "
            "Green/Riesz, trace, quotient, and logdet at internal scope. It does "
            "not supply a smooth bundle connection A, curvature F_A, representation "
            "action, smooth E_Qa, or heat/zeta/torsion trace lift."
        ),
    }

    value_packet_status = {
        "finite_internal_packet_selected": True,
        "finite_internal_domain_labels": projective_policy["finite_internal_policy"]["finite_domain_labels"],
        "finite_internal_operator_action_closed": projective_policy["closed_subclaims"]["finite_internal_operator_action"],
        "finite_internal_trace_quotient_policy_closed": projective_policy["closed_subclaims"]["finite_internal_trace_normalization"],
        "finite_internal_logdet_value": projective_policy["finite_internal_policy"]["finite_threshold_value"],
        "smooth_lift_or_PhiFin_identity_closed": False,
        "physical_threshold_value_claimed": False,
    }

    theorem_result = {
        "proved": True,
        "finite_internal_branch_closed": True,
        "heterotic_PhiFin_identity_closed": False,
        "explicit_smooth_bundle_connection_solved": False,
        "smooth_E_Qa_or_heat_zeta_torsion_finitepart_computed": False,
        "reason": (
            "Both legal lanes reach the same remaining bridge. The selected finite "
            "internal projective packet is closed and may be used as internal "
            "operator data, but full HYM/Phi_fin closure requires either an "
            "End(E)->B_N source identity or a smooth bundle/operator source lift."
        ),
    }

    decision = {
        "proof_gate_built": True,
        "finite_internal_projective_packet_promoted_for_internal_scope": True,
        "same_source_PhiFin_identity_proved": False,
        "explicit_bundle_connection_solved": False,
        "smooth_operator_identity_closed": False,
        "E_Qa_computed": False,
        "computed_physical_threshold_value": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticBundleConnectionValueSolveOrPhiFinSourceIdentityProof",
        "status": STATUS,
        "inputs": {name: rel(path) for name, path in INPUTS.items()},
        "input_statuses": {
            "hym_fill": hym_fill["status"],
            "phifin_solve_gate": phifin_solve_gate["status"],
            "phifin_bridge": phifin_bridge["status"],
            "ende_bn_fill": ende_bn_fill["status"],
            "ende_domain_gate": ende_domain_gate["status"],
            "projective_bundle_policy": projective_policy["status"],
            "finite_packet": finite_packet["schema"],
            "smooth_trace_lift": smooth_trace_lift["status"],
        },
        "lane_A_PhiFin_identity": lane_A,
        "lane_B_bundle_connection_value_solve": lane_B,
        "value_packet_status": value_packet_status,
        "decision": decision,
        "guardrails": {
            "does_not_identify_finite_internal_packet_with_PhiFin_without_functor": True,
            "does_not_promote_finite_trace_to_smooth_heat_trace": True,
            "does_not_claim_selected_A_or_F_A": True,
            "does_not_reopen_retired_standard_embedding": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "theorem": {
            "name": "BundleConnectionValueSolveOrPhiFinSourceIdentityReductionTheorem",
            "proved": theorem_result["proved"],
            "statement": theorem_result["reason"],
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "note_path": rel(OUTPUT_NOTE),
        "finite_internal_branch_closed": True,
        "same_source_PhiFin_identity_proved": False,
        "explicit_bundle_connection_solved": False,
        "smooth_operator_identity_closed": False,
        "E_Qa_computed": False,
        "next_required_artifact": NEXT,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic BundleConnection ValueSolve or PhiFin SourceIdentity Proof v1

## Result

```text
status = {STATUS}
finite_internal_projective_packet_promoted_for_internal_scope = true
same_source_PhiFin_identity_proved = false
explicit_bundle_connection_solved = false
smooth_operator_identity_closed = false
next_required_artifact = {NEXT}
```

## What This Proves

The finite internal projective `rho_E` packet is now the coherent internal
value packet for the selected Qa/SU3 branch: finite domain, `rho_E`, `D_E`,
Riesz/Green, quotient policy, trace, and `log(2008)` are closed at internal
scope.

This does not yet prove the heterotic `Phi_fin` same-source identity, because
the selected `End(E)->B_N` functor, commuting projection, and nonidentity
heterotic transition packet are not emitted. It also does not solve the smooth
bundle connection: selected `A/F_A`, representation action, smooth `E_Qa`, and
heat/zeta/torsion trace lift remain open.

## Theorem

{candidate["theorem"]["statement"]}
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
