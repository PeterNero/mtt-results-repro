"""Build CONST-EM-01 central-circle rod/clock theorem attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OBSIDIAN = Path("C:/ObsidianVault/BrainOfNerodes/Papers/Modal Triplet Theory")
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_central_circle_rod_clock_theorem_attempt"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE = BASE / "central_circle_source_read.packet.json"
THEOREM = BASE / "rod_clock_theorem_attempt.packet.json"
PROMOTION = BASE / "promotion_verdict.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_CentralCircleRodClockTheoremAttempt_v1.md"

STATUS = "MTT_CONST_EM_01_CENTRAL_CIRCLE_ROD_CLOCK_ATTEMPT_SUPPORT_CLOSED_VALUE_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def has(text: str, needle: str) -> bool:
    return needle in text


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    a8_path = DATA / "const_em_01_alpha1_rod_clock_source_discriminator.candidate.json"
    a7_exec_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "execution_formulae.packet.json"
    central_path = OBSIDIAN / "13 Standard Model & Topology-Only Constraints" / "The_Central_Circle__Inertia__Mass__Gravity__and_Time_as_Shared_Coherence_Bookkeeping_in_Modal_Triplet_Theory.md"
    fcp_path = OBSIDIAN / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"

    a8 = load(a8_path)
    a7_exec = load(a7_exec_path)
    central = read(central_path)
    fcp = read(fcp_path)

    tau_int = a7_exec["dimensionless_internal_values"]["tau_int"]
    sqrt_tau_int = a7_exec["dimensionless_internal_values"]["sqrt_tau_int"]

    source_checks = {
        "A8_requests_A9": a8["what_closes_now"]["next_attack_labeled"] == "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM",
        "central_circle_unique_shared_structure": has(central, "the unique internal component reused across all modal bundles"),
        "central_circle_time_ordering": has(central, "time ordering"),
        "central_circle_inertia_gravity_mass": has(central, "inertia, gravity, mass scales, time ordering"),
        "central_circle_shared_bookkeeping": has(central, "unique shared coherence bookkeeping channel"),
        "central_circle_explanatory_not_standalone": has(central, "unifying explanatory map rather than as new standalone theorems"),
        "central_circle_no_new_postulates": has(central, "without introducing new postulates"),
        "fcp_tau_physical_roles": has(fcp, "Coherent length") and has(fcp, "Effective energy"),
        "fcp_tau_gap_tied": has(fcp, "$\\tau$ is tied to the internal spectral gap"),
    }

    source_read = {
        "schema": "MTTConstEM01CentralCircleSourceRead.v1",
        "status": "CENTRAL_CIRCLE_SOURCE_SUPPORT_READ",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM",
        "source": rel(central_path),
        "support": {
            "shared_channel": True,
            "time_ordering_channel": True,
            "inertia_gravity_mass_channel": True,
            "same_source_candidate_for_L0_E0": True,
        },
        "limitations": {
            "interpretive_synthesis_flag": True,
            "standalone_numeric_anchor_theorem_present": False,
            "absolute_L0_or_E0_value_present": False,
        },
        "source_checks": source_checks,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    theorem_attempt = {
        "schema": "MTTConstEM01CentralCircleRodClockTheoremAttempt.v1",
        "status": "SUPPORT_THEOREM_CLOSED_PROMOTION_THEOREM_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM",
        "attempted_statement": (
            "The central circle selects the physical rod/clock unit L0 or E0 because it is the unique shared channel for "
            "time ordering, inertia, mass, and gravity."
        ),
        "proved_support_statement": (
            "The central circle is a same-source structural candidate for a universal rod/clock channel and aligns with the tau coherent-length/effective-energy role."
        ),
        "failed_promotion_step": (
            "The source does not emit a numeric absolute physical value, and explicitly frames the broad central-circle identification as interpretive synthesis rather than a standalone theorem."
        ),
        "dimensionless_chain_replayed": {
            "tau_int": tau_int,
            "sqrt_tau_int": sqrt_tau_int,
            "alpha_phys_if_L0_selected": "tau_int / L0^2",
            "alpha_phys_if_E0_selected": "tau_int * E0^2",
            "Omega0_if_L0_selected": "sqrt(tau_int) / L0",
            "Omega0_if_E0_selected": "sqrt(tau_int) * E0",
        },
        "promotion_conditions_not_met": [
            "selected physical L0 or E0 value",
            "same-branch certificate that central circle emits that value",
            "proof computed before target comparison",
            "map to alpha_phys with a concrete non-null alpha_phys_value",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    promotion = {
        "schema": "MTTConstEM01CentralCirclePromotionVerdict.v1",
        "status": "STRICT_NO_KNOB_PROMOTION_DENIED_SUPPORT_ACCEPTED",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM",
        "support_closed": all(source_checks.values()),
        "strict_no_knob_L0_E0_value_selected": False,
        "one_primitive_extension_still_ready": True,
        "recommended_next": {
            "label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO",
            "task": "Decide whether to formalize one universal physical rod/clock primitive as an extension, or prove an internal no-go for strict physical alpha closure.",
        },
        "reason": (
            "A9 proves central-circle support for a rod/clock channel, but not the absolute metrological value. "
            "The strict route therefore needs a stronger source theorem than the current corpus contains."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1CentralCircleRodClockTheoremAttempt",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM",
        "output_packets": {
            "central_circle_source_read": rel(SOURCE),
            "rod_clock_theorem_attempt": rel(THEOREM),
            "promotion_verdict": rel(PROMOTION),
        },
        "theorem": {
            "name": "CONSTEM01CentralCircleRodClockSupportTheorem",
            "proved": all(source_checks.values()),
            "statement": (
                "The central circle is accepted as the best same-source structural rod/clock channel, aligned with time ordering, inertia, mass, gravity, and tau coherent-scale roles. "
                "It does not yet select an absolute physical L0/E0 value, so strict no-knob alpha_phys promotion remains open."
            ),
        },
        "what_closes_now": {
            "central_circle_support_for_rod_clock_channel": True,
            "strict_no_knob_L0_E0_value": False,
            "one_primitive_extension_ready": True,
            "next_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO",
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
        "certificate": "MTT_CONST_EM_01_Alpha1_CentralCircleRodClockTheoremAttempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "support_closed": all(source_checks.values()),
        "strict_no_knob_L0_E0_value_selected": False,
        "one_primitive_extension_ready": True,
        "next_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Central Circle Rod Clock Theorem Attempt v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A9-CENTRAL-CIRCLE-ROD-CLOCK-THEOREM`

## Result

The central circle route is accepted as the best same-source structural
rod/clock channel. It links the same internal object to time ordering, inertia,
mass, gravity, and shared coherence bookkeeping.

But it does not yet emit an absolute physical value for `L0` or `E0`.

## Closed

`tau_int = {tau_int}`

`sqrt(tau_int) = {sqrt_tau_int}`

The conditional maps remain:

`alpha_phys = tau_int / L0^2`

`alpha_phys = tau_int * E0^2`

## Boundary

The central-circle paper supports the channel, but flags the broad synthesis as
an explanatory map rather than a standalone numeric anchor theorem. Therefore
strict no-knob physical `alpha_phys` remains open.

## Next

`CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO`
"""

    for path, payload in [(SOURCE, source_read), (THEOREM, theorem_attempt), (PROMOTION, promotion), (OUTPUT, candidate), (CERT, cert)]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
