"""Try to fill the selected same-source alpha1 normalization packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

TEMPLATE = DATA / "selected_samesource_alpha1_normalization_packet.template.json"
KERNEL = DATA / "selected_samesource_alpha1_normalization_pin_down_kernel.candidate.json"
VALUE_ATTEMPT = DATA / "selected_alpha1_source_strength_value_emission_attempt.candidate.json"
TANGENT = DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
NORMALIZATION_THEOREM = DATA / "selected_alpha1_source_strength_normalization_theorem.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
SOURCE_DRIVER = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
SAMESOURCE_PACKET = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"

PACKET = DATA / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"
OUTPUT = DATA / "selected_samesource_alpha1_normalization_packet_fill_attempt.candidate.json"
CERT = CERTS / "selected_samesource_alpha1_normalization_packet_fill_attempt_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_Attempt_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_samesource_alpha1_normalization_packet.py"

STATUS = "MTT_SELECTED_SAMESOURCE_ALPHA1_NORMALIZATION_PACKET_FILL_ATTEMPT_FAILED_FINAL_VALIDATION"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_SourceIdentity_or_RetardedKernel_Value_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        report = json.loads(proc.stdout)
    except json.JSONDecodeError:
        report = {"raw_output": proc.stdout}
    report["exit_code"] = proc.returncode
    return report


def field(
    *,
    selected: bool,
    same_source: bool,
    theorem: bool,
    provenance: str,
    support: bool,
    reason: str,
    **extra: Any,
) -> dict[str, Any]:
    return {
        "selected_emitted": selected,
        "same_source": same_source,
        "theorem_derived": theorem,
        "provenance": provenance,
        "support_present": support,
        "reason_not_selected": reason,
        **extra,
    }


def main() -> int:
    template = load(TEMPLATE)
    kernel = load(KERNEL)
    value_attempt = load(VALUE_ATTEMPT)
    tangent = load(TANGENT)
    normalization = load(NORMALIZATION_THEOREM)
    dotd_probe = load(DOTD_PROBE)
    source_driver = load(SOURCE_DRIVER)
    same_source = load(SAMESOURCE_PACKET)

    h = value_attempt["emission_attempt"]["conditional_value_candidate"]
    h_l2_sq = h["h_ext_l2"] ** 2
    source_support = source_driver["source_origin_audit"]["support_closed"]
    selected_flags = source_driver["source_origin_audit"]["selected_flags"]
    dotd_boundary = dotd_probe["validator_boundary"]

    packet = {
        **template,
        "status": "FILL_ATTEMPT_VALUES_PRESENT_FINAL_VALIDATION_FAILED",
        "branch_id": "q79/F,m=1/S3_GS/RouteC_or_same_visible_source",
        "source_identity": field(
            selected=False,
            same_source=source_support["same_source_support_converges"],
            theorem=False,
            provenance="support_shape_only",
            support=True,
            reason=(
                "Source-level q79/F,m=1 S3/GS support converges, but selected visible/Route-C "
                "operator-source identity is still not theorem-emitted."
            ),
            certificate_path=rel(SOURCE_DRIVER),
            selected_flags=selected_flags,
        ),
        "source_strength_coordinate": field(
            selected=False,
            same_source=True,
            theorem=False,
            provenance="coordinate_convention_only",
            support=True,
            reason=(
                "lambda_alpha1=1 is the unique current unit coordinate candidate, but the "
                "source-strength coordinate itself is not emitted by the same branch."
            ),
            symbol="alpha1",
            lambda_alpha1=1.0,
            derivation="conditional unit coordinate from transport/value-emission attempt",
        ),
        "normalization_functional": field(
            selected=False,
            same_source=True,
            theorem=False,
            provenance="coordinate_convention_only",
            support=True,
            reason=(
                "The canonical dual functional N(f)=<f,h_ext>/||h_ext||^2 gives N(h_ext)=1, "
                "but this is not a selected MTT normalization functional."
            ),
            kind="canonical_L2_dual_to_h_ext",
            formula="N_alpha1(f)=<f,h_ext>/||h_ext||_L2^2",
            h_ext_l2_squared=h_l2_sq,
            N_alpha1_h_ext=1.0,
        ),
        "tangent_equality": field(
            selected=False,
            same_source=True,
            theorem=False,
            provenance="support_shape_only",
            support=True,
            reason=(
                "The local HYM tangent h_ext is solved with residual below tolerance, but no "
                "selected h_alpha1 from the same source is emitted to compare against it."
            ),
            h_selected_alpha1="candidate_h_ext_only",
            h_ext_reference=rel(TANGENT),
            residual_l2=0.0,
            local_hym_residual_l2=h["h_ext_residual_l2"],
            tolerance=1e-12,
        ),
        "sector_dotd_equality": field(
            selected=False,
            same_source=False,
            theorem=False,
            provenance="diagnostic_lift",
            support=True,
            reason=(
                "Full-flag dotD replay passes only as a diagnostic when flags are lifted; the "
                "honest no-lift packet still fails by alpha1_driver_verified."
            ),
            sector_residuals_l2={},
            validator_replay_path=dotd_boundary["source_only_probe_path"],
            honest_validator_exit_code=dotd_boundary["source_only_validation"]["exit_code"],
            full_flag_validator_exit_code=dotd_boundary["full_flag_validation"]["exit_code"],
            diagnostic_lift_used_as_proof=False,
            source_only_fails_only_by_alpha1_driver=dotd_boundary["source_only_fails_only_by_alpha1_driver"],
        ),
        "forbidden_inputs_used": [],
        "promotion_result": {
            "selected_value_emitted": False,
            "alpha1_driver_verified": False,
            "honest_dotd_validator_closed": False,
            "target_fitting_used": False,
        },
    }

    PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True), encoding="utf-8")
    validator_report = run_validator(PACKET)

    fields = [
        "source_identity",
        "source_strength_coordinate",
        "normalization_functional",
        "tangent_equality",
        "sector_dotd_equality",
    ]
    data = {
        "candidate": "MTTSelectedSameSourceAlpha1NormalizationPacketFillAttempt",
        "status": STATUS,
        "inputs": {
            "template": rel(TEMPLATE),
            "pin_down_kernel": rel(KERNEL),
            "value_attempt": rel(VALUE_ATTEMPT),
            "tangent": rel(TANGENT),
            "normalization_theorem": rel(NORMALIZATION_THEOREM),
            "dotd_probe": rel(DOTD_PROBE),
            "source_driver": rel(SOURCE_DRIVER),
            "same_source_packet": rel(SAMESOURCE_PACKET),
        },
        "filled_packet_path": rel(PACKET),
        "fill_summary": {
            "required_fields": len(fields),
            "candidate_values_filled": len(fields),
            "selected_emitted_fields": sum(1 for name in fields if packet[name]["selected_emitted"]),
            "support_present_fields": sum(1 for name in fields if packet[name]["support_present"]),
            "validator_ok": validator_report.get("ok", False),
            "validator_exit_code": validator_report["exit_code"],
        },
        "validator_report": validator_report,
        "kernel_decision": {
            "lambda_alpha1": 1.0,
            "N_alpha1_h_ext": 1.0,
            "tangent_residual_l2": 0.0,
            "local_hym_residual_l2": h["h_ext_residual_l2"],
            "promotes_selected_value": False,
            "reason": (
                "The exact candidate values can be filled, but the selected-source, theorem-derived, "
                "same-source flags required by the pin-down kernel are still absent."
            ),
        },
        "failed_fields": {
            name: packet[name]["reason_not_selected"]
            for name in fields
            if packet[name]["selected_emitted"] is not True
        },
        "what_closes_now": {
            "exact_packet_fill_attempted": True,
            "lambda_alpha1_value_inserted": True,
            "canonical_dual_normalization_inserted": True,
            "tangent_equality_candidate_inserted": True,
            "final_validator_executed": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_source_identity": True,
            "selected_source_strength_coordinate": True,
            "selected_normalization_functional": True,
            "selected_h_alpha1_tangent_from_same_source": True,
            "honest_sector_dotd_equality": True,
            "alpha1_driver_verified": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "classification": "EXACT_PACKET_FILL_ATTEMPT_FINAL_VALIDATION_FAILED",
            "straight_path_tested": "same-source normalization packet with canonical h_ext dual",
            "alternative_path_remaining": "typed B_N retarded alpha1 kernel",
            "locked_target": "lambda_alpha1=1 promoted only by selected same-source theorem",
            "uses_observed_constants": False,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_Attempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "filled_packet_path": rel(PACKET),
        "note_path": rel(NOTE),
        "validator_ok": validator_report.get("ok", False),
        "validator_exit_code": validator_report["exit_code"],
        "lambda_alpha1": 1.0,
        "N_alpha1_h_ext": 1.0,
        "selected_value_emitted": False,
        "alpha1_driver_verified": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Same-Source Alpha1 Normalization Packet Fill Attempt v1

Status: `{STATUS}`.

## Filled Candidate Values

```text
lambda_alpha1 = 1
N_alpha1(h_ext) = 1
tangent residual = 0
local HYM residual = {h["h_ext_residual_l2"]}
```

The attempted normalization functional is the canonical local dual:

```text
N_alpha1(f) = <f,h_ext> / ||h_ext||_L2^2
```

This fills the exact numerical candidate packet, but final validation fails.
The reason is not numerical: the packet still lacks theorem-derived selected
source identity, selected source-strength coordinate, selected normalization
functional, selected same-source tangent emission, and honest no-lift sector
dotD equality.

## Final Validation

Validator: `validate_samesource_alpha1_normalization_packet.py`

```text
ok = {validator_report.get("ok", False)}
exit_code = {validator_report["exit_code"]}
```

No observed constants, benchmark matrices, target fits, or lifted flags are used
as proof.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(PACKET)}")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(json.dumps({"status": STATUS, "validator_ok": validator_report.get("ok", False)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
