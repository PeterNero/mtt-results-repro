"""Build CONST-EW-02 B17 operator tables or physical matching frontier.

B17 imports the newest sibling-repo state for the weak-mixing source payload:

* finite internal rhoE/Phi_fin branch data are closed at internal scope;
* Route-C and projective rhoE operator tables are constructed, but conditional;
* gauge-kinetic/RG matching route is selected, but values remain open.

This narrows the remaining no-knob gate without promoting support tables,
conditional operators, or one-primitive matching to strict weak-angle closure.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b17_operator_tables_or_physical_matching"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PHIFIN = BASE / "finite_internal_phifin_source_lift_import.packet.json"
TABLES = BASE / "routec_projective_operator_tables_import.packet.json"
MATCHING = BASE / "physical_matching_lane_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b17_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B17_OperatorTablesOrPhysicalMatching_v1.md"

STATUS = "MTT_CONST_EW_02_B17_INTERNAL_PHIFIN_AND_CONDITIONAL_TABLES_IMPORTED_SELECTED_VALUES_OPEN"


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


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b16_path = DATA / "const_ew_02_weak_mixing_b16_source_operator_or_torsion_payload.candidate.json"
    b16_boundary_path = DATA / "const_ew_02_weak_mixing_b16_source_operator_or_torsion_payload" / "weak_mixing_b16_boundary.packet.json"

    phifin_note = QA / "proof_corpus" / "Selected_Heterotic_BundleConnection_ValueSolve_or_PhiFin_SourceIdentity_Proof_v1.md"
    phifin_cert_path = QA / "certificates" / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof_certificate.json"
    tables_note = QA / "proof_corpus" / "Selected_U1Y_RouteC_or_ProjectiveRhoE_Selected_Operator_Tables_v1.md"
    tables_cert_path = QA / "certificates" / "selected_u1y_routec_or_projective_rhoe_selected_operator_tables_certificate.json"
    stability_note = QA / "proof_corpus" / "Selected_U1Y_Stability_HYM_or_RouteC_Residual_Source_v1.md"
    matching_note = QA / "proof_corpus" / "Selected_Electroweak_GaugeKinetic_Normalization_and_RG_Scheme_SourceTheorem_v1.md"
    matching_cert_path = QA / "certificates" / "selected_electroweak_gaugekinetic_normalization_and_rg_scheme_certificate.json"
    physical_anchor_note = QA / "proof_corpus" / "Selected_Electroweak_PhysicalAnchor_RG_and_MatchingScale_v1.md"

    b16 = load(b16_path)
    b16_boundary = load(b16_boundary_path)
    phifin_cert = load(phifin_cert_path)
    tables_cert = load(tables_cert_path)
    matching_cert = load(matching_cert_path)

    phifin = {
        "schema": "MTTConstEW02B17FiniteInternalPhiFinSourceLiftImport.v1",
        "status": "FINITE_INTERNAL_PROJECTIVE_PACKET_IMPORTED_SMOOTH_SOURCE_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B17-HETEROTIC-BUNDLECONNECTION-OR-PHIFIN-IDENTITY",
        "inputs": {
            "B16_candidate": rel(b16_path),
            "B16_boundary": rel(b16_boundary_path),
            "phifin_note": rel(phifin_note),
            "phifin_certificate": rel(phifin_cert_path),
        },
        "imported_internal_closure": {
            "finite_internal_branch_closed": phifin_cert["finite_internal_branch_closed"],
            "finite_domain_rhoE_DE_Riesz_Green_trace_log2008_closed_internal": True,
        },
        "not_promoted": {
            "same_source_PhiFin_identity_proved": phifin_cert["same_source_PhiFin_identity_proved"],
            "explicit_bundle_connection_solved": phifin_cert["explicit_bundle_connection_solved"],
            "smooth_operator_identity_closed": phifin_cert["smooth_operator_identity_closed"],
            "E_Qa_computed": phifin_cert["E_Qa_computed"],
        },
        "meaning_for_weak_mixing": (
            "The internal finite operator packet is now available as internal source data. "
            "It still does not identify the heterotic/smooth electroweak threshold operator "
            "or emit physical matching data."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    tables = {
        "schema": "MTTConstEW02B17RouteCProjectiveOperatorTablesImport.v1",
        "status": "CONDITIONAL_TABLES_CONSTRUCTED_SELECTED_TABLES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B17-U1Y-ROUTEC-OR-PROJECTIVE-RHOE-OPERATOR-TABLES",
        "inputs": {
            "tables_note": rel(tables_note),
            "tables_certificate": rel(tables_cert_path),
            "stability_note": rel(stability_note),
        },
        "closed_support": tables_cert["closed"],
        "constructed_tables": {
            "routec_conditional_A_table_constructed": tables_cert["closed"]["routec_conditional_A_table_constructed"],
            "routec_rank_solve_exact": tables_cert["closed"]["routec_rank_solve_exact"],
            "projective_rhoE_mesh_validator_imported": tables_cert["closed"]["projective_rhoE_mesh_validator_imported"],
            "projective_DE_dotD_shape_support_imported": tables_cert["closed"]["projective_DE_dotD_shape_support_imported"],
        },
        "open_selected_fields": tables_cert["open"],
        "not_promoted": {
            "selected_operator_tables_emitted": False,
            "selected_A_selected_emitted": False,
            "selected_b_selected_emitted": False,
            "selected_projective_rhoE_tables_emitted": False,
            "selected_finite_part_found": False,
            "lambda_12_computable": False,
        },
        "next_required_object": tables_cert["next_required_object"],
        "parallel_projective_next_object": tables_cert["parallel_projective_next_object"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    matching = {
        "schema": "MTTConstEW02B17PhysicalMatchingLaneImport.v1",
        "status": "GAUGEKINETIC_RG_ROUTE_SELECTED_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B17-KGAUGE-MUMATCH-RG-SCHEME",
        "inputs": {
            "matching_note": rel(matching_note),
            "matching_certificate": rel(matching_cert_path),
            "physical_anchor_note": rel(physical_anchor_note),
        },
        "selected_route": {
            "strict_primary_route_selected": matching_cert["strict_primary_route_selected"],
            "meaning": "heterotic/Strominger threshold-kernel route is the strict no-knob primary path",
        },
        "closed_internal_values": {
            "internal_lambda_12_value": matching_cert["internal_lambda_12_value"],
            "internal_Delta_G12_value": matching_cert["internal_Delta_G12_value"],
        },
        "open_physical_matching": {
            "gaugekinetic_normalization_closed": matching_cert["gaugekinetic_normalization_closed"],
            "matching_scale_closed": matching_cert["matching_scale_closed"],
            "RG_scheme_closed": matching_cert["RG_scheme_closed"],
            "measured_electroweak_closure": matching_cert["measured_electroweak_closure"],
        },
        "one_primitive_lane": {
            "available_if_declared": True,
            "strict_no_knob": False,
            "guard": "A primitive universal normalization cannot be tuned to observed weak-angle or gauge data.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B17Boundary.v1",
        "status": "INTERNAL_AND_CONDITIONAL_SUPPORT_ADVANCED_SELECTED_PHYSICAL_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B17-BOUNDARY",
        "closed_now": {
            "finite_internal_projective_packet_for_internal_scope": phifin_cert["finite_internal_branch_closed"],
            "routec_conditional_operator_constructed": tables_cert["closed"]["routec_conditional_A_table_constructed"],
            "routec_rank_solve_exact": tables_cert["closed"]["routec_rank_solve_exact"],
            "projective_validator_table_constructed": tables_cert["closed"]["projective_rhoE_mesh_validator_imported"],
            "strict_primary_physical_route_selected": matching_cert["strict_primary_route_selected"] == "B_flux_strominger_threshold",
        },
        "still_open": {
            "same_source_PhiFin_identity": not phifin_cert["same_source_PhiFin_identity_proved"],
            "smooth_bundle_connection": not phifin_cert["explicit_bundle_connection_solved"],
            "selected_U1Y_operator_tables": tables_cert["open"]["selected_projective_rhoE_operator_tables"] or tables_cert["open"]["selected_visible_or_routec_operator_source"],
            "selected_DE_dotD_Riesz_Green_values": tables_cert["open"]["selected_DE_dotD_Riesz_Green_values"],
            "primitive_C1_contractions": tables_cert["open"]["primitive_C1_contractions"],
            "finite_part_or_spectrum": tables_cert["open"]["finite_part_or_spectrum"],
            "gaugekinetic_normalization": not matching_cert["gaugekinetic_normalization_closed"],
            "matching_scale": not matching_cert["matching_scale_closed"],
            "RG_scheme": not matching_cert["RG_scheme_closed"],
            "actual_xL_source_emission": True,
            "physical_weak_angle_closure": True,
        },
        "carried_from_B16": {
            "P_perp_projector_and_trace_policy": b16_boundary["closed_now"]["P_perp_projector_and_trace_policy"],
            "internal_Qa_stack_finitepart_policy": b16_boundary["closed_now"]["internal_Qa_stack_finitepart_policy"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B17NextWork.v1",
        "status": "NEXT_WORKORDER_SOURCE_LIFT_OR_SELECTED_VALUES",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B18-SOURCE-LIFT-OR-SELECTED-VALUES",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B18-FINITE-RHOE-TO-PHIFIN-OR-SMOOTH-BUNDLE-SOURCELIFT",
            "task": "Prove End(E)->B_N/Phi_fin same-source identity or lift the finite internal rhoE packet to a smooth selected heterotic bundle/operator connection.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B18-U1Y-STABILITY-OR-ROUTEC-RESIDUAL-VALUES",
            "task": "Promote reduced AH stability to selected good-cover/HYM source or emit selected Route-C residual values and D_E/dotD operator tables.",
        },
        "physical_matching_lane": {
            "label": "CONST-EW-02 / WEAK-MIXING / B18-HETEROTIC-STROMINGER-EW-KERNEL-VALUES",
            "task": "Emit gauge normalization, stack determinants, mu_match, and RG scheme from the selected heterotic/Strominger threshold kernel.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB17OperatorTablesOrPhysicalMatching",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B17-OPERATOR-TABLES-OR-PHYSICAL-MATCHING",
        "output_packets": {
            "finite_internal_phifin_source_lift_import": rel(PHIFIN),
            "routec_projective_operator_tables_import": rel(TABLES),
            "physical_matching_lane_import": rel(MATCHING),
            "weak_mixing_b17_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B17OperatorTablesOrPhysicalMatchingTheorem",
            "proved": True,
            "statement": (
                "The finite internal rhoE/Phi_fin packet is closed at internal scope, "
                "and the strongest Route-C/projective operator tables have been "
                "constructed as conditional/support objects. The strict physical route "
                "is selected as the heterotic/Strominger threshold kernel. None of "
                "these emits selected operator values, xL, or physical weak-angle "
                "closure yet."
            ),
        },
        "strict_xL_emitted_now": False,
        "selected_operator_values_emitted": False,
        "physical_matching_closed": False,
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B17_OperatorTablesOrPhysicalMatching_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "input_candidate": rel(b16_path),
        "finite_internal_branch_closed": phifin_cert["finite_internal_branch_closed"],
        "routec_conditional_operator_constructed": tables_cert["closed"]["routec_conditional_A_table_constructed"],
        "routec_rank_solve_exact": tables_cert["closed"]["routec_rank_solve_exact"],
        "projective_validator_table_constructed": tables_cert["closed"]["projective_rhoE_mesh_validator_imported"],
        "selected_operator_values_emitted": False,
        "physical_matching_closed": False,
        "strict_xL_emitted_now": False,
        "physical_weak_angle_closure": False,
        "strict_primary_route_selected": matching_cert["strict_primary_route_selected"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B17 Operator Tables Or Physical Matching v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B17-OPERATOR-TABLES-OR-PHYSICAL-MATCHING`

## Result

B17 imports three advances from the sibling Qa/SU3 frontier.

Closed or constructed support:

```text
finite internal rhoE/Phi_fin packet closed at internal scope = {phifin_cert["finite_internal_branch_closed"]}
Route-C conditional operator table constructed = {tables_cert["closed"]["routec_conditional_A_table_constructed"]}
Route-C rank solve exact = {tables_cert["closed"]["routec_rank_solve_exact"]}
projective rhoE validator table constructed = {tables_cert["closed"]["projective_rhoE_mesh_validator_imported"]}
strict physical route selected = {matching_cert["strict_primary_route_selected"]}
```

Still not closed:

```text
same-source Phi_fin identity
smooth bundle connection / E_Qa
selected U1Y operator values
selected D_E/dotD/Riesz/Green values
finite part or spectrum
K_gauge, mu_match, RG scheme
xL and physical weak angle
```

## Next

`CONST-EW-02 / WEAK-MIXING / B18-SOURCE-LIFT-OR-SELECTED-VALUES`
"""

    for path, payload in [
        (PHIFIN, phifin),
        (TABLES, tables),
        (MATCHING, matching),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
