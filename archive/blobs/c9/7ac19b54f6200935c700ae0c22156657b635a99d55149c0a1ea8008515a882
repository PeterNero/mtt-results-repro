"""Build CONST-EM-01 alpha1 frontier closure ledger.

This is the handoff artifact for the main repo.  It freezes what alpha1 has
actually achieved, what remains open, and how to use the result for the next
constant without weakening the no-knob standard.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_frontier_closure_ledger"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
HANDOFF = BASE / "main_repo_handoff.packet.json"
STATUS_PACKET = BASE / "alpha1_status.packet.json"
NEXT_CONSTANT = BASE / "next_constant_template.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_FrontierClosureLedger_v1.md"

STATUS = "MTT_CONST_EM_01_ALPHA1_FRONTIER_CLOSURE_LEDGER_BUILT_HANDOFF_READY"


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

    a10_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo.candidate.json"
    a10_verdict_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "two_path_verdict.packet.json"
    a10_primitive_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo" / "one_universal_primitive.packet.json"
    a7_exec_path = DATA / "const_em_01_alpha1_dimensional_anchor_fill_attempt" / "execution_formulae.packet.json"
    weaksplit_path = DATA / "const_em_01_alpha1_internal_weaksplit_import.candidate.json"
    weaksplit_values_path = DATA / "const_em_01_alpha1_internal_weaksplit_import" / "internal_threshold_promotion.packet.json"
    u1y_path = DATA / "const_em_01_alpha1_u1y_factorized_operator_source.candidate.json"

    a10 = load(a10_path)
    verdict = load(a10_verdict_path)
    primitive = load(a10_primitive_path)
    a7_exec = load(a7_exec_path)
    weaksplit = load(weaksplit_path)
    weaksplit_values = load(weaksplit_values_path)
    u1y = load(u1y_path)

    values = a7_exec["dimensionless_internal_values"]

    import_checks = {
        "A10_strict_current_corpus_nogo": a10["what_closes_now"]["strict_current_corpus_nogo"] is True,
        "A10_one_primitive_extension_ready": a10["what_closes_now"]["one_universal_primitive_extension"] is True,
        "A10_policy_separation": a10["what_closes_now"]["policy_separation"] is True,
        "strict_path_no_go": verdict["path_A_strict_no_knob"]["verdict"] == "NO_GO_FOR_CURRENT_CORPUS",
        "primitive_path_ready": verdict["path_B_one_universal_primitive"]["verdict"] == "READY_AS_EXTENSION",
        "primitive_not_no_knob": primitive["status_relative_to_no_knob"] == "NOT_STRICT_NO_KNOB_CLOSURE",
        "no_observed_selector": all(
            packet.get("observed_data_used_as_selector") is False
            for packet in [a10, verdict, primitive, a7_exec, weaksplit, u1y]
        ),
        "no_target_fit": all(packet.get("target_fitting_used") is False for packet in [a10, verdict, primitive, a7_exec, weaksplit, u1y]),
    }

    alpha_status = {
        "schema": "MTTConstEM01Alpha1Status.v1",
        "status": "ALPHA1_FRONTIER_STATUS_FROZEN",
        "active_label": "CONST-EM-01 / ALPHA1-FRONTIER / A11-CLOSURE-LEDGER",
        "strict_no_knob": {
            "status": "CURRENT_CORPUS_NO_GO_FOR_NUMERICAL_PHYSICAL_ALPHA",
            "reason": "No source-selected absolute L0/E0 or equivalent action unit exists in the current corpus.",
            "physical_alpha_zero_or_MZ_closed": False,
        },
        "one_universal_primitive": {
            "status": "READY_AS_EXTENSION_NOT_NO_KNOB",
            "primitive_options": ["L0", "E0"],
            "formulae": {
                "alpha_phys_from_L0": "tau_int / L0^2",
                "alpha_phys_from_E0": "tau_int * E0^2",
            },
        },
        "internal_values": {
            "tau_int": values["tau_int"],
            "sqrt_tau_int": values["sqrt_tau_int"],
            "inv_sqrt_tau_int": values["inv_sqrt_tau_int"],
            "Omega0_over_sqrt_alpha_phys": values["Omega0_over_sqrt_alpha_phys"],
            "omega_gap_phys_over_sqrt_alpha_phys": values["omega_gap_phys_over_sqrt_alpha_phys"],
            "Lambda_gap_phys_over_sqrt_alpha_phys": values["Lambda_gap_phys_over_sqrt_alpha_phys"],
            "lambda_internal": values["lambda_internal"],
            "p_a_internal": weaksplit_values["promoted_internal_values"]["p_a_internal"],
            "p_Y_internal": weaksplit_values["promoted_internal_values"]["p_Y_internal"],
            "lambda_12_internal": weaksplit_values["promoted_internal_values"]["lambda_12_internal"],
            "Delta_G12_internal": weaksplit_values["promoted_internal_values"]["Delta_G12_internal"],
        },
        "source_scope": {
            "U1Y_factorized_operator_replay": u1y["status"],
            "internal_weak_split_import": weaksplit["status"],
            "dimensional_anchor_policy": a10["status"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    handoff = {
        "schema": "MTTConstEM01MainRepoHandoff.v1",
        "status": "HANDOFF_READY",
        "active_label": "CONST-EM-01 / ALPHA1-FRONTIER / A11-CLOSURE-LEDGER",
        "recommended_main_repo_claim": (
            "Alpha1 physical normalization is closed to a rigorous frontier: strict no-knob numerical alpha is a current-corpus no-go, "
            "while a one-universal-primitive extension is fully specified and guardrailed."
        ),
        "paper_insert_section": {
            "title": "Alpha1 Frontier Closure Ledger",
            "claims_to_add": [
                "The internal U1/Y and weak-split source-side structures are reproducibly closed at internal scope.",
                "The physical normalization problem reduces to one absolute rod/clock/action-unit anchor.",
                "The present corpus does not select that anchor; therefore strict no-knob physical alpha remains open.",
                "A one-universal-primitive extension is ready and must be labeled as such.",
            ],
            "claims_to_forbid": [
                "measured alpha(0) or alpha(M_Z) is derived",
                "internal alpha_int=1 is a physical SI prediction",
                "central-circle support is a numeric metrological theorem",
                "one primitive is no-knob closure",
            ],
        },
        "import_paths": {
            "closure_candidate": rel(OUTPUT),
            "alpha_status": rel(STATUS_PACKET),
            "A10_verdict": rel(a10_verdict_path),
            "A7_execution_formulae": rel(a7_exec_path),
            "internal_weak_split": rel(weaksplit_path),
            "internal_weak_split_values": rel(weaksplit_values_path),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_constant = {
        "schema": "MTTIndividualConstantsNextConstantTemplate.v1",
        "status": "NEXT_CONSTANT_TEMPLATE_READY",
        "active_label": "CONST-NEXT / TEMPLATE / IMPORT_ALPHA1_GUARDRAILS",
        "recommended_sequence": [
            "choose a dimensionless or ratio-like constant first",
            "separate internal replay from physical-unit normalization",
            "build strict no-knob and one-primitive lanes from the start",
            "forbid observed-value selectors in every packet",
            "finish with a closure ledger before moving on",
        ],
        "candidate_next_targets": [
            {
                "target": "weak mixing angle / sin^2 theta_W",
                "reason": "Adjacent to closed internal weak-split and electroweak convention map.",
                "risk": "needs RG/matching scheme before physical comparison.",
            },
            {
                "target": "dimensionless mass ratios",
                "reason": "Avoids the absolute-unit obstruction that blocked strict alpha_phys.",
                "risk": "needs Yukawa/source-emission packets.",
            },
            {
                "target": "alpha_s ratio or gauge splitting",
                "reason": "Can reuse threshold/gauge packet discipline.",
                "risk": "requires SU3/color operator source ownership.",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1FrontierClosureLedger",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-FRONTIER / A11-CLOSURE-LEDGER",
        "output_packets": {
            "alpha1_status": rel(STATUS_PACKET),
            "main_repo_handoff": rel(HANDOFF),
            "next_constant_template": rel(NEXT_CONSTANT),
        },
        "theorem": {
            "name": "CONSTEM01Alpha1FrontierClosureLedgerTheorem",
            "proved": all(import_checks.values()),
            "statement": (
                "The alpha1 branch is closed as a frontier ledger: internal structures and conditional formulae are reproducible; "
                "strict physical alpha is a current-corpus no-go; one-universal-primitive closure is ready as an explicitly non-no-knob extension."
            ),
        },
        "import_checks": import_checks,
        "handoff_ready_for_main_repo": True,
        "next_constant_ready": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_FrontierClosureLedger_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "handoff_ready_for_main_repo": True,
        "strict_no_knob_alpha_phys_closed": False,
        "strict_current_corpus_nogo": True,
        "one_universal_primitive_extension_ready": True,
        "next_constant_template_ready": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 Frontier Closure Ledger v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-FRONTIER / A11-CLOSURE-LEDGER`

## Handoff Claim

Alpha1 physical normalization is closed to a rigorous frontier:

- strict no-knob numerical `alpha_phys` is a current-corpus no-go,
- one-universal-primitive closure is ready as an extension,
- no observed alpha, Newton/Planck, mass, cosmology, TeV, or electroweak value is used as a selector.

## Values To Carry

`tau_int = {values["tau_int"]}`

`sqrt(tau_int) = {values["sqrt_tau_int"]}`

`Omega0/sqrt(alpha_phys) = {values["Omega0_over_sqrt_alpha_phys"]}`

`lambda_12_internal = {weaksplit_values["promoted_internal_values"]["lambda_12_internal"]}`

`Delta_G12_internal = {weaksplit_values["promoted_internal_values"]["Delta_G12_internal"]}`

## Paper Boundary

Do not claim measured `alpha(0)` or `alpha(M_Z)` is derived. The correct claim is
that the physical normalization problem has been reduced to exactly one
absolute rod/clock/action-unit anchor.

## Next Constant Template

Prefer a dimensionless or ratio-like next target, and preserve the two-lane
discipline from the start:

- strict no-knob lane,
- one-universal-primitive extension lane.
"""

    for path, payload in [(STATUS_PACKET, alpha_status), (HANDOFF, handoff), (NEXT_CONSTANT, next_constant), (OUTPUT, candidate), (CERT, cert)]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
