"""Audit the chart-atlas / Deligne-Cech local-fields source-amendment packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_sourceamendment.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_sourceamendment.candidate.json"
EQUATIONS = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_equations.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_sourceamendment_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_ChartAtlas_DeligneCech_LocalFields_SourceAmendment_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_CHARTATLAS_DELIGNECECH_LOCALFIELDS_EQUATIONPACKET_BUILT_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_LocalFieldSolve_or_CoverSelectionNoGo_v1"


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
    equations = load(EQUATIONS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    known_geometry = equations["known_same_branch_geometry"]
    source_status = equations["source_status"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and equations["status"] == "EQUATION_PACKET_BUILT_VALUES_OPEN", (data["status"], cert["status"], equations["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("equation packet built", decision["equation_packet_built"] is True and cert["equation_packet_built"] is True, decision)
    check("geometry known but local B open", known_geometry["known_geometry_can_supply_curvature_H"] is True and known_geometry["known_geometry_can_supply_local_potentials_B_i"] is False and cert["known_geometry_can_supply_local_potentials_B_i"] is False, known_geometry)
    check("coframe and torsion carried", len(known_geometry["orthonormal_coframe"]) == 6 and len(known_geometry["torsion_H_or_d_c_omega_components"]) > 0, known_geometry)
    check("formal nerve carried", equations["finite_nerve_scaffold"]["nerve_is_two_simplex"] is True and len(equations["finite_nerve_scaffold"]["cover_nodes"]) == 3, equations["finite_nerve_scaffold"])
    check("symbolic local unknowns only", equations["local_field_unknowns"]["chart_atlas"]["realization_status"] == "SYMBOLIC_REQUIRED_NOT_EMITTED" and equations["local_field_unknowns"]["deligne_cech_fields"]["realization_status"] == "SYMBOLIC_REQUIRED_NOT_EMITTED", equations["local_field_unknowns"])
    check("eleven label transitions", len(equations["local_field_unknowns"]["label_transition_unknowns"]) == 11, equations["local_field_unknowns"]["label_transition_unknowns"])
    check("Deligne equations included", "B_j - B_i = d A_ij" in equations["required_equations"]["deligne_cech"] and "DD(T_c) = c * tau for c in {-1,0,+1}" in equations["required_equations"]["deligne_cech"], equations["required_equations"]["deligne_cech"])
    check("transition equations included", "projective_triple_overlap" in equations["required_equations"]["transition_shadow"] and "freed_witten_bianchi" in equations["required_equations"]["transition_shadow"], equations["required_equations"]["transition_shadow"])
    check("source values still open", source_status["same_branch_local_B_i_A_ij_g_ijk_values_found"] is False and source_status["selected_smooth_cover_values_found"] is False and source_status["selected_transition_matrices_found"] is False, source_status)
    check("closed support exact", all(data["closed_support"].values()), data["closed_support"])
    check("open leaves exact", all(data["open_leaves"].values()) and "local_B_i_two_forms" in data["open_leaves"], data["open_leaves"])
    check("does not close S1", decision["S1_closed"] is False and cert["S1_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no target fitting", data["target_fitting_used"] is False and equations["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("note records equation packet", NEXT in note and str(EQUATIONS.relative_to(ROOT)) in note and "not a substitute" in note, NOTE)

    print("\nSelected heterotic projective rho_E chart-atlas / Deligne-Cech local-fields source-amendment audit")


if __name__ == "__main__":
    main()
