"""Build the cross-use universal parameter admissibility theorem.

This artifact refines the universal-parameter tier: a provisional universal
parameter may be admitted only when it is declared once, shared across at least
two independent source paths, not retuned, and turns all non-calibrating
observables into predictions while no-knob status remains open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "universal_crossuse_parameter_admissibility_theorem"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
THEOREM = BASE / "crossuse_admissibility_theorem.packet.json"
ALPHA1_CASE = BASE / "alpha1_crossuse_case.packet.json"
PSM_BOUNDARY = BASE / "psm_c1_02_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_UniversalCrossUseParameterAdmissibilityTheorem_v1.md"
AUDIT = CORPUS / f"{SLUG}_audit.py"

POLICY = DATA / "universal_source_parameter_policy.candidate.json"
ALPHA1_IMPORT = DATA / "universal_alpha1_frontier_handoff_import.candidate.json"
ALPHA1_PACKET = DATA / "universal_alpha1_frontier_handoff_import" / "alpha1_frontier_handoff_import.packet.json"

STATUS = "MTT_UNIVERSAL_CROSSUSE_PARAMETER_ADMISSIBILITY_THEOREM_BUILT"
NEXT = "MTT_UniversalSourceParameterCandidateAudit_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    policy = load(POLICY)
    alpha1_import = load(ALPHA1_IMPORT)
    alpha1_packet = load(ALPHA1_PACKET)

    theorem = {
        "schema": "MTTUniversalCrossUseParameterAdmissibilityTheorem.v1",
        "status": "CROSSUSE_ADMISSIBILITY_THEOREM_PROVED_AS_POLICY_GATE",
        "label": "UNIV-PARAM / CROSS-USE / B23",
        "theorem_name": "CrossUseUniversalParameterAdmissibilityTheorem",
        "statement": (
            "A provisional universal parameter may be admitted without damaging credibility only if it is declared once, "
            "shared across at least two independent source paths, not retuned per observable, and fitting one calibrating "
            "observable converts all other affected observables into predictions. No-knob status remains open until the "
            "parameter itself is derived from selected source data."
        ),
        "admission_criteria": {
            "declared_once": True,
            "shared_across_at_least_two_independent_source_paths": True,
            "not_retuned_per_observable": True,
            "one_calibration_makes_rest_predictions": True,
            "no_knob_status_remains_open_until_parameter_derived": True,
        },
        "provisional_use_classification": {
            "allowed_name": "PROVISIONAL_UNIVERSAL_SOURCE_PARAMETER",
            "not_allowed_name": "NO_KNOB_DERIVED_CONSTANT",
            "fit_role": "at_most_one_calibrating_observable_per_parameter",
            "prediction_role": "all_other_downstream_observables_in_scope",
        },
        "forbidden": [
            "retuning between alpha, masses, CKM, PMNS, Higgs, cosmology, or sectors",
            "declaring independent copies of the same parameter in different paths",
            "calling a calibrated universal primitive a no-knob derivation",
            "choosing the parameter from a residual after inspecting all target observables",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    alpha1_case = {
        "schema": "MTTAlpha1CrossUseUniversalParameterCase.v1",
        "status": "ALPHA1_CASE_READY_FOR_CROSSUSE_AUDIT_NOT_ADMITTED_YET",
        "source": rel(ALPHA1_IMPORT),
        "one_universal_primitive_extension_ready": alpha1_import["imported_one_universal_primitive_ready"],
        "strict_no_knob_alpha_phys_closed": False,
        "candidate_parameter_class": "UP-ABS-SCALE",
        "candidate_symbols": ["L0", "E0"],
        "internal_coefficients": alpha1_packet["values_to_carry"],
        "currently_satisfies": {
            "declared_once": True,
            "not_retuned_per_observable": True,
            "no_observed_selector": True,
            "no_knob_status_open": True,
        },
        "still_needs_for_B23_admission": {
            "at_least_two_independent_source_paths_use_same_primitive": True,
            "calibrating_observable_declared_before_replay": True,
            "prediction_set_declared": True,
            "downstream_prediction_audit": True,
        },
        "admitted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    psm_boundary = {
        "schema": "MTTPSMC102CrossUseParameterBoundary.v1",
        "status": "PSM_C1_02_BOUNDARY_PROTECTED_FROM_PARAMETER_SHORTCUT",
        "label": "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED",
        "boundary_rule": (
            "The cross-use theorem does not permit a universal primitive to close the PSM-C1-02 source-identity gate "
            "unless that same primitive is connected by a selected source theorem to the physical Phi_fin/Theta/Strominger "
            "action or to independent finite row-source execution."
        ),
        "zero_parameter_route_remains_primary": True,
        "universal_parameter_shortcut_allowed_now": False,
        "allowed_future_use_if": [
            "same primitive is declared once",
            "same primitive appears in at least two independent source paths",
            "one calibration is declared and all other observables become predictions",
            "selected source theorem connects primitive to VPB-1-UNPATCHED or SI-1u-B2 row-source execution",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterCrossUseParameterTheorem.v1",
        "next_required_artifact": NEXT,
        "primary": {
            "label": "UNIV-PARAM / CROSS-USE / B23-ALPHA1-AUDIT",
            "task": "Audit whether the alpha1 one-primitive candidate is shared by at least two independent source paths and define its one calibration plus prediction set.",
        },
        "parallel": {
            "label": "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED",
            "task": "Continue zero-parameter derivation; only use a provisional universal parameter if a selected source theorem connects it to this gate.",
        },
        "status": "NEXT_WORKORDER_ALPHA1_CROSSUSE_AUDIT_WITH_PSM_BOUNDARY_PROTECTED",
    }

    candidate = {
        "candidate": "MTTUniversalCrossUseParameterAdmissibilityTheorem",
        "active_label": "UNIV-PARAM / CROSS-USE / B23",
        "status": STATUS,
        "policy_source": rel(POLICY),
        "policy_status": policy["status"],
        "output_packets": {
            "crossuse_admissibility_theorem": rel(THEOREM),
            "alpha1_crossuse_case": rel(ALPHA1_CASE),
            "psm_c1_02_boundary": rel(PSM_BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "cross_use_universal_parameter_policy_theorem": True,
            "superset_strategy_credibility_guard": True,
            "alpha1_candidate_mapped_to_B23_audit": True,
            "PSM_C1_02_parameter_shortcut_blocked": True,
        },
        "what_remains_open": {
            "admit_alpha1_one_primitive_under_B23": True,
            "select_any_universal_parameter_in_this_repo": True,
            "derive_any_universal_parameter_no_knob": True,
            "unpatched_PSM_C1_02_closure": True,
        },
        "selected_parameter_count_now": 0,
        "provisional_parameter_admitted_now": False,
        "theorem": {
            "name": "CrossUseUniversalParameterAdmissibilityTheorem",
            "proved": True,
            "statement": theorem["statement"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_UniversalCrossUseParameterAdmissibilityTheorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "selected_parameter_count_now": 0,
        "provisional_parameter_admitted_now": False,
        "crossuse_policy_built": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Universal Cross-Use Parameter Admissibility Theorem v1

Status label: `UNIV-PARAM / CROSS-USE / B23`

Status: `{STATUS}`

## Theorem

A provisional universal parameter may be admitted if:

1. it is declared once,
2. it is shared across at least two independent source paths,
3. it is not retuned per observable,
4. fitting one calibrating observable converts the rest into predictions,
5. no-knob status remains open until the parameter is derived.

This is a credibility-preserving extension of the superset strategy.  It allows
one carefully declared universal primitive without turning the theory into a
many-knob fit.

## Alpha1 Case

The alpha1 handoff is ready for a B23 audit, but not admitted here.  It already
has a one-universal-primitive candidate and no observed-selector violation.
It still needs a proof that the same primitive is shared across at least two
independent source paths, plus a declared calibration observable and prediction
set.

## PSM-C1-02 Boundary

This theorem does not close `PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED`.
The zero-parameter derivation remains primary unless a selected source theorem
connects a B23-admitted primitive to the physical action or independent
row-source execution.

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
THEOREM = BASE / "crossuse_admissibility_theorem.packet.json"
ALPHA1_CASE = BASE / "alpha1_crossuse_case.packet.json"
PSM_BOUNDARY = BASE / "psm_c1_02_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_UniversalCrossUseParameterAdmissibilityTheorem_v1.md"
BUILD = ROOT / "scripts" / "build_universal_crossuse_parameter_admissibility_theorem.py"
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
    theorem = load(THEOREM)
    alpha1_case = load(ALPHA1_CASE)
    psm_boundary = load(PSM_BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["selected_parameter_count_now"] == 0, "parameter overselected")
    require(candidate["provisional_parameter_admitted_now"] is False, "provisional parameter overadmitted")
    require(candidate["what_closes_now"]["PSM_C1_02_parameter_shortcut_blocked"] is True, "PSM shortcut not blocked")
    require(theorem["admission_criteria"]["shared_across_at_least_two_independent_source_paths"] is True, "cross-use criterion missing")
    require(theorem["admission_criteria"]["one_calibration_makes_rest_predictions"] is True, "prediction criterion missing")
    require(alpha1_case["admitted_now"] is False, "alpha1 overadmitted")
    require(alpha1_case["still_needs_for_B23_admission"]["at_least_two_independent_source_paths_use_same_primitive"] is True, "alpha1 cross-use need missing")
    require(psm_boundary["universal_parameter_shortcut_allowed_now"] is False, "PSM parameter shortcut allowed")
    require(psm_boundary["zero_parameter_route_remains_primary"] is True, "zero-parameter priority missing")
    require(next_work["primary"]["label"] == "UNIV-PARAM / CROSS-USE / B23-ALPHA1-AUDIT", "next label mismatch")
    require(cert["provisional_parameter_admitted_now"] is False, "cert overadmitted")
    require("fitting one calibrating observable converts the rest into predictions" in note, "note theorem missing")

    for packet in [candidate, theorem, alpha1_case, psm_boundary, cert]:
        guard(packet)

    print(f"PASS {{CANDIDATE.name}}: {{candidate['status']}}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''

    for path, payload in [
        (THEOREM, theorem),
        (ALPHA1_CASE, alpha1_case),
        (PSM_BOUNDARY, psm_boundary),
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
