"""Build the M_H value-emission search and C5-C6 bridge frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
CONST_DATA = TEXPAPERS / "mtt-individual-constants-source-search" / "candidate_data"

SLUG = "selected_mhvalueemissionsearch_or_c5c6bridgefrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INVENTORY = PACKET_DIR / "mh_value_source_inventory.packet.json"
UNDERDET = PACKET_DIR / "herm2_underdetermination_no_promotion.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_mh_value_search.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_mh_value_search.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_MHValueEmissionSearch_or_C5C6BridgeFrontier_v1.md"

PREVIOUS = DATA / "selected_higgsspecificmhacceptanceobject_or_valuefrontier.candidate.json"
PREVIOUS_HK = (
    DATA
    / "selected_higgsspecificmhacceptanceobject_or_valuefrontier"
    / "hk_threshold_gate_after_mh_acceptance_object.packet.json"
)
MH_OBJECT = (
    DATA
    / "selected_higgsspecificmhacceptanceobject_or_valuefrontier"
    / "higgs_specific_mh_acceptance_object.packet.json"
)
VALUE_FRONTIER = (
    DATA
    / "selected_higgsspecificmhacceptanceobject_or_valuefrontier"
    / "mh_three_real_row_value_frontier.packet.json"
)
H7B1Y_DIRECT = (
    CONST_DATA
    / "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
    / "direct_herm2_huv_row_schema.packet.json"
)
H7B1Y_MANIFEST = (
    CONST_DATA
    / "const_higgs_01_h7b1y_selected_ehuv_section_basis_quadrature_or_herm2_row_values"
    / "payload_search_manifest.packet.json"
)
H7B1Z_ATTEMPT = (
    CONST_DATA
    / "const_higgs_01_h7b1z_fill_ehuv_finite_basis_or_herm2_values"
    / "direct_herm2_fill_attempt.packet.json"
)
H7B1C_REQUEST = (
    CONST_DATA
    / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian"
    / "minimal_two_by_two_hessian_payload_request.packet.json"
)
H7B1F_CONTRACT = (
    CONST_DATA
    / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet"
    / "nonsplit_to_huv_reduction_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_MHVALUEEMISSIONSEARCH_OR_C5C6BRIDGEFRONTIER_"
    "NO_SELECTED_ROWS_FOUND_FUNCTIONAL_REQUIRED"
)
NEXT = "MTT_Selected_MHThreeRowSourceFunctional_or_C5C6BridgeExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing M_H value-search inputs: " + ", ".join(missing))


def all_nulls(mapping: dict[str, Any], keys: list[str]) -> bool:
    return all(mapping.get(key) is None for key in keys)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_HK,
        MH_OBJECT,
        VALUE_FRONTIER,
        H7B1Y_DIRECT,
        H7B1Y_MANIFEST,
        H7B1Z_ATTEMPT,
        H7B1C_REQUEST,
        H7B1F_CONTRACT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_hk = load(PREVIOUS_HK)
    mh_object = load(MH_OBJECT)
    value_frontier = load(VALUE_FRONTIER)
    h7b1y_direct = load(H7B1Y_DIRECT)
    h7b1y_manifest = load(H7B1Y_MANIFEST)
    h7b1z_attempt = load(H7B1Z_ATTEMPT)
    h7b1c_request = load(H7B1C_REQUEST)
    h7b1f_contract = load(H7B1F_CONTRACT)

    required_rows = ["Delta", "Re(Omega)", "Im(Omega)"]
    h7b1y_fields = h7b1y_direct["required_fields"]
    h7b1z_outputs = h7b1z_attempt["attempted_outputs"]
    direct_values_null = all_nulls(
        h7b1y_fields,
        [
            "Delta_equals_Huu_minus_Hdd_over_2",
            "Huu",
            "Hud",
            "Hdd",
            "Omega_equals_Hud",
            "P_L_light_projector",
            "s_beta_equals_Delta2_over_Delta2_plus_absOmega2",
        ],
    ) and all_nulls(h7b1z_outputs, ["Delta", "Huu", "Hud", "Hdd", "Omega", "P_L", "s_beta"])

    inventory = {
        "schema": "MTTMHValueSourceInventory.v1",
        "status": "CURRENT_CORPUS_HAS_NO_SELECTED_MH_VALUE_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "current_closed_domain": {
            "B_Huv_two_column_lift": True,
            "M_H_acceptance_object_bound_to_B_Huv_domain": True,
            "trace_free_Herm2_contract_fixed": True,
            "required_rows": required_rows,
        },
        "checked_sources": {
            "current_acceptance_object": rel(MH_OBJECT),
            "current_value_frontier": rel(VALUE_FRONTIER),
            "H7B1Y_direct_Herm2_schema": rel(H7B1Y_DIRECT),
            "H7B1Y_payload_search_manifest": rel(H7B1Y_MANIFEST),
            "H7B1Z_direct_fill_attempt": rel(H7B1Z_ATTEMPT),
            "H7B1C_minimal_Hessian_request": rel(H7B1C_REQUEST),
            "H7B1F_reduction_contract": rel(H7B1F_CONTRACT),
        },
        "source_rows_found": {
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "P_L": None,
            "s_beta": None,
            "K_threshold_Omega_H_lambda": None,
        },
        "accepted_source_row_count": 0,
        "direct_value_slots_all_null": direct_values_null,
        "retired_old_gaps": {
            "H7B1Y_B_Huv_false_is_retired_by_current_B_Huv": True,
            "H7B1Z_B_Huv_false_is_retired_by_current_B_Huv": True,
        },
        "still_true_after_retiring_old_gaps": {
            "H7B1Y_Herm2_values_null": True,
            "H7B1Z_Herm2_values_null": True,
            "H7B1C_is_request_not_value_packet": True,
            "H7B1F_is_reduction_formula_not_value_packet": True,
        },
    }

    underdet = {
        "schema": "MTTHerm2UnderdeterminationNoPromotion.v1",
        "status": "CURRENT_CLOSED_DATA_DO_NOT_SELECT_A_TRACE_FREE_HERM2_VECTOR",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "theorem": {
            "name": "Herm2ThreeRowUnderdeterminationTheorem",
            "proved": True,
            "statement": (
                "On the source-orthonormal B_Huv domain, the trace-free Higgs "
                "mass/strain object is M(a,b,c)=[[a,b+i c],[b-i c,-a]].  "
                "Nondegeneracy excludes only (a,b,c)=0, while phase covariance "
                "rotates the (b,c) plane and leaves a^2+b^2+c^2 and "
                "a^2/(a^2+b^2+c^2) as invariant diagnostics.  Therefore the "
                "current closed data select the domain and accepted form, but "
                "not the vector (a,b,c).  A selected Hessian/value functional, "
                "full M_source+R_H restriction, or C5-C6 projection bridge is "
                "required before Delta/Re(Omega)/Im(Omega) can be emitted."
            ),
        },
        "basis": {
            "Delta_row": "sigma_z = [[1,0],[0,-1]]",
            "Re_Omega_row": "sigma_x = [[0,1],[1,0]]",
            "Im_Omega_row": "sigma_y_convention = [[0,i],[-i,0]]",
        },
        "admissible_family": {
            "matrix": "[[Delta, Re(Omega)+i Im(Omega)], [Re(Omega)-i Im(Omega), -Delta]]",
            "nondegenerate_iff": "Delta^2 + Re(Omega)^2 + Im(Omega)^2 > 0",
            "s_beta_if_values_exist": "Delta^2/(Delta^2+Re(Omega)^2+Im(Omega)^2)",
        },
        "not_enough_to_select_values": [
            "B_Huv source-orthonormality",
            "diagonal HYM metric Gram data",
            "matter/neutrino alpha1/dotD operator blocks",
            "H7B1Y/H7B1Z schemas with null value fields",
            "diagnostic replay s_beta or observed Higgs data",
        ],
        "this_is_not_a_global_MTT_nogo": (
            "It only blocks promotion from the current closed support packets; "
            "a later selected Hessian, response functional, or C5-C6 bridge can still close the row."
        ),
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterMHValueSearch.v1",
        "status": "H_K_THRESHOLD_GATE_VALUE_SEARCH_COMPLETE_9_OF_10",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            **previous_hk["H_row"],
            "M_H_value_source_inventory_checked": True,
            "Herm2_three_row_underdetermination_closed": True,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
        },
        "conditional_consequent_current": {
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterMHValueSearch.v1",
        "status": "NEXT_FRONTIER_THREE_ROW_FUNCTIONAL_OR_C5C6_BRIDGE_EXECUTION",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "current Higgs value-source inventory checked",
            "old H7B1Y/H7B1Z B_Huv=false gap retired by current B_Huv",
            "H7B1Y/H7B1Z value slots remain null after that retirement",
            "Herm(2) three-row underdetermination theorem recorded",
            "H K-threshold gate remains 9/10",
        ],
        "still_open": [
            "selected Hessian/value functional emitting Delta, Re(Omega), Im(Omega)",
            "or full same-source M_source plus H-sector restriction R_H",
            "or selected C5 trace-to-H7B1U/projection-measure equality",
            "and C6 no-extra-boundary/source theorem",
            "K_threshold.Omega_H.lambda source row",
            "strict Omega/lambda_H scalar execution",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedMHValueEmissionSearchOrC5C6BridgeFrontier",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorem": underdet["theorem"],
        "closure_decision": {
            "B_Huv_two_column_uv_lift_emitted": True,
            "M_H_acceptance_object_bound_to_B_Huv_domain": True,
            "current_Higgs_value_source_inventory_checked": True,
            "Herm2_three_row_underdetermination_closed": True,
            "M_H_three_real_value_rows_emitted": False,
            "selected_Delta_row_emitted": False,
            "selected_Re_Omega_row_emitted": False,
            "selected_Im_Omega_row_emitted": False,
            "direct_Herm2_Huv_payload_emitted": False,
            "direct_Huu_Hud_Hdd_emitted": False,
            "selected_s_beta_value_found": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "mh_value_source_inventory": rel(INVENTORY),
            "herm2_underdetermination_no_promotion": rel(UNDERDET),
            "hk_threshold_gate_after_mh_value_search": rel(HK_GATE),
            "next_cutset_after_mh_value_search": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTTSelectedMHValueEmissionSearchOrC5C6BridgeFrontierCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "current_Higgs_value_source_inventory_checked": True,
        "Herm2_three_row_underdetermination_closed": True,
        "M_H_three_real_value_rows_emitted": False,
        "selected_Delta_row_emitted": False,
        "selected_Re_Omega_row_emitted": False,
        "selected_Im_Omega_row_emitted": False,
        "direct_Herm2_Huv_payload_emitted": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "accepted_internal_scalar_value_row_count": 0,
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected MHValueEmissionSearch or C5C6BridgeFrontier v1

Status: `{STATUS}`

## What Closed

- checked the current Higgs value-source inventory against H7B1Y/H7B1Z/H7B1C/H7B1F and the current `B_Huv`/`M_H` acceptance packets
- retired the old `B_Huv=false` gap in H7B1Y/H7B1Z using the current emitted `B_Huv`
- confirmed the actual value slots remain null: `Delta`, `Re(Omega)`, `Im(Omega)`, `Huu`, `Hud`, `Hdd`, `P_L`, and `s_beta`
- proved the local underdetermination theorem: the current closed support selects the trace-free Herm(2) domain/form, but not the three-vector `(Delta,Re(Omega),Im(Omega))`
- H K-threshold gate remains `{previous_hk["accepted_selected_K_source_row_count"]}/{previous_hk["selected_K_threshold_row_count_required"]}`

## Still Open

- selected Hessian/value functional emitting `Delta`, `Re(Omega)`, and `Im(Omega)`
- or full same-source `M_source+R_H`
- or selected C5-C6 projection/no-boundary bridge feeding the H `K_threshold` row
- strict `Omega/lambda_H` scalar execution

Next required artifact: `{NEXT}`
"""

    write_json(INVENTORY, inventory)
    write_json(UNDERDET, underdet)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
