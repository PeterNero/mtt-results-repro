"""Build CONST-EM-01 alpha1 QA-SU3 replay.

This artifact replays the QA-SU3 U1Y Route-C alpha1 driver theorem as a
local dependency, instead of importing it by authority.  The replay can close
only the MTT source-side alpha1 driver.  It cannot identify that driver with
alpha(0), alpha(M_Z), or a GUT-normalized alpha_1 convention.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_qa_replay"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
QA_REPLAY = BASE / "qa_dependency_replay.packet.json"
SOURCE_DECISION = BASE / "alpha1_source_side_closure_decision.packet.json"
CONVENTION = BASE / "alpha_convention_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_QAReplay_v1.md"

STATUS = "MTT_CONST_EM_01_ALPHA1_QA_REPLAY_ACCEPTED_SOURCE_SIDE_DRIVER_CLOSED_CONVENTION_MAP_OPEN"

QA_FILES = {
    "dotd_transport": "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver.candidate.json",
    "source_strength": "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet.candidate.json",
    "chernweil_value": "selected_u1y_routec_samesource_chernweil_operator_functional_value.candidate.json",
    "operator_emission": "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap.candidate.json",
    "final_replay": "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json",
}

QA_AUDITS = [
    "selected_u1y_routec_dotd_alpha1_transport_derivative_and_driver_audit.py",
    "selected_u1y_routec_alpha1_source_strength_value_or_samesource_packet_audit.py",
    "selected_u1y_routec_samesource_chernweil_operator_functional_value_audit.py",
    "selected_u1y_routec_operator_emission_overlap_from_terminal_slotmap_audit.py",
    "selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap_audit.py",
]


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


def run_audit(name: str) -> dict[str, Any]:
    path = QA_SU3 / "proof_corpus" / name
    if not path.exists():
        return {
            "audit": name,
            "path": rel(path),
            "present": False,
            "exit_code": 1,
            "passed": False,
            "tail": ["missing audit"],
        }
    proc = subprocess.run(
        [sys.executable, str(path)],
        cwd=QA_SU3,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    lines = [line.rstrip() for line in proc.stdout.splitlines() if line.strip()]
    return {
        "audit": name,
        "path": rel(path),
        "present": True,
        "exit_code": proc.returncode,
        "passed": proc.returncode == 0,
        "tail": lines[-12:],
    }


def guardrail_ok(candidate: dict[str, Any]) -> bool:
    guards = candidate.get("guardrails", {})
    forbidden = [
        "uses_observed_data",
        "uses_benchmark_data",
        "uses_observed_or_benchmark_inputs",
        "uses_diagnostic_lift_as_proof",
        "uses_full_flag_probe_as_proof",
        "uses_locked_C1_columns",
        "target_fitting_used",
    ]
    return all(guards.get(key) is not True for key in forbidden) and candidate.get("target_fitting_used") is not True


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    qa_candidates = {
        key: load(QA_SU3 / "candidate_data" / filename)
        for key, filename in QA_FILES.items()
    }
    audit_results = [run_audit(name) for name in QA_AUDITS]
    all_audits_pass = all(item["passed"] for item in audit_results)
    all_guardrails_ok = all(guardrail_ok(item) for item in qa_candidates.values())

    dotd = qa_candidates["dotd_transport"]
    source = qa_candidates["source_strength"]
    cw = qa_candidates["chernweil_value"]
    emission = qa_candidates["operator_emission"]
    final = qa_candidates["final_replay"]

    dependency_checks = {
        "qa_repo_present": QA_SU3.exists(),
        "qa_audits_all_pass": all_audits_pass,
        "qa_guardrails_all_preserved": all_guardrails_ok,
        "transport_derivative_formula_closed": dotd["decision"]["transport_derivative_formula_closed"] is True,
        "dotD_source_formula_closed": dotd["decision"]["selected_dotD_source_formula_closed"] is True,
        "source_strength_equivalence_theorem_proved": source["decision"]["source_strength_equivalence_theorem_proved"] is True,
        "source_strength_no_go_before_same_source_value_proved": source["decision"]["current_source_value_no_go_proved"] is True,
        "chernweil_support_value_is_unit": cw["decision"]["support_candidate_value_N_alpha1_h_ext"] == 1.0,
        "chernweil_support_residual_zero": cw["decision"]["support_candidate_residual_zero"] is True,
        "operator_emission_same_branch_closed": emission["decision"]["same_branch_functional_operator_emission_closed"] is True,
        "operator_overlap_normalization_emitted": emission["decision"]["selected_overlap_normalization_emitted"] is True,
        "operator_U10_Ubar5_blocks_emitted": emission["decision"]["selected_U10_Ubar5_operator_blocks_emitted"] is True,
        "operator_1M_Dirac_block_emitted": emission["decision"]["selected_1M_Dirac_operator_block_emitted"] is True,
        "final_alpha_requirements_all_true": all(final["alpha_requirements"].values()),
        "final_selected_N_alpha1_h_ext_value": final["what_closes_now"]["selected_N_alpha1_h_ext_value"] is True,
        "final_du_dalpha1_equals_h_ext": final["what_closes_now"]["du_dalpha1_equals_h_ext"] is True,
        "final_alpha1_driver_verified": final["decision"]["alpha1_driver_verified"] is True,
        "final_selected_dotD_source_verified": final["decision"]["selected_dotD_source_verified"] is True,
        "final_honest_dotD_validator_closed": final["decision"]["honest_dotD_validator_closed"] is True,
        "final_promoted_value_unit": final["promoted_value"]["N_alpha1_h_ext"] == 1.0,
        "final_promoted_lambda_unit": final["promoted_value"]["lambda_alpha1"] == 1.0,
        "final_tangent_residual_zero": final["promoted_value"]["tangent_residual_l2"] == 0.0,
    }
    source_side_accepted = all(dependency_checks.values())

    qa_replay = {
        "schema": "MTTConstEM01Alpha1QAReplayDependencyPacket.v1",
        "status": "QA_REPLAY_DEPENDENCIES_PASS" if source_side_accepted else "QA_REPLAY_DEPENDENCIES_FAIL",
        "active_label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1-REPLAY-QA",
        "qa_repo": rel(QA_SU3),
        "qa_candidates": {
            key: {
                "path": rel(QA_SU3 / "candidate_data" / QA_FILES[key]),
                "status": payload.get("status"),
                "closure_claimed": payload.get("closure_claimed"),
                "target_fitting_used": payload.get("target_fitting_used"),
                "guardrail_ok": guardrail_ok(payload),
            }
            for key, payload in qa_candidates.items()
        },
        "audit_results": audit_results,
        "dependency_checks": dependency_checks,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    source_decision = {
        "schema": "MTTConstEM01Alpha1SourceSideClosureDecision.v1",
        "status": "SOURCE_SIDE_ALPHA1_DRIVER_ACCEPTED" if source_side_accepted else "SOURCE_SIDE_ALPHA1_DRIVER_NOT_ACCEPTED",
        "active_label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1-REPLAY-QA",
        "decision": {
            "source_side_alpha1_driver_accepted_here": source_side_accepted,
            "selected_N_alpha1_h_ext_value": source_side_accepted,
            "N_alpha1_h_ext": 1.0 if source_side_accepted else None,
            "lambda_alpha1": 1.0 if source_side_accepted else None,
            "du_dalpha1_equals_h_ext": source_side_accepted,
            "alpha1_driver_verified_source_side": source_side_accepted,
            "selected_dotD_source_verified_source_side": source_side_accepted,
            "honest_dotD_replay_source_side": source_side_accepted,
            "physical_alpha_value_claimed": False,
            "alpha_zero_or_MZ_claimed": False,
            "GUT_normalized_alpha1_claimed": False,
            "universal_parameter_selected": False,
            "target_fitting_used": False,
        },
        "scope": "selected U1Y Route-C functional/operator source-side driver only",
        "why_not_physical_alpha_yet": [
            "No map from MTT source-strength coordinate to U(1)_Y coupling convention is built here.",
            "No SU(2)xU(1) electroweak mixing convention is applied here.",
            "No source-scale to alpha(0) or alpha(M_Z) running/threshold policy is applied here.",
            "No covariance or empirical comparison profile is used here.",
        ],
        "residual_open": {
            "alpha_convention_map": True,
            "alpha_zero_value": True,
            "alpha_MZ_value": True,
            "GUT_normalized_alpha1_value": True,
            "primitive_C1_contractions": True,
            "lambda_12": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_magnitudes": True,
            "full_SM_or_constants_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "source_side_closure_claimed": source_side_accepted,
    }

    convention = {
        "schema": "MTTConstEM01AlphaConventionBoundaryAfterQAReplay.v1",
        "status": "ALPHA_CONVENTION_MAP_STILL_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP",
        "source_side_result_available": source_side_accepted,
        "not_yet_identified_with": [
            "alpha(0)",
            "alpha(M_Z)",
            "GUT-normalized alpha_1=(5/3)alpha_Y",
            "low-energy e^2/(4*pi) convention",
            "any measured fine-structure value",
        ],
        "required_next_maps": [
            "MTT alpha1 source coordinate -> selected U(1)_Y/hypercharge normalization",
            "U(1)_Y and SU(2) coupling basis -> electromagnetic coupling basis",
            "source scale -> M_Z and Thomson-limit scale transport",
            "threshold and hadronic vacuum-polarization policy",
            "uncertainty/covariance comparison policy",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterConstEM01QAReplay.v1",
        "status": "NEXT_WORKORDER_ALPHA_CONVENTION_MAP",
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP",
            "task": "Construct the source-to-observable convention map from the selected MTT alpha1 source driver to U(1)_Y, electroweak mixing, alpha(M_Z), and alpha(0) comparison conventions.",
        },
        "secondary": {
            "label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A3-PAPER-PROMOTION",
            "task": "Prepare a paper-ready theorem insertion that promotes only the source-side driver and explicitly marks all physical-alpha maps open.",
        },
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1QAReplay",
        "status": STATUS if source_side_accepted else "MTT_CONST_EM_01_ALPHA1_QA_REPLAY_NOT_ACCEPTED",
        "active_label": "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1-REPLAY-QA",
        "output_packets": {
            "qa_dependency_replay": rel(QA_REPLAY),
            "alpha1_source_side_closure_decision": rel(SOURCE_DECISION),
            "alpha_convention_boundary": rel(CONVENTION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "qa_su3_alpha1_driver_theorem_replayed": source_side_accepted,
            "source_side_alpha1_driver_accepted_here": source_side_accepted,
            "selected_N_alpha1_h_ext_value": source_side_accepted,
            "du_dalpha1_equals_h_ext": source_side_accepted,
            "honest_dotD_replay_source_side": source_side_accepted,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "physical_alpha_zero_or_MZ_value": True,
            "GUT_normalized_alpha1_value": True,
            "source_to_electroweak_convention_map": True,
            "threshold_running_and_hadronic_vacuum_polarization": True,
            "primitive_C1_contractions": True,
            "lambda_12": True,
            "full_constants_or_SM_closure": True,
        },
        "theorem": {
            "name": "CONSTEM01Alpha1QAReplaySourceSidePromotionTheorem",
            "proved": source_side_accepted,
            "statement": (
                "If the QA-SU3 U1Y Route-C dependency audits replay successfully and their no-observed-data, "
                "no-target-fitting, and no-diagnostic-lift guardrails hold, then this constants repo may promote "
                "the selected source-side alpha1 driver: N_alpha1(h_ext)=1, lambda_alpha1=1, and du/dalpha1=h_ext "
                "at the selected oriented functional HYM/End0 layer.  This theorem does not identify the result "
                "with alpha(0), alpha(M_Z), GUT-normalized alpha_1, or any measured electromagnetic coupling."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "source_side_closure_claimed": source_side_accepted,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_QAReplay_v1",
        "status": candidate["status"],
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "source_side_alpha1_driver_accepted_here": source_side_accepted,
        "selected_N_alpha1_h_ext_value": source_side_accepted,
        "du_dalpha1_equals_h_ext": source_side_accepted,
        "physical_alpha_value_claimed": False,
        "universal_parameter_selected": False,
        "next_primary": "CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 QA Replay v1

Status: `{candidate["status"]}`

Label: `CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1-REPLAY-QA`

## Result

The QA-SU3 U1Y Route-C alpha1 driver theorem has been replayed as a local
dependency rather than imported by authority.

The replay accepts the **source-side** alpha1 driver:

- `N_alpha1(h_ext)=1`,
- `lambda_alpha1=1`,
- `du/dalpha1=h_ext`,
- source-side `alpha1_driver_verified`,
- source-side honest dotD replay.

This is a real promotion for the individual-constant search, but it is not yet
the physical fine-structure constant.

## Boundary

This artifact does not claim:

- `alpha(0)`,
- `alpha(M_Z)`,
- GUT-normalized `alpha_1`,
- threshold/running closure,
- primitive `C1` contractions,
- `lambda_12`,
- Yukawa magnitudes,
- full SM or full constants closure.

No observed value, benchmark value, or target fit is used as a selector.

## Superset Strategy

This is a constrained superset import.  We combine the QA-SU3 operator/emission
route, the Chern-Weil support value, and the dotD transport route, then lock the
target to a single allowed statement: the selected MTT source-side alpha1 driver
is closed.  We do not let that combined route leak into the physical alpha
convention layer.

## Next

Next label: `CONST-EM-01 / ALPHA1-CONVENTION / A2-MAP`

Build the source-to-observable convention map before any comparison with
measured electromagnetic couplings.
"""

    for path, payload in [
        (QA_REPLAY, qa_replay),
        (SOURCE_DECISION, source_decision),
        (CONVENTION, convention),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))
    return 0 if source_side_accepted else 1


if __name__ == "__main__":
    raise SystemExit(main())
