"""Audit the local-field solve or cover-selection no-go packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_localfieldsolve_or_coverselection_nogo.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_localfieldsolve_or_coverselection_nogo.candidate.json"
CALC = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_localfieldsolve_dH_and_conditional_poincare.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_localfieldsolve_or_coverselection_nogo_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_LocalFieldSolve_or_CoverSelectionNoGo_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_LOCALFIELDSOLVE_DH_CLOSED_COVER_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SelectedCoverHomotopy_or_DeligneLocalPotentialValues_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    calc = load(CALC)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and calc["status"] == "DH_CLOSED_CONDITIONAL_LOCAL_POTENTIALS_VALUES_OPEN", (data["status"], cert["status"], calc["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("dH computed closed", decision["dH_computed"] is True and decision["dH_closed"] is True and calc["dH_closed"] is True and cert["dH_closed"] is True, calc)
    check("dH components empty", calc["dH_components"] == {}, calc["dH_components"])
    check("H and de components carried", len(calc["canonical_H_components"]) == 4 and len(calc["de_components"]["de5"]) == 2 and len(calc["de_components"]["de6"]) == 2, calc)
    check("conditional Poincare live", calc["conditional_poincare"]["local_B_i_exist_conditionally"] is True and calc["conditional_poincare"]["values_emitted"] is False, calc["conditional_poincare"])
    check("abstract shadow validator only", calc["algebraic_shadow_solve"]["abstract_scalar_transition_solution_exists"] is True and calc["algebraic_shadow_solve"]["promotable_to_smooth_source"] is False, calc["algebraic_shadow_solve"])
    check("closed now exact", data["closed_now"]["invariant_dH_zero_check"] is True and data["closed_now"]["conditional_poincare_local_potential_existence_theorem"] is True, data["closed_now"])
    check("still open exact", all(data["still_open"].values()) and "explicit_local_B_i_values" in data["still_open"], data["still_open"])
    check("no selected cover values", decision["selected_cover_emitted"] is False and decision["same_branch_local_values_found"] is False, decision)
    check("no smooth tau derived", decision["smooth_tau_shadow_derived"] is False and decision["local_B_i_A_ij_g_ijk_values_emitted"] is False, decision)
    check("does not close S1", decision["S1_closed"] is False and cert["S1_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no target fitting", data["target_fitting_used"] is False and calc["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("note records calculation", NEXT in note and str(CALC.relative_to(ROOT)) in note and "Poincare" in note, NOTE)

    print("\nSelected heterotic projective rho_E local-field solve / cover-selection no-go audit")


if __name__ == "__main__":
    main()
