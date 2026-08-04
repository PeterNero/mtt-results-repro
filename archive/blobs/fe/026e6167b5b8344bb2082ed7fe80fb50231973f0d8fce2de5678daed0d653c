"""Partially fill the visible Route-C source identity / typed B_N derivative gate.

This builder uses the already proved symbolic transport-conjugation replay to
promote the stationary visible/Route-C source-identity fields, while leaving
the alpha1-specific derivative and honest dotD replay unpromoted.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

TEMPLATE = DATA / "visible_routec_sourceidentity_or_typedbn_derivative.template.json"
TRANSPORT = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
GAUGE_TRACE = DATA / "selected_gauge_transported_bn_phifin_trace.candidate.json"
DOTD = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
ALPHA1_FILL = DATA / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"
VALIDATOR = ROOT / "scripts" / "validate_visible_routec_sourceidentity_or_typedbn_derivative.py"

OUTPUT = DATA / "visible_routec_sourceidentity_or_typedbn_derivative.partial_fill.json"
CERT = CERTS / "visible_routec_sourceidentity_or_typedbn_derivative_partial_fill_certificate.json"
NOTE = CORPUS / "MTT_Visible_RouteC_SourceIdentity_or_TypedBNRetardedDerivative_PartialFill_v1.md"

STATUS = "MTT_VISIBLE_ROUTEC_SOURCEIDENTITY_PARTIAL_FILL_ALPHA1_DERIVATIVE_OPEN"
NEXT = "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def promoted_field(required: str, path: Path, theorem: str) -> dict[str, Any]:
    return {
        "required": required,
        "selected_emitted": True,
        "same_branch": True,
        "theorem_derived": True,
        "provenance": "symbolic_transport_conjugation_theorem",
        "certificate_path": rel(path),
        "support_present": True,
        "support_source": rel(path),
        "theorem": theorem,
    }


def blocked_field(
    required: str,
    support: Path,
    reason: str,
    *,
    same_branch: bool = True,
    theorem_derived: bool = False,
    provenance: str = "selected_alpha1_payload_open",
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    field: dict[str, Any] = {
        "required": required,
        "selected_emitted": False,
        "same_branch": same_branch,
        "theorem_derived": theorem_derived,
        "provenance": provenance,
        "certificate_path": None,
        "support_present": True,
        "support_source": rel(support),
        "reason_not_selected": reason,
    }
    if extra:
        field.update(extra)
    return field


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        parsed = json.loads(proc.stdout)
    except json.JSONDecodeError:
        parsed = {"raw_output": proc.stdout}
    parsed["exit_code"] = proc.returncode
    return parsed


def build_note(data: dict[str, Any]) -> str:
    validation = data["validation"]
    return f"""# MTT Visible Route-C Source Identity / Typed B_N Derivative Partial Fill v1

Status: `{STATUS}`

Next artifact: `{NEXT}`

## Result

The first two Lane A fields are now filled by theorem-derived same-branch data:

- `source_identity`
- `visible_routec_operator_source`

The source is the symbolic transport-conjugation replay. It proves that the
selected diagonal End0/HYM connection is related to the model-active `B_N`
packet by the exact transport `U=exp(-u ad(T3))`, so stationary projector,
Riesz/Green, and source identities are accepted by exact conjugation rather
than by lifted finite flags.

## What Still Fails

The validator still rejects the packet, as it should. The remaining Lane A
blockers are:

- `phi_fin_payload`: the stationary transported trace is proved, but not the
  selected `Phi_fin alpha1` payload.
- `same_branch_alpha1_derivative`: the formula for a tangent `h=du/dalpha` is
  proved, but no theorem-derived physical `alpha1` driver selects `h_ext`.
- `dotd_validator_replay`: the source-only replay still fails exactly by
  `alpha1_driver_verified`.

Lane B remains an alternate route, but the retarded data are still support
patterns rather than theorem-derived typed `B_N` source values.

## Validator

The partial fill validator result is:

```json
{json.dumps(validation, indent=2, sort_keys=True)}
```

