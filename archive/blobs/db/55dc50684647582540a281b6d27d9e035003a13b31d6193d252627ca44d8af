"""Audit the selected K_CKM kernel import and Pi trace functional cutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_kckmtraceassemblyrule_or_oneprincipleckmclosure"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
KERNEL_IMPORT = PACKET_DIR / "q79_selected_kckm_kernel_principle_import.packet.json"
SCOPE = PACKET_DIR / "kckm_trace_assembly_scope_separation.packet.json"
NEXT_GATE = PACKET_DIR / "pickm_closurecost_trace_functional_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_KCKMTraceAssemblyRule_or_OnePrincipleCKMClosure_v1.md"

STATUS = "MTT_SELECTED_KCKM_KERNEL_PRINCIPLE_IMPORTED_PI_TRACE_FUNCTIONAL_OPEN"
NEXT = "MTT_Selected_PiCKMClosureCostTraceFunctional_or_AngleWeightRows_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    kernel_import = load(KERNEL_IMPORT)
    scope = load(SCOPE)
    next_gate = load(NEXT_GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "cert next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["name"] == "KCKMKernelPrincipleScopeSeparationTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")

    require(kernel_import["status"] == "Q79_SELECTED_KCKM_KERNEL_PRINCIPLE_IMPORTED_FOR_CP_SCOPE", "kernel status")
    require(kernel_import["kernel_ownership_promoted"] is True, "kernel ownership")
    require(kernel_import["does_not_emit_angle_magnitude_trace_rows"] is True, "kernel overclaim")
    for marker in ["K_CKM^phys = K_sel", "E_CP", "J_sel(g)"]:
        require(marker in kernel_import["source_markers_verified"], f"missing marker {marker}")

    require(scope["closed_subclaim"]["selected_K_CKM_kernel_principle_available"] is True, "K subclaim")
    require(scope["not_closed_by_kernel_principle"]["selected_K_CKM_trace_assembly_rule_for_weights"] is False, "trace overclaim")
    require(scope["not_closed_by_kernel_principle"]["selected_Pi_CKM_12_row_certificate"] is False, "Pi12 overclaim")
    require(scope["not_closed_by_kernel_principle"]["selected_Pi_CKM_23_row_certificate"] is False, "Pi23 overclaim")
    require(scope["not_closed_by_kernel_principle"]["selected_Pi_CKM_13_row_certificate"] is False, "Pi13 overclaim")
    require(scope["accepted_weight_rows"] == 0, "scope weights")

    require(next_gate["status"] == "PICKM_CLOSURECOST_TRACE_FUNCTIONAL_REQUIRED", "gate status")
    require(next_gate["next_required_artifact"] == NEXT, "gate next")
    require("Pi_CKM^ij" in next_gate["remaining_object"], "remaining object")
    require(set(next_gate["must_emit"]) == {"Pi_CKM^12", "Pi_CKM^23", "Pi_CKM^13"}, "must emit")
    require("measured CKM angles as selectors" in next_gate["forbidden_inputs"], "forbidden selectors")

    closure = data["closure_decision"]
    require(closure["selected_K_CKM_kernel_principle_imported"] is True, "closure K import")
    require(closure["selected_K_CKM_trace_assembly_rule_for_weights_emitted"] is False, "closure trace overclaim")
    require(closure["selected_Pi_CKM_row_certificates"] == 0, "closure Pi certs")
    require(closure["accepted_weight_rows"] == 0, "closure weights")
    require(closure["accepted_exact_ckm_correction_rows"] == 0, "closure corrections")
    require(closure["accepted_no_knob_CKM_angle_rows"] == 0, "closure CKM rows")
    require(closure["true_SM_equivalence_closed"] is False, "true SM overclaim")
    require(closure["full_no_knob_closure_closed"] is False, "no-knob overclaim")

    nums = data["key_numbers"]
    require(nums["accepted_eckm_weight_rows"] == 0, "key accepted")
    require(nums["remaining_pi_row_certificates"] == 3, "key Pi certs")
    require(data["closure_claimed"] is False, "closure claimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector")
    require(data["target_fitting_used"] is False, "target fitting")
    require(cert["selected_K_CKM_kernel_principle_imported"] is True, "cert K import")
    require(cert["selected_K_CKM_trace_assembly_rule_for_weights_emitted"] is False, "cert trace overclaim")
    require(cert["selected_Pi_CKM_row_certificates"] == 0, "cert Pi certs")
    require(cert["closure_claimed"] is False, "cert closure")
    require("K_CKM CP-kernel ownership imported : true" in note, "note K import")
    require("accepted W rows                    : 0/3" in note, "note weights")
    require(NEXT in note, "note next")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
