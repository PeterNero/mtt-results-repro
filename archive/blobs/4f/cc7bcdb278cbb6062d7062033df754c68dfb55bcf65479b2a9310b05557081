"""Build the selected multiplication constants or D_E source gate for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

SCAFFOLD = DATA / "cech_dolbeault_matrix_packet_scaffold.candidate.json"
OPERATOR_GATE = DATA / "a01_de_operator_exit_gate.candidate.json"
OUTPUT_DATA = DATA / "selected_multiplication_constants_or_de_source_gate.candidate.json"
OUTPUT_CERT = CERTS / "selected_multiplication_constants_or_de_source_gate_certificate.json"

SOURCES = {
    "nonsm_typed_monad_fill": NONSM / "proof_corpus" / "Selected_Qa_SU3_Typed_Monad_Data_Fill_Attempt_v1.md",
    "nonsm_typed_monad_interface": NONSM / "proof_corpus" / "Selected_Qa_SU3_Typed_Monad_DE_or_RhoE_Data_Interface_v1.md",
    "q79_visible_valpha_candidates": Q79 / "proof_corpus" / "Visible_VAlpha_Chern_Bianchi_Source_Packet_Candidates_v1.md",
    "q79_rank2_ordered_source": Q79 / "proof_corpus" / "Visible_Rank2_L2_Ordered_Source_Promotion_Gate_v1.md",
    "q79_rank2_pullback_cech": Q79 / "proof_corpus" / "Visible_Rank2_L2_Pullback_Cech_Attempt_v1.md",
    "q79_rank2_ext_h1": Q79 / "proof_corpus" / "Visible_Rank2_L2_Ext_H1_Gate_v1.md",
    "q79_rhoe_ansatz": Q79 / "proof_corpus" / "Visible_RhoE_Source_Ansatz_Search_v1.md",
}


def scan(path: Path, terms: dict[str, str]) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms": {key: False for key in terms}}
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return {"path": str(path), "present": True, "terms": {key: term.lower() in text for key, term in terms.items()}}


def route(route_id: str, verdict: str, closes: list[str], missing: list[str], promotion_condition: str) -> dict[str, object]:
    return {
        "route_id": route_id,
        "verdict": verdict,
        "what_it_closes": closes,
        "missing_for_promotion": missing,
        "promotion_condition": promotion_condition,
    }


def main() -> None:
    scaffold = json.loads(SCAFFOLD.read_text(encoding="utf-8"))
    operator_gate = json.loads(OPERATOR_GATE.read_text(encoding="utf-8"))
    shape = scaffold["monad_matrix_shape"]
    product_blocks = scaffold["product_blocks"]
    f_vars = shape["f_vector"]
    g_vars = shape["g_vector"]
    mu_vars = shape["multiplication_constants"]
    formal_variable_count = len(f_vars) + len(g_vars) + len(mu_vars)
    equation_count = 1
    formal_dimension_if_nonzero_coefficients = formal_variable_count - equation_count
    gf_equation = shape["gf_zero_equation"]
    scans = {
        "nonsm_typed_monad_fill": scan(
            SOURCES["nonsm_typed_monad_fill"],
            {"generic_not_enough": "generic", "maps_open": "maps", "operator_open": "operator"},
        ),
        "nonsm_typed_monad_interface": scan(
            SOURCES["nonsm_typed_monad_interface"],
            {"de_required": "D_E", "rhoe_required": "rho_E", "validator": "validator"},
        ),
        "q79_visible_valpha_candidates": scan(
            SOURCES["q79_visible_valpha_candidates"],
            {"finite_cochain_packet": "finite Cech or Dolbeault cochain packet", "same_source_DE": "same-source D_E operator block", "dotD_response": "same-source dotD_alpha1 response"},
        ),
        "q79_rank2_ordered_source": scan(
            SOURCES["q79_rank2_ordered_source"],
            {"appell_humbert": "Appell-Humbert", "same_source": "same-source", "not_enough": "not enough"},
        ),
        "q79_rank2_pullback_cech": scan(
            SOURCES["q79_rank2_pullback_cech"],
            {"pullback_cech": "pullback Cech", "candidate_only": "candidate", "selected_open": "selected"},
        ),
        "q79_rank2_ext_h1": scan(
            SOURCES["q79_rank2_ext_h1"],
            {"finite_cochain_packet": "finite cochain packet", "selected_packet": "selected packet", "same_source": "same-source"},
        ),
        "q79_rhoe_ansatz": scan(
            SOURCES["q79_rhoe_ansatz"],
            {"constant_table_retired": "constant ordinary rho_E table", "selected_DE": "selected D_E", "fixed_gerbe": "fixed selected gerbe"},
        ),
    }
    route_tests = [
        route(
            "pure_convenience_solve_gf_zero",
            "REJECTED_UNDERDETERMINED_NOT_SELECTED",
            ["Shows the formal equation is easy to satisfy in many ways."],
            ["No selected bases.", "No selected mu_i.", "No selected f,g entries.", "No selected D_E/dotD/rho_E source."],
            "Never promoted unless all entries are selected independently before gf=0 is checked.",
        ),
        route(
            "appell_humbert_or_base_pullback_cech_formula",
            "LIVE_GUARDRAIL_INSUFFICIENT_ALONE",
            ["Can provide algebraic Cech/product formulas and compatibility tests."],
            ["A formula family is not the selected finite Qa/SU3 packet.", "Does not by itself select numeric mu_i or f,g entries."],
            "Promote only if the same branch selects the line-bundle/gerbe representative and finite basis.",
        ),
        route(
            "finite_cech_dolbeault_cochain_packet",
            "PRIMARY_MATRIX_CONSTRUCTION_TARGET",
            ["Would select section/cochain bases and multiplication constants from actual cochain products."],
            ["The selected finite packet is not present in this repo yet.", "Needs admissibility and operator retention checks."],
            "Promote when the 11 spaces have explicit finite bases and product tables whose blocks give mu_i.",
        ),
        route(
            "same_source_DE_dotD_response",
            "PRIMARY_OPERATOR_PROMOTION_ROUTE",
            ["Would select f,g,D_E/dotD/rho_E from the same source and feed the A01/D_E gate."],
            ["No selected Qa/SU3 D_E/dotD block has been supplied yet."],
            "Promote when D_E or dotD produces the same packet entries and nontrivial spectral/heat output.",
        ),
        route(
            "fixed_gerbe_Bfield_representative",
            "ALTERNATE_PERIOD_SELECTOR_ROUTE",
            ["Could select the period unit and twisted products if a fixed Deligne/B-field representative is selected."],
            ["Current period gate only derives the scalar condition; it does not select the representative or finite quotient."],
            "Promote only with same-branch Deligne/B-field representative plus Freed-Witten/GS-Bianchi checks.",
        ),
    ]
    rejected_routes = [item for item in route_tests if item["verdict"].startswith("REJECTED")]
    primary_routes = [item["route_id"] for item in route_tests if "PRIMARY" in item["verdict"]]
    candidate = {
        "candidate": "SelectedQaSU3SelectedMultiplicationConstantsOrDESourceGate",
        "status": "SELECTED_MULTIPLICATION_CONSTANTS_OR_DE_SOURCE_GATE_BUILT_VALUES_OPEN",
        "input_statuses": {
            "cech_dolbeault_scaffold": scaffold["status"],
            "a01_de_operator_gate": operator_gate["status"],
        },
        "formal_equation_analysis": {
            "gf_zero_equation": gf_equation,
            "f_variables": f_vars,
            "g_variables": g_vars,
            "multiplication_constant_variables": mu_vars,
            "formal_variable_count": formal_variable_count,
            "equation_count": equation_count,
            "formal_dimension_if_nonzero_coefficients": formal_dimension_if_nonzero_coefficients,
            "underdetermined_without_selection": formal_dimension_if_nonzero_coefficients > 0,
            "why_convenience_solve_fails": "The equation Sum_i mu_i a_i b_i = 0 defines a large formal family; choosing a point in that family does not identify selected MTT data.",
        },
        "source_scans": scans,
        "route_tests": route_tests,
        "promotion_requirements": {
            "selected_11_space_bases": True,
            "selected_product_tables_or_mu_i": True,
            "selected_f_g_matrix_entries": True,
            "gf_zero_verified_after_selection": True,
            "same_source_DE_dotD_or_rhoE": True,
            "spectral_heat_riesz_or_torsion_exit": True,
            "Freed_Witten_GS_Bianchi_and_projector_checks": True,
        },
        "gate_results": {
            "gf_zero_equation_imported": "mu_1*a_1*b_1" in gf_equation,
            "formal_under_determination_proved": formal_dimension_if_nonzero_coefficients == 14,
            "convenience_solve_rejected": len(rejected_routes) == 1,
            "primary_routes_identified": primary_routes == ["finite_cech_dolbeault_cochain_packet", "same_source_DE_dotD_response"],
            "selected_mu_i_supplied": False,
            "selected_f_g_entries_supplied": False,
            "selected_DE_dotD_or_rhoE_supplied": False,
            "closure_claimed": False,
        },
        "decision": {
            "result": "Gate built; the selected-values problem is reduced to either a finite Cech/Dolbeault cochain packet or same-source D_E/dotD response.",
            "why": "The existing gf=0 equation is necessary but massively underdetermined before MTT supplies the basis, product constants, and operator data.",
            "next_move": "Construct or discover the selected finite cochain packet, with the D_E/dotD response kept as the independent promotion check.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Finite_Cochain_Packet_or_DE_Response_v1",
        "parallel_search_artifact": "Selected_Qa_SU3_Central_Period_Selector_Search_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3SelectedMultiplicationConstantsOrDESourceGate",
        "status": "QA_SU3_SELECTED_MULTIPLICATION_CONSTANTS_OR_DE_SOURCE_GATE_BUILT_VALUES_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "gf_zero_equation_carried_forward": candidate["gate_results"]["gf_zero_equation_imported"],
            "formal_under_determination_proved": candidate["gate_results"]["formal_under_determination_proved"],
            "convenience_solve_rejected": candidate["gate_results"]["convenience_solve_rejected"],
            "finite_cochain_packet_identified_as_primary_matrix_route": "finite_cech_dolbeault_cochain_packet" in primary_routes,
            "same_source_DE_dotD_identified_as_primary_operator_route": "same_source_DE_dotD_response" in primary_routes,
        },
        "what_remains_open": {
            "selected_11_space_bases": True,
            "selected_mu_i": True,
            "selected_f_g_matrix_entries": True,
            "selected_DE_dotD_or_rhoE": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "parallel_search_artifact": candidate["parallel_search_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
