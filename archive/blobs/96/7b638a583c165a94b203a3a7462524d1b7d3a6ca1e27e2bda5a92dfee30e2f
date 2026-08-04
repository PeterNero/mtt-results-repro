"""Audit heterotic source-amendment/projective-rhoE representative tables."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_sourceamendment_or_projectiverhoe_representative_tables_certificate.json"
TEMPLATE = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smooth_promotion.template.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_SourceAmendment_or_ProjectiveRhoE_RepresentativeTables_v1.md"

STATUS = "HETEROTIC_SOURCEAMENDMENT_PROJECTIVERHOE_REPRESENTATIVE_TABLES_FINITE_CANDIDATE_PROMOTION_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_FiniteCandidate_PromotionOrSmoothRepresentative_v1"


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
    cert = load(CERT)
    template = load(TEMPLATE)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("primary projective", data["repair_comparison"]["selected_primary_lane"] == "projective_rhoE_finite_candidate_promotion_or_smooth_representative", data["repair_comparison"])
    check("finite candidate built", cert["finite_projective_candidate_built"] is True and data["decision"]["finite_projective_candidate_built"] is True, cert)

    tables = data["projective_representative_tables"]
    finite = tables["fills_finite_candidate_leaves"]
    check("tau and period emitted finitely", finite["period_denominator_or_smooth_unit"].startswith("primitive integer") and finite["central_cocycle_law_checked"] is True, finite)
    check("finite response carried", finite["D_E"].startswith("finite Galerkin") and finite["Riesz_projector"][2][2] == 1 and finite["finite_part"]["finite_trace_tau_squared"] == 8, finite)
    check("rhoE central character only", "exp(2*pi*i" in finite["rho_E_central_character"] and tables["does_not_fill_smooth_heterotic_leaves"]["rho_E_generator_or_boundary_matrices_as_transition_tables"] is None, tables)
    check("smooth leaves open", tables["does_not_fill_smooth_heterotic_leaves"]["selected_Deligne_Cech_or_B_field_representative"] is None and cert["smooth_heterotic_representative_emitted"] is False, tables["does_not_fill_smooth_heterotic_leaves"])
    check("typed lane not filled", data["typed_source_amendment_contract"]["can_be_shortcut_by_generic_constant_maps"] is False and cert["typed_source_amendment_filled"] is False, data["typed_source_amendment_contract"])
    check("template exact", set(template["must_supply"]) == {
        "smooth_or_finite_source_selection_theorem",
        "selected_Deligne_Cech_or_B_field_representative",
        "local_B_i",
        "overlap_A_ij",
        "triple_overlap_g_ijk",
        "map_to_tau_equals_finite_candidate",
        "rho_E_transition_or_boundary_matrices",
        "metric_or_unitarity_compatibility",
        "Freed_Witten_check",
        "Green_Schwarz_Bianchi_check",
        "projector_retention_check",
        "same_source_operator_identity_to_finite_response",
    }, template["must_supply"])
    check("no downstream closure", cert["EndE_to_BN_functor_filled"] is False and cert["E_Qa_computed"] is False and cert["threshold_value_computed"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()) and data["target_fitting_used"] is False, data["guardrails"])
    check("note records boundary", NEXT in note and "finite-candidate scope" in note, NOTE)

    print("\nSelected heterotic source-amendment/projective-rhoE representative tables audit")


if __name__ == "__main__":
    main()
