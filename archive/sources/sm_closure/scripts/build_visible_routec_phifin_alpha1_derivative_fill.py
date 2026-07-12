"""Build the visible Route-C Phi_fin alpha1 derivative fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "visible_routec_phifin_alpha1_derivative_fill"
OUT = ROOT / "candidate_data" / SLUG
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Visible_RouteC_PhiFinAlpha1Derivative_Fill_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_visible_routec_sourceidentity_or_typedbn_derivative.py"

PARTIAL = ROOT / "candidate_data" / "visible_routec_sourceidentity_or_typedbn_derivative.partial_fill.json"
PHIFIN = ROOT / "candidate_data" / "selected_phifin_alpha1_payload.candidate.json"
DOTD = ROOT / "candidate_data" / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
TRANSPORT = ROOT / "candidate_data" / "selected_transport_conjugation_validator_replay.candidate.json"
ALPHA_PACKET = ROOT / "candidate_data" / "selected_samesource_alpha1_normalization_packet.fill_attempt.json"

STATUS = "MTT_VISIBLE_ROUTEC_PHIFIN_ALPHA1_DERIVATIVE_FILL_ATTEMPT_BUILT_PAYLOAD_DRIVER_OPEN"
NEXT = "MTT_Selected_PhiFinAlpha1PayloadValues_or_TypedBNRetardedDerivativeExecution_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validator_result(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        payload = {"validator": VALIDATOR.name, "path": str(path), "ok": False, "errors": [proc.stdout]}
    payload["exit_code"] = proc.returncode
    return payload


def lane_field(
    *,
    required: str,
    support_source: str,
    support_present: bool,
    selected_emitted: bool,
    same_branch: bool,
    theorem_derived: bool,
    provenance: str | None,
    certificate_path: str | None = None,
    reason_not_selected: str | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    field: dict[str, Any] = {
        "required": required,
        "support_source": support_source,
        "support_present": support_present,
        "selected_emitted": selected_emitted,
        "same_branch": same_branch,
        "theorem_derived": theorem_derived,
        "provenance": provenance,
        "certificate_path": certificate_path,
    }
    if reason_not_selected:
        field["reason_not_selected"] = reason_not_selected
    if extra:
        field.update(extra)
    return field


def main() -> int:
    partial = load(PARTIAL)
    phifin = load(PHIFIN)
    dotd = load(DOTD)
    transport = load(TRANSPORT)
    alpha_packet = load(ALPHA_PACKET)

    payload_flags = phifin["payload_summary"]["selected_payload_flags"]
    all_support = phifin["payload_summary"]["all_support_shapes_present"]
    selected_payload_values_closed = all(payload_flags.values())
    dotd_formula_closed = dotd["promotion_decision"]["selected_dotD_source_formula_closed"]
    alpha_driver_closed = dotd["promotion_decision"]["alpha1_driver_verified"]
    honest_dotd_closed = dotd["validator_boundary"]["source_only_validation"]["exit_code"] == 0

    lane_a = partial["lane_A_visible_routec_source_identity"]
    fill = {
        "schema": "MTTVisibleRouteCSourceIdentityOrTypedBNRetardedDerivative.v1",
        "branch_id": partial["branch_id"],
        "forbidden_inputs_used": [],
        "lane_A_visible_routec_source_identity": {
            "source_identity": lane_a["source_identity"],
            "visible_routec_operator_source": lane_a["visible_routec_operator_source"],
            "phi_fin_payload": lane_field(
                required="selected Phi_fin alpha1 payload values",
                support_source=str(PHIFIN.relative_to(ROOT)).replace("\\", "/"),
                support_present=all_support,
                selected_emitted=False,
                same_branch=True,
                theorem_derived=False,
                provenance="support_shape_only",
                reason_not_selected=(
                    "All support shapes are present, but selected rho_E, D_E, Green, dotD, "
                    "C1 Hessian, zero-mode basis, and primitive contraction payload flags remain false."
                ),
                extra={
                    "stationary_phi_fin_trace_selected": True,
                    "selected_payload_values_closed": selected_payload_values_closed,
                    "open_payload_flags": [key for key, value in payload_flags.items() if value is False],
                },
            ),
            "same_branch_alpha1_derivative": lane_field(
                required="same-branch derivative proving du/dalpha1 = h_ext",
                support_source=str(DOTD.relative_to(ROOT)).replace("\\", "/"),
                support_present=dotd_formula_closed,
                selected_emitted=False,
                same_branch=True,
                theorem_derived=False,
                provenance="driver_normalization_open",
                reason_not_selected=(
                    "The transport derivative formula is proved for h=du/dalpha, but h_ext is still not "
                    "theorem-selected as the physical alpha1 driver."
                ),
                extra={
                    "transport_derivative_formula_proved": dotd_formula_closed,
                    "h_ext_residual_l2": dotd["driver_audit"]["h_ext_residual_l2"],
                    "alpha1_driver_verified": alpha_driver_closed,
                },
            ),
            "dotd_validator_replay": lane_field(
                required="honest dotD replay without lifted flags",
                support_source=str(DOTD.relative_to(ROOT)).replace("\\", "/"),
                support_present=True,
                selected_emitted=False,
                same_branch=True,
                theorem_derived=False,
                provenance="driver_normalization_open",
                reason_not_selected="The honest no-lift validator still fails only because alpha1_driver_verified is false.",
                extra={
                    "honest_validator_exit_code": dotd["validator_boundary"]["source_only_validation"]["exit_code"],
                    "source_only_fails_only_by_alpha1_driver": dotd["validator_boundary"]["source_only_fails_only_by_alpha1_driver"],
                    "validator_replay_path": dotd["validator_boundary"]["source_only_probe_path"],
                },
            ),
        },
        "lane_B_typed_bn_retarded_derivative": partial["lane_B_typed_bn_retarded_derivative"],
        "promotion_result": {
            "lambda_alpha1": alpha_packet["source_strength_coordinate"]["lambda_alpha1"],
            "N_alpha1_h_ext": alpha_packet["normalization_functional"]["N_alpha1_h_ext"],
            "selected_value_emitted": False,
            "alpha1_driver_verified": False,
            "target_fitting_used": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "status": STATUS,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    fill_path = OUT / "visible_routec_phifin_alpha1_derivative_fill.packet.json"
    write_json(fill_path, fill)
    validation = validator_result(fill_path)
    fill["validation"] = validation
    write_json(fill_path, fill)

    obstruction = {
        "status": "PHIFIN_ALPHA1_DERIVATIVE_FILL_OBSTRUCTION_EXACT",
        "closed_now": [
            "stationary visible/Route-C source identity remains filled",
            "visible operator source remains filled",
            "transport derivative formula is imported",
            "honest validator failure is localized to alpha1_driver_verified",
        ],
        "remaining_lane_A_blockers": {
            "selected_PhiFin_alpha1_payload_values": not selected_payload_values_closed,
            "same_branch_alpha1_driver_theorem": not alpha_driver_closed,
            "honest_dotD_validator_replay": not honest_dotd_closed,
        },
        "selected_payload_open_flags": [key for key, value in payload_flags.items() if value is False],
        "minimal_ways_forward": [
            "emit selected Phi_fin alpha1 payload values from the same q79/F,m=1 branch",
            "prove h_ext is the same-branch physical alpha1 driver and promote N_alpha1(h_ext)=1",
            "or execute Lane B with a theorem-derived typed B_N retarded derivative and transfer normalization",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUT / "phifin_alpha1_derivative_obstruction.packet.json", obstruction)

    candidate = {
        "candidate": "MTTVisibleRouteCPhiFinAlpha1DerivativeFill",
        "status": STATUS,
        "inputs": {
            "partial_fill": str(PARTIAL.relative_to(ROOT)).replace("\\", "/"),
            "phifin_alpha1_payload": str(PHIFIN.relative_to(ROOT)).replace("\\", "/"),
            "dotd_transport_derivative_probe": str(DOTD.relative_to(ROOT)).replace("\\", "/"),
            "transport_conjugation_validator_replay": str(TRANSPORT.relative_to(ROOT)).replace("\\", "/"),
            "alpha1_packet_fill_attempt": str(ALPHA_PACKET.relative_to(ROOT)).replace("\\", "/"),
        },
        "output_packets": {
            "fill_attempt": str(fill_path.relative_to(ROOT)).replace("\\", "/"),
            "obstruction": str((OUT / "phifin_alpha1_derivative_obstruction.packet.json").relative_to(ROOT)).replace("\\", "/"),
        },
        "theorem": {
            "name": "VisibleRouteCPhiFinAlpha1DerivativeFillObstructionTheorem",
            "proved": True,
            "statement": (
                "The current repo cannot honestly fill the remaining Lane A alpha1 fields. "
                "The stationary source identity and visible operator source are theorem-derived, and the dotD transport "
                "formula is theorem-derived, but selected Phi_fin alpha1 payload values and same-branch alpha1-driver "
                "normalization are absent. Therefore the validator must remain open without lifted flags."
            ),
        },
        "validation": validation,
        "closure_decision": {
            "stationary_source_identity_closed": True,
            "visible_routec_operator_source_closed": True,
            "phi_fin_alpha1_payload_closed": False,
            "same_branch_alpha1_derivative_closed": False,
            "honest_dotd_validator_replay_closed": False,
            "alpha1_driver_verified": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "what_closes_now": {
            "fill_attempt_executed": True,
            "obstruction_matrix_built": True,
            "validator_failure_localized_to_payload_and_driver": True,
            "superset_strategy_preserved": True,
        },
        "what_remains_open": {
            "selected_PhiFin_alpha1_payload_values": True,
            "same_branch_alpha1_driver_theorem": True,
            "honest_dotD_validator_replay_without_lifted_flags": True,
            "typed_BN_retarded_derivative_alternative": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "superset_strategy": {
            "classification": "LANE_A_FILL_ATTEMPT_WITH_LANE_B_RETARDED_ALTERNATIVE",
            "straight_path": "visible/Route-C source identity plus Phi_fin alpha1 derivative",
            "alternative_path": "typed B_N retarded derivative and transfer normalization",
            "locked_target": "promote alpha1_driver_verified without observed-data selectors",
            "uses_observed_constants": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(DATA, candidate)

    cert = {
        "candidate_path": str(DATA.relative_to(ROOT)).replace("\\", "/"),
        "status": STATUS,
        "theorem_proved": True,
        "fill_attempt_executed": True,
        "validator_ok": validation["ok"],
        "phi_fin_alpha1_payload_closed": False,
        "same_branch_alpha1_derivative_closed": False,
        "honest_dotd_validator_replay_closed": False,
        "alpha1_driver_verified": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        "\n".join(
            [
                "# MTT Visible Route-C PhiFin Alpha1 Derivative Fill v1",
                "",
                f"Status: `{STATUS}`",
                "",
                f"Next artifact: `{NEXT}`",
                "",
                "## Result",
                "",
                "The fill attempt was executed, but it must not be promoted.",
                "Lane A already has theorem-derived stationary `source_identity` and",
                "`visible_routec_operator_source`. The transport derivative formula is also",
                "proved. What is missing is stronger: selected `Phi_fin alpha1` payload",
                "values and a theorem that selects `h_ext` as the physical same-branch",
                "`alpha1` driver.",
                "",
                "## Exact Obstruction",
                "",
                "- `phi_fin_payload` remains open because the selected payload flags are still false.",
                "- `same_branch_alpha1_derivative` remains open because `alpha1_driver_verified` is false.",
                "- `dotd_validator_replay` remains open because the honest validator still fails by that driver flag.",
                "",
                "No observed constants, benchmark matrices, or lifted validator flags are used.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
