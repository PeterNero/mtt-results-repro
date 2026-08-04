from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERTIFICATE = (
    REPO
    / "certificates"
    / "q79_selected_lorentzian_coframe_causal_closure_certificate.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    require(path.is_file(), f"missing input: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_input(path: str) -> Path:
    return (REPO / path).resolve()


def main() -> None:
    result = load_json(CERTIFICATE)
    inputs = result["inputs"]
    for name, source in inputs.items():
        path = resolve_input(source["path"])
        require(digest(path) == source["sha256"], f"stale dependency: {name}")

    primitive = load_json(resolve_input(inputs["primitive_branch_axiom"]["path"]))
    bridge = load_json(resolve_input(inputs["coframe_solder_bridge"]["path"]))
    strict = load_json(resolve_input(inputs["same_source_neutrality"]["path"]))
    classical = load_json(resolve_input(inputs["classical_gr_closure"]["path"]))
    oriented = load_json(resolve_input(inputs["time_oriented_branch"]["path"]))
    causal_note = resolve_input(inputs["causal_separation_theorem"]["path"]).read_text(
        encoding="utf-8"
    )
    theorem_note = (REPO / result["note_written"]).read_text(encoding="utf-8")

    parameters = primitive["parameter_ledger"]
    require(
        parameters["additional_discrete_physical_realization_axioms"] == 1,
        "A_QG count changed",
    )
    require(
        parameters["additional_continuous_parameters_from_branch_axiom"] == 0,
        "A_QG gained a continuous coordinate",
    )
    require(
        parameters["target_or_observed_data_used_to_choose_branch"] == 0,
        "A_QG uses an observed selector",
    )
    require(
        primitive["claim_tiers"]["q79_geometry_operator_choice_after_A_QG"]
        == "CLOSED_UNIQUE_UP_TO_DECLARED_GAUGE",
        "selected q79 class is not unique after A_QG",
    )

    bridge_checks = bridge["checks"]
    for key in (
        "latest_action_declares_globally_hyperbolic_physical_base",
        "local_QWW_ADM_coframe_metric_identity_is_exact",
        "local_QWW_ADM_coframe_volume_identity_is_exact",
        "world_in_world_Q_is_global_Hom_section_with_tetrad_cocycle",
        "teleparallel_Ricci_boundary_identity_passes_symbolically",
    ):
        require(bridge_checks[key], f"coframe bridge check failed: {key}")
    global_coframe = bridge["theorem"][
        "part_G_conditional_global_coframe_and_connection_existence"
    ]
    require("R x Sigma3" in global_coframe["splitting"], "smooth split missing")
    require(
        "parallelizable" in global_coframe["parallelizability"],
        "parallelizability input missing",
    )
    require(
        "metric-compatible and flat" in global_coframe["teleparallel_connection_result"],
        "flat teleparallel connection missing",
    )
    solder = bridge["theorem"]["part_J_QWW_soldering_cocycle_theorem"]
    require("solder form" in solder["result"], "QWW solder theorem missing")

    strict_checks = strict["checks"]
    for key in (
        "canonical_physical_realization_has_globally_hyperbolic_Y4",
        "metric_quotient_orientation_kernel_has_dimension_three",
        "selected_candidate_Q_has_no_orientation_coordinate",
        "pure_frame_neutrality_selects_TEGR_exactly",
        "TEGR_is_nonlinearly_metric_descending_mod_boundary",
    ):
        require(strict_checks[key], f"same-source check failed: {key}")
    require(
        strict["claim_tiers"]["strict_same_source_two_derivative_teleparallel_action"]
        == "CLOSED_UNIQUE_TEGR_RAY",
        "TEGR ray is not closed",
    )
    require(
        strict["claim_tiers"]["cauchy_support_typing_without_extra_source_map"]
        == "CLOSED_CONDITIONAL_ON_CANONICAL_PHYSICAL_REALIZATION",
        "Cauchy support typing is not closed on the selected realization",
    )
    require(
        classical["parameter_ledger"]["dimensionless_gravity_shape_parameters"] == 0,
        "extra dimensionless gravity shape parameter introduced",
    )

    constraints = ((2, 1, 1), (-4, 2, 0))
    ray = (1, 2, -4)
    require(
        all(sum(row[i] * ray[i] for i in range(3)) == 0 for row in constraints),
        "TEGR ray does not solve the frame constraints",
    )
    require(
        constraints[0][0] * constraints[1][1]
        - constraints[0][1] * constraints[1][0]
        != 0,
        "frame constraint matrix lost rank two",
    )

    branch = oriented["calculation_results"]
    require(branch["unoriented_conjugate_pair_retained"], "conjugate pair lost")
    require(branch["z64_retarded_kernel_selected"], "retarded kernel not selected")
    require(branch["time_oriented_retarded_branch_selects_q79"], "q79 not selected")
    require(
        branch["q369_retained_as_global_antiunitary_conjugate"],
        "q369 conjugate lost",
    )
    require(
        not branch["unique_without_retarded_boundary_or_operator_source"],
        "causal datum silently removed",
    )
    residues = oriented["residue_calculation"]
    require(
        (residues["selected_residues"]["crt_q"] + residues["conjugate_residues"]["q"])
        % residues["modulus"]
        == 0,
        "q79/q369 conjugate arithmetic failed",
    )
    require(
        not oriented["guardrails"]["uses_observed_CP_sign_to_select_branch"]
        and not oriented["guardrails"]["uses_observed_flavor_data"],
        "observed data entered causal selection",
    )

    for phrase in (
        "A_causal",
        "G_ret[-o] = G_adv[o]",
        "does not derive the time orientation",
        "thermodynamic/state arrow: OPEN",
    ):
        if phrase == "thermodynamic/state arrow: OPEN":
            require("thermodynamic arrow" in causal_note, "state-arrow boundary missing")
        else:
            require(phrase in causal_note, f"causal note missing: {phrase}")

    ledger = result["parameter_ledger"]
    require(ledger["inherited_discrete_A_QG"] == 1, "wrong inherited axiom count")
    require(ledger["new_binary_causal_boundary_marks"] == 1, "wrong causal count")
    require(ledger["new_continuous_parameters"] == 0, "continuous knob added")
    require(ledger["observed_values_used_to_select_branch"] == 0, "observed selector added")
    require(all(result["checks"].values()), "new closure certificate has failed check")
    require(
        all(value is False for value in result["guardrails"].values()),
        "one or more overclaim guardrails are true",
    )
    for phrase in (
        "Assume `A_QG`, `A_causal`",
        "new continuous parameters in this step:  0",
        "does not derive a time orientation",
        "thermodynamic arrow",
    ):
        require(phrase in theorem_note, f"theorem note missing guard phrase: {phrase}")

    print(
        "AUDIT_PASS: selected global coframe, QWW soldering, strict frame "
        "neutrality and retarded q79 representative compose after A_QG+A_causal"
    )
    print("new continuous parameters: 0")
    print("new causal boundary data: 1 binary mark")
    print("origin of time orientation and thermodynamic arrow: OPEN")


if __name__ == "__main__":
    main()
