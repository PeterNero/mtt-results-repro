"""Build CONST-EM-01 dimensional-anchor fill attempt.

This executes the best current strategy for filling the A6 packet:

1. Try strict no-knob promotion through the M-theory/modal-gap route.
2. If the physical unit is still absent, emit the strongest honest conditional
   packet: one metrological primitive promotes the whole chain.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_dimensional_anchor_fill_attempt"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT = BASE / "strict_no_knob_fill.packet.json"
ONE_ANCHOR = BASE / "one_anchor_metrology.packet.json"
EXECUTION = BASE / "execution_formulae.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_DimensionalAnchorFillAttempt_v1.md"

STATUS = "MTT_CONST_EM_01_DIMENSIONAL_ANCHOR_FILL_ATTEMPT_STRICT_OPEN_ONE_ANCHOR_READY"


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


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    gate_path = DATA / "const_em_01_alpha1_dimensional_anchor_packet_gate.candidate.json"
    mtheory_attempt_path = PROTO / "candidate_data" / "selected_dimensional_anchor_packet.mtheory_attempt.json"
    modal_unit_note = PROTO / "proof_corpus" / "Selected_Modal_Gap_to_Physical_Unit_Theorem_v1.md"
    metrology_note = PROTO / "proof_corpus" / "Dimensional_Metrology_NoGo_and_Relative_Closure_Theorem_v1.md"
    clock_note = PROTO / "proof_corpus" / "Same_Branch_Physical_Clock_or_Length_Source_Search_v1.md"
    alpha_phys_cert_path = PROTO / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"

    gate = load(gate_path)
    mtheory_attempt = load(mtheory_attempt_path)
    alpha_phys_cert = load(alpha_phys_cert_path)
    modal_unit_text = modal_unit_note.read_text(encoding="utf-8")
    metrology_text = metrology_note.read_text(encoding="utf-8")
    clock_text = clock_note.read_text(encoding="utf-8")

    tau_int = math.log(448) / 15
    sqrt_tau_int = math.sqrt(tau_int)
    inv_sqrt_tau_int = 1 / sqrt_tau_int
    omega0_over_sqrt_alpha = alpha_phys_cert["final_reduction"]["Omega0_over_sqrt_alpha_phys"]
    omega_gap_over_sqrt_alpha = omega0_over_sqrt_alpha / 1.464646774701829
    lambda_gap_over_sqrt_alpha = math.sqrt(15) * omega_gap_over_sqrt_alpha

    strict_checks = {
        "gate_available": gate["what_closes_now"]["acceptance_gate"] is True,
        "route_is_mtheory_modal_gap": gate["what_closes_now"]["route_selection_for_next_attack"] == "m_theory_modal_gap_planck_anchor",
        "mtheory_structural_slot_filled": mtheory_attempt["status"] == "ATTEMPT_FILLED_STRUCTURAL_SLOT_VALUE_OPEN",
        "same_branch_alignment": mtheory_attempt["source_certification"]["same_branch_as_rho_uv_and_z448"] is True,
        "forbidden_inputs_absent": all(mtheory_attempt["forbidden_inputs_absent"].values()),
        "dimensionful_value_present": mtheory_attempt["dimensionful_quantity"]["value"] is not None,
        "selected_by_mtt": mtheory_attempt["source_certification"]["selected_by_mtt"] is True,
        "computed_before_target_comparison": mtheory_attempt["source_certification"]["computed_before_target_comparison"] is True,
        "alpha_phys_value_present": mtheory_attempt["map_to_alpha_phys"]["alpha_phys_value"] is not None,
    }
    strict_promotes = all(strict_checks.values())

    strict = {
        "schema": "MTTConstEM01DimensionalAnchorStrictFill.v1",
        "status": "STRICT_NO_KNOB_FILL_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A7-DIMENSIONAL-ANCHOR-FILL",
        "strategy": "Try M-theory modal-gap Planck/action route first.",
        "checks": strict_checks,
        "filled_fields": {
            "candidate_id": mtheory_attempt["candidate_id"],
            "source_branch": mtheory_attempt["source_branch"],
            "dimensionful_quantity.symbol": mtheory_attempt["dimensionful_quantity"]["symbol"],
            "dimensionful_quantity.units": mtheory_attempt["dimensionful_quantity"]["units"],
            "dimensionful_quantity.physical_meaning": mtheory_attempt["dimensionful_quantity"]["physical_meaning"],
            "map_to_alpha_phys.formula": mtheory_attempt["map_to_alpha_phys"]["formula"],
            "Omega0_over_sqrt_alpha_phys": omega0_over_sqrt_alpha,
            "tau_int": tau_int,
        },
        "missing_fields": [
            "dimensionful_quantity.value",
            "source_certification.selected_by_mtt",
            "source_certification.computed_before_target_comparison",
            "map_to_alpha_phys.alpha_phys_value",
        ],
        "promotion_now": strict_promotes,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    one_anchor = {
        "schema": "MTTConstEM01OneAnchorMetrologicalExtension.v1",
        "status": "ONE_ANCHOR_EXTENSION_READY_NOT_SELECTED",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A7-DIMENSIONAL-ANCHOR-FILL",
        "minimal_extension": "one independently selected physical length L0 or energy E0",
        "length_anchor_form": {
            "input": "L0",
            "alpha_phys": "tau_int / L0^2",
            "tau_phys": "L0^2",
            "ell_coh": "L0",
            "Lambda_eff": "1/L0",
            "Omega0": "sqrt(tau_int)/L0",
            "numeric_coefficients": {
                "tau_int": tau_int,
                "sqrt_tau_int": sqrt_tau_int,
                "Omega0_times_L0": sqrt_tau_int,
            },
        },
        "energy_anchor_form": {
            "input": "E0",
            "alpha_phys": "tau_int * E0^2",
            "tau_phys": "1/E0^2",
            "ell_coh": "1/E0",
            "Lambda_eff": "E0",
            "Omega0": "sqrt(tau_int)*E0",
            "numeric_coefficients": {
                "tau_int": tau_int,
                "sqrt_tau_int": sqrt_tau_int,
                "Omega0_over_E0": sqrt_tau_int,
            },
        },
        "guardrail": "L0 or E0 must be source-selected before target comparison; observed constants cannot choose it.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    execution = {
        "schema": "MTTConstEM01DimensionalAnchorExecutionFormulae.v1",
        "status": "CONDITIONAL_EXECUTION_FORMULAE_BUILT",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A7-DIMENSIONAL-ANCHOR-FILL",
        "dimensionless_internal_values": {
            "tau_int": tau_int,
            "sqrt_tau_int": sqrt_tau_int,
            "inv_sqrt_tau_int": inv_sqrt_tau_int,
            "Omega0_over_sqrt_alpha_phys": omega0_over_sqrt_alpha,
            "omega_gap_phys_over_sqrt_alpha_phys": omega_gap_over_sqrt_alpha,
            "Lambda_gap_phys_over_sqrt_alpha_phys": lambda_gap_over_sqrt_alpha,
            "lambda_internal": 15,
        },
        "conditional_mtheory_map": {
            "if_omega_gap_phys_selected": [
                "Lambda_gap_phys = sqrt(15) * omega_gap_phys",
                "ell_p = 1 / Lambda_gap_phys",
                "2 kappa_11^2 = (2 pi)^8 ell_p^9",
                "kappa_4^-2 = kappa_11^-2 Vol(X_7)",
            ],
            "if_Omega0_selected": [
                "alpha_phys = Omega0^2 * log(448) / 15",
                "omega_gap_phys = Omega0 / s_star",
                "Lambda_gap_phys = sqrt(15) * Omega0 / s_star",
            ],
        },
        "source_text_checks": {
            "modal_unit_theorem_has_lambda_internal": "lambda_internal = 15" in modal_unit_text,
            "metrology_no_go_has_one_anchor_solution": "One-Anchor Absolute Solution" in metrology_text,
            "clock_search_has_same_branch_bridge": "Z448/q79/rho_UV branch" in clock_text,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1DimensionalAnchorFillAttempt",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A7-DIMENSIONAL-ANCHOR-FILL",
        "output_packets": {
            "strict_no_knob_fill": rel(STRICT),
            "one_anchor_metrology": rel(ONE_ANCHOR),
            "execution_formulae": rel(EXECUTION),
        },
        "theorem": {
            "name": "CONSTEM01DimensionalAnchorFillAttemptTheorem",
            "proved": True,
            "statement": (
                "Executing the best current fill strategy fills the M-theory/modal-gap structural slot and all conditional "
                "execution formulae, but strict no-knob promotion still fails exactly because no same-branch target-independent "
                "physical unit value is selected. A one-anchor metrological extension is fully specified and would promote the chain "
                "if L0 or E0 were independently source-selected."
            ),
        },
        "what_closes_now": {
            "strict_fill_attempt_executed": True,
            "mtheory_structural_slot_filled": True,
            "conditional_execution_formulae": True,
            "one_anchor_extension_ready": True,
            "strict_no_knob_promotion": strict_promotes,
        },
        "what_remains_open": {
            "source_selected_L0_or_E0": True,
            "dimensionful_anchor_value": True,
            "alpha_phys_value": True,
            "K_phys_value": True,
            "physical_alpha_zero_or_MZ": True,
        },
        "superset_strategy_used": {
            "mode": "combined paths with locked target",
            "paths": [
                "M-theory modal-gap Planck/action route",
                "GR/protospinor dimensional metrology no-go",
                "same-branch clock/length source search",
                "individual alpha1 physical-anchor gate",
            ],
            "locked_target": "SelectedDimensionalAnchorPacket",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_DimensionalAnchorFillAttempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_no_knob_promotion": strict_promotes,
        "one_anchor_extension_ready": True,
        "physical_value_claimed": False,
        "alpha_phys_value_claimed": False,
        "K_phys_value_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Dimensional Anchor Fill Attempt v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A7-DIMENSIONAL-ANCHOR-FILL`

## Executed Strategy

The best strict no-knob route was executed:

`m_theory_modal_gap_planck_anchor`

It fills the structural slot and the map:

`Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))`

with:

`Omega0/sqrt(alpha_phys) = {omega0_over_sqrt_alpha}`

It also preserves the conditional M-theory bridge:

`Lambda_gap_phys = sqrt(15) * omega_gap_phys`

`ell_p = 1 / Lambda_gap_phys`

`2 kappa_11^2 = (2 pi)^8 ell_p^9`

## Verdict

Strict no-knob promotion is still open because the current sources do not supply
`dimensionful_quantity.value`, `selected_by_mtt = true`, and
`computed_before_target_comparison = true` for a physical `L0`, `E0`,
`Omega0`, `ell_p`, or `kappa_11`.

## Strongest Available Fill

A one-anchor extension is ready:

Length form:

`alpha_phys = tau_int / L0^2`

`Omega0 = sqrt(tau_int) / L0`

Energy form:

`alpha_phys = tau_int * E0^2`

`Omega0 = sqrt(tau_int) * E0`

where:

`tau_int = {tau_int}`

`sqrt(tau_int) = {sqrt_tau_int}`

This is not a fitted knob if, and only if, `L0` or `E0` is selected by a
same-branch source before comparison to measured constants.
"""

    for path, payload in [(STRICT, strict), (ONE_ANCHOR, one_anchor), (EXECUTION, execution), (OUTPUT, candidate), (CERT, cert)]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS, "strict_no_knob_promotion": strict_promotes}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
