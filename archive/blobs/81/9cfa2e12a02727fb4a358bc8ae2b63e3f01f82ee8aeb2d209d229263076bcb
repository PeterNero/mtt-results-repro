"""Build the next alpha1 provenance certificate contract.

This artifact constructs the exact certificate and validator needed next.  It
does not claim that either lane is already filled; it makes the required fields
explicit and executable so a future fill can promote the alpha1 normalization
packet immediately if it validates.
"""

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

PREVIOUS = DATA / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt.candidate.json"
FILLED_PACKET = DATA / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"
SOURCE_DRIVER = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
PHIFIN_ALPHA1 = DATA / "selected_phifin_alpha1_payload.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
CONSTANTS_RETARDED = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-nonsm-constants-no-knob/candidate_data/"
    "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
)

TEMPLATE = DATA / "visible_routec_sourceidentity_or_typedbn_derivative.template.json"
OUTPUT = DATA / "visible_routec_sourceidentity_or_typedbn_derivative_contract.candidate.json"
CERT = CERTS / "visible_routec_sourceidentity_or_typedbn_derivative_contract_certificate.json"
NOTE = CORPUS / "MTT_Visible_RouteC_SourceIdentity_or_TypedBNRetardedDerivative_Contract_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_visible_routec_sourceidentity_or_typedbn_derivative.py"

STATUS = "MTT_VISIBLE_ROUTEC_SOURCEIDENTITY_OR_TYPEDBN_DERIVATIVE_CONTRACT_BUILT_VALUES_OPEN"
NEXT = "MTT_Visible_RouteC_SourceIdentity_or_TypedBNRetardedDerivative_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def blank_field(required: str, support: bool, support_source: str | None = None) -> dict[str, Any]:
    return {
        "required": required,
        "support_present": support,
        "support_source": support_source,
        "selected_emitted": False,
        "same_branch": False,
        "theorem_derived": False,
        "provenance": None,
        "certificate_path": None,
    }


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


