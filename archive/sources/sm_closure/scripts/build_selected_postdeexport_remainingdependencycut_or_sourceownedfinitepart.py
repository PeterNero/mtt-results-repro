"""Lock the non-looping dependency cut after the 4/8 D_E export promotion."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_postdeexport_remainingdependencycut_or_sourceownedfinitepart"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DEPENDENCY_PACKET = PACKET_DIR / "remaining_four_dependency_cut.packet.json"
LOGDET_PACKET = PACKET_DIR / "logdet_no_lift_strict_gate_after_4of8.packet.json"
NEXT_PACKET = PACKET_DIR / "next_sourceowned_finitepart_or_cechhym_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PostDEExport_RemainingDependencyCut_or_SourceOwnedFinitepart_v1.md"

PREVIOUS = DATA / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables.candidate.json"
PREVIOUS_TABLES = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "eight_table_revalidation_after_de_export.packet.json"
)
PREVIOUS_NEXT = (
    DATA
    / "selected_derieszgreenkerneltraceexport_promotion_or_remainingconnectiontables"
    / "next_four_remaining_connection_tables_contract.packet.json"
)
LOGDET_GATE = (
    DATA
    / "selected_finiterhoetoorientedbnfunctor_or_smootheqarepresentative_or_directhkrow"
    / "bn27_sourceowned_logdet_gate.packet.json"
)
VALIDATOR_GATE = (
    DATA
    / "selected_finiterhoetoorientedbnfunctor_or_smootheqarepresentative_or_directhkrow"
    / "bn27_validator_export_transport_gate.packet.json"
)
SOURCE_ID_GATE = (
    DATA
    / "selected_bn27sectortransferconnectionrepresentative_or_sourceidcertificate"
    / "sourceid_certificate_gate.packet.json"
)
EXACT_VALUES = (
    DATA
    / "selected_torsionalweitzenbockendomorphism_or_ouweightssourcederivation"
    / "exact_oriented_finitepart_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_POSTDEEXPORT_REMAININGDEPENDENCYCUT_OR_SOURCEOWNEDFINITEPART_"
    "FOUR_OF_EIGHT_RETAINED_SOURCEOWNEDFINITEPART_OR_CECHHYM_REQUIRED"
)
NEXT = "MTT_Selected_SourceOwnedFinitepartKernelPolicy_or_CechHYMConnectionValues_v1"
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
        raise FileNotFoundError("missing post-D_E dependency cut inputs: " + ", ".join(missing))


def main() -> int:
    require_sources([PREVIOUS, PREVIOUS_TABLES, PREVIOUS_NEXT, LOGDET_GATE, VALIDATOR_GATE, SOURCE_ID_GATE, EXACT_VALUES])

    previous = load(PREVIOUS)
    tables = load(PREVIOUS_TABLES)
    previous_next = load(PREVIOUS_NEXT)
    logdet = load(LOGDET_GATE)
    validators = load(VALIDATOR_GATE)
    source_id = load(SOURCE_ID_GATE)
    exact_values = load(EXACT_VALUES)

    if tables["accepted_final_same_source_connection_tables"] != 4:
        raise ValueError("previous final connection-table count is not 4/8")
    if tables["accepted_rows"] != ACCEPTED:
        raise ValueError("previous accepted rows are not the canonical 4/8 set")
    if tables["remaining_rows"] != REMAINING:
        raise ValueError("previous remaining rows are not the expected four")
    if previous_next["current_count"] != "4/8":
        raise ValueError("previous next packet does not describe the 4/8 frontier")

    exact = exact_values["finitepart_values"]
    logdet_gate = logdet["sourceowned_logdet"]
    finitepart_gate = logdet["direct_finitepart_arithmetic"]
    validator_source = validators["source_identity_transport"]
    validator_export = validators["validator_export"]

    dependency_cut = {
        "schema": "MTTPostDEExportRemainingFourDependencyCut.v1",
        "status": "FOUR_OF_EIGHT_RETAINED_DEPENDENCIES_SPLIT_TO_CECH_HYM_OR_SOURCEOWNED_FINITEPART",
        "closure_claimed": True,
        "current_count": "4/8",
        "accepted_rows": ACCEPTED,
        "remaining_rows": REMAINING,
        "dependency_classes": {
            "geometric_connection_values": {
                "rows": ["cech_transition_cocycles", "selected_HYM_or_projective_connection_coefficients"],
                "needed_for": [
                    "selected smooth/good-cover representative",
                    "projective/HYM coefficient provenance",
                    "connection-table route to unconditional BN27 replay",
                ],
                "closed_now": False,
            },
            "finitepart_and_replay_provenance": {
                "rows": ["finitepart_log92160000_identity_from_values", "no_lifted_flags_connection_replay"],
                "exact_arithmetic_available": True,
                "conditional_replay_available": True,
                "closed_now": False,
                "missing": [
                    "source-owned finitepart functional",
                    "kernel/trace policy ownership",
                    "source_branch_identity or equivalent connection-value export",
                ],
            },
        },
        "shortest_nonlooping_routes": [
            "source-owned finitepart/kernel policy theorem for the existing exact oriented BN27 values",
            "selected Cech/HYM/projective connection values that export the same BN27 validator fields",
            "direct H K-threshold row, if it bypasses the BN27 connection tables",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    logdet_no_lift = {
        "schema": "MTTLogdetNoLiftStrictGateAfter4of8.v1",
        "status": "EXACT_LOGDET_AND_CONDITIONAL_NOLIFT_PRESENT_STRICT_PROVENANCE_OPEN",
        "closure_claimed": True,
        "exact_values": {
            "oriented_abs_sector_product": exact["oriented_abs_sector_product"],
            "oriented_abs_sector_logdet_exact": exact["oriented_abs_sector_logdet_exact"],
            "oriented_abs_sector_logdet_numeric": exact["oriented_abs_sector_logdet_numeric"],
            "plus_sector_product": exact["plus_sector_product"],
            "minus_sector_product": exact["minus_sector_product"],
            "full_positive_product": exact["full_positive_product"],
            "full_positive_logdet_exact": exact["full_positive_logdet_exact"],
        },
        "sourceowned_logdet_gate": {
            "direct_finitepart_arithmetic_closed": finitepart_gate["direct_finitepart_arithmetic_closed"],
            "source_object_named_S_QaSU3_BN27": finitepart_gate["source_object_named_S_QaSU3_BN27"],
            "kernel_trace_source_owned": finitepart_gate["kernel_trace_source_owned"],
            "source_owned_finitepart_functional_closed": finitepart_gate["source_owned_finitepart_functional_closed"],
            "source_owned_logdet_closed": logdet_gate["source_owned_logdet_closed"],
            "sourceowned_logdet_minimal_packet_built": logdet_gate["sourceowned_logdet_minimal_packet_built"],
        },
        "no_lift_gate": {
            "no_lift_replay_conditional_closed": validator_source["no_lift_replay_conditional_closed"],
            "operator_coemission_conditional_closed": validator_source["operator_coemission_conditional_closed"],
            "source_branch_identity_closed": validator_source["source_branch_identity_closed"],
            "same_source_export_to_BN27_validators": validator_export["same_source_export_to_BN27_validators"],
            "selected_export_owned_count": validator_export["selected_export_owned_count"],
            "open_validator_count": validator_export["open_validator_count"],
        },
        "source_id_gate": {
            "direct_source_theorem_closed": source_id["direct_source_theorem_closed"],
            "connection_tables_closed": source_id["connection_tables_closed"],
            "source_id_certificate_closed": source_id["source_id_certificate_closed"],
            "why_direct_route_is_shortest": source_id["why_direct_route_is_shortest"],
        },
        "strict_rows_promoted_now": [],
        "why_no_promotion_after_4of8": [
            "D_E/Riesz/Green trace export does not close determinant/torsion finitepart policy",
            "exact log(92160000) arithmetic is support until source-owned finitepart/kernel policy is emitted",
            "no-lift replay is conditional until source_branch_identity or same-source connection export closes",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSourceOwnedFinitepartOrCechHYMContract.v1",
        "status": "NEXT_TARGET_SOURCEOWNED_FINITEPART_OR_SELECTED_CECH_HYM_VALUES",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "current_count": "4/8",
        "remaining_rows": REMAINING,
        "option_A_sourceowned_finitepart_kernel_policy": [
            "name and own S_QaSU3^BN27 or equivalent selected threshold source",
            "prove kernel/shared-circle policy and trace/zeta finitepart policy are source-owned",
            "promote log(92160000) and no-lift replay from the emitted source fields",
        ],
        "option_B_selected_cech_hym_connection_values": [
            "emit selected good-cover Cech cocycles",
            "emit selected HYM/projective connection coefficients or endomorphism_E",
            "derive logdet/no-lift replay from those completed connection values",
        ],
        "option_C_direct_HK": "emit direct same-branch K_threshold.Omega_H.lambda row with certificate",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPostDEExportRemainingDependencyCutOrSourceOwnedFinitepart",
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
            "previous_next": rel(PREVIOUS_NEXT),
            "logdet_gate": rel(LOGDET_GATE),
            "validator_gate": rel(VALIDATOR_GATE),
            "source_id_gate": rel(SOURCE_ID_GATE),
            "exact_values": rel(EXACT_VALUES),
        },
        "output_packets": {
            "remaining_four_dependency_cut": rel(DEPENDENCY_PACKET),
            "logdet_no_lift_strict_gate_after_4of8": rel(LOGDET_PACKET),
            "next_sourceowned_finitepart_or_cechhym_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "accepted_final_same_source_connection_tables": 4,
            "required_final_same_source_connection_tables": 8,
            "accepted_rows": ACCEPTED,
            "remaining_rows": REMAINING,
            "exact_log92160000_arithmetic_available": True,
            "conditional_no_lift_replay_available": True,
            "source_owned_logdet_closed": False,
            "kernel_trace_policy_source_owned": False,
            "source_owned_finitepart_functional_closed": False,
            "source_branch_identity_closed": False,
            "same_source_export_to_BN27_validators": False,
            "new_rows_promoted": 0,
            "strict_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "PostDEExportRemainingDependencyCutTheorem",
            "proved": True,
            "statement": (
                "After the D_E/Riesz/Green export promotion, the final connection table frontier is exactly 4/8. "
                "The remaining four rows split into geometric connection values (Cech and HYM/projective coefficients) "
                "and finitepart/replay provenance (log(92160000) and no-lift).  The logdet number and conditional "
                "no-lift replay are already present, but strict promotion is blocked only by source-owned finitepart/"
                "kernel policy, source_branch_identity, or equivalent selected connection-value export."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedPostDEExportRemainingDependencyCutOrSourceOwnedFinitepart",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "accepted_final_same_source_connection_tables": 4,
        "required_final_same_source_connection_tables": 8,
        "accepted_rows": ACCEPTED,
        "remaining_rows": REMAINING,
        "exact_log92160000_arithmetic_available": True,
        "conditional_no_lift_replay_available": True,
        "source_owned_logdet_closed": False,
        "kernel_trace_policy_source_owned": False,
        "source_owned_finitepart_functional_closed": False,
        "source_branch_identity_closed": False,
        "same_source_export_to_BN27_validators": False,
        "new_rows_promoted": 0,
        "strict_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Post-D_E Export Remaining Dependency Cut or Source-Owned Finitepart v1

## Theorem

`PostDEExportRemainingDependencyCutTheorem` is proved.

## Result

The final connection-table frontier remains `4/8`, but the remaining blockers
are now classified without ambiguity:

- Geometric values: `cech_transition_cocycles`, `selected_HYM_or_projective_connection_coefficients`.
- Provenance values: `finitepart_log92160000_identity_from_values`, `no_lifted_flags_connection_replay`.

The exact value `log(92160000)` and conditional no-lift replay are available,
but strict promotion still needs source-owned finitepart/kernel policy,
`source_branch_identity`, or equivalent selected connection-value export.

## Next Artifact

`{NEXT}`
"""

    write_json(DEPENDENCY_PACKET, dependency_cut)
    write_json(LOGDET_PACKET, logdet_no_lift)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
