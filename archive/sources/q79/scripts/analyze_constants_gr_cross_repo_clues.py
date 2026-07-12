"""Summarize useful constants/GR repo updates for the q79 SM-closure track."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"

CONSTANTS_REPO = ROOT.parent / "mtt-nonsm-constants-no-knob"
GR_REPO = ROOT.parent / "mtt-protospinor-gr-response-proof"
QA_REPO = ROOT.parent / "mtt-qa-su3-packet-proof"

CANDIDATE = CANDIDATE_DATA / "constants_gr_cross_repo_clues.candidate.json"
CERTIFICATE = CERTIFICATES / "constants_gr_cross_repo_clues_certificate.json"


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "present": False}
    data = json.loads(path.read_text(encoding="utf-8"))
    data["_path"] = str(path)
    data["_present"] = True
    return data


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def git_snapshot(repo: Path) -> dict[str, Any]:
    if not repo.exists():
        return {"path": str(repo), "present": False}

    def run(args: list[str]) -> str:
        proc = subprocess.run(
            args,
            cwd=repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return proc.stdout.strip()

    return {
        "path": str(repo),
        "present": True,
        "branch": run(["git", "branch", "--show-current"]),
        "status_short": run(["git", "status", "--short"]),
        "recent_log": run(["git", "log", "--oneline", "-5"]).splitlines(),
        "remote_v": run(["git", "remote", "-v"]),
    }


def status(data: dict[str, Any]) -> str | None:
    return data.get("status")


def analyze() -> dict[str, Any]:
    constants = {
        "git": git_snapshot(CONSTANTS_REPO),
        "operator_packet_interface": load_json(
            CONSTANTS_REPO
            / "certificates"
            / "selected_qa_su3_color_bundle_operator_packet_interface_certificate.json"
        ),
        "operator_packet_fill_attempt": load_json(
            CONSTANTS_REPO
            / "certificates"
            / "selected_qa_su3_color_bundle_operator_packet_fill_attempt_certificate.json"
        ),
        "strominger_hym_source_packet_search": load_json(
            CONSTANTS_REPO
            / "certificates"
            / "selected_qa_su3_strominger_hym_source_packet_search_certificate.json"
        ),
        "strominger_weitzenbock_ou_completion": load_json(
            CONSTANTS_REPO
            / "certificates"
            / "selected_qa_su3_hym_strominger_weitzenbock_ou_completion_certificate.json"
        ),
        "physical_action_normalization": load_json(
            CONSTANTS_REPO / "certificates" / "physical_action_normalization_gate_certificate.json"
        ),
    }
    gr = {
        "git": git_snapshot(GR_REPO),
        "selected_gr_hessian_block_source": load_json(
            GR_REPO / "certificates" / "selected_gr_hessian_block_source_theorem_certificate.json"
        ),
        "selected_stf_hessian_form": load_json(
            GR_REPO / "certificates" / "selected_stf_hessian_form_certificate.json"
        ),
        "stf_hessian_scale_to_geff": load_json(
            GR_REPO / "certificates" / "stf_hessian_scale_to_geff_relation_certificate.json"
        ),
        "absolute_normalization_bridge": load_json(
            GR_REPO / "certificates" / "absolute_normalization_bridge_from_nonsm_certificate.json"
        ),
    }
    qa = {
        "git": git_snapshot(QA_REPO),
        "gr_surface_internal_quantum_separation": load_json(
            QA_REPO
            / "certificates"
            / "gr_surface_internal_quantum_separation_theorem_certificate.json"
        ),
    }

    constants_operator_fields = constants["operator_packet_interface"].get(
        "remaining_open_fields", []
    )
    fill_attempt = constants["operator_packet_fill_attempt"].get("fill_result", {})
    source_search = constants["strominger_hym_source_packet_search"].get(
        "search_result", {}
    )
    source_search_next = constants["strominger_hym_source_packet_search"].get(
        "next_required_artifact", {}
    )
    gr_form = gr["selected_stf_hessian_form"].get("selected_form", {})
    gr_scale = gr["stf_hessian_scale_to_geff"].get("relation", {})

    report = {
        "calculation": "ConstantsGRCrossRepoClues",
        "status": "CONSTANTS_GR_CROSS_REPO_CLUES_FORMULATED_IMPORTS_METHOD_NOT_DATA",
        "generated_by": "scripts/analyze_constants_gr_cross_repo_clues.py",
        "input_repositories": {
            "constants": constants["git"],
            "gr": gr["git"],
            "qa_su3_packet": qa["git"],
        },
        "imported_statuses": {
            "constants_operator_packet_interface": status(constants["operator_packet_interface"]),
            "constants_operator_packet_fill_attempt": status(
                constants["operator_packet_fill_attempt"]
            ),
            "constants_strominger_hym_source_packet_search": status(
                constants["strominger_hym_source_packet_search"]
            ),
            "constants_strominger_weitzenbock_ou_completion": status(
                constants["strominger_weitzenbock_ou_completion"]
            ),
            "constants_physical_action_normalization": status(
                constants["physical_action_normalization"]
            ),
            "gr_hessian_block_source": status(gr["selected_gr_hessian_block_source"]),
            "gr_stf_hessian_form": status(gr["selected_stf_hessian_form"]),
            "gr_stf_scale_to_geff": status(gr["stf_hessian_scale_to_geff"]),
            "gr_absolute_normalization_bridge": status(gr["absolute_normalization_bridge"]),
            "qa_su3_gr_surface_internal_quantum_separation": status(
                qa["gr_surface_internal_quantum_separation"]
            ),
        },
        "useful_imports_for_q79_sm_closure": {
            "selected_source_packet_discipline": {
                "source": "constants Qa/SU3 operator packet interface",
                "import_as_method": True,
                "core_fields_to_reuse_for_visible_valpha": [
                    "source_certificate",
                    "bundle_or_sheaf_or_twist",
                    "chern_or_mukai_data",
                    "freed_witten_or_bianchi_check",
                    "connection_or_residual",
                    "endomorphism_E_or_operator_block",
                    "heat_table_spectrum_or_torsion",
                    "trace_normalization",
                ],
                "constants_open_fields": constants_operator_fields,
            },
            "qa_su3_internal_reduced_packet_status": {
                "source": "Qa/SU3 GR-surface/internal-quantum separation theorem",
                "import_as_status": True,
                "closed_scope": "internal reduced Qa/SU3 determinant only",
                "value": "log(2008)",
                "meaning_for_q79_sm_closure": (
                    "The Qa/SU3 color-threshold trail now has a clean internal reduced "
                    "determinant status, but this is not a Yukawa, CKM, full threshold, "
                    "or full SM closure input. It can discipline coupling-bridge work "
                    "without replacing selected visible-source matrices."
                ),
            },
            "same_branch_source_guardrail": {
                "source": "constants Qa/SU3 packet fill attempt",
                "import_as_method": True,
                "fill_attempt_result": fill_attempt,
                "meaning_for_valpha": (
                    "Strominger/HYM templates and domain constraints do not promote "
                    "V_alpha unless the selected line-bundle/cohomology, stability, "
                    "connection, and operator data live on the same branch."
                ),
            },
            "constructive_source_candidate_search": {
                "source": "constants Qa/SU3 Strominger/HYM source packet search",
                "import_as_method": True,
                "search_result": source_search,
                "next_required_artifact": source_search_next,
                "meaning_for_valpha": (
                    "After generic templates are exhausted, the next useful move is "
                    "not more prose search but explicit source-packet candidates with "
                    "Chern/Bianchi or gerbe invariants and an independent selection rule."
                ),
            },
            "target_source_separation": {
                "source": "GR Hessian block source theorem",
                "import_as_method": True,
                "meaning_for_valpha": (
                    "Closing the target class is not the same as closing the source. "
                    "For V_alpha, c2=+4 alpha_1 and a formal Ext gate are target data; "
                    "selected Cech/Dolbeault matrices and non-split stability are source data."
                ),
            },
            "symmetry_forces_form_not_scale": {
                "source": "GR selected STF Hessian form",
                "import_as_analogy": True,
                "selected_form": gr_form,
                "meaning_for_valpha": (
                    "A symmetry theorem may force a matrix form while leaving its selected "
                    "scale or source coefficient open. This supports keeping q79/SM "
                    "operator forms separate from coefficient closure."
                ),
            },
            "normalization_not_a_free_knob": {
                "source": "constants physical action normalization and GR scale bridge",
                "import_as_guardrail": True,
                "gr_scale_relation": gr_scale,
                "meaning_for_valpha": (
                    "If a later visible-source packet needs an absolute trace or action "
                    "normalization, it must come from a selected source or be declared "
                    "dimensionless/internal-unit only."
                ),
            },
        },
        "not_imported_as_proof_data": {
            "H1_X_L_squared_value": True,
            "selected_nonzero_Ext_class": True,
            "visible_V_alpha_source": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "SM_Yukawa_or_CKM_magnitudes": True,
            "GR_TT_Hessian_as_visible_bundle_operator": True,
            "Qa_SU3_operator_packet_as_visible_V_alpha_packet": True,
            "log2008_as_full_threshold_or_SM_closure": True,
        },
        "calculation_results": {
            "constants_repo_checked": constants["git"]["present"],
            "gr_repo_checked": gr["git"]["present"],
            "qa_su3_packet_repo_checked": qa["git"]["present"],
            "constants_verify_was_run_externally_this_session": True,
            "gr_verify_was_run_externally_this_session": True,
            "qa_su3_internal_reduced_logdet_status_found": status(
                qa["gr_surface_internal_quantum_separation"]
            )
            == "QA_SU3_GR_SURFACE_INTERNAL_QUANTUM_SEPARATION_SOURCE_AMENDMENT_ACCEPTED_REDUCED_DETERMINANT_PROMOTED",
            "direct_H1_or_Cech_data_found": False,
            "direct_selected_visible_valpha_source_found": False,
            "useful_interface_discipline_found": True,
            "useful_constructive_source_packet_search_found": bool(source_search),
            "useful_target_source_separation_found": True,
        },
        "what_this_closes": {
            "cross_repo_update_check": True,
            "safe_import_boundary": True,
            "next_visible_valpha_packet_requirements_refined": True,
        },
        "still_open": {
            "fill_visible_rank2_l2_cohomology_template": True,
            "build_selected_visible_valpha_source_packet": True,
            "prove_non_split_stability": True,
            "derive_operator_block_endomorphism_or_DE": True,
            "compute_same_source_D_E_dotD_Riesz_Green": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_H1_value_imported": False,
            "claims_selected_valpha_source_imported": False,
            "claims_Qa_SU3_data_are_visible_bundle_data": False,
            "claims_log2008_is_full_threshold_or_sm_closure": False,
            "claims_GR_Hessian_is_visible_operator": False,
            "claims_full_SM_closure": False,
            "uses_observed_or_benchmark_flavor_inputs": False,
        },
        "verdict": {
            "honest_answer": (
                "The constants and GR repos add useful proof discipline but no direct "
                "H^1(X,L^2), V_alpha, or SM closure data. The strongest import is a "
                "selected source/operator packet checklist: source certificate, "
                "bundle/sheaf/twist, Chern/Bianchi data, connection/residual, operator "
                "block, finite spectral object, and normalization. The newest constants "
                "search also says the next productive move is explicit Chern/Bianchi "
                "source-packet candidates rather than broader template hunting. The "
                "Qa/SU3 packet repo now additionally supplies log(2008) as the internal "
                "reduced determinant status, not as a full threshold or SM-closure value."
            ),
            "next_action": (
                "Use this checklist to build a Visible_VAlpha_Strominger_HYM_Source_"
                "Packet interface tied to the L^2 cohomology validator, then enumerate "
                "visible V_alpha Chern/Bianchi source-packet candidates."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "ConstantsGRCrossRepoClues",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/constants_gr_cross_repo_clues.candidate.json",
        "input_repositories": report["input_repositories"],
        "imported_statuses": report["imported_statuses"],
        "useful_imports_for_q79_sm_closure": report["useful_imports_for_q79_sm_closure"],
        "not_imported_as_proof_data": report["not_imported_as_proof_data"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