def main() -> int:
    previous = load(PREVIOUS)
    packet = load(FILLED_PACKET)
    source_driver = load(SOURCE_DRIVER)
    phifin = load(PHIFIN_ALPHA1)
    dotd_probe = load(DOTD_PROBE)
    constants_retarded = load(CONSTANTS_RETARDED)

    packet_values = {
        "lambda_alpha1": packet["source_strength_coordinate"]["lambda_alpha1"],
        "N_alpha1_h_ext": packet["normalization_functional"]["N_alpha1_h_ext"],
        "tangent_residual_l2": packet["tangent_equality"]["residual_l2"],
        "local_hym_residual_l2": packet["tangent_equality"]["local_hym_residual_l2"],
    }

    lane_a_support = previous["proof_lanes"]["lane_A_same_source_identity"]["support_closed"]
    lane_b_support = previous["proof_lanes"]["lane_B_typed_retarded_kernel"]["support_closed"]
    transfer = constants_retarded["transfer_checks"]

    template = {
        "schema": "MTTVisibleRouteCSourceIdentityOrTypedBNRetardedDerivative.v1",
        "status": "TEMPLATE_VALUES_TO_FILL",
        "branch_id": "q79/F,m=1/S3_GS/RouteC_or_same_visible_source",
        "forbidden_inputs_used": [],
        "lane_A_visible_routec_source_identity": {
            "source_identity": blank_field(
                "selected visible/Route-C operator-source identity on q79/F,m=1",
                lane_a_support["same_source_support_converges"],
                rel(SOURCE_DRIVER),
            ),
            "visible_routec_operator_source": blank_field(
                "selected visible bundle/sheaf/twisted-gerbe or Route-C source",
                source_driver["source_origin_audit"]["support_closed"]["visible_chern_weil_contract_reduced"],
                rel(SOURCE_DRIVER),
            ),
            "phi_fin_payload": blank_field(
                "selected Phi_fin alpha1 payload values",
                phifin["payload_summary"]["all_support_shapes_present"],
                rel(PHIFIN_ALPHA1),
            ),
            "same_branch_alpha1_derivative": blank_field(
                "same-branch derivative proving du/dalpha1 = h_ext",
                dotd_probe["promotion_decision"]["selected_dotD_source_formula_closed"],
                rel(DOTD_PROBE),
            ),
            "dotd_validator_replay": {
                **blank_field(
                    "honest dotD replay without lifted flags",
                    dotd_probe["validator_boundary"][
                        "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"
                    ],
                    rel(DOTD_PROBE),
                ),
                "honest_validator_exit_code": None,
                "validator_replay_path": None,
            },
        },
        "lane_B_typed_bn_retarded_derivative": {
            "retarded_source_selector": blank_field(
                "non-observed retarded/source selector choosing the q79 orientation",
                lane_b_support["ckm_retarded_kernel_pattern_available"],
                rel(CONSTANTS_RETARDED),
            ),
            "typed_bn_alpha1_derivative": blank_field(
                "typed q79 B_N alpha1 derivative or retarded-overlap derivative",
                transfer["K2_q79_phi_fin_alpha1_support_available"],
                rel(CONSTANTS_RETARDED),
            ),
            "selected_transfer_normalization": blank_field(
                "selected transfer normalization with N_alpha1(h_ext)=1",
                transfer["K1_ckm_retarded_kernel_pattern_available"],
                rel(CONSTANTS_RETARDED),
            ),
            "sector_dotd_equality": blank_field(
                "sector equality from typed derivative to existing dotD matrices",
                lane_b_support["q79_and_q369_reach_de_green_dotd_layer"],
                rel(CONSTANTS_RETARDED),
            ),
            "dotd_validator_replay": {
                **blank_field(
                    "honest dotD replay from typed kernel without lifted flags",
                    transfer["K1_ckm_retarded_kernel_pattern_available"],
                    rel(CONSTANTS_RETARDED),
                ),
                "honest_validator_exit_code": None,
                "validator_replay_path": None,
            },
        },
        "promotion_result": {
            "selected_value_emitted": False,
            "alpha1_driver_verified": False,
            "lambda_alpha1": packet_values["lambda_alpha1"],
            "N_alpha1_h_ext": packet_values["N_alpha1_h_ext"],
            "target_fitting_used": False,
        },
    }

    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True), encoding="utf-8")
    validator_report = run_validator(TEMPLATE)

    data = {
        "candidate": "MTTVisibleRouteCSourceIdentityOrTypedBNRetardedDerivativeContract",
        "status": STATUS,
        "inputs": {
            "previous_attempt": rel(PREVIOUS),
            "filled_alpha1_packet": rel(FILLED_PACKET),
            "source_driver": rel(SOURCE_DRIVER),
            "phifin_alpha1": rel(PHIFIN_ALPHA1),
            "dotd_probe": rel(DOTD_PROBE),
            "constants_retarded": rel(CONSTANTS_RETARDED),
        },
        "template_path": rel(TEMPLATE),
        "validator_path": rel(VALIDATOR),
        "template_validation": validator_report,
        "packet_values_preserved": packet_values,
        "required_certificate": {
            "schema": template["schema"],
            "branch_id": template["branch_id"],
            "lane_A_fields": list(template["lane_A_visible_routec_source_identity"].keys()),
            "lane_B_fields": list(template["lane_B_typed_bn_retarded_derivative"].keys()),
            "promotion_rule": (
                "If either lane validates, promote the filled alpha1 packet by setting "
                "selected_value_emitted=true and alpha1_driver_verified=true."
            ),
            "forbidden_provenance": [
                "support_shape_only",
                "diagnostic_lift",
                "observed_sm_data",
                "benchmark_matrix",
                "retarded_pattern_only",
                "coordinate_convention_only",
            ],
        },
        "current_result": {
            "contract_built": True,
            "template_validates_now": False,
            "reason": "The template intentionally has values open; it is the next fill target.",
            "lane_A_preferred": True,
            "lane_B_available_as_alternative": True,
        },
        "what_closes_now": {
            "dual_lane_certificate_template_built": True,
            "promotion_validator_built": True,
            "alpha1_packet_values_bound_to_certificate": True,
            "support_sources_attached": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "fill_lane_A_selected_source_identity": True,
            "or_fill_lane_B_typed_retarded_derivative": True,
            "honest_dotD_validator_replay_without_lifted_flags": True,
            "promote_alpha1_driver_verified": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "classification": "DUAL_LANE_CERTIFICATE_CONTRACT",
            "straight_path": "selected visible/Route-C source identity certificate",
            "alternative_path": "typed B_N retarded alpha1 derivative",
            "locked_target": "promote the filled alpha1 normalization packet",
            "uses_observed_constants": False,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Visible_RouteC_SourceIdentity_or_TypedBNRetardedDerivative_Contract_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "template_path": rel(TEMPLATE),
        "validator_path": rel(VALIDATOR),
        "note_path": rel(NOTE),
        "lambda_alpha1": packet_values["lambda_alpha1"],
        "N_alpha1_h_ext": packet_values["N_alpha1_h_ext"],
        "contract_built": True,
        "template_validates_now": False,
        "selected_value_emitted": False,
        "alpha1_driver_verified": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Visible RouteC SourceIdentity or TypedBN RetardedDerivative Contract v1

Status: `{STATUS}`.

## Purpose

This is the exact object needed next.  It supplies a dual-lane certificate
template and validator for promoting the already-filled alpha1 normalization
packet.

Preserved packet values:

```text
lambda_alpha1 = {packet_values["lambda_alpha1"]}
N_alpha1(h_ext) = {packet_values["N_alpha1_h_ext"]}
tangent residual = {packet_values["tangent_residual_l2"]}
```

## Lane A

Fill selected visible/Route-C source identity:

```text
source_identity
visible_routec_operator_source
phi_fin_payload
same_branch_alpha1_derivative
dotd_validator_replay
```

## Lane B

Fill typed `B_N` retarded derivative:

```text
retarded_source_selector
typed_bn_alpha1_derivative
selected_transfer_normalization
sector_dotd_equality
dotd_validator_replay
```

If either lane validates, the filled alpha1 packet can promote
`selected_value_emitted=true` and `alpha1_driver_verified=true`.

Template: `{rel(TEMPLATE)}`

Validator: `{rel(VALIDATOR)}`

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(TEMPLATE)}")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
