"""Import cross-repo update status and sharpen the next local gate."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"

REPOS = {
    "mtt_nonsm_constants_no_knob": ROOT,
    "mtt_q79_proof_repro": TEXPAPERS / "mtt-q79-proof-repro",
    "mtt_qa_su3_packet_proof": TEXPAPERS / "mtt-qa-su3-packet-proof",
    "mtt_sm_parity_closure": TEXPAPERS / "mtt-sm-parity-closure",
    "mtt_protospinor_gr_response_proof": TEXPAPERS / "mtt-protospinor-gr-response-proof",
}

SM = REPOS["mtt_sm_parity_closure"]

LOCAL_VISIBLE_FUNCTIONAL = CERTS / "selected_visible_source_functional_on_orbit_classification_certificate.json"
LOCAL_CW_ATTEMPT = CERTS / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json"
LOCAL_RANK2_H1 = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"
LOCAL_TERMINAL_SELECTOR = CERTS / "selected_terminal_monad_lane_source_selector_attempt_certificate.json"

SM_VISIBLE_CW = SM / "certificates" / "selected_visible_chern_weil_operator_source_certificate.json"
SM_SAME_SOURCE_PACKET = SM / "certificates" / "selected_nonsplit_rank2_or_routec_same_source_packet_certificate.json"
SM_SYMMETRY_BREAKER = SM / "certificates" / "same_source_symmetry_breaking_source_certificate.json"
SM_ORIENTATION_DEDOTD = SM / "certificates" / "selected_orientation_carrying_de_dotd_source_certificate.json"
SM_SOURCE_ALPHA1 = SM / "certificates" / "selected_source_origin_and_alpha1_driver_certificate.json"
SM_PHIFIN_ALPHA1 = SM / "certificates" / "selected_phifin_alpha1_payload_certificate.json"
SM_PHIFIN_OR_BN = SM / "certificates" / "selected_phifin_payload_or_bn_basis_emission_certificate.json"
SM_DE_ON_BN = SM / "certificates" / "selected_routec_de_action_on_smooth_bn_certificate.json"

OUTPUT = CERTS / "cross_repo_update_chain_and_next_gate_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def git_lines(repo: Path, *args: str) -> list[str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return [line for line in proc.stdout.splitlines() if line.strip()]


def repo_state(repo: Path) -> dict[str, Any]:
    status = git_lines(repo, "status", "--short")
    head = git_lines(repo, "log", "--oneline", "-1")
    return {
        "path": str(repo),
        "head": head[0] if head else "NO_GIT_HEAD",
        "dirty": bool(status),
        "status_count": len(status),
        "status_sample": status[:12],
    }


def main() -> None:
    local_visible = load(LOCAL_VISIBLE_FUNCTIONAL)
    local_cw = load(LOCAL_CW_ATTEMPT)
    local_h1 = load(LOCAL_RANK2_H1)
    local_terminal = load(LOCAL_TERMINAL_SELECTOR)
    sm_visible_cw = load(SM_VISIBLE_CW)
    sm_same_source = load(SM_SAME_SOURCE_PACKET)
    sm_symmetry = load(SM_SYMMETRY_BREAKER)
    sm_orientation = load(SM_ORIENTATION_DEDOTD)
    sm_source_alpha1 = load(SM_SOURCE_ALPHA1)
    sm_phifin_alpha1 = load(SM_PHIFIN_ALPHA1)
    sm_phifin_or_bn = load(SM_PHIFIN_OR_BN)
    sm_de_on_bn = load(SM_DE_ON_BN)

    repos = {name: repo_state(path) for name, path in REPOS.items()}

    chain = [
        {"artifact": "SM selected visible Chern-Weil operator source", "status": sm_visible_cw["status"], "next": sm_visible_cw["primary_next_artifact"]},
        {"artifact": "SM non-split rank2 or Route-C same-source packet", "status": sm_same_source["status"], "next": sm_same_source["primary_next_artifact"]},
        {"artifact": "SM same-source symmetry-breaking source", "status": sm_symmetry["status"], "next": sm_symmetry["primary_next_artifact"]},
        {"artifact": "SM orientation-carrying D_E/dotD source", "status": sm_orientation["status"], "next": sm_orientation["primary_next_artifact"]},
        {"artifact": "SM selected source origin and alpha1 driver", "status": sm_source_alpha1["status"], "next": sm_source_alpha1["primary_next_artifact"]},
        {"artifact": "SM selected Phi_fin alpha1 payload", "status": sm_phifin_alpha1["status"], "next": sm_phifin_alpha1["primary_next_artifact"]},
        {"artifact": "SM Phi_fin payload or BN basis emission", "status": sm_phifin_or_bn["status"], "next": sm_phifin_or_bn["primary_next_artifact"]},
        {"artifact": "SM Route-C D_E action on smooth BN", "status": sm_de_on_bn["status"], "next": "source promotion, dotD, C1 response, replay without lifted flags"},
    ]

    same_source_reduction_imported = (
        sm_visible_cw["what_closes"]["single_same_source_packet_contract_locked"]
        and sm_same_source["what_closes"]["common_symmetry_breaking_source_blocker_identified"]
        and sm_symmetry["what_closes"]["orientation_carrying_de_dotd_selected_as_primary_route"]
        and sm_orientation["what_closes"]["validator_stack_first_blocker_identified"]
        and sm_source_alpha1["what_closes"]["source_and_alpha1_reduced_to_one_payload"]
        and sm_phifin_or_bn["what_closes"]["dependency_order_locked"]
        and sm_de_on_bn["what_closes"]["D_E_matrix_on_27_mode_BN_emitted"]
    )

    output = {
        "certificate": "CrossRepoUpdateChainAndNextGate",
        "status": "CROSS_REPO_UPDATES_IMPORTED_SOURCE_PROMOTION_AND_DOTD_C1_OPEN",
        "repo_states": repos,
        "external_update_caveat": {
            "sm_parity_closure_has_uncommitted_update_batch": repos["mtt_sm_parity_closure"]["dirty"],
            "q79_repo_has_uncommitted_cross_repo_clue_updates": repos["mtt_q79_proof_repro"]["dirty"],
            "import_status": "provisional cross-repo update import; external dirty artifacts are not immutable baselines",
        },
        "inputs": {
            "local_visible_functional": str(LOCAL_VISIBLE_FUNCTIONAL.relative_to(ROOT)),
            "local_cw_attempt": str(LOCAL_CW_ATTEMPT.relative_to(ROOT)),
            "local_rank2_h1": str(LOCAL_RANK2_H1.relative_to(ROOT)),
            "local_terminal_selector": str(LOCAL_TERMINAL_SELECTOR.relative_to(ROOT)),
            "sm_visible_cw": str(SM_VISIBLE_CW),
            "sm_same_source_packet": str(SM_SAME_SOURCE_PACKET),
            "sm_symmetry_breaker": str(SM_SYMMETRY_BREAKER),
            "sm_orientation_dedotd": str(SM_ORIENTATION_DEDOTD),
            "sm_source_alpha1": str(SM_SOURCE_ALPHA1),
            "sm_phifin_alpha1": str(SM_PHIFIN_ALPHA1),
            "sm_phifin_or_bn": str(SM_PHIFIN_OR_BN),
            "sm_de_on_bn": str(SM_DE_ON_BN),
        },
        "closed_now": {
            "all_five_repos_scanned": len(repos) == 5,
            "local_repo_state_captured_at_scan": True,
            "local_next_gate_was_cw_operator_source": local_visible["next_closing_object"]["name"]
            == "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1",
            "local_rank2_h1_fixture_available_but_unselected": local_h1["imported_h1_packet"]["h1"] == 8
            and local_h1["imported_h1_packet"]["source_selected_by_mtt"] is False,
            "local_terminal_lane_still_needs_base_order_breaking_source": local_terminal["not_closed"]["base_order_breaking_source"],
            "sm_parity_same_source_chain_imported_as_reduction": same_source_reduction_imported,
            "sm_parity_routec_de_matrix_on_bn_available_as_unpromoted_artifact": sm_de_on_bn["what_closes"]["D_E_matrix_on_27_mode_BN_emitted"],
        },
        "imported_chain": chain,
        "updated_local_frontier": {
            "old_frontier": local_cw["relation_to_common_payload"]["current_frontier"],
            "old_next_local_object": local_cw["next_object"]["name"],
            "new_frontier": "Selected_Source_Certificate_or_BN_Basis_PhiFin_Payload_Fill_v1",
            "reason": [
                "SM-parity update reduces visible CW source to same-source packet.",
                "Same-source packet reduces to orientation-carrying D_E/dotD.",
                "Orientation-carrying D_E/dotD reduces to source origin plus alpha1 driver.",
                "Source plus alpha1 reduces to selected Phi_fin payload or BN basis emission.",
                "A 27-mode BN D_E matrix exists externally, but source promotion, dotD, C1 response, and honest replay remain open.",
            ],
        },
        "not_closed": {
            "external_sm_parity_updates_committed": not repos["mtt_sm_parity_closure"]["dirty"],
            "source_promotion_without_lifted_flags": True,
            "same_branch_dotD_alpha1_in_same_basis": True,
            "selected_C1_response": True,
            "selected_PhiFin_payload_values": True,
            "selected_BN_basis_values": True,
            "branch_selection_or_antiunitary_retarded_selector": True,
            "full_SM_closure": True,
        },
        "next_closing_object": {
            "name": "Selected_Source_Certificate_or_BN_Basis_PhiFin_Payload_Fill_v1",
            "acceptance": [
                "import or construct selected source certificate without lifted flags",
                "bind selected source to either selected Phi_fin payload or selected BN basis emission contract",
                "promote the 27-mode BN D_E matrix only if the source certificate justifies it",
                "compute dotD alpha1 in the same basis and selected C1 response",
                "replay validators without observed flavor, CP sign, masses, or benchmark entries",
            ],
        },
        "guardrails": {
            "claims_external_dirty_artifacts_are_final": False,
            "claims_selected_source_promotion_now": False,
            "claims_dotD_C1_yukawa_closure": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "All five repos were scanned. The biggest relevant update is the SM-parity "
            "uncommitted chain: visible Chern-Weil source is reduced through same-source "
            "symmetry breaking to source/Phi_fin or BN-basis payload filling, with an "
            "unpromoted 27-mode BN D_E matrix available. The next local gate is source "
            "certificate or BN/Phi_fin payload fill, not manual promotion of selected flags."
        ),
    }

    if "--write-certificate" in __import__("sys").argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
