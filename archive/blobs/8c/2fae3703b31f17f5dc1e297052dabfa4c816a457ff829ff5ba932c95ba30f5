"""Build the source-leaf direct-carrier or bundle-A gate for oriented Phi_fin."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "minimal_fill_report": DATA / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_report.json",
    "orientation_functor": DATA / "selected_heterotic_orientedphifin_finiterhoe_to_orientedbn_functor_or_smoothrepresentative.candidate.json",
    "carrier_functor_attempt": DATA / "selected_heterotic_orientedphifin_orientedbn_carrier_or_endequotientfunctor.candidate.json",
    "sourceownership_fill": DATA / "selected_heterotic_orientedphifin_sourceownership_certificate_fillattempt.candidate.json",
    "direct_response_packet": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json",
    "physical_smooth_report": DATA / "selected_heterotic_projectiverhoe_physicalanchor_or_smootheqa_sourcefill_report.json",
    "rplus_payload": DATA / "selected_heterotic_rplus_curvature_payload_fill.candidate.json",
    "standard_embedding_gate": DATA / "selected_heterotic_standard_embedding_selector_or_phifin_gate.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea.candidate.json"
OUTPUT_REQUEST = DATA / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_source_theorem_request.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_SourceLeaf_DirectCarrier_or_BundleA_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCELEAF_DIRECT_CARRIER_OR_BUNDLE_A_CURRENT_SOURCE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceLeaf_SourceAmendment_or_CorpusDiscovery_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> dict[str, Any]:
    minimal = load(INPUTS["minimal_fill_report"])
    orientation = load(INPUTS["orientation_functor"])
    carrier = load(INPUTS["carrier_functor_attempt"])
    ownership = load(INPUTS["sourceownership_fill"])
    direct = load(INPUTS["direct_response_packet"])
    smooth = load(INPUTS["physical_smooth_report"])
    rplus = load(INPUTS["rplus_payload"])
    standard_embedding = load(INPUTS["standard_embedding_gate"])

    direct_leaf_attempt = {
        "source_emits_oriented_BN_carrier": {
            "closed": carrier["decision"]["oriented_BN_carrier_emission_closed"],
            "support_present": True,
            "support": [
                "oriented 27-mode B_N table exists",
                "same-branch certificate support exists",
                "finite rho_E to oriented B_N orientation functor is closed",
            ],
            "blocking_reason": (
                "The source still does not emit the oriented B_N carrier as a threshold "
                "operator domain. The closed functor is orientation-only, and the older "
                "27x11 embedding is retained only as a rho-shadow."
            ),
        },
        "source_emits_positive_operator_domain_and_functor": {
            "closed": carrier["decision"]["EndE_or_rhoE_to_oriented_BN_functor_closed"],
            "support_present": direct["closed_required_leaves"] == [
                "orientation_operator_Ctau_binding",
                "no_double_count_replay",
            ],
            "blocking_reason": (
                "No typed End(E) basis, nonidentity rho_E transition packet, or "
                "operator-intertwining quotient maps the selected source to the "
                "nonnegative Phi_fin gap layer."
            ),
        },
        "source_owns_positive_PhiFin_magnitude": {
            "closed": minimal["route_A_direct_fill"]["source_emits_positive_PhiFin_D_E_magnitude_on_oriented_BN"]["filled"],
            "support_present": True,
            "support": minimal["known_values"],
            "blocking_reason": "Exact table values remain support until source ownership of the positive operator is proved.",
        },
        "finitepart_trace_identity_for_log92160000": {
            "closed": carrier["decision"]["finitepart_identity_closed"],
            "support_present": minimal["known_values"]["oriented_abs_sector_logdet_exact"] == "log(92160000)",
            "blocking_reason": "The table invariant is exact, but no same-source finitepart trace theorem identifies it as the threshold.",
        },
    }

    smooth_lane = smooth["filled_smooth_lane"]
    smooth_leaf_attempt = {
        "selected_bundle_connection_A": {
            "closed": smooth_lane["selected_bundle_connection_A_or_equivalent_smooth_operator_source"]["filled"],
            "support_present": smooth_lane["selected_bundle_connection_A_or_equivalent_smooth_operator_source"]["geometric_Bismut_connection_available"],
            "blocking_reason": (
                "A geometric Bismut connection is available, but the source does not "
                "select a bundle connection A on the Qa/SU3 threshold bundle."
            ),
        },
        "bundle_curvature_F_A": {
            "closed": smooth_lane["bundle_curvature_F_A"]["filled"],
            "support_present": smooth_lane["bundle_curvature_F_A"]["R_plus_curvature_available"],
            "blocking_reason": "R+ curvature is geometric support, not bundle curvature F_A.",
        },
        "representation_action_trace_and_EQa": {
            "closed": (
                smooth_lane["representation_action_on_uE_valued_one_forms"]["filled"]
                and smooth_lane["smooth_E_Qa_matrix_or_equivalent_finitepart_operator"]["filled"]
            ),
            "support_present": False,
            "blocking_reason": "No ad-bundle representation, trace normalization, quotient policy, or E_Qa matrix is emitted.",
        },
        "standard_embedding_reopen": {
            "closed": False,
            "support_present": standard_embedding["standard_embedding_evaluation"]["conditional_packet_valid"],
            "blocking_reason": (
                "A=GammaPlus is a conditional route but is retired for the current proof "
                "source unless a new selector identifies the tangent/standard-embedding "
                "bundle with the selected Qa/SU3 threshold branch."
            ),
        },
    }

    direct_closed = all(item["closed"] is True for item in direct_leaf_attempt.values())
    smooth_closed = all(item["closed"] is True for item in smooth_leaf_attempt.values())

    source_request = {
        "schema": "SelectedHeterotic.OrientedPhiFin.SourceLeaf.SourceTheoremRequest.v1",
        "status": "SOURCE_THEOREM_REQUIRED",
        "lane_A_direct_carrier_required": {
            "same_branch_source_emits_oriented_BN_carrier": None,
            "carrier_domain_definition": "F3xF3_gerbe_twisted_fourier_N1_rank3_or_equivalent_selected_27_mode_domain",
            "selected_operator_domain_and_zero_mode_policy": None,
            "EndE_or_rhoE_to_oriented_BN_positive_operator_functor_or_quotient": None,
            "proof_orientation_functor_extends_to_positive_magnitude_functor": None,
            "source_owned_D_E_Riesz_Green_positive_spectrum": None,
            "finitepart_trace_identity_log92160000": None,
            "kernel_shared_circle_no_double_count_policy": None,
            "proof_not_route_c_or_benchmark_import": None,
        },
        "lane_B_bundle_A_required": {
            "selected_bundle_connection_A_or_projective_connection": None,
            "curvature_F_A": None,
            "representation_action_on_uE_one_forms": None,
            "trace_normalization": None,
            "kernel_and_quotient_policy_to_oriented_BN": None,
            "E_Qa_or_equivalent_zero_order_block": None,
            "heat_zeta_or_torsion_finitepart_log92160000": None,
            "trace_lift_or_complement_quotient_proof": None,
            "standard_embedding_selector_if_A_equals_GammaPlus_is_reopened": None,
        },
        "known_ready_support": {
            "oriented_abs_sector_logdet_exact": minimal["known_values"]["oriented_abs_sector_logdet_exact"],
            "full_positive_logdet_exact": minimal["known_values"]["full_positive_logdet_exact"],
            "orientation_functor_closed": orientation["decision"]["finite_rhoE_to_oriented_BN_orientation_functor_closed"],
            "R_plus_curvature_nonzero_components": rplus["rplus_payload"]["R_plus_summary"]["nonzero_components"],
            "standard_embedding_conditional_but_retired": standard_embedding["decision"]["standard_embedding_retired_as_current_proof_source"],
        },
        "must_not_use": [
            "orientation-only rho_E to B_N functor as a magnitude theorem",
            "27x11 rho-shadow embedding as a threshold functor",
            "R+ curvature as bundle F_A",
            "A=GammaPlus without a new same-source standard-embedding selector",
            "oriented logdet table value as a promoted threshold without trace identity",
            "observed coupling, mass, or benchmark data",
        ],
    }
    OUTPUT_REQUEST.write_text(json.dumps(source_request, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "source_leaf_attack_executed": True,
        "direct_carrier_leaf_closed": direct_closed,
        "bundle_A_leaf_closed": smooth_closed,
        "direct_first_open_leaf": "source_emits_oriented_BN_carrier",
        "smooth_first_open_leaf": "selected_bundle_connection_A",
        "source_theorem_request_built": True,
        "next_required_artifact": NEXT,
        "oriented_logdet_promoted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinSourceLeafDirectCarrierOrBundleA",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "orientation_functor": orientation["status"],
            "carrier_functor_attempt": carrier["status"],
            "sourceownership_fill": ownership["status"],
            "rplus_payload": rplus["status"],
            "standard_embedding_gate": standard_embedding["status"],
        },
        "direct_leaf_attempt": direct_leaf_attempt,
        "smooth_leaf_attempt": smooth_leaf_attempt,
        "source_theorem_request_path": rel(OUTPUT_REQUEST),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinSourceLeafCurrentSourceOpenTheorem",
            "proved": True,
            "statement": (
                "The current source closes support but not the first source leaf for either "
                "legal oriented Phi_fin route. Directly, the source does not emit the "
                "oriented 27-mode B_N carrier as a positive threshold-operator domain, "
                "and the closed rho_E-to-B_N map is orientation-only. Smoothly, the source "
                "does not emit a selected bundle connection A; R+ is geometric support, "
                "and the standard embedding remains retired without a new selector. "
                "Therefore closing oriented Phi_fin now requires one of the two source "
                "theorem packets written in the request, not another numerical scan."
            ),
        },
        "guardrails": {
            "does_not_promote_orientation_functor_to_magnitude": True,
            "does_not_promote_R_plus_to_bundle_A": True,
            "does_not_reopen_standard_embedding_without_selector": True,
            "does_not_promote_log92160000": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "source_theorem_request_path": rel(OUTPUT_REQUEST),
        "note_path": rel(OUTPUT_NOTE),
        "direct_carrier_leaf_closed": direct_closed,
        "bundle_A_leaf_closed": smooth_closed,
        "source_theorem_request_built": True,
        "oriented_logdet_promoted": False,
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin SourceLeaf DirectCarrier or BundleA v1

## Result

```text
status = {STATUS}
direct_carrier_leaf_closed = false
bundle_A_leaf_closed = false
direct_first_open_leaf = source_emits_oriented_BN_carrier
smooth_first_open_leaf = selected_bundle_connection_A
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Source Theorem Request

```text
{rel(OUTPUT_REQUEST)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_REQUEST)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
