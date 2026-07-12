"""Build the initial individual-constants frontier ledger."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY = TEXPAPERS / "mtt-sm-parity-closure"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "constant_frontier_ledger"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TARGETS = BASE / "individual_constant_targets.packet.json"
FIRST = BASE / "first_attack_alpha1.packet.json"
UNIV = BASE / "universal_parameter_policy_import.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_IndividualConstants_FrontierLedger_v1.md"

STATUS = "MTT_INDIVIDUAL_CONSTANTS_FRONTIER_LEDGER_BUILT_ALPHA1_FIRST"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def exists(path: Path) -> bool:
    return path.exists()


def load_if_exists(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    universal_policy = load_if_exists(SM_PARITY / "candidate_data" / "universal_source_parameter_policy.candidate.json")
    alpha1_strength = load_if_exists(SM_PARITY / "candidate_data" / "selected_alpha1_source_strength_normalization_theorem.candidate.json")
    alpha1_value = load_if_exists(SM_PARITY / "candidate_data" / "selected_alpha1_source_strength_value_emission_attempt.candidate.json")
    alpha1_bridge = load_if_exists(SM_PARITY / "candidate_data" / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt.candidate.json")
    nonsm_bridge = load_if_exists(NONSM / "candidate_data" / "q79_alpha1_retarded_kernel_formula_nmtt_bridge.candidate.json")

    univ = {
        "schema": "MTTIndividualConstantsUniversalPolicyImport.v1",
        "status": "UNIVERSAL_PARAMETER_POLICY_IMPORTED_ZERO_SELECTED",
        "source_repo": rel(SM_PARITY),
        "source_candidate": rel(SM_PARITY / "candidate_data" / "universal_source_parameter_policy.candidate.json"),
        "source_present": universal_policy is not None,
        "selected_parameter_count_now": universal_policy.get("selected_parameter_count_now") if universal_policy else None,
        "maximum_live_universal_parameters": universal_policy.get("maximum_live_universal_parameters") if universal_policy else None,
        "policy_used": "No universal parameter may be used to close a constant until a candidate-specific source theorem selects it before empirical replay.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    targets = {
        "schema": "MTTIndividualConstantTargets.v1",
        "status": "TARGETS_CLASSIFIED_INITIAL_FRONTIER",
        "targets": [
            {
                "label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH",
                "constant_family": "fine-structure / electroweak U(1) normalization",
                "why_first": "Most existing source-strength, retarded-kernel, transported dotD, and alpha1 bridge scaffolding already exists.",
                "readiness": "HIGHEST",
                "preferred_route": "derive same-branch source-strength normalization or typed retarded-overlap kernel before measured alpha comparison",
                "possible_universal_parameter_classes": ["UP-RET-OVERLAP", "UP-ACTION-NORM"],
                "value_claimed_now": False,
            },
            {
                "label": "CONST-GR-01 / ABSOLUTE-SCALE-GN",
                "constant_family": "Newton/Planck absolute scale",
                "why_not_first": "Likely needs dimensionful anchor policy and GR/protospinor bridge; source machinery is broader and less local.",
                "readiness": "MEDIUM",
                "preferred_route": "derive physical absolute scale from modal gap/source anchor",
                "possible_universal_parameter_classes": ["UP-ABS-SCALE"],
                "value_claimed_now": False,
            },
            {
                "label": "CONST-CP-01 / FINITE-PHASE-ORIENTATION",
                "constant_family": "CP-like finite phase/orientation",
                "why_not_first": "Finite quotient support exists, but physical map to CKM/PMNS phase still needs selected source binding.",
                "readiness": "MEDIUM",
                "preferred_route": "derive finite phase branch from quotient/topological admissibility before CKM comparison",
                "possible_universal_parameter_classes": ["UP-PHASE"],
                "value_claimed_now": False,
            },
            {
                "label": "CONST-COSMO-01 / BOUNDARY-ADMISSIBILITY",
                "constant_family": "cosmological/boundary constants",
                "why_not_first": "Needs measurement/cosmology boundary interface before useful individual constant attack.",
                "readiness": "LOW",
                "preferred_route": "derive global boundary/admissibility rule",
                "possible_universal_parameter_classes": ["UP-BOUNDARY"],
                "value_claimed_now": False,
            },
            {
                "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD",
                "constant_family": "Higgs quartic/threshold",
                "why_not_first": "Precision profile machinery exists, but source-normalized threshold kernel remains less direct than alpha1.",
                "readiness": "LOW_TO_MEDIUM",
                "preferred_route": "derive selected Higgs projector/source and threshold kernel",
                "possible_universal_parameter_classes": ["UP-ACTION-NORM", "UP-RET-OVERLAP"],
                "value_claimed_now": False,
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    first = {
        "schema": "MTTFirstIndividualConstantAttackAlpha1.v1",
        "status": "ALPHA1_SELECTED_AS_FIRST_ATTACK_VALUE_OPEN",
        "label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH",
        "target_constant": "fine-structure/electroweak U(1) source-strength normalization",
        "why_first": [
            "Current repo already has a source-strength normalization theorem gate.",
            "Current repo already has alpha1 source-identity / retarded-kernel attempts.",
            "Sibling constants repo appears to contain a q79 alpha1 retarded-kernel bridge.",
            "This target is a likely universal retarded-overlap or action-normalization test without using masses or flavor data.",
        ],
        "imported_support": {
            "sm_parity_universal_policy": univ["source_present"],
            "sm_parity_alpha1_strength_theorem": alpha1_strength is not None,
            "sm_parity_alpha1_value_attempt": alpha1_value is not None,
            "sm_parity_alpha1_retarded_kernel_attempt": alpha1_bridge is not None,
            "nonsm_q79_alpha1_bridge": nonsm_bridge is not None,
        },
        "must_not_do": [
            "fit alpha from its measured value",
            "choose the branch by minimizing alpha residual",
            "reuse a benchmark coupling as a source-strength coordinate",
            "promote a universal parameter before its source theorem is built",
        ],
        "first_calculation_goal": "construct a source-side alpha1 candidate packet: selected source-strength coordinate, retarded-overlap kernel or action-normalization route, expected scale role, and validator comparing only after selection",
        "value_claimed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterConstantFrontierLedger.v1",
        "next_required_artifact": "MTT_CONST_EM_01_Alpha1SourceStrengthCandidatePacket_v1",
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1",
            "task": "Import alpha1 source-strength, retarded-kernel, and universal-parameter policy support; build the first selected-source candidate packet without using measured alpha as selector.",
        },
        "secondary": {
            "label": "UNIV-PARAM / SOURCE-ANCHOR / UP-1",
            "task": "Check whether alpha1 requires zero parameters or a single universal retarded-overlap/action-normalization parameter selected upstream.",
        },
        "status": "NEXT_WORKORDER_ALPHA1_CANDIDATE_PACKET",
    }

    candidate = {
        "candidate": "MTTIndividualConstantsFrontierLedger",
        "status": STATUS,
        "source_repos_scanned": {
            "mtt_sm_parity_closure": exists(SM_PARITY),
            "mtt_nonsm_constants_no_knob": exists(NONSM),
        },
        "output_packets": {
            "universal_parameter_policy_import": rel(UNIV),
            "individual_constant_targets": rel(TARGETS),
            "first_attack_alpha1": rel(FIRST),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "new_repo_initialized_for_individual_constants": True,
            "universal_parameter_policy_imported": univ["source_present"],
            "constant_targets_ranked": True,
            "alpha1_selected_as_first_attack": True,
        },
        "what_remains_open": {
            "alpha1_candidate_source_packet": True,
            "alpha1_value_derivation": True,
            "universal_parameter_selection_if_needed": True,
            "any_constant_value_claim": True,
        },
        "recommendation": "Attack CONST-EM-01 / ALPHA1-SOURCE-STRENGTH first.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_IndividualConstants_FrontierLedger_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "first_attack": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH",
        "value_claimed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT Individual Constants Frontier Ledger v1

Status: `{STATUS}`

This repo starts the individual-constants fork.

## First Target

`CONST-EM-01 / ALPHA1-SOURCE-STRENGTH`

This is the best first constant to attack because existing repos already contain
alpha1 source-strength, retarded-kernel, transported dotD, and source-identity
scaffolding.  The goal is not to fit the measured fine-structure constant.  The
goal is to build a selected source-side packet first, then compare downstream.

## Universal Parameter Policy

The universal-parameter middle tier is imported from `mtt-sm-parity-closure`.
Current selected universal parameter count is `0`.  Up to `3` universal source
parameters may be considered only after source-level selection theorems.

## Guardrail

No constant value is claimed here.  Measured constants may be used only for
post-selection comparison, never to choose branches, kernels, source-strength
coordinates, or universal parameters.

## Next

Next artifact: `MTT_CONST_EM_01_Alpha1SourceStrengthCandidatePacket_v1`
"""

    audit = '''"""Audit the initial individual constants frontier ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "constant_frontier_ledger"
CANDIDATE = DATA / "constant_frontier_ledger.candidate.json"
TARGETS = BASE / "individual_constant_targets.packet.json"
FIRST = BASE / "first_attack_alpha1.packet.json"
UNIV = BASE / "universal_parameter_policy_import.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "constant_frontier_ledger_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_IndividualConstants_FrontierLedger_v1.md"
BUILD = ROOT / "scripts" / "build_constant_frontier_ledger.py"

STATUS = "MTT_INDIVIDUAL_CONSTANTS_FRONTIER_LEDGER_BUILT_ALPHA1_FIRST"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    targets = load(TARGETS)
    first = load(FIRST)
    univ = load(UNIV)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["alpha1_selected_as_first_attack"] is True, "alpha1 not selected first")
    require(candidate["what_remains_open"]["alpha1_value_derivation"] is True, "alpha1 value should remain open")
    require(candidate["recommendation"] == "Attack CONST-EM-01 / ALPHA1-SOURCE-STRENGTH first.", "recommendation mismatch")

    require(targets["targets"][0]["label"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH", "first target mismatch")
    require(targets["targets"][0]["readiness"] == "HIGHEST", "alpha1 readiness mismatch")
    require(all(item["value_claimed_now"] is False for item in targets["targets"]), "target value overclaim")

    require(first["label"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH", "first packet label mismatch")
    require(first["value_claimed_now"] is False, "alpha1 value overclaimed")
    require(first["imported_support"]["sm_parity_universal_policy"] is True, "universal policy not imported")
    require(first["imported_support"]["sm_parity_alpha1_strength_theorem"] is True, "alpha1 strength theorem not found")

    require(univ["source_present"] is True, "universal policy source missing")
    require(univ["selected_parameter_count_now"] == 0, "universal parameter count must start at zero")
    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1", "next label mismatch")
    require(cert["first_attack"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH", "cert first attack mismatch")
    require("No constant value is claimed here" in note, "note guard missing")

    for packet in [candidate, targets, first, univ, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (UNIV, univ),
        (TARGETS, targets),
        (FIRST, first),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    (CORPUS / "constant_frontier_ledger_audit.py").write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
