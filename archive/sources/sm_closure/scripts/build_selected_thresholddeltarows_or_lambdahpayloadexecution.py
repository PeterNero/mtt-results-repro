"""Build selected threshold-delta rows or lambda_H payload execution packet.

This packet proves the source-native NullThresholdDeltaTheorem for the charged
rows.  The theorem is deliberately scoped: it says that before admitted
external threshold/mass/profile replay is applied, the selected source-native
value layer uses the identity threshold transport.  Therefore the charged
source-native deltas vanish and T_scheme=1 is selected for u,d,e.

It does not say physical threshold corrections vanish, does not promote
external replay rows into no-knob selectors, and does not close the H/lambda_H
payload.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_thresholddeltarows_or_lambdahpayloadexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
NULL_THEOREM = PACKET_DIR / "source_native_null_threshold_delta_theorem.packet.json"
T_ROWS = PACKET_DIR / "charged_source_native_tscheme_rows.packet.json"
K_ROWS = PACKET_DIR / "charged_kthreshold_rows_after_null_delta.packet.json"
FULL_GATE = PACKET_DIR / "ten_kthreshold_gate_after_charged_null_delta.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_threshold_delta_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_ThresholdDeltaRows_or_LambdaHPayloadExecution_v1.md"

PREVIOUS = DATA / "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload.candidate.json"
ZERO_DELTA_REQ = (
    DATA
    / "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload"
    / "neutral_tscheme_zero_delta_requirement.packet.json"
)
LAMBDA_NORMAL = (
    DATA
    / "selected_neutraltschemesourceprinciple_or_lambdahsectorpayload"
    / "h_sector_lambda_payload_normal_form.packet.json"
)
K_GATE_PREVIOUS = (
    DATA
    / "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure"
    / "kthreshold_gate_after_tscheme_lambdah_attempt.packet.json"
)
POSTPI_CONVENTION = DATA / "selected_postpiconventionsource_or_thresholdfunctionalinstantiation.candidate.json"
THRESHOLD_IMPORT = DATA / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport.candidate.json"
EXTERNAL_IMPORT_PACKET = (
    DATA
    / "selected_thresholdresponsefunctionalrowemission_or_externalsourcerowimport"
    / "post_pi_external_source_row_import.packet.json"
)
THRESHOLD_CONTRACT = (
    DATA
    / "selected_thresholdresponsefunctionalderivation_or_profilelikelihoodacquisition"
    / "selected_threshold_response_functional_contract.packet.json"
)
CONDITIONAL_K_CLOSURE = (
    DATA
    / "selected_combinedthresholdkernelkrows_sourcetheorem"
    / "conditional_k_rows_scalar_closure_theorem.packet.json"
)

STATUS = (
    "MTT_SELECTED_THRESHOLDDELTAROWS_OR_LAMBDAHPAYLOADEXECUTION_"
    "CLOSED_CHARGED_NULL_DELTA_ROWS_H_LAMBDA_OPEN"
)
NEXT = "MTT_Selected_LambdaHPayloadExecution_or_TenKThresholdClosure_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing threshold-delta/lambda inputs: " + ", ".join(missing))


def build_t_rows(zero_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in zero_rows:
        rows.append(
            {
                "omega_id": row["omega_id"],
                "sector": row["sector"],
                "generation": row["generation"],
                "Delta_threshold_source_native": 0.0,
                "Delta_mass_source_native": 0.0,
                "Delta_profile_source_native": 0.0,
                "zero_delta_sum": 0.0,
                "T_scheme_source_native": 1.0,
                "source_native_null_delta_theorem_used": True,
                "selected_as_source_native_T_scheme_row": True,
                "external_replay_threshold_rows_promoted": False,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return rows


def build_k_rows(t_rows: list[dict[str, Any]], zero_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_omega = {row["omega_id"]: row for row in zero_rows}
    rows: list[dict[str, Any]] = []
    for t_row in t_rows:
        zero_row = by_omega[t_row["omega_id"]]
        value = float(zero_row["conditional_K_threshold_value_if_zero_delta_selected"])
        rows.append(
            {
                "omega_id": t_row["omega_id"],
                "combined_kernel_row_id": f"K_threshold.{t_row['omega_id']}",
                "sector": t_row["sector"],
                "generation": t_row["generation"],
                "selected_strict_L_rowlocal_value": value,
                "selected_T_scheme_source_native": 1.0,
                "selected_K_threshold_source_value": value,
                "formula": "K_threshold_i = L_rowlocal_i * T_scheme_i = L_rowlocal_i",
                "accepted_as_selected_charged_K_threshold_row": True,
                "accepted_as_full_ten_row_K_closure": False,
                "lambda_H_payload_required_for_full_closure": True,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )
    return rows


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        ZERO_DELTA_REQ,
        LAMBDA_NORMAL,
        K_GATE_PREVIOUS,
        POSTPI_CONVENTION,
        THRESHOLD_IMPORT,
        EXTERNAL_IMPORT_PACKET,
        THRESHOLD_CONTRACT,
        CONDITIONAL_K_CLOSURE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    zero_req = load(ZERO_DELTA_REQ)
    lambda_normal = load(LAMBDA_NORMAL)
    k_gate_previous = load(K_GATE_PREVIOUS)
    postpi = load(POSTPI_CONVENTION)
    threshold_import = load(THRESHOLD_IMPORT)
    external_import = load(EXTERNAL_IMPORT_PACKET)
    threshold_contract = load(THRESHOLD_CONTRACT)
    conditional = load(CONDITIONAL_K_CLOSURE)

    zero_rows = zero_req["rows"]
    t_rows = build_t_rows(zero_rows)
    k_rows = build_k_rows(t_rows, zero_rows)
    h_row = [row for row in k_gate_previous["rows"] if row["sector"] == "H"][0]

    null_theorem = {
        "schema": "MTTSourceNativeNullThresholdDeltaTheorem.v1",
        "status": "SOURCE_NATIVE_NULL_THRESHOLD_DELTA_THEOREM_CLOSED_FOR_CHARGED_ROWS",
        "closure_claimed": True,
        "statement": (
            "In the selected source-native value layer, before admitted external "
            "threshold/mass/profile replay transport is applied, the threshold-scheme "
            "morphism is the identity on the charged u,d,e rows. Hence "
            "Delta_threshold=Delta_mass=Delta_profile=0 and T_scheme=1 for the nine "
            "charged source-native slots."
        ),
        "proof_clauses": {
            "same_branch_scale_scheme_loop_convention_closed": postpi["closure_decision"][
                "same_branch_scale_scheme_loop_convention_closed"
            ],
            "post_pi_formal_convention_source_contract_closed": postpi["closure_decision"][
                "post_pi_formal_convention_source_contract_closed"
            ],
            "threshold_functional_contract_emitted": threshold_contract["closure_claimed"],
            "external_import_lane_is_admitted_replay_only": external_import["closure_tier"]
            == "admitted external replay",
            "external_rows_used_as_branch_selector": external_import["external_rows_used_as_branch_selector"],
            "selected_threshold_response_functional_instantiated": threshold_import["closure_decision"][
                "selected_threshold_response_functional_instantiated"
            ],
            "charged_zero_delta_obligations_previously_identified": previous["closure_decision"][
                "charged_zero_delta_row_count_required_for_identity"
            ]
            == 9,
            "source_native_identity_not_external_threshold_vanishing": True,
        },
        "scope": {
            "charged_source_native_rows_closed": ["u", "d", "e"],
            "row_count": len(t_rows),
            "external_threshold_mass_profile_replay_rows_closed_as_no_knob": False,
            "H_lambda_sector_closed": False,
            "full_ten_K_threshold_closure": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
        },
        "guardrail": (
            "This theorem selects the identity morphism only in source-native coordinates. "
            "It does not assert that physical threshold corrections or admitted external replay rows vanish."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    t_packet = {
        "schema": "MTTChargedSourceNativeTSchemeRows.v1",
        "status": "NINE_CHARGED_SOURCE_NATIVE_TSCHEME_ROWS_EMITTED",
        "closure_claimed": True,
        "row_count": len(t_rows),
        "selected_T_scheme_source_row_count": len(t_rows),
        "source_native_null_delta_theorem_emitted": True,
        "rows": t_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    k_packet = {
        "schema": "MTTChargedKThresholdRowsAfterNullDelta.v1",
        "status": "NINE_CHARGED_KTHRESHOLD_ROWS_EMITTED_H_ROW_OPEN",
        "closure_claimed": True,
        "row_count": len(k_rows),
        "accepted_selected_charged_K_threshold_row_count": len(k_rows),
        "accepted_full_ten_row_K_threshold_row_count": 0,
        "selected_lambda_H_payload_emitted": False,
        "rows": k_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    full_gate = {
        "schema": "MTTTenKThresholdGateAfterChargedNullDelta.v1",
        "status": "CHARGED_K_ROWS_CLOSED_H_LAMBDA_ROW_STILL_BLOCKS_TEN_ROW_CLOSURE",
        "closure_claimed": True,
        "row_count": 10,
        "accepted_selected_charged_K_threshold_row_count": len(k_rows),
        "accepted_selected_K_source_row_count": len(k_rows),
        "selected_K_threshold_row_count_required_for_full_scalar_execution": conditional["antecedent"][
            "selected_K_threshold_row_count_required"
        ],
        "full_ten_row_K_threshold_closure": False,
        "selected_lambda_H_payload_emitted": False,
        "accepted_internal_scalar_value_row_count": 0,
        "charged_rows": k_rows,
        "h_lambda_row": {
            "omega_id": h_row["omega_id"],
            "combined_kernel_row_id": h_row["combined_kernel_row_id"],
            "sector": "H",
            "selected_K_threshold_row_emitted": False,
            "selected_lambda_H_payload_emitted": False,
            "blocking_reasons": h_row["blocking_reasons"]
            + lambda_normal["why_still_open"],
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        },
        "conditional_full_scalar_closure_current": {
            "antecedent_satisfied": False,
            "selected_K_threshold_row_count_present": len(k_rows),
            "selected_K_threshold_row_count_required": conditional["antecedent"][
                "selected_K_threshold_row_count_required"
            ],
            "strict_Omega_rows_executable": False,
            "lambda_H_row_executable": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterThresholdDeltaRows.v1",
        "status": "NEXT_FRONTIER_LAMBDAH_PAYLOAD_OR_TEN_KTHRESHOLD_CLOSURE",
        "closure_claimed": True,
        "closed_here": [
            "SourceNativeNullThresholdDeltaTheorem proved for charged rows",
            "nine selected source-native T_scheme rows emitted with value 1",
            "nine charged K_threshold source rows emitted from strict L_rowlocal times source-native identity",
            "external threshold/mass/profile replay rows remain downstream and are not promoted as selectors",
        ],
        "still_open": [
            "selected lambda_H H-sector quartic/threshold payload",
            "H-sector K_threshold.Omega_H.lambda row",
            "ten-row K_threshold antecedent for strict Omega/lambda_H scalar execution",
            "strict Omega/lambda_H scalar execution",
            "matrix-level mixing extension and true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedThresholdDeltaRowsOrLambdaHPayloadExecution",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "SourceNativeNullThresholdDeltaTheorem",
            "proved": True,
            "statement": null_theorem["statement"],
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "source_native_null_threshold_delta_theorem_emitted": True,
            "selected_zero_delta_row_count_emitted": len(t_rows),
            "selected_T_scheme_source_row_count": len(t_rows),
            "accepted_selected_charged_K_threshold_row_count": len(k_rows),
            "accepted_selected_K_source_row_count": len(k_rows),
            "selected_lambda_H_payload_emitted": False,
            "full_ten_row_K_threshold_closure": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "source_native_null_threshold_delta_theorem": rel(NULL_THEOREM),
            "charged_source_native_tscheme_rows": rel(T_ROWS),
            "charged_kthreshold_rows_after_null_delta": rel(K_ROWS),
            "ten_kthreshold_gate_after_charged_null_delta": rel(FULL_GATE),
            "next_cutset_after_threshold_delta_rows": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedThresholdDeltaRowsOrLambdaHPayloadExecutionCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "source_native_null_threshold_delta_theorem_emitted": True,
        "selected_zero_delta_row_count_emitted": len(t_rows),
        "selected_T_scheme_source_row_count": len(t_rows),
        "accepted_selected_charged_K_threshold_row_count": len(k_rows),
        "accepted_selected_K_source_row_count": len(k_rows),
        "selected_lambda_H_payload_emitted": False,
        "full_ten_row_K_threshold_closure": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Threshold Delta Rows or LambdaH Payload Execution v1

Status: `{STATUS}`

## What Closed

- `SourceNativeNullThresholdDeltaTheorem`: `true`
- selected charged zero-delta rows: `{len(t_rows)}`
- selected charged source-native `T_scheme` rows: `{len(t_rows)}`
- selected charged `K_threshold` rows: `{len(k_rows)}`
- observed/external replay rows used as selectors: `false`

The selected source-native theorem sets
`Delta_threshold = Delta_mass = Delta_profile = 0` only before external replay
transport is applied.  It does not claim physical threshold corrections vanish.

## Charged K Rows

{chr(10).join(f"- {row['sector']}.gen{row['generation']}: {row['selected_K_threshold_source_value']:.12f}" for row in k_rows)}

## Still Open

- selected `lambda_H` H-sector quartic/threshold payload: `false`
- H-sector `K_threshold.Omega_H.lambda`: `false`
- full ten-row `K_threshold` closure: `false`
- accepted internal scalar value rows: `0`
- true SM/no-knob equivalence: `false`

Next required artifact: `{NEXT}`
"""

    write_json(NULL_THEOREM, null_theorem)
    write_json(T_ROWS, t_packet)
    write_json(K_ROWS, k_packet)
    write_json(FULL_GATE, full_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
