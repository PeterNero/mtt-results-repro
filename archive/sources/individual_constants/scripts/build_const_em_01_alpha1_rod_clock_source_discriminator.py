"""Build CONST-EM-01 rod/clock source discriminator.

After the A7 fill attempt, the remaining object is a source-selected physical
length L0 or energy E0.  This artifact ranks current candidate sources and
separates strict no-knob closure from a possible one-universal-primitive
extension.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
OBSIDIAN = Path("C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory")

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_rod_clock_source_discriminator"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTES = BASE / "rod_clock_route_table.packet.json"
DECISION = BASE / "decision.packet.json"
NEXT = BASE / "next_attack.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_RodClockSourceDiscriminator_v1.md"

STATUS = "MTT_CONST_EM_01_ROD_CLOCK_SOURCE_DISCRIMINATOR_BUILT_STRICT_SOURCE_OPEN"


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


def contains(path: Path, needle: str) -> bool:
    return needle in path.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    fill_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt.candidate.json"
    one_anchor_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "one_anchor_metrology.packet.json"
    execution_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "execution_formulae.packet.json"
    obstruction_path = NONSM / "certificates" / "dimensionful_constant_obstruction_certificate.json"
    fcp_path = OBSIDIAN / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"
    central_circle_path = OBSIDIAN / "13 Standard Model & Topology-Only Constraints" / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
    modal_unit_path = PROTO / "proof_corpus" / "Selected_Modal_Gap_to_Physical_Unit_Theorem_v1.md"
    metrology_path = PROTO / "proof_corpus" / "Dimensional_Metrology_NoGo_and_Relative_Closure_Theorem_v1.md"

    fill = load(fill_path)
    one_anchor = load(one_anchor_path)
    execution = load(execution_path)
    obstruction = load(obstruction_path)

    tau_int = execution["dimensionless_internal_values"]["tau_int"]
    sqrt_tau_int = execution["dimensionless_internal_values"]["sqrt_tau_int"]
    inv_sqrt_tau_int = execution["dimensionless_internal_values"]["inv_sqrt_tau_int"]

    source_checks = {
        "A7_fill_attempt_available": fill["what_closes_now"]["one_anchor_extension_ready"] is True,
        "one_anchor_guardrail_present": "source-selected before target comparison" in one_anchor["guardrail"],
        "dimensionful_obstruction_certified": obstruction["status"] == "OBSTRUCTION_CERTIFIED",
        "fcp_tau_selected_by_leakage_tolerance": contains(fcp_path, "The finite damping time $\\tau$ is selected by a leakage tolerance"),
        "fcp_tau_tied_to_gap": contains(fcp_path, "$\\tau$ is tied to the internal spectral gap"),
        "fcp_coherent_length_energy_roles": contains(fcp_path, "Coherent length") and contains(fcp_path, "Effective energy"),
        "central_circle_time_bookkeeping_present": contains(central_circle_path, "time ordering") and contains(central_circle_path, "shared coherence bookkeeping"),
        "central_circle_marks_identification_interpretive": contains(central_circle_path, "unifying explanatory map rather than as new standalone theorems"),
        "modal_unit_theorem_requires_physical_unit": contains(modal_unit_path, "If a selected physical inverse-length unit"),
        "metrology_no_go_requires_one_primitive": contains(metrology_path, "exactly one metrological primitive"),
    }

    route_table = {
        "schema": "MTTConstEM01RodClockRouteTable.v1",
        "status": "ROUTES_RANKED_STRICT_SOURCE_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A8-ROD-CLOCK-SOURCE-DISCRIMINATOR",
        "source_checks": source_checks,
        "routes": {
            "finite_coherent_projection_tau": {
                "classification": "RELATIVE_ROLE_CLOSED_ABSOLUTE_VALUE_OPEN",
                "strict_no_knob_accept_now": False,
                "closed": [
                    "tau role as damping/coherence scale",
                    "tau tied to selected internal spectral gap",
                    "L0/E0 formulas after one anchor",
                ],
                "blocker": "tau_int is dimensionless/internal until a physical unit converts it to L^2 or E^-2.",
            },
            "central_circle_time_bookkeeping": {
                "classification": "PROMISING_SHARED_SOURCE_NOT_NUMERIC_ANCHOR",
                "strict_no_knob_accept_now": False,
                "closed": [
                    "central circle is shared coherence/time/inertia bookkeeping structure",
                    "candidate same-source channel for a future rod/clock theorem",
                ],
                "blocker": "current source labels the central-circle synthesis as interpretive/explanatory, not a standalone physical scale theorem.",
            },
            "m_theory_modal_gap_planck_anchor": {
                "classification": "BEST_STRUCTURAL_ROUTE_VALUE_OPEN",
                "strict_no_knob_accept_now": False,
                "closed": [
                    "maps physical modal-gap unit to ell_p/kappa_11",
                    "same structural route selected by A6/A7",
                ],
                "blocker": "no same-branch physical omega_gap/L0/E0 value is emitted.",
            },
            "proper_time_sigma_model_flow": {
                "classification": "SCALE_VARIABLE_NOT_ABSOLUTE_ANCHOR",
                "strict_no_knob_accept_now": False,
                "closed": [
                    "proper-time/heat-kernel scale variable aligns with tau role",
                ],
                "blocker": "a scale variable is not an absolute metrological value.",
            },
            "declared_universal_primitive": {
                "classification": "ONE_PRIMITIVE_EXTENSION_CREDIBLE_NOT_NO_KNOB",
                "strict_no_knob_accept_now": False,
                "closed": [
                    "one L0 or E0 would propagate all physical normalization formulae",
                    "would avoid multiple fitted constants if declared once before target comparison",
                ],
                "blocker": "this changes the standard from zero-parameter no-knob to one universal primitive.",
            },
            "observed_constant_backsolve": {
                "classification": "FORBIDDEN",
                "strict_no_knob_accept_now": False,
                "blocker": "uses alpha, Newton/Planck, masses, cosmology, or TeV data to select the value being predicted.",
            },
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    decision = {
        "schema": "MTTConstEM01RodClockDecision.v1",
        "status": "STRICT_NO_KNOB_L0_E0_NOT_FOUND_ONE_PRIMITIVE_READY",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A8-ROD-CLOCK-SOURCE-DISCRIMINATOR",
        "strict_no_knob_result": {
            "L0_or_E0_source_selected_now": False,
            "reason": "Current corpus closes the internal/relative tau chain and the structural physical roles, but not an absolute physical value.",
            "best_current_no_knob_route": "m_theory_modal_gap_planck_anchor plus central-circle rod/clock theorem request",
        },
        "one_universal_primitive_result": {
            "extension_ready": True,
            "primitive": "L0 or E0",
            "credibility_condition": "Declared once before target comparison, not adjusted per sector or per constant.",
            "formulae": {
                "alpha_phys_from_L0": "tau_int / L0^2",
                "alpha_phys_from_E0": "tau_int * E0^2",
                "Omega0_from_L0": "sqrt(tau_int) / L0",
                "Omega0_from_E0": "sqrt(tau_int) * E0",
            },
            "numeric_internal_coefficients": {
                "tau_int": tau_int,
                "sqrt_tau_int": sqrt_tau_int,
                "inv_sqrt_tau_int": inv_sqrt_tau_int,
                "tau_int_check": math.log(448) / 15,
            },
        },
        "source_promotion_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_attack = {
        "schema": "MTTConstEM01RodClockNextAttack.v1",
        "status": "NEXT_ATTACK_CENTRAL_CIRCLE_ROD_CLOCK_THEOREM",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM",
        "task": "Attempt to promote the central circle from shared bookkeeping role to a selected physical rod/clock source theorem.",
        "must_emit": [
            "selected physical L0 or E0 value, or a proof no such value can exist internally",
            "same-branch certificate tying it to q79/Z448/rho_UV/tau_int",
            "proof computed before comparison to alpha, Newton/Planck, masses, cosmology, or TeV data",
            "map to alpha_phys using A7 formulae",
        ],
        "fallback_if_no_promotion": "Record one-universal-primitive alpha_phys as a clearly declared extension, not no-knob closure.",
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1RodClockSourceDiscriminator",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A8-ROD-CLOCK-SOURCE-DISCRIMINATOR",
        "output_packets": {
            "rod_clock_route_table": rel(ROUTES),
            "decision": rel(DECISION),
            "next_attack": rel(NEXT),
        },
        "theorem": {
            "name": "CONSTEM01RodClockSourceDiscriminatorTheorem",
            "proved": all(source_checks.values()),
            "statement": (
                "The current corpus supplies a selected internal tau/coherent-scale chain and a shared central-circle physical role, "
                "but no strict same-branch absolute L0/E0 value. The strongest next no-knob attack is a central-circle rod/clock theorem; "
                "the strongest nonzero-parameter extension is one universal primitive declared before data comparison."
            ),
        },
        "what_closes_now": {
            "candidate_source_table": True,
            "strict_no_knob_L0_E0_found": False,
            "one_universal_primitive_extension_ready": True,
            "next_attack_labeled": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM",
        },
        "what_remains_open": {
            "source_selected_L0_or_E0": True,
            "alpha_phys_value": True,
            "K_phys_value": True,
            "physical_alpha_zero_or_MZ": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_RodClockSourceDiscriminator_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_no_knob_L0_E0_found": False,
        "one_universal_primitive_extension_ready": True,
        "next_attack": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Rod Clock Source Discriminator v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A8-ROD-CLOCK-SOURCE-DISCRIMINATOR`

## Result

The current corpus does not yet emit a strict no-knob physical `L0` or `E0`.

What is closed:

- the internal selected tau chain,
- the physical role of `sqrt(tau)` as coherent length and `tau^-1/2` as effective energy,
- the one-anchor propagation formulae,
- the M-theory/modal-gap structural route,
- the central-circle shared bookkeeping route as the best candidate source channel.

What is not closed:

- a same-branch absolute physical value for `L0` or `E0`.

## One-Primitive Extension

If a single universal primitive is allowed, the whole chain is ready:

`alpha_phys = tau_int / L0^2`

or

`alpha_phys = tau_int * E0^2`

with:

`tau_int = {tau_int}`

`sqrt(tau_int) = {sqrt_tau_int}`

This is credible only if the primitive is declared once before target comparison.
It is not strict no-knob closure.

## Next

Next label:

`CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM`
"""

    for path, payload in [(ROUTES, route_table), (DECISION, decision), (NEXT, next_attack), (OUTPUT, candidate), (CERT, cert)]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
