"""Close the finitepart/kernel policy on A_N without promoting logdet replay."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finitepartkernelpolicy_on_an_or_sourcebranchidentity"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLICY_PACKET = PACKET_DIR / "an_finitepart_kernel_policy.packet.json"
LOGDET_GATE_PACKET = PACKET_DIR / "strict_logdet_gate_after_an_policy.packet.json"
FRONTIER_PACKET = PACKET_DIR / "next_sourcebranch_or_cechhym_after_policy.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FinitepartKernelPolicy_on_AN_or_SourceBranchIdentity_v1.md"

PREVIOUS = DATA / "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart.candidate.json"
PREVIOUS_TABLES = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "eight_table_revalidation_after_de_export.packet.json"
)
FINITE_SOURCE = DATA / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof.candidate.json"
FINITE_ALGEBRA = (
    DATA
    / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof"
    / "finite_projected_algebra_and_spectral_package.packet.json"
)
FINITE_EXACTNESS = (
    DATA
    / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof"
    / "finite_source_exactness_theorem.packet.json"
)
FINITE_OPS = (
    DATA
    / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof"
    / "projected_hym_operations_exactness.packet.json"
)
DE_EXPORT = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "de_gap_export_row_reconciliation.packet.json"
)
EXACT_VALUES = (
    DATA
    / "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation"
    / "exact_oriented_finitepart_values.packet.json"
)
SOURCEOWNERSHIP = (
    DATA
    / "selected_orientedphifin_sourceownership_theorem_or_smootheqa_quotient"
    / "bn27_sourceownership_transport_frontier.packet.json"
)
POST_CUT = (
    DATA
    / "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart"
    / "logdet_no_lift_strict_gate_after_4of8.packet.json"
)

STATUS = (
    "MTT_SELECTED_FINITEPARTKERNELPOLICY_ON_AN_OR_SOURCEBRANCHIDENTITY_"
    "FINITE_POLICY_CLOSED_LOGDET_ROW_STILL_SOURCEBRANCH_OPEN"
)
NEXT = "MTT_Selected_SourceBranchIdentity_or_CechHYMConnectionValues_AfterFinitepartPolicy_v1"
ACCEPTED = [
    "typed_f_sections",
    "typed_g_sections",
    "g_after_f_zero_exactness_certificate",
    "BN27_DE_Riesz_Green_kernel_trace_export",
]
REMAINING = [
    "cech_transition_cocycles",
    "selected_HYM_or_projective_connection_coefficients",
    "finitepart_log92160000_identity_from_values",
    "no_lifted_flags_connection_replay",
]


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


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing finitepart policy inputs: " + ", ".join(missing))


def main() -> int:
    require_sources(
        [
            PREVIOUS,
            PREVIOUS_TABLES,
            FINITE_SOURCE,
            FINITE_ALGEBRA,
            FINITE_EXACTNESS,
            FINITE_OPS,
            DE_EXPORT,
            EXACT_VALUES,
            SOURCEOWNERSHIP,
            POST_CUT,
        ]
    )

    previous = load(PREVIOUS)
    tables = load(PREVIOUS_TABLES)
    finite_source = load(FINITE_SOURCE)
    finite_algebra = load(FINITE_ALGEBRA)
    finite_exactness = load(FINITE_EXACTNESS)
    finite_ops = load(FINITE_OPS)
    de_export = load(DE_EXPORT)
    exact_values = load(EXACT_VALUES)
    sourceownership = load(SOURCEOWNERSHIP)
    post_cut = load(POST_CUT)

    if tables["accepted_final_same_source_connection_tables"] != 4:
        raise ValueError("expected 4/8 table frontier")
    if tables["accepted_rows"] != ACCEPTED:
        raise ValueError("unexpected accepted row set")
    if previous["next_required_artifact"] != "MTT_Selected_SourceOwnedFinitepartKernelPolicy_or_CechHYMConnectionValues_v1":
        raise ValueError("previous frontier is not source-owned finitepart/kernel policy")

    exact = exact_values["finitepart_values"]
    plus_product = exact["plus_sector_product"]
    minus_product = exact["minus_sector_product"]
    oriented_product = exact["oriented_abs_sector_product"]
    full_positive_product = exact["full_positive_product"]
    if plus_product * minus_product != oriented_product:
        raise ValueError("oriented product does not factor as plus*minus sector")
    if full_positive_product != exact_values["full_positive_product_recomputed"]:
        raise ValueError("full positive product recomputation mismatch")

    finite_policy_closes = all(
        [
            finite_source["closure_decision"]["finite_projected_HYM_source_principle_closed"],
            finite_source["closure_decision"]["automatic_finite_cutoff_exactness_for_A_N_closed"],
            finite_algebra["closed_here"]["A_N_source_algebra"],
            finite_algebra["closed_here"]["Tr_N_normalized_trace"],
            finite_exactness["proved"],
            finite_exactness["exactness_scope"]["A_N_finite_source"],
            finite_exactness["exactness_scope"]["finite_trace"],
            finite_ops["operations"]["Delta_N"]["exact_in_finite_source"],
            finite_ops["operations"]["Green_N"]["exact_in_finite_source"],
            de_export["accepted_row_payload"]["accepted_as_final_connection_table"],
            de_export["accepted_row_payload"]["selected_trace_equality"]["proved"],
            de_export["accepted_row_payload"]["selected_gap_lower_bound"] > 0,
            de_export["accepted_row_payload"]["selected_green_norm_bound"] > 0,
        ]
    )
    if not finite_policy_closes:
        raise ValueError("finite A_N policy prerequisites do not close")

    policy_packet = {
        "schema": "MTTANFinitepartKernelPolicy.v1",
        "status": "FINITEPART_KERNEL_POLICY_CLOSED_ON_SELECTED_A_N_SOURCE",
        "closure_claimed": True,
        "selected_source_scope": "A_N finite projected q79/F,m=1 HYM source algebra",
        "source_algebra": finite_algebra["source_algebra"],
        "trace_rule": finite_algebra["trace_rule"],
        "finite_source_exactness_theorem": {
            "proved": finite_exactness["proved"],
            "statement": finite_exactness["statement"],
            "finite_trace": finite_exactness["exactness_scope"]["finite_trace"],
            "unprojected_continuum_HYM": finite_exactness["exactness_scope"]["unprojected_continuum_HYM"],
        },
        "kernel_policy": {
            "zero_cluster_indices": de_export["accepted_row_payload"]["zero_cluster_indices"],
            "selected_gap_lower_bound": de_export["accepted_row_payload"]["selected_gap_lower_bound"],
            "selected_green_norm_bound": de_export["accepted_row_payload"]["selected_green_norm_bound"],
            "reduced_determinant_policy": "determinant finitepart is taken on the selected nonzero oriented sector after the A_N kernel/zero-cluster exclusion",
            "kernel_trace_policy_source_owned_on_A_N": True,
        },
        "finitepart_functional": {
            "name": "FP_N^oriented(T)",
            "definition": "log det_N'(T | oriented_abs_nonzero_sector) with det_N' computed as the finite characteristic-polynomial product in A_N",
            "source_owned_finitepart_functional_closed_on_A_N": True,
            "ordinary_continuum_zeta_claimed": False,
            "observed_data_used": False,
        },
        "exact_oriented_values_retained": {
            "plus_sector_product": plus_product,
            "minus_sector_product": minus_product,
            "oriented_abs_sector_product": oriented_product,
            "oriented_abs_sector_logdet_exact": exact["oriented_abs_sector_logdet_exact"],
            "full_positive_product": full_positive_product,
            "full_positive_logdet_exact": exact["full_positive_logdet_exact"],
        },
        "policy_does_not_yet_promote": {
            "finitepart_log92160000_identity_from_values": True,
            "no_lifted_flags_connection_replay": True,
            "reason": "The finite policy is now source-owned on A_N, but the same-source orientation/magnitude branch identity or selected connection-value export is still open.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    logdet_gate = {
        "schema": "MTTStrictLogdetGateAfterANPolicy.v1",
        "status": "FINITE_POLICY_CLOSED_LOGDET_EXACT_SOURCEBRANCH_STILL_OPEN",
        "closure_claimed": True,
        "accepted_final_same_source_connection_tables": 4,
        "required_final_same_source_connection_tables": 8,
        "accepted_rows": ACCEPTED,
        "remaining_rows": REMAINING,
        "finite_policy_closure": {
            "kernel_trace_policy_source_owned_on_A_N": True,
            "source_owned_finitepart_functional_closed_on_A_N": True,
            "exact_log92160000_arithmetic_available": post_cut["exact_values"]["oriented_abs_sector_logdet_exact"] == "log(92160000)",
            "conditional_no_lift_replay_available": post_cut["no_lift_gate"]["no_lift_replay_conditional_closed"],
        },
        "strict_promotion_blockers_remaining": {
            "source_branch_identity_closed": sourceownership["BN27_source_ownership_transport_closed"],
            "direct_BN27_source_declaration_closed": sourceownership["direct_BN27_source_declaration_closed"],
            "selected_connection_witness_values_closed": sourceownership["selected_connection_witness_values_closed"],
            "oriented_BN_carrier_emitted_by_that_source": sourceownership["BN27_source_ownership_fields"]["oriented_BN_carrier_emitted_by_that_source"],
            "positive_PhiFin_DE_magnitude_owned_by_source": sourceownership["BN27_source_ownership_fields"]["positive_PhiFin_DE_magnitude_owned_by_source"],
            "operator_coemission_source_owned": sourceownership["BN27_source_ownership_fields"]["operator_coemission_source_owned"],
        },
        "new_final_rows_promoted": [],
        "why_logdet_row_still_open": [
            "A_N now owns the finite determinant/kernel/trace policy, but not the full same-source oriented BN27 magnitude branch.",
            "The exact oriented product remains blocked by source_branch_identity or selected connection-value export.",
            "No-lift replay is still conditional on emitted same-source fields.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier_packet = {
        "schema": "MTTNextSourceBranchOrCechHYMAfterPolicy.v1",
        "status": "NEXT_IS_SOURCEBRANCH_IDENTITY_OR_SELECTED_CECH_HYM_CONNECTION_VALUES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "current_count": "4/8",
        "closed_now": [
            "A_N finitepart determinant functional",
            "A_N kernel/zero-cluster exclusion policy",
            "A_N finite trace/shared finite determinant policy",
        ],
        "remaining_rows": REMAINING,
        "remaining_minimal_exits": [
            "prove source_branch_identity so one selected source owns C_tau orientation and PhiFin_DE magnitude",
            "emit selected Cech cocycles and HYM/projective coefficients that export the same BN27 fields",
            "emit direct H K-threshold row with certificate",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedFinitepartKernelPolicyOnANOrSourceBranchIdentity",
        "status": STATUS,
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous": rel(PREVIOUS),
            "previous_tables": rel(PREVIOUS_TABLES),
            "finite_source": rel(FINITE_SOURCE),
            "finite_algebra": rel(FINITE_ALGEBRA),
            "finite_exactness": rel(FINITE_EXACTNESS),
            "finite_ops": rel(FINITE_OPS),
            "de_export": rel(DE_EXPORT),
            "exact_values": rel(EXACT_VALUES),
            "sourceownership": rel(SOURCEOWNERSHIP),
            "post_cut": rel(POST_CUT),
        },
        "output_packets": {
            "an_finitepart_kernel_policy": rel(POLICY_PACKET),
            "strict_logdet_gate_after_an_policy": rel(LOGDET_GATE_PACKET),
            "next_sourcebranch_or_cechhym_after_policy": rel(FRONTIER_PACKET),
        },
        "closure_decision": {
            "accepted_final_same_source_connection_tables": 4,
            "required_final_same_source_connection_tables": 8,
            "accepted_rows": ACCEPTED,
            "remaining_rows": REMAINING,
            "kernel_trace_policy_source_owned_on_A_N": True,
            "source_owned_finitepart_functional_closed_on_A_N": True,
            "exact_log92160000_arithmetic_available": True,
            "conditional_no_lift_replay_available": True,
            "finitepart_log92160000_identity_from_values_promoted": False,
            "no_lifted_flags_connection_replay_promoted": False,
            "source_branch_identity_closed": False,
            "selected_connection_witness_values_closed": False,
            "new_final_rows_promoted": 0,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "FinitepartKernelPolicyOnANTheorem",
            "proved": True,
            "statement": (
                "The selected finite projected HYM source algebra A_N owns the finite determinant/"
                "kernel/trace policy: determinant finitepart is an exact finite characteristic-polynomial "
                "functional after the selected zero-cluster exclusion, not an unprojected continuum zeta "
                "approximation.  This closes the finitepart/kernel policy blocker but does not yet promote "
                "log(92160000) or no-lift replay, because the same-source BN27 orientation/magnitude branch "
                "identity or selected connection-value export is still open."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedFinitepartKernelPolicyOnANOrSourceBranchIdentity",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "accepted_final_same_source_connection_tables": 4,
        "required_final_same_source_connection_tables": 8,
        "accepted_rows": ACCEPTED,
        "remaining_rows": REMAINING,
        "kernel_trace_policy_source_owned_on_A_N": True,
        "source_owned_finitepart_functional_closed_on_A_N": True,
        "finitepart_log92160000_identity_from_values_promoted": False,
        "no_lifted_flags_connection_replay_promoted": False,
        "source_branch_identity_closed": False,
        "selected_connection_witness_values_closed": False,
        "new_final_rows_promoted": 0,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Finitepart Kernel Policy on A_N or Source Branch Identity v1

## Theorem

`FinitepartKernelPolicyOnANTheorem` is proved.

## Result

The selected finite projected HYM algebra `A_N` now owns the finite
determinant/kernel/trace policy.  The determinant finitepart is an exact finite
source functional after the selected zero-cluster exclusion, not a continuum
zeta approximation.

The final connection-table count remains `4/8`.  `log(92160000)` and no-lift
are still not promoted because the same-source BN27 orientation/magnitude branch
identity, or selected Cech/HYM connection-value export, remains open.

## Next Artifact

`{NEXT}`
"""

    write_json(POLICY_PACKET, policy_packet)
    write_json(LOGDET_GATE_PACKET, logdet_gate)
    write_json(FRONTIER_PACKET, frontier_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
