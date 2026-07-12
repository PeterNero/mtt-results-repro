"""Build the pin-down kernel for selected alpha1 normalization.

This artifact turns the remaining source-strength gap into an executable
acceptance contract.  It does not promote lambda_alpha1=1 by convention; it
defines the exact same-source packet or typed B_N retarded derivative needed to
promote it.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

VALUE_ATTEMPT = DATA / "selected_alpha1_source_strength_value_emission_attempt.candidate.json"
NORMALIZATION_THEOREM = DATA / "selected_alpha1_source_strength_normalization_theorem.candidate.json"
DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
TANGENT = DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
SAMESOURCE_PACKET = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
CONSTANTS_ALPHA1 = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-nonsm-constants-no-knob/candidate_data/"
    "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
)
Q79_DOTD = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro/certificates/"
    "q79_selected_dotd_alpha1_c1_response_emission_certificate.json"
)

OUTPUT = DATA / "selected_samesource_alpha1_normalization_pin_down_kernel.candidate.json"
TEMPLATE = DATA / "selected_samesource_alpha1_normalization_packet.template.json"
CERT = CERTS / "selected_samesource_alpha1_normalization_pin_down_kernel_certificate.json"
NOTE = CORPUS / "MTT_Selected_SameSource_Alpha1_Normalization_PinDown_Kernel_v1.md"

STATUS = "MTT_SELECTED_SAMESOURCE_ALPHA1_NORMALIZATION_PINDOWN_KERNEL_BUILT_PACKET_VALUES_OPEN"
NEXT = "MTT_Selected_SameSource_Alpha1_Normalization_Packet_Fill_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    value_attempt = load(VALUE_ATTEMPT)
    normalization = load(NORMALIZATION_THEOREM)
    dotd_probe = load(DOTD_PROBE)
    tangent = load(TANGENT)
    same_source = load(SAMESOURCE_PACKET)
    constants_alpha1 = load(CONSTANTS_ALPHA1)
    q79_dotd = load(Q79_DOTD)

    h = value_attempt["emission_attempt"]["conditional_value_candidate"]
    same_source_counts = same_source["field_counts"]
    transfer_checks = constants_alpha1["transfer_checks"]
    q79_obstruction = q79_dotd["selected_tangent_or_retarded_kernel_obstruction"]

    packet_schema = {
        "schema": "MTTSelectedSameSourceAlpha1NormalizationPacket.v1",
        "required_branch_id": "q79/F,m=1/S3_GS/RouteC_or_same_visible_source",
        "required_fields": {
            "source_identity": {
                "type": "selected_branch_certificate",
                "must_equal": "same source as selected Phi_fin/Strominger/HYM branch",
                "selected_emitted_now": False,
            },
            "source_strength_coordinate": {
                "type": "coordinate_emission",
                "must_emit": "alpha1 as the selected source-strength coordinate, not a free Ext-scale knob",
                "target_candidate": "lambda_alpha1 = 1",
                "selected_emitted_now": False,
            },
            "normalization_functional": {
                "type": "linear_functional_or_retarded_kernel_derivative",
                "must_emit": "N_alpha1 with N_alpha1(h_ext)=1, or typed d/dalpha1 Phi_fin whose zero-mean tangent is h_ext",
                "selected_emitted_now": False,
            },
            "tangent_equality": {
                "type": "finite_or_functional_equality",
                "must_prove": "h_selected_alpha1 = h_ext in the selected zero-mean HYM gauge",
                "tolerance": 1e-12,
                "current_h_ext_residual_l2": h["h_ext_residual_l2"],
                "selected_emitted_now": False,
            },
            "sector_dotd_equality": {
                "type": "operator_replay_equality",
                "must_prove": "transport-derived dotD_h equals the existing same-basis finite dotD_alpha1 matrices sector-by-sector",
                "selected_emitted_now": False,
            },
        },
        "forbidden_inputs": [
            "observed alpha_EM, weak angle, masses, CKM, PMNS, or CP phase",
            "benchmark matrices",
            "diagnostic lifted selected flags",
            "declaring lambda_alpha1=1 by coordinate convention alone",
            "importing CKM retarded-kernel pattern without typed q79 B_N alpha1 derivative",
        ],
    }

    acceptance_kernel = {
        "name": "SelectedSameSourceAlpha1NormalizationPinDownKernel",
        "promotes_value_if_and_only_if": [
            "source_identity.selected_emitted",
            "source_strength_coordinate.selected_emitted",
            "normalization_functional.selected_emitted",
            "tangent_equality.residual_l2 <= 1e-12",
            "sector_dotd_equality.selected_emitted",
            "honest_dotd_validator_replay_passes_without_lifted_flags",
        ],
        "selected_value_when_passed": {
            "lambda_alpha1": 1.0,
            "du_dalpha1": "h_ext",
            "h_ext_l2": h["h_ext_l2"],
            "h_ext_residual_l2": h["h_ext_residual_l2"],
            "alpha1_driver_verified": True,
            "selected_value_emitted": True,
        },
        "current_evaluation": {
            "source_identity_selected": False,
            "source_strength_coordinate_selected": False,
            "normalization_functional_selected": False,
            "tangent_equality_selected": False,
            "sector_dotd_equality_selected": False,
            "honest_dotd_validator_replay_without_lifted_flags": False,
            "selected_value_emitted_now": False,
        },
    }

    route_status = {
        "route_A_same_source_packet": {
            "preferred": True,
            "same_source_required_fields": same_source_counts["required"],
            "same_source_selected_fields": same_source_counts["selected_emitted"],
            "normalization_available_now": False,
            "why_open": "The current same-source packet is a contract with support fields only; no selected normalization functional is emitted.",
        },
        "route_B_typed_BN_retarded_kernel": {
            "preferred": False,
            "ckm_pattern_available": transfer_checks["K1_ckm_retarded_kernel_pattern_available"],
            "selected_transfer_normalization": transfer_checks["K5_selected_transfer_normalization"],
            "selected_BN_tangent_or_retarded_kernel": transfer_checks[
                "K6_selected_BN_tangent_or_retarded_kernel"
            ],
            "retarded_derivative_formula": q79_obstruction["derivative_payload_checks"][
                "D6_retarded_overlap_derivative_formula"
            ],
            "why_open": "Retarded structure is available as a pattern, but the typed q79 B_N alpha1 derivative is not emitted.",
        },
    }

    data = {
        "candidate": "MTTSelectedSameSourceAlpha1NormalizationPinDownKernel",
        "status": STATUS,
        "inputs": {
            "value_attempt": rel(VALUE_ATTEMPT),
            "normalization_theorem": rel(NORMALIZATION_THEOREM),
            "dotd_probe": rel(DOTD_PROBE),
            "tangent": rel(TANGENT),
            "same_source_packet": rel(SAMESOURCE_PACKET),
            "constants_alpha1": rel(CONSTANTS_ALPHA1),
            "q79_dotd": rel(Q79_DOTD),
        },
        "packet_schema": packet_schema,
        "acceptance_kernel": acceptance_kernel,
        "route_status": route_status,
        "pin_down_result": {
            "lambda_alpha1_candidate_pinned_as_unique_current_candidate": True,
            "lambda_alpha1_selected_now": False,
            "reason": (
                "The kernel identifies exactly when the unit source-strength candidate becomes selected, "
                "but current artifacts do not emit the needed same-source normalization functional or typed "
                "B_N retarded derivative."
            ),
            "minimal_next_fill": [
                "source_identity",
                "source_strength_coordinate",
                "normalization_functional",
                "tangent_equality",
                "sector_dotd_equality",
            ],
        },
        "what_closes_now": {
            "promotion_acceptance_kernel_built": True,
            "minimal_same_source_packet_schema_built": True,
            "retarded_kernel_alternative_schema_built": True,
            "lambda_alpha1_unit_candidate_unique_under_current_local_algebra": True,
            "unsafe_coordinate_promotion_excluded": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "fill_selected_samesource_alpha1_normalization_packet": True,
            "or_emit_typed_BN_retarded_alpha1_kernel": True,
            "prove_sector_dotd_equality": True,
            "run_honest_dotd_validator_without_lifted_flags": True,
            "promote_alpha1_driver_verified": True,
            "full_SM_or_no_knob_closure": True,
        },
        "superset_strategy": {
            "classification": "PIN_DOWN_KERNEL_FOR_SUPERSET_ROUTES",
            "straight_path": "same-source HYM/Strominger/Phi_fin normalization packet",
            "alternative_path": "typed q79 B_N retarded-overlap derivative kernel",
            "locked_target": "promote lambda_alpha1=1 and du/dalpha1=h_ext only after same-branch source emission",
            "uses_observed_constants": False,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    template = {
        "schema": packet_schema["schema"],
        "status": "TEMPLATE_VALUES_TO_FILL",
        "branch_id": None,
        "source_identity": {
            "selected_emitted": False,
            "certificate_path": None,
            "same_branch_as": "selected Phi_fin/Strominger/HYM branch",
        },
        "source_strength_coordinate": {
            "selected_emitted": False,
            "symbol": "alpha1",
            "lambda_alpha1": None,
            "derivation": None,
        },
        "normalization_functional": {
            "selected_emitted": False,
            "kind": None,
            "N_alpha1_h_ext": None,
            "derivation": None,
        },
        "tangent_equality": {
            "selected_emitted": False,
            "h_selected_alpha1": None,
            "h_ext_reference": "candidate_data/selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json",
            "residual_l2": None,
            "tolerance": 1e-12,
        },
        "sector_dotd_equality": {
            "selected_emitted": False,
            "sector_residuals_l2": {},
            "validator_replay_path": None,
        },
        "forbidden_inputs_used": [],
    }

    cert = {
        "certificate": "MTT_Selected_SameSource_Alpha1_Normalization_PinDown_Kernel_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "template_path": rel(TEMPLATE),
        "note_path": rel(NOTE),
        "promotion_acceptance_kernel_built": True,
        "minimal_packet_schema_built": True,
        "lambda_alpha1_candidate": 1.0,
        "lambda_alpha1_selected_now": False,
        "selected_value_emitted": False,
        "alpha1_driver_verified": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Same-Source Alpha1 Normalization Pin-Down Kernel v1

Status: `{STATUS}`.

## Pin-Down Kernel

The current local algebra gives one candidate:

```text
lambda_alpha1 = 1
du/dalpha1 = h_ext
||h_ext||_L2 = {h["h_ext_l2"]}
residual_L2 = {h["h_ext_residual_l2"]}
```

This artifact defines when that candidate is selected:

```text
selected source identity
+ selected alpha1 source-strength coordinate
+ selected normalization functional N_alpha1 with N_alpha1(h_ext)=1
+ residual(h_selected_alpha1 - h_ext) <= 1e-12
+ sector dotD equality
+ honest dotD validator replay
```

Only then may the repo set:

```text
selected_value_emitted = true
alpha1_driver_verified = true
```

## Why This Pins It Down

The ambiguity is now reduced to a finite packet fill, not a conceptual gap.
Either the same-source packet emits the normalization functional, or a typed
`B_N` retarded-overlap kernel emits the same derivative.  The template
`{rel(TEMPLATE)}` is the fill target.

No observed constants, benchmark matrices, target fits, or lifted flags are
admissible.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    TEMPLATE.write_text(json.dumps(template, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(TEMPLATE)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
