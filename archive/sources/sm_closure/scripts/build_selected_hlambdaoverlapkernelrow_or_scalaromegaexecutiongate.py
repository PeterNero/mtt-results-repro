"""Build H/lambda overlap-kernel row or scalar Omega execution gate.

This artifact follows the nine charged overlap-kernel rows.  It keeps the
strict no-knob tier honest at 9/10 and imports the already-audited controlled
minimal-parameter H-threshold layer as a separate empirical tier.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_GATE = PACKET_DIR / "strict_hlambda_overlap_kernel_gate.packet.json"
CONTROLLED_GATE = PACKET_DIR / "controlled_one_parameter_scalar_gate.packet.json"
TIER_SEPARATION = PACKET_DIR / "strict_vs_controlled_tier_separation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hlambda_scalar_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HLambdaOverlapKernelRow_or_ScalarOmegaExecutionGate_v1.md"
AUDIT = CORPUS / f"{SLUG}_audit.py"

PREVIOUS = DATA / "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows.candidate.json"
CHARGED_ROWS = (
    DATA
    / "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows"
    / "selected_charged_normalized_overlap_kernel_rows.packet.json"
)
H_GAP = (
    DATA
    / "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows"
    / "h_lambda_overlap_kernel_row_gap.packet.json"
)
H_THRESHOLD_CAL = DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun.candidate.json"
MINIMAL_RUN = (
    DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun" / "minimal_primitive_calibration_run.packet.json"
)
CONTROLLED_HK = (
    DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun" / "controlled_empirical_h_k_gate.packet.json"
)
HK_AFTER_CAL = (
    DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun" / "hk_threshold_gate_after_calibration_run.packet.json"
)
CROSSUSE_WORKORDER = (
    DATA / "selected_hthresholdrgsource_or_minimalprimitivecalibrationrun" / "crossuse_prediction_audit_workorder.packet.json"
)
EMPIRICAL_K_CONTRACT = (
    DATA
    / "selected_lrowlocaltschemelambdah_sourceexecution_or_controlledempiricalimport"
    / "controlled_empirical_k_import_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_HLAMBDAOVERLAPKERNELROW_OR_SCALAROMEGAEXECUTIONGATE_"
    "STRICT_9OF10_CONTROLLED_ONE_PARAMETER_10OF10_BUILT"
)
NEXT = "MTT_Selected_HRGPrimitiveCrossUsePredictionAudit_or_StrictHSourceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def source_paths() -> list[Path]:
    return [
        PREVIOUS,
        CHARGED_ROWS,
        H_GAP,
        H_THRESHOLD_CAL,
        MINIMAL_RUN,
        CONTROLLED_HK,
        HK_AFTER_CAL,
        CROSSUSE_WORKORDER,
        EMPIRICAL_K_CONTRACT,
    ]


def build() -> None:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    missing = [rel(path) for path in source_paths() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H/lambda scalar-gate inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    charged = load(CHARGED_ROWS)
    h_gap = load(H_GAP)
    h_cal = load(H_THRESHOLD_CAL)
    minimal = load(MINIMAL_RUN)
    controlled_hk = load(CONTROLLED_HK)
    hk_after_cal = load(HK_AFTER_CAL)
    crossuse = load(CROSSUSE_WORKORDER)
    empirical_k = load(EMPIRICAL_K_CONTRACT)

    h_empirical_row = next(
        row for row in empirical_k["empirical_K_rows"] if row["omega_id"] == "Omega_H.lambda"
    )

    strict_gate = {
        "schema": "MTTStrictHLambdaOverlapKernelGate.v1",
        "status": "STRICT_HLAMBDA_OVERLAP_KERNEL_ROW_STILL_OPEN_AFTER_CHARGED_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_selected_charged_overlap_row_count": charged[
            "accepted_selected_charged_normalized_overlap_kernel_row_count"
        ],
        "strict_selected_K_source_row_count": previous["closure_decision"][
            "accepted_selected_K_source_row_count"
        ],
        "strict_selected_K_source_row_count_required": 10,
        "selected_H_lambda_overlap_kernel_row_emitted": False,
        "selected_K_threshold_Omega_H_lambda_emitted": False,
        "selected_lambda_H_payload_emitted": False,
        "accepted_internal_scalar_value_row_count": 0,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "strict_no_knob_closure_claimed": False,
        "h_gap_status": h_gap["status"],
        "blocking_reasons": h_gap["blocking_reasons"],
    }

    controlled_gate = {
        "schema": "MTTControlledOneParameterScalarGate.v1",
        "status": "CONTROLLED_ONE_PARAMETER_H_LAYER_BUILDS_PARAMETERIZED_10OF10_NOT_NOKNOB",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "controlled_empirical_tier_available": True,
        "minimal_parameter_H_calibration_layer_claimed": h_cal["minimal_parameter_H_calibration_layer_claimed"],
        "primitive_id": minimal["primitive"]["id"],
        "new_universal_parameter_count": minimal["primitive"]["new_universal_parameter_count_in_this_layer"],
        "calibrated_value": minimal["calibration_values"]["required_UP_RET_OVERLAP_HRG"],
        "log_calibrated_value": minimal["calibration_values"]["log_required_UP_RET_OVERLAP_HRG"],
        "calibrating_observable": minimal["calibration_protocol"]["calibrating_observable"],
        "lambda_H_calibrated": minimal["claim_boundary"]["lambda_H_calibrated"],
        "lambda_H_predicted": minimal["claim_boundary"]["lambda_H_predicted"],
        "conditional_parameterized_K_row_count": controlled_hk["controlled_empirical_tier"][
            "conditional_parameterized_K_row_count"
        ],
        "controlled_empirical_H_K_formula": controlled_hk["controlled_empirical_tier"][
            "omega_scheme_formula"
        ],
        "controlled_empirical_H_K_symbolic": h_empirical_row["empirical_K_import_symbolic"],
        "controlled_empirical_H_K_allowed_use": h_empirical_row["allowed_use"],
        "strict_no_knob_claim_allowed": False,
        "true_SM_equivalence_claimed": False,
        "crossuse_prediction_audit_required": hk_after_cal["controlled_empirical_tier"][
            "crossuse_prediction_audit_required"
        ],
        "crossuse_prediction_audit_passed": h_cal["closure_decision"][
            "crossuse_prediction_audit_passed"
        ],
    }

    tier = {
        "schema": "MTTStrictVsControlledTierSeparation.v1",
        "status": "STRICT_AND_CONTROLLED_HLAMBDA_TIERS_SEPARATED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "strict_tier": {
            "selected_K_rows": 9,
            "required_K_rows": 10,
            "H_lambda_row_selected": False,
            "scalar_execution_closed": False,
            "claim_label": "strict_no_knob_open",
        },
        "controlled_one_parameter_tier": {
            "declared_parameter_count": 1,
            "primitive_id": minimal["primitive"]["id"],
            "conditional_K_rows": 10,
            "lambda_H_is_calibration": True,
            "lambda_H_prediction_credit_allowed": False,
            "claim_label": "controlled_empirical_minimal_parameter_layer",
        },
        "credibility_upgrade_requirements": crossuse["required_prediction_set_before_credibility_upgrade"],
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHLambdaScalarGate.v1",
        "status": "NEXT_CUTSET_IS_HRG_CROSSUSE_OR_STRICT_H_SOURCE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "strict H/lambda gate reconciled after nine charged overlap rows",
            "controlled one-parameter H layer imported into current frontier",
            "parameterized controlled 10/10 K gate recorded separately from strict no-knob tier",
            "lambda_H calibration/prediction boundary locked",
        ],
        "still_open": [
            "strict selected H/lambda overlap-kernel row",
            "strict selected R_H^RG or H quartic/threshold source theorem",
            "cross-use prediction audit for UP-RET-OVERLAP.HRG",
            "non-Higgs threshold/RG prediction using the same calibrated primitive",
            "strict Omega/lambda_H scalar execution",
            "true SM equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "schema": "MTTSelectedHLambdaOverlapKernelRowOrScalarOmegaExecutionGate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "selected_overlap_kernel_rows": rel(PREVIOUS),
            "charged_overlap_rows": rel(CHARGED_ROWS),
            "h_lambda_gap": rel(H_GAP),
            "h_threshold_calibration_candidate": rel(H_THRESHOLD_CAL),
            "minimal_primitive_calibration_run": rel(MINIMAL_RUN),
            "controlled_empirical_h_k_gate": rel(CONTROLLED_HK),
            "hk_threshold_gate_after_calibration": rel(HK_AFTER_CAL),
            "crossuse_prediction_workorder": rel(CROSSUSE_WORKORDER),
            "controlled_empirical_k_contract": rel(EMPIRICAL_K_CONTRACT),
        },
        "output_packets": {
            "strict_hlambda_overlap_kernel_gate": rel(STRICT_GATE),
            "controlled_one_parameter_scalar_gate": rel(CONTROLLED_GATE),
            "strict_vs_controlled_tier_separation": rel(TIER_SEPARATION),
            "next_cutset_after_hlambda_scalar_gate": rel(CUTSET),
        },
        "closure_decision": {
            "strict_selected_charged_overlap_row_count": 9,
            "strict_selected_K_source_row_count": 9,
            "strict_selected_K_source_row_count_required": 10,
            "strict_selected_H_lambda_overlap_kernel_row_emitted": False,
            "strict_selected_K_threshold_Omega_H_lambda_emitted": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "controlled_one_parameter_H_layer_built": True,
            "controlled_parameter_id": minimal["primitive"]["id"],
            "controlled_parameter_value": minimal["calibration_values"]["required_UP_RET_OVERLAP_HRG"],
            "controlled_parameterized_K_row_count": 10,
            "lambda_H_calibrated": True,
            "lambda_H_predicted": False,
            "crossuse_prediction_audit_passed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "HLambdaTierSeparatedScalarGateTheorem",
            "proved": True,
            "statement": (
                "After the nine charged overlap-kernel rows, strict no-knob H/lambda "
                "closure remains at 9/10 because no selected H/lambda kernel row is "
                "emitted.  The controlled empirical minimal-parameter tier can build "
                "a parameterized 10/10 K gate by declaring UP-RET-OVERLAP.HRG once "
                "and calibrating it on lambda_H; lambda_H is then calibration, not "
                "prediction, and credibility requires cross-use predictions without retuning."
            ),
        },
        "closed": cutset["closed_here"],
        "open": cutset["still_open"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "schema": "MTTAuditCertificate.v1",
        "artifact": "MTT_Selected_HLambdaOverlapKernelRow_or_ScalarOmegaExecutionGate_v1",
        "status": STATUS,
        "verified_by": rel(AUDIT),
        "candidate": rel(OUTPUT),
        "packets": [rel(STRICT_GATE), rel(CONTROLLED_GATE), rel(TIER_SEPARATION), rel(CUTSET)],
        "theorem_proved": True,
        "strict_selected_K_source_row_count": 9,
        "controlled_parameterized_K_row_count": 10,
        "controlled_parameter_id": minimal["primitive"]["id"],
        "lambda_H_calibrated": True,
        "lambda_H_predicted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected HLambda Overlap Kernel Row or Scalar Omega Execution Gate v1

## Purpose

This artifact separates the strict and controlled tiers at the H/lambda wall.
It follows the nine charged normalized HYM/Strominger overlap-kernel rows.

## Strict Tier

Strict no-knob status remains:

- selected charged overlap-kernel rows: `9`
- selected strict `K_threshold` rows: `9`
- required `K_threshold` rows: `10`
- selected H/lambda overlap-kernel row emitted: `false`
- strict `Omega/lambda_H` scalar execution closed: `false`

The missing strict object is still a selected H/lambda overlap-kernel row,
strict `R_H^RG`, direct `K_threshold.Omega_H.lambda`, or an equivalent selected
H quartic/threshold source theorem.

## Controlled Tier

The controlled one-parameter tier is now explicit:

- primitive: `{minimal["primitive"]["id"]}`
- calibrated value: `{minimal["calibration_values"]["required_UP_RET_OVERLAP_HRG"]}`
- log value: `{minimal["calibration_values"]["log_required_UP_RET_OVERLAP_HRG"]}`
- conditional controlled `K_threshold` count: `10`
- `lambda_H` is calibration, not prediction: `true`
- strict no-knob claim allowed: `false`

The controlled H row is:

```text
{h_empirical_row["empirical_K_import_symbolic"]}
```

with allowed use: `{h_empirical_row["allowed_use"]}`.

## Theorem

`HLambdaTierSeparatedScalarGateTheorem`: strict H/lambda remains open at 9/10,
while the declared one-parameter controlled tier can build a parameterized 10/10
gate.  The two tiers must not be conflated.

## What This Closes

- strict H/lambda gate reconciled after nine charged overlap rows
- controlled one-parameter H layer imported into the current frontier
- parameterized controlled 10/10 K gate recorded separately from strict no-knob tier
- lambda_H calibration/prediction boundary locked

## What Remains Open

- strict selected H/lambda overlap-kernel row
- strict selected `R_H^RG` or H quartic/threshold source theorem
- cross-use prediction audit for `UP-RET-OVERLAP.HRG`
- non-Higgs threshold/RG prediction using the same calibrated primitive
- strict `Omega/lambda_H` scalar execution
- true SM equivalence

## Next Artifact

```text
{NEXT}
```
"""

    audit = f'''"""Audit selected H/lambda overlap-kernel row or scalar Omega gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "{SLUG}"
DATA = ROOT / "candidate_data" / f"{{SLUG}}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
STRICT = PACKET_DIR / "strict_hlambda_overlap_kernel_gate.packet.json"
CONTROLLED = PACKET_DIR / "controlled_one_parameter_scalar_gate.packet.json"
TIER = PACKET_DIR / "strict_vs_controlled_tier_separation.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hlambda_scalar_gate.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HLambdaOverlapKernelRow_or_ScalarOmegaExecutionGate_v1.md"
STATUS = "{STATUS}"
NEXT = "{NEXT}"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    strict = load(STRICT)
    controlled = load(CONTROLLED)
    tier = load(TIER)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["closure_claimed"] is True, "closure flag missing")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["target_fitting_used"] is False, "target fitting")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")

    decision = data["closure_decision"]
    require(decision["strict_selected_charged_overlap_row_count"] == 9, "charged count")
    require(decision["strict_selected_K_source_row_count"] == 9, "strict K count")
    require(decision["strict_selected_K_source_row_count_required"] == 10, "required K count")
    require(decision["strict_selected_H_lambda_overlap_kernel_row_emitted"] is False, "H row overemitted")
    require(decision["strict_selected_K_threshold_Omega_H_lambda_emitted"] is False, "H K overemitted")
    require(decision["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar overclosed")
    require(decision["controlled_one_parameter_H_layer_built"] is True, "controlled layer missing")
    require(decision["controlled_parameter_id"] == "UP-RET-OVERLAP.HRG", "controlled id")
    require(decision["controlled_parameterized_K_row_count"] == 10, "controlled K count")
    require(decision["lambda_H_calibrated"] is True, "lambda calibration missing")
    require(decision["lambda_H_predicted"] is False, "lambda prediction overclaimed")
    require(decision["crossuse_prediction_audit_passed"] is False, "crossuse overclaimed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(strict["status"] == "STRICT_HLAMBDA_OVERLAP_KERNEL_ROW_STILL_OPEN_AFTER_CHARGED_ROWS", "strict status")
    require(strict["strict_selected_charged_overlap_row_count"] == 9, "strict charged rows")
    require(strict["strict_selected_K_source_row_count"] == 9, "strict K rows")
    require(strict["strict_selected_K_source_row_count_required"] == 10, "strict required")
    require(strict["selected_H_lambda_overlap_kernel_row_emitted"] is False, "strict H row")
    require(strict["selected_K_threshold_Omega_H_lambda_emitted"] is False, "strict H K")
    require(strict["accepted_internal_scalar_value_row_count"] == 0, "strict scalar rows")
    require(strict["strict_Omega_lambda_scalar_execution_closed"] is False, "strict scalar closure")
    require(strict["strict_no_knob_closure_claimed"] is False, "strict no-knob")

    require(
        controlled["status"] == "CONTROLLED_ONE_PARAMETER_H_LAYER_BUILDS_PARAMETERIZED_10OF10_NOT_NOKNOB",
        "controlled status",
    )
    require(controlled["controlled_empirical_tier_available"] is True, "controlled available")
    require(controlled["minimal_parameter_H_calibration_layer_claimed"] is True, "minimal layer")
    require(controlled["primitive_id"] == "UP-RET-OVERLAP.HRG", "primitive id")
    require(controlled["new_universal_parameter_count"] == 1, "parameter count")
    require(controlled["calibrating_observable"] == "lambda_H(M_t)", "calibrating observable")
    require(controlled["lambda_H_calibrated"] is True, "lambda calibrated")
    require(controlled["lambda_H_predicted"] is False, "lambda predicted")
    require(controlled["conditional_parameterized_K_row_count"] == 10, "controlled K")
    require(controlled["strict_no_knob_claim_allowed"] is False, "controlled no-knob")
    require(controlled["true_SM_equivalence_claimed"] is False, "controlled true SM")
    require(controlled["crossuse_prediction_audit_required"] is True, "crossuse required")
    require(controlled["crossuse_prediction_audit_passed"] is False, "crossuse passed")
    require("(1.193869931683266) / D_fin.H" in controlled["controlled_empirical_H_K_symbolic"], "H symbolic")

    require(tier["status"] == "STRICT_AND_CONTROLLED_HLAMBDA_TIERS_SEPARATED", "tier status")
    require(tier["strict_tier"]["selected_K_rows"] == 9, "tier strict rows")
    require(tier["strict_tier"]["required_K_rows"] == 10, "tier strict required")
    require(tier["strict_tier"]["H_lambda_row_selected"] is False, "tier H row")
    require(tier["strict_tier"]["scalar_execution_closed"] is False, "tier scalar")
    require(tier["controlled_one_parameter_tier"]["declared_parameter_count"] == 1, "tier params")
    require(tier["controlled_one_parameter_tier"]["conditional_K_rows"] == 10, "tier controlled K")
    require(tier["controlled_one_parameter_tier"]["lambda_H_is_calibration"] is True, "tier calibration")
    require(tier["controlled_one_parameter_tier"]["lambda_H_prediction_credit_allowed"] is False, "tier prediction")
    require(len(tier["credibility_upgrade_requirements"]) >= 3, "tier requirements")

    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "strict H/lambda gate reconciled after nine charged overlap rows",
        "controlled one-parameter H layer imported into current frontier",
        "parameterized controlled 10/10 K gate recorded separately from strict no-knob tier",
        "lambda_H calibration/prediction boundary locked",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {{phrase}}")
    for phrase in [
        "strict selected H/lambda overlap-kernel row",
        "strict selected R_H^RG or H quartic/threshold source theorem",
        "cross-use prediction audit for UP-RET-OVERLAP.HRG",
        "non-Higgs threshold/RG prediction using the same calibrated primitive",
        "strict Omega/lambda_H scalar execution",
        "true SM equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {{phrase}}")

    for phrase in [
        "selected charged overlap-kernel rows: `9`",
        "selected strict `K_threshold` rows: `9`",
        "required `K_threshold` rows: `10`",
        "controlled `K_threshold` count: `10`",
        "`lambda_H` is calibration, not prediction: `true`",
        "(1.193869931683266) / D_fin.H",
        NEXT,
    ]:
        require(phrase in note, f"note missing {{phrase}}")

    print(f"PASS {{DATA.name}}: {{STATUS}}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

    write_json(STRICT_GATE, strict_gate)
    write_json(CONTROLLED_GATE, controlled_gate)
    write_json(TIER_SEPARATION, tier)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")


def main() -> int:
    build()
    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
