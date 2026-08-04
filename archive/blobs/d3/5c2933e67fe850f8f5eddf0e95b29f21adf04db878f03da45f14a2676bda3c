"""Audit the selected-cover homotopy or Deligne local-potential values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_selectedcoverhomotopy_or_deligne_localpotentialvalues.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_selectedcoverhomotopy_or_deligne_localpotentialvalues.candidate.json"
VALUES = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_invariant_B_potential_candidate.values.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_selectedcoverhomotopy_or_deligne_localpotentialvalues_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SelectedCoverHomotopy_or_DeligneLocalPotentialValues_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_INVARIANT_B_POTENTIAL_CANDIDATE_BUILT_TAU_DERIVATION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FlatTorsionGerbe_or_ProjectiveTransition_SourceValues_v1"


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
    values = load(VALUES)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and values["status"] == "INVARIANT_B_POTENTIAL_CANDIDATE_VALUES_BUILT_NOT_TAU_SOURCE", (data["status"], cert["status"], values["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("B candidate exact", decision["invariant_B_candidate_found"] is True and values["B_candidate_components"] == {"56": "6"}, values["B_candidate_components"])
    check("dB equals H", decision["dB_equals_H"] is True and values["dB_equals_H"] is True and values["dB_components"] == values["H_components"], values)
    check("nonzero tau obstruction", values["can_derive_nonzero_tau_from_B_only"] is False and len(values["nonzero_tau_labels_requiring_flat_torsion_or_projective_transition"]) == 8, values)
    check("triple class trivial", values["deligne_triple_class_from_B_only"] == 0 and decision["can_derive_nonzero_tau_from_B_only"] is False, values)
    check("flat torsion required", decision["flat_torsion_or_projective_transition_required"] is True and cert["flat_torsion_or_projective_transition_required"] is True, decision)
    check("cover still open", all(value is None for value in data["known_cover_status"].values()) and data["still_open"]["selected_smooth_good_cover"] is True, data["known_cover_status"])
    check("closed now exact", data["closed_now"]["invariant_primitive_candidate_for_H"] is True and data["closed_now"]["B_only_tau_obstruction_identified"] is True, data["closed_now"])
    check("does not close S1", decision["S1_closed"] is False and cert["S1_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no target fitting", data["target_fitting_used"] is False and values["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("note records B and next", "B = 6 e5 wedge e6" in note and NEXT in note and str(VALUES.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic projective rho_E selected-cover homotopy / Deligne local-potential values audit")


if __name__ == "__main__":
    main()
