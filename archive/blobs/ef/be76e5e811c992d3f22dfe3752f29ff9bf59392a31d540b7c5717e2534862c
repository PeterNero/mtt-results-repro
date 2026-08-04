"""Build oriented Phi_fin direct finite-response fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

INPUTS = {
    "direct_contract": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_source_contract.json",
    "contract_gate": DATA / "selected_heterotic_orientedphifin_directfiniteresponse_or_projectiverhoe_sourceamendment.candidate.json",
    "oriented_table": DATA / "selected_heterotic_orientedphifin_simultaneous_ctau_phifin_table.json",
    "direct_operator_attempt": DATA / "selected_heterotic_phifin_direct_operator_emission_attempt.candidate.json",
    "routec_prefix": DATA / "selected_electroweak_qastack_threshold_operator_from_nonidentity_rhoe_quotientbn.candidate.json",
    "internal_packet_emission": DATA / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.candidate.json",
    "internal_finitepart": DATA / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.candidate.json",
}

OUTPUT_DATA = DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt.candidate.json"
OUTPUT_PACKET = DATA / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_packet.json"
OUTPUT_CERT = CERTS / "selected_heterotic_orientedphifin_directfiniteresponse_fillattempt_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Heterotic_OrientedPhiFin_DirectFiniteResponse_FillAttempt_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_DIRECTFINITE_RESPONSE_FILLATTEMPT_SUPPORT_ONLY_SOURCE_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_SourceIdentity_or_OrientedBN_OperatorEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def oriented_response_from_table(table: dict[str, Any]) -> dict[str, Any]:
    nonzero = [entry for entry in table["entries"] if entry["C_tau"] != 0 and entry["is_positive_magnitude"]]
    plus = [entry for entry in nonzero if entry["C_tau"] == 1]
    minus = [entry for entry in nonzero if entry["C_tau"] == -1]
    positive = [float(entry["PhiFin_DE_eigenvalue"]) for entry in nonzero]
    green = [1.0 / value for value in positive]
    squared_green = [1.0 / (value * value) for value in positive]

    return {
        "schema": "SelectedHeterotic.OrientedPhiFin.DirectFiniteResponse.FillAttemptPacket.v1",
        "domain": {
            "basis_id": table["basis_id"],
            "basis_dimension": table["basis_dimension"],
            "oriented_nonzero_count": len(nonzero),
            "oriented_plus_count": len(plus),
            "oriented_minus_count": len(minus),
            "kernel_count_total": table["counts"]["PhiFin_kernel_count"],
            "ctau_kernel_count": table["counts"]["C_tau_spectrum"]["0"],
        },
        "operator_values_materialized": {
            "D_E_diagonal_on_oriented_nonzero_BN": [
                {
                    "row": entry["row"],
                    "basis_label": entry["basis_label"],
                    "C_tau": entry["C_tau"],
                    "D_E_eigenvalue": entry["PhiFin_DE_eigenvalue"],
                    "oriented_eigenvalue": entry["oriented_eigenvalue"],
                    "Riesz_Green_diagonal": 1.0 / float(entry["PhiFin_DE_eigenvalue"]),
                }
                for entry in nonzero
            ],
            "positive_spectrum": positive,
            "green_trace": sum(green),
            "green_square_trace": sum(squared_green),
            "minimum_positive_eigenvalue": min(positive),
            "maximum_positive_eigenvalue": max(positive),
        },
        "finitepart_candidates": {
            "oriented_plus_sector_logdet": table["logdet_values"]["oriented_plus_sector_logdet"],
            "oriented_minus_sector_logdet": table["logdet_values"]["oriented_minus_sector_logdet"],
            "oriented_abs_sector_logdet_sum": table["logdet_values"]["oriented_abs_sector_logdet_sum"],
            "oriented_signed_sector_logdet_difference": table["logdet_values"]["oriented_signed_sector_logdet_difference"],
            "promoted_to_threshold_finitepart": False,
            "why_not": "The diagonal table supplies a candidate determinant, but not a same-branch finitepart trace identity.",
        },
        "source_tests": {
            "orientation_operator_Ctau_binding": table["commutation"]["simultaneous_functional_calculus_closed"],
            "same_branch_heterotic_source_certificate": False,
            "selected_domain_or_quotient_map_to_oriented_BN": False,
            "finitepart_trace_identity_for_oriented_logdet": False,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> dict[str, Any]:
    contract = load(INPUTS["direct_contract"])
    contract_gate = load(INPUTS["contract_gate"])
    oriented_table = load(INPUTS["oriented_table"])
    direct_attempt = load(INPUTS["direct_operator_attempt"])
    routec_prefix = load(INPUTS["routec_prefix"])
    internal_emission = load(INPUTS["internal_packet_emission"])
    internal_finitepart = load(INPUTS["internal_finitepart"])

    packet = oriented_response_from_table(oriented_table)

    leaf_status = {
        "same_branch_source_certificate": {
            "closed": False,
            "support": [
                direct_attempt["branch_compatibility"]["heterotic_selected_source"],
                "oriented table is built on the 27-mode B_N basis",
            ],
            "blocker": "No theorem yet identifies the oriented 27-mode B_N response as emitted by the selected heterotic Qa/SU3 source.",
        },
        "selected_domain_or_quotient_map_to_oriented_BN": {
            "closed": False,
            "support": "The B_N labels and orientation table are explicit, but the selected heterotic quotient/functor map is not emitted.",
            "blocker": "Need a same-branch quotient map from End(E), rho_E/projective transitions, or source-certified direct finite response to oriented B_N.",
        },
        "D_E_or_EQa_matrix_on_oriented_BN": {
            "closed": False,
            "support": "A diagonal D_E table on oriented nonzero B_N has been materialized in the packet.",
            "blocker": "The table is not yet source-promoted as the heterotic Qa/SU3 threshold D_E or E_Qa matrix.",
        },
        "orientation_operator_Ctau_binding": {
            "closed": True,
            "support": "C_tau and Phi_fin are simultaneous diagonal operators and commute on the stored table.",
        },
        "Riesz_or_Green_operator": {
            "closed": False,
            "support": "A diagonal Green/Riesz candidate is computable on the nonzero oriented sector.",
            "blocker": "Riesz/Green is only legal after the D_E/E_Qa matrix is source-certified on this branch.",
        },
        "positive_spectrum_or_heat_zeta_torsion": {
            "closed": False,
            "support": "The nonzero oriented sector has positive magnitudes with minimum eigenvalue 1.",
            "blocker": "Positive spectrum support is present, but the heat/zeta/torsion finitepart prescription is not source-emitted.",
        },
        "finitepart_trace_identity_for_oriented_logdet": {
            "closed": False,
            "support": "The oriented sector logdet candidates are recomputed from the same table.",
            "blocker": "No trace theorem identifies those logdets with the selected threshold finite part.",
        },
        "no_double_count_replay": {
            "closed": True,
            "support": "The prior finite-quotient policy keeps GR/smooth surface response outside this internal oriented packet.",
        },
    }

    closed_required = [key for key, value in leaf_status.items() if value["closed"] is True]
    open_required = [key for key, value in leaf_status.items() if value["closed"] is False]
    packet["leaf_status"] = leaf_status
    packet["closed_required_leaves"] = closed_required
    packet["open_required_leaves"] = open_required
    OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    decision = {
        "fill_attempt_executed": True,
        "oriented_diagonal_response_materialized": True,
        "orientation_binding_support_closed": leaf_status["orientation_operator_Ctau_binding"]["closed"],
        "no_double_count_replay_closed": leaf_status["no_double_count_replay"]["closed"],
        "source_identity_closed": False,
        "direct_same_source_finite_response_closed": False,
        "oriented_logdet_promoted": False,
        "new_threshold_value_closed": False,
        "open_required_leaves": open_required,
        "closed_required_leaves": closed_required,
        "next_required_artifact": NEXT,
        "packet_path": rel(OUTPUT_PACKET),
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "SelectedHeteroticOrientedPhiFinDirectFiniteResponseFillAttempt",
        "status": STATUS,
        "inputs": {key: rel(path) for key, path in INPUTS.items()},
        "parent_statuses": {
            "contract_gate": contract_gate["status"],
            "direct_operator_attempt": direct_attempt["status"],
            "routec_prefix": routec_prefix["status"],
            "internal_packet_emission": internal_emission["status"],
            "internal_finitepart": internal_finitepart["status"],
        },
        "contract_status": contract["status"],
        "packet_path": rel(OUTPUT_PACKET),
        "decision": decision,
        "theorem": {
            "name": "OrientedPhiFinDirectFiniteResponseFillAttemptSupportTheorem",
            "proved": True,
            "statement": (
                "The oriented 27-mode B_N table is sufficient to materialize a diagonal "
                "D_E candidate, its nonzero-sector Riesz/Green inverse, and oriented "
                "logdet candidates. This closes only support leaves already owned by "
                "the oriented table: C_tau binding and no-double-count policy. It does "
                "not prove the selected heterotic Qa/SU3 source identity, quotient map "
                "to oriented B_N, source-certified D_E/E_Qa, or finitepart trace identity; "
                "therefore no threshold value is promoted."
            ),
        },
        "guardrails": {
            "does_not_promote_oriented_logdet": True,
            "does_not_promote_routec_prefix": True,
            "does_not_promote_internal_packet_to_oriented_response": True,
            "does_not_claim_source_identity": True,
            "does_not_claim_direct_response_closure": True,
            "does_not_use_observed_data": True,
            "target_fitting_used": False,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_DATA.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": candidate["candidate"],
        "status": STATUS,
        "candidate_path": rel(OUTPUT_DATA),
        "packet_path": rel(OUTPUT_PACKET),
        "note_path": rel(OUTPUT_NOTE),
        "oriented_diagonal_response_materialized": True,
        "direct_same_source_finite_response_closed": False,
        "oriented_logdet_promoted": False,
        "open_required_leaves": open_required,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# Selected Heterotic OrientedPhiFin DirectFiniteResponse FillAttempt v1

## Result

```text
status = {STATUS}
oriented_diagonal_response_materialized = true
direct_same_source_finite_response_closed = false
oriented_logdet_promoted = false
next_required_artifact = {NEXT}
```

## Theorem

{candidate["theorem"]["statement"]}

## Packet

```text
{rel(OUTPUT_PACKET)}
```

## Open Required Leaves

```text
{chr(10).join(open_required)}
```
"""
    OUTPUT_NOTE.write_text(note, encoding="utf-8")
    return candidate


if __name__ == "__main__":
    result = main()
    print(f"wrote {rel(OUTPUT_DATA)}")
    print(f"wrote {rel(OUTPUT_PACKET)}")
    print(f"wrote {rel(OUTPUT_CERT)}")
    print(f"wrote {rel(OUTPUT_NOTE)}")
    print(result["status"])
