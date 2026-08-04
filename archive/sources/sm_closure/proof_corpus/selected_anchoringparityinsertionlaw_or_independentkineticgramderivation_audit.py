from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_anchoringparityinsertionlaw_or_independentkineticgramderivation"
STATUS = "MTT_SELECTED_RELATIVE_SIGN_POSITIVE_QUOTIENT_REPRESENTATIVE_AND_DEFECT_HESSIAN_DERIVED_ACTION_OWNERSHIP_OPEN"
NEXT = "MTT_Selected_FullAnchorDefectHessianActionOwnershipAndSpectatorCancellation_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    quotient = load(ROOT / "candidate_data" / SLUG / "central_normalization_quotient_and_positive_representative.packet.json")
    defect = load(ROOT / "candidate_data" / SLUG / "full_anchor_projector_defect_hessian.packet.json")
    execution = load(ROOT / "candidate_data" / SLUG / "positive_representative_gauge_execution.packet.json")
    guardrails = load(ROOT / "candidate_data" / SLUG / "discarded_sign_mechanisms_and_scope_guard.packet.json")
    gate = load(ROOT / "candidate_data" / SLUG / "remaining_action_ownership_and_spectator_gate.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_AnchoringParityInsertionLaw_or_IndependentKineticGramDerivation_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(quotient["theorem"]["proved"], "quotient theorem")
    check(quotient["difference_is_delta_e_I"], "identity difference")
    check(quotient["positive_representative_psd"], "positive representative")
    check(defect["projector_distance_theorem"]["proved"], "defect theorem")
    check(defect["selected_application"]["H_anchor_psd"], "positive Hessian")
    check(not defect["scope_guard"]["physical_gauge_action_identified_with_D_anchor"], "action overclaim")
    check(execution["ratio_representative_residual"] < 1e-14, "ratio invariance")
    check(execution["residual_to_A78_dual_branch"] < 1e-14, "A78 replay")
    check(not guardrails["J_anchor_status"]["literal_indefinite_action_insertion_required"], "indefinite grading")
    check(not guardrails["quarter_character_square_route"]["promoted"], "i-square shortcut")
    check(not guardrails["analytic_torsion_parity_route"]["promoted"], "torsion shortcut")
    check(all(gate["closed"].values()), "closed gate")
    check(gate["relative_ratio_source_parameters"] == {"continuous": 0, "discrete_sign": 0}, "parameter count")
    check(not cert["physical_gauge_action_ownership_closed"], "ownership overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict values")
    for phrase in ["Central-normalization quotient theorem", "Positive full-anchor defect Hessian", "Corrected interpretation of A79", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("anchoring parity quotient/defect Hessian audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
