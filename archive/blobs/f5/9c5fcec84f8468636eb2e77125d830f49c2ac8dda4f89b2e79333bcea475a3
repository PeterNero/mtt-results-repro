"""Audit flat torsion gerbe / projective transition source-values gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_flattorsiongerbe_or_projectivetransition_sourcevalues.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_flattorsiongerbe_or_projectivetransition_sourcevalues.candidate.json"
VALUES = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_formal_flattorsion_projective_transition_values.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_flattorsiongerbe_promotion_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_flattorsiongerbe_or_projectivetransition_sourcevalues_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_FlatTorsionGerbe_or_ProjectiveTransition_SourceValues_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_FORMAL_FLATTORSION_PROJECTIVE_VALUES_BUILT_SOURCE_SELECTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FlatTorsionPromotion_or_SmoothTransitionTables_v1"


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
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and values["status"] == "FORMAL_VALUES_BUILT_NOT_SMOOTH_SOURCE", (data["status"], cert["status"], values["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and contract["next_required_artifact"] == NEXT, decision)
    check("formal values built", decision["formal_flat_torsion_values_built"] is True and cert["formal_flat_torsion_values_built"] is True, decision)
    check("curvature split", values["curvature_split"]["exact_invariant_B_candidate"] == {"56": "6"} and values["curvature_split"]["flat_torsion_layer_carries_nonzero_tau"] is True, values["curvature_split"])
    check("eleven labels", len(values["flat_projective_values"]) == 11 and set(values["flat_projective_values"]) == set(values["cover"][:0]) | set(values["flat_projective_values"]), values["flat_projective_values"].keys())
    check("triple tau checks", values["all_triples_match_tau"] is True and all(row["triple_matches_tau"] for row in values["flat_projective_values"].values()), values["flat_projective_values"])
    check("product cancellation", values["all_products_cancel_to_P"] is True and len(values["product_cancellation"]) == 5, values["product_cancellation"])
    check("not promotable", values["promotable_now"] is False and decision["promotable_now"] is False and cert["promotable_now"] is False, decision)
    check("same branch still open", values["same_branch_smooth_source_values_found"] is False and decision["same_branch_smooth_values_found"] is False, values)
    check("contract open leaves", all(value is None for value in contract["must_supply"].values()) and contract["formal_values_allowed_as"] == "validator and target shape only", contract)
    check("does not close S1", decision["S1_closed"] is False and cert["S1_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no target fitting", data["target_fitting_used"] is False and values["target_fitting_used"] is False and contract["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("note records values and contract", str(VALUES.relative_to(ROOT)) in note and str(CONTRACT.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E flat torsion gerbe / projective transition source-values audit")


if __name__ == "__main__":
    main()