No observed constants, benchmark matrices, or diagnostic lifted flags are used
to promote a field.
"""


def main() -> int:
    template = load(TEMPLATE)
    transport = load(TRANSPORT)
    gauge = load(GAUGE_TRACE)
    dotd = load(DOTD)
    alpha1 = load(ALPHA1_FILL)

    candidate = copy.deepcopy(template)
    lane_a = candidate["lane_A_visible_routec_source_identity"]
    lane_b = candidate["lane_B_typed_bn_retarded_derivative"]

    transport_ok = (
        transport["validator_result"]["selected_source_verified"] is True
        and transport["validator_result"]["selected_rho_s_validator_ready"] is True
        and transport["what_closes_now"]["selected_projector_source_verified"] is True
    )
    gauge_ok = (
        gauge["what_closes_now"]["gauge_transported_PhiFin_trace"] is True
        and gauge["promotion_decision"]["selected_source_verified_for_functional_End0_trace"] is True
    )

    if not (transport_ok and gauge_ok):
        raise RuntimeError("stationary source transport prerequisites are not closed")

    lane_a["source_identity"] = promoted_field(
        "selected visible/Route-C operator-source identity on q79/F,m=1",
        TRANSPORT,
        "SelectedTransportConjugationValidatorReplay",
    )
    lane_a["visible_routec_operator_source"] = promoted_field(
        "selected visible bundle/sheaf/twisted-gerbe or Route-C source",
        GAUGE_TRACE,
        "SelectedGaugeTransportedBNPhiFinTrace",
    )
    lane_a["phi_fin_payload"] = blocked_field(
        "selected Phi_fin alpha1 payload values",
        GAUGE_TRACE,
        "The gauge-transported stationary Phi_fin trace is theorem-derived, but the alpha1 payload values are not emitted.",
        theorem_derived=True,
        provenance="stationary_trace_not_alpha1_payload",
        extra={"stationary_phi_fin_trace_selected": True},
    )
    lane_a["same_branch_alpha1_derivative"] = blocked_field(
        "same-branch derivative proving du/dalpha1 = h_ext",
        DOTD,
        "The transport derivative formula is proved for an arbitrary selected h=du/dalpha, but the physical alpha1 driver h_ext is not selected.",
        theorem_derived=True,
        provenance="driver_normalization_open",
        extra={
            "transport_derivative_formula_proved": True,
            "h_ext_residual_l2": dotd["driver_audit"]["h_ext_residual_l2"],
        },
    )
    lane_a["dotd_validator_replay"] = blocked_field(
        "honest dotD replay without lifted flags",
        DOTD,
        "The source-only replay fails only because alpha1_driver_verified is not theorem-derived.",
        theorem_derived=False,
        provenance="driver_normalization_open",
        extra={
            "honest_validator_exit_code": dotd["validator_boundary"]["source_only_validation"]["exit_code"],
            "source_only_fails_only_by_alpha1_driver": dotd["validator_boundary"][
                "source_only_fails_only_by_alpha1_driver"
            ],
            "validator_replay_path": dotd["validator_boundary"]["source_only_probe_path"],
        },
    )

    for name, field in lane_b.items():
        field["same_branch"] = bool(field.get("support_present"))
        field["provenance"] = field.get("provenance") or "retarded_pattern_support_only"
        field["reason_not_selected"] = "Lane B remains support-only until a non-observed typed B_N retarded derivative/source selector is emitted."

    candidate.update(
        {
            "status": STATUS,
            "schema": "MTTVisibleRouteCSourceIdentityOrTypedBNRetardedDerivative.v1",
            "next_required_artifact": NEXT,
            "closure_claimed": False,
            "target_fitting_used": False,
            "partial_fill_result": {
                "lane_A_source_identity_closed": True,
                "lane_A_visible_routec_operator_source_closed": True,
                "lane_A_phi_fin_alpha1_payload_closed": False,
                "lane_A_same_branch_alpha1_derivative_closed": False,
                "lane_A_dotd_validator_replay_closed": False,
                "lane_B_typed_retarded_derivative_closed": False,
                "alpha1_driver_promoted": False,
            },
            "packet_values_preserved": {
                "lambda_alpha1": alpha1["source_strength_coordinate"]["lambda_alpha1"],
                "N_alpha1_h_ext": alpha1["normalization_functional"]["N_alpha1_h_ext"],
                "local_hym_residual_l2": alpha1["tangent_equality"]["local_hym_residual_l2"],
                "tangent_residual_l2": alpha1["tangent_equality"]["residual_l2"],
            },
            "superset_strategy": {
                "classification": "STRAIGHT_LANE_A_PARTIAL_FILL_WITH_LANE_B_HELD_AS_ALTERNATIVE",
                "straight_path": "symbolic transport-conjugation promotes stationary visible/Route-C source identity",
                "alternative_path": "typed B_N retarded derivative remains available but support-only",
                "locked_target": "promote alpha1 only after Phi_fin alpha1 payload, same-branch derivative, and honest dotD replay validate",
                "uses_observed_constants": False,
            },
        }
    )

    candidate["validation"] = {"ok": False, "errors": ["validation pending"]}
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    # Validator must fail at this stage; the point is a strict partial fill.
    candidate["validation"] = run_validator(OUTPUT)
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    cert = {
        "certificate": "MTTVisibleRouteCSourceIdentityOrTypedBNRetardedDerivativePartialFill",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "validator_path": rel(VALIDATOR),
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "target_fitting_used": False,
        "lane_A_source_identity_closed": True,
        "lane_A_visible_routec_operator_source_closed": True,
        "remaining_lane_A_blockers": [
            "phi_fin_payload",
            "same_branch_alpha1_derivative",
            "dotd_validator_replay",
        ],
        "lane_B_closed": False,
        "alpha1_driver_verified": False,
        "validator_ok": candidate["validation"]["ok"],
        "validator_exit_code": candidate["validation"]["exit_code"],
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(build_note(candidate), encoding="utf-8")
    print(json.dumps({"status": STATUS, "candidate": rel(OUTPUT), "certificate": rel(CERT)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
