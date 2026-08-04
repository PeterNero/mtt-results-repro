"""Build the universal source-parameter policy artifact.

This creates the middle tier between the zero-parameter no-knob ideal and
ordinary measured-parameter replay.  Universal source parameters are allowed
only if they are global, source-level, typed before comparison to observed
data, and audited through every downstream use.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "universal_source_parameter_policy"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
POLICY = BASE / "universal_source_parameter_policy.packet.json"
CANDIDATES = BASE / "candidate_universal_parameters.packet.json"
GATES = BASE / "current_gate_mapping.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_UniversalSourceParameterPolicy_v1.md"
AUDIT = CORPUS / f"{SLUG}_audit.py"

STATUS = "MTT_UNIVERSAL_SOURCE_PARAMETER_POLICY_BUILT_NO_PARAMETERS_SELECTED"
NEXT = "MTT_UniversalSourceParameterCandidateAudit_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    policy = {
        "schema": "MTTUniversalSourceParameterPolicy.v1",
        "status": "POLICY_BUILT_NO_UNIVERSAL_PARAMETER_SELECTED",
        "label": "UNIV-PARAM / SOURCE-ANCHOR / UP-0",
        "tiers": {
            "NO_KNOB_IDEAL": {
                "target": "zero fitted universal constants",
                "status": "PREFERRED_STRONGEST_TARGET",
            },
            "MINIMAL_UNIVERSAL_PARAMETER_REALISM": {
                "target": "0 to 3 universal source parameters if forced by selected universe-level structure",
                "status": "ALLOWED_ONLY_UNDER_STRICT_POLICY",
            },
            "ORDINARY_FITTED_KNOBS": {
                "target": "sector-specific or observable-specific fitted parameters",
                "status": "FORBIDDEN_AS_SOURCE_PROOF",
            },
        },
        "admissibility_rules": [
            "parameter is universal across sectors and observables",
            "parameter is selected before comparison to measured constants",
            "parameter has a typed source-level role in the selected MTT packet",
            "parameter is not refit per particle, sector, generation, or observable",
            "parameter use is propagated through explicit downstream maps",
            "parameter cannot be inferred from the locked target residual it later explains",
            "parameter count and role are declared before replay",
        ],
        "forbidden_uses": [
            "using Yukawa, CKM, PMNS, Higgs, alpha, or mass targets to choose the parameter",
            "introducing one parameter per sector or observable",
            "renaming measured constants as source constants",
            "using a benchmark residual to select a branch",
            "closing no-knob claims with a parameter whose source role is not theorem-derived",
        ],
        "maximum_live_universal_parameters": 3,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    candidates = {
        "schema": "MTTUniversalSourceParameterCandidates.v1",
        "status": "CANDIDATE_CLASSES_DEFINED_NONE_SELECTED",
        "candidate_classes": [
            {
                "id": "UP-ACTION-NORM",
                "name": "global action normalization",
                "possible_role": "overall normalization of selected Phi_fin/Theta/Strominger action",
                "may_affect": ["dimensionful action scale", "source-strength normalization"],
                "admissible_if": "normalization is fixed by selected source/action principle before empirical replay",
                "selected_now": False,
            },
            {
                "id": "UP-ABS-SCALE",
                "name": "physical absolute scale anchor",
                "possible_role": "dimensionful conversion between internal MTT units and physical units",
                "may_affect": ["G_N", "Planck scale", "cosmological/dimensionful constants"],
                "admissible_if": "single universe-level unit anchor is declared and not sector-fitted",
                "selected_now": False,
            },
            {
                "id": "UP-RET-OVERLAP",
                "name": "universal retarded-overlap strength",
                "possible_role": "global normalization for retarded overlap or dynamic C1 transfer",
                "may_affect": ["alpha1 driver", "dynamic C1 overlap", "threshold kernels"],
                "admissible_if": "same value controls all sectors through typed source maps",
                "selected_now": False,
            },
            {
                "id": "UP-PHASE",
                "name": "universal finite phase or orientation selector",
                "possible_role": "global orientation/phase branch for finite quotient data",
                "may_affect": ["CP-like finite character", "orientation-carrying source maps"],
                "admissible_if": "phase is selected by topology/admissibility before CKM/PMNS comparison",
                "selected_now": False,
            },
            {
                "id": "UP-BOUNDARY",
                "name": "universal boundary/admissibility parameter",
                "possible_role": "global admissible boundary condition or record-selection strength",
                "may_affect": ["cosmology", "measurement/record interface"],
                "admissible_if": "one boundary rule applies globally and is not adjusted per dataset",
                "selected_now": False,
            },
        ],
        "selected_parameter_count_now": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    gates = {
        "schema": "MTTUniversalSourceParameterGateMapping.v1",
        "status": "CURRENT_GATES_MAPPED_TO_POSSIBLE_UNIVERSAL_PARAMETER_CLASSES",
        "gate_mapping": {
            "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED": {
                "preferred_zero_parameter_route": "derive SelectedWeylVariationActionPrinciple directly",
                "possible_universal_parameter_if_needed": ["UP-ACTION-NORM", "UP-RET-OVERLAP"],
                "parameter_allowed_to_close_now": False,
            },
            "alpha1_driver/source-strength": {
                "preferred_zero_parameter_route": "derive same-branch source-strength normalization",
                "possible_universal_parameter_if_needed": ["UP-RET-OVERLAP", "UP-ACTION-NORM"],
                "parameter_allowed_to_close_now": False,
            },
            "dimensionful absolute normalization": {
                "preferred_zero_parameter_route": "derive physical scale from selected modal gap/source anchor",
                "possible_universal_parameter_if_needed": ["UP-ABS-SCALE"],
                "parameter_allowed_to_close_now": False,
            },
            "finite CP/orientation branch": {
                "preferred_zero_parameter_route": "derive branch from finite quotient/topological admissibility",
                "possible_universal_parameter_if_needed": ["UP-PHASE"],
                "parameter_allowed_to_close_now": False,
            },
            "measurement/cosmology boundary": {
                "preferred_zero_parameter_route": "derive record/boundary selection from admissibility/fixed point",
                "possible_universal_parameter_if_needed": ["UP-BOUNDARY"],
                "parameter_allowed_to_close_now": False,
            },
        },
        "policy_effect": "Universal parameters are now a named audit lane, but none may be used until a candidate-specific source theorem is built.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterUniversalSourceParameterPolicy.v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "UNIV-PARAM / SOURCE-ANCHOR / UP-1",
            "task": "Audit each candidate universal source parameter against source-priority, universality, non-fitting, and downstream-use rules.",
        },
        "parallel": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED",
            "task": "Continue trying zero-parameter derivation of the SelectedWeylVariationActionPrinciple; universal parameters cannot be used here until a UP candidate is selected by theorem.",
        },
        "status": "NEXT_WORKORDER_AUDIT_CANDIDATE_UNIVERSAL_PARAMETERS_WITH_ZERO_PARAMETER_ROUTE_PRESERVED",
    }

    candidate = {
        "candidate": "MTTUniversalSourceParameterPolicy",
        "active_label": "UNIV-PARAM / SOURCE-ANCHOR / UP-0",
        "status": STATUS,
        "output_packets": {
            "policy": rel(POLICY),
            "candidate_universal_parameters": rel(CANDIDATES),
            "current_gate_mapping": rel(GATES),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "minimal_universal_parameter_tier_named": True,
            "admissibility_rules_declared": True,
            "forbidden_knob_policy_declared": True,
            "current_gates_mapped": True,
        },
        "what_remains_open": {
            "select_any_universal_parameter": True,
            "prove_candidate_specific_source_theorem": True,
            "use_universal_parameter_to_close_current_gate": True,
            "zero_parameter_no_knob_closure": True,
        },
        "selected_parameter_count_now": 0,
        "maximum_live_universal_parameters": 3,
        "theorem": {
            "name": "UniversalSourceParameterAdmissibilityPolicy",
            "proved": True,
            "statement": "A nonzero universal parameter count is credible only for source-level constants selected before empirical replay, universal across sectors, typed into the selected MTT packet, and never refit per observable. This policy creates that tier without selecting any such parameter now.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_UniversalSourceParameterPolicy_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_parameter_count_now": 0,
        "maximum_live_universal_parameters": 3,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Universal Source Parameter Policy v1

Status label: `UNIV-PARAM / SOURCE-ANCHOR / UP-0`

Status: `{STATUS}`

## Result

The repo now has a formal middle tier between the zero-parameter no-knob ideal
and ordinary measured-parameter replay.

No universal parameter is selected here.  The selected count is `0`, with a
maximum live allowance of `3` only if future artifacts prove source-level,
universal, pre-empirical selection.

Allowed classes are global action normalization, physical absolute scale,
universal retarded-overlap strength, universal finite phase/orientation, and
universal boundary/admissibility parameter.  All are currently unselected.

## Guardrail

Universal parameters are not fitted knobs.  They may not be chosen from
Yukawa, CKM, PMNS, Higgs, gauge, mass, CP, or residual target values.  They
must be selected upstream and applied globally through typed maps.

## Current Use

For `PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED`, the preferred route remains
zero-parameter derivation of the `SelectedWeylVariationActionPrinciple`.  A
universal action normalization or retarded-overlap strength is only a future
candidate if a source theorem selects it before data comparison.

Next artifact: `{NEXT}`
"""

    audit = f'''"""Audit {SLUG}."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "{SLUG}"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{{SLUG}}.candidate.json"
POLICY = BASE / "universal_source_parameter_policy.packet.json"
CANDIDATES = BASE / "candidate_universal_parameters.packet.json"
GATES = BASE / "current_gate_mapping.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_UniversalSourceParameterPolicy_v1.md"
BUILD = ROOT / "scripts" / "build_universal_source_parameter_policy.py"
STATUS = "{STATUS}"


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
    policy = load(POLICY)
    candidates = load(CANDIDATES)
    gates = load(GATES)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["selected_parameter_count_now"] == 0, "selected parameter count must be zero")
    require(candidate["maximum_live_universal_parameters"] == 3, "max parameter count mismatch")
    require(candidate["theorem"]["proved"] is True, "policy theorem missing")
    require(candidate["what_closes_now"]["minimal_universal_parameter_tier_named"] is True, "tier not named")
    require(candidate["what_remains_open"]["select_any_universal_parameter"] is True, "selection should remain open")

    require(policy["label"] == "UNIV-PARAM / SOURCE-ANCHOR / UP-0", "policy label mismatch")
    require(policy["tiers"]["NO_KNOB_IDEAL"]["status"] == "PREFERRED_STRONGEST_TARGET", "no-knob tier mismatch")
    require(policy["tiers"]["ORDINARY_FITTED_KNOBS"]["status"] == "FORBIDDEN_AS_SOURCE_PROOF", "fitted knob tier mismatch")
    require(policy["maximum_live_universal_parameters"] == 3, "policy max mismatch")
    require(len(policy["admissibility_rules"]) >= 7, "admissibility rules incomplete")

    require(candidates["selected_parameter_count_now"] == 0, "candidate packet selected parameter")
    require(len(candidates["candidate_classes"]) == 5, "candidate class count mismatch")
    require(all(item["selected_now"] is False for item in candidates["candidate_classes"]), "candidate class overselected")

    require(gates["gate_mapping"]["PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED"]["parameter_allowed_to_close_now"] is False, "PSM gate should not allow parameter closure now")
    require("UP-ABS-SCALE" in gates["gate_mapping"]["dimensionful absolute normalization"]["possible_universal_parameter_if_needed"], "absolute scale candidate missing")
    require(next_work["primary"]["label"] == "UNIV-PARAM / SOURCE-ANCHOR / UP-1", "next label mismatch")
    require(cert["selected_parameter_count_now"] == 0, "cert selected parameter count mismatch")
    require("No universal parameter is selected here" in note, "note guard missing")
    require("not fitted knobs" in note, "note fitted knob guard missing")

    for packet in [candidate, policy, candidates, gates, cert]:
        guard(packet)

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (POLICY, policy),
        (CANDIDATES, candidates),
        (GATES, gates),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
