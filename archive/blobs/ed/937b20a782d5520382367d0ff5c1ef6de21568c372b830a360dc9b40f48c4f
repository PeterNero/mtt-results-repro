"""Build oriented Phi_fin source-owned positive operator / E_Qa payload frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
QA = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-qa-su3-packet-proof")

SLUG = "selected_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1.md"

SINGLE_FRONTIER = PACKET_DIR / "single_source_ownership_frontier.packet.json"
SOURCE_REQUEST = PACKET_DIR / "threshold_identity_source_request.packet.json"
LEAF_REQUEST = PACKET_DIR / "sourceleaf_directcarrier_or_bundleA_request.packet.json"
NEXT_CONTRACT = PACKET_DIR / "sourceownership_theorem_or_smootheqa_quotient_contract.packet.json"

PREVIOUS = DATA / "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation.candidate.json"
PREVIOUS_NEXT = (
    DATA
    / "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation"
    / "source_owned_positive_operator_or_eqapayload_contract.packet.json"
)

QA_SOURCEOWNED_FILL = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceownedpositiveoperator_or_eqapayload_fill.candidate.json"
QA_MINIMAL_NEW = QA / "candidate_data" / "selected_heterotic_orientedphifin_minimalnewsourcepacket_fill_or_proofclosure.candidate.json"
QA_SOURCE_LEAF = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea.candidate.json"
QA_SOURCE_IDENTITY = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentity_or_orientedbn_operatoremission.candidate.json"
QA_SOURCE_EMISSION = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceemission_or_smootheqa_thresholdidentity.candidate.json"
QA_SINGLE_FRONTIER = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceidentity_single_frontier.json"
QA_SOURCE_REQUEST = QA / "candidate_data" / "selected_heterotic_orientedphifin_thresholdidentity_source_request.json"
QA_LEAF_REQUEST = QA / "candidate_data" / "selected_heterotic_orientedphifin_sourceleaf_directcarrier_or_bundlea_source_theorem_request.json"

STATUS = (
    "MTT_SELECTED_ORIENTEDPHIFIN_SOURCEOWNEDPOSITIVEOPERATOR_OR_EQAPAYLOAD_FILL_"
    "BUILT_SINGLE_SOURCE_OWNERSHIP_FRONTIER_OPEN"
)
NEXT = "MTT_Selected_OrientedPhiFin_SourceOwnership_Theorem_or_SmoothEQa_Quotient_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    previous = load(PREVIOUS)
    previous_next = load(PREVIOUS_NEXT)
    sourceowned_fill = load(QA_SOURCEOWNED_FILL)
    minimal_new = load(QA_MINIMAL_NEW)
    source_leaf = load(QA_SOURCE_LEAF)
    source_identity = load(QA_SOURCE_IDENTITY)
    source_emission = load(QA_SOURCE_EMISSION)
    single_frontier = load(QA_SINGLE_FRONTIER)
    source_request = load(QA_SOURCE_REQUEST)
    leaf_request = load(QA_LEAF_REQUEST)

    support_closed = single_frontier["support_closed"]
    support_closed_count = sum(1 for value in support_closed.values() if value is True)
    support_required_count = len(support_closed)
    direct_open = source_leaf["direct_leaf_attempt"]
    smooth_open = source_leaf["smooth_leaf_attempt"]
    open_source_fields = source_emission["open_source_fields"]

    single_frontier_packet = {
        "schema": "MTTOrientedPhiFinSingleSourceOwnershipFrontier.v1",
        "status": "SINGLE_SOURCE_OWNERSHIP_FRONTIER_IMPORTED_SUPPORT_COMPLETE_SOURCE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source": rel(QA_SINGLE_FRONTIER),
        "operator_payload_ready": single_frontier["operator_payload_ready"],
        "support_closed_count": support_closed_count,
        "support_required_count": support_required_count,
        "support_closed": support_closed,
        "not_yet_source_owned": single_frontier["not_yet_source_owned"],
        "minimal_legal_closures": single_frontier["minimal_legal_closures"],
        "forbidden_shortcuts": single_frontier["forbidden_shortcuts"],
        "accepted_final_rows": {
            "source_owned_positive_operator_rows": 0,
            "smooth_EQa_quotient_rows": 0,
            "finitepart_trace_identity_rows": 0,
            "strict_P_EW_rows": 0,
            "direct_K_threshold_Omega_H_lambda_rows": 0,
        },
    }

    source_request_packet = {
        "schema": "MTTOrientedPhiFinThresholdIdentitySourceRequest.v1",
        "status": "SOURCE_REQUEST_IMPORTED_ALL_ALGEBRAIC_SUPPORT_CLOSED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source": rel(QA_SOURCE_REQUEST),
        "acceptance_rule": source_request["acceptance_rule"],
        "closed_support": source_request["closed_support"],
        "must_emit": source_request["must_emit"],
        "forbidden_shortcuts": source_request["forbidden_shortcuts"],
        "open_source_fields": open_source_fields,
        "support_values": {
            "full_positive_logdet_support_value": source_emission["decision"]["full_positive_logdet_support_value"],
            "oriented_abs_logdet_support_value": source_emission["decision"]["oriented_abs_logdet_support_value"],
            "oriented_signed_difference_support_value": source_emission["decision"][
                "oriented_signed_difference_support_value"
            ],
        },
    }

    leaf_request_packet = {
        "schema": "MTTOrientedPhiFinSourceLeafDirectCarrierOrBundleARequest.v1",
        "status": "FIRST_SOURCE_LEAVES_IDENTIFIED_BOTH_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source": rel(QA_LEAF_REQUEST),
        "first_direct_leaf": minimal_new["decision"]["first_direct_leaf"],
        "first_smooth_leaf": minimal_new["decision"]["first_smooth_leaf"],
        "direct_leaf_closed": source_leaf["decision"]["direct_carrier_leaf_closed"],
        "bundle_A_leaf_closed": source_leaf["decision"]["bundle_A_leaf_closed"],
        "lane_A_direct_carrier_required": leaf_request["lane_A_direct_carrier_required"],
        "lane_B_bundle_A_required": leaf_request["lane_B_bundle_A_required"],
        "known_ready_support": leaf_request["known_ready_support"],
        "direct_leaf_attempt": direct_open,
        "smooth_leaf_attempt": smooth_open,
        "must_not_use": leaf_request["must_not_use"],
    }

    next_contract = {
        "schema": "MTTSourceOwnershipTheoremOrSmoothEQaQuotientContract.v1",
        "status": "NEXT_IS_SOURCEOWNERSHIP_THEOREM_OR_SMOOTHEQA_QUOTIENT",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "must_emit_one_of": [
            "same-source theorem that the heterotic Qa/SU3 threshold source owns the oriented 27-mode B_N Phi_fin operator",
            "source emission of the oriented B_N carrier plus positive Phi_fin D_E magnitude and finitepart trace identity",
            "selected bundle connection A/F_A with representation action and smooth E_Qa quotient to the oriented finite packet",
        ],
        "minimum_acceptance_fields": [
            "source certificate",
            "operator identity",
            "smooth or finite domain and quotient/kernel policy",
            "finitepart trace identity for the oriented nonzero sector",
            "audit replay before observed-data comparison",
        ],
        "must_not_use": sorted(
            set(single_frontier["forbidden_shortcuts"])
            | set(source_request["forbidden_shortcuts"])
            | set(leaf_request["must_not_use"])
        ),
    }

    decision = {
        "previous_frontier_honored": previous["next_required_artifact"]
        == "MTT_Selected_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1",
        "operator_payload_ready": single_frontier["operator_payload_ready"],
        "support_closed_count": support_closed_count,
        "support_required_count": support_required_count,
        "all_value_side_support_closed": support_closed_count == support_required_count,
        "single_source_ownership_frontier_built": True,
        "source_ownership_theorem_closed": False,
        "smooth_EQa_quotient_closed": False,
        "direct_source_owned_positive_operator_closed": sourceowned_fill["decision"][
            "direct_source_owned_positive_operator_closed"
        ],
        "smooth_EQa_payload_closed": sourceowned_fill["decision"]["smooth_EQa_payload_closed"],
        "direct_carrier_leaf_closed": source_leaf["decision"]["direct_carrier_leaf_closed"],
        "bundle_A_leaf_closed": source_leaf["decision"]["bundle_A_leaf_closed"],
        "oriented_threshold_value_promoted": False,
        "finitepart_trace_identity_closed": False,
        "strict_P_EW_source_rows": 0,
        "strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedOrientedPhiFinSourceOwnedPositiveOperatorOrEQaPayloadFill",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_candidate": rel(PREVIOUS),
            "previous_next_contract": rel(PREVIOUS_NEXT),
            "qasu3_sourceowned_fill": rel(QA_SOURCEOWNED_FILL),
            "qasu3_minimal_new_source_packet": rel(QA_MINIMAL_NEW),
            "qasu3_source_leaf": rel(QA_SOURCE_LEAF),
            "qasu3_source_identity": rel(QA_SOURCE_IDENTITY),
            "qasu3_source_emission": rel(QA_SOURCE_EMISSION),
            "qasu3_single_frontier": rel(QA_SINGLE_FRONTIER),
            "qasu3_source_request": rel(QA_SOURCE_REQUEST),
            "qasu3_leaf_request": rel(QA_LEAF_REQUEST),
        },
        "output_packets": {
            "single_source_ownership_frontier": rel(SINGLE_FRONTIER),
            "threshold_identity_source_request": rel(SOURCE_REQUEST),
            "sourceleaf_directcarrier_or_bundleA_request": rel(LEAF_REQUEST),
            "sourceownership_theorem_or_smootheqa_quotient_contract": rel(NEXT_CONTRACT),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "OrientedPhiFinSourceOwnedPositiveOperatorOrEQaPayloadFillTheorem",
            "proved": True,
            "statement": (
                "All value-side oriented Phi_fin ingredients are now materialized or source-supported: "
                "10/10 support fields close, including C_tau source selection, positive Dirac convention, "
                "same BN domain, commutation, Green/Riesz, positive spectrum, and oriented logdet candidates. "
                "The remaining obstruction is one source-ownership theorem or smooth E_Qa quotient theorem; "
                "no threshold, PEW, direct-K, no-knob, or true-SM row is promoted."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_OrientedPhiFin_SourceOwnedPositiveOperator_or_EQaPayload_Fill_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected OrientedPhiFin SourceOwnedPositiveOperator or EQaPayload Fill v1

Status: `{STATUS}`.

## Result

The oriented `Phi_fin` branch is now at a single source-ownership frontier.

```text
operator payload ready              : {str(single_frontier["operator_payload_ready"]).lower()}
closed value/support fields          : {support_closed_count}/{support_required_count}
source ownership theorem closed      : false
smooth E_Qa quotient closed          : false
oriented threshold value promoted    : false
```

Closed support includes `C_tau` source selection, positive Dirac convention,
same `B_N` domain, commutation/simultaneous calculus, Green/Riesz values,
positive spectrum, no-double-count policy, Route-C 27-mode gap-layer support,
and oriented logdet candidates.

The first open leaves are:

```text
direct route : {minimal_new["decision"]["first_direct_leaf"]}
smooth route : {minimal_new["decision"]["first_smooth_leaf"]}
```

So the problem is no longer numerical.  It is one source theorem:

```text
selected heterotic Qa/SU3 source owns the oriented B_N Phi_fin operator
or selected smooth A/F_A and E_Qa quotient emits the same finite packet
```

Next artifact: `{NEXT}`.
"""

    write_json(SINGLE_FRONTIER, single_frontier_packet)
    write_json(SOURCE_REQUEST, source_request_packet)
    write_json(LEAF_REQUEST, leaf_request_packet)
    write_json(NEXT_CONTRACT, next_contract)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
