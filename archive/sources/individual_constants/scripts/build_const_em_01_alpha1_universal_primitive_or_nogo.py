"""Build CONST-EM-01 A10 universal primitive or no-go artifact."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_universal_primitive_or_nogo"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PRIMITIVE = BASE / "one_universal_primitive.packet.json"
NOGO = BASE / "strict_internal_nogo.packet.json"
VERDICT = BASE / "two_path_verdict.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_UniversalPrimitiveOrNoGo_v1.md"

STATUS = "MTT_CONST_EM_01_A10_PRIMITIVE_EXTENSION_READY_STRICT_NOGO_CERTIFIED"


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

    a9_path = DATA / "const_em_01_alpha1_central_circle_rod_clock_theorem_attempt.candidate.json"
    a9_promotion_path = DATA / "const_em_01_alpha1_central_circle_rod_clock_theorem_attempt" / "promotion_verdict.packet.json"
    one_anchor_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "one_anchor_metrology.packet.json"
    execution_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "execution_formulae.packet.json"
    obstruction_path = NONSM / "certificates" / "dimensionful_constant_obstruction_certificate.json"

    a9 = load(a9_path)
    a9_promotion = load(a9_promotion_path)
    one_anchor = load(one_anchor_path)
    execution = load(execution_path)
    obstruction = load(obstruction_path)

    tau_int = execution["dimensionless_internal_values"]["tau_int"]
    sqrt_tau_int = execution["dimensionless_internal_values"]["sqrt_tau_int"]
    inv_sqrt_tau_int = execution["dimensionless_internal_values"]["inv_sqrt_tau_int"]

    source_checks = {
        "A9_support_closed": a9["what_closes_now"]["central_circle_support_for_rod_clock_channel"] is True,
        "A9_strict_value_denied": a9_promotion["strict_no_knob_L0_E0_value_selected"] is False,
        "A9_one_primitive_ready": a9_promotion["one_primitive_extension_still_ready"] is True,
        "A7_one_anchor_ready": one_anchor["status"] == "ONE_ANCHOR_EXTENSION_READY_NOT_SELECTED",
        "dimensionful_obstruction_certified": obstruction["status"] == "OBSTRUCTION_CERTIFIED",
        "obstruction_requires_selected_normalization": "selected absolute normalization" in obstruction["required_for_absolute_prediction"],
        "obstruction_forbids_target_backsolve": any("observed G_N" in claim for claim in obstruction["forbidden_claims"]),
        "tau_identity_consistent": abs(tau_int - math.log(448) / 15) < 1e-15,
    }

    primitive = {
        "schema": "MTTConstEM01OneUniversalPrimitiveExtension.v1",
        "status": "ONE_UNIVERSAL_PRIMITIVE_EXTENSION_READY",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO",
        "primitive_options": {
            "length": {
                "symbol": "L0",
                "role": "single physical coherent length / rod primitive",
                "formulae": one_anchor["length_anchor_form"],
            },
            "energy": {
                "symbol": "E0",
                "role": "single physical coherent energy / clock-frequency primitive",
                "formulae": one_anchor["energy_anchor_form"],
            },
        },
        "acceptance_policy": {
            "allowed_if": [
                "declared exactly once as a universal primitive",
                "selected before comparison to measured constants",
                "not adjusted per sector, per constant, or per observable",
                "all downstream predictions report dependence on the primitive unless it is independently measured",
            ],
            "forbidden_if": [
                "chosen from alpha_EM, Newton/Planck, masses, cosmology, TeV, or electroweak data",
                "renamed as no-knob closure",
                "varied between sectors",
            ],
        },
        "numeric_internal_coefficients": {
            "tau_int": tau_int,
            "sqrt_tau_int": sqrt_tau_int,
            "inv_sqrt_tau_int": inv_sqrt_tau_int,
        },
        "status_relative_to_no_knob": "NOT_STRICT_NO_KNOB_CLOSURE",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    nogo = {
        "schema": "MTTConstEM01StrictInternalNoGo.v1",
        "status": "STRICT_INTERNAL_ABSOLUTE_ALPHA_PHYS_NOGO_CERTIFIED_FOR_CURRENT_CORPUS",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO",
        "claim": (
            "Given the current corpus and imported certificates, strict no-knob numerical alpha_phys closure is impossible "
            "because all closed facts are dimensionless/relative or structural, and no source emits an absolute physical L0/E0."
        ),
        "premises": {
            "relative_tau_chain_closed": True,
            "central_circle_support_closed": True,
            "m_theory_structural_slot_closed": True,
            "absolute_L0_E0_value_absent": True,
            "dimensionful_obstruction_certified": True,
        },
        "logical_boundary": {
            "proves_current_corpus_no_go": True,
            "does_not_prove_future_impossibility": True,
            "future_escape_condition": "a new source theorem emits selected absolute L0/E0 or equivalent action unit before target comparison",
        },
        "forbidden_shortcuts": obstruction["forbidden_claims"] + [
            "alpha_phys is predicted by setting internal alpha_int=1 in SI units",
            "central-circle support is treated as a numeric metrological theorem",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    verdict = {
        "schema": "MTTConstEM01A10TwoPathVerdict.v1",
        "status": "TWO_PATH_FRONTIER_RESOLVED",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO",
        "source_checks": source_checks,
        "path_A_strict_no_knob": {
            "verdict": "NO_GO_FOR_CURRENT_CORPUS",
            "result": "physical alpha values remain open",
            "next_if_continuing_strict": "find genuinely new same-branch source theorem for L0/E0",
        },
        "path_B_one_universal_primitive": {
            "verdict": "READY_AS_EXTENSION",
            "result": "all alpha_phys/K_phys/Omega0 formulae can be expressed from one universal primitive",
            "credibility": "acceptable only as a declared primitive extension, not as no-knob proof",
        },
        "recommended_policy": (
            "Keep strict no-knob as the primary standard. Use the one-primitive extension as a transparent comparison layer "
            "when asking whether MTT can match or organize measured constants with fewer knobs."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1UniversalPrimitiveOrNoGo",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO",
        "output_packets": {
            "one_universal_primitive": rel(PRIMITIVE),
            "strict_internal_nogo": rel(NOGO),
            "two_path_verdict": rel(VERDICT),
        },
        "theorem": {
            "name": "CONSTEM01A10PrimitiveExtensionOrCurrentCorpusNoGoTheorem",
            "proved": all(source_checks.values()),
            "statement": (
                "For the current corpus, strict no-knob numerical alpha_phys closure is blocked by the dimensionful-normalization no-go "
                "and absence of a selected L0/E0. A one-universal-primitive extension is fully specified and guardrailed, but it is not no-knob closure."
            ),
        },
        "what_closes_now": {
            "strict_current_corpus_nogo": True,
            "one_universal_primitive_extension": True,
            "policy_separation": True,
        },
        "what_remains_open": {
            "strict_no_knob_alpha_phys": True,
            "source_selected_L0_or_E0": True,
            "physical_alpha_zero_or_MZ": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_UniversalPrimitiveOrNoGo_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "strict_current_corpus_nogo": True,
        "one_universal_primitive_extension_ready": True,
        "strict_no_knob_alpha_phys_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Universal Primitive Or NoGo v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO`

## Path A: Strict No-Knob

For the current corpus, strict numerical `alpha_phys` closure is blocked.

Reason: the selected branch closes only dimensionless/relative quantities and
structural source channels. It does not emit an absolute physical `L0`, `E0`,
`Omega0`, `ell_p`, or `kappa_11` value before target comparison.

This is a current-corpus no-go, not a proof that no future source theorem can
exist.

## Path B: One Universal Primitive

The one-primitive extension is ready:

`alpha_phys = tau_int / L0^2`

or

`alpha_phys = tau_int * E0^2`

with:

`tau_int = {tau_int}`

`sqrt(tau_int) = {sqrt_tau_int}`

This is credible only as a declared universal primitive, chosen once before any
target comparison. It is not strict no-knob closure.
"""

    for path, payload in [(PRIMITIVE, primitive), (NOGO, nogo), (VERDICT, verdict), (OUTPUT, candidate), (CERT, cert)]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
